# Technical Assessment Report
 
*Independent Hiero Network Deployment, Phase 1 · MAKE Group, LLC for Hedera Hashgraph, LLC · October 2026*
 
This report assesses the technical readiness and maturity of Hiero for organizations that want to run their own network. Its sections cover operational workflows, installation complexity, developer and operator experience, and automation maturity. The last section compares Hiero with industry practice. The report draws on the two deployments described in the Deployment Validation Report and on a review of public documentation, repositories and distribution channels.
 
**Overall:** the software is technically mature, and the mechanisms an operator relies on, such as upgrades, node changes and metrics, already exist. The documentation, packaging and automation around it lag behind. They were built for Hedera's own network and for local test networks, most likely because that is where Hiero has run so far, and for networks run independently they are still at an early stage.
 
## What we mean by a production network
 
There is no single definition of a production blockchain network, and requirements differ between end users, from hardware to the preferred way of deploying. We therefore describe a production network by the outcomes it must deliver rather than by a distribution or hardware profile: several independent organizations operate it jointly and securely, and can monitor, upgrade, recover and govern it without help from the Hiero team.
 
To make this concrete, we defined eight properties, drawing on our own experience of operating blockchain networks. Some apply to any production software, and for these Google's Production Readiness Review and AWS Well-Architected served as reference points. Others are specific to a blockchain network, which has to be decentralized and needs lifecycle procedures such as upgrade, eviction and recovery by social consensus. Its operators also need to know whether the network as a whole is live, since every node can be up while the network is not. The table below shows what each property requires of a Hiero network:
 
| Property | What it requires of a Hiero network |
|---|---|
| Decentralized | Several independent operators, each holding its own keys. No single party can sign for the network or change its membership alone. |
| Secure | No default or shared secrets, TLS on client and node links, hardened hosts, minimal network exposure. |
| Understandable | An operator can explain every component, port, file and setting it runs. |
| Reproducible | Versioned, verifiable artifacts and a deployment anyone can repeat. |
| Operable | Health is visible day to day and problems can be diagnosed. |
| Recoverable | Losing a node or its data does not lose the ledger. |
| Upgradeable | The network moves to new releases without forking or long downtime. |
| Governable | Membership changes and emergencies follow an agreed process. |
 
All eight apply to any organization running its own network, whether a university research group or a company consortium. Section 2 groups the deployment tracks by audience, since these organizations want different levels of automation.
 
## 1. Operational workflows
 
**Verdict: a private network lacks written procedures for the mechanisms Hiero already has.**
 
An operator needs to check health, monitor, upgrade, add or replace nodes, halt and recover. For each of these tasks some mechanism exists, such as freeze-based upgrades, governed node changes, saved state and metrics, and we used several of them. However, there is no written procedure that tells an operator of a private network when and how to use each mechanism, and who must sign what. Today's procedures assume Hedera's governance; node admission, for example, goes through the Hedera Council, and Hedera's operations team coordinates mainnet upgrades. A private network has no equivalent for admitting, evicting or replacing a member, or for staging an upgrade.
 
A few examples show what this means in practice:
 
- Hiero's security policy lets organizations apply for early notice of critical fixes, but nothing points the operators of a private network to it, and they have no published advisories to follow.
- When the consensus node is upgraded, an operator cannot tell whether the mirror node has to be upgraded as well, because no component publishes which versions work together.
- A release binary can technically be traced to its source, because it is built by a public workflow and the build is deterministic. However, there is no documented way to do it and no signature that ties the published checksum to the build, a limitation HIP-1496 also notes for Council members on mainnet.
- An idle network writes no blocks, so in the mirror node and explorer it looks the same as a stalled one.
## 2. Installation complexity and onboarding tracks
 
**Verdict: every production track still depends on knowledge that is documented only in source code.**
 
An organization can deploy a network in several ways, and the right one depends on who runs it. We therefore grouped the tracks an organization is likely to choose under two audiences. Enthusiasts are individuals, students, evaluators and small teams who want a node or a small network running with as little effort as possible. Professionals are DevOps and infrastructure teams running a network for an organization or a consortium, who expect automation and repeatable lifecycle operations.
 
| Track | Public support today | Status |
|---|---|---|
| ***Enthusiasts*** | | |
| Local test network on one machine | Solo one-shot deploy, hiero-local-node | Available, test networks only |
| A node or small network on a VM or home server, from a package | Node Management Tools installer, written for mainnet nodes; it runs a private network only with manual workarounds and has no usage guide | Partial: no guide or private-network support |
| Cloud marketplace image | Mirror node only (GCP) | Missing for the consensus node |
| AI-agent-assisted setup | llms.txt indexes and agent instructions on the docs sites | Partial: agents inherit the documentation gaps |
| ***Professionals*** | | |
| Kubernetes, several nodes | Solo and solo-charts for test networks; solo-operator and solo-provisioner (HIP-1495) written for Council members | Partial: no production values, sizing, secrets handling or upgrade procedure for a private network |
| Virtual machines or bare metal with own automation | Council requirements page; the enthusiast package would serve here too | Missing: this is the track we had to work out from Solo's source code |
 
Both audiences need the same foundation underneath: published artifacts, a key and genesis tool, a configuration reference and an upgrade procedure. On any track, running a production network also requires the operator to understand the system-account model, the genesis keys, and node settings that today are documented only in source code.
 
Comparable projects support both Kubernetes deployments for professional teams and traditional packaging. Besu, for example, documents binary, Docker and Kubernetes installs side by side. For Hiero, the question is therefore which to build first, and the table below compares the two:
 
| | Kubernetes | Traditional packaging |
|---|---|---|
| **Suits** | Professional teams with Kubernetes skills | Single machines and dedicated servers; enthusiasts and teams with their own automation. In other networks we work with, many operators run dedicated servers by following written instructions. |
| **Strengths** | Declarative deployment, rolling upgrades and an operator model. HIP-1495 suggests this is where Hashgraph's own investment is heading. | Easy to audit and to run on one machine. The package manager resolves dependencies. |
| **Limits** | Assumes Kubernetes skills that many organizations and most enthusiasts lack. Every image still needs a reliable build of the node inside it. | Upgrades and membership changes stay more manual. Packages must be built and tested per distribution, which raises the question of which distributions come first. |
 
Our proposed path follows the natural evolution of software distribution. Signed, verifiable builds come first, because building from source on each host loses the guarantee that every operator runs the same binary. OS packages come next, starting with Ubuntu LTS, which we tested. Container images are then built from those packages, since the package manager installs the binary with its dependencies and makes the image reproducible. On top of those images run both Kubernetes for professionals, built on the HIP-1495 components, and Docker Compose for a single machine, which the Node Management Tools already use. Judging by what we have observed, Hedera may choose to prioritize Kubernetes; in that case the image and chart work would move forward on the same signed builds. The final decision rests with Hedera and the Hiero TSC.
 
## 3. Developer and operator experience
 
**Verdict: good for developers on a test network, not yet for operators of a production network.**
 
Solo's documentation gets a developer to a test network quickly, and its errors are numbered and linked to documentation. Beyond Solo, the public documentation covers two settings: Council onboarding to mainnet, which is coordinated with Hedera's team, and local test networks for developers. Neither shows an organization how to run its own network independently. The block node's documentation already includes a complete production runbook, a model the consensus node can follow.
 
We also noted the following problems in our deployments:
 
- An ignored setting left a network running with the publicly known genesis key, and the setup still finished with a success code.
- The SDKs have built-in settings only for Hedera's own networks. A private network works with them, but it has to be configured by hand, without a guide.
- Recent SDK versions read account balances only through a mirror node, so basic client checks fail on a network without one.
- Event streams, which are on by default and never deleted, filled the disks of an idle network in under four days and halted it, and no component raised an alert.
## 4. Automation maturity
 
**Verdict: mature for single-operator test networks, early for production.**
 
We looked at how much of each lifecycle task can be done without manual steps:
 
- Starting a test network is fully automated. Solo sets up consensus nodes, a mirror node, relay and explorer in one command, in about five minutes.
- Adding a node and upgrading the network are automated on Kubernetes through Solo. When our AI agent tried both, a governed node addition took about five minutes and a network-wide upgrade about three. The mirror node, block node and relay also ship container images and Helm charts, while the consensus node has no documented image or chart of its own.
- Starting a production network is largely manual. Solo's configuration templates are set up for test networks, and the Node Management Tools install single nodes for mainnet, so we scripted the virtual-machine network ourselves.
- Starting a network with several organizations has no automation. Solo expects one party to generate and hold every node's keys, and no tool builds the genesis roster or the genesis key.
In short, automation is strongest where a single operator runs a test network, and weakest where several organizations have to act together.
 
## 5. Comparison with industry practice
 
To put these findings in context, we compared Hiero with five projects that organizations use to run their own networks: Hyperledger Besu (private Ethereum networks), Hyperledger Fabric, the Cosmos SDK, Avalanche L1s and the Polkadot SDK. For releases, we also looked at Geth, a widely used Ethereum client. The table below shows what operators of these projects get and where Hiero stands today:
 
| What operators of comparable networks get | Examples | Hiero today |
|---|---|---|
| Starting a new network is a documented, first-class task | Besu's "Create a QBFT network" tutorial generates the genesis file and node keys with one command. Fabric's "Deploying a production network" guide walks through it step by step. | Only Council onboarding to mainnet and local test networks are documented. |
| Each organization contributes to genesis without handing over private keys | In Cosmos, each validator signs its own genesis transaction and a coordinator merges them. In Fabric, each organization runs its own certificate authority. | The genesis roster format is not documented, and Solo generates every node's keys in one place. |
| Test defaults are clearly separated from production | Avalanche's CLI asks whether to use test defaults, which fund a well-known key. Polkadot's docs warn that development keys must never hold value. | Solo starts a network with the publicly known genesis key without asking. The node does the same if an operator's own key is set in the wrong file. |
| Upgrades follow a written procedure, often automated | Cosmos schedules upgrades on-chain, and Cosmovisor switches binaries at the upgrade height. Fabric publishes a four-step upgrade guide. Besu documents upgrades for Linux, Docker, Kubernetes and Ansible. | HIP-1496 describes how Hedera mainnet freezes and upgrades its nodes, but there is no written upgrade procedure for a private network. |
| Monitoring works out of the box | Besu exposes Prometheus metrics and publishes a Grafana dashboard. Fabric nodes have an operations endpoint with metrics and health checks. | A metrics endpoint exists, but there is no metric reference and no published dashboard. |
| Releases are easy to find and verify | Geth signs its downloads with PGP. Besu publishes releases on GitHub with SHA-256 checksums. | Builds have checksums but no signatures, come from a single server, and no document links to them or explains how to trace one to its source. The Node Management Tools installers are signed with a key that is not published in Hedera's documentation and has since been revoked, so the signatures cannot be used. |
 
**Sources.** Besu: Create a QBFT network, QBFT configuration, Upgrade Besu, Metrics. Fabric: Deploying a production network, Upgrading, Operations service. Cosmos: x/genutil, Cosmovisor. Avalanche: Create an L1. Polkadot: Deploy on Polkadot. Geth: Downloads. Hiero: Security policy, HIP-1496.
 
## Conclusion
 
The software is technically mature, but the documentation, packages and procedures an operator needs around it are not. In every area we assessed, Hiero already has the underlying mechanism, and an organization mainly lacks the procedure, package or guide to use it on its own network. Much of this is most likely knowledge the project already has but has not yet had a reason to publish. This is why about two thirds of iteration 1, the minimum needed to run a private network, is documentation rather than new tooling. The Gap Analysis lists each gap and recommends an order for closing them.
 
