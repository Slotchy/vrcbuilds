# VRChat Stable Build Archive

Static GitHub Pages website, plus a GitHub Actions job that fetches VRChat's **PC** minimum build from `https://vrchat.com/api/1/config` every hour and saves it to `minimum-build.json`.

## Setup
1. Upload all files, including `.github/workflows/update-minimum.yml`, to the repository default branch.
2. In **Settings → Pages**, select **Deploy from a branch**, your default branch, and **/(root)**.
3. In **Actions**, enable workflows if prompted and manually run **Update VRChat minimum build** once.
4. In **Settings → Actions → General → Workflow permissions**, allow **Read and write permissions** if the update cannot push commits. Some organizations restrict this setting.

The site reads `minimum-build.json` when opened or when the Refresh status button is clicked. GitHub Actions runs hourly (scheduled jobs may be delayed). If the API fails, the action fails without overwriting the previous successful data. The site labels old data as possibly outdated. The initial JSON is a manually recorded fallback, not live verified.

The build-to-manifest list remains manually maintained; the API only updates the minimum supported PC build number. A higher minimum does not automatically add a missing manifest.
