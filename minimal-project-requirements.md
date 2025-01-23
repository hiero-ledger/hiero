# Minimal project requirements

This document describes the minimal requirements for a project under the Hiero org.
A general description on how to transfer a project to Hiero can be found in the [howto-transfer.md](howto-transfer.md) document.

## Requirements for a projects before transferring to Hiero org

The project must fulfill the following requirements before it can be transferred to the Hiero org:

- A README.md file that describes the project and how to use it.
  Hiero has some more concrete requirements for the README.md file that need to be fullfilled after the project has been
  transferred to the Hiero org.
  Those requirements are described later in this document.
- A LICENSE file that describes the license of the project.
  The license should be Apache 2.0 or MIT in best case.
  In general all licenses that are [approved by the Linux Foundation Decentralized Trust](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses.html) are allowed.
- Each commit of a project must be GPG signed.
  More information can be found [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)
- The project muss fulfill a license check.
  A concrete documentation on how to do that will be provided soon.
- An up-to-date list of maintainers and committers of the project must be available and shared with the TSC.

## Requirements for a project when transferring to Hiero org

When the project get transferred to Hiero the following steps must be done:

- For Projects that are hosted under the Linux Foundation each commit must contain a DCO sign-off.
  We have a GitHub action in place that will check for that.
- The TSC will define a list of "must-have" GitHub apps that must be installed in the project.
  This list and configuration details will be provided soon.
  All those plugins must be installed and configured directly after the project has been transferred to the Hiero org.
- One of the first commits after the transfer should contain an update of the readme that contains information about our Code of Conduct and other important information.
  A template for a README.md file will be provided soon.