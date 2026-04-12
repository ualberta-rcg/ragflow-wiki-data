---
title: "R-INLA"
slug: "r-inla"
lang: "base"

source_wiki_title: "R-INLA"
source_hash: "66df1d315c405dd984dbcb9d38dabdd9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:44:35.706250+00:00"

tags:
  - software

keywords:
  - "dependencies"
  - "job script"
  - "R package"
  - "pre-compiled executables"
  - "INLA"
  - "R-INLA package"
  - "Installation"
  - "Standard software environment"
  - "patch"
  - "runsetrpaths.sh"
  - "load required modules"
  - "Bayesian inference"
  - "R-INLA"
  - "LD_LIBRARY_PATH"

questions:
  - "What is the primary function of the R-INLA package?"
  - "Why is the installation process for R-INLA more complicated than that of most standard R packages?"
  - "What are the key steps and module dependencies required to configure the pre-compiled executables for the standard software environment?"
  - "What is required to properly install the R-INLA package and its dependencies?"
  - "Which pre-compiled executables must be installed for R-INLA to operate?"
  - "Why is it necessary to patch the pre-compiled executables for the Standard software environment?"
  - "What is the purpose of modifying the `LD_LIBRARY_PATH` and executing `setrpaths.sh` within the INLA library directory?"
  - "Why must the same required modules be loaded in both the configuration script and the job script?"
  - "Which specific R package and operating system architecture are being targeted by this script snippet?"
  - "What is required to properly install the R-INLA package and its dependencies?"
  - "Which pre-compiled executables must be installed for R-INLA to operate?"
  - "Why is it necessary to patch the pre-compiled executables for the Standard software environment?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[R-INLA](https://www.r-inla.org/) is a package in [R](r.md) that performs approximate Bayesian inference for Latent Gaussian Models.

## Installation

The installation of the R-INLA package is a bit more complicated than most [R](r.md) packages, as it downloads other pre-compiled executables that need to be made compatible with our [Standard software environment](../programming/standard_software_environments.md).

The scripts below have been tested with the versions mentioned therein. Because R will always install the latest versions of packages, the versions of the modules will likely have to be adjusted in the future.

=== "StdEnv/2023 r/4.4"

```bash linenums="1" title="install_INLA_StdEnv2023.sh"
#!/bin/bash

# (1)
module load StdEnv/2023 gcc/12.3 r/4.4.0 geos/3.12.0 gdal/3.9.1 udunits/2.2.28 gsl/2.7 jags/4.3.2

LOGFILE=r_INLA_install_${EBVERSIONR}_${CC_CLUSTER}_$(date --iso=min).log

# (2)
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/${EBVERSIONR:0:3}"
echo  "R_LIBS is $R_LIBS"
mkdir -p $R_LIBS
R -e 'install.packages("remotes", repos=c("https://mirror.csclub.uwaterloo.ca/CRAN/"))'
R -e 'install.packages("INLA", version="25.06.07", repos=c("https://mirror.csclub.uwaterloo.ca/CRAN/", INLA="https://inla.r-inla-download.org/R/stable"), dep=TRUE, Ncpus=2)' \
    |& tee  $LOGFILE

# (3)
R -e 'library(INLA); inla.binary.install(os="Rocky Linux-8")' |& tee -a $LOGFILE

# (4)
chmod u+x $R_LIBS/INLA/bin/linux/64bit/{*.so.*,*.so,first/*.so}
sed -i  's/\(^.*export LD_LIBRARY_PATH\)/echo "Skipping LD_LIBRARY_PATH." #\1/g' $R_LIBS/INLA/bin/linux/64bit/*.run
setrpaths.sh --path $R_LIBS/INLA/bin/linux/64bit/malloc --add_path "\$ORIGIN:$EBROOTGENTOO/lib/gcc/x86_64-pc-linux-gnu/${EBVERSIONGCC::2}"
setrpaths.sh --path $R_LIBS/INLA/bin/linux/64bit --add_path '$ORIGIN/first:$ORIGIN:$ORIGIN/malloc'
```

=== "StdEnv/2020 r/4.2.1"

```bash linenums="1" title="install_INLA_StdEnv2020.sh"
#!/bin/bash

# (1)
module load StdEnv/2020 gcc/9.3.0 r/4.2.1 geos/3.9.1 gdal/3.2.3 udunits/2.2.26 gsl/2.6

LOGFILE=r_INLA_install_${EBVERSIONR}_${CC_CLUSTER}_$(date --iso=sec).log

# (2)
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/${EBVERSIONR:0:3}"
echo  "R_LIBS is $R_LIBS"
mkdir -p $R_LIBS
R -e 'install.packages("INLA", repos=c("https://cran.utstat.utoronto.ca/", INLA="https://inla.r-inla-download.org/R/stable"), dep=TRUE, Ncpus=2)' \
     |& tee  $LOGFILE

# (3)
R -e 'library(INLA); inla.binary.install(os="CentOS Linux-7")' |& tee -a $LOGFILE

# (4)
chmod u+x $R_LIBS/INLA/bin/linux/64bit/{*.so.*,*.so,first/*.so}
sed -i  's/\(^.*export LD_LIBRARY_PATH\)/echo "Skipping LD_LIBRARY_PATH." #\1/g' $R_LIBS/INLA/bin/linux/64bit/*.run
setrpaths.sh --path $R_LIBS/INLA/bin/linux --add_path '$ORIGIN/first:$ORIGIN'
```

Comments in the script:

*   (1) Load required modules. The same modules have to be loaded in the job script as well.
*   (2) Install the R-INLA package and its dependencies.
*   (3) Install the pre-compiled executables that R-INLA needs.
*   (4) Patch the pre-compiled executables so that they are compatible with our [Standard software environment](../programming/standard_software_environments.md).