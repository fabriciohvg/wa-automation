import { config } from './config.js'
import { openDatabase } from './db/database.js'
import { logger } from './logger.js'

const db = openDatabase(config.databasePath)
logger.info({ path: config.databasePath }, 'database ready')
db.close()
