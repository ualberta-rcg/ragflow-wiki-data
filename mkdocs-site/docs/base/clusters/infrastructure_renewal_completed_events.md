---
title: "Infrastructure renewal completed events"
slug: "infrastructure_renewal_completed_events"
lang: "base"

source_wiki_title: "Infrastructure renewal completed events"
source_hash: "46ed83cff119f7036669941885b7510b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:06:02.532883+00:00"

tags:
  []

keywords:
  - "Mist cluster"
  - "maintenance"
  - "Outage"
  - "Cluster outage"
  - "Job wait times"
  - "Jan 22 2025"
  - "Cedar"
  - "system improvements"
  - "Juno Cloud"
  - "Infrastructure renewal"
  - "capacity reduction"
  - "storage migration"
  - "system decommission"
  - "storage systems"
  - "Planned outage"
  - "compute clusters"
  - "Niagara and Mist"
  - "Narval"
  - "Cluster services"
  - "Béluga Cloud"
  - "Cloud instances"
  - "Trillium"
  - "Scheduled maintenance"
  - "infrastructure renewal"
  - "Capacity reduction"
  - "Compute nodes"
  - "Trillium transition"
  - "Niagara"
  - "Compute cluster"
  - "Niagara cluster"

questions:
  - "What was the timeline and process for the capacity reduction and eventual decommissioning of the Niagara and Mist clusters in 2025?"
  - "How did the data migration and system transition work affect the operations and services of the Graham compute cluster prior to its retirement?"
  - "What were the specific impacts on file backups, restores, and nearline data accessibility during the tape storage system migration for Béluga, Narval, and Juno?"
  - "What specific performance issues were experienced by jobs running on the Fir cluster?"
  - "At what capacity levels did the Niagara and Mist clusters operate starting January 6, 2025?"
  - "What was the underlying purpose for reducing the capacity of the Niagara and Mist clusters?"
  - "What caused the extended outage and the long-term capacity reduction on the Cedar cluster during 2025?"
  - "How did the scheduled electrical maintenance in June 2025 impact the compute nodes and cloud instances of the Béluga, Narval, and Juno platforms?"
  - "Which specific systems and services were unavailable during the Rorqual cluster's scheduled maintenance on September 3, 2025?"
  - "Why was the Graham cluster outage extended, and what specific services were unavailable during this period?"
  - "How did the system handle running and scheduled jobs differently during the Cedar cluster outage compared to the Béluga and Narval maintenance?"
  - "Which specific cloud instances and storage systems remained operational despite the scheduled shutdowns of their associated compute nodes?"
  - "What happened to the jobs on the Juno Cloud non-High Availability zone that were scheduled to finish after 9:00 a.m. on June 6?"
  - "Which specific cloud instances experienced short access outages during the maintenance period?"
  - "How were the storage systems on Béluga and Narval affected by the work, and through what methods did they remain accessible?"
  - "When exactly are the Niagara and Mist compute nodes scheduled to be shut down?"
  - "What is the primary purpose of the planned system outage?"
  - "Which systems will remain accessible during the maintenance, and how will the scheduler handle newly submitted jobs?"
  - "What specific actions must users take regarding their data on the Cedar cluster before the January 13, 2025 shutdown?"
  - "How does the job scheduler handle submitted tasks that cannot be completed before the scheduled maintenance periods?"
  - "Which specific services, such as cloud or login nodes, remain operational during the Cedar cluster outages?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page provides details of completed events which are part of the infrastructure renewal activities.

## Niagara and Mist Capacity Reduction and Decommissioning (Jan 6 - Sept 30, 2025)

**Start Time:** Jan 6, 2025
**End Time:** Sept 30, 2025 (268 days)
**Status:** Complete
**System:** Niagara (50% → decommissioned), Mist (35% → decommissioned)
**Type:** Reduction

Beginning January 6, 2025, the **Niagara** cluster operated at approximately **50%** capacity and **Mist** at approximately **35%** to support ongoing system improvements and the transition to the new [Trillium](trillium.md) system.

!!! note
    Mist required a brief temporary shutdown on January 6.

In September 2025, additional staged reductions were implemented ahead of system retirement:

*   **Sept 4:** Niagara reduced to **863** compute nodes.
*   **Sept 9:** **Niagara Open OnDemand** decommissioned; data-centre firewall upgrade caused a brief interruption; end-of-day capacity **647** nodes.
*   **Sept 11:** **Trillium Open OnDemand** launched: <https://ondemand.scinet.utoronto.ca>.
*   **Sept 16:** Full-day maintenance; Niagara reduced to **431** nodes; **Mist decommissioned**.
*   **Sept 24:** Niagara reduced to **215** compute nodes.
*   **Sept 30:** **Niagara decommissioned**.

These reductions remained in effect until each system’s end of service.

## Graham Capacity Reduction and Decommissioning (Feb 25 - Sept 1, 2025)

**Start Time:** Feb 25, 2025
**End Time:** Sept 1, 2025 (188 days)
**Status:** Complete
**System:** Graham (25%)
**Type:** Reduction

Beginning February 25, 2025, the **Graham** compute cluster operated at approximately **25% capacity** while data migration and system transition work were underway ahead of its retirement on September 1.

!!! info "Background"
    *   The start of the reduction was postponed from January to February while storage migration progressed.
    *   During this period, user logins remained available and storage was accessible, though project storage was temporarily read-only during migration.
    *   Graham operated under a simplified scheduling configuration with limited runtimes and support for CPU and GPU jobs (V100, T4, A100, A5000).
    *   Auxiliary services such as Globus and gra-vdi returned as resources allowed.
    *   **Graham Cloud remained fully operational throughout the reduction period.**

Graham was fully decommissioned on September 1, 2025.

## Béluga, Narval, and Juno Tape Storage System Migration (July 15 - Sept 8, 2025)

**Start Time:** July 15, 2025
**End Time:** Sept 8, 2025 (55 days)
**Status:** Complete
**System:** Béluga, Narval, Juno
**Type:** Outage

From July 15 to August 25, 2025, the tape storage system behind the TSM service, including backups and migrated /nearline data, was unavailable during its migration to a new data centre.

*   **File backup and restore services were unavailable.**
    *   Users were asked to keep a backup copy of important data on another system and double-check delete operations.
    *   Restores of data created before July 15 resumed once the tape system returned to service.
    *   Data created or modified between July 15 and August 11 could not be recovered.
*   On Béluga and Narval, files in /nearline that had been migrated to tape were not accessible.
    *   To identify these files, see ["Transferring data from /nearline."](https://docs.alliancecan.ca/wiki/using-nearline-storage#transferring_data_from_/nearline)
*   **The TSM service itself was fully unavailable.**

!!! note
    Other storage systems, compute nodes on all clusters, and Juno Cloud instances remained fully operational. Globus transfers functioned normally except when accessing tape-migrated /nearline files.

## Fir Capacity Reduction for Cooling Equipment Commissioning (Aug 25 - Sept 5, 2025)

**Start Time:** August 25, 2025
**End Time:** Sept 5, 2025 (12 days)
**Status:** Complete
**System:** Fir
**Type:** Reduction

To support commissioning of new cooling equipment, some compute nodes on **Fir** were temporarily unavailable from Monday, August 25 through Thursday, August 28, with reduced capacity through September 5.

*   **Fewer jobs ran concurrently** on **Fir**.
*   Jobs often **started more slowly** and **wait times were longer**.

## Niagara and Mist Initial Capacity Reduction (Jan 6 - Sept 16, 2025)

**Start Time:** Jan 6, 2025
**End Time:** Sept 16, 2025 (254 days)
**Status:** Complete
**System:** Niagara (50%), Mist (35%)
**Type:** Reduction

Beginning January 6, 2025, the **Niagara** cluster operated at approximately **50%** capacity and **Mist** at approximately **35%** to support ongoing system improvements and the transition to [Trillium](trillium.md).

!!! note
    **Mist** required a temporary shutdown for a few hours on January 6.

## Rorqual Scheduled Maintenance Outage (Sept 3, 2025)

**Start Time:** Sept 3, 2025
**End Time:** Sept 3, 2025 (1 day)
**Status:** Complete
**System:** Rorqual
**Type:** Outage

On September 3, 2025, from **8:00 a.m. (EDT)** until **5:00 p.m. (EDT)**, the **Rorqual** compute cluster was fully unavailable for scheduled maintenance.

*   All compute nodes were offline.
*   Jobs scheduled to complete after **8:00 a.m. (EDT)** on September 3 remained in the queue until service returned.
*   Network and storage systems associated with **Rorqual** were unavailable.

!!! note
    The **Narval** cluster and cloud instances on the **Béluga** and **Juno** platforms were not affected.

## Cedar Capacity Reduction (Jan 22 - Aug 11, 2025)

**Start Time:** Jan 22, 2025
**End Time:** Aug 11, 2025
**Status:** Complete
**System:** Cedar
**Type:** Reduction (70%)

Starting January 22, Cedar cluster will operate at approximately 70% capacity until Fir is commissioned during summer of 2025.

## Cedar Extended Outage for Infrastructure Renewal (June 16 - July 1, 2025)

**Start Time:** June 16, 2025
**End Time:** June 27, 2025 **(Extended to July 1, 2025)** (16 days)
**Status:** Complete
**System:** Cedar (100%)
**Type:** Outage

As part of the final phase of infrastructure renewal activities, a planned extended outage was scheduled from June 16 to June 27, 2025 to support critical data-centre power and cooling upgrades for the new system installation.

*   Login node access was unavailable for the entire outage period due to vendor data synchronization work.
*   File systems were accessible read-only via Globus only throughout the outage.
*   During the week of June 16, read-only access was provided to all file systems.
*   During the week of June 23, read-only access was limited to the old project file system (`/project/<project name>` via Globus).
*   Job submissions were suspended during the outage; previously submitted jobs ran once the outage concluded.
*   Cedar Cloud remained operational, though brief interruptions occurred during the maintenance window.

Following an unexpected cooling tower failure over the weekend, full recovery required a system reset to bring the cluster back online.

!!! note
    No action was required, but users should have planned accordingly for job scheduling.

## Béluga, Narval, and Juno (non-HA) Electrical Maintenance Outage (June 13 - June 16, 2025)

**Start Time:** June 13, 2025
**End Time:** June 16, 2025 (3 days)
**Status:** Complete
**System:** Béluga, Narval, Juno (non-HA)
**Type:** Outage

A second scheduled electrical maintenance required the shutdown of **Béluga and Narval compute nodes** from 12:00 p.m. (noon EDT) on June 13 until 12:00 p.m. (noon EDT) on June 16, 2025. Cloud instances in the **Juno Cloud (non-High Availability zone)** were also shut down. Jobs scheduled to finish after 12:00 p.m. on June 13 remained queued until the clusters returned to service.

!!! info
    These interruptions did **not affect** Béluga cloud instances or Juno cloud instances in the **High Availability zone**.

**Béluga and Narval storage remained accessible** via Globus and the login nodes of each cluster. The previously announced outage from June 6 to June 10, 2025, proceeded as planned. This June 13–16 window was **in addition** to that work.

## Béluga, Narval, and Juno (non-HA) Electrical Maintenance Outage (June 6 - June 10, 2025)

**Start Time:** June 6, 2025, 9:00 AM (EDT)
**End Time:** June 10, 2025, 12:00 PM (EDT) (4 days)
**Status:** Complete
**System:** Béluga, Narval, Juno (non-HA)
**Type:** Outage

Scheduled electrical maintenance required the shutdown of **Béluga and Narval compute nodes** from 9:00 a.m. (EDT) on June 6 until 12:00 p.m. (noon) on June 10, 2025. Cloud instances in the **Juno Cloud (non-High Availability zone)** were also shut down. Jobs scheduled to finish after 9:00 a.m. on June 6 remained queued until the clusters were back online. Brief interruptions for network and storage maintenance occurred:

*   **Cloud instances on Béluga Cloud and in the Juno Cloud HA zone** experienced short access outages.
*   **Storage systems on Béluga and Narval** remained accessible via Globus and login nodes but saw intermittent disruptions due to the work.

## Béluga, Narval, and Juno (non-HA) Electrical Maintenance Outage (April 30 - May 1, 2025)

**Start Time:** April 30, 2025
**End Time:** May 1, 2025 (1 day)
**Status:** Complete
**System:** Béluga, Narval, Juno (non-HA)
**Type:** Outage

Scheduled electrical maintenance required the shutdown of **Béluga and Narval compute nodes** from 12:00 PM (EDT) on April 30 until 12:00 PM (EDT) on May 1, 2025. Cloud instances in the **Juno cloud (non-high availability zone)** were also shut down during this time.

Jobs scheduled to finish after 12:00 PM on April 30 remained queued until the clusters were back online.

!!! info
    These interruptions did **not affect** Béluga cloud instances or Juno cloud instances in the **high availability zone**.

**Béluga and Narval storage remained accessible** through Globus and the login nodes of each cluster.

## Cedar Planned Outage for Power Modifications (March 31 - April 2, 2025)

**Start Time:** March 31, 2025
**End Time:** April 2, 2025 (2 days)
**Status:** Complete
**System:** Cedar (100%)
**Type:** Outage

As part of the preparations for bringing new equipment online, a planned outage was required to perform power modifications.

The Cedar cluster was completely unavailable during this time. Users were not able to log in or run jobs on the cluster. Any jobs running at the time of the outage were terminated and had to be re-submitted once the cluster came back online.

!!! info
    **Cedar Cloud remained operational during this period.**

## Cedar Planned Outage for Power Modifications (March 31 - April 2, 2025)

**Start Time:** March 31, 2025
**End Time:** April 2, 2025 (2 days)
**Status:** Complete
**System:** Cedar (100%)
**Type:** Outage

As part of the preparations for bringing new equipment online, a planned outage was required to perform power modifications.

The Cedar cluster was completely unavailable during this time. Users were not able to log in or run jobs on the cluster. Any jobs running at the time of the outage were terminated and had to be re-submitted once the cluster came back online.

!!! info
    **Cedar Cloud remained operational during this period.**

## Graham Complete Data Centre Shutdown (Dec 7, 2024 - Feb 24, 2025)

**Start Time:** Dec 7, 2024
**End Time:** Jan 3, 2025 **(Extended to Feb 24, 2025)**
**Status:** Complete
**System:** Graham (100%)
**Type:** Outage

Ongoing renovations require a complete data centre shutdown originally scheduled from Dec 7, 2024 to Jan 3, 2025. During this time, all Graham cluster services, storage, and cloud services will be entirely unavailable.

!!! warning "Jan 28, 2025 Update"
    This outage has been extended due to some delays. For updated information, please see <https://status.alliancecan.ca>.

## Béluga and Narval Temporary Capacity Reduction for Rorqual Tests (Jan 13 - Feb 14, 2025)

**Start Time:** Jan 13, 2025
**End Time:** Feb 14, 2025
**Status:** Complete
**System:** Béluga, Narval
**Type:** Temporary Reduction

Performance and stability tests on Rorqual will require the shutdown of all Béluga compute nodes and about half of Narval compute nodes from 8 a.m. on January 13 until 12 p.m. (noon) on January 31, 2025 (EST). Login nodes and data access will remain operational. On Narval, approximately 50% of nodes from each category (CPU, GPU, and large memory) will be shut down. During the shutdown time, Béluga Storage will be mounted to Narval (`/lustre01`, `/lustre02`, `/lustre03`, `/lustre04` of Beluga). Béluga and Juno cloud instances are unaffected. Jobs on Béluga scheduled to complete after 8 a.m. on January 13 will remain queued until the cluster resumes.

!!! warning "Jan 30, 2025 Update"
    Narval's compute capacity is at 100% until February 6, then again at 30% for the last Rorqual tests. Béluga and Narval should be back to 100% capacity on February 14. For updated information, please see <https://status.alliancecan.ca>.

## Niagara and Mist Outage for System Improvements (Jan 22, 2025)

**Start Time:** Jan 22, 2025
**End Time:** Jan 22, 2025 (1 day)
**Status:** Complete
**System:** Niagara, Mist
**Type:** Outage

Niagara and Mist compute nodes will be shut down on January 22, 2025 from 8 AM to 5 PM EST to support ongoing system improvements and the integration with the new system, [Trillium](trillium.md). The login nodes, file systems, and the HPSS system will remain available. The scheduler will hold jobs that are submitted until the maintenance has finished.

## Cedar Outage for Infrastructure Renewal (Jan 13 - Jan 21, 2025)

**Start Time:** Jan 13, 2025
**End Time:** Jan 21, 2025 (9 days)
**Status:** Complete
**System:** Cedar (100%)
**Type:** Outage

The Cedar compute cluster will be shut down in preparation for the infrastructure renewal. Jobs submitted to the cluster will queue and may start running if they can complete before the shutdown. Jobs that cannot run will remain in the queue until the cluster is fully operational on January 21. The Cedar `/scratch` filesystem will be migrated to new storage.

!!! warning
    **Please move any important data immediately to your `/project`, `/nearline`, or `/home` directory.**

!!! info
    Cedar cloud will remain operational during this period.

## Niagara Power Shutdown for Trillium Cluster Setup (Nov 25 - Nov 26, 2024)

**Start Time:** Nov 25, 2024
**End Time:** Nov 26, 2024 (1 day)
**Status:** Complete
**System:** Niagara
**Type:** Outage

A full power shutdown will take place for main panel upgrades ahead of [Trillium](trillium.md) cluster setup. All Niagara services, including the cluster and scheduler, will pause during this time. The scheduler will hold jobs that cannot finish before the start of the shutdown. Users are encouraged to submit smaller, short-duration jobs to optimize idle node usage before the maintenance begins.

## SciNet Data Centre Outage for Electrical Equipment Installation (Nov 7 - Nov 8, 2024)

**Start Time:** Nov 7, 2024
**End Time:** Nov 8, 2024 (1 day)
**Status:** Complete
**System:** Niagara
**Type:** Outage

All systems and storage at the SciNet Data centre (Niagara, Mist, HPSS, Rouge, Teach, JupyterHub, Balam) will be unavailable from 7 a.m. to 5 p.m. ET. This outage is necessary for installing new electrical equipment (UPS) as part of a systems refresh. The scheduler will pause jobs unable to finish before the shutdown. Users can prioritize short jobs to utilize otherwise idle nodes prior to maintenance.

## Cedar Compute Node Outage (Nov 7 - Nov 8, 2024)

**Start Time:** Nov 7, 2024, 6 a.m. PST
**End Time:** Nov 8, 2024, 6 a.m. PST
**Status:** Complete
**System:** Cedar
**Type:** Outage

Cedar compute nodes will be unavailable during this period.

!!! info
    However, Cedar login nodes, storage, and cloud services will remain operational and unaffected.