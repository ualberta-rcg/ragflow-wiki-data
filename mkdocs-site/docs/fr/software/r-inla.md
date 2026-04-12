---
title: "R-INLA/fr"
slug: "r-inla"
lang: "fr"

source_wiki_title: "R-INLA/fr"
source_hash: "86e7056ea0d93a8ef88744a894515da8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:45:13.278756+00:00"

tags:
  - software

keywords:
  - "exécutables précompilés"
  - "installation"
  - "INLA"
  - "paquet R"
  - "paquet R-INLA"
  - "charger les modules"
  - "installer"
  - "environnements logiciels standards"
  - "setrpaths.sh"
  - "script pour la tâche"
  - "dépendances"
  - "R-INLA"
  - "LD_LIBRARY_PATH"
  - "inférence bayésienne"

questions:
  - "Qu'est-ce que le paquet R-INLA et quelle méthodologie statistique utilise-t-il ?"
  - "Pourquoi l'installation de R-INLA est-elle plus complexe que celle des autres paquets R ?"
  - "Quelles sont les étapes de configuration et les modules requis pour installer R-INLA dans un environnement logiciel standard ?"
  - "Comment installer le paquet R-INLA ainsi que ses dépendances ?"
  - "Quels exécutables précompilés sont requis par R-INLA lors de l'installation ?"
  - "Pourquoi faut-il corriger les exécutables précompilés pour les environnements logiciels standards ?"
  - "Quel est l'objectif de la modification des chemins de bibliothèques (LD_LIBRARY_PATH) pour le package R INLA dans ce script ?"
  - "Pourquoi est-il indispensable de charger les mêmes modules dans le script de la tâche que ceux indiqués dans les commentaires ?"
  - "Comment ce script gère-t-il les dépendances et les chemins d'exécution (rpaths) dans l'environnement Linux 64 bits ?"
  - "Comment installer le paquet R-INLA ainsi que ses dépendances ?"
  - "Quels exécutables précompilés sont requis par R-INLA lors de l'installation ?"
  - "Pourquoi faut-il corriger les exécutables précompilés pour les environnements logiciels standards ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[R-INLA](https://www.r-inla.org/) est un paquet en langage [R](r.md) qui utilise une méthodologie d'approximation de l’inférence bayésienne.

## Installation

L'installation est un peu plus compliquée que celle pour les autres paquets [R](r.md) parce que d'autres exécutables précompilés doivent être téléchargés pour assurer la compatibilité avec nos [environnements logiciels standards](standard-software-environments.md).

Les scripts ci-dessous ont été testés avec les versions qu'ils utilisent. Puisque R installe toujours la dernière version des paquets, les versions des modules devront être ajustées au besoin.

```bash tab="install_INLA_StdEnv2023.sh"
#!/bin/bash

# (1)
module load StdEnv/2023 gcc/12.3 r/4.4.0 geos/3.12.0 gdal/3.9.1 udunits/2.2.28 gsl/2.7 jags/4.3.2

LOGFILE=r_INLA_install_${EBVERSIONR}_${CC_CLUSTER}_$(date --iso=min).log

# (2)
export R_LIBS="$HOME/R/x86_64-pc-linux-gnu-library/${EBVERSIONR:0:3}"
echo  "R_LIBS is $R_LIBS"
mkdir -p $R_LIBS
R -e 'install.packages("remotes", repos=c("https://mirror.csclub.uwaterloo.ca/CRAN/"))'
R -e 'install.packages("INLA", version="25.06.07", repos=c("https://mirror.csclub.uwater Waterloo.ca/CRAN/", INLA="https://inla.r-inla-download.org/R/stable"), dep=TRUE, Ncpus=2)' \
    |& tee  $LOGFILE

# (3)
R -e 'library(INLA); inla.binary.install(os="Rocky Linux-8")' |& tee -a $LOGFILE

# (4)
chmod u+x $R_LIBS/INLA/bin/linux/64bit/{*.so.*,*.so,first/*.so}
sed -i  's/\(^.*export LD_LIBRARY_PATH\)/echo "Skipping LD_LIBRARY_PATH." #\1/g' $R_LIBS/INLA/bin/linux/64bit/*.run
setrpaths.sh --path $R_LIBS/INLA/bin/linux/64bit/malloc --add_path "\$ORIGIN:$EBROOTGENTOO/lib/gcc/x86_64-pc-linux-gnu/${EBVERSIONGCC::2}"
setrpaths.sh --path $R_LIBS/INLA/bin/linux/64bit --add_path '$ORIGIN/first:$ORIGIN:$ORIGIN/malloc'
```

```bash tab="install_INLA_StdEnv2020.sh"
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

Commentaires sur le script

*   (1) Pour charger les modules requis. Il faut aussi charger les mêmes modules dans le script pour la tâche.
*   (2) Pour installer le paquet R-INLA et ses dépendances.
*   (3) Pour installer les exécutables précompilés requis par R-INLA.
*   (4) Pour corriger les exécutables précompilés pour qu'ils soient compatibles avec nos [environnements logiciels standards](standard-software-environments.md).