---
title: "SubatomicPhysics/en"
slug: "subatomicphysics"
lang: "en"

source_wiki_title: "SubatomicPhysics/en"
source_hash: "50a71ed512d7ec9d5522fafdf583bc7a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:42:25.919463+00:00"

tags:
  []

keywords:
  - "Singularity containers"
  - "Compute Canada"
  - "CVMFS repositories"
  - "CVMFS"
  - "setuid environment"
  - "performance benefits"
  - "Singularity"
  - "container"
  - "Subatomic and High Energy Physics"
  - "executable versions"
  - "ATLAS"
  - "CVMFS repository"
  - "Singularity Image"
  - "image caching"

questions:
  - "Why do conflicts occur between the standard Compute Canada environment (CCenv) and the CVMFS repositories from CERN or the Open Science Grid?"
  - "What is the recommended solution for running High Energy Physics software on Compute Canada nodes that lack the required HEP_OSLibs packages?"
  - "What are the two main CVMFS repositories for accessing HEP-related container images, and how are they distributed?"
  - "What are the specific file paths or commands required to load Singularity on the cedar, graham, and niagara systems?"
  - "What are the two different methods available for invoking a container from a CVMFS repository?"
  - "Why might a user choose to pull and store a container image locally rather than invoking it directly from the repository?"
  - "Where are the Singularity images located within the system directory?"
  - "Why is the Singularity executable installed outside of the standard Compute Canada CVMFS stack?"
  - "What is the recommended approach for selecting a Singularity version to run on Compute Canada sites?"
  - "What are the specific file paths or commands required to load Singularity on the cedar, graham, and niagara systems?"
  - "What are the two different methods available for invoking a container from a CVMFS repository?"
  - "Why might a user choose to pull and store a container image locally rather than invoking it directly from the repository?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Subatomic and High Energy Physics Software

This page is maintained by the Compute Canada Subatomic Physics National Team and was last updated July 2021.

There is a reference page for the [Astronomy and High Energy Physics Interactive Analysis Facility](astronomy-and-high-energy-physics-interactive-analysis-facility.md).

Many of the subatomic experimental physics groups are relying on CVMFS repositories from CERN or the Open Science Grid and specific repositories for each experiment.

The CCenv that is set up for regular users can create conflicts with some of the setups from these repositories as standard libraries are provided from the Compute Canada soft.computecanada.ca CVMFS repository which uses Nix and Easybuild to provide access rather than having the software installed on the base OS of the compute nodes.

!!! warning "Note"
    ATLAS users should use the recommended setups for Tier-3 use rather than reinventing techniques that are described below.
*   <https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s>
*   <https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers>

Many setups assume that the base nodes have the [HEP_OSLibs](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/master/README.md) packages/RPMs set up, which is **not** true on the CC computing nodes. One might be able to get away with some simple setups from the 'sft.cern.ch' repository, but the suggested approach is to use Singularity containers which have the necessary RPMs installed, which is described in the next section below. This also allows use of different OS bases (e.g., SL6) on the CentOS7-based Compute Canada infrastructure.

To set up a CentOS7-based view from sft.cern.ch (e.g., with gcc8):

```bash
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_95 x86_64-centos7-gcc8-opt
```

This will include the necessary paths to compilers, Geant4, ROOT, etc.

Available setups for `<arch-os-compiler>` for LCG_95 are:
*   `x86_64-centos7-gcc7-dbg`
*   `x86_64-centos7-gcc7-opt`
*   `x86_64-centos7-gcc8-dbg`
*   `x86_64-centos7-gcc8-opt`
*   `x86_64-slc6-gcc62-opt`
*   `x86_64-slc6-gcc7-dbg`
*   `x86_64-slc6-gcc7-opt`
*   `x86_64-slc6-gcc8-dbg`
*   `x86_64-slc6-gcc8-opt`
*   `x86_64-ubuntu1804-gcc7-opt`
*   `x86_64-ubuntu1804-gcc8-dbg`
*   `x86_64-ubuntu1804-gcc8-opt`

A list of all the RPMs installed via HEP_OSlibs for CentOS7 is available at [this GitLab repository](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt).

### Running in Containers

As of this writing, there are two main repositories for container images that we are aware of for HEP-related software, both distributed via CVMFS repositories. One from ATLAS and the other from WLCG.

*   ATLAS - The ATLAS distributions of Singularity images are documented well at <https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment>
    *   Single file packed images: `/cvmfs/atlas.cern.ch/repo/containers/images/singularity/`
    *   Unpacked images: `/cvmfs/atlas.cern.ch/repo/containers/fs/singularity/`

*   WLCG unpacked repository - This is a development project that uses [DUCC](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html) to automate publishing of container images from a Docker image registry to CVMFS. The images are published to CVMFS in a standard directory structure format that is used by Singularity, as well as the layered format used by Docker, allowing Docker to instantiate images directly from CVMFS using the [graph driver](https://cvmfs.readthedocs.io/en/stable/cpt-graphdriver.html) plugin. There is additional documentation for this project at <https://github.com/cvmfs/ducc>. The list of images that are automatically published is [here](https://gitlab.cern.ch/unpacked/sync/blob/master/recipe.yaml) and includes the `atlas-grid-centos7` image. To add one to the list you can submit a merge request.
    *   Images are under `/cvmfs/unpacked.cern.ch/`

## Invoking Singularity Image

The Singularity executable is provided on Compute Canada sites in slight variants as this is run in a `setuid` environment by default so is installed outside of the usual Compute Canada CVMFS stack. There are various versions available on each site and defaults may be changed, so it is best to invoke the necessary version (as of this writing 2.6.1, 3.2.0, and 3.3.0 are the most likely candidates).

*   cedar: `/opt/software/singularity-x.x.x`
*   graham: `/opt/software/singularity-x.x.x`
*   niagara: `module load singularity; /opt/singularity/2`

Invoking a container from a CVMFS repository can be either done directly as the image will be cached, or the image can be pulled and stored in your local area which may give some performance benefits, depending on the system.