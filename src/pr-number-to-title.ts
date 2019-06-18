import http from 'http'

import { FileBox } from 'file-box'

export async function prNumberToTitle (org: string, repo: string, pr: number): Promise<string> {
  const options: http.OutgoingHttpHeaders = {
    'User-Agent': 'FileBox',
  }

  const token = process.env['GITHUB_TOKEN']
  if (token) {
    options['Authorization'] = 'token ' + token
  }

  const fileBox = FileBox.fromUrl(
    // https://stackoverflow.com/a/34601082/1123955
    `https://api.github.com/repos/${org}/${repo}/pulls/${pr}`,
    'pr.json',
    options,
  )

  const buf        = await fileBox.toBuffer()
  const prJsonText = buf.toString()
  const prJson     = JSON.parse(prJsonText)
  const prTitle    = prJson.title as string

  return prTitle
}
