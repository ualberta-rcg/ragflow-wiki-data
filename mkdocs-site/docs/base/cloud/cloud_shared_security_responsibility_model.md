---
title: "Cloud shared security responsibility model"
slug: "cloud_shared_security_responsibility_model"
lang: "base"

source_wiki_title: "Cloud shared security responsibility model"
source_hash: "d29322c6273e513489c5a83c8f38c5d7"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:30:35.270893+00:00"

tags:
  - cloud

keywords:
  - "security of the cloud"
  - "cloud team responsibilities"
  - "shared compliance responsibilities"
  - "research team responsibilities"
  - "security in the cloud"

questions:
  - "What specific security duties are assigned to research teams for protecting their data and virtual machines in the cloud?"
  - "What security-related tasks does the cloud support team handle to protect the cloud platform itself?"
  - "Which compliance obligations are shared between the cloud support team and research teams, and what policies must they follow?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Canada’s advanced research computing environment includes several cloud platforms for research. This document’s purpose is to describe the responsibilities of the cloud team who administers our cloud platforms; the responsibilities of the many research teams who use these platforms; and shared responsibilities between both. **Security in the cloud** is the responsibility of the research teams. **Security of the cloud** is the responsibility of our cloud support team.

## Research team responsibilities: Security in the cloud
Research teams are responsible for the following:
*   implementing security controls to protect the confidentiality, integrity, and availability of their research data;
*   installing, configuring, and managing their virtual machines, as well as their operating systems, services and applications;
*   [applying updates](security_considerations_when_running_a_vm.md#updating-your-vm) and security patches on a timely basis;
*   configuring security group rules that limit the services exposed to the Internet;
*   implementing and testing backup and recovery procedures;
*   encrypting sensitive data in transit and/or at rest;
*   ensuring the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) is followed when granting access.

## Cloud team responsibilities: Security of the cloud
The cloud support team is responsible for the following:
*   protecting our cloud platforms;
*   configuring and managing these compute, storage, database, and networking capabilities;
*   applying updates and security patches applicable to the cloud platform on a timely basis;
*   maintaining logs sufficient for supporting investigations and incident response;
*   ensuring the environmental and physical security of the cloud infrastructure.

!!! warning "Important Operational Detail"
    Our cloud support team does not support or manage virtual machines. However, if a virtual machine is adversely impacting others, it may be shut down and locked by the team. In these cases, the research team may be asked to provide remediation plans before access to the virtual machine is restored. This is so that others are protected.

## Shared responsibilities
Compliance is a shared responsibility between our cloud support team and the research teams using our cloud services. Everyone is responsible to comply with applicable laws, policies, procedures, and contracts. Alliance Federation and institutional policy compliance is required, particularly with respect to the [Terms of Service](https://www.alliancecan.ca/en/policies). Being *good Net citizens* will protect the reputation of our networks and prevent all of us from being blocked or banned.

!!! note "Questions?"
    If you have any questions about this model please contact cloud@tech.alliancecan.ca.

## Further resources
For more information please see the following resources:
*   [Alliance Federation’s cloud service description](cloud.md)
*   [Cloud security considerations for research teams](security_considerations_when_running_a_vm.md)
*   [Alliance Policies](https://www.alliancecan.ca/en/policies)