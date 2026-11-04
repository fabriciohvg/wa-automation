import assert from 'node:assert/strict'
import { mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { test } from 'node:test'
import { openDatabase } from './database.js'

test('openDatabase creates missing directories and applies pragmas', (t) => {
  const dir = mkdtempSync(join(tmpdir(), 'wa-automation-'))
  t.after(() => rmSync(dir, { recursive: true, force: true }))

  const db = openDatabase(join(dir, 'nested', 'test.db'))
  t.after(() => db.close())

  assert.equal(db.pragma('journal_mode', { simple: true }), 'wal')
  assert.equal(db.pragma('synchronous', { simple: true }), 1)
  assert.equal(db.pragma('foreign_keys', { simple: true }), 1)
})
