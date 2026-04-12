---
title: "Migrating between clusters/en"
slug: "migrating_between_clusters"
lang: "en"

source_wiki_title: "Migrating between clusters/en"
source_hash: "283538a4718c825864da25486aeb0997"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:06:19.802592+00:00"

tags:
  []

keywords:
  - "filesystems"
  - "job submission"
  - "software"
  - "Globus"
  - "clusters"

questions:
  - "How is data storage managed across different clusters, and what is the recommended method for transferring large amounts of data between them?"
  - "What software and environment configurations are shared globally across clusters, and which ones must be manually reinstalled or reconfigured by the user?"
  - "What specific hardware and allocation differences must be considered when adapting a Slurm job submission script for a new cluster?"
  - "How is data storage managed across different clusters, and what is the recommended method for transferring large amounts of data between them?"
  - "What software and environment configurations are shared globally across clusters, and which ones must be manually reinstalled or reconfigured by the user?"
  - "What specific hardware and allocation differences must be considered when adapting a Slurm job submission script for a new cluster?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

While our clusters have a relatively high degree of uniformity, particularly the general-purpose clusters, there are still significant distinctions that you need to be aware of when moving from one cluster to another. This page explains what is the same between clusters and what changes you'll need to adapt to on a new cluster.

!!! tip "Data transfer recommendation"
    To transfer data from one cluster to another, we recommend using [Globus](globus.md), particularly when the amount of data involved exceeds a few hundred megabytes.

## Access

Each cluster is accessible via [SSH](ssh.md), simply by changing the name of the cluster to the appropriate value; your username and password are the same across all of the clusters. Note that accessing [Niagara](../clusters/national_systems.md) does require a [further step](../clusters/national_systems.md#access-to-niagara).

## Filesystems

While each of the general-purpose clusters has a similar [filesystem structure](../storage-and-data/storage_and_file_management.md), it is important to realize that there is no mirroring of data between the clusters. The contents of your home, scratch, and project spaces are independent on each cluster. The [quota policies](../storage-and-data/storage_and_file_management.md#filesystem-quotas-and-policies) may also differ between clusters, though in general not by much. If a group you work with has a special storage allocation on one cluster, for example `$HOME/projects/rrg-jsmith`, it will normally only be available on that particular cluster. Equally so, if your group requested that the default project space quota on a cluster be increased from 1 to 10 TB, this change will only have been made on that cluster. To transfer the data from one cluster to another, we recommend using [Globus](globus.md), particularly when the amount of data involved exceeds a few hundred megabytes.

## Software

The collection of [globally installed modules](../programming/utiliser_des_modules.md) is the same across all of our general-purpose clusters, distributed using CVMFS. For this reason, you should not notice substantial differences among the modules available, assuming you are using the same [standard software environment](../programming/standard_software_environments.md). However, any [Python virtual environments](../software/python.md#creating-and-using-a-virtual-environment) or [R](../software/r.md#installing-r-packages) and [Perl](../software/perl.md#installing-packages) packages that you may have installed in your directories on one cluster will need to be re-installed on the new cluster, using the same steps that you employed on the original cluster. Equally so, if you modified your `$HOME/.bashrc` file on one cluster to customize your environment, you will need to modify the same file on the new cluster you're using. If you installed a particular program in your directories, this will also need to be re-installed on the new cluster since, as we mentioned above, the filesystems are independent between clusters.

## Job submission

All of our clusters use Slurm for job submission, so many parts of a job submission script will work across clusters. However, you should note that the number of CPU cores per node or per GPU may vary significantly, so check the page of the cluster you are using to verify how many cores can be used on a node. The amount of memory per node or per core also varies, so you may need to adapt your script to account for this as well.

On some clusters, compute nodes may not have direct Internet access. Access the cluster's link, from the sidebar on the left, to find out about site-specific policies.

Each research group has access to a default allocation on every cluster, e.g., `#SBATCH --account=def-jsmith`, however special compute allocations like RRG or contributed allocations are tied to a particular cluster and will not be available on other clusters.