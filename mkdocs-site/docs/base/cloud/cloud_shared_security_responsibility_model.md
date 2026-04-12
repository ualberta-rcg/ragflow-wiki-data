---
title: "Cloud shared security responsibility model"
slug: "cloud_shared_security_responsibility_model"
lang: "base"

source_wiki_title: "Cloud shared security responsibility model"
source_hash: "bd7b557c92a67a9e956187a277af1e03"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:25:31.318755+00:00"

tags:
  - cloud

keywords:
  - "Shared responsibility model"
  - "Research teams"
  - "Virtual machines"
  - "Cloud security"
  - "Cloud support team"

questions:
  - "What are the specific responsibilities of research teams regarding \"security in the cloud,\" such as managing virtual machines and protecting research data?"
  - "What duties fall under the cloud support team's responsibility for \"security of the cloud,\" including infrastructure management and handling disruptive virtual machines?"
  - "How do the cloud support team and research teams share the responsibility for compliance with applicable laws, policies, and the Alliance Federation Terms of Use?"
  - "What are the specific responsibilities of research teams regarding \"security in the cloud,\" such as managing virtual machines and protecting research data?"
  - "What duties fall under the cloud support team's responsibility for \"security of the cloud,\" including infrastructure management and handling disruptive virtual machines?"
  - "How do the cloud support team and research teams share the responsibility for compliance with applicable laws, policies, and the Alliance Federation Terms of Use?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Canada’s advanced research computing environment includes several cloud platforms for research. This document’s purpose is to describe the responsibilities of the cloud team who administers our cloud platforms; the responsibilities of the many research teams who use these platforms; and shared responsibilities between both.

!!! important
    **Security in the cloud** is the responsibility of the research teams. **Security of the cloud** is the responsibility of our cloud support team.

## Research team responsibilities: Security in the cloud
Research teams are responsible for the following:
*   implementing security controls to protect the confidentiality, integrity, and availability of their research data;
*   installing, configuring, and managing their virtual machines, as well as their operating systems, services and applications;
*   [applying updates](security-considerations-when-running-a-vm.md#updating-your-vm) and security patches on a timely basis;
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

!!! warning "Disruptive Virtual Machines"
    Our cloud support team does not support or manage virtual machines. However, if a virtual machine is adversely impacting others, it may be shut down and locked by the team. In these cases, the research team may be asked to provide remediation plans before access to the virtual machine is restored. This is so that others are protected.

## Shared responsibilities
Compliance is a shared responsibility between our cloud support team and the research teams using our cloud services. Everyone is responsible to comply with applicable laws, policies, procedures, and contracts. Alliance Federation and institutional policy compliance is required, particularly with respect to the [Terms of Use](https://alliancecan.ca/sites/default/files/2022-03/1-terms-of-use.pdf). Being *good Net citizens* will protect the reputation of our networks and prevent all of us from being blocked or banned.

!!! note "Contact"
    If you have any questions about this model please contact cloud@tech.alliancecan.ca.

## Further resources
For more information please see the following resources:
*   [Alliance Federation’s cloud service description](cloud.md)
*   [Cloud security considerations for research teams](security-considerations-when-running-a-vm.md)
*   [Alliance Federation Terms of Use](https://alliancecan.ca/sites/default/files/2022-03/1-terms-of-use.pdf)