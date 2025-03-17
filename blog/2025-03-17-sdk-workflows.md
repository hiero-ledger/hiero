# SDK workflows

This file contains several SDK workflows and ideas for discussion in the SDK community.

## How protobuf should be handled

The following best practices should be used in SDKs:

- SDK repositories should not contain any protobuf files. All protobuf files should be on "server side" projects like consensus node
- SDKs can use protobuf files from consensus node, mirror node and block node. All those nodes have a GRPC endpoint that can be used by an SDK to communicate / interact with an node.
- All SDKs should use the protobuf files from "server side" projects to generate language specific SDK code
- All SDKs should following this pattern:
  - As a build step the SDK should download the protobuf files from the "server side" projects and generate language specific code out of them
  - The downloaded protobuf files should not be added to git. Maybe a folder (like protobuf in the root) is used and added to .gitignore or a temp folder is used. (Question: should / can be specify it more concrete)
  - If we publish build artifacts for the SDK, the generated code should not be committed. There are reasons, why the code must be committed.
    For Go, the GitHub repo is used as dependency for other projects and therefore it makes sense to commit the code, for Java that is not needed an it would make sense to create the code in the build and not commit it.
  - When downloading the protobuf files from the "server side" projects we always use a TAG.
    By doing so we have a fix version of the protobuf that is used. This is essential for releases.
    For some developer usecases it might make sense to use a branch or specific commit instead of a TAG.
    The script that does it should be flexible enough but should always need a param.
  - The information about the "server side" project versions (tag/branch/commit) must be stored in a (text) file of a release

**Question:** It looks like all protobuf files can be found in the conensus-node repo today, including `transaction_list.proto`, `consensus_service.proto`, and `mirror_network_service.proto`. 
In the code of the consensus-node `transaction_list.proto` is never used. Is that the correct approach and SDKs only need to depend on protobuf files found in consensus-node or do we need to depend on mirror-node and block-node?

## CI Tests with Solo / Local-node

SDKs use `hedera-local-node` in their CI workflows to test and verify SDK functionality.
Solo (and the GitHub action, which is already a part of Hiero) are currently being integrated into the C++ SDK.
Once functionality there is verified, we can move to use the Solo GitHub action in all SDKs.

## Naming best practices

When moving the SDK projects from Hedera to Hiero we have not changed the naming and usage of the name "Hedera" and "Hashgraph" in documentation (markdown and code). That should be done as a next step and we want to provide some best practices:

- It is not our goal to remove the word "Hedera" 100%, kit is our goal to rewrite the documentration to be technical correct from a Hiero perspective.
  The most important goal is that the documentation matches to the context where it is used.
  As an example in the project "Mainnet" or "testnet" are not defined.
  We should use "Hedera mainnet" or "Hedera testnet" in those cases if we need to mention those explicit networks.
- While we want the documentation to be unbranded (not Hedera specific) it is not forbidden to use the name "Hedera" and/or "Hashgraph".
  If we for example have a sentance "The following code shows how that can be achived on Mainnet" it will be fine to rewrite that sentence to "The following code shows how that can be achived on Hedera Mainnet".
- Whenever a documentation is talking about the "Hedera network" in general, we should rename it to "Hiero based network".
  Examples: "... any proto messages that are sent to or from any Hedera network." should be rewritten to "... any proto messages that are sent to or from any Hiero based network."
  "This represents a network of Hedera nodes" should be rewritten to "This represents a network of Hiero nodes"
- We have a LFDT discord (https://discord.gg/qEEN8JYQ) that should be used instead of Hedera discord.

**Question:** While the hips repo will me migrated to Hiero in near future it is not clear right now how links to https://hips.hedera.com should be handled.
Will we have hips.hiero.org in near future and change the links in SDK docs to that domain?

## Refactoring of code to be more unbranded / vendor neutral

In best case we do not have "Hedera" in any class/type names or namespaces. While changing that can end in breaking changes we will do the fiollowing as best practices:

- If "Hedera" or "Hashgraph" is used in names of provate API we should change it to "Hiero"
- If "Hedera" or "Hashgraph" is used in public API we should not change it now (if possible) and do that as a single change once everything else has been done (only 1 breaking change release instead of many)
- Every usage of "Hedera" and or "Hashgraph" in samples and tests should be refactored
- If code logic is Hedera specific (like `Client.forMainnet()` or `Client.forTestnet()`) we need to deprecate that code and provide a generic approach.
  The documentation of the deprecated code should link to the new approach.
- Changing Hedera specific code to a general approach should be defined globally over all SDKs if possible.
  By doing so the same patterns can be used. (see https://github.com/hiero-ledger/tsc/issues/98 as a sample).
  Once we have an SDK metadata repository we should define those new APIs in thatb repo before implementing them.
- In the samples most SDKs use environment variables like `HEDERA_NETWORK`. We should change them (`HIERO_NETWORK` in that case).
- Any other strings that reference Hedera should be changed in accordance to our best practices.
- Solidity files exist in the SDKs to provide basic smart contracts with which the SDK integration tests can interact.
  They reference Hedera either in the name, or in the comments. We should rename all that to "Hiero"

