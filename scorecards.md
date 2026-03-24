# OpenSSF Scorecards

## What is OpenSSF

The Open Source Security Foundation ([OpenSSF](https://github.com/ossf)) is a cross-industry forum launched in 2020 by the Linux Foundation to enhance open-source software security. OpenSSF provides technical and educational initiatives, including a security baseline, automation tools for SBOMs, and a professional certificate program. It also manages projects like Alpha-Omega and [OpenSSF Scorecard](https://scorecard.dev/) to mitigate risks. 

More detailed information about Scorecards, including what is measured and how they are reviewed, can be found in the [OpenSSF Scorecard GitHub Repo](https://github.com/ossf/scorecard).

## How to Check my Project's Score

**Via reports from the weekly cron job**
Use the [Webviewer](https://scorecard.dev/viewer/) to find your project's score by appending your repository URI to the `uri` parameter, for example: [Webviewer example](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero).
If your project is not available, please add it via PR to the [OpenSSF Scorecard GitHub Repo](https://github.com/ossf/scorecard).
[Example PR](https://github.com/ossf/scorecard/pull/4884).

**Via GitHub Actions and API**
Run the score manually in your repo by adding a workflow in your repo's GitHub Actions or use the API as mentioned in the [documentation](https://github.com/ossf/scorecard?tab=readme-ov-file#scorecard-rest-api).

## Repo Scores

| Project                     | Badge                                                                                                                                                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hiero                       | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero)                                             |
| hiero-block-node            | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-block-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-block-node)                       |
| hiero-consensus-node        | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-consensus-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-consensus-node)               |
| hiero-did-sdk-python        | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-did-sdk-python/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-did-sdk-python)               |
| hiero-docs                  | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-docs/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-docs)                                   |
| hiero-gradle-conventions    | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-gradle-conventions/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-gradle-conventions)       |
| hiero-improvement-proposals | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-improvement-proposals/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-improvement-proposals) |
| hiero-json-rpc-relay        | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-json-rpc-relay/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-json-rpc-relay)               |
| hiero-local-node            | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-local-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-local-node)                       |
| hiero-mirror-node           | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-mirror-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-mirror-node)                     |
| hiero-mirror-node-explorer  | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-mirror-node-explorer/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-mirror-node-explorer)   |
| hiero-sdk-cpp               | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-cpp/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-cpp)                             |
| hiero-sdk-go                | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-go/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-go)                               |
| hiero-sdk-java              | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-java/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-java)                           |
| hiero-sdk-js                | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-js/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-js)                               |
| hiero-sdk-python            | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-python/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-python)                       |
| hiero-sdk-rust              | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-rust/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-rust)                           |
| hiero-sdk-swift             | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-swift/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-swift)                         |
| hiero-sdk-tck               | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-sdk-tck/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-sdk-tck)                             |
| hiero-solo-action           | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-solo-action/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-solo-action)                     |
| hiero-website               | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/hiero-website/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/hiero-website)                             |
| sdk-collaboration-hub       | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/sdk-collaboration-hub/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/sdk-collaboration-hub)             |
| solo                        | [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hiero-ledger/solo/badge)](https://scorecard.dev/viewer/?uri=github.com/hiero-ledger/solo)                                               |
