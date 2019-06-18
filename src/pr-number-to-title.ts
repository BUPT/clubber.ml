import { FileBox } from 'file-box'

export async function prNumberToTitle (org: string, repo: string, pr: number): Promise<string> {
  const fileBox = FileBox.fromUrl(
    // https://stackoverflow.com/a/34601082/1123955
    `https://api.github.com/repos/${org}/${repo}/pulls/${pr}`,
    'pr.json',
    {
      'User-Agent': 'FileBox',
    }
  )
  const prJsonText = (await fileBox.toBuffer()).toString()
  // console.log(prJsonText)
  const prJson = JSON.parse(prJsonText)
  const prTitle = prJson.title as string
  return prTitle
}
