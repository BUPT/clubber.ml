#!/usr/bin/env ts-node

import test  from 'tstest'

import { prNumberToTitle } from './pr-number-to-title'

test('pr number to title', async t => {
  const ORG = 'bupt'
  const REPO = 'ai-ml.club'
  const PR = 141
  const EXPECTED_TITLE = 'fix S2E13'

  for (let n = 0; n < 100; n++) {
    const title = await prNumberToTitle(ORG, REPO, PR)
    t.equal(title, EXPECTED_TITLE, 'should get the right pr title #' + n)
  }
})
