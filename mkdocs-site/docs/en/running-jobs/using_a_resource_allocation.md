---
title: "Using a resource allocation/en"
slug: "using_a_resource_allocation"
lang: "en"

source_wiki_title: "Using a resource allocation/en"
source_hash: "cbfad4a78e7c50156954d43642a0a7ec"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:50:24.089299+00:00"

tags:
  []

keywords:
  - "--account option"
  - "RAC award"
  - "allocation"
  - "Storage allocation"
  - "RAP membership"
  - "submit jobs"
  - "Principal Investigators"
  - "Compute allocation"
  - "Sponsored users"
  - "Job submission"
  - "LDAP group"
  - "Manage RAP Memberships"
  - "Resource Allocation Project"
  - "Cloud resources"
  - "co-PIs"
  - "Resource Allocation Competition"
  - "Resource Allocation Projects"
  - "compute allocation"
  - "CCDB portal"

questions:
  - "What are the main differences between a Default Resource Allocation Project (RAP) and a RAC RAP?"
  - "How do students and collaborators register for their own accounts under a Principal Investigator's sponsorship?"
  - "How can a Principal Investigator manage and restrict which sponsored users have access to their specific RAC allocation?"
  - "How can a Principal Investigator add new members or bulk-add sponsored users to their Resource Allocation Project (RAP)?"
  - "What is the correct way to specify a group name using the `--account` option when submitting jobs to the scheduler?"
  - "How is the `/project` storage allocation structured, and what tool is recommended for transferring large amounts of data to an Alliance cluster?"
  - "Who automatically has access to a RAC award by default?"
  - "Can a user control or restrict which specific individuals are allowed to use their allocation?"
  - "What are the exact steps required to add new members to a Resource Allocation Project (RAP) through the CCDB portal?"
  - "How is RAP membership represented within the system and what privileges does it grant to its users?"
  - "How does the scheduler determine which compute allocation a submitted job is assigned to by default?"
  - "What command option must be specified when submitting a job if a user belongs to more than one Principal Investigator (PI) or group?"
  - "How should users transfer large amounts of data to their allocated storage on the cluster, and how do they locate their specific `/project` directory?"
  - "What is the difference in naming conventions and default user access between cloud resources allocated via the Rapid Access Service (RAS) versus the Resource Allocation Competition (RAC)?"
  - "What are the specific steps a Principal Investigator (PI) must take in the CCDB portal to add or manage members for their Resource Allocation Project (RAP)?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction to RAC

This page is a guide for Principal Investigators (PIs) who have applied to the Alliance's [Resource Allocation Competition (RAC)](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition), peer-reviewed processes to grant priority access to storage and compute resources beyond what can be obtained via the [Rapid Access Service](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service).

Your award may have come from one of these processes:
- Resources for Research Groups (RRG)
- Research Platforms and Portals (RPP)

You will be notified of the results of your application before the start of the new RAC year. The RAC year typically begins the first week of April, so you should expect notification sometime in March. You and your sponsored users can begin to use the awarded resources at the beginning of the RAC year.

## Projects, group names, and allocations

Alliance resources are made available to PIs through Resource Allocation Projects (RAP). Each RAP has a project identifier (RAPI) and an associated group name.

In general, there are two main types of RAPs:
- **Default RAP:** A default RAP is automatically created when a PI role is activated. Default quotas and Rapid Access Service quotas for storage and cloud resources are managed via this default RAP. The Default RAP allows PIs and sponsored users to make opportunistic use of compute resources with the default (that is, the lowest) priority. The default RAPI typically takes the form `abc-123-aa` and has an associated group name that follows the convention `def-profname`.
- **RAC RAP:** This RAP is created when the PI receives an award through the Resource Allocation Competition. The RAC RAPI typically takes the form `abc-123-ab`, with an associated group name that follows the convention `rrg-profname` or `rpp-profname` for HPC resources, or `cpp-profname` or `crg-profname` for cloud resources.

A RAC award consists of one or more **allocations**. Each allocation consists of a resource (such as `nibi-cpu`, `nibi-gpu`, `nibi-storage`) and an amount, and has a designation like `abc-123-aa-001`.

You can find RAPIs and their corresponding group names and allocations by visiting the [CCDB portal](https://ccdb.alliancecan.ca).
For more details on accounts and projects, see [Running jobs: Accounts and projects](running_jobs.md#accounts-and-projects).

For more details about RAP and RAP memberships, visit the [CCDB FAQ page](../getting-started/frequently_asked_questions_about_the_ccdb.md).

## Sponsored users

Alliance accounts are *per person:* Account sharing is strictly forbidden. Each of your students, employees, or collaborators who will use the resources should therefore obtain their own account under your sponsorship. They should go to the [CCDB](https://ccdb.alliancecan.ca) to register in their own name, using your CCRI to indicate your sponsorship when filling out the web form. You (the sponsor) will receive an email with a link to click on to confirm the sponsorship of this individual. There is no limit on the number of sponsored accounts that a PI can have, but such sponsorship should only be in the context of a genuine and sustained research collaboration. More details on the process of obtaining an Alliance account are available [here](https://alliancecan.ca/en/services/advanced-research-computing/account-management/apply-account).

# Information on each resource

For more information, please click on the tab below corresponding to where you have been granted resources. *General-purpose clusters* are [Rorqual](../clusters/rorqual.md), [Fir](../software/fir.md), [Nibi](../clusters/nibi.md) and [Narval](../clusters/narval.md). More than one tab may apply if, for example, you have been granted an allocation on both [Trillium](../clusters/trillium.md) and a general-purpose cluster.

=== "General-purpose clusters"

    ### Who can use the allocation?

    !!! note "Information for RAC Allocations"
        Information in this section is for RAC allocations and RAC projects.

    By default, every role that you have sponsored through your Alliance CCDB registration has access to your RAC award. Any co-PIs that were listed on your RAC application will also have access.

    If desired, you can select which users may use your allocation. To do so:

    1. Log in at [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/)
    2. From the *My Account* menu, select *Manage RAP Memberships*. This will take you to [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members). In the *Resource Allocation Project (RAP)* drop-down list on this page, select the RAP to which you want to add members.
    3. To add a new member, go to *Add Members* and enter the CCRI of the user you want to add. Once added, you will see the new member highlighted in yellow.
    4. If you add a new PI as a member, you can add any of their sponsored users or co-PIs at the same time. Go to *Add Members* and click on the *In bulk* link: this will take you to a new page where you can add all or several of the roles associated with that PI at once. If you do not see the name of the user that you are looking for in that list, then click on *Cancel* to go back to the RAP membership page and return to step 3.

    RAP membership is represented as a group in LDAP. It defines a group of users that are authorized to submit jobs against the RAPI (which is the ID of the RAP) and share files within the same Unix group.

    ### Using a compute allocation

    When submitting jobs to the scheduler, users will need to specify a group name as the value of the `--account` option. Jobs pertaining to the research described in the RAC application should be submitted with the group name corresponding to the RAC award, e.g., `--account=rrg-profname-ab`. Jobs pertaining to other research should be submitted with the default group name, e.g., `--account=def-profname`.

    See [Running jobs: Accounts and projects](running_jobs.md#accounts-and-projects) for more details.

    ### Using allocated storage

    If you have substantial amounts of data to transfer to an Alliance cluster in order to use your storage allocation, we strongly recommend the use of [Globus](../getting-started/globus.md).

    #### `/project`

    A `/project` storage allocation on a general-purpose cluster is created as a directory of the form `/project/<group-name>`, e.g., `/project/rrg-profname-ab`, and an associated quota defining the amount of data that can be stored in the directory. Files pertaining to the research described in the RAC application should be stored there by all sponsored users. More guidance on the use of `/project` space can be found at [Project layout](../storage-and-data/project_layout.md) and [Sharing data](../storage-and-data/sharing_data.md).

    Note that you will also have default project space of the form `/project/def-profname`. You may wish to move data from that default project space to the RRG or RPP `/project` directory, if the data pertains to the research described in the RAC application.

    #### `/nearline`

    Please see [Using nearline storage](../storage-and-data/using_nearline_storage.md).

=== "Trillium"

    ### Who can use the allocation?

    By default, every role that you have sponsored through your Alliance CCDB registration has access to your RAC award. Any co-PIs that were listed on your RAC application will also have access.

    If desired, you can select which users may use your allocation. To do so:

    1. Log in at [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/)
    2. From the *My Account* menu, select *Manage RAP Memberships*. This will take you to [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members). In the *Resource Allocation Project (RAP)* drop-down list on this page, select the RAP to which you want to add members.
    3. To add a new member, go to *Add Members* and enter the CCRI of the user you want to add. Once added, you will see the new member highlighted in yellow.
    4. If you add a new PI as a member, you can add any of their sponsored users or co-PIs at the same time. Go to *Add Members* and click on the *In bulk* link: this will take you to a new page where you can add all or several of the roles associated with that PI at once. If you do not see the name of the user that you are looking for in that list, then click on *Cancel* to go back to the RAP membership page and return to step 3.

    RAP membership is represented as a group in LDAP. It defines a group of users that are authorized to submit jobs against the RAPI (which is the ID of the RAP) and share files within the same Unix group.

    ### Using a compute allocation

    When a user submits a job to the scheduler, the job will be assigned to the current allocation of the user's PI. If the user has more than one PI, i.e. more than one group, they must specify a group name as the value of the `--account` option.

    See [Running jobs: Accounts and projects](running_jobs.md#accounts-and-projects) for more details.

    ### Using allocated storage

    If you have substantial amounts of data to transfer to the cluster in order to use your storage allocation, we strongly recommend the use of [Globus](../getting-started/globus.md).

    #### `/project`

    The location of a `/project` storage allocation on Niagara should be found by using the environment variable `$PROJECT`. This variable will point to a user-specific directory in the research group's project space.

    #### `/nearline`

    A `/nearline` allocation on Niagara means space in HPSS. Please see [Using nearline storage](../storage-and-data/using_nearline_storage.md).

=== "Cloud"

    Cloud resources allocated via the Rapid Access Service (RAS) use the default RAP.

    Cloud resources allocated via the Resource Allocation Competition are awarded through a RAC RAP which follows a different naming convention than default projects. The group name of RAC RAPs with cloud allocations typically takes the form of `crg-profname` (for cloud resources allocated to a research group) or `cpp-profname` (for cloud resources allocated to a research platform or portal).

    ### Who can use the allocation?

    If you have an active cloud resource allocation, you should already have a RAP and therefore access to the particular cloud on which you have an allocation.

    - **Default RAP:** Cloud resources granted to you via RAS are allocated through your default RAP. All your activated sponsored user roles are always members of your default RAP. That is, confirming sponsorship of a user confers on them membership in your default RAP. However, you can at any time deactivate any role you sponsor.
    - **RAC RAP:** By default, only the PI is added as a member of a RAP associated with cloud resources allocated via the Resource Allocation Competition. If desired, you can add sponsored users and/or other active Alliance users as members to the RAP. Only members added to your RAP can use your cloud allocation.

    If desired, you can select which users may use your allocation. To do so:

    1. Log in at [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/)
    2. From the *My Account* menu, select *Manage RAP Memberships*. This will take you to [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members). In the *Resource Allocation Project (RAP)* drop-down list on this page, select the RAP to which you want to add members.
    3. Go to *Add Members*, and click on the *In bulk* link: this will take you to a new page that will allow you to easily add co-PIs and any of their associated sponsored user roles.
    4. If the *In bulk* page in step 3 above does not show the name of the user that you want to add, then click on *Cancel* to go back to the RAP membership page. Once there, go to the *Add Members* section, and enter the CCRI of the member in the *One by one using a CCRI* field.
    5. Following step 4 will allow you to add an associated PI that was not included as co-PI in your RAC application. Once a new PI is added as a member to your RAP using this process, you will be able to add any of their associated sponsored user roles through the *In bulk* mechanism explained in step 3.

    !!! important
        - Any new member added to a RAP for your cloud project will automatically have access to your cloud allocation. If desired, at any time you can promote members to Managers, or remove members.
        - Membership in your Cloud RAP allows full access to your OpenStack tenants. For more details, see our wiki page on OpenStack projects.

    For information about logging in and using a particular cloud see [using the cloud](../cloud/cloud.md). If you are unsure about your cloud allocation or if you have difficulty logging into a cloud where you have an allocation, please contact [technical support](../support/technical_support.md).