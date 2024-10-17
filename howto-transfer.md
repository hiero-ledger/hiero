# How to transfer a project to Hiero

This document shows the workflow for transferring any (public or private) project to Hiero and advises on several best practices for setting up a good
open-source project that fits the pattern we use in Hiero.

> **Note**
>
> This document is only a draft and not final.
> We create the document in the open and feedback is more than welcome.
> The content of the document is not official until the technical steering committee (TSC) of Hiero voted on it.

## Getting in touch with the Hiero community

The first and most important task to contribute to Hiero is to become a community member.
Hiero defines an open and welcoming community, and we are happy for any contribution independent of its size or type.
Our [GitHub discussions](https://github.com/orgs/LFDT-Hiero/discussions) are a good starting point for contacting the community.
Through discussions with the community, you will understand if your project is a good fit for Hiero.
Next to the discussions we have a weekly community call that is open to attend.
More information about that and other Hiero appoitnments and events can be found in our [public calender](https://zoom-lfx.platform.linuxfoundation.org/meetings/lf-decentralized-trust?view=week).

To start submitting, transferring, or creating a project to Hiero, the technical steering committee (TSC) must be informed.
Individual maintainers of the projects form the TSC and will decide what projects will be part of Hiero.
If you want to contact the TSC regarding adding a project to Hiero, the best way is by open an issue in the [TSC repo](https://github.com/LFDT-Hiero/tsc).

## Minimal requirements of a project

Since Hiero is part of the [Linux Foundation (LF)](https://www.linuxfoundation.org), all requirements defined by LF must be met for a project to be considered.
Hiero is part of the sub-foundation [LF Decentralized Trust (LFDT)](https://www.lfdecentralizedtrust.org) within the Linux Foundation, which adds additional project constraints.
A project must fulfill the following requirements:

- Each commit of a project must be signed by the DCO.
  More information can be found [here](https://wiki.linuxfoundation.org/dco).
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

TODO

## TSC will vote on the issue

TODO



