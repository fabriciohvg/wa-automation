import { Browsers, type UserFacingSocketConfig } from 'baileys'

// O preset desktop é o que libera o histórico estendido no sync inicial.
export const socketOptions = {
  browser: Browsers.macOS('Desktop'),
  syncFullHistory: true,
} satisfies Partial<UserFacingSocketConfig>
