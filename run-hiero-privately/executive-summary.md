# Executive Summary
 
*Independent Hiero Network Deployment, Phase 1 · MAKE Group, LLC for Hedera Hashgraph, LLC · October 2026*
 
At Hedera's request, MAKE Group assessed whether an independent organization can deploy and run a production Hiero network using only public software and documentation. The short answer is "not yet". The available public material focuses on the components that give access to network data, such as the mirror node, block node and JSON-RPC relay. However, it does not fully cover running a private network or the consensus node it requires. The likely reason is that Hiero has so far run as Hedera's permissioned network, where Hedera's own team installs, configures and upgrades the nodes together with the Council. As a result, a good deal of the knowledge needed to run a private network has never had a reason to be published.
 
In our assessment, we defined a production network as one that several independent organizations operate jointly and securely, and can monitor, upgrade, recover and govern without help from the Hiero team. We evaluated readiness from the perspective of an experienced infrastructure engineer with no prior Hiero background, who needs to set up a private Hiero network using only public material.
 
During the exercise, we started a Solo test network as a baseline, and then launched a private four-node network with our own identity and keys, running each consensus node on its own virtual machine. Solo's documentation was enough to start the test network. For the virtual-machine network, we used an AI assistant to work out how to put a network together from the source code of Solo and the consensus node. Without it, reaching the same result would have taken considerably longer.
 
We documented our experience and assessment in the attached Deployment Validation Report and Technical Assessment Report. We also evaluated the Hiero ecosystem against what such an engineer would typically expect to find, and recorded the results in the attached Gap Analysis and its register.
 
Across all components, we checked 125 items and found 95 gaps, 15 of which we consider must-haves. The must-haves fall into three areas:
 
- **Launching a private network.** No guide explains how several organizations start a network together while each keeps its own keys, how to set up and size a consensus node, or how to use the available tools, which are built for local test networks or for Hedera mainnet. An operator has to reconstruct these steps from source code, and a mistake can leave the network controlled by a publicly known key, as happened on our first attempt.
- **Maintenance and governance.** Hiero has the mechanisms for upgrades, configuration changes and admitting or removing nodes, but a private network has no written procedure for using them. Every change would be improvised, and an upgrade that leaves nodes on different versions can halt the network.
- **Observing the network state.** The mirror node documentation covers only Hedera's own networks, and no guide explains how to connect a mirror node to a private network. Without one, a private network has no network explorer or JSON-RPC relay, and applications built with the client SDKs can submit transactions but cannot read the network's history.
Fortunately, most of these gaps can be closed without changes to the protocol, and many only require documenting what already works. For example, our virtual-machine deployment showed that several organizations can already start a network together, and only the written procedure is missing.
 
Assuming the work would be done in the open by the community or by independent contractors, we grouped the gaps into iterations, so that items within each iteration can be prioritized and addressed in parallel:
 
- **Iteration 1, the bare minimum to run a private network (27 gaps):** operator guides, upgrade and membership procedures, metrics and health, and key and node tooling. About two thirds of them are documentation, most of it small.
- **Iteration 2, a complete foundation (13 gaps):** signed OS packages, vulnerability announcements, and halt, recovery and backup procedures.
- **Iterations 3 to 6 (55 gaps):** container images built from the iteration 2 packages, Kubernetes charts and operators, marketplace images, deeper monitoring, testing and convenience tooling.
The suggested iterations follow the natural evolution of software distribution, from signed builds to OS packages, and then to container images and Kubernetes. However, judging by what we have observed, Hedera may arrange them differently, for example by bringing the Kubernetes items forward. With that in mind, we populated iterations 1 and 2 with items that would be needed on every route, so work on them can start while Hedera is still choosing the preferred deployment track.
 
A few decisions are left with Hedera:
 
- Whether the suggested order of iterations aligns with Hedera's vision.
- Whether any non-public tooling can be opened, which would shrink the affected items.
- Which work suits community contributors and which needs funded engineering.
- Where the work should live so operators can find it.
Once these decisions are made, we propose to estimate the selected iterations together with Hedera as the first step of the next phase.
 
