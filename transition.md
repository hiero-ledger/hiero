# Transition of Hedera projects to Hiero

This document contains an overview of the state of the project transition from Hedera to Hiero.
We will do the transition in phases and several different tasks need to be done and checked for each and every project.
Therefore, we created a matrix that shows the state of all projects for that the transition has been started or is planned for the near future.

| Hedera Repo                                                                             | Hiero Repo                  | DCO check      | License check  | README and others updated | user rights    | vendor neutral code | GitHub Actions     | deployments        |
| --------------------------------------------------------------------------------------- | --------------------------- | -------------- | -------------- | ------------------------- | -------------- | ------------------- | ------------------ | ------------------ |
| [hedera-sdk-go](https://github.com/hashgraph/hedera-sdk-go)                             | hiero-sdk-go                | :construction: | :construction: | :construction:            | :construction: |                     | :construction:     | :heavy_minus_sign: |
| [hedera-sdk-swift](https://github.com/hashgraph/hedera-sdk-swift)                       | hiero-sdk-swift             | :construction: | :construction: | :construction:            | :construction: |                     | :construction:     | :heavy_minus_sign: |
| [hedera-sdk-tck](https://github.com/hashgraph/hedera-sdk-tck)                           | hiero-sdk-tck               |                |                |                           |                |                     |                    |                    |
| [hedera-sdk-js](https://github.com/hashgraph/hedera-sdk-js)                             | hiero-sdk-js                |                |                |                           |                |                     |                    |                    |
| [hedera-sdk-cpp](https://github.com/hashgraph/hedera-sdk-cpp)                           | hiero-sdk-cpp               |                |                |                           |                |                     |                    |                    |
| [hedera-sdk-java](https://github.com/hashgraph/hedera-sdk-java)                         | hiero-sdk-java              |                |                |                           |                |                     |                    |                    |
| [hedera-sdk-rust](https://github.com/hashgraph/hedera-sdk-rust)                         | hiero-sdk-rust              |                |                |                           |                |                     |                    |                    |
| [solo](https://github.com/hashgraph/solo)                                               |                             |                |                |                           |                |                     |                    |                    |
| [hedera-local-node](https://github.com/hashgraph/hedera-local-node)                     |                             |                |                |                           |                |                     |                    |                    |
| [hedera-json-rpc-relay](https://github.com/hashgraph/hedera-json-rpc-relay)             |                             |                |                |                           |                |                     |                    |                    |
| [hedera-mirror-node](https://github.com/hashgraph/hedera-mirror-node)                   |                             |                |                |                           |                |                     |                    |                    |
| [hedera-mirror-node-explorer](https://github.com/hashgraph/hedera-mirror-node-explorer) |                             |                |                |                           |                |                     |                    |                    |
| [hedera-block-node](https://github.com/hashgraph/hedera-block-node)                     |                             |                |                |                           |                |                     |                    |                    |
| [hedera-services](https://github.com/hashgraph/hedera-services)                         |                             |                |                |                           |                |                     |                    |                    |
| [hedera-docs](https://github.com/hashgraph/hedera-docs)                                 |                             |                |                |                           |                |                     |                    |                    |
| [did-method](https://github.com/hashgraph/did-method)                                   |                             |                |                |                           |                |                     |                    |                    |
| [did-sdk-js](https://github.com/hashgraph/did-sdk-js)                                   |                             |                |                |                           |                |                     |                    |                    |
| [did-sdk-java](https://github.com/hashgraph/did-sdk-java)                               |                             |                |                |                           |                |                     |                    |                    |
| [hedera-protobufs](https://github.com/hashgraph/hedera-protobufs)                       |                             |                |                |                           |                |                     |                    |                    |
| [hedera-improvement-proposal](https://github.com/hashgraph/hedera-improvement-proposal) | hiero-improvement-proposals | :construction: | :construction: | :construction:            | :construction: |                     | :construction:     | :heavy_minus_sign: |

### Icons

:x: - Problem with given tasks

:white_check_mark: - Task sucessfull 

:construction: - In progress

:heavy_minus_sign: - not needed (for example a repo without deployments)

### Defintions of columns

**Hedera Repo** - Name and maybe link to old Hedera repo

**Hiero Repo** - Name and maybe link to new Hiero repo

**DCO check** - Check if all commits in the repo are signed the DCO

**License check** - Check if the repo license and the licenses of all transitive dependencies are compatible with the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html)

**README and others updated** - Files like README.md, MAINTAINERS.md and others must exist and be up to date. More information can be found in the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/repository-structure.html)

**user rights** - Users, groups and rights are managed by the `config.yaml` file in the https://github.com/LFDT-Hiero/governance repo. We will create custom groups for each repo. That groups must be created and added to the specific repos in the `config.yaml`.

**vendor neutral code** - Names like "Hedera" and or "Hashgraph" are removed from the code (and other ressources) of the repository.

**GitHub Actions** - GitHub Actions must work for Hiero repositories. This can include the creation of possible tokens, service accounts or custom GitHub action runners.

**deployments** - Deployments can be published webpages (like for HIPs or docs) or release artifacts (like a jar) that is deployed to a registry. All that need to be reconfigured for Hiero.

