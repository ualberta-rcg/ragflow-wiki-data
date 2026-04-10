---
title: "HPC4Health"
slug: "hpc4health"
lang: "base"

source_wiki_title: "HPC4Health"
source_hash: "0b288feaebc1fc4b128e4cca8361facd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:12:00.065410+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Background

In the 2020 RAC, HPC4Health is part of a pilot project for the allocation of resources on a cluster provided by HPC4Health.

HPC4Health is a consortium of health providers from the University Health Network and The Hospital for Sick Children who build and maintain a virtualized compute infrastructure with high levels of security for health-related computation.

Service configuration will be as per Compute Canada standards (Slurm, CVMFS); by request, specific technical configurations could also be considered. Availability and support is not yet fully determined and may change during the allocation year, but the platform is anticipated to be supported to the same degree as other host sites.

## Requirements

Pre-consultation with HPC4Health is required in order for an allocation request to be considered. Contact [rac@computecanada.ca](mailto:rac@computecanada.ca) to arrange a consultation.

In order to be eligible for HPC4Health resources, RAC awardees will be required to:
1.  Sign a collaboration agreement with the University Health Network
2.  Not act as a health information network provider under PHIPA (i.e., not to use HPC4Health resources to share the data to collaborators or through the web)
3.  Use two factor authentication to log into the services

Once awarded, recipients of the HPC4Health RAC resources will require consultation with the HPC4Health team to coordinate signing of the collaboration agreement and confirmation that recipients will not act as health information network providers.

Eligible projects for HPC4Health resources will be health-related. Health research computation includes data sets which may otherwise be restricted to local institution compute systems due to it containing PHI, de-identified but still sensitive data, or data which cannot be easily deidentified (e.g. whole genomes). HPC4Health will work with end users and their institutional REB and Legal departments to ensure any specific requirements can be met.

## Infrastructure For RAC 2020

HPC4Health is allocating 500 CPU cores and 60TB of storage to the RAC pilot project.

Compute node specifications:

*   7 compute nodes with 38 cores and 230GB RAM
*   7 compute nodes with 38 cores and 125GB RAM
*   10 GE interconnects
*   60TB of scale-out NFS accessible storage

!!! warning "User Responsibility"
    HPC4Health does not provide clients with backups (i.e. tape), backups are the responsibility of the user.