# Hedera-to-Hiero Transition Report

**Date:** 2024-12-19 
**Author:** Hendrik Ebbers (@hendrikEbbers)

This file is a report on the transition of the Hedera projects to Hiero.
While we have the “transfer document” at https://github.com/hiero-ledger/hiero/blob/main/transition.md that contains a matrix of the transition state,
the document can not contain all the details regarding every project that are needed to understand some of the blockers, problems, and general challenges.
This document has been created to give a better understanding of the transition process.

## DCO checks
Two tools are available for the DCO checks. The Linux Foundation (LF) provides the “lftools” tool to perform DCO checks. 
he documentation can be found at https://docs.releng.linuxfoundation.org/projects/lftools/en/latest/commands/dco.html.
The tool scans not only the main branch of a project but also all unclosed feature branches.
This comprehensive scanning reveals many commits with missing DCOs.
As a result, we developed a custom tool, which is available on Github (https://github.com/hiero-ledger/hiero/tree/main/dco-check).
The tool is based on an initial script by Michael Garber (@mgarbs) and has been refactored to a generic tool by Timo Brandstätter (@timo0) and me.

We had several Google sheets with the goal of having a good overview of all missing DCO commits.
Since many people started to work in those sheets, we often lost track, and the current state of things was unclear.
Therefore, I created a new spreadsheet to which only I have write access.
Everybody else is welcome to comment.

Based on the new sheet, we have 134 commits without DCO signing today:

- 1 commit of 1 user in the Swift SDK
- 6 commits of 5 users in the JS SDK
- 6 commits of 4 users in the Java SDK
- 1 commit by 1 user in the JSON-RCP-Relay
- 11 commits by 1 user in the Mirror-Node
- 6 commits by 1 user in the Mirror-Node Explorer
- 4 commits by 2 users in the Services / Consensus-Node
- 32 commits by 22 users in the Docs
- 20 commits by 1 user in the DID-Methods
- 16 commits by 2 users in the DID Java SDK
- 31 commits by 12 users in the HIPs

We already sent out emails to all valid mail addresses some weeks ago, but so far, only three persons have replied.

We mailed LFDT and asked about best practices for the next steps.
Simi Hunjan (@SimiHunjan) is currently in contact with Ry by mail to discuss the commits of the docs repo.

## License checks
Other than for license checks, the LF does not provide open or free tooling for license checks.
Therefore, we needed to find a good way to do such scans automatically and periodically for our projects.
LF does scans for the projects of LFDT but only scheduled in a fix time range. This approach does not fit our needs.

Since SNYK is used for the project under the Hashgraph organization at GitHub, I started to analyse reports from SNYK.
Thanks to Nathan Klick (@nathanklick) I received access to the SNYK resources of most repositories.
Since SNYK does not support all the programming languages and build tools we are using, and I do not have access to 100% of all projects, I needed to find another way to do those license checks.

When doing a check, I concentrated only on dependencies that are used at RUNTIME of the project and not on dependencies that are needed at BUILDTIME or TESTTIME.
Next to that my main goal was to create an automation for the checks.

Since I have not found a good tool (including suggestions by LF: https://www.linuxfoundation.org/resources/open-source-guides/tools-managing-open-source-programs) I started to create a small project on my own: https://github.com/hendrikebbers/oss-license-scanner
That project allowed me to scan most of our projects automatically. Since GitHub needs to be polled a lot for those check runs, it can only be executed a given number of runs a day since the GitHub REST API is limited in calls per hour. After some iterations of working on the tooling, the results looked quite good and are published at https://github.com/hendrikebbers/oss-license-scanner/tree/main/missing
Since coming from the Java ecosystem, it took me some time to understand how RUST, Swift, Python, NPM,… define projects and dependencies. Just this week, it took me hours to understand what the “string-width-cjs” JavaScript dependency does, which is used in local-node, and why it is a possible attack vector (see https://snyk.io/de/blog/supply-chain-string-width-cjs-npm/ for more information).
The tool sadly had a bug for scanning JS-based projects, and therefore, the results for our JS projects looked too optimistic for some time. I fixed that bug earlier this week.
Based on the latest iteration of scans, the following projects depend on some libs with problematic or questionable licenses:

- Services / Consensus-Node depends on com.github.spotbugs:spotbugs-annotations that uses LGPL-2.1 as a license. This problem can easily be solved since it is not needed at runtime.
- Services / Consensus-Node depends on net.i2p.crypto:eddsa that uses CC0-1.0 as a license.
- The JS SDK depends on argparse that uses Python-2.0 as a license.
- The JS SDK depends on tslib that uses 0BSD as a license.
- The Swift SDK depends on CryptoSwift that uses a custom license (https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE) as a license.
- Local-Node depends on tslib that uses 0BSD as a license. This is coming from the JS SDK.
- Local-Node depends on argparse that uses Python-2.0 as a license. This is coming from the JS SDK.

The Rust SDK and Java SDK do not have any problematic dependencies and can be transferred from the current point of view.
Based on the JS-specific bug and some other points Solo, Mirror-Node, Mirror-Node-Explorer, and JSON-RCP-Relay are again checked.

With all those problems in mind, I had some chats with people from the OSS community the last days and found a new tool yesterday that might end in better results: The OSS Review Toolkit (https://oss-review-toolkit.org/ort/).
The tool is open source and supports license scans for a huge range of language and build tools.
I created JSON-based results and even a WebView for results.
Currently, I plan to use that tool for scanning and then import the JSON results in my oss-license-scanner to create results for our projects.
Scanning a single project with that tool takes some time (just had a scan that needed 30 min).
I plan to come up with new results by the end of the year.
I had a Zoom Call with the lead developer today, and he helped me solve several issues.

## Releases and Deployments
Since this week, we have everything set up in the Hiero organization at GitHub to publish releases to NPMJS and Maven Central.
Until now, we have not migrated a project that needs those mechanisms, and therefore, we will test it for the first time in the future.

The projects migrated to LFDT have already created releases in GitHub.

## Conclusion
Since the DCO and License remediation are not 100% done today, we will continue to move those topics forward.
Every repository that has no more commits with missing DCO signing and has passed the license check can be transferred to Hiero.
For that, we will always try to have the matrix at https://github.com/hiero-ledger/hiero/blob/main/transition.md as updated as possible.

The following steps for the DCO topic are currently being discussed with the Linux Foundation, and we hope to have an answer soon.

For the license scan, I will use the OSS Review Toolkit (ORT) to scan the projects.
I’m now invited to the Slack server of ORT and have already answered several of my questions for scanning all our projects.
I assume this approach will end in very good and reproducible results shortly.

Transferring a project like the Hedera sources to an Open Source Foundation like the Linux Foundation is a more complex topic than one might think.
I already had some experience in that topic as a founding member of Eclipse Adoptium.
For that project, we transferred all the sources from AdoptOpenJDK to the Eclipse Foundation.
However, against the amount and complexity of projects we have with the transition to Hiero, Eclipse Adoptium was a small migration.
With that in mind, I hope that we can create a well-documented and reproducible toolchain for the transfer that will help us and others in the future.
