---
title: "SAIGE"
slug: "saige"
lang: "base"

source_wiki_title: "SAIGE"
source_hash: "cdd8be6a76ed920d0769a2e6fbbb1423"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:10:53.981831+00:00"

tags:
  - software

keywords:
  - "genome-wide association tests"
  - "R package"
  - "Makevars"
  - "SAIGE"
  - "dplyr"
  - "installation patch"
  - "FlexiBLAS"
  - "LAPACK"
  - "git clone"
  - "generalized mixed models"
  - "installation"
  - "R"

questions:
  - "What is the primary purpose of the SAIGE R package and what key features does it offer for genome-wide association tests?"
  - "Which specific system modules and environment variables must be loaded and configured before installing SAIGE under the StdEnv/2020 environment?"
  - "What are the necessary steps for downloading the source code, installing the exact R dependencies, and patching the SAIGE version 1.0.0 installation?"
  - "Why should the configure file be removed before proceeding with the installation?"
  - "How does modifying the library name to link to the Makevars file resolve the \"-llapack\" error?"
  - "What commands are required to compile, install, and test the availability of the package?"
  - "How is the specific version 1.1.0 of the dplyr package installed via the R command line?"
  - "What command is required to clone version 1.0.0 of the SAIGE repository?"
  - "Which files are modified or removed during the patching step of the SAIGE installation?"
  - "Why should the configure file be removed before proceeding with the installation?"
  - "How does modifying the library name to link to the Makevars file resolve the \"-llapack\" error?"
  - "What commands are required to compile, install, and test the availability of the package?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[SAIGE](https://saigegit.github.io/SAIGE-doc/) is an R package developed with Rcpp for genome-wide association tests in large-scale data sets and biobanks.

The method

*   accounts for sample relatedness based on the generalized mixed models;
*   allows for model fitting with either full or sparse genetic relationship matrix (GRM);
*   works for quantitative and binary traits;
*   handles case-control imbalance of binary traits;
*   computationally efficient for large data sets;
*   performs single-variant association tests;
*   provides effect size estimation through Firth’s Bias-Reduced Logistic Regression;
*   performs conditional association analysis.

This page discusses how to install SAIGE package 1.0.0.

## Installing SAIGE under the environment StdEnv/2020

1.  Load the appropriate modules.

    ```bash
    module load StdEnv/2020 gcc/9.3.0 r/4.2.2 savvy/2.1.0 superlu/5.2.1 flexiblas/3.0.4
    ```

2.  Create the installation directory.

    ```bash
    mkdir -p ~/.local/R/$EBVERSIONR/
    export R_LIBS=~/.local/R/$EBVERSIONR/
    ```

3.  Install the [R dependencies](r.md#installing-r-packages).

    !!! note "Exact Dependency Versions"
        It is important to install these exact versions. During installation, if you are prompted to install the latest version of any dependency, simply press Enter to decline.

    ```bash
    [name@server ~]$ R -e 'install.packages("remotes", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("Rcpp", version="1.0.10", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("RcppParallel", version="5.1.6", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("data.table", version="1.17.8", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("RcppArmadillo", version="14.0.2-1", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("SPAtest", version="3.1.2", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("RcppEigen", version="0.3.3.9.3", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("BH", version="1.81.0-1", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("optparse", version="1.7.3", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("SKAT", version="2.2.5", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("MetaSKAT", version="0.82", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("qlcMatrix", version="0.9.5", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("RhpcBLASctl", version="0.23-42", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("RSQLite", version="2.3.8", repos="https://cloud.r-project.org/")'
    [name@server ~]$ R -e 'remotes::install_version("dplyr", version="1.1.0", repos="https://cloud.r-project.org/")'
    ```

4.  Download SAIGE version 1.0.0.

    ```bash
    git clone --recursive https://github.com/saigegit/SAIGE.git -b 1.0.0
    cd SAIGE/
    ```

5.  Patch the installation.

    ```bash
    rm configure
    sed -i 's/llapack/lflexiblas/' src/Makevars
    ```

    First, remove the *configure* file to avoid installing already available dependencies. Then, change the library name to correctly link to the *Makevars* file to make sure that the linking options will use FlexiBLAS. Doing so will prevent the *unable to find -llapack* error message displayed at installation. Read more information on [FlexiBLAS, BLAS and LAPACK](blas-and-lapack.md).

6.  Compile and install.

    ```bash
    R CMD INSTALL .
    ```

7.  Test that it is available.

    ```bash
    R -e 'library(SAIGE)'