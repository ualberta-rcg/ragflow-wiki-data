---
title: "GDAL/en"
slug: "gdal"
lang: "en"

source_wiki_title: "GDAL/en"
source_hash: "5f73c44b76c9726d75ff4f66bea01c11"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:17:39.719727+00:00"

tags:
  - software

keywords:
  - "StdEnv/2023"
  - "R packages"
  - "CRAN mirror"
  - "module load"
  - "terra"
  - "units package"
  - "install_sf_terra"
  - "geospatial data formats"
  - "R library"
  - "bash script"
  - "Python"
  - "GDAL"
  - "osgeo"
  - "sf"
  - "R"

questions:
  - "What is the GDAL library and what are its primary functions for handling geospatial data?"
  - "How do you determine and load the compatible Python modules required to use the osgeo package with different versions of GDAL?"
  - "Which modern R packages rely on GDAL for spatial data analysis, and what additional system modules must be loaded to install them?"
  - "What specific modules must be loaded to successfully install the `sf` and `terra` packages under StdEnv/2023?"
  - "How do you create and configure the local R library directory in the user's home folder prior to installation?"
  - "What R command is executed to download and install the packages from the Canadian CRAN mirror?"
  - "What specific software modules and versions must be loaded before setting up the R environment according to the script?"
  - "How does the script configure the local directory structure and environment variables for the R library?"
  - "Which R package is explicitly mentioned as requiring a specific dependency in the provided text?"
  - "What specific modules must be loaded to successfully install the `sf` and `terra` packages under StdEnv/2023?"
  - "How do you create and configure the local R library directory in the user's home folder prior to installation?"
  - "What R command is executed to download and install the packages from the Canadian CRAN mirror?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[GDAL](https://www.gdal.org/) is an open source translator library for raster geospatial data formats. It can be used as a library, which presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful command line utilities for data translation and processing.

GDAL is used by a [long list of software packages](https://gdal.org/software_using_gdal.html#software-using-gdal) and its functionality can be used in scripts written in [Python](python.md) or [R](r.md).

## Using GDAL from Python
GDAL functionality can be used via the [osgeo](https://gdal.org/api/python/osgeo.html) package, which we install as an extension to the GDAL module. In order to use it, you need to load a compatible Python module alongside the GDAL module.

### Using osgeo under StdEnv/2020
Check which Python modules are compatible with e.g. `gdal/3.5.1`:

```bash
module whatis gdal/3.5.1
# Result:
# gdal/3.5.1          : Description: GDAL is a translator library for raster geospatial data formats...
# gdal/3.5.1          : Homepage: https://www.gdal.org/
# gdal/3.5.1          : URL: https://www.gdal.org/
# gdal/3.5.1          : Compatible modules: python/3.8, python/3.9, python/3.10
```

We have the choice between Python 3.8, 3.9 and 3.10. Let's choose `python/3.10` for this.

```bash
module load StdEnv/2020 gcc/9.3.0 python/3.10 gdal/3.5.1
```

`osgeo_gdal.py`
```python
#!/usr/bin/env python3
from osgeo import gdal

print("osgeo.gdal version:", gdal.__version__)
# osgeo.gdal version: 3.5.1
```

### Using osgeo under StdEnv/2023
Check which Python modules are compatible with e.g. `gdal/3.7.2`:

```bash
module whatis gdal/3.7.2
# Result:
# gdal/3.7.2          : Description: GDAL is a translator library for raster geospatial data formats...
#  data translation and processing.
# gdal/3.7.2          : Homepage: https://www.gdal.org/
# gdal/3.7.2          : URL: https://www.gdal.org/
# gdal/3.7.2          : Compatible modules: python/3.10, python/3.11
# gdal/3.7.2          : Extensions: osgeo-3.7.2
```

We have the choice between Python 3.10 and 3.11. Let's choose `python/3.11` for this.

```bash
module load StdEnv/2023 gcc/12.3 python/3.11 gdal/3.7.2
```

`osgeo_gdal.py`
```python
#!/usr/bin/env python3
from osgeo import gdal

print("osgeo.gdal version:", gdal.__version__)
# osgeo.gdal version: 3.7.2
```

## Using GDAL from R
Several [R-packages for Analysis of Spatial Data](https://cran.r-project.org/web/views/Spatial.html) directly depend on GDAL as a System dependency. For example:
*   [sf](https://CRAN.R-project.org/package=sf): Simple Features for R
*   [terra](https://CRAN.R-project.org/package=terra): Spatial Data Analysis

The older package [rgdal](https://CRAN.R-project.org/package=rgdal) has been discontinued in favour of sf and terra.

### Installing `sf` and `terra` under StdEnv/2020
Installing these packages not only requires loading a `gdal` module, but also `udunits` which is required by [units](https://CRAN.R-project.org/package=units).

`install_sf_terra_StdEnv2020.sh`
```bash
# load required modules:
module load  StdEnv/2020  gcc/9.3.0  udunits/2.2.28  gdal/3.5.1  r/4.2.2

# create a local R library in $HOME:
mkdir -p $HOME/R/x86_64-pc-linux-gnu-library/4.2
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/4.2:$R_LIBS"

# install sf and terra from a Canadian CRAN mirror:
R -e "install.packages(c('sf', 'terra'), repos='https://mirror.csclub.uwaterloo.ca/CRAN/', dep=TRUE)"
```

### Installing `sf` and `terra` under StdEnv/2023
!!! note
    Under StdEnv/2023, in addition to modules `gdal` and `udunits` also `hdf/4.3.1` is required.

`install_sf_terra_StdEnv2020.sh`
```bash
# load required modules:
module load  StdEnv/2023  gcc/12.3  udunits/2.2.28  hdf/4.2.16  gdal/3.7.2  r/4.4.0

# create a local R library in $HOME:
mkdir -p $HOME/R/x86_64-pc-linux-gnu-library/4.4
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/4.4:$R_LIBS"

# install sf and terra from a Canadian CRAN mirror:
R -e "install.packages(c('sf', 'terra'), repos='https://mirror.csclub.uwaterloo.ca/CRAN/', dep=TRUE)"