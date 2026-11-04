import { join } from 'node:path'
import { fileURLToPath } from 'node:url'

// Resolve a partir deste arquivo para funcionar tanto em src/ quanto em dist/.
const dataDir = fileURLToPath(new URL('../data/', import.meta.url))

export const config = {
  databasePath: join(dataDir, 'wa.db'),
  authDir: join(dataDir, 'auth'),
  logLevel: process.env.LOG_LEVEL ?? 'info',
}
