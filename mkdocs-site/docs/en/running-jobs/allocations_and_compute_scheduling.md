---
title: "Allocations and compute scheduling/en"
slug: "allocations_and_compute_scheduling"
lang: "en"

source_wiki_title: "Allocations and compute scheduling/en"
source_hash: "5efd949e9ed651b11d4fac8c7f0e595c"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:44:50.309963+00:00"

tags:
  - slurm

keywords:
  - "Resource Allocation Project"
  - "evaluation criteria"
  - "Resource Allocation Competition"
  - "core equivalent"
  - "RAPIs"
  - "H100-3g.40gb"
  - "SLURM Raw Usage"
  - "P100-12gb GPUs"
  - "reference GPU unit (RGU)"
  - "Slurm scheduler"
  - "End date (incl.)"
  - "Plotly"
  - "priority calculation"
  - "GPU usage"
  - "figure legend toggles"
  - "proposal score"
  - "projected usage"
  - "GPU memory constraints"
  - "GPU instance"
  - "legend toggling"
  - "Metric"
  - "cores"
  - "compute resource"
  - "core year"
  - "GPU year"
  - "scheduler"
  - "memory-to-core ratio"
  - "H100-80gb"
  - "A100-40gb"
  - "CPU days"
  - "zoom and pan tools"
  - "SLURM Raw Shares"
  - "Projection"
  - "Running total"
  - "research group"
  - "show submitter usage"
  - "Tensor cores"
  - "projection of jobs"
  - "Queued jobs"
  - "project account"
  - "figure navigation"
  - "reference GPU unit"
  - "narval-gpu"
  - "Multi-Instance GPU"
  - "GPU-core-memory bundle"
  - "monthly breakdown"
  - "allocation"
  - "FP16 performance ratio"
  - "RAC committee"
  - "core-memory bundle"
  - "Usage by submitter"
  - "Slurm portal"
  - "Narval"
  - "Start date (incl.)"
  - "RGUs"
  - "RGU equivalents"
  - "GB"
  - "total usage"
  - "active national clusters"
  - "Allocation target"
  - "RGU values"
  - "resource usage"
  - "gpu-years"
  - "cores and memory"
  - "View Group Usage"
  - "Select system and dates"
  - "Reference GPU Units (RGUs)"
  - "FP32 performance ratio"
  - "single‑click/double‑click item control"

questions:
  - "What is the difference between storage allocations and core/GPU year allocations in high‑performance computing?"
  - "How does the scheduler prioritize jobs to help research groups stay within their allocation targets?"
  - "Why were Reference GPU Units (RGUs) introduced, and what criteria are used to rank GPU models?"
  - "What evaluation criteria are used to rank the different GPU models in the study?"
  - "How is the weighting distributed among the FP32 and FP16 performance ratios?"
  - "What specific hardware components are associated with the FP32 and FP16 performance measurements?"
  - "What criteria and weighting factors are used to calculate the RGU (Reference GPU Unit) scores for whole GPU models and their instances?"
  - "How does the Multi‑Instance GPU (MIG) technology affect the allocation of GPU resources, and what are the available instance profiles for the A100 and H100 GPUs in RAC 2027?"
  - "In the Resource Allocation Competition (RAC), how are RGUs derived from requested gpu‑years, and what happens to the RGU allocation if a project is moved to a different cluster?"
  - "How does the scheduler calculate job priority based on the resources requested versus the resources actually used?"
  - "What is a core‑equivalent, and how are jobs charged when their core‑to‑memory requests differ from the standard 1 core / 4 GB ratio?"
  - "How are GPU resources accounted for using the reference GPU unit (RGU), and what determines the number of RGU‑equivalents charged to a research group?"
  - "How is the number of RGUs determined from the requested gpu‑years for a specific GPU model?"
  - "What criteria does the RAC committee use to allocate up to the calculated RGUs for a proposal?"
  - "How is the allocation adjusted if the project’s resources need to be moved to a different cluster?"
  - "How does the RGU‑equivalent calculation handle cases where a research group requests more GPUs than the number of core‑memory bundles they have?"
  - "Why is the example job request counted as 2 RGU equivalents despite only having one core‑memory bundle?"
  - "What impact does the number of RGU equivalents have on a research group’s priority in the scheduling system?"
  - "When a research group requests more cores than the RGU‑core‑memory bundle allows, how is the job’s RGU‑equivalent count determined?"
  - "When a research group requests more memory than the RGU‑core‑memory bundle allows, how is the job’s RGU‑equivalent count determined?"
  - "What are the cores‑per‑RGU and memory‑per‑RGU ratios for each Alliance cluster, and how do the GPU‑core‑memory bundle characteristics (RGU per GPU and recommended resources) vary for models such as the H100‑80 GB on Fir and the A100‑40 GB on Narval?"
  - "What are the core counts and memory capacities for the H100‑3g.40gb node compared to the A100‑40gb node?"
  - "How do the performance values (e.g., 3.48, 6.1, 4.0) differ among the listed GPU configurations such as 00‑2g.20gb, H100‑3g.40gb, and the various A100 variants?"
  - "Which of the listed configurations belong to the Narval system, and what are their specific specifications?"
  - "How does the Slurm portal let users select a system, date range, and specific SLURM account to view resource‑usage metrics, and what interactive features does the resulting histogram provide?"
  - "What are the CPU core and memory allocations for each GPU bundle (e.g., H100‑1g.10gb, H100‑2g.20gb, H100‑3g.40gb) on the Nibi, Rorqual, and Trillium nodes as shown in the table?"
  - "According to the note, what must users keep in mind about the physical GPU‑to‑CPU ratios when they request multiple GPUs per node?"
  - "How can you toggle individual metrics (e.g., SLURM Raw Usage, SLURM Raw Shares, CCDB allocation, Queued jobs, Total) on and off using the figure legend?"
  - "What does the red horizontal line for SLURM Raw Shares represent, and how can you show or hide it and the Queued jobs metric for a selected account?"
  - "How do you choose a specific cluster and time interval, and what effect does selecting an end date in the future have on the displayed usage figure?"
  - "How can you navigate the figure using Plotly tools such as zoom and pan?"
  - "What is the effect of single‑clicking versus double‑clicking an item in the legend?"
  - "Where do the Plotly tool icons appear when you hover your mouse over the figure window?"
  - "What entries are shown in the pull‑down menu and which scheduler do they correspond to?"
  - "How do the “Start date (incl.)” and “End date (incl.)” fields determine the jobs displayed in the figure?"
  - "What is displayed when an end date set in the future is selected?"
  - "How does the “Projection” area work when an end time after the present is selected, and what assumptions are made about pending and running jobs?"
  - "What is the difference between the “Total” and “Running total” summation options, and how does the “Include Running jobs” setting influence the displayed usage data?"
  - "How can users use the running‑total view of account usage together with the Allocation Target to evaluate fair‑share scheduling, and why is a 30‑day interval recommended?"
  - "What details are shown in the “Usage by Resource Allocation Project” tab and how are they summarized?"
  - "How does the system display GPU usage for allocation projects, and what role do Reference GPU Units (RGUs) play in that breakdown?"
  - "In what way can usage be grouped and examined by individual submitters, and how can monthly breakdowns be accessed?"
  - "What information is displayed in the tables regarding total and projected usage for the current allocation period?"
  - "How does the “Show monthly usage” link in the Extra Info column provide a detailed breakdown of usage by month for a specific cluster?"
  - "What does the “Show submitter usage” option reveal about the jobs submitted by individual users on the cluster?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Job scheduling policies](job_scheduling_policies.md)*

# Allocations for high-performance computing

**An allocation is an amount of resources that a research group can target for use for a period of time, usually a year.** This amount is either a maximum amount, as is the case for storage, or an average amount of usage over the period, as is the case for shared resources like computation cores.

Allocations are usually made in terms of core years, GPU years, or storage space. Storage allocations are the most straightforward to understand: research groups will get a maximum amount of storage that they can use exclusively throughout the allocation period. Core year and GPU year allocations are more difficult to understand because these allocations are meant to capture average use throughout the allocation period—typically meant to be a year—and this use will occur across a set of resources shared with other research groups.

The time period of an allocation when it is granted is a reference value, used for the calculation of the average which is applied to the actual period during which the resources are available. This means that if the allocation period was a year and the clusters were down for a week of maintenance, a research group would not be entitled to an additional week of resource usage. Equally so, if the allocation period were to be extended by a month, research groups affected by such a change would not see their resource access diminish during this month.

It should be noted that in the case of core year and GPU year allocations, both of which target resource usage averages over time on shared resources, a research group is more likely to hit (or exceed) its target(s) if the resources are used evenly over the allocation period than if the resources are used in bursts or if use is put off until later in the allocation period.

## From compute allocations to job scheduling

Compute-related resources granted by core-year and GPU-year allocations require research groups to submit what are referred to as *jobs* to a *scheduler*. A job is a combination of a computer program (an application) and a list of resources that the application is expected to use. The [scheduler](what_is_a_scheduler.md) is a program that calculates the priority of each job submitted and provides the needed resources based on the priority of each job and the available resources.

The scheduler uses prioritization algorithms to meet the allocation targets of all groups and it is based on a research group’s recent usage of the system as compared to their allocated usage on that system. The past of the allocation period is taken into account but the most weight is put on recent usage (or non-usage). The point of this is to allow a research group that matches their actual usage with their allocated amounts to operate roughly continuously at that level. This smooths resource usage over time across all groups and resources, allowing for it to be theoretically possible for all research groups to hit their allocation targets.

## Consequences of overusing a CPU or GPU allocation

If you have jobs waiting to run, and competing demand is low enough, then the scheduler may allow more of your jobs to run than your target level. The only consequence of this is that succeeding jobs of yours *may* have lower priority for a time while the scheduler prioritizes other groups which were below their target. You are not prevented from submitting or running new jobs, and the average of your usage over time should still be close to your target, that is, your allocation.

It is even possible that you could end a month or even a year having run more work than your allocation would seem to allow, although this is unlikely given the demand on our resources.

# Reference GPU Units (RGUs)

The performance of GPUs has dramatically increased in recent years and continues to do so. Until RAC 2023 we treated all GPUs as equivalent to each other for allocation purposes. This caused problems both in the allocation process and while running jobs, so in the 2024 RAC year we introduced the *reference GPU unit*, or **RGU**, to rank all GPU models in production and alleviate these problems. Since the 2025 RAC year we also have to deal with new complexity involving [multi-instance GPU technology](../programming/multi-instance_gpu.md).

Because roughly half of our users primarily use single-precision floating-point operations ([FP32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)), the other half use half-precision floating-point operations ([FP16](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)), and a significant portion of all users are constrained by the amount of memory on the GPU, we chose the following evaluation criteria and corresponding weights to rank the different GPU models:

| Evaluation Criterion | Weight |
| :------------------- | :----- |
| FP32 performance ratio (with dense matrices on regular GPU cores) | 40% |
| FP16 performance ratio (with dense matrices on *[Tensor cores](https://www.techspot.com/article/2049-what-are-tensor-cores/)*) | 40% |
| GPU memory size ratio | 20% |

We currently use the NVIDIA **A100-40gb** GPU as the reference model and assign it an RGU value of 4.0 for historical reasons. We define its FP16 performance, FP32 performance, and memory size each as 1.0. Multiplying the percentages in the above table by 4.0 yields the coefficients used to calculate the score of each component. RGU values of the available models are:

**RGU scores for whole GPU models**

| | FP32 score | FP16 score | Memory score | Combined score | Allocatable |
| :-------------------- | :--------- | :--------- | :----------- | :------------- | :---------- |
| **A100-40gb** | **1.60** | **1.60** | **0.80** | **4.0** | Yes |
| A100-80gb | 1.60 | 1.60 | 1.60 | 4.8 | No |
| H100-80gb | 5.48 | 5.08 | 1.60 | 12.2 | Yes |
| B200-180gb | 6.16 | 11.28 | 3.60 | 21.0 | Yes |

With the 2025 [infrastructure renewal](../clusters/infrastructure_renewal.md), it became possible to schedule a fraction of a GPU using [multi-instance GPU](../programming/multi-instance_gpu.md) technology. Different jobs, potentially belonging to different users, can run on the same GPU at the same time. Following [NVIDIA's terminology](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#terminology), a fraction of a GPU allocated to a single job is called a *GPU instance*, also sometimes called a *MIG instance*.

The following table lists the GPU models and instances that can be selected in the CCDB form for RAC 2027. RGU values for GPU instances have been estimated from whole-GPU performance numbers and the fraction of the GPU which comprises the instance.

**GPU models and instances available for RAC 2027**

| Model or instance | Fraction of GPU | RGU |
| :---------------- | :-------------- | :-- |
| A100-40gb | Whole GPU ⇒ 100% | 4.0 |
| A100-1g.5gb | max(1g/7g, 5GB/40GB) ⇒ 14% | 0.6 |
| A100-2g.10gb | max(2g/7g, 10GB/40GB) ⇒ 28% | 1.1 |
| A100-3g.20gb | max(3g/7g, 20GB/40GB) ⇒ 50% | 2.0 |
| H100-80gb | Whole GPU ⇒ 100% | 12.2 |
| H100-1g.10gb | max(1g/7g, 40GB/80GB) ⇒ 14% | 1.7 |
| H100-2g.20gb | max(2g/7g, 40GB/80GB) ⇒ 28% | 3.5 |
| H100-3g.40gb | max(3g/7g, 40GB/80GB) ⇒ 50% | 6.1 |
| B200-180gb | Whole GPU ⇒ 100% | 21.0 |

Note: a GPU instance of profile **1g** is worth 1/7 of an A100 or H100 GPU. The case of **3g** takes into consideration the extra amount of memory per **g**. **4g** profiles are not available on the clusters.

## RAC awards hold RGU values constant

*   During the Resource Allocation Competition (RAC), any proposal asking for GPUs must specify the preferred GPU model for the project. Then, in the CCDB form, the amount of reference GPU units (RGUs) will automatically be calculated from the requested amount of GPU-years per year of project.
    *   For example, if you select the *narval-gpu* resource and request 13 GPU-years of the model A100-40gb, the corresponding amount of RGUs would be 13 * 4.0 = 52. The RAC committee would then allocate up to 52 RGUs, depending on the proposal score. If your allocation must be moved to a different cluster, the committee will allocate GPU-years at that cluster so as to keep the amount of RGUs the same.

# Detailed effect of resource usage on priority

The overarching principle governing the calculation of priority on our national clusters is that compute-based jobs are considered in the calculation based on the resources that others are prevented from using and not on the resources actually used.

The most common example of unused cores contributing to a priority calculation occurs when a submitted job requests multiple cores but uses fewer cores than requested when run. The usage that will affect the priority of future jobs is the number of cores requested, not the number of cores the application actually used. This is because the unused cores were unavailable to others to use during the job.

Another common case is when a job requests memory beyond what is associated with the cores requested. If a cluster that has 4GB of memory associated with each core receives a job request for only a single core but 8GB of memory, then the job will be deemed to have used two cores. This is because other researchers were effectively prevented from using the second core because there was no memory available for it.

## Cores equivalent used by the scheduler

A core equivalent is a bundle made up of a single core and some amount of associated memory. In other words, a core equivalent is a core plus the amount of memory considered to be associated with each core on a given system.

On most of our clusters we define a core-equivalent to be 4GB and a core, since this is the memory-to-core ratio in the most common node type. Jobs are charged in terms of core-equivalent usage at the rate of 4 GB per core, as explained above. A core equivalent is defined as one core plus 4GB of memory.

Allocation target tracking is straightforward when requests to use resources on the clusters are made entirely of core and memory amounts that can be portioned only into complete equivalent cores. Things become more complicated when jobs request portions of a core equivalent because it is possible to have many points counted against a research group’s allocation, even when they are using only portions of core equivalents. In practice, the method used by the Alliance to account for system usage solves problems about fairness and perceptions of fairness but unfortunately the method is not initially intuitive.

Research groups are charged for the maximum number of core equivalents they take from the resources. Assuming a core equivalent of 1 core and 4GB of memory:

*   For example, if a research group requests two cores and 2GB per core (for a total of 4 GB of memory), and this leads to using more cores than memory based on the 1 core/4GB memory ratio, they will be charged by cores. The request effectively requires 2 core equivalents worth of cores, even though it only uses one bundle for memory. This job request will be counted as 2 core equivalents when priority is calculated.

*   Conversely, if a research group requests two cores and 5GB per core (for a total of 10 GB of memory), using more memory than the 1 core/4GB ratio, they will be charged by memory. The request requires 2.5 core equivalents worth of memory, even though it only uses two bundles for cores. This job request will be counted as 2.5 core equivalents when priority is calculated.

## Reference GPU unit equivalent used by the scheduler

Use of GPUs and their associated resources follow the same principles as already described for core equivalents, except that a reference GPU unit (RGU) is added to the bundle alongside multiple cores and memory. This means that the accounting for GPU-based allocation targets must include the RGU. Similar to how the point system was used above when considering resource use as an expression of the concept of core equivalence, we use a similar point system here as an expression of RGU equivalence.

Research groups are charged for the maximum number of RGU-core-memory bundles they use. Assuming a fictive bundle of 1 RGU, 3 cores, and 4 GB of memory:

*   Research groups using more RGUs than cores or memory per RGU-core-memory bundle will be charged by RGU. For example, a research group requests 2 P100-12gb GPUs (1 RGU each), 3 cores, and 4 GB of memory. The request is for 2 bundles worth of RGUs, but only one bundle for memory and cores. This job request will be counted as 2 RGU equivalents when the research group’s priority is calculated.

*   Research groups using more cores than RGUs or memory per RGU-core-memory bundle will be charged by core. For example, a researcher requests 1 RGU, 5 cores, and 5 GB of memory. The request is for 1.66 bundles worth of cores, but only one bundle for RGUs and 1.25 bundles for memory. This job request will be counted as 1.66 RGU equivalents when the research group’s priority is calculated.

*   Research groups using more memory than RGUs or cores per RGU-core-memory bundle will be charged by memory. For example, a researcher requests 1 RGU, 2 cores, and 6 GB of memory. The request is for 1.5 bundles worth of memory, but only one bundle for GPUs and 0.66 bundle for cores. This job request will be counted as 1.5 RGU equivalents when the research group’s priority is calculated.

*   On the same fictive cluster, a bundle with one V100-32gb GPU, 7.8 CPU cores and 10.4 GB of memory is worth 2.6 RGU equivalents.

*   On the same fictive cluster, a bundle with one A100-40gb GPU, 12 CPU cores and 16 GB of memory is worth 4.0 RGU equivalents.

### Ratios in bundles

Alliance systems have the following RGU-core-memory bundle characteristics (only one ratio per cluster):

| Cluster | Cores per RGU | Memory per RGU (GB) |
| :------ | :------------ | :------------------ |
| [Fir](../software/fir.md#node-characteristics) | 0.98 | 23.6 |
| [Narval](../clusters/narval.md#node-characteristics) | 3.00 | 31.1 |
| [Nibi](../clusters/nibi.md#node-characteristics) | 1.15 | 20.5 |
| [Rorqual](../clusters/rorqual.md#node-characteristics) | 1.31 | 10.2 |
| [Trillium](../clusters/trillium.md#node-characteristics) | 1.97 | 15.4 |

And the following GPU-core-memory bundle characteristics:

| Cluster | Model or instance | RGU per GPU | Bundle per GPU | Recommended per GPU |
| :------ | :---------------- | :---------- | :------------- | :------------------ |
| [Fir](../software/fir.md#node-characteristics) | **H100-80gb** | **12.2** | **12 cores, 288 GB** | **12 cores, 280 GB** |
| [Fir](../software/fir.md#node-characteristics) | H100-1g.10gb | 1.74 | 1.7 cores, 41 GB | 1 core, 35 GB |
| [Fir](../software/fir.md#node-characteristics) | H100-2g.20gb | 3.48 | 3.4 cores, 82 GB | 3 cores, 70 GB |
| [Fir](../software/fir.md#node-characteristics) | H100-3g.40gb | 6.1 | 6 cores, 144 GB | 6 cores, 140 GB |
| [Narval](../clusters/narval.md#node-characteristics) | **A100-40gb** | **4.0** | **12 cores, 124.5 GB** | **12 cores, 124 GB** |
| [Narval](../clusters/narval.md#node-characteristics) | A100-1g.5gb | 0.57 | 1.7 cores, 17.7 GB | 1 core, 15 GB |
| [Narval](../clusters/narval.md#node-characteristics) | A100-2g.10gb | 1.14 | 3.4 cores, 35.4 GB | 3 cores, 31 GB |
| [Narval](../clusters/narval.md#node-characteristics) | A100-3g.20gb | 2.0 | 6.0 cores, 62.2 GB | 6 cores, 62 GB |
| [Nibi](../clusters/nibi.md#node-characteristics) | **H100-80gb** | **12.2** | **14 cores, 250 GB** | **14 cores, 250 GB** |
| [Nibi](../clusters/nibi.md#node-characteristics) | H100-1g.10gb | 1.74 | 2 cores, 35.7 GB | 2 cores, 31 GB |
| [Nibi](../clusters/nibi.md#node-characteristics) | H100-2g.20gb | 3.48 | 4 cores, 71.4 GB | 4 cores, 62 GB |
| [Nibi](../clusters/nibi.md#node-characteristics) | H100-3g.40gb | 6.1 | 7 cores, 125 GB | 6 cores, 124 GB |
| [Rorqual](../clusters/rorqual.md#node-characteristics) | **H100-80gb** | **12.2** | **16 cores, 124.5 GB** | **16 cores, 124 GB** |
| [Rorqual](../clusters/rorqual.md#node-characteristics) | H100-1g.10gb | 1.74 | 2.3 cores, 17.7 GB | 2 cores, 15 GB |
| [Rorqual](../clusters/rorqual.md#node-characteristics) | H100-2g.20gb | 3.48 | 4.5 cores, 35.4 GB | 4 cores, 31 GB |
| [Rorqual](../clusters/rorqual.md#node-characteristics) | H100-3g.40gb | 6.1 | 8 cores, 62.2 GB | 8 cores, 62 GB |
| [Trillium](../clusters/trillium.md#node-characteristics) | **H100-80gb** | **12.2** | **24 cores, 188 GB** | **24 cores, 188 GB** |
| [Trillium](../clusters/trillium.md#node-characteristics) | **B200-180gb** | **21.0** | **12 cores, 250 GB** | **12 cores, 250 GB** |

!!! note
    While the scheduler will compute the priority based on the usage calculated with the above bundles, users requesting multiple GPUs per node also have to take into account the physical ratios.

# Viewing resource usage in the portal

[portal.alliancecan.ca/slurm](https://portal.alliancecan.ca/slurm) provides an interface for exploring time-series data about jobs on our national clusters. This portal includes a display that can present various usage metrics. Upon first login, it typically shows CPU days on a default cluster across all project accounts you have access to. If no usage is present for that cluster, a message indicating *No Data or usage too small to have a meaningful plot* will be displayed. You can modify the data shown using control panels located along the left margin of the page. These include three main panels:

*   Select system and dates
*   Parameters
*   SLURM account

## Displaying a specified account

If you have access to more than one [Slurm account](running_jobs.md#accounts-and-projects), the *Select user’s account* pull-down menu within the *SLURM account* panel allows you to choose which project account's data will be displayed. If the *Select user’s account* is left empty, the display will show all of your usage across accounts on the specified cluster during the selected time period. The *Select user’s account* pull-down menu is populated by a list of all the accounts that have job records on the selected cluster during the selected time interval. Other accounts that you have access to but do not have usage on the selected cluster during the selected time interval will also appear in the pull-down menu but will be greyed out and not selectable as they would not generate a figure. When you select a single project account, the display is updated and the summary panel titled *Allocation Information* is populated with details of the project account. The height of each bar in the histogram corresponds to the metric for that day (e.g., CPU-equivalent days) across all users in the account on the system. The top seven users are displayed in unique colours stacked on top of the summed metric for all other users in grey. The display supports navigation using [Plotly](https://plotly.com/graphing-libraries/) tools such as zoom and pan, which are typically accessible via icons when you hover over the display area. You can also manipulate the data shown using the legend on the right-hand side. Single-clicking an item in the legend will toggle its presence in the display, while double-clicking an item will toggle all other items off or on.

## Options in the figure legend

The legend of the usage display offers various options. You can enable or disable additional variables through it. Beyond displaying the colour affiliation of each user shown in the usage display, the legend provides access to displaying *SLURM Raw Usage*, *SLURM Raw Shares*, *CCDB allocation*, the resources pending for *Queued jobs*, and the daily *Total*. *SLURM Raw Usage* and *SLURM Raw Shares* are obtained from a poll of `sshare` for each account on the clusters. *CCDB allocation* is the account profile at CCDB representation of the *SLURM Raw Shares*. *Queued jobs* is a metric that represents the quantity of resources belonging to jobs that are pending in the job queue and is represented with narrow grey bars for each day in the display. *Total* adds text at the top of each bar indicating the daily total of the metric across users for the day. By single-clicking any of the items in the legend, the specific item is toggled in the display. By double-clicking any of the items in the legend, all other items in the display are toggled on or off.

## Displaying the allocation target and queued resources

When a single account has been selected for display, the *SLURM Raw Shares* can be shown as a horizontal red line. It can be turned off or on with the *Display allocation target by default* item in the *Parameters* panel, or by clicking on *SLURM Raw Shares* in the legend to the right of the display.

You can toggle the display of the *Queued jobs* metric, which presents a sum of all resources in pending jobs at each time point, by clicking on the words *Queued jobs* in the legend to the right of the display.

## Mouse hover over the figure window

Interactive options, native to Plotly, become available at the top right of the display when you hover your mouse pointer over it. Icons for 'Download plot as a png', 'Zoom', 'Pan', 'Box Select', 'Lasso Select', 'Zoom in', 'Zoom out', 'Autoscale', and 'Reset axes' facilitate interactive navigation of the data selection and scale. When hovering over individual data points (e.g., bars in a histogram), hover text appears, providing the 'User Name', 'Day', and 'Usage' quantity for the specific item under the pointer. Note that this returns the usage quantity for the specific user, not the sum across users for the day.

## Default SLURM Raw Shares and the SLURM Raw Usage

The SLURM Raw Shares of an allocation rrg-* or rpp-* account is a straight line that corresponds to the account's resource allocation on the cluster. For default accounts, the SLURM Raw Shares are dynamic over time based on the number of active accounts on the cluster. Plotting the SLURM Raw Shares of a default account on a specific cluster is an easy way of determining the expected usage that can be achieved by a default account on a given cluster.

The SLURM Raw Usage is a metric that the scheduling software uses to determine the priority of accounts. The SLURM Raw Usage is the cumulative sum of the account's usage in billing units plus a half-life decay period. Plotting the account's SLURM Raw Usage is a convenient way to assess how past usage influences the account's priority over time. A good rule of thumb in these figures is that if the SLURM Raw Usage is at 10 times the SLURM Raw Shares, then the account's usage is at par with its target share (e.g., the usage rate that the scheduler will try to maintain for the account).

## Selecting a specific cluster and time interval

The display shows your usage for a single cluster over a specified time interval. The *System* pull-down menu contains entries for each of the currently active national clusters that use Slurm as a scheduler. You can use the "Start date (incl.)" and "End date (incl.)" fields in the "Select system and dates" panel to change the time interval displayed. It will include all jobs on the specified cluster that were in a running (R) or pending (PD) state during the time interval, including both the start and end date. Selecting an end date in the future will display the *projection* of currently running and pending jobs for their requested duration into the future.

## Displaying usage over an extended time period into the future

If you select an end time after the present time, the display will have a transparent red area overlaid on the future time, labelled *Projection*. In this projection period, each job is assumed to run to its requested time limit. For queued resources, the projection supposes that each pending job starts at the beginning of the projected time (that is, right now) and runs until its requested time limit. This is not intended to be a forecast of actual future events!

## Metrics, summation, and running jobs

Use the *Metric* pull-down control in the *Parameters* panel to select from the following metrics: CPU, CPU-equivalent, RGU, RGU-equivalent, Memory, Billing, GPU, and all specific GPU models available on the selected cluster.

The *Summation* pull-down allows you to switch between the daily *Total* and *Running total*. If you select *Total*, each bar of the histogram represents the total usage for that single day. If you select "Running total", each bar represents the sum of that day's usage and all previous days back to the beginning of the time interval. If the *Allocation Target* is displayed, it is similarly adjusted to show the running total of the target usage. See the next section for more.

If you set *Include Running jobs* to *No*, the display shows only data from records of completed jobs. If you set it to *Yes*, it includes data from running jobs as well.

## Display of the running total of account usage

When displaying the running total of usage for a single account alongside the *Allocation target*, the usage histogram illustrates how an account deviates from its target share over the displayed period. The values in this view are the cumulative sum across days from the "total" summation view for both the usage and allocation target. When an account is submitting jobs that request more than the account’s target share, it is expected that the usage cumulative sum will oscillate above and below the target share cumulative sum if the scheduler is managing fair share properly. Because the scheduler uses a decay period for the impact of past usage, a good interval to use to inspect the scheduler’s performance in maintaining the account's fair share is to display the past 30 days.

# Viewing resource usage in CCDB

You can find information on the usage of compute resources by your groups by logging into the CCDB and navigating to *My Account > View Group Usage*.

CPU and GPU core year values are calculated based on the quantity of resources allocated to jobs on the clusters. It is important to note that the values summarized in these pages do not represent core-equivalent measures such that, in the case of large memory jobs, the usage values will not match the cluster scheduler’s representation of the account usage.

The first tab bar offers these options:
*   **By Compute Resource**: cluster on which jobs are submitted;
*   **By Resource Allocation Project**: projects to which jobs are submitted;
*   **By Submitter**: user that submits the jobs;
*   **Storage usage** is discussed in [Storage and file management](../storage-and-data/storage_and_file_management.md).

## Usage by compute resource

This view shows the usage of compute resources per cluster used by groups owned by you or of which you are a member for the current allocation year starting April 1st. The tables contain the total usage to date as well as the projected usage to the end of the current allocation period.

From the *Extra Info* column of the usage table, *Show monthly usage* can be clicked to display a further breakdown of the usage by month for the specific cluster row in the table. By clicking *Show submitter usage*, a similar breakdown is displayed for the specific users who submitted jobs on the cluster.

## Usage by resource allocation project

Under this tab, a third tag bar displays the RAPIs (Resource Allocation Project Identifiers) for the selected allocation year. The tables contain detailed information for each allocation project and the resources used by the projects on all of the clusters. The top of the page summarizes information such as the account name (e.g., def-, rrg- or rpp-*, etc.), the project title and ownership, as well as allocation and usage summaries.

## GPU usage and Reference GPU Units (RGUs)

For resource allocation projects that have GPU usage, the table is broken down into usage on various GPU models and measured in RGUs.

## Usage by submitter

Usage can also be displayed grouped by the users who submitted jobs from within the resource allocation projects (group accounts). This view shows the usage for each user aggregated across systems. Selecting from the list of users will display that user’s usage broken down by cluster. Like the group summaries, these user summaries can then be broken down monthly by clicking the *Show monthly usage* link in the *Extra Info* column of the CPU/GPU Usage (in core/GPU years) table for the specific Resource row.