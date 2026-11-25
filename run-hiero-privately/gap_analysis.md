# Gap Analysis
 
*Independent Hiero Network Deployment, Phase 1 · MAKE Group, LLC for Hedera Hashgraph, LLC · October 2026*
 
To find out what an independent organization still needs before it can run a production Hiero network, we evaluated the Hiero ecosystem against what an experienced infrastructure engineer would typically expect to find. We reviewed the public documentation, repositories and distribution channels of the consensus node, mirror node, block node, JSON-RPC relay and network explorer, as well as of the private network as a whole, and drew on our experience deploying two Hiero networks. Wherever comparable projects publish something that we could not find for Hiero, we counted it as a gap. Each item has a row in the gap register (separately attached artifact), with its status, need, recommended iteration, relative size, comments and a link to what we checked. This document summarizes the register, recommends an order for closing the gaps and highlights the ones that matter most.
 
In total we checked 125 items. Of these, 30 are available today, and the remaining 95 are gaps, 15 of them must-haves.
 
## Assumptions
 
We carried out the gap analysis under the following assumptions:
 
- We assume the gaps will be closed in the open, by the community or by independent contractors, using public material only. We therefore did not count on access to non-public tooling, and an item that may exist privately is still a gap for an outside operator.
- We assume that what comparable projects publish is a fair measure of what an experienced infrastructure engineer expects to find. We therefore judged each item against that rather than against a formal framework or certification.
- We assume the work will be shared among several teams, so we split items per component and per expectation, and each can be planned, prioritized and assigned on its own.
- We assume that questions about missing technical details get reasonably prompt answers from the engineers who maintain the components.
## 1. How to read the register
 
| Column | What it shows | Values |
|---|---|---|
| Category | The area the item belongs to, with the topic after the colon, for example "Documentation: setup". | **Documentation.** Guides and references an operator needs.<br>**Operations.** What it takes to distribute, deploy, monitor and support a network.<br>**Tooling.** Tools an operator uses, including AI tools. |
| Component | The part of the network the item applies to. | Consensus node, mirror node, block node, JSON-RPC relay, network explorer.<br>**Private network.** The network as a whole, such as launch, upgrades and membership.<br>**Other.** Items not tied to one component, such as support channels and security reporting. |
| Item | What an operator would expect to find, named as a deliverable, for example "Consensus node setup guide". | Free text |
| Status | Whether the item can be found in public material. Documentation in a repository counts as public material, while source code does not. | **Available.** An operator can find and use the item today.<br>**Partially available.** Something exists, but it covers only part of the need, for example only Hedera mainnet or only a local test network.<br>**Not found.** We could not find the item in public material. |
| Need | How important the item is for running a production network. | **Must have.** An independent organization cannot run a production network without it.<br>**Should have.** An operator would expect it to be there.<br>**Nice to have.** It improves adoption or experience. |
| Iteration | The recommended order of work, as explained in section 3. Available items have none. | 1 to 6 |
| Size | A relative t-shirt size that compares items with each other, a signal for planning, not a time estimate or a commitment. Available items have none. | **S, M and L.** Small, medium and large, relative to each other.<br>**XL.** Large or open-ended. |
| Comments | What we found, such as where partial material exists and its limits. | "Repo docs only" marks documentation that exists only in a repository. |
| Evidence | Links to the material we checked. Rows without a link are mostly items we could not find. | Links |
 
Partially available and not found items count as gaps. Some available items may still need work if Hedera decides to make the approach consistent across all components, for example where documentation lives or how artifacts are published. That work is not counted among the gaps and is not sized.
 
If a process already works but is not written down, its size covers only documenting it. If something already exists but is built with tooling that is not public, such as the consensus node container image, its size covers building an open alternative, and it would become smaller if that tooling were made public. Consensus node items are often sized larger than the same item for other components, because the consensus node is functionally more complex.
 
## 2. Gaps by category
 
The SOW asks for four kinds of gaps: missing capabilities, operational risks, documentation gaps and tooling gaps. We assigned every gap in the register to one of them.
 
| Category | Must have | Should have | Nice to have | Total |
|---|---:|---:|---:|---:|
| Missing capabilities | 0 | 8 | 16 | 24 |
| Operational risks | 5 | 9 | 3 | 17 |
| Documentation gaps | 8 | 7 | 14 | 29 |
| Tooling gaps | 2 | 3 | 20 | 25 |
| **Total** | **15** | **27** | **53** | **95** |
 
### Missing capabilities
 
Most of the missing capabilities concern distribution. Every component can be built from source, and the mirror node, block node, relay and explorer also ship container images and Helm charts. The consensus node, however, which every network needs, has release builds that no documentation links to, no OS package, and no documented container image or Helm chart. Beyond that, the consensus node's Kubernetes operator is still an early release, documented only for a local test network, and no other component has one. Only the mirror node has a cloud marketplace listing, and there is no published benchmark or capacity guidance for a private network.
 
### Operational risks
 
The day-to-day processes an operator relies on most likely exist inside Hedera's own operations but have not been published for private networks. As a result, a private network has no defined way to upgrade, change its configuration, admit or remove a member, or halt and recover.
 
Security communication follows the same pattern. Hiero's security policy lets organizations apply for early notice of critical fixes, but nothing points a private network's operators to it, they have no published advisories to follow, and release announcements target Hedera mainnet.
 
Operators also have no documented way to verify a consensus node build. Releases come from a single server with checksums but no signatures, and nothing explains where they are published or how to trace a build to its source. The Node Management Tools installers are signed, but the signing key is not published in Hedera's documentation and has been revoked, so the signatures cannot be used. HIP-1496 notes the same limitation on mainnet, where Council members currently have no way to independently verify that the software being deployed matches what was reviewed and approved, and proposes deterministic container images to address it. Each of these is a risk an organization would carry from its first day in production.
 
### Documentation gaps
 
Operator documentation today serves two audiences: Hedera Council members joining mainnet, and developers running a local test network. It does not yet cover launching a private network, including how several organizations start one together while each keeps its own keys and shares control of the governance accounts, and how to keep the publicly known genesis key out of it. Nor does it explain how to set up a consensus node or the Node Management Tools, or how to connect a mirror node. Hardware and architecture guidance, meanwhile, assumes Hedera mainnet. The block node's production runbook is a good example of what the consensus node documentation could look like.
 
### Tooling gaps
 
The available tooling is built either for test networks or for Hedera mainnet. Solo, a test tool, starts a network with the publicly known genesis key unless told otherwise and keeps every node's keys in one place. Its configuration templates are also set up for test networks, and nothing documents which settings a production network should change. Hedera's Node Management Tools install, start and upgrade a node, but they are built for mainnet: on our private network they worked only after manual fixes, their defaults assume mainnet hardware, and their key command protects node keys with a fixed password. Finally, no tool creates the genesis roster or the genesis key.
 
## 3. Recommended order
 
We grouped the gaps into six iterations, in a recommended order. Iteration 1 is the bare minimum to run a private network, iteration 2 completes the foundation, and iterations 3 to 6 can be scheduled as demand appears:
 
| Iteration | Focus | What it covers | Gaps | Sizes |
|---|---|---|---:|---|
| 1 | Bare minimum to run a private network | Linked release builds, operator guides for launch, consensus node, Node Management Tools and mirror node, upgrade, configuration and membership procedures, metrics and health endpoints, key and node management tooling | 27 | 15 S, 11 M, 1 L |
| 2 | Complete foundation | OS packages with signed artifacts, vulnerability announcements, compatibility matrices, halt and restart, recovery and backup procedures, a guide for connecting SDK clients | 13 | 7 S, 2 M, 4 L |
| 3 | Container image and supporting components | Consensus node container image, relay and explorer documentation, alerting recommendations, AI skills and MCP servers, a network health check, faucet and a local portal | 26 | 10 S, 15 M, 1 L |
| 4 | Kubernetes packaging and dashboards | Consensus node Helm chart, Grafana dashboards, remaining alerting, storage resize | 7 | 5 M, 2 L |
| 5 | Automation and verification at scale | Kubernetes operators, acceptance and smoke tests, benchmarks, load generation, capacity planning, a public testnet, deprecation announcements | 16 | 6 M, 1 L, 9 XL |
| 6 | Marketplaces and performance testing | Cloud marketplace images, relay operator, API performance tests | 6 | 3 M, 3 XL |
 
About two thirds of the gaps in iteration 1 are documentation, most of it small, because the process already works and only needs writing down.
 
The order follows dependencies rather than strict stages. Some gaps depend on others being closed first, while gaps in the same iteration can be worked on in parallel.
 
Distribution illustrates the logic best, because it follows a natural evolution: a published, verifiable build, then OS packages, then a container image built from those packages, then a Helm chart, and only then a Kubernetes operator or a marketplace image. Building from source on each host loses the guarantee that every operator runs the same binary. A package manager, in turn, is what makes an image reproducible, because it installs the binary together with its dependencies.
 
The same reasoning orders everything else. Metrics and health endpoints come first, because operators need visibility from the first day. Alerting follows once the network runs, and dashboards follow alerting. Acceptance tests and benchmarks come late because until then operators can verify a network in simpler ways. AI skills and MCP servers come in iteration 3 because they package the documentation that the first two iterations produce.
 
This order is our recommendation, and Hedera and the Hiero community may change it for a strategic reason. Judging by what we have observed, Hedera may choose to prioritize Kubernetes; in that case the container image, Helm chart and operators would move forward while still resting on the published, signed builds from iterations 1 and 2. Those two iterations are needed on every route, so work on them can start before that choice is made.
 
## 4. The must-haves
 
All 15 must-have gaps fall in iteration 1. Grouped by area, with sizes in brackets, they are:
 
**Launching a private network**
 
- Private network launch and configuration documentation (M)
- Private network component architecture documentation (S)
- Consensus node setup guide (M)
- Consensus node hardware requirements (L)
- Node Management Tools installation and usage guide (S)
- Keypair generation tool (M)
- CLI node management (M)
**Maintenance and governance**
 
- Network upgrade process (S)
- Mirror node upgrade process (S)
- Network configuration change process (S)
- Consensus node acceptance process (S)
- Consensus node eviction process (S)
**Observing the network state**
 
- Mirror node run setup guide (M)
- Mirror node hardware requirements (M)
- Connecting mirror node to a private network (S)
## 5. Quick wins
 
Several items in iterations 1 and 2 have a small first step that the community could propose now, without waiting for the rest of the item:
 
- Link builds.hedera.com and the public container registry from each release note, with checksums and an explanation of how to check a binary against the public build.
- State in each release note which mirror node, relay and block node versions it works with.
- Publish the key that signs the Node Management Tools installers, or re-sign them with a key that has not been revoked.
- Point the operator documentation to the security policy, and explain how an operator can apply for early notice of critical fixes.
- Correct the repository document that tells operators to put their own genesis key in a file the consensus node never reads.
- Make the consensus node warn when a network starts with the publicly known genesis key.
- Document the metrics and status endpoint the consensus node already serves.
## 6. Who can do the work, and where
 
The facts behind many iteration 1 items have to come from engineers who know the node internals. Once those facts exist, documentation, dashboards, AI skills and MCP servers suit community contributors and pull-request review. Lifecycle procedures for a private network, multi-organization launch, release signing and package pipelines, by contrast, need core engineering, and signing and pipelines also need Hedera's release infrastructure or an open replacement for it.
 
We assume the work happens in the open, which keeps decisions traceable: each item would be proposed to the Hiero TSC, incubated under Hiero Hackers or in open hiero-ledger repositories, discussed on the LFDT Discord, and listed on the public Hiero roadmap, where deployability would be a new item. Our deployment scripts and runbook can serve as a starting point for the launch and mirror node items and would go upstream through the normal Hiero review process.
 
The HIP-1495 components that the proposed path builds on, solo-operator and solo-provisioner, still live in the hashgraph organization, and solo-provisioner currently accepts contributions only from trusted maintainers. Their move to the hiero-ledger organization is approved but not yet complete, and would open them to the same process.
 
## 7. Checkpoints and success criteria
 
Each checkpoint should be passed by an engineer from outside the team that did the work, using published documentation only:
 
- **After iteration 1:** deploy a four-node network and a mirror node on virtual machines, with its own genesis key and each operator holding its own keys; then upgrade it to the next release and add and remove a node by following published procedures.
- **After iteration 2:** install the same network from signed packages, halt and restart it, and restore a node from backup. At this point an independent organization can deploy a network without our help, which is the SOW's Phase 3 acceptance test.
- **Iterations 3 to 6:** each package, from container image to marketplace image, is accepted when an outside engineer deploys a network from it.
In addition, the following should hold across all iterations:
 
- A new network cannot start with the publicly known genesis key without an explicit, visible override.
- Several organizations launch one network without any of them handling another's private keys.
- Everything we had to discover in source code during Phase 1 is in published documentation.
- All tooling and documentation are accepted upstream through the Hiero review process.
 
