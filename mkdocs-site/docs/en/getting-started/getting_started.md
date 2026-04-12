---
title: "Getting started/en"
slug: "getting_started"
lang: "en"

source_wiki_title: "Getting started/en"
source_hash: "674756343cd696cfa8af3978b14347a4"
last_synced: "2026-04-12T15:59:52.668416+00:00"
last_processed: "2026-04-12T18:10:06.582726+00:00"

tags:
  []

keywords:
  - "Regional partners"
  - "Online training"
  - "Cloud resources"
  - "Job submission"
  - "Training"
  - "Linux operating system"
  - "Research computing"
  - "computing power"
  - "Technical support"
  - "Workshops"
  - "appropriate resources"
  - "CCDB account"
  - "technical support"
  - "job requirements"
  - "HPC clusters"

questions:
  - "What credentials are required to log into the national HPC systems, and where can users find their username?"
  - "What are the different types of computing systems available, such as cloud sites and general-purpose clusters, and what are their primary functions?"
  - "What specific software and hardware requirements should users evaluate when deciding which system is best suited for their computational needs?"
  - "What formats and levels of training are offered by the Alliance's regional partners?"
  - "Which specific regional partners organize these workshops and provide dedicated training resources?"
  - "Where can individuals find a complete, merged list of all upcoming training events?"
  - "What specific technical specifications and resource estimates are needed to evaluate a typical job?"
  - "What steps should you take if you do not know the answers to the technical questions regarding your job?"
  - "How will the technical support team use your job requirements to assist you?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## What do you want to do?
*   If you don't already have an account, see
    *   [Apply for a CCDB account](apply_for_a_ccdb_account.md)
    *   [Multifactor authentication](multifactor_authentication.md)
    *   [Frequently Asked Questions about the CCDB](frequently_asked_questions_about_the_ccdb.md)
*   If you are an experienced HPC user and are ready to log into a cluster, you probably want to know
    *   [what systems are available](#what-systems-are-available);
    *   [what software is available](../programming/available_software.md);
    *   [how environment modules work](../programming/utiliser_des_modules.md);
    *   [how to submit jobs](../running-jobs/running_jobs.md);
    *   [how filesystems are organized](../storage-and-data/storage_and_file_management.md).
*   If you are new to HPC, you can
    *   [read about how to connect to our HPC systems with SSH](ssh.md);
    *   [read an introduction to Linux systems](linux_introduction.md);
    *   [read about how to transfer files to and from our systems](transferring_data.md);
*   If you want to know which software and hardware are available for a specific discipline, a series of discipline guides is in preparation. At this time, you can consult the guides on
    *   [AI and Machine Learning](../software/ai-ml/ai_and_machine_learning.md)
    *   [Bioinformatics](../software/bioinformatics/bioinformatics.md)
    *   [Biomolecular simulation](../software/molecular-sim/biomolecular_simulation.md)
    *   [Computational chemistry](../software/chemistry/computational_chemistry.md)
    *   [Computational fluid dynamics](../programming/computational_fluid_dynamics.md) (CFD)
    *   Geographic information systems ([GIS](../software/gis.md))
    *   [Visualization](../software/visualization.md)
*   If you have hundreds of gigabytes of data to move across the network, [read about the Globus file transfer service](globus.md).
*   Python users can learn how to [install modules in a virtual environment](../software/python.md#creating-and-using-a-virtual-environment).
*   R users can learn how to [install packages](../software/r.md).
*   If you want to experiment with software that doesn’t run well on our HPC clusters, [read about our cloud resources](../cloud/cloud.md).

For any other questions, you might try the *Search* box in the upper right corner of this page, the main page for [our technical documentation](../general/technical_documentation.md) or [contact us by email](../support/technical_support.md).

## Username and password
Your password to log in to all new national systems is [the same one you use to log into CCDB](https://ccdb.alliancecan.ca/). Your **username** will be displayed at the top of the page once you've logged in.

## What systems are available?
You can [request access](https://ccdb.alliancecan.ca/me/access_systems) to any or all of our systems: [Arbutus](../cloud/cloud_resources.md), [Fir](../software/fir.md), [Narval](../clusters/narval.md), [Nibi](../clusters/nibi.md), [Rorqual](../clusters/rorqual.md), and [Trillium](../clusters/trillium.md).

*   [Arbutus](../cloud/cloud_resources.md) is a cloud site, which allows users to launch and customize virtual machines. See [Cloud](../cloud/cloud.md) for how to obtain access to Arbutus.

*   [Fir](../software/fir.md), [Narval](../clusters/narval.md), [Nibi](../clusters/nibi.md), and [Rorqual](../clusters/rorqual.md) are **general-purpose clusters** (or supercomputers) composed of a variety of nodes including large memory nodes and nodes with accelerators such as GPUs. You can log into any of these using [SSH](ssh.md). A `/home` directory will be automatically created for you the first time you log in.

*   [Trillium](../clusters/trillium.md) is a homogeneous cluster (or supercomputer) designed for **large parallel** jobs (>1000 cores).

In this documentation, we generally use the term “cluster” instead of “supercomputer” since it better reflects the architecture of our systems: A large number of individual computers, or “nodes”, linked together as a unit, or “cluster”.

## What system should I use?
This question is hard to answer because of the range of needs we serve and the wide variety of resources we have available. If the descriptions above are insufficient, contact our [technical support](../support/technical_support.md).

In order to identify the best resource to use, we may ask specific questions, such as:
*   What software do you want to use?
    *   Does the software require a commercial license?
    *   Can the software be used non-interactively? That is, can it be controlled from a file prepared prior to its execution rather than through a graphical interface?
    *   Can it run on the Linux operating system?
*   How much memory, time, computing power, accelerators, storage, network bandwidth and so forth—are required by a typical job? Rough estimates are fine.
*   How frequently will you need to run this type of job?

You may know the answer to these questions or not. If you do not, our technical support team is there to help you find the answers. They will then be able to direct you to the most appropriate resources for your needs.

## What training is available?
Most workshops are organized by the Alliance's regional partners; both online and in-person training opportunities exist on a wide variety of subjects and at different levels of sophistication. We invite you to consult the following regional training calendars and websites for more information,
*   WestDRI (Western Canada Research Computing covering both BC and the Prairies regions)
    *   [Training Materials website](https://training.westdri.ca): click on *Upcoming sessions* or browse the menu at the top for recorded webinars
    *   [UAlberta ARC Bootcamp](https://www.ualberta.ca/information-services-and-technology/research-computing/bootcamps.html): videos of previous sessions available
*   [SHARCNET](https://www.sharcnet.ca)
    *   [Training Events Calendar](https://www.sharcnet.ca/my/news/calendar)
    *   [YouTube Channel](http://youtube.sharcnet.ca/)
    *   [Online Workshops](https://training.sharcnet.ca/)
*   [SciNet](https://www.scinethpc.ca)
    *   [SciNet Education Site](https://education.scinet.utoronto.ca)
    *   [SciNet YouTube Channel](https://www.youtube.com/c/SciNetHPCattheUniversityofToronto)
*   [Calcul Québec](https://www.calculquebec.ca/en/)
    *   [Workshops](https://calculquebec.eventbrite.ca/)
    *   [Training information](https://www.calculquebec.ca/en/academic-research-services/training/)
*   [ACENET](https://www.ace-net.ca/)
    *   [Training information](https://www.ace-net.ca/training.html)
    *   [ACENET YouTube Channel](https://www.youtube.com/@ACENETDRI)
See the complete and merged list of [upcoming training events on Explora](https://explora.alliancecan.ca/events).