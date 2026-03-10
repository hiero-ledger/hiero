## Title: Hiero Github Workflow App
Hiero Github Workflow App is a mentorship project at Hiero. It involves coding scalable, highly secure, end-to-end maintainer workflows that support contributor onboarding, progression and repository management across Hiero.


## Primary Focus

Coding

## Description

The Hiero ecosystem includes a growing number of diverse contributors, repositories, junior committers/committers/maintainers, pull requests, issues, discussions, and quality requirements. 

To build a diverse ecosystem which generates high-quality code, maintainers need to spend a significant amount of time on repetitive coordination tasks such as checking contributor qualifications, validating pull request quality, unassigning inactive contributors, closing stale issues, creating issues at different difficulties, and ensuring that repository processes are followed consistently.

We have demonstrated in some SDK repositories many of these maintainer tasks can be automated using custom github action workflows and templates. However, the current setup is fragmented, difficult to customize and scale, and inconsistent across repositories. Different repositories may require different rules, but maintainers still need support to ensure they are working on the most important tasks, and developers need support to help them progress quickly and qualify to gain more responsibilities.

This mentorship project aims to design and build an automation framework and application for Hiero end-to-end maintainer workflows. The system should support configurable repository automation features that maintainers can turn on or off, depending on the repository context. 

Example user onboarding workflows:

- Checking contributors are humans
- Checking whether contributors meet contribution requirements before assigning issues
- Offering automatic issue assignment
- Automatically assigning mentors for new contributors
- Issue templates and documentations

Example pull request review and quality workflows:

- AI issue planning
- AI initial reviewing
- Automated code quality, DCO, GPG, etc checks based on configurable quality requirements
- Automatic review based on configurable quality requirements

Example developer progression workflows:

- Automatic issue recommendations after a merged pull request to next available issues
- Checking whether advanced contributors meet requirements to progress to JC/committer/maintainer

Example issue management workflows:

- Managing stale issues or pull requests
- Requesting help or feedback from specified teams based on labels

A core requirement of the project is to ensure that these automations are reliable, consistent, secure, and scalable enough to be used across a variety of repositories inside Hiero (and one day optionally across LFDT). 

The project should also define clear boundaries for what the automation is allowed to do, how maintainers configure it, and how users can understand or override automated actions when necessary.

The result should not just be a prototype for a single repository, but a hardened and reusable solution that can serve multiple Hiero repositories with different policies and maintenance needs.
It thus should also be efficient, minimizing github action workflow time or resources.

## Learning Objectives

- Understand open source maintainer workflows and common repository management challenges
- Learn how GitHub-based automation works
- Understand how to design configurable automation systems 
- Learn how to create reliable and scalable backend services for workflow orchestration
- Learn about safety, auditability, and transparency requirements for maintainer-facing tooling
- Improve skills in testing, observability, and operational hardening of developer infrastructure

## Expected Outcome and Deliverables

The successful completion of this project will result in a working application for Hiero maintainer workflows that can be used safely across repositories that opt-in.

Expected deliverables include:

- A reusable automation application or GitHub App for maintainer workflows
- Support for a configurable set of workflows that can be enabled or disabled per repository
- An initial implementation of several high-value workflows that are built for maintainability, scalability and security.
- Tests covering core logic, workflow behavior, and safety constraints
- Documentation for maintainers and contributors for running the solution in production
- Recommendations for future extensions and long-term maintainability

## Relation to LF Decentralized Trust and impact on the community

The contribution will support the Hiero ecosystem by improving the day-to-day experience of contributors across multiple repositories. By reducing repetitive manual work and making repository workflows more consistent, the project aims to raise the opportunities for getting started for new starters, progression and raise the quality of code contributions. Maintainers focus more on technical review, community support, and strategic project work.

The project also has broader value for the LF Decentralized Trust community because the result could be applied in the future across LFDT projects. A successful implementation could improve diverse contributor onboarding, pull request quality and nurture the junior committer-committer-maintainer pipelines.

## Recommended Skills

- Proficiency in Javascript/Typescript and yaml
- Experience with Git and GitHub, including pull requests, issues, labels, and review workflows
- Familiarity with GitHub APIs, Actions and or GitHub App development
- Understanding of software architecture and building maintainable automation systems
- Familiarity with testing, CI pipelines, and observability
- Understanding of safety and permission boundaries
- Prior contributions to open source projects

## Mentor(s) Names and Contact Info

Name: Sophie Bulloch
Email: exploreriii57@gmail.com
Company affiliation: Independent

Name:  
Email:  
Company affiliation:

## Additional Information

The project should pay special attention to:

- Safety and permissions of automated actions
- Clear auditability and transparency of bot decisions
- Repository-specific configurability without excessive complexity
- Scalability across multiple repositories
- Consistency of behavior across different maintainer workflows
- Clear fallback and error handling

Example advanced directions could include:

- Reviewer recommendation logic
- PR health scoring or rule-based feedback
- Escalation workflows for inactive assignments
- Dashboards or reporting for maintainer insights
