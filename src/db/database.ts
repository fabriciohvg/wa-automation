import { mkdirSync } from 'node:fs'
import { dirname } from 'node:path'
import Database from 'better-sqlite3'

export function openDatabase(path: string): Database.Database {
  mkdirSync(dirname(path), { recursive: true })

  const db = new Database(path)
  // WAL permite ler enquanto o sync grava e deixa as escritas em lote mais rápidas.
  db.pragma('journal_mode = WAL')
  // Com WAL, NORMAL não corrompe o banco em caso de queda e evita um fsync por transação.
  db.pragma('synchronous = NORMAL')
  // O SQLite vem com as chaves estrangeiras desligadas em cada conexão.
  db.pragma('foreign_keys = ON')

  return db
}
