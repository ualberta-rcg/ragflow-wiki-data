---
title: "EasyBuild"
slug: "easybuild"
lang: "base"

source_wiki_title: "EasyBuild"
source_hash: "96131e50ca04d3beebefd12001a13bc6"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:11:44.446480+00:00"

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

[EasyBuild](https://easybuild.io/) is a tool for building, installing, and maintaining software on high-performance computing systems. We use it to build almost everything in our software repository, [CVMFS](accessing-cvmfs.md).

## EasyBuild and modules
One of the key features of EasyBuild is that it automatically generates environment [modules](utiliser-des-modules/en.md) which can be used to make a software package available in your session. In addition to defining standard Linux environment variables such as `PATH`, `CPATH` and `LIBRARY_PATH`, EasyBuild also defines some environment variables specific to EasyBuild, two of which may be particularly interesting to users:
*   `EBROOT<name>`: Contains the full path to the location where the software `<name>` is installed.
*   `EBVERSION<name>`: Contains the full version of the software `<name>` loaded by this module.

For example, the module `python/3.10.2` on Narval defines:
*   `EBROOTPYTHON`: `/cvmfs/soft.computecanada.ca/easybuild/software/2020/avx2/Core/python/3.10.2`
*   `EBVERSIONPYTHON`: `3.10.2`

You can see the environment variables defined by the `python/3.10.2` module using:
```bash
module show python/3.10.2 | grep EB
```

## Installation recipes and logs
EasyBuild keeps a copy of the recipe used to install each software package, as well as a detailed log inside the installation directory. This is accessible in the directory `$EBROOT<name>/easybuild`. For example, for the `python/3.10.2` module, the installation directory contains, amongst other things:
*   `$EBROOTPYTHON/easybuild/Python-3.10.2.eb`
*   `$EBROOTPYTHON/easybuild/easybuild-Python-3.10.2-*.log`

## Using EasyBuild in your own account
EasyBuild can be used to install software packages in your own account. However, in most cases, it is preferable to ask our [technical support](technical-support.md) to install the software centrally for you. This is because that will ensure that the software package is available on all of our clusters. It will also avoid using your quota, and it will avoid causing undue load on the parallel filesystems.

!!! warning "When to use or not use EasyBuild to install software in your home"
    There are a few use cases in which you may want to use EasyBuild to install software in your own space:
    *   if you need a custom or modified build
    *   if you need to install a nightly build, or a version of a software which does not have a release number
    *   if we are not allowed to install the package centrally for licensing reasons, such as some commercial software packages ([VASP](vasp.md) and [Materials Studio](materials-studio.md) in particular)

    On the contrary, you **should not** install software packages in your own space for the following reasons:
    *   if you need a different release version
    *   if you need a software package built using a different compiler, MPI or CUDA implementation

    When in doubt, please ask our [technical support](technical-support.can) for advice.

### What is a recipe
!!! note
    Writing a recipe from scratch will not be discussed here; you can find more about this in the [EasyBuild documentation](https://docs.easybuild.io/en/latest/Writing_easyconfig_files.html). Modifying a recipe for your particular situation is easier, and it is easier still to find a suitable recipe and use it unmodified.

Recipes, also known as EasyConfig files are text files containing the information EasyBuild needs to build a particular piece of software in a particular environment. They are named following a convention:
*   `<name>-<version>-<toolchain name>-<toolchain version>.eb`
where `<name>` is the name of the package, `<version>` is its version, `<toolchain name>` is the name of the toolchain and `<toolchain version>` is its version. More on toolchains later.

### Finding a recipe
EasyBuild contains a lot of recipes which may or may not compile with the toolchains we have. The surest way to get a recipe that works is to start from one of the recipes which we have installed. These can be found either in the installation folder, as mentioned above, or in the `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO` folder.

!!! info "What is in a toolchain?"
    Toolchains are a combination of compiler, MPI implementation, CUDA version, and mathematical libraries, which are used to compile the software package. They usually hold a rather obscure name such as `gofbc` which, in this case, means it is a combination of GCC, OpenMPI, FlexiBlas and CUDA. However, you do not need to remember this naming, since toolchains themselves have recipes, which are also available in the `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO` directory. For example, the `gofbc` toolchain, version `2020.1.403.114` contains, as per `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO/gofbc/gofbc-2020.1.403.114.eb`:

    ```ini
    local_gccver = '9.3.0'

    # specify subtoolchains as builddependencies
    # this way they will be considered as subtoolchains but
    # are not loaded in the modulefile or software compiled
    # with this toolchain
    builddependencies = [
        ('gccflexiblascuda', '2020.1.114'),
        ('gompic', version),
    ]

    dependencies = [
        ('GCC', local_gccver),  # part of gcccuda
        ('CUDA', '11.4', '', ('GCC', local_gccver)),  # part of gcccuda
        ('OpenMPI', '4.0.3', '', ('gcccuda', '2020.1.114')),
        ('FlexiBLAS', '3.0.4'),
    ]
    ```

    which means that it contains GCC version 9.3.0, OpenMPI 4.0.3, CUDA 11.4, and FlexiBLAS 3.0.4. The `builddependencies` part means that the `gofbc` toolchain is a superset of the `gompic` and the `gccflexiblascuda` toolchains. When a toolchain is a superset of other toolchains, it allows software packages built with the former to have dependencies on software packages built with the latter, i.e. software packages built with `gofbc` can depend on software packages built with `gompic`, but not the other way around.

### Installing a software with EasyBuild
Once you have found a recipe matching your needs, copy its recipe from the `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO` folder, and modify it as needed. Then, run
```bash
eb <recipe.eb>
```
to install it. This will install the software inside of your home directory, in `$HOME/.local/easybuild`. After the installation is completed, exit your session and reconnect to the cluster, and it should be available to load as a module.

#### Reinstalling an existing version
If you are reinstalling the exact same version as one we have installed centrally, but with modified parameters, you need to use
```bash
eb <recipe.eb> --force
```
to install a local version in your home.

#### Installing in a different location
You may want to install the software package in a different location than your home directory, for example in a project directory. To do so, use the following:
```bash
eb <recipe.eb> --installpath /path/to/your/project/easybuild
```
Then, to get these modules available in your sessions, run
```bash
export RSNT_LOCAL_MODULEPATHS=/path/to/your/project/easybuild/modules
```
If you want to have this available by default in your sessions, you can add this command to your `.bashrc` file in your home.

## Additional resources

*   Webinar [*Building software on Compute Canada clusters using EasyBuild*](https://westgrid.github.io/trainingMaterials/getting-started/#building-software-with-easybuild) (recording and slides)
*   [Our staff-facing documentation is available here.](https://github.com/ComputeCanada/software-stack/blob/main/doc/easybuild.md)
*   [Many tutorials on EasyBuild are available](https://easybuild.io/tutorial/)