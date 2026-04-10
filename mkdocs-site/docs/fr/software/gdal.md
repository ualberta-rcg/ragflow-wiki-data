---
title: "GDAL/fr"
slug: "gdal"
lang: "fr"

source_wiki_title: "GDAL/fr"
source_hash: "943e853bda24b77282007947c5fde1a6"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:35:26.992350+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[GDAL](https://www.gdal.org/) est une bibliothèque de traduction *open source* pour les formats de données géospatiales raster. Elle peut être utilisée comme une bibliothèque, car elle présente un modèle de données abstrait unique à l'application qui l’appelle, pour tous les formats pris en charge. Elle est également livrée avec une variété d'utilitaires de ligne de commande pour la traduction et le traitement des données.

GDAL est utilisée par une [longue liste de progiciels](https://gdal.org/software_using_gdal.html#software-using-gdal) et ses fonctionnalités peuvent être utilisées dans des scripts écrits en [Python](python.md) ou [R](r.md).

## Utiliser GDAL avec Python
La fonctionnalité GDAL peut être utilisée via le paquet [osgeo](https://gdal.org/api/python/osgeo.html) que nous installons comme une extension du module GDAL. Pour l'utiliser, vous devez charger un module Python compatible avec le module GDAL.

### Utiliser osgeo avec StdEnv/2020
Pour connaître les modules Python qui sont compatibles avec par exemple `gdal/3.5.1`, utilisez le code suivant :

```bash
module whatis gdal/3.5.1
gdal/3.5.1          : Description: GDAL is a translator library for raster geospatial data formats...
gdal/3.5.1          : Homepage: https://www.gdal.org/
gdal/3.5.1          : URL: https://www.gdal.org/
gdal/3.5.1          : Compatible modules: python/3.8, python/3.9, python/3.10
```

Nous avons donc le choix entre 3.8, 3.9 et 3.10. Nous choisissons `python/3.10`.

```bash
module load StdEnv/2020 gcc/9.3.0 python/3.10 gdal/3.5.1
```

```python title="osgeo_gdal.py"
#!/usr/bin/env python3
from osgeo import gdal

print("osgeo.gdal version:", gdal.__version__)
# osgeo.gdal version: 3.5.1
```

### Utiliser osgeo avec StdEnv/2023
Pour connaître les modules Python qui sont compatibles avec par exemple `gdal/3.7.2`, utilisez le code suivant :

```bash
module whatis gdal/3.7.2
gdal/3.7.2          : Description: GDAL is a translator library for raster geospatial data formats...
 data translation and processing.
gdal/3.7.2          : Homepage: https://www.gdal.org/
gdal/3.7.2          : URL: https://www.gdal.org/
gdal/3.7.2          : Compatible modules: python/3.10, python/3.11
gdal/3.7.2          : Extensions: osgeo-3.7.2
```

Nous avons donc le choix entre 3.10 et 3.11. Nous choisissons `python/3.11`.

```bash
module load StdEnv/2023 gcc/12.3 python/3.11 gdal/3.7.2
```

```python title="osgeo_gdal.py"
#!/usr/bin/env python3
from osgeo import gdal

print("osgeo.gdal version:", gdal.__version__)
# osgeo.gdal version: 3.7.2
```

## Utiliser GDAL avec R
Plusieurs [paquets R pour l’analyse des données spatiales](https://cran.r-project.org/web/views/Spatial.html) dépendent de GDAL pour leurs fonctionnalités, par exemple :
*   [sf](https://CRAN.R-project.org/package=sf) : Simple Features for R
*   [terra](https://CRAN.R-project.org/package=terra) : Analyse de données spatiales

L’ancien paquet [rgdal](https://CRAN.R-project.org/package=rgdal) a été abandonné et remplacé par `sf` et `terra`.

### Installer `sf` et `terra` dans StdEnv/2020
L'installation de ces paquets nécessite non seulement le chargement d'un module `gdal`, mais également de `udunits` requis par le paquet [units](https://CRAN.R-project.org/package=units).

```bash title="install_sf_terra_StdEnv2020.sh"
# charger les modules requis :
module load  StdEnv/2020  gcc/9.3.0  udunits/2.2.28  gdal/3.5.1  r/4.2.2

# créer une bibliothèque R locale dans $HOME :
mkdir -p $HOME/R/x86_64-pc-linux-gnu-library/4.2
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/4.2:$R_LIBS"

# installer sf et terra à partir d'un miroir CRAN canadien :
R -e "install.packages(c('sf', 'terra'), repos='https://mirror.csclub.uwaterloo.ca/CRAN/', dep=TRUE)"
```

### Installer `sf` et `terra` dans StdEnv/2023
Notez qu’avec StdEnv/2023, en plus des modules `gdal` et `udunits`, `hdf/4.3.1` est également requis.

```bash title="install_sf_terra_StdEnv2023.sh"
# charger les modules requis :
module load  StdEnv/2023  gcc/12.3  udunits/2.2.28  hdf/4.2.16  gdal/3.7.2  r/4.4.0

# créer une bibliothèque R locale dans $HOME :
mkdir -p $HOME/R/x86_64-pc-linux-gnu-library/4.4
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/4.4:$R_LIBS"

# installer sf et terra à partir d'un miroir CRAN canadien :
R -e "install.packages(c('sf', 'terra'), repos='https://mirror.csclub.uwaterloo.ca/CRAN/', dep=TRUE)"