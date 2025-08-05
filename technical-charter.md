# Technical Charter (the "Charter") for Hiero a Series of LF Projects, LLC
> Adopted September 16, 2024
> Amended July 7, 2025

This Charter sets forth the responsibilities and procedures for technical contribution to, and oversight of, the Hiero
open source project, which has been established as Hiero a Series of LF Projects, LLC (the “Project”).  LF Projects, LLC
(“LF Projects”) is a Delaware series limited liability company. All contributors (including committers, maintainers, and
other technical positions) and other participants in the Project (collectively, “Collaborators”) must comply with the
terms of this Charter.

1. **Mission and Scope of the Project**

   1. The mission of the Project is to create and support a fully open source developer ecosystem of tools, libraries,
      and core capabilities of and around the Hedera public distributed ledger (DLT) and its unique Hashgraph algorithm.
      The Project supports the ecosystem of the Hedera network, a fast, fair, and secure public distributed ledger.
   
   2. The scope of the Project includes collaborative development under the Project License (as defined herein)
      supporting the mission, including documentation, testing, integration and the creation of other artifacts that aid
      the development, deployment, operation, or adoption of the open source project.
   
   3. The Project encourages the development of applications and core platform features that support an enterprise-grade
      Hedera network. Additionally, the Project seeks to enable  the development of applications such as wallets,
      exchanges, explorers, bridges, SDKs, private ledgers, and cryptography, which help maintain and enhance the
      network's capabilities.

2. **Values**

    1. The Project shall strive to align to the following principles:
   
       1. Fast is better than slow: The Project enables sub-projects to progress at high velocity to support aggressive
          adoption by users.
       
       2. Open: The Project is open, accessible, and operates independently of specific partisan interests. The Project
          accepts all contributors based on the merit of their contributions, and the Project’s technology must be
          available to all according to open source values. The technical community and its decisions shall be
          transparent. It shall at all times encourage and accept input from the community at large.
       
       3. Fair: The Project seeks to avoid undue influence and bad behavior by members and contributors.
       
       4. Strong technical identity: The Project will achieve and maintain a high degree of its own technical identity
          that is shared across the projects and the public stakeholder ecosystem.
       
       5. Clear boundaries: The Project shall establish clear goals, and in some cases, what the non-goals of the
          Project are, to allow sub-projects to effectively co-exist, and to help the ecosystem understand where to
          focus for new innovation.
       
       6. Ecosystem Enhancing: The Project exists to strengthen the ecosystem using this Project’s software

3. **Technical Steering Committee**

    1. The Technical Steering Committee (the “TSC”) is responsible for all technical oversight of the open source
       Project.
   
    2. All meetings of the TSC are intended to be open to the public, and can be conducted electronically, via
       teleconference, or in person.
   
    3. The TSC members of the Project will be as set forth within the “TSC_MEMBERS.md” file within the Project’s code
       repository.
   
    4. TSC projects generally will involve Maintainers, Committers, and Contributors:
   
       1. Contributors include anyone in the community that contributes code, documentation, or other technical
          artifacts to the Project;
       
       2. Committers are Contributors who have earned the ability to modify (“commit”) source code, documentation or
          other technical artifacts in a project’s repository; and
       
       3. Maintainers are Committers who have earned the right to vote on (1) promotion of Contributors to Committers;
          (2) promotion of Committers to Maintainers; (3) the removal of any Committer or Maintainer; (4) representation
          on the TSC; (5) other scenarios that require a vote for good governance of the sub-project.
       
    5. The Consensus Node project will additionally define a Project Lead role:
   
       1. The Project Lead is a Maintainer who also has the ability to revert changes to the consensus node project
          unilaterally.
       
       2. The Project Lead is Dr. Leemon Baird. The Project Lead may delegate the role to another individual on a
          temporary, time limited, basis, not to exceed fourteen (14) days. Such delegation is limited to no more than
          six (6) times in any given calendar year. If this is done, that individual will be listed in a file in the
          Consensus Node project.
       
       3. For the avoidance of doubt, the Project Lead role within the Consensus Node sub-project automatically
          terminates when Leemon Baird’s participation in that role terminates and the governance of the Consensus Node
          sub-project shall revert to the normal governance processes defined in this charter.
       
    6. Participation in the Project through becoming a Contributor, Committer, and Maintainer is open to anyone so long
       as they abide by the terms of this Charter.
   
    7. The TSC may (1) establish workflow procedures for the submission, approval, and closure/archiving of projects,
       (2) set requirements for the promotion of Contributors to Committer status, or Committers to Maintainer status,
       as applicable, and (3) amend, adjust, refine and/or eliminate the roles of Contributors, and Committers, and
       Maintainers, and create new roles, and publicly document any TSC roles, as it sees fit, so long as such rules
       remain compliant with the terms of this charter.
   
    8. TSC Members are expected to cover deep technical domains including consensus technologies, technical operations,
       tokenization, smart contracts, ecosystem applications such as wallets, exchanges, etc. The TSC shall consist of a
       total of nine (9) members (the “TSC Members”). Each TSC Member must meet the criteria set forth in **3.ix.b**.
       The TSC Members shall otherwise be selected as follows:
   
       1. Dr. Leemon Baird, inventor of the hashgraph algorithm, has a permanent seat on the TSC representing himself
          independent of any Related Parties.
       
       2. For the first three (3) years following the inception of the Project (the “Startup Period”), the
          multi-stakeholder governing body of the Hedera network (currently incorporated as “Hedera Hashgraph, LLC”) has
          a transitional seat on the TSC and shall appoint one (1) TSC Member to represent itself.
       
       3. All Maintainers of the Project, including any of its sub-projects, shall together elect three (3) TSC Members.
       
       4. All Contributors who have contributed within the past year to the Project, including any of its sub-projects,
          will be entitled to vote for one (1) “Contributor” seat on the TSC.
       
       5. The TSC shall define the procedure to elect one (1) “End User” to the TSC. An End User is defined as an
          individual of a company using projects from the Project ecosystem to build their products and services and/or
          an organization primarily consuming the Project software, rather than producing it. An initial End User
          representative may be included in the initial set of TSC Members.
       
       6. The TSC Members defined in **3.viii.a to 3.viii.e** shall together elect two (2) additional TSC Members
          during the Startup Period and three (3) additional TSC Members following the Startup Period.
       
       7. Each group identified in **3.viii.a to 3.viii.e** (i.e., Dr. Leemon Baird, Hedera Hashgraph, LLC, Maintainers
          of Graduated projects, and the TSC itself) is defined as a Selecting Group.
       
          1. If more than two (2) TSC Members would be from the same group of Related Parties (see Section 9), either at
             the time of election or from a later job change, they will jointly decide who should step down, or if there
             is no agreement, random lots shall be drawn. Dr. Leemon Baird represents himself and does not contribute
             toward this number.
          
          2. Each TSC Member may delegate their representation on the TSC to an alternate of their choosing, without
             respect to Related Parties, on a temporary, time limited, basis, not to exceed fourteen (14) days. Such
             delegation is limited to no more than six (6) times in any given calendar year As with all TSC Members, the
             alternate must meet the requirements in **3.ix.b.**
          
    9. Operating Model
   
         1. The TSC may elect a TSC Chair, who will preside over meetings of the TSC and will serve until their
            resignation or replacement by the TSC. The TSC Chair, or any other TSC member so designated by the TSC, will
            serve as the primary communication contact between the Project and the LFDT and any staff assigned to the
            Project.
       
         2. Nominees for the TSC shall:
       
            1. Commit that they have the available bandwidth to make the time to invest in the TSC,
            
            2. Demonstrate an advanced level of professional experience as engineers in the scope of the Project, and
            
            3. Operate neutrally in discussions and put the goals and success of the Project in balance with any
               particular sub-project governed by the TSC
            
         3. Nominations to the TSC
       
            1. Each individual with the right to nominate a member to the TSC may nominate up to two (2) people, at most
               one (1) of whom may be from the same group of Related Companies (see Section 9). Each nominee must agree
               to participate prior to being added to the nomination list.
            
            2. The TSC shall determine the process and timeline for the nominations, qualification, and election of TSC
               members
            
            3. A minimum of 14 calendar days shall be reserved for an Evaluation Period whereby TSC nominees may be
               contacted by members of the TSC.
            
         4. Constraints
       
            1. TSC Members shall serve two-year terms. Dr. Leemon Baird has a permanent seat (the "Baird Seat").
            
            2. With the exception of TSC members appointed through subsections **3.viii.a to 3.viii.e**, TSC members
               may be removed by a two-thirds vote of the other TSC members, with the impacted individual ineligible to
               participate in the vote.
            
            3. Permanent members may be removed for violation of the Project’s Code of Conduct pursuant to a review by
               the Series Manager.
            
    10. Responsibilities: The TSC will be responsible for all aspects of oversight relating to the Project, in
        coordination with any staff provided by the LFDT for the technical direction of the Project;
   
        1. approving project or system proposals (including, but not limited to, incubation, deprecation, and changes to
           a sub-project’s scope);
        
        2. organizing sub-projects and removing sub-projects;
        
        3. creating sub-committees or working groups to focus on cross-project technical issues and requirements;
        
        4. appointing representatives to work with other open source or open standards communities;
        
        5. establishing community norms, workflows, issuing releases, and security issue reporting policies;
        
        6. approving and implementing policies and processes for contributing (to be published in the CONTRIBUTING file)
           and coordinating with the Series Manager of the Project (as provided for in the Series Agreement, the “Series
           Manager”) to resolve matters or concerns that may arise as set forth in Sections **5.v and 8** of this
           Charter;
        
        7. discussions, seeking consensus, and where necessary, voting on technical matters relating to the code base
           that affect multiple projects; and
        
        8. coordinating with LFDT and/or other stakeholders who lead any marketing, events, or communications regarding
           the Project, as appropriate.
        
4. **TSC Voting**

   1. While the Project aims to operate as a consensus-based community, if any TSC decision requires a vote to move the
      Project forward, the TSC will vote on a one vote per member basis.
   
   2. Quorum for TSC meetings requires at least two thirds of all members of the TSC to be present. The
      TSC may continue to meet if quorum is not met but will be prevented from making any decisions at the meeting.
   
   3. Except as provided in Section **8.iii. and 10.i**, decisions by vote at a meeting require a majority vote of
      those in attendance, provided quorum is met. Decisions made by electronic vote without a meeting require a
      majority vote of the TSC.
   
   4. In the event a vote cannot be resolved by the TSC, any member of the TSC may refer the matter to the Series
      Manager for assistance in reaching a resolution.
   
5. **Compliance with Policies**

   1. This Charter is subject to the Series Agreement for the Project and the Operating Agreement of LF Projects.
      Contributors will comply with the policies of LF Projects as may be adopted and amended by LF Projects, including,
      without limitation the policies listed at https://lfprojects.org/policies/.
   
   2. The TSC may adopt a code of conduct (“CoC”) for the Project, which is subject to approval by the Series Manager.
      In the event that a Project-specific CoC has not been approved, the LF Projects Code of Conduct listed at
      https://lfprojects.org/policies will apply for all Collaborators in the Project.
   
   3. When amending or adopting any policy applicable to the Project, LF Projects will publish such policy, as to be
      amended or adopted, on its web site at least 30 days prior to such policy taking effect; provided, however, that
      in the case of any amendment of the Trademark Policy or Terms of Use of LF Projects, any such amendment is
      effective upon publication on LF Project’s web site.
   
   4. All Collaborators must allow open participation from any individual or organization meeting the requirements for
      contributing under this Charter and any policies adopted for all Collaborators by the TSC, regardless of
      competitive interests. Put another way, the Project community must not seek to exclude any participant based on
      any criteria, requirement, or reason other than those that are reasonable and applied on a non-discriminatory
      basis to all Collaborators in the Project community.
   
   5. The Project will operate in a transparent, open, collaborative, and ethical manner at all times. The output of all
      Project discussions, proposals, timelines, decisions, and status will be made open and easily visible to all
      except in matters related to security, where making information public could expose the Project to harmful
      actions. Any potential violations of this requirement should be reported immediately to the Series Manager.
   
   6. The TSC will abide by any and all required policies and procedures as defined by the LFDT.
   
6. **Community Assets**

   1. LF Projects will hold title to all trade or service marks used by the Project (“Project Trademarks”), whether
      based on common law or registered rights. Project Trademarks will be transferred and assigned to LF Projects to
      hold on behalf of the Project. Any use of any Project Trademarks by Collaborators in the Project will be in
      accordance with the license from LF Projects and inure to the benefit of LF Projects.
   
   2. The Project will, as permitted and in accordance with such license from LF Projects, develop and own all Project
      GitHub and social media accounts, and domain name registrations created by the Project community.
   
   3. Under no circumstances will LF Projects be expected or required to undertake any action on behalf of the Project
      that is inconsistent with the tax-exempt status or purpose, as applicable, of the Joint Development Foundation or
      LF Projects, LLC.
   
7. **General Rules and Operations**

   1. The Project will:
   
      1. engage in the work of the Project in a professional manner consistent with maintaining a cohesive community,
         while also maintaining the goodwill and esteem of LF Projects, Joint Development Foundation and other partner
         organizations in the open source community; and
      
      2. respect the rights of all trademark owners, including any branding and trademark usage guidelines.
      
8. **Intellectual Property Policy**

   1. Collaborators acknowledge that the copyright in all new contributions will be retained by the copyright holder as
      independent works of authorship and that no contributor or copyright holder will be required to assign copyrights
      to the Project.
   
   2. Except as described in Section **8.iii** below, all contributions to the Project are subject to the following:
   
      1. All new inbound code contributions to the Project must be made using Apache License, Version 2.0 available at
         http://www.apache.org/licenses/LICENSE-2.0  (the “Project License”).
      
      2. All new inbound code contributions must also be accompanied by a Developer Certificate of Origin
         (http://developercertificate.org) sign-off in the source code system that is submitted through a TSC-approved
         contribution process which will bind the authorized contributor and, if not self-employed, their employer to
         the applicable license;
      
      3. All outbound code will be made available under the Project License.
      
      4. Documentation will be received and made available by the Project under the Creative Commons Attribution 4.0
         International License (available at http://creativecommons.org/licenses/by/4.0/).
      
      5. The Project may seek to integrate and contribute back to other open source projects (“Upstream Projects”). In
         such cases, the Project will conform to all license requirements of the Upstream Projects, including
         dependencies, leveraged by the Project.  Upstream Project code contributions not stored within the Project’s
         main code repository will comply with the contribution process and license terms for the applicable Upstream
         Project.
      
   3. The TSC may approve the use of an alternative license or licenses for inbound or outbound contributions on an
      exception basis. To request an exception, please describe the contribution, the alternative open source
      license(s), and the justification for using an alternative open source license for the Project. License
      exceptions must be approved by a two-thirds vote of the TSC.
   
   4. Contributed files should contain license information, such as SPDX short form identifiers, indicating the open
      source license or licenses pertaining to the file.
   
9. **Related Parties**

     1. “Related Party” shall mean
   
        1. any person or entity which controls or is controlled by a TSC Member or which, together with a TSC Member,
           is under the common control of a third party, in each case where such control results from
        
           1. ownership, either directly or indirectly, of more than fifty percent of the voting securities or
              membership interests of the entity in question, or
           
           2. the ability to exercise managerial control over the entity in question, or
           
        2. any employee of or independent contractor engaged by a TSC Member, which for the avoidance of doubt shall
           include an independent contractor who contracts with the TSC Member via a sole proprietorship or similar
           entity, but shall expressly exclude
        
           1. third party vendors (such as, but not limited to, development shops) that employ multiple individuals and
              serve multiple clients ("Vendors") or
           
           2. the employees or contractors of such Vendors.
           
     2. “Related Parties” are entities that are each a Related Party of a TSC Member.
   
     3. “Managerial control” means the capacity to direct or significantly influence the decisions and actions of an
        entity by virtue of holding leadership positions within the company. This includes the authority of roles such
        as executives, directors, or other senior leaders who have the authority to make strategic decisions that affect
        the direction and operations of the entity. Managerial control excludes scenarios where an entity’s influence is
        limited to overseeing a contractual relationship without having direct leadership or decision-making authority
        within the entity.
   
10. **Amendments**

    1. This charter may be amended by a two-thirds vote of the TSC and is subject to approval by LF Projects; and
    
    2. Changes to the Baird Seat definition must be amended by a unanimous vote of all members of the TSC other than the
       Baird Seat, subject to approval by LF Projects.
