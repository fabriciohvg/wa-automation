#!/usr/bin/env python3
"""Convert WhiskeySockets/docs (Mintlify MDX) into a compact, LLM-oriented Markdown reference."""
import json, os, re, sys, shutil, textwrap

SRC, OUT = sys.argv[1], sys.argv[2]
META = json.load(open(os.path.join(SRC, 'scripts/api-reference-source.json')))
VERSION = META['version']
BANNER = f'> Baileys **v7** reference — package version `{VERSION}` (npm `latest`). Not valid for v6 or v8.\n'

GUIDES = [  # (group, page) in docs.json order; community/, index, migration/v8 and pt-BR intentionally dropped
    ('Get started', ['introduction', 'installation', 'quickstart', 'faq']),
    ('Authentication', ['authentication/qr-code', 'authentication/pairing-code', 'authentication/session-management']),
    ('Core concepts', ['concepts/socket-config', 'concepts/events', 'concepts/jids', 'concepts/data-store']),
    ('Messaging', ['messaging/sending-messages', 'messaging/media-messages', 'messaging/message-actions', 'messaging/chat-management']),
    ('Features', ['features/groups', 'features/privacy', 'features/presence', 'features/broadcasts-stories']),
    ('Advanced', ['advanced/history-sync', 'advanced/usync', 'advanced/calls', 'advanced/custom-functionality', 'advanced/troubleshooting']),
    ('Migration', ['migration/v7']),
]
API_KIND_DIR = {'functions': 'functions', 'type-aliases': 'types', 'interfaces': 'interfaces',
                'classes': 'classes', 'enumerations': 'enums', 'variables': 'variables'}
API_KIND_LABEL = {'functions': 'Function', 'types': 'Type alias', 'interfaces': 'Interface',
                  'classes': 'Class', 'enums': 'Enum', 'variables': 'Variable'}


def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    return meta, text


def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = re.sub(r'\n{3,}', '\n\n', content).strip() + '\n'
    open(path, 'w').write(content)


# ---------------------------------------------------------------- route mapping

def route_to_file(route):
    """Site route -> output path relative to OUT (or None if dropped)."""
    route, _, anchor = route.lstrip('/').partition('#')
    if route.startswith('api-reference/'):
        parts = route.split('/')
        if parts[1] == 'overview':
            return 'api/README.md', anchor
        return f'api/{API_KIND_DIR[parts[1]]}/{parts[2]}.md', anchor
    if route.startswith('proto-reference/'):
        parts = route.split('/')[1:]
        if parts == ['overview']:
            return 'proto/README.md', anchor
        if 'classes' in parts:  # classes are dropped; point at the interface
            i = parts.index('classes')
            parts = parts[:i] + ['interfaces', 'I' + parts[i + 1]]
        return 'proto/' + '/'.join(p for p in parts if p not in ('interfaces', 'enumerations')) + '.md', anchor
    pages = [p for _, ps in GUIDES for p in ps]
    if route in pages:
        return f'guides/{route}.md', anchor
    return None, anchor


def rewrite_links(text, cur_rel):
    def sub(m):
        label, route = m.group(1), m.group(2)
        target, anchor = route_to_file(route)
        if not target:
            return label
        rel = os.path.relpath(target, os.path.dirname(cur_rel))
        return f'[{label}]({rel}{"#" + anchor if anchor else ""})'
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', sub, text)


# ---------------------------------------------------------------- guides (hand-written MDX)

CALLOUTS = {'Note': 'Note', 'Tip': 'Tip', 'Warning': 'Warning', 'Info': 'Info', 'Check': 'Check'}
COMPONENTS = ['Steps', 'Step', 'CodeGroup', 'CardGroup', 'Card', 'AccordionGroup', 'Accordion',
              'Note', 'Tip', 'Warning', 'Info', 'Check', 'Tabs', 'Tab', 'Frame']


def attr(attrs, name):
    m = re.search(name + r'=(?:"([^"]*)"|\{([^}]*)\})', attrs)
    return (m.group(1) or m.group(2)) if m else None


def convert_components(text):
    pat = re.compile(r'^([ \t]*)<(' + '|'.join(COMPONENTS) + r')\b([^>]*?)(/?)>[ \t]*\n?((?:(?!<(?:' + '|'.join(COMPONENTS) + r')\b).)*?)^[ \t]*</\2>[ \t]*$',
                     re.S | re.M)
    step_counter = {}
    while True:
        # innermost first: body must not contain another opening tag of a known component
        found = False
        for m in pat.finditer(text):
            indent, tag, attrs, _, body = m.groups()
            if re.search(r'<(' + '|'.join(COMPONENTS) + r')\b', body):
                continue
            body = textwrap.dedent(body).strip('\n')
            if tag in ('CardGroup', 'Card', 'Frame'):
                out = ''
            elif tag in CALLOUTS and re.search(r'not affiliated|unofficial library', body):
                out = ''  # legal disclaimer, not reference material
            elif tag in CALLOUTS:
                out = '\n'.join('> ' + l if l else '>' for l in (f'**{CALLOUTS[tag]}:** ' + body).splitlines())
            elif tag == 'Step':
                out = f'**Step: {attr(attrs, "title")}**\n\n{body}'
            elif tag in ('Accordion', 'Tab'):
                out = f'**{attr(attrs, "title")}**\n\n{body}'
            else:  # Steps, CodeGroup, AccordionGroup, Tabs: unwrap
                out = body
            out = '\n'.join(indent + l if l else l for l in out.splitlines())
            text = text[:m.start()] + out + text[m.end():]
            found = True
            break
        if not found:
            return text


def number_steps(text):
    n = 0
    def sub(m):
        nonlocal n
        n += 1
        return f'**Step {n}: '
    out = []
    for block in re.split(r'(?=^## )', text, flags=re.M):
        n = 0
        out.append(re.sub(r'\*\*Step: ', sub, block))
    return ''.join(out)


def drop_sections(text, titles):
    for t in titles:
        text = re.sub(r'^## ' + t + r'\s*\n.*?(?=^## |\Z)', '', text, flags=re.S | re.M | re.I)
    return text


def convert_guide(page):
    meta, body = frontmatter(open(os.path.join(SRC, page + '.mdx')).read())
    rel = f'guides/{page}.md'
    body = convert_components(body)
    body = number_steps(body)
    body = drop_sections(body, ["What's next", 'Next steps', 'Related', 'See also', 'Disclaimer',
                                'What you can build', 'Is Baileys affiliated with WhatsApp\\?'])
    body = re.sub(r'https://baileys\.wiki/docs/api/([a-z-]+)/([A-Za-z0-9_]+)/?', r'/api-reference/\1/\2', body)
    body = re.sub(r'^---\s*$', '', body, flags=re.M)
    body = rewrite_links(body, rel)
    head = f'# {meta.get("title", page)}\n\n{BANNER}\n{meta.get("description", "")}\n\n'
    write(rel, head + body)
    return meta


# ---------------------------------------------------------------- TypeDoc compaction

def plain(s):
    """TypeDoc markdown type expression -> plain TypeScript text."""
    s = s.replace('\\[', '\x00').replace('\\]', '\x01')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = s.replace('\x00', '[').replace('\x01', ']')
    s = s.replace('`', '').replace('**', '')
    s = re.sub(r'\*(\w+)\*', r'\1', s)
    s = re.sub(r'\\(.)', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def prose(s):
    s = re.sub(r'\[`?([^\]`]*)`?\]\((?:/|\.)[^)]*\)', r'`\1`', s)  # internal links -> code names
    if not s.startswith('```'):
        s = re.sub(r'\\([{}\[\]_<>|*])', r'\1', s)
    return s


class Node:
    def __init__(self, level, title):
        self.level, self.title, self.blocks, self.children = level, title, [], []
        self.rel = None


def parse(body):
    root = Node(1, '')
    stack = [root]
    lines = body.splitlines()
    i, para = 0, []

    def flush():
        if para:
            text = '\n'.join(para)
            top, group = stack[-1], None
            for k in range(len(stack) - 1, -1, -1):
                if stack[k].title in ('Parameters', 'Returns'):
                    break
                if stack[k].title == 'Type declaration':
                    group = stack[k] if (top is stack[k] or top.blocks) else None
                    break
            if group and re.match(r'^(\\\{.*\\\}|\[`[^`]+`\]\([^)]*\)|`[^`]+`)$', text.strip()):
                v = Node(99, '\x02variant')
                v.blocks.append(text)
                group.children.append(v)
            else:
                stack[-1].blocks.append(text)
            para.clear()
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            flush()
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            stack[-1].blocks.append('\n'.join(lines[i:j + 1]))
            i = j + 1
            continue
        m = re.match(r'^(#{2,6}) (.*)$', line)
        if m:
            flush()
            n = Node(len(m.group(1)), m.group(2).strip())
            while stack[-1].level >= n.level:
                stack.pop()
            stack[-1].children.append(n)
            stack.append(n)
        elif line.strip() in ('', '***'):
            flush()
        else:
            para.append(line)
        i += 1
    flush()
    renest(root)
    return root


def member_name(title):
    return re.sub(r'\(\)$', '', plain(title)).rstrip('?')


def renest(node):
    """TypeDoc skips heading levels for dotted members (`#### chats.lock.id` under `## Type declaration`); nest by path."""
    kids, i = list(node.children), 0
    while i < len(kids):  # hoist dotted members wrongly nested under an unrelated sibling by heading level
        c = kids[i]
        cn = member_name(c.title)
        section = c.title in GROUPS or c.title in LABELED or c.title in SKIP or c.title in ('Parameters', 'Returns')
        hoist = [] if section else [k for k in c.children
                                    if '.' in member_name(k.title) and not member_name(k.title).startswith(cn + '.')]
        c.children = [k for k in c.children if k not in hoist]
        kids[i + 1:i + 1] = hoist
        i += 1
    node.children = kids
    new, seen = [], {}
    for c in node.children:
        renest(c)
        nm = member_name(c.title)
        parent, pre = None, nm
        while '.' in pre:
            pre = pre.rsplit('.', 1)[0]
            if pre in seen:
                parent = seen[pre]
                break
        if parent:
            c.rel = nm[len(pre) + 1:]
            parent.children.append(c)
        else:
            if '.' in nm:
                c.rel = nm
            new.append(c)
        seen[nm] = c
    node.children = new


SKIP = {'Implementation of', 'Inherited from', 'Overrides', 'Implements', 'Hierarchy', 'Extended by', 'Implemented by'}
GROUPS = {'Properties', 'Type declaration', 'Methods', 'Enumeration Members', 'Accessors', 'Constructors',
          'Index Signature', 'Indexable', 'Call Signature', 'Variables', 'Functions', 'Type Aliases', 'Interfaces',
          'Classes', 'Enumerations', 'Namespaces', 'Get Signature', 'Set Signature'}
LABELED = {'Example', 'Examples', 'Remarks', 'Deprecated', 'See', 'Throws', 'Default', 'Default Value', 'Since',
           'Extends', 'Type Parameters'}


class Ctx:
    def __init__(self, proto):
        self.proto = proto
        self.source = None


def is_sig(b):
    return b.startswith('> ')


def clean_type(t, ctx):
    if ctx.proto:
        t = re.sub(r'(^|: |\(|<)null \| ', r'\1', t)
    return t.replace('Uint8Array<ArrayBufferLike>', 'Uint8Array')


def split_blocks(node, ctx, top=False):
    sigs, desc = [], []
    for b in node.blocks:
        if b.startswith('Defined in:'):
            if top and not ctx.proto:
                m = re.search(r'\[([^\]]+)\]', b)
                ctx.source = m.group(1) if m else None
            continue
        if is_sig(b) and not b.startswith('> [!'):
            sigs.append(clean_type(plain(b[2:]), ctx))
        else:
            desc.append(prose(b))
    return sigs, desc


def child(node, title):
    return next((c for c in node.children if c.title == title), None)


def param_info(pnode, ctx):
    name = plain(pnode.title)
    blocks = list(pnode.blocks)
    typ = clean_type(plain(blocks.pop(0)), ctx) if blocks and not blocks[0].startswith('```') else ''
    rest = False
    if typ.startswith('...'):
        typ, rest = typ[3:], True
    typed = ('...' if rest else '') + name + (': ' + typ if typ else '')
    return name.rstrip('?'), typed, [prose(b) for b in blocks], pnode.children


def balanced_groups(s):
    out, depth, start = [], 0, None
    for i, ch in enumerate(s):
        if ch == '(':
            if depth == 0:
                start = i
            depth += 1
        elif ch == ')' and depth:
            depth -= 1
            if depth == 0:
                out.append((start, i))
    return out


def merge_params(sig, params):
    names = [p[0] for p in params]
    for a, b in balanced_groups(sig):
        inner = [x.strip().lstrip('.').rstrip('?') for x in sig[a + 1:b].split(',') if x.strip()]
        if inner == names:
            return sig[:a + 1] + ', '.join(p[1] for p in params) + sig[b:], True
    return sig, False


def fmt_sig(sig, title):
    # "optional foo: T" -> "foo?: T"; "readonly"/"static" kept as prefixes
    m = re.match(r'^((?:readonly |static |abstract )*)optional (\S+?)(\??):', sig)
    if m:
        sig = f'{m.group(1)}{m.group(2)}?:' + sig[m.end():]
    return sig


def returns_type(node, ctx):
    r = child(node, 'Returns')
    if r and r.blocks and not r.blocks[0].startswith('```'):
        return clean_type(plain(r.blocks[0]), ctx)
    return None


def render_desc(desc, ind):
    out = []
    for d in desc:
        for l in d.splitlines():
            out.append((ind + l) if l.strip() else '')
        out.append('')
    return out


def render_member(node, ctx, ind=''):
    if node.title == '\x02variant':
        return [f'{ind}- union member: `{plain(node.blocks[0])}`']
    overloads = [c for c in node.children if c.title == 'Call Signature']
    if overloads:
        out = []
        for c in overloads:
            n = Node(node.level, node.title)
            n.blocks, n.children, n.rel = node.blocks + c.blocks, c.children, node.rel
            out += render_member(n, ctx, ind)
        return out
    sigs, desc = split_blocks(node, ctx)
    pnode = child(node, 'Parameters')
    params = [param_info(c, ctx) for c in pnode.children] if pnode else []
    name = plain(node.title)
    if not sigs:
        if pnode or child(node, 'Returns'):
            bare = re.sub(r'\(\)$', '', name)
            ret = returns_type(node, ctx) or 'void'
            sigs = [f'{bare}(' + ', '.join(p[1] for p in params) + f') => {ret}']
            merged_all = True
        else:
            sigs = [name]
            merged_all = True
    else:
        merged_all = True
        new = []
        for s in sigs:
            if params:
                s, ok = merge_params(s, params)
                merged_all &= ok
            new.append(fmt_sig(s, name))
        sigs = new
    if node.rel:
        last = node.rel.rsplit('.', 1)[-1]
        sigs = [re.sub(r'^((?:readonly |static |abstract )*)' + re.escape(last) + r'(?=[?:(<])',
                       lambda m: m.group(1) + node.rel, x, count=1) for x in sigs]
    out = []
    head = f'{ind}- `' + '` / `'.join(sigs) + '`'
    if len(desc) == 1 and '\n' not in desc[0] and not desc[0].startswith(('```', '>', '|', '-')):
        head += ' — ' + desc[0]
        desc = []
    out.append(head)
    sub = ind + '  '
    if desc:
        out.append('')
        out += render_desc(desc, sub)
    for p in params:
        pname, typed, pdesc, pkids = p
        if pdesc or pkids or not merged_all:
            line = f'{sub}- param `{typed}`' + (' — ' + pdesc[0] if len(pdesc) == 1 and '\n' not in pdesc[0] else '')
            out.append(line)
            if len(pdesc) > 1 or (pdesc and '\n' in pdesc[0]):
                out += render_desc(pdesc, sub + '  ')
            for k in pkids:
                out += render_member(k, ctx, sub + '  ')
    out += render_children(node, ctx, sub, skip={'Parameters'})
    return out


def render_children(node, ctx, ind, skip=(), top=False):
    out = []
    for c in node.children:
        t = c.title
        if t in skip or t in SKIP:
            continue
        if t == 'Returns':
            sigs, desc = split_blocks(c, ctx)
            rdesc = desc[1:] if desc and not desc[0].startswith('```') else desc
            if top and c.children:
                out += ['', '## Returns', '']
                if rdesc:
                    out += render_desc(rdesc, '')
                for k in c.children:
                    out += render_member(k, ctx, '') if k.title not in GROUPS else render_group(k, ctx, '')
                continue
            if rdesc or c.children:
                out.append(f'{ind}- returns' + (' — ' + rdesc[0] if len(rdesc) == 1 and '\n' not in rdesc[0] else ':'))
                if len(rdesc) > 1:
                    out += render_desc(rdesc, ind + '  ')
                for k in c.children:
                    out += render_member(k, ctx, ind + '  ')
        elif t == 'Type Parameters':
            tps = []
            for k in c.children:
                extra = [plain(b) for b in k.blocks]
                tps.append(plain(k.title) + (' ' + ' '.join(extra) if extra else ''))
            for b in c.blocks:
                tps.append(plain(b).lstrip('• '))
            if tps:
                out.append(('' if top else ind + '- ') + 'Type params: `' + ', '.join(tps) + '`')
                if top:
                    out.append('')
        elif t in GROUPS:
            out += render_group(c, ctx, '' if top else ind, top)
        elif t in LABELED:
            sigs, desc = split_blocks(c, ctx)
            body = desc + [f'`{s}`' for s in sigs]
            for k in c.children:
                body.append(plain(k.title) + ' ' + ' '.join(plain(b) for b in k.blocks))
            if top:
                out += ['', f'## {t}', ''] + render_desc(body, '')
            else:
                out.append(f'{ind}- {t}:')
                out += render_desc(body, ind + '  ')
        else:
            out += render_member(c, ctx, '' if top else ind)
    return out


def render_group(c, ctx, ind, top=False):
    out = []
    sigs, desc = split_blocks(c, ctx)
    if c.title in ('Index Signature', 'Indexable'):
        sigs += [plain(d) for d in desc if not d.startswith('```')]
        desc = [d for d in desc if d.startswith('```')]
    if top:
        out += ['', f'## {c.title}', '']
        if sigs:
            out.append('`' + '` / `'.join(sigs) + '`')
            out.append('')
        out += render_desc(desc, '')
        for k in c.children:
            out += render_member(k, ctx, '') if k.title not in GROUPS else render_group(k, ctx, '')
    else:
        label = f'{ind}- {c.title}' + (': `' + '` / `'.join(sigs) + '`' if sigs else ':')
        out.append(label)
        out += render_desc(desc, ind + '  ')
        for k in c.children:
            out += render_member(k, ctx, ind + '  ') if k.title not in GROUPS else render_group(k, ctx, ind + '  ')
    return out


def convert_typedoc(src_path, rel, title, kind_label, proto):
    meta, body = frontmatter(open(src_path).read())
    ctx = Ctx(proto)
    root = parse(body)
    sigs, desc = split_blocks(root, ctx, top=True)
    pnode = child(root, 'Parameters')
    params = [param_info(c, ctx) for c in pnode.children] if pnode else []
    merged_all = True
    new = []
    for s in sigs:
        if params:
            s, ok = merge_params(s, params)
            merged_all &= ok
        new.append(s)
    sigs = new
    if kind_label == 'Type alias':
        sigs = ['type ' + re.sub(r'^(\w+(?:<[^>]*>)?): ', r'\1 = ', s, count=1) for s in sigs]
    elif kind_label == 'Function':
        sigs = ['function ' + s for s in sigs]
    rtype = returns_type(root, ctx)
    if kind_label == 'Function' and not sigs and (pnode or rtype):
        sigs = [f'function {title}(' + ', '.join(p[1] for p in params) + f'): {rtype or "void"}']
    d = meta.get('description', '')
    flat = ' '.join(' '.join(desc).split())
    if re.search(r'in the Baileys API\.$|generated from WAProto\.$', d) or (d and d.rstrip('.') in flat):
        d = ''
    out = [f'# {title}', '', BANNER.rstrip(), '']
    info = f'{kind_label}' + (f' · source `{ctx.source}`' if ctx.source else '')
    if kind_label == 'Protobuf interface':
        info += ' · all fields optional and nullable (`null` omitted below)'
    out += [info, '']
    for s in sigs:
        out += ['```ts', s, '```', '']
    if d:
        out += [d, '']
    out += render_desc(desc, '')
    if params and (not merged_all or any(p[2] or p[3] for p in params)):
        out += ['## Parameters', '']
        for pname, typed, pdesc, pkids in params:
            out.append(f'- `{typed}`' + (' — ' + pdesc[0] if len(pdesc) == 1 and '\n' not in pdesc[0] else ''))
            if len(pdesc) > 1:
                out += render_desc(pdesc, '  ')
            for k in pkids:
                out += render_member(k, ctx, '  ')
    out += render_children(root, ctx, '', skip={'Parameters'}, top=True)
    text = '\n'.join(out)
    write(rel, text)
    first = next((x for x in desc if not x.startswith(('```', '>'))), d)
    summary = re.split(r'(?<=[.!?])\s', ' '.join(first.split()))[0] if first else ''
    return sigs[0] if sigs else '', summary


# ---------------------------------------------------------------- main

def main():
    if os.path.exists(OUT):
        for e in ('README.md', 'guides', 'api', 'proto', 'llms.txt'):
            p = os.path.join(OUT, e)
            if os.path.isdir(p):
                shutil.rmtree(p)
            elif os.path.exists(p):
                os.remove(p)
    guide_meta = {}
    for _, pages in GUIDES:
        for p in pages:
            guide_meta[p] = convert_guide(p)

    api_index = {}
    for srcdir, outdir in API_KIND_DIR.items():
        d = os.path.join(SRC, 'api-reference', srcdir)
        for f in sorted(os.listdir(d)):
            name = f[:-4]
            rel = f'api/{outdir}/{name}.md'
            sig, summ = convert_typedoc(os.path.join(d, f), rel, name, API_KIND_LABEL[outdir], False)
            api_index.setdefault(outdir, []).append((name, rel, sig, summ))

    proto_index = []
    base = os.path.join(SRC, 'proto-reference')
    for dirpath, dirs, files in os.walk(base):
        dirs.sort()
        kind = os.path.basename(dirpath)
        if kind not in ('interfaces', 'enumerations'):
            continue
        ns = os.path.relpath(os.path.dirname(dirpath), base)
        ns = '' if ns == '.' else ns
        for f in sorted(files):
            name = f[:-4]
            rel = 'proto/' + (ns + '/' if ns else '') + name + '.md'
            full = 'proto.' + (ns.replace('/', '.') + '.' if ns else '') + name
            label = 'Protobuf interface' if kind == 'interfaces' else 'Protobuf enum'
            convert_typedoc(os.path.join(dirpath, f), rel, full, label, True)
            proto_index.append((full, rel, kind))

    write_indexes(guide_meta, api_index, proto_index)


def write_indexes(guide_meta, api_index, proto_index):
    # api/README.md
    lines = ['# Baileys API reference index', '', BANNER, '',
             f'Generated (TypeDoc) from Baileys `master` commit `{META["commit"][:12]}` = version `{VERSION}`.',
             'One file per exported symbol: `api/<kind>/<Name>.md`. Signatures are inlined; type names are plain',
             'text — find a referenced type with a glob like `api/**/<Name>.md` or `proto/**/<Name>.md`.',
             'Unexported helper types (e.g. `Mentionable`, `Contextable`, `WithDimensions`) have no page.', '',
             '**Start here:** [`makeWASocket`](functions/makeWASocket.md) — its return value is the socket; every',
             '`sock.*` method (sendMessage, groupCreate, …) is listed there with its signature.',
             'Also: [`SocketConfig`](types/SocketConfig.md), [`BaileysEventMap`](types/BaileysEventMap.md) (all `sock.ev` events),',
             '[`AnyMessageContent`](types/AnyMessageContent.md) (sendMessage payloads), [`DisconnectReason`](enums/DisconnectReason.md).', '']
    order = ['functions', 'types', 'interfaces', 'classes', 'enums', 'variables']
    titles = {'functions': 'Functions', 'types': 'Type aliases', 'interfaces': 'Interfaces', 'classes': 'Classes',
              'enums': 'Enums', 'variables': 'Variables'}
    for k in order:
        lines += [f'## {titles[k]}', '']
        for name, rel, sig, summ in api_index[k]:
            r = os.path.relpath(rel, 'api')
            if k == 'functions' and sig and len(sig) < 220:
                lines.append(f'- [{name}]({r}) `{sig[len("function "):]}`' + (f' — {summ}' if summ else ''))
            else:
                lines.append(f'- [{name}]({r})' + (f' — {summ}' if summ else ''))
        lines.append('')
    write('api/README.md', '\n'.join(lines))

    # proto/README.md
    lines = ['# Baileys protobuf (`proto` namespace) index', '', BANNER, '',
             "WhatsApp wire-format types generated from `WAProto.proto`, exported as `proto` (`import { proto } from 'baileys'`).",
             'Only the plain-object `I*` interfaces and enums are kept (the generated classes duplicate the interfaces and only add',
             '`create/encode/decode/fromObject/toObject/verify`). All fields are optional and nullable.',
             'Nested types live in folders: `proto.Message.IImageMessage` -> `proto/Message/IImageMessage.md`.',
             'You rarely need these: most Baileys APIs take plain objects (see `api/types/AnyMessageContent.md`).',
             'Key ones: `proto.IMessage` (message content union), `proto.IWebMessageInfo` (= `WAMessage` base), `proto.IMessageKey`.', '']
    for k, title in (('interfaces', 'Interfaces'), ('enumerations', 'Enums')):
        lines += [f'## {title}', '']
        for full, rel, kind in sorted(proto_index):
            if kind == k:
                lines.append(f'- [{full}]({os.path.relpath(rel, "proto")})')
        lines.append('')
    write('proto/README.md', '\n'.join(lines))

    # root README
    lines = [f'# Baileys v7 docs for LLM agents', '', BANNER, '',
             '## Version this documents', '',
             f'- Library: **Baileys** (WhiskeySockets), WhatsApp Web API over WebSocket, TypeScript/Node.js.',
             f'- Version: **`{VERSION}`**, the npm `latest` dist-tag (published 2026-07-29). v7 is still in RC; `6.7.x` is the `legacy` tag.',
             f'- API reference generated from Baileys `master` @ `{META["commit"][:12]}` (package.json version `{VERSION}`).',
             '- Install: `npm i baileys` (canonical) — `@whiskeysockets/baileys` is published at the same version. The guides import from',
             "  `'@whiskeysockets/baileys'`; use whichever name you installed. The package is **ESM-only** (`\"type\": \"module\"`), Node.js **>= 20**.",
             '- If a project pins `6.x`, these docs may not match: read [guides/migration/v7.md](guides/migration/v7.md) for the breaking changes',
             '  (LIDs, ESM, removed APIs). v8 is unreleased and not covered.',
             '- Source: https://github.com/WhiskeySockets/docs (English only; pt-BR, community pages, site config and the v8 preview dropped).', '',
             '## How to use this directory', '',
             '1. Task-oriented questions ("how do I send an image / reconnect / use pairing code") -> `guides/`.',
             '2. Exact signatures/fields -> `api/README.md` (index with inlined function signatures), then `api/<kind>/<Name>.md`.',
             '3. Socket methods (`sock.sendMessage`, `sock.groupMetadata`, ...) -> `api/functions/makeWASocket.md`.',
             '4. Raw protobuf shapes (`proto.IMessage`, `proto.Message.IImageMessage`, ...) -> `proto/README.md`.',
             '5. Find any symbol by file name: `**/<Name>.md`, or grep the tree.', '',
             '## Guides', '']
    for group, pages in GUIDES:
        lines.append(f'### {group}')
        lines.append('')
        for p in pages:
            m = guide_meta[p]
            lines.append(f'- [{m.get("title", p)}](guides/{p}.md) — {m.get("description", "")}')
        lines.append('')
    lines += ['## Reference', '',
              f'- [API index](api/README.md) — {sum(len(v) for v in api_index.values())} exported symbols (functions, types, interfaces, classes, enums, variables).',
              f'- [Protobuf index](proto/README.md) — {len(proto_index)} `proto.*` interfaces and enums.', '']
    write('README.md', '\n'.join(lines))


main()
