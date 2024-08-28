# Technical Charter (the “Charter”) for Hiero a Series of LF Projects, LLC

This Charter sets forth the responsibilities and procedures for technical contribution to, and oversight of,
the Hiero open source project, which has been established as Hiero a Series of LF Projects,
LLC (the “Project”). 
LF Projects, LLC (“LF Projects”) is a Delaware series limited liability company.
All contributors (including committers, maintainers, and other technical positions) and other participants in the
Project (collectively, “Collaborators”) must comply with the terms of this Charter.

## 1. Mission and Scope of the Project

- a) The mission of the Project is to create and support a fully open source developer ecosystem of tools, libraries,
  and core capabilities of and around the Hedera public distributed ledger (DLT) and its unique Hashgraph algorithm.
  The Project supports the ecosystem of the Hedera network, a fast, fair, and secure public distributed ledger.
- b) The scope of the Project includes collaborative development under the Project License (as defined herein)
  supporting the mission, including documentation, testing, integration and the creation of other artifacts
  that aid the development, deployment, operation, or adoption of the open source project.
- c) The Project encourages the development of applications and core platform features that support an
  enterprise-grade Hedera network.
  Additionally, applications such as wallets, exchanges, explorers, bridges, SDKs, private ledgers,
  and cryptography, will be supported.

## 2. Values

- a) The Project shall strive to align to the following principles:
    - i) Fast is better than slow: The Project enables sub-projects to progress at high velocity to support
    aggressive adoption by users.
    - ii) Open: The Project is open, accessible, and operates independently of specific partisan interests.
    The Project accepts all contributors based on the merit of their contributions, and the Project’s
    technology must be available to all according to open source values.
    The technical community and its decisions shall be transparent.
    It shall at all times encourage and accept input from the community at large.
    - iii) Fair: The Project seeks to avoid undue influence and bad behavior by members and contributors.
    - iv) Strong technical identity: The Project will achieve and maintain a high degree of its own
    technical identity that is shared across the projects and the public stakeholder ecosystem.
    - v) Clear boundaries: The Project shall establish clear goals, and in some cases, what the
    non-goals of the Project are, to allow sub-projects to effectively co-exist,
    and to help the ecosystem understand where to focus for new innovation.
    - vi) Ecosystem Enhancing: The Project exists to strengthen the ecosystem using this Project’s software

## 3. Technical Steering Committee

- a) The Technical Steering Committee (the “TSC”) is responsible for all technical oversight of the
  open source Project.
- b) All meetings of the TSC are intended to be open to the public, and can be conducted electronically,
  via teleconference, or in person.
- c) The TSC members of the Project will be as set forth within the “TSC_MEMBERS.md” file within the
  Project’s code repository. 
- d) TSC projects generally will involve Maintainers, Committers, and Contributors: 
  - i) Contributors include anyone in the community that contributes code, documentation, or other
    technical artifacts to the Project;
  - ii) Committers are Contributors who have earned the ability to modify (“commit”) source code,
    documentation or other technical artifacts in a project’s repository; and
  - iii) Maintainers are Committers who have earned the right to vote on (1) promotion of Contributors
    to Committers; (2) promotion of Committers to Maintainers;
  (3) the removal of any Committer or Maintainer; (4) representation on the TSC;
  (5) other scenarios that require a vote for good governance of the sub-project.
- e) The Consensus Node project will additionally define a Project Lead role:
  - i) The Project Lead is a Maintainer who also has the ability to revert changes to the consensus node
    project unilaterally.
  - ii) The Project Lead is Dr. Leemon Baird. The Project Lead may delegate the role to another individual.
    If this is done, that individual will be listed in a file in the Consensus Node project.
- f) Participation in the Project through becoming a Contributor, Committer, and Maintainer is open to
  anyone so long as they abide by the terms of this Charter. 
- g) The TSC may (1) establish workflow procedures for the submission, approval, and closure/archiving
  of projects, (2) set requirements for the promotion of Contributors to Committer status,
  or Committers to Maintainer status, as applicable, and (3) amend, adjust, refine and/or eliminate the
  roles of Contributors, and Committers, and Maintainers, and create new roles, and publicly document any
  TSC roles, as it sees fit.
- h) TSC Members are expected to cover deep technical domains including consensus technologies,
  technical operations, tokenization, smart contracts, ecosystem applications such as wallets, exchanges, etc.
  The TSC shall consist of a total of nine (9) members (the “TSC Members”).
  Each TSC Member must meet the criteria set forth in 3.g.ii.
  The TSC Members shall otherwise be selected as follows:
  - i) Dr. Leemon Baird, inventor of the hashgraph algorithm, has a permanent seat on the TSC representing
    himself independent of any Related Parties. 
  - ii) Hedera Hashgraph LLC has a permanent seat on the TSC and shall appoint one (1) TSC Member to
    represent itself
  - iii) Graduated project Maintainers shall together elect three (3) TSC Members.
  - iv) All Contributors who have contributed within the past year to the Project, including any of
    its sub-projects, and/or any individual who has signed a CLA, or company who has signed a CCLA,
    shall be entitled to vote for one (1) “Contributor” seat on the TSC
  - v) The TSC shall define the procedure to elect one (1) “End User” to the TSC.
    An End User is defined as an individual of a company using projects from the Project ecosystem
    to build their products and services and/or an organization primarily consuming the Project software,
    rather than producing it.
    An initial End User representative may be included in the initial set of TSC Members. 
  - vi) The TSC Members defined in 3.f.i-3.f.v shall together elect two (2) additional TSC Members
  - vii) Each group identified in 3.f.i–vi (i.e., Dr. Leemon Baird, Hedera Hashgraph LLC, Graduated project
    Maintainers, and the TSC itself) is defined as a Selecting Group.
    - 1 If more than two (2) TSC Members would be from the same group of Related Parties (see Section 9),
      either at the time of election or from a later job change, they will jointly decide who should step down, or if
      there is no agreement, random lots shall be drawn. Dr. Leemon Baird represents himself and does not contribute
      toward this number.
    - 2 Each TSC Member may delegate their representation on the TSC to an alternate of their choosing, without respect
      to Related Parties. As with all TSC Members, the alternate must meet the requirements in 3.g.ii.
- i) Operating Model
  - i) The TSC may elect a TSC Chair, who will preside over meetings of the TSC and will serve until their resignation
    or replacement by the TSC.
    The TSC Chair, or any other TSC member so designated by the TSC, will serve as the primary communication contact
    between the Project and the LFDT and any staff assigned to the Project. 
  - ii) Nominees for the TSC shall:
    - 1 Commit that they have the available bandwidth to make the time to invest in the TSC,
    - 2 Demonstrate an advanced level of professional experience as engineers in the scope of the Project, and
    - 3 Operate neutrally in discussions and put the goals and success of the Project in balance with any particular
      sub-project governed by the TSC
  - iii) Nominations to the TSC
    - 1 Each individual with the right to nominate a member to the TSC may nominate up to two (2) people, at most
      one (1) of whom may be from the same group of Related Companies (see Section 9).
      Each nominee must agree to participate prior to being added to the nomination list.
    - 2 The TSC shall determine the process and timeline for the nominations, qualification, and election of TSC members
    - 3 A minimum of 14 calendar days shall be reserved for an Evaluation Period whereby TSC nominees may be contacted
      by members of the TSC.
  - iv) Constraints
    - 1 TSC Members shall serve two-year terms. Dr. Leemon Baird and Hedera Hashgraph LLC. have permanent seats.
    - 2 Non-permanent TSC members may be removed by a two-thirds vote of the other TSC members, with the impacted
      individual ineligible to participate in the vote.
    - 3 Permanent members may be removed for violation of the Project’s Code of Conduct pursuant to a review by the
      Series Manager.
    - 4 Any TSC member, including permanent members,  that misses three (3) consecutive meetings shall be automatically
      suspended from eligibility to vote until having attended two meetings consecutively.
      For avoidance of doubt, the suspended TSC member shall be eligible to vote in the second consecutive meeting.
- i) Responsibilities: The TSC will be responsible for all aspects of oversight relating to the Project, in
  coordination with any staff provided by the LFDT for the technical direction of the Project;
  - i) approving project or system proposals (including, but not limited to, incubation, deprecation, and changes to
    a sub-project’s scope);
  - ii) organizing sub-projects and removing sub-projects;
  - iii) creating sub-committees or working groups to focus on cross-project technical issues and requirements;
  - iv) appointing representatives to work with other open source or open standards communities;
  - v) establishing community norms, workflows, issuing releases, and security issue reporting policies;
  - vi) approving and implementing policies and processes for contributing (to be published in the CONTRIBUTING file)
    and coordinating with the series manager of the Project
    (as provided for in the Series Agreement, the “Series Manager”) to resolve matters or concerns that may arise as
    set forth in Section 7 of this Charter;
  - vii) discussions, seeking consensus, and where necessary, voting on technical matters relating to the code base
    that affect multiple projects; and
  - viii) coordinating any marketing, events, or communications regarding the Project.

## 4. TSC Voting

- a) While the Project aims to operate as a consensus-based community, if any TSC decision requires a vote to move the
  Project forward, the voting members of the TSC will vote on a one vote per voting member basis.
- b) Quorum for TSC meetings requires at least two thirds of all voting members of the TSC to be present.
  The TSC may continue to meet if quorum is not met but will be prevented from making any decisions at the meeting.
- c) Except as provided in Section 8.c. and 10.a, decisions by vote at a meeting require a majority vote of those in
  attendance, provided quorum is met. Decisions made by electronic vote without a meeting require a majority vote of all voting members of the TSC.
- d) In the event a vote cannot be resolved by the TSC, any voting member of the TSC may refer the matter to the
  Series Manager for assistance in reaching a resolution.

## 5. Compliance with Policies

- a) This Charter is subject to the Series Agreement for the Project and the Operating Agreement of LF Projects.
  Contributors will comply with the policies of LF Projects as may be adopted and amended by LF Projects, including,
  without limitation the policies listed at https://lfprojects.org/policies/.  
- b) The TSC may adopt a code of conduct (“CoC”) for the Project, which is subject to approval by the Series Manager.
  In the event that a Project-specific CoC has not been approved, the LF Projects Code of Conduct listed
  at https://lfprojects.org/policies will apply for all Collaborators in the Project.
- c) When amending or adopting any policy applicable to the Project, LF Projects will publish such policy, as to be
  amended or adopted, on its web site at least 30 days prior to such policy taking effect;
  provided, however, that in the case of any amendment of the Trademark Policy or Terms of Use of LF Projects, any such
  amendment is effective upon publication on LF Project’s web site.
- d) All Collaborators must allow open participation from any individual or organization meeting the requirements for
  contributing under this Charter and any policies adopted for all Collaborators by the TSC, regardless of
  competitive interests.
  Put another way, the Project community must not seek to exclude any participant based on any criteria, requirement,
  or reason other than those that are reasonable and applied on a non-discriminatory basis to all Collaborators
  in the Project community.
- e) The Project will operate in a transparent, open, collaborative, and ethical manner at all times.
  The output of all Project discussions, proposals, timelines, decisions, and status will be made open and easily
  visible to all except in matters related to security, where making information public could expose the Project
  to harmful actions. Any potential violations of this requirement should be reported immediately to the Series Manager.
- f) The TSC will abide by any and all required policies and procedures as defined by the LFDT

## 6. Community Assets

- a) LF Projects will hold title to all trade or service marks used by the Project (“Project Trademarks”),
  whether based on common law or registered rights.
  Project Trademarks will be transferred and assigned to LF Projects to hold on behalf of the Project.
  Any use of any Project Trademarks by Collaborators in the Project will be in accordance with the license from
  LF Projects and inure to the benefit of LF Projects.  
- b) The Project will, as permitted and in accordance with such license from LF Projects, develop and own all Project
  GitHub and social media accounts, and domain name registrations created by the Project community.
- c) Under no circumstances will LF Projects be expected or required to undertake any action on behalf of the Project
  that is inconsistent with the tax-exempt status or purpose, as applicable, of the Joint Development Foundation
  or LF Projects, LLC.

## 7. General Rules and Operations

- a) The Project will:
  - i) engage in the work of the Project in a professional manner consistent with maintaining a cohesive community,
    while also maintaining the goodwill and esteem of LF Projects, Joint Development Foundation and other partner
    organizations in the open source community; and
  - i) respect the rights of all trademark owners, including any branding and trademark usage guidelines.

## 8. Intellectual Property Policy

- a) Collaborators acknowledge that the copyright in all new contributions will be retained by the copyright holder
  as independent works of authorship and that no contributor or copyright holder will be required to assign
  copyrights to the Project. 
- b) Except as described in Section 7.c., all contributions to the Project are subject to the following: 
  - i) All new inbound code contributions to the Project must be made using Apache License, Version 2.0 available
    at http://www.apache.org/licenses/LICENSE-2.0  (the “Project License”). 
  - ii) All new inbound code contributions must also be accompanied by a Developer Certificate of Origin (http://developercertificate.org)
    sign-off in the source code system that is submitted through a TSC-approved contribution process which will bind
    the authorized contributor and, if not self-employed, their employer to the applicable license;
  - iii) All outbound code will be made available under the Project License.
  - iv) Documentation will be received and made available by the Project under the Creative Commons Attribution 4.0
    International License (available at http://creativecommons.org/licenses/by/4.0/). 
  - v) The Project may seek to integrate and contribute back to other open source projects (“Upstream Projects”).
    In such cases, the Project will conform to all license requirements of the Upstream Projects, including
    dependencies, leveraged by the Project.
    Upstream Project code contributions not stored within the Project’s main code repository will comply with the
    contribution process and license terms for the applicable Upstream Project.
- c) The TSC may approve the use of an alternative license or licenses for inbound or outbound contributions on an
  exception basis.
  To request an exception, please describe the contribution, the alternative open source license(s), and the
  justification for using an alternative open source license for the Project.
  License exceptions must be approved by a two-thirds vote of the entire TSC. 
- d) Contributed files should contain license information, such as SPDX short form identifiers, indicating the
  open source license or licenses pertaining to the file.

## 9. Related Parties

- a) Definitions:
  - i) “Subsidiaries” shall mean any entity in which a TSC Member owns, directly or indirectly, more than fifty percent
    of the voting securities or membership interests of the entity in question.
  - ii) “Related Party” shall mean any person or entity which controls or is controlled by a TSC Member or which,
    together with a TSC Member, is under the common control of a third party, in each case where such control results
    from either (1) ownership, either directly or indirectly, of more than fifty percent of the voting securities
    or membership interests of the entity in question, or (2) a relationship that is effectively one of employment,
    such as where an individual has created an entity as an independent contractor for regulatory or tax purposes
    but takes direction exclusively from a TSC Member. 
  - iii) “Related Parties” are entities that are each a Related Party of a TSC Member.

## 10. Amendments

- a) This charter may be amended by a two-thirds vote of the entire TSC and is subject to approval by LF Projects; and
- a) Changes to the Permanent Seat definitions must be amended by a unanimous vote of the entire TSC for actions
  materially detrimental to the Project or in opposition to this Charter and its Values, subject to approval by
  LF Projects. The Permanent Seat holder may not participate in this vote.
