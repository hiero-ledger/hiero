# Transition of projects to Hiero

This document contains an overview of the state of the project transition to Hiero.
For all projects that are transferred from Hedera to Hiero we have an [extra page](transition.md).

The general process for transferring a project to Hiero can be found [here](howto-transfer.md).

## Initial steps

The following table contains an overview of the initial steps that need to be done for each project before the actual transition can start.

| Source Repo                                                                 | Hiero Repo                                                                   | Proposal created   | DCO check & remediation   | License check & remediation | user rights       | TSC presentation & voting |  transfered |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------| ------------------ | ------------------------- | --------------------------- | ----------------- | ------------------------- |------------|
| -                                                                           | [hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python)         | :white_check_mark: | :white_check_mark:        | :white_check_mark:         | :white_check_mark: | :white_check_mark:        | :tada:     |
| -                                                                           | [hiero-solo-action](https://github.com/hiero-ledger/hiero-solo-action)       | :white_check_mark: | :white_check_mark:        | :white_check_mark:         | :white_check_mark: | :white_check_mark:        | :tada:     |
| -                                                                           | [hiero-did-sdk-python](https://github.com/hiero-ledger/hiero-did-sdk-python) | :white_check_mark: | :white_check_mark:        | :white_check_mark:         | :white_check_mark: | :white_check_mark:        | :tada:     |
| [gomint-api](https://github.com/gomintco/gomint-api)                        | -                                                                            | :construction: |         |         | |  |    |
| [hashgraph-online/standards-sdk](https://github.com/hashgraph-online/standards-sdk)                        | -                                                                            | :white_check_mark: |         |         | |  |    |
| [did-method](https://github.com/hashgraph/did-method)                       | hiero-did-method                                                             | :construction: | | | | | |
| [did-sdk-py](https://github.com/hashgraph/did-sdk-py)                       | hiero-did-sdk-py                                                             | :construction: | | | | | |
| [did-sdk-js](https://github.com/hashgraph/did-sdk-js)                       | hiero-did-sdk-js                                                             | :construction: | | | | | |
| [did-sdk-java](https://github.com/hashgraph/did-sdk-java)                   | hiero-did-sdk-java                                                           | :construction: | | | | | |
| [hedera-smart-contracts](https://github.com/hashgraph/hedera-smart-contracts)      | hiero-smart-contracts                                                        | :construction: | | | | | |
| [hedera-the-graph](https://github.com/hashgraph/hedera-the-graph)           | hiero-the-graph                                                              | :construction: | | | | | |
| [hedera-metamask-snaps](https://github.com/hashgraph/hedera-metamask-snaps) | hiero-metamask-snaps                                                         | :construction: | | | | | |
| [hedera-forking](https://github.com/hashgraph/hedera-forking)               | hiero-forking                                                                | :construction: | | | | | |
| [hiero-enterprise-java](https://github.com/OpenElements/hiero-enterprise-java)               | hiero-enterprise-java                                       | :white_check_mark: | | | | | |
| [Hederium](https://github.com/LimeChain/Hederium) | [hiero-hederium](https://github.com/hiero-ledger/hiero-hederium) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :construction: | :white_check_mark: | :construction: |

### Defintions of columns

**Source Repo** - Name and maybe link to old project repo

**Hiero Repo** - Name and maybe link to new Hiero repo

**Proposal created** - A proposal for the project must created. More information can be found [here](howto-transfer.md).

**DCO check & remediation** - We need to ensure that all commits on the main branch are DCO signed. This can be accomplished by retroactively signing commits through an empty signed commit on the repository.

**License check & remediation** - Check if the repo license and the licenses of all transitive dependencies are compatible with the [LFDT guidelines](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html).

**user rights** - Users, groups and rights are managed by the `config.yaml` file in the https://github.com/LFDT-Hiero/governance repo. We will create custom groups for each repo. That groups must be created and added to the specific repos in the `config.yaml`.

**TSC presentation & voting** - The TSC need to vote for adding the project to Hiero
