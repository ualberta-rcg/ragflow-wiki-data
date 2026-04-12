---
title: "Clusterstats"
slug: "clusterstats"
lang: "base"

source_wiki_title: "Clusterstats"
source_hash: "8429c251646ffb9e9cfd3c562bc10b1c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:28:53.295683+00:00"

tags:
  []

keywords:
  - "computing nodes"
  - "Down (Nodes)"
  - "job ranking"
  - "LevelFS"
  - "GPU nodes"
  - "Nodes"
  - "cluster"
  - "Partitions"
  - "partition"
  - "available resources"
  - "User Account"
  - "Cluster Information"
  - "Clusterstats"
  - "cpu=32"
  - "Jobs"
  - "Accounting group"
  - "cpu"
  - "Mem"
  - "Mem=3095000"
  - "v100 GPUs"
  - "scontrol command"
  - "Job information"
  - "job priority"
  - "Basic summary"
  - "job information"
  - "CPU cores"
  - "system memory"
  - "node status"
  - "pending job"
  - "job state"
  - "Fairshare"
  - "GPU RAM"

questions:
  - "What is the primary purpose of the clusterstats utility and what specific types of information does it display?"
  - "How do users interact with and navigate the main menu of clusterstats once the data has loaded?"
  - "How does the utility organize and present cluster resource data in relation to node types and maximum job run-times?"
  - "What are the specific CPU and memory configurations for the nodes detailed in the text?"
  - "How many nodes are currently reported as \"Down\" in the system?"
  - "What is the significance of the numerical values distributed across the columns for each node category?"
  - "How do you interpret the hardware specification strings, such as \"v100l:4, cpu=32, Mem=192000\", in the cluster information tables?"
  - "How does the table represent the availability of a resource across different job duration limits, such as a 0-24 hour job?"
  - "What are the different operational states used to categorize the GPU nodes in the provided table?"
  - "What specific metrics and Fairshare values are displayed when viewing information about an accounting group?"
  - "How does the user account table differ from the group information table in terms of the data presented?"
  - "What details are included in the \"Basic\" summary when querying information about a specific user job?"
  - "What specific GPU hardware and VRAM capacity does the \"v100l:4\" designation indicate?"
  - "How many CPU cores are allocated to the nodes described in the configuration string?"
  - "What does the value \"192000\" represent in the context of the node's system memory?"
  - "How is the priority rank of a job determined and what does it signify in relation to other jobs?"
  - "What specific information about node availability and hardware types is provided when selecting the \"Report\" option for a pending job?"
  - "Which option should be selected to view more detailed diagnostic information about a job, and what command generates this output?"
  - "What are the three information options you can select from to learn more about a given job?"
  - "What specific details are displayed in the one-line summary when the \"Basic\" option is selected?"
  - "Under what specific job state will the \"Basic\" summary include the rank of the job?"
  - "How is the priority rank of a job determined and what does it signify in relation to other jobs?"
  - "What specific information about node availability and hardware types is provided when selecting the \"Report\" option for a pending job?"
  - "Which option should be selected to view more detailed diagnostic information about a job, and what command generates this output?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Cluster Information

Clusterstats is a custom utility which displays information on partitions, nodes, jobs, your account, your group(s), and your priority.

To run clusterstats, just type the command on a cluster.

```bash
clusterstats
```

Clusterstats may take a few minutes to update and get fresh data, or it may use some recently-cached data.

```text
[✔] Loading node information (success, loaded cached version that is 2 min old)
[✔] Loading job information (success, loaded cached version that is 2 min old)
[✔] Loading share information (success, loaded cached version that is 1 min old)
```

Once the data is loaded, the main menu will appear asking if you would like information about your user, your group, or the state of the cluster. You can scroll up and down with the arrow keys, and make a selection with the "Enter" key. You can move back a level by selecting "Back" and quit the program by selecting "Quit".

```text
Information on? (Use arrow keys, press Enter to select)
‣ User
  Group
  Cluster
  Quit
```

### Information on the Cluster

You will be asked a number of questions about what part of the cluster you wish to see, and what type of information you wish to display. Once you do, you will see a table listing the resources grouped by node type, and by the maximum run-time of jobs those nodes allow. Notice that the longer the run-time of a job is, the fewer resources are available to it.

```text
Information on? Cluster
Please select on which part of the cluster would you like more information? CPU, (highmem or large) more than 12 GB of RAM per Core
Information on ? Jobs/Partitions/Nodes for whole node jobs
Please select the information you would like to display? Nodes
```

!!! note
    This table shows all available resources in the partition. A resource that is available to run 0-24 hour jobs will show up in the (0-3), (3-12), and (12-24) columns.

| cpularge_bynode       | interactive | 0-3 hr | 3-12 hr | 12-24 hr | 1-3 day | 3-7 day | 7-28 day |
| :-------------------- | :---------- | :----- | :------ | :------- | :------ | :------ | :------- |
| Total (Nodes)         | 2           | 50     | 50      | 50       | 35      | 17      | 7        |
| &nbsp;&nbsp;cpu=32, Mem=3095000 | 0           | 4      | 4       | 4        | 4       | 1       | 1        |
| &nbsp;&nbsp;cpu=32, Mem=1547000 | 0           | 24     | 24      | 24       | 16      | 8       | 3        |
| &nbsp;&nbsp;cpu=32, Mem=515000  | 2           | 22     | 22      | 22       | 15      | 8       | 3        |
| Idle (Nodes)          | 2           | 0      | 0       | 0        | 0       | 0       | 0        |
| &nbsp;&nbsp;cpu=32, Mem=515000  | 2           | 0      | 0       | 0        | 0       | 0       | 0        |
| Running (Nodes)       | 0           | 46     | 46      | 46       | 34      | 17      | 7        |
| &nbsp;&nbsp;cpu=32, Mem=3095000 | 0           | 3      | 3       | 3        | 3       | 1       | 1        |
| &nbsp;&nbsp;cpu=32, Mem=1547000 | 0           | 21     | 21      | 21       | 16      | 8       | 3        |
| &nbsp;&nbsp;cpu=32, Mem=515000  | 0           | 22     | 22      | 22       | 15      | 8       | 3        |
| Down (Nodes)          | 0           | 4      | 4       | 4        | 1       | 0       | 0        |
| &nbsp;&nbsp;cpu=32, Mem=3095000 | 0           | 1      | 1       | 1        | 1       | 0       | 0        |
| &nbsp;&nbsp;cpu=32, Mem=1547000 | 0           | 3      | 3       | 3        | 0       | 0       | 0        |

**cpu=32, Mem=515000** means that the nodes in that row have 32 CPU cores and 515,000 MiB of system memory (RAM).

An example for GPU nodes:

```text
Please select on which part of the cluster would you like more information? GPU
Information on ? Jobs/Partitions/Nodes for whole node jobs
Please select the information you would like to display? Nodes
```

!!! note
    This table shows all available resources in the partition. A resource that is available to run 0-24 hour jobs will show up in the (0-3), (3-12), and (12-24) columns.

| gpubase_bynode                | interactive | 0-3 hr | 3-12 hr | 12-24 hr | 1-3 day | 3-7 day | 7-28 day |
| :---------------------------- | :---------- | :----- | :------ | :------- | :------ | :------ | :------- |
| Total (Nodes)                 | 2           | 336    | 336     | 270      | 204     | 120     | 60       |
| &nbsp;&nbsp;p100:4 , cpu=24, Mem=128000 | 2           | 112    | 112     | 88       | 64      | 32      | 16       |
| &nbsp;&nbsp;p100l:4, cpu=24, Mem=257000 | 0           | 32     | 32      | 28       | 24      | 12      | 6        |
| &nbsp;&nbsp;v100l:4, cpu=32, Mem=192000 | 0           | 192    | 192     | 154      | 116     | 76      | 38       |
| Idle (Nodes)                  | 1           | 2      | 2       | 1        | 1       | 1       | 1        |
| &nbsp;&nbsp;p100:4 , cpu=24, Mem=128000 | 1           | 0      | 0       | 0        | 0       | 0       | 0        |
| &nbsp;&nbsp;p100l:4, cpu=24, Mem=257000 | 0           | 2      | 2       | 1        | 1       | 1       | 1        |
| Running (Nodes)               | 0           | 315    | 315     | 254      | 194     | 116     | 57       |
| &nbsp;&nbsp;p100:4 , cpu=24, Mem=128000 | 0           | 104    | 104     | 83       | 62      | 31      | 16       |
| &nbsp;&nbsp;p100l:4, cpu=24, Mem=257000 | 0           | 26     | 26      | 23       | 20      | 11      | 5        |
| &nbsp;&nbsp;v100l:4, cpu=32, Mem=192000 | 0           | 185    | 185     | 148      | 112     | 74      | 36       |
| Down (Nodes)                  | 1           | 19     | 19      | 15       | 9       | 3       | 2        |
| &nbsp;&nbsp;p100:4 , cpu=24, Mem=128000 | 1           | 8      | 8       | 5        | 2       | 1       | 0        |
| &nbsp;&nbsp;p100l:4, cpu=24, Mem=257000 | 0           | 4      | 4       | 4        | 3       | 0       | 0        |
| &nbsp;&nbsp;v100l:4, cpu=32, Mem=192000 | 0           | 7      | 7       | 6        | 4       | 2       | 2        |

**v100l:4, cpu=32, Mem=192000** means that the nodes in that row have 4 V100 GPUs with 32 GB of GPU RAM (V100l) as well as 32 CPU cores and 192,000 MiB of system memory (RAM).

### Information on your Group(s)

When you choose "Information on Group", you will be prompted to select one of the accounting groups that you belong to. You will see a table of all the users who are members of that accounting group, the group's share of the cluster and how much the group has recently used it, each member's share of the group and how much that member has recently used it, and Fairshare values derived therefrom. The group's LevelFS is the group's share of the cluster divided by the group's use. Fairshare is the main component of the priority of any job.

```text
Information on? Group
Information on Job ? def-kamil-ab_cpu
```

| Account          | User     | Group     | Group     | Group    | User's  | User's  | User's        |
| :--------------- | :------- | :-------- | :-------- | :------- | :------ | :------ | :------------ |
|                  |          | Share     | Used      | LevelFS  | Share   | Used    | Fairshare     |
|                  |          | % Cluster | % Cluster |          | % Group | % Group | Using Account |
| def-kamil-ab_cpu | kamil    | SLEEPING  | 0.0       | SLEEPING | 50.0    | 100.0   | SLEEPING      |
| def-kamil-ab_cpu | tmcguire | SLEEPING  | 0.0       | SLEEPING | 50.0    | 0.0     | SLEEPING      |

In this example, user kamil has 50% of the group's share but used 100% of the resources used by the group. The default group def-kamil-ab_cpu has used almost zero resources and is currently inactive.

Shares of active default groups are set to the (unallocated resources / number of active default groups). Inactive default groups get no share and are labelled as SLEEPING; when a group member submits a job, the group is soon classified as active.

### Information on the User

If you choose "Information on User", you will be asked to select "Account" or "Jobs".

#### User Account Table

Select "Account" and you will get information in a table for all the groups you are a member of, as described in the Groups section above, but you will not see the other group members.

```text
Information on? User
Information on ? Account
```

| Account          | Group     | Group     | Group    | kamil's | kamil's | kamil's       |
| :--------------- | :-------- | :-------- | :------- | :------ | :------ | :------------ |
|                  | Share     | Used      | LevelFS  | Share   | Used    | Fairshare     |
|                  | % Cluster | % Cluster |          | % Group | % Group | Using Account |
| def-kamil-ab_cpu | SLEEPING  | 0.0       | SLEEPING | 50.0    | 100.0   | SLEEPING      |
| def-kamil-ab_gpu | SLEEPING  | 0.0       | SLEEPING | 50.0    | 100.0   | SLEEPING      |
| rrg-kamil_gpu    | 0.0495    | 0.0815    | 0.606848 | 6.25    | 75.8338 | 0.325922      |

#### User Jobs Options

If you select "Jobs", and you have any jobs running or pending, you will be prompted to select a particular job you wish more information on. For a given job, you can select "Basic", "Report", or "Output of the scontrol command". Selecting "Basic" will print a one-line summary giving the job's state (pending, running, or recently completed), its partition, its priority, and if pending, its rank.

```text
Information on ? Basic
Job:46460857 state: pending partition: cpubase_bycore_b4 priority: 1618298
    This job is ranked 1517 of 7825 in terms of priority
```

The rank has the following meaning: The nodes that can potentially run the job can also run 7,825 other jobs. When all these jobs are ranked by priority from highest to lowest, this job is 1,517th.

Selecting "Report" will show the nodes that your job can run on and the state of those nodes.

```text
Information on ? Report
Job 65066247:
    This pending job belongs to user kamil, accounting group rrg-kamil_gpu in partition gpubase_bynode_b5
    Nodes that can possibly run the job:
      Total: 120 Busy: 116 Down: 3 Idle: 1
        Node Type (p100:4, cpu=24, Mem=128000):  Total 32 Down 1 Idle 0
        Node Type (p100l:4, cpu=24, Mem=257000):  Total 12 Down 0 Idle 1
        Node Type (v100l:4, cpu=32, Mem=192000):  Total 76 Down 2 Idle 0
      This job is ranked 46 of 3737 in terms of priority on these nodes
```

Selecting "Output of the scontrol command" will display more detailed diagnostics obtained from `scontrol show job`.