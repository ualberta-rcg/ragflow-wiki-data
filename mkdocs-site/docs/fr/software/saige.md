---
title: "SAIGE/fr"
slug: "saige"
lang: "fr"

source_wiki_title: "SAIGE/fr"
source_hash: "1fb4cd5b8d2354b1c8ac808e8b7d125c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:11:26.737990+00:00"

tags:
  - software

keywords:
  - "remotes::install_version"
  - "Makevars"
  - "RSQLite"
  - "SAIGE"
  - "dplyr"
  - "paquet R"
  - "associations pangénomiques"
  - "FlexiBLAS"
  - "modèles mixtes généralisés"
  - "hpcBLASctl"
  - "compilation"
  - "installation"

questions:
  - "Qu'est-ce que le paquet SAIGE et pour quel type d'étude est-il principalement utilisé ?"
  - "Quelles sont les principales caractéristiques et méthodes analytiques offertes par SAIGE pour le traitement des données génétiques ?"
  - "Quelles sont les étapes et les dépendances spécifiques requises pour installer la version 1.0.0 de SAIGE dans l'environnement StdEnv/2020 ?"
  - "Pourquoi faut-il supprimer le fichier configure et modifier le fichier Makevars lors de l'installation ?"
  - "Quelle commande permet de compiler et d'installer le paquet SAIGE ?"
  - "Comment effectuer un test pour vérifier que la bibliothèque SAIGE est correctement installée ?"
  - "Quels sont les paquets R spécifiques et leurs versions qui doivent être installés via la ligne de commande ?"
  - "Quel dépôt et quelle fonction R sont utilisés pour installer ces paquets ?"
  - "Quelle version du logiciel SAIGE est-il demandé de télécharger à la suite de ces installations ?"
  - "Pourquoi faut-il supprimer le fichier configure et modifier le fichier Makevars lors de l'installation ?"
  - "Quelle commande permet de compiler et d'installer le paquet SAIGE ?"
  - "Comment effectuer un test pour vérifier que la bibliothèque SAIGE est correctement installée ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[SAIGE](https://saigegit.github.io/SAIGE-doc/) est un paquet R développé avec Rcpp pour l’étude d'associations pangénomiques avec les grands ensembles de données et les biobanques.

Cette méthode :

*   tient compte de la parenté des échantillons sur la base des modèles mixtes généralisés;
*   permet l'ajustement des modèles selon une matrice de relations génétiques complète ou clairsemée (GRM);
*   fonctionne pour les traits quantitatifs et binaires;
*   gère le déséquilibre des traits binaires dans les cas témoin;
*   produit des calculs efficaces pour les grands ensembles de données;
*   effectue des tests d'association à un seul variant;
*   fournit une estimation de la taille de l'effet grâce à la régression logistique à biais réduit de Firth;
*   effectue l'analyse d'association conditionnelle.

Cette page décrit l'installation du paquet 1.0.0 de SAIGE.

## Installation dans l'environnement StdEnv/2020

1.  Chargez les modules nécessaires.

    ```bash
    module load StdEnv/2020 gcc/9.3.0 r/4.2.2 savvy/2.1.0 superlu/5.2.1 flexiblas/3.0.4
    ```

2.  Créez le répertoire d'installation.

    ```bash
    mkdir -p ~/.local/R/$EBVERSIONR/
    export R_LIBS=~/.local/R/$EBVERSIONR/
    ```

3.  Installez les [dépendances de R](r.md#installation-des-paquets-r).

    !!! attention "Précision sur les versions"
        Il est important d'installer exactement ces versions. Si au cours de l'installation on vous demande d'installer la plus récente version d'une dépendance, appuyez sur Entrée pour refuser.

    ```bash
    R -e 'install.packages("remotes", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("Rcpp", version="1.0.10", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("RcppParallel", version="5.1.6", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("data.table", version="1.17.8", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("RcppArmadillo", version="14.0.2-1", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("SPAtest", version="3.1.2", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("RcppEigen", version="0.3.3.9.3", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("BH", version="1.81.0-1", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("optparse", version="1.7.3", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("SKAT", version="2.2.5", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("MetaSKAT", version="0.82", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("qlcMatrix", version="0.9.5", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("RhpcBLASctl", version="0.23-42", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("RSQLite", version="2.3.8", repos="https://cloud.r-project.org/")'
    R -e 'remotes::install_version("dplyr", version="1.1.0", repos="https://cloud.r-project.org/")'
    ```

4.  Téléchargez la version 1.0.0 de SAIGE.

    ```bash
    git clone --recursive https://github.com/saigegit/SAIGE.git -b 1.0.0
    cd SAIGE/
    ```

5.  Modifiez l'installation.

    ```bash
    rm configure
    sed -i 's/llapack/lflexiblas/' src/Makevars
    ```

    Supprimez d'abord le fichier *configure* pour éviter d'installer des dépendances qui sont déjà disponibles. Ensuite, modifiez le nom de la bibliothèque pour qu'elle utilise le fichier *Makevars* et que les options utilisent FlexiBLAS. Vous évitez ainsi d'obtenir le message d'erreur *unable to find -llapack* à l'installation. Pour plus d'information, lisez [BLAS et LAPACK](../programming/blas_and_lapack.md).

6.  Compilez et installez.

    ```bash
    R CMD INSTALL .
    ```

7.  Effectuez un test.

    ```bash
    R -e 'library(SAIGE)'