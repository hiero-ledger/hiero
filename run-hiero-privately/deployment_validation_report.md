# Deployment Validation Report
 
*Independent Hiero Network Deployment, Phase 1 · MAKE Group, LLC for Hedera Hashgraph, LLC · October 2026*
 
## 1. What we set out to do
 
As the SOW requires, MAKE Group set out to deploy a complete Hiero network using only public software and documentation, and to record every step along the way. The target was a self-contained network with its own identity and keys, not connected to Hedera mainnet or testnet and not based on Hashgraph's HashSphere offering. Throughout, we worked to the operator profile agreed with Hedera at the start of the project: an experienced infrastructure engineer with some blockchain familiarity and no Hedera knowledge. Wherever public documentation ran out, we read public source code or used an AI assistant on the public repositories. Section 4 lists each of these steps, because they are the points where a typical operator would stop.
 
## 2. The two deployments
 
We built two networks, deliberately taking different routes. Deployment A is a Solo test network, started by following Hedera's local development guide as a baseline. Deployment B is a private four-node network with its own identity and keys, built on virtual machines. The table below compares them:
 
| | A. Kubernetes with Solo | B. Virtual machines, Solo not used to deploy |
|---|---|---|
| **Infrastructure** | One AWS EC2 host (Ubuntu), local Kubernetes cluster created by Solo | AWS EC2: 4 consensus node hosts (16 GB), 1 mirror node and explorer host (8 GB), Ubuntu 24.04, in one AWS account, with the four operators simulated by one team |
| **Software** | Solo 0.91.0, consensus node v0.76.4, mirror node v0.161.0, relay v0.78.1, explorer v26.2.0 | Consensus node v0.76.4 release builds, mirror node v0.163.0, explorer v26.2.0; node configuration templates taken from Solo's repository |
| **Network identity** | Solo's defaults, including the publicly known genesis key | Own ledger ID, chain ID and genesis key |
| **Time to a working network** | Under 1 working day | A few working days the first time, including research and one rebuild; about one working day to repeat and verify with our runbook |
| **Steps recorded in** | Hedera's local development guide, followed as written | Hiero Private Network Runbook, with its scripts, attached as a separate artifact |
 
**Steps, deployment A:**
 
1. Install Node.js and Docker, add the user to the docker group, and install Solo from npm. Solo provisions everything else.
2. Deploy a network with one consensus node, the mirror node, relay and explorer, following Hedera's local development guide. Solo creates the local Kubernetes cluster itself.
3. Validate the network with the checks in the guide.
**Steps, deployment B:**
 
1. Prepare each host.
2. Each operator generates its own node keys, moves its admin key offline and publishes only a public bundle.
3. One operator acts as the coordinator. It builds the genesis roster from the public bundles and creates the genesis key, and every operator then checks the roster hash.
4. Download and verify the release build, configure each node and start it as a service.
5. Connect a mirror node: it pulls each node's record files over a read-only sync, and its address book is built from the genesis file. Add the explorer.
6. Validate.
## 3. What we validated
 
We then validated the virtual-machine network against the following checks:
 
| Check | Result |
|---|---|
| Consensus across 4 nodes, transactions submitted through every node | Passed |
| Transfers and consensus service messages | Passed |
| Token service and a Solidity smart contract called through each node | Passed |
| Identical results read back from every node and from the mirror node | Passed: 24 of 24 checks in each of 4 runs, and 7 of 7 mirror checks |
| Our own genesis key controls the treasury, not the publicly known one | Passed after a rebuild (see below) |
| One node stopped and restarted while the network runs | Passed, back in about 40 s with no downtime |
| Several days of idle running | Failed: halted after 3.8 days when the disks filled (see below) |
 
**The genesis key incident.** We built the virtual-machine network twice, first with our runbook's scripts and later with Hedera's Node Management Tools. The first network started with the publicly known genesis key controlling the treasury account, because the repository's configuration document names a file that the node never reads. Only a client test that tried to use our own key revealed the problem, and the fix was a full rebuild from genesis. An operator without that test would not have noticed. The Node Management Tools build, made with the corrected procedure, passed the key check the first time.
 
**The disk incident.** The network built with Hedera's Node Management Tools ran idle for 3.8 days and then stopped reaching consensus. Event streaming, which is on by default, had written about 5 GB per node per day and filled the 30 GB disks. One node exited and was not restarted, a second stopped contributing, and the network halted. No component raised an alert, and the failure showed only in the platform status metric and the node logs. Our runbook now turns event streams off, sizes disks at 100 GB and lists the alerts an operator should configure. We have not yet repeated the multi-day run with these changes.
 
Our Hiero Private Network Test Report, with the full results for the virtual-machine deployment, is attached as a separate artifact.
 
## 4. What we had to figure out
 
Hedera asked for a record of every manual step, every workaround and every place where Solo supplied missing knowledge. Each row below marks one point where public documentation was not enough.
 
| What we needed | How we found it |
|---|---|
| How to start a new network at all | Operator docs cover only Council onboarding. We read Solo and consensus node sources. |
| Where to download a release, and what it needs to run | Download location and layout found only in Solo's scripts. Builds are published there before each GitHub release, but nothing links to them. The required Java version found in build files. |
| Node keys: types, sizes, file names, how to generate them | Copied from Solo's key manager. File names are off by one from the node ID. The repository's own key tool is a development tool that produces the same keys for the same node ID every time, so it must not be used for a real network. The Node Management Tools generate random keys but protect them with a fixed store password. |
| The genesis roster that starts a multi-node network | Its format exists only in Solo's code and a developer example. |
| Where the genesis key goes | Only one configuration file works, and a repository document names a different one (see the incident above). |
| Running a node outside Kubernetes | No guide for a private network. An AI assistant reconstructed what Solo does inside Kubernetes, and the configuration templates still come from Solo's repository, with test values such as `hedera.profiles.active=TEST` and `netty.mode=TEST`.<br><br>Hedera's Node Management Tools, an installer for running a node, are built for mainnet nodes. They are referenced only from the Council requirements page and have no usage guide. When we built the virtual-machine network with them, they worked only with manual workarounds: the license prompt hangs without a terminal, prerequisites are neither installed nor checked, memory defaults are sized for mainnet (a 118 GB heap), the upgrade watcher fails until a missing logs folder is created, and a node that stops is not restarted. |
| Connecting a mirror node to a private network | Docs cover only Hedera's networks. Several required settings found in mirror node source and by trial. We built the mirror's address book from the genesis file ourselves and moved record files with our own sync. |
| Whether an idle network is alive | Blocks are written only for transactions, so an idle healthy network looks stalled in the explorer. We checked node status metrics, rounds and state signatures on the nodes instead. |
| Running Solo on a fresh Ubuntu host | The deployment failed until the user was added to the docker group. |
 
In addition to the two deployments above, our autonomous AI agent deployed a four-node Solo network without help from the team. It gave the network its own identity and genesis key, added a fifth node and upgraded all nodes to a newer release. Here are some findings from that run:
 
- Adding the fifth node through a governed change took about five minutes, and the upgrade from v0.76.4 to v0.77.2 took about three. After both, the network was still controlled by its own genesis key.
- Giving the network its own identity and genesis key meant working out the settings from source code. The genesis key setting is documented only in the consensus node's source code, and Solo needs the same key in a separate variable to operate the network it created.
- In Solo 0.91.0, the multi-node command in Solo's quickstart deployed one node and still reported success, because it dropped the node count. The current Solo source still behaves this way.
## 5. Conclusion
 
A private Hiero network can be deployed and operated with public software. A network with its own identity and keys cannot, however, be built from public documentation alone: our virtual-machine deployment depended on reading source code, working out with AI assistance how Solo builds a network, or working around silent failures. Our operator runbook and scripts, written with the help of an AI assistant and optimized for human readers, now make the result repeatable for us, with each operator bringing up its own node and sharing only public data with the coordinator. Whether another team can reproduce it from the attached runbook would be a good test for the next phase.
 
Measured against our definition, neither network is a production-ready deployment. An operator has no way to be confident that the setup did not miss a critical step that would compromise the network. Our own first attempt started with a publicly known key controlling the treasury, and only a client test revealed it. The networks also cannot be monitored properly, because the explorer cannot tell an idle network from a stalled one. Finally, it is not clear how to maintain a network safely. Without written procedures for upgrades and recovery, an operator cannot tell whether an upgrade has left the network in a correct state, and nothing yet describes how several organizations would share control of the treasury key.
 
