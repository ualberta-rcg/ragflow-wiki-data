---
title: "Technical support"
slug: "technical_support"
lang: "base"

source_wiki_title: "Technical support"
source_hash: "4788205cb864a2d159b82aebd39a6499"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:52:03.400176+00:00"

tags:
  []

keywords:
  - "job script"
  - "time limit error"
  - "Job submission script"
  - "Cluster name"
  - "SBATCH"
  - "mpiexec"
  - "Support request"
  - "job 123456"
  - "loaded modules"
  - "error logs"
  - "CC Rorqual cluster"
  - "Job ID"
  - "Email addresses"
  - "account access permission"
  - "job cancellation"

questions:
  - "What steps should a user take before sending a support request to ensure it is processed efficiently?"
  - "How should a user determine which specific email address to use for their inquiry?"
  - "What specific details must be included in a support request, and what sensitive information should never be shared?"
  - "How can the user fix the job cancellation error caused by the time limit?"
  - "What software modules were loaded in the user's environment when the job ran?"
  - "What is the required procedure for granting support staff permission to access and inspect a user's account?"
  - "What specific errors did the user encounter with job 123456 on the CC Rorqual cluster?"
  - "What are the SLURM resource allocations and commands specified in the provided job script?"
  - "When was the job submitted and what is the file path to the original script?"
  - "How can the user fix the job cancellation error caused by the time limit?"
  - "What software modules were loaded in the user's environment when the job ran?"
  - "What is the required procedure for granting support staff permission to access and inspect a user's account?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Ask support
* Before writing to us, consider checking first on the [system status page](https://status.computecanada.ca) to see if the problem you're experiencing has already been reported. If you can't find the information you need on our wiki, send an email to the address below that best matches your need.
* **Please ensure that the email address from which you are writing is registered in your [account](https://ccdb.computecanada.ca/email)**. This way, our ticketing system will be able to recognize you automatically.
* A well-written question (or a problem description) will likely result in faster and more accurate assistance from our staff (see a [support request example](#support-request-example) below).
* An email titled "Something is wrong" or "Nothing works" will take a long time to resolve, because we will have to ask you to provide missing information (see [Information required](#information-required) below).
* In the subject line of the email, include the system/cluster name and a few words of what may be wrong. For example, "Job 123456 fails to run on the Rorqual cluster". A good subject line really helps to identify issues at a glance.
* Please do not request help on a different topic as a follow-up to an old email thread. Instead, start a brand new one to avoid reopening an old ticket.

### Email addresses
Please choose the address that corresponds best to your question or issue:
* [accounts@tech.alliancecan.ca](mailto:accounts@tech.alliancecan.ca) -- Questions about accounts
* [renewals@tech.alliancecan.ca](mailto:renewals@tech.alliancecan.ca) -- Questions about account renewals
* [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) -- Questions about **[Globus](globus.md)** file transfer services
* [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca) -- Questions about using **[Cloud](cloud.md)** resources
* [allocations@tech.alliancecan.ca](mailto:allocations@tech.alliancecan.ca) -- Questions about the [Resource Allocation Competition](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition) (RAC)
* [trillium@tech.alliancecan.ca](mailto:trillium@tech.alliancecan.ca) -- For questions or issues regarding the [Trillium](trillium.md) cluster specifically
* **[support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca)** -- For any other question or issue

## Information required
To help us help you better, please include the following information in your support request:
* Cluster name
* Job ID
* Job submission script: you can either give the full path of the script on the cluster; copy and paste the script; or attach the script file
* File or files which contain the error message(s): give the full path of the file(s); copy and paste the file(s); or attach the error message(s) file(s)
* Commands that you were executing
* Avoid sending screenshots or other large image attachments except when necessary - the plain text of your commands, job script, etc. is usually more helpful. See [Copy and paste](faq.md#copy-and-paste) if you have trouble with this.
* Software (name and version) you were trying to use
* When did the problem happen?
* If you want us to access, copy or edit your files, or inspect your account and possibly make changes there, say so explicitly in your email. For example, instead of attaching files to an email, you may indicate where they are located in your account and give us permission to access them. If you have already granted us permission via the CCDB interface to access your files, then you do not need to do it again in your support request.

## Things to beware
* **Never send a password!**
* Maximum attachment size is 40 MB.

## Support request example
!!! example "Support Request Example"
    Here's an example of a well-formatted support request:

    ```text
    To: support@tech.alliancecan.ca
    Subject: Job 123456 gives errors on the CC Rorqual cluster
    ```

    Hello:

    My name is Alice, user `asmith`. Today at 10:00 am MST, I submitted a job 123456 on the Rorqual cluster. The job script is located `/my/job/script/path`. I have not changed it since submitting my job. Since it is short, I included it in the email below:

    ```bash
    #!/bin/bash
    #SBATCH --account=def-asmith-ab
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=16
    #SBATCH --time=00:05:00
    { time mpiexec -n 1 ./sample1 ; } 2>out.time
    ```

    A list of the following modules were loaded at the time:

    ```text
    [asmith@rorqual2]$ module list
    Currently Loaded Modules:
      1) CCconfig   2) gentoo/2023 (S)   3) gcccore/.12.3 (H)   
      4) gcc/12.3 (t)   5) hwloc/2.9.1   6) ucx/1.14.1   
      7) libfabric/1.18.0   8) pmix/4.2.4   9) ucc/1.2.0  
      10) openmpi/4.1.5 (m)  11) flexiblas/3.3.1  12) aocl-blas/5.1  
      13) aocl-lapack/5.1  14) StdEnv/2023 (S)  15) mii/1.1.2
    ```

    The job ran quickly and the `myjob-123456.out` and `myjob-123456.err` files were created. There was no output in the `myjob-123456.out` file but there was a message in the `myjob-123456.err` output:

    ```text
    [asmith@rorqual2 scheduling]$ cat myjob-123456.err
    slurmstepd: error: *** JOB 123456 ON cdr692 CANCELLED AT 2018-09-06T15:19:16 DUE TO TIME LIMIT ***
    ```

    Can you tell me how to fix this problem?

## Access to your account
If you want us to access, copy or edit your files, or inspect your account and possibly make changes there, you should state so explicitly in your email (unless you have provided consent via the CCDB). For example, instead of attaching files to an email, you may tell where they are located in your account and give us written permission to access them.