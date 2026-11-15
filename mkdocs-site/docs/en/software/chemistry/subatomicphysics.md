---
title: "SubatomicPhysics/en"
slug: "subatomicphysics"
lang: "en"

source_wiki_title: "SubatomicPhysics/en"
source_hash: "a0342e34bf86cb15a90ccb5742e97194"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:46:11.942280+00:00"

tags:
  []

keywords:
  - "HEP_OSLibs"
  - "CVMFS repository"
  - "CVMFS repositories"
  - "container invocation"
  - "image caching"
  - "local storage"
  - "Compute Canada"
  - "atlas-grid-centos7 image"
  - "merge request"
  - "Apptainer"
  - "performance benefits"
  - "Singularity containers"
  - "singularity"
  - "ATLAS Tier-3"
  - "cvmfs/unpacked.cern.ch"

questions:
  - "What are the recommended setups for ATLAS users on Compute Canada Tier‑3 resources to avoid conflicts with the CCenv environment?"
  - "How can a user configure a CentOS 7 view from the CERN sft.cern.ch repository on Compute Canada nodes, and which <arch‑os‑compiler> options are available for LCG_95?"
  - "Where are the HEP‑related Singularity (Apptainer) container images hosted, and how are they accessed or invoked on Compute Canada systems such as Trillium?"
  - "What are the two ways to invoke a container from a CVMFS repository?"
  - "How does invoking the container directly rely on caching of the image?"
  - "When might pulling the image to local storage provide performance benefits?"
  - "Where can the `recipe.yaml` file be accessed and which container image does it currently include?"
  - "What is the process for adding a new image to the list of available containers?"
  - "How are containers executed on Trillium, and what is the role of Apptainer versus the `singularity` symlink?"

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

There is a reference page for the Astronomy and High Energy Physics Interactive Analysis Facility.

Many of the subatomic experimental physics groups are relying on CVMFS repositories from CERN or the Open Science Grid and specific repositories for each experiment.

The CCenv that is set up for regular users can create conflicts with some of the setups from these repositories as standard libraries are provided from the Compute Canada soft.computecanada.ca CVMFS repository which uses Nix and Easybuild to provide access rather than having the software installed on the base OS of the compute nodes.

For ATLAS users, there are pages housed on the TRIUMF twiki that should be helpful.

!!! note "ATLAS Users"
    ATLAS users should use the recommended setups for Tier-3 use rather than reinventing techniques that are described below.

* <https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s>
* <https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers>

Many setups assume that the base nodes have the [HEP_OSLibs](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/master/README.md) packages/rpms setup[^1], which is **not** true on the CC computing nodes. One might be able to get away with some simple setups from the 'sft.cern.ch' repository, but the suggested approach is to use singularity containers which have the necessary rpm's installed, which is described in the next section below. This also allows use of different OS bases (e.g. SL6) on the CentOS7-based Compute Canada infrastructure.

To set up a CentOS7 based view from sft.cern.ch (e.g. with gcc8):

```bash
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_95 x86_64-centos7-gcc8-opt
```

This will include the necessary paths to compilers, geant4, ROOT, etc.

Available setups for `<arch-os-complier>` for LCG_95 are:
* `x86_64-centos7-gcc7-dbg`
* `x86_64-centos7-gcc7-opt`
* `x86_64-centos7-gcc8-dbg`
* `x86_64-centos7-gcc8-opt`
* `x86_64-slc6-gcc62-opt`
* `x86_64-slc6-gcc7-dbg`
* `x86_64-slc6-gcc7-opt`
* `x86_64-slc6-gcc8-dbg`
* `x86_64-slc6-gcc8-opt`
* `x86_64-ubuntu1804-gcc7-opt`
* `x86_64-ubuntu1804-gcc8-dbg`
* `x86_64-ubuntu1804-gcc8-opt`

[^1]: A list of all the rpm's installed via HEPOS_Libs for CentOS7 is available at <https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt>

### Running in containers

As of this writing there are two main repositories for container images that we are aware of for HEP-related software, both distributed via CVMFS repositories. One from ATLAS and the other from WLCG.

*   ATLAS - The ATLAS distributions of Singularity images are documented well at <https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment>
    *   Single file packed images: `/cvmfs/atlas.cern.ch/repo/containers/images/singularity/`
    *   Unpacked images: `/cvmfs/atlas.cern.ch/repo/containers/fs/singularity/`

*   WLCG unpacked repository - This is a development project that uses [DUCC](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html) to automate publishing of container images from a Docker image registry to CVMFS. The images are published to CVMFS in a standard directory structure format that is used by Singularity, as well as the layered format used by Docker, allowing Docker to instantiate images directly from CVMFS using the [graph driver](https://cvmfs.readthedocs.io/en/stable/cpt-graphdriver.html) plugin. There is additional documentation for this project at <https://github.com/cvmfs/ducc>. The list of images that are automatically published is [here](https://gitlab.cern.ch/unpacked/sync/blob/master/recipe.yaml) and includes the atlas-grid-centos7 image. To add one to the list you can submit a merge request.
    *   Images are under `/cvmfs/unpacked.cern.ch/`

## Invoking Singularity Image

On Trillium, containers are run with [Apptainer](../containers/apptainer.md), which is installed system-wide. The `apptainer` command is available, and `/usr/bin/singularity` is a symbolic link to it.

Invoking a container from a CVMFS repository can be done directly as the image will be cached, or the image can be pulled and stored in your local area which may give some performance benefits, depending on the system.