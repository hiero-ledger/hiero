### Primary Focus

Coding

### Description

The hiero-eneterprise-java project provides a layer on top of Hiero SDKs to integrate hiero functionality in enterprise java applications that are based on frameorks like JakartaEE, Microprofile, Quarkus or Spring Boot.
Instead of just defining the SDK API the project creates a layer on top of it by providing services and repositories for a more easy and integrated interaction with an hiero based network.

The project invests a lot in rich and easy to useable APIs to interact with smart contracts.
While deploying smart contracts and calling functions of contracts is already part of the project, the log and event functionality of smart contracts is missing.
This functionality allows smart contract functionalities to share informations with external observers of the contract.
At Hiero events and logs of smart contracts can be accessed by the mirror node.
Sadly the workflow is very complexe and now easy to use API exists to easily receive events for a specific smart contract instance.

This project should extend hiero-enterprise-java by providing a new public API and implementation for events and log observation of smart contracts.

### Learning Objectives

- Understanding smart contracts and solidy as smart contract languages
- Understanding best practices for creating smart contracts
- Deploy smart contracts and interact with smart contracts on an Hiero based network
- Understand the Hiero SDKs
- Understand the Hiero Mirror Node
- Learn about hiero-eneterprise-java and best pratices for providing functionality to enterprise Java frameworks

### Expected Outcome and Deliverables

The successful completion of this project will result in the new code and modules in the hiero-eneterprise-java project.
Next to that tests, documentation and samples of the new functionallity are part of the expected outcome.

Mostly all of that will be part of the hiero-eneterprise-java project (excluding stand alone examples).

We expect that events and logs of any deployed smart contracts can be observed by the API (by using callbacks).



### Relation to LF Decentralized Trust and impact on the community

The contribution will be done to the hiero-eneterprise-java project what is a subproject of the graduated Hiero project.
The successfull implementation of the project will directly allow developers a better way to interact with smart contracts.
Next to that it will allow the Hiero community to get a lot of input on how future SDKs should integrate interaction with Mirror node and smart contract events / logs.

### Recommended Skills

- Knowledge of Java and Java enterprise frameworks (like Spring Boot)
- Understanding web services and design of service interfaces (HTTP, RESTful interfaces, gRPC, OpenAPI)
- Experience with Hiero (in best the SDKs) are a big plus
- Experience with smart contracts and solidity are a big plus

### Mentor(s) Names and Contact Info

Name: Hendrik Ebbers
Email: hendrik.ebbers@hashgraph.com
Company affiliation: Hashgraph

Name:
Email:
Company affiliation:

### Additional Information

TODO