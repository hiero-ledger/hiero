### Primary Focus

Coding

### Description

With the move of the Hedera codebase to Hiero, the project became a much broader scope.
The SDKs that are currently available are all coming with the limited scope to Hedera and the Hedera network.
Next to that some of the SDKs are not created in the best possible way for the underlying programming language.
Therefore SDK usage is from time to time hard to understand and developer can run into issues.
Next to that with all the changes came to Hiero over the last years, including the modularization of the consensus node and the support for custom services and transactions, the architecture and public API of the SDKs is outdated at several points.
Since we want to provide a great developer experience for our users, the current SDKs are not suitable for the future.

Based on all these factors, we started to invest in prototyping a possible new architecture and API for the future of our SDKs.
That work is currently named "SKD V3" and happens in the [SDK collaboration hub of Hiero](https://github.com/hiero-ledger/sdk-collaboration-hub).
Here we currently define language agnostic APIs and language best practices for architecture and APIs of the future SDKs.
Regarding general language agnostic API design our [API guideline](https://github.com/hiero-ledger/sdk-collaboration-hub/blob/main/guides/api-guideline.md) is a good starting point.
based on that guideline we already started to create a [draft of the new SDK architecture and APIs](https://github.com/hiero-ledger/sdk-collaboration-hub/tree/main/v3-sandbox/prototype-api).

As a next step we need to create PoCs for the new SDK architecture and APIs in multiple languages.
This is the main goal of this mentorship program project:
- Create PoCs for the new SDK architecture and APIs in multiple languages
- Create a roadmap for the new SDK architecture and APIs
- Contribute to our guidelines and documentation to make the new SDK architecture and APIs more accessible to developers
- Check how AI (like claude code or Github Co-Pilot) can be used as a helpful tool when working on SDK code with all our guidelines and documentation in context

### Learning Objectives

- Understand Hiero and how Hiero based networks work
- Undertand the Communication between a Hiero network (a consensus node and a mirror node) and a client
- Understand the current SDKs of Hiero and how they work
- Learn how to create future proof and non breaking APIs
- Learn how to use language features like generics and type inference to create the best possible SDKs

### Expected Outcome and Deliverables

The successful completion of this project will result in at least 3 SDK V3 PoCs in multiple languages.
Next to that we hope that contributions can be done to the general API guidelines and specifications.

### Relation to LF Decentralized Trust and impact on the community

The contribution will be done to the [Hiero SDK project](https://github.com/hiero-ledger/sdk-collaboration-hub) project is a subproject of the graduated Hiero project.
Our main goal is to provide an awesome developer experience for our users.
This will have a huge impact on the community since it will enable developers to use the new SDKs and APIs in a more efficient way.
Especially the usage and understanding for new developers will be improved.

### Recommended Skills

- Proficiency in at least one modern programming language, such as Java, JavaScript/TypeScript, Go, Rust, Swift, Python, or C++ (languages used for Hiero SDKs)  ￼
- Understanding of software architecture and API design, including principles for building stable and maintainable APIs
- Familiarity with SDK development concepts, client libraries, and developer tooling
- Experience with Git (+ GitHub) and collaborative open source development workflows
- Understanding of type systems, generics, and modern language features
- Interest in developer experience (DX) and usability of APIs
- Experience with documentation and developer guides is a plus
- Curiosity about AI-assisted development tools (e.g., GitHub Copilot or Claude Code)
- Experience working with Protobuf / gRPC APIs are a big plus
- Familiarity with testing frameworks and CI pipelines are a big plus
- Prior contributions to open source projects are a big plus
- Experience building client libraries or SDKs are a big plus
- Experience with Hiero SDKs are a big plus

### Mentor(s) Names and Contact Info

Name: Hendrik Ebbers
Email: hendrik.ebbers@hashgraph.com
Company affiliation: Hashgraph

Name: 
Email: 
Company affiliation: 

### Additional Information

TODO