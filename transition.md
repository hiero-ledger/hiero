# Transition of Hedera projects to Hiero

This document contains an overview of the state of the project transition from Hedera to Hiero.
We will do the transition in phases and several different tasks need to be done and checked for each and every project.
Therefore, we created a matrix that shows the state of all projects for that the transition has been started or is planned for the near future.
Next to the matrix that is shown in this document we create issues for each repo that should be transfered.
The issues might contain more detailed information about the transition state as shown in the matrix.
A list of all issues can be found [here](https://github.com/LFDT-Hiero/tsc/issues/5).

A step-by-step guide for doing the transition of a repository can be found [here](https://github.com/hiero-ledger/hiero/blob/main/hashgraph-transfer.md).

| Hedera Repo                                                                             | Hiero Repo                  | DCO check          | DCO remediation  | License remediation  | README and others updated | user rights    | vendor neutral code | GitHub Actions     | deployments        | Community informed |
| --------------------------------------------------------------------------------------- | --------------------------- | ------------------ | ---------- | -------------- | ------------------------- | -------------- | ------------------- | ------------------ | ------------------ | ------------------ |
| [hedera-sdk-go](https://github.com/hashgraph/hedera-sdk-go)                             | hiero-sdk-go                | :white_check_mark: | :white_check_mark: | :construction: |             | :construction: |                     | :construction:     | :heavy_minus_sign: | |
| [hedera-sdk-swift](https://github.com/hashgraph/hedera-sdk-swift)                       | hiero-sdk-swift             | :white_check_mark: | :white_check_mark: | :construction: |             | :construction: |                     | :construction:     | :heavy_minus_sign: | |
| [hedera-sdk-tck](https://github.com/hashgraph/hedera-sdk-tck)                           | [hiero-sdk-tck](https://github.com/hiero-ledger/hiero-sdk-tck)               | :white_check_mark: | :white_check_mark: | :white_check_mark: | :construction: | :white_check_mark: |                     | :construction: | :heavy_minus_sign: | |
| [hedera-sdk-js](https://github.com/hashgraph/hedera-sdk-js)                             | hiero-sdk-js                | :white_check_mark: | :white_check_mark: | :white_check_mark: |                           |                |                     |                    | :construction:| |
| [hedera-sdk-cpp](https://github.com/hashgraph/hedera-sdk-cpp)                           | [hiero-sdk-cpp](https://github.com/hiero-ledger/hiero-sdk-cpp)               | :white_check_mark: | :white_check_mark: | :white_check_mark: | :construction: | :white_check_mark: |                     | :construction: | :heavy_minus_sign: | |
| [hedera-sdk-java](https://github.com/hashgraph/hedera-sdk-java)                         | hiero-sdk-java              | :white_check_mark:     |            | :white_check_mark: |                          |  :white_check_mark: |                     |                    | :construction: | |
| [hedera-sdk-rust](https://github.com/hashgraph/hedera-sdk-rust)                         | hiero-sdk-rust              | :white_check_mark: | :white_check_mark: | :construction: |                           |                |                     |                    |                    | |
| [solo](https://github.com/hashgraph/solo)                                               |                             | :white_check_mark: | :white_check_mark: |      :white_check_mark: |                           |                |                     |                    | :construction: | |
| [hedera-local-node](https://github.com/hashgraph/hedera-local-node)                     |                             | :white_check_mark: | :white_check_mark: | :white_check_mark: |                           |                |                     |                    | :construction: | |
| [hedera-json-rpc-relay](https://github.com/hashgraph/hedera-json-rpc-relay)             |                             | :white_check_mark:    |            | :white_check_mark: |                           |                |                     |                    |                    | |
| [hedera-mirror-node](https://github.com/hashgraph/hedera-mirror-node)                   |                             | :white_check_mark:    |            | :construction: |                           | :white_check_mark: |                     |                    |                    | |
| [hedera-mirror-node-explorer](https://github.com/hashgraph/hedera-mirror-node-explorer) |                             | :white_check_mark: |            |      :construction: |                           |                |                     |                    |                    | |
| [hedera-block-node](https://github.com/hashgraph/hedera-block-node)                     |                             | :white_check_mark: | :white_check_mark: | :construction: |                           |:white_check_mark: |                     |                    |                    | |
| [hedera-services](https://github.com/hashgraph/hedera-services)                         |                             | :white_check_mark:    |            | :construction: |                           |                |                     |                    |                    | |
| [hedera-docs](https://github.com/hashgraph/hedera-docs)                                 |                             | :construction:     |            | :construction:|                           |                |                     |                    |                    | |
| [did-method](https://github.com/hashgraph/did-method)                                   |                             | :construction:     |            | :construction:  |                           |                |                     |                    |                    | |
| [did-sdk-js](https://github.com/hashgraph/did-sdk-js)                                   |                             | :white_check_mark: | :white_check_mark: | :construction: |                           |                |                     |                    |                    | |
| [did-sdk-java](https://github.com/hashgraph/did-sdk-java)                               |                             | :construction:     |            | :construction: |                           |                |                     |                    |                    | |
| [hedera-protobufs](https://github.com/hashgraph/hedera-protobufs)                       |                             | :white_check_mark: | :white_check_mark: | :white_check_mark: |                           |     |                     |                    |                    | |
| [hedera-improvement-proposal](https://github.com/hashgraph/hedera-improvement-proposal) | hiero-improvement-proposals | :construction:     |            | :construction: | :construction:            | :construction: |                     | :construction:     | :heavy_minus_sign: | |

### Icons

:x: - Problem with given tasks

:white_check_mark: - Task sucessfull 

:construction: - In progress

:heavy_minus_sign: - not needed (for example a repo without deployments)

### Defintions of columns

**Hedera Repo** - Name and maybe link to old Hedera repo

**Hiero Repo** - Name and maybe link to new Hiero repo

**DCO check** - Check if all commits in the repo are signed the DCO. We have [a python tool](https://github.com/hiero-ledger/hiero/tree/main/dco-check) that can run the checks for you.

**DCO remediation** - We need to ensure that all commits on the main branch are DCO signed. This can be accomplished by retroactively signing commits through an empty signed commit on the repository.

**License remediation** - Check if the repo license and the licenses of all transitive dependencies are compatible with the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html). All open issues regarding license problems can be found [here](https://github.com/LFDT-Hiero/tsc/labels/license%20issue).

**README and others updated** - Files like README.md, MAINTAINERS.md and others must exist and be up to date. More information can be found in the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/repository-structure.html)

**user rights** - Users, groups and rights are managed by the `config.yaml` file in the https://github.com/LFDT-Hiero/governance repo. We will create custom groups for each repo. That groups must be created and added to the specific repos in the `config.yaml`.

**vendor neutral code** - Names like "Hedera" and or "Hashgraph" are removed from the code (and other ressources) of the repository.

**GitHub Actions** - GitHub Actions must work for Hiero repositories. This can include the creation of possible tokens, service accounts or custom GitHub action runners.

**deployments** - Deployments can be published webpages (like for HIPs or docs) or release artifacts (like a jar) that is deployed to a registry. All that need to be reconfigured for Hiero.

