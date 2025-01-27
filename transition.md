# Transition of Hedera projects to Hiero

This document contains an overview of the state of the project transition from Hedera to Hiero.
We will do the transition in phases and several different tasks need to be done and checked for each and every project.
Therefore, we created a matrix that shows the state of all projects for that the transition has been started or is planned for the near future.
Next to the matrix that is shown in this document we create issues for each repo that should be transfered.
The issues might contain more detailed information about the transition state as shown in the matrix.
A list of all issues can be found [here](https://github.com/LFDT-Hiero/tsc/issues/5).

A step-by-step guide for doing the transition of a repository can be found [here](https://github.com/hiero-ledger/hiero/blob/main/hashgraph-transfer.md).

## Initial steps

The following table contains an overview of the initial steps that need to be done for each project before the actual transition can start.

| Hedera Repo                        | Hiero Repo                        | automatic DCO check | DCO remediation           | automatic License check    | License remediation        | user rights        | transfered |
| ---------------------------------- | --------------------------------- | ------------------- | ------------------------- | -------------------------- | -------------------------- | ------------------ | ---------- |
| [hedera-sdk-go](https://github.com/hashgraph/hedera-sdk-go)               | [hiero-sdk-go](https://github.com/hiero-ledger/hiero-sdk-go)               | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :white_check_mark: | :tada: |
| [hedera-sdk-tck](https://github.com/hashgraph/hedera-sdk-tck)              | [hiero-sdk-tck](https://github.com/hiero-ledger/hiero-sdk-tck)            | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :white_check_mark: | :tada: |
| [hedera-sdk-cpp](https://github.com/hashgraph/hedera-sdk-cpp)              | [hiero-sdk-cpp](https://github.com/hiero-ledger/hiero-sdk-cpp)            | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :white_check_mark: |  :tada: |
| [hedera-sdk-swift](https://github.com/hashgraph/hedera-sdk-swift)            | [hiero-sdk-swift](https://github.com/hiero-ledger/hiero-sdk-swift)                   | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark: | :white_check_mark: | :tada: |
| [hedera-sdk-js](https://github.com/hashgraph/hedera-sdk-js)               | [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js)               | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :white_check_mark: | :tada: |
| [hedera-sdk-java](https://github.com/hashgraph/hedera-sdk-java)             | [hiero-sdk-java](https://github.com/hiero-ledger/hiero-sdk-java)                    | :white_check_mark:  | :white_check_mark:             | :white_check_mark:         | :white_check_mark:         | :white_check_mark: | :tada: |
| [hedera-sdk-rust](https://github.com/hashgraph/hedera-sdk-rust)             | hiero-sdk-rust                    | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/84)             | :white_check_mark: |  |
| [solo](https://github.com/hashgraph/solo)                        | solo                              | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/44) | |
| [hedera-local-node](https://github.com/hashgraph/hedera-local-node)           | [hiero-local-node](https://github.com/hiero-ledger/hiero-local-node)   | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :white_check_mark: | :tada: |
| [hedera-json-rpc-relay](https://github.com/hashgraph/hedera-json-rpc-relay)       | hiero-json-rpc-relay              | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark: | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/43) | |
| [hedera-mirror-node](https://github.com/hashgraph/hedera-mirror-node)          | hiero-mirror-node                 | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/86)              | :white_check_mark:         | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/79) | :white_check_mark: | |
| [hedera-mirror-node-explorer](https://github.com/hashgraph/hedera-mirror-node-explorer) | hiero-mirror-node-explorer        | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/87)              | :white_check_mark:         | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/31) | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/54) | |
| [hedera-block-node](https://github.com/hashgraph/hedera-block-node)           | hiero-block-node                  | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/85)             | :white_check_mark: | |
| [hedera-services](https://github.com/hashgraph/hedera-services)             | hiero-consensus-node              | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/88)              | :construction:             | :construction:             | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/48) | |
| [hedera-docs](https://github.com/hashgraph/hedera-docs)                 | hiero-docs                        | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/89)              | :white_check_mark:         | :white_check_mark:         | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/47) | |
| [did-method](https://github.com/hashgraph/did-method)                  |                                   | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/90)              | :white_check_mark:         | :white_check_mark:         | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/46) | |
| [did-sdk-js](https://github.com/hashgraph/did-sdk-js)                  |                                   | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/42) | |
| [did-sdk-java](https://github.com/hashgraph/did-sdk-java)                |                                   | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/91)              | :construction:             | :construction:             | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/45) | |
| [hedera-protobufs](https://github.com/hashgraph/hedera-protobufs)            | hiero-protobufs                   | :white_check_mark:  | :white_check_mark:        | :white_check_mark:         | :white_check_mark:         | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/77) |  |
| [hedera-improvement-proposal](https://github.com/hashgraph/hedera-improvement-proposal) | hiero-improvement-proposals       | :white_check_mark:  | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/92)              | :white_check_mark:         | :red_circle:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/80) | :construction:[<sup>*</sup>](https://github.com/hiero-ledger/tsc/issues/40) | |

### Defintions of columns

**Hedera Repo** - Name and maybe link to old Hedera repo

**Hiero Repo** - Name and maybe link to new Hiero repo

**automatic DCO check** - Check if all commits in the repo are automatically checked for DCO signing

**DCO remediation** - We need to ensure that all commits on the main branch are DCO signed. This can be accomplished by retroactively signing commits through an empty signed commit on the repository.

**automatic License check** - Check if the repo is automatically checked for licensing issues

**License remediation** - Check if the repo license and the licenses of all transitive dependencies are compatible with the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html).

**user rights** - Users, groups and rights are managed by the `config.yaml` file in the https://github.com/LFDT-Hiero/governance repo. We will create custom groups for each repo. That groups must be created and added to the specific repos in the `config.yaml`.
