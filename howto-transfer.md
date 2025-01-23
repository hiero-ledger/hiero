# How to transfer a project to Hiero

This document shows the workflow for transferring any (public or private) project to Hiero and advises on several best practices for setting up a good
open-source project that fits the pattern we use in Hiero.

## Getting in touch with the Hiero community

The first and most important task to contribute to Hiero is to become a community member.
Hiero defines an open and welcoming community, and we are happy for any contribution independent of its size or type.
Our [GitHub discussions](https://github.com/orgs/LFDT-Hiero/discussions) are a good starting point for contacting the community.
Through discussions with the community, you will understand if your project is a good fit for Hiero.
Next to the discussions we have a weekly community call that is open to attend.
More information about that and other Hiero appoitnments and events can be found in our [public calender](https://zoom-lfx.platform.linuxfoundation.org/meetings/lf-decentralized-trust?view=week).

To start submitting, transferring, or creating a project to Hiero, the [technical steering committee (TSC)](https://github.com/hiero-ledger/tsc?tab=readme-ov-file#overview) must be informed.
Individual maintainers of the Hiero projects form the TSC and will decide what projects will be part of Hiero.

## Minimal requirements of a project

Since Hiero is part of the [Linux Foundation (LF)](https://www.linuxfoundation.org), all requirements defined by LF must be met for a project to be considered.
Hiero is part of the sub-foundation [LF Decentralized Trust (LFDT)](https://www.lfdecentralizedtrust.org) within the Linux Foundation, which adds additional project constraints.
A project must fulfill the following requirements:

- Each commit of a project must be GPG signed.
  More information can be found [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)
- LFDT must support the project licenses and all transient dependencies.
  A complete list of all supported licenses can be found [here](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html).
  If a needed license is not listed in that document, the TSC can be contacted for further discussion.
- A project must contain specific files defining the LFDT Code of Conduct and more.
  A detailed overview can be found [here](https://lf-decentralized-trust.github.io/governance/governing-documents/repository-structure.html).
  We have already covered several of those files at [https://github.com/hiero-ledger/.github](https://github.com/hiero-ledger/.github).
- LFDT defined some [best practices for projects](https://lf-decentralized-trust.github.io/governance/guidelines/project-best-practices.html).
  We recommend to fulfill as many of those as possible.

## Project sponsors

To become a project of Hiero sponsors from the community are needed.
A sponsor can be a maintainer of another project, a [registered LFDT member](https://www.lfdecentralizedtrust.org/members) or a member of the TSC.
The TSC expect that a project that should be transfered to Hiero has at least 3 sponsors.
If you are new to LFDT and or Hiero the best way to get in contact with possible sponsors is by getting in touch with the Hiero community.
Details about that can be found above.

## Create an issue for the project

A project proposal must be created as an issue in the [tsc repository](https://github.com/hiero-ledger/tsc).
The issue must be labeled by the ['project proposal' label](https://github.com/hiero-ledger/tsc/labels/project%20proposal).
We are currently working on a good template for a project proposal.

## TSC will vote on the issue

The TSC will review the submitter of the proposal to a TSC meeting and provide a slot to introduce the project.
Here the TSC can ask any additional questions regarding the project and the project proposal.
As a next step and final the TSC will decide (by voting) if the project will be added directly to the [hiero-ledger org](https://github.com/hiero-ledger).
For some projects the TSC might suggest to transfer it to the [LF Decentralized Trust labs](https://lf-decentralized-trust-labs.github.io).
This allows the project to mature and align with industry standards before it is potentially transferred to Hiero.


