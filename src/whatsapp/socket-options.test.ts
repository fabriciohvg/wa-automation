import assert from 'node:assert/strict'
import { test } from 'node:test'
import { socketOptions } from './socket-options.js'

test('socketOptions uses the macOS desktop preset with full history', () => {
  const [platform, browser] = socketOptions.browser

  assert.equal(platform, 'Mac OS')
  assert.equal(browser, 'Desktop')
  assert.equal(socketOptions.syncFullHistory, true)
})
