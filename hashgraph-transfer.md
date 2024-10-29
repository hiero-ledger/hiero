# Hashgraph to Hiero Repository Transfer Process

When transferring ownership of a repository from [Hashgraph](https://github.com/hashgraph) to [Hiero-Ledger](https://github.com/hiero-ledger) in Github the steps outlined below must be completed

## Definitions

- **Repository Transfer Agent (TA)** 
  - The person responsible for transferring the repository
  - Must have ability to create a repository on the receiving organizations side (Hiero)
- **Repository Transfer Approval Agent (AA)**
  - The person responsible for approving PRs throughout the transfer process
  - Must have approval authority on the Hiero-Ledger/governance repository and on the target repository

## PRE-TRANSFER Checks

Prior to the day of transfer the following items shall be defined and made available to the **Repository Transfer Agent**

- Target Repository Name (like hiero-sdk-foo)
- Maintainer Group Name (like hiero-sdk-foo-maintainer)
- Maintainers List (should be 2-3 people)
- Committer Group Name (like hiero-sdk-foo-commiter)
- Committers List 

## Transfer Day

Throughout the transfer process both TA and AA shall be available.

The following steps shall occur to transfer a repository into Hiero from a source organization

- The TA will generate a pull request in the [Hiero-Ledger Governance](https://github.com/hiero-ledger/governance) repository
  - The TA will modify the `config.yaml` file in this repository with the following information
    - The new maintainer group name
    - The new maintainers for the group
    - The new committer group name
    - the new set of committers for that group
    - The new repository to pull in
- The AA will approve the changes in `Hiero-Ledger/governance`
- The TA will transfer the repository from the source organization into Hiero
  - The TA will assign the `Target Repository Name` to the repo upon transfer
- The TA will assign the `Target Repository` to the appropriate github self-hosted runner group
- The TA will open a PR on the `Target Repository`
  - The TA will modify the self-hosted runner labels in the github actions
    - Note: This will enable the repository actions to run after transfer
- The AA will approve the PR on the `Target Repository`
- The AA will set the "Social preview" in the repository settings to https://github.com/hiero-ledger/.github/blob/main/resources/social-media-template.png

At this point the repository is considered **transferred**.

## Post-Transfer Activities

After the repository is transferred the maintainers and committers shall ensure the repository behaves as expected and will triage and solve any immediate issues
