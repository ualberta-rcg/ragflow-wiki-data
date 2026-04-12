---
title: "CFOUR/fr"
slug: "cfour"
lang: "fr"

source_wiki_title: "CFOUR/fr"
source_hash: "83fec65609afee633cc7a309a4a95396"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:57:28.181742+00:00"

tags:
  - software

keywords:
  - "fichier ZMAT"
  - "clusters couplés"
  - "chimie quantique"
  - "tâche séquentielle"
  - "SBATCH"
  - "CC_CONV"
  - "SCF_CONV"
  - "LINEQ_CONV"
  - "CFOUR"
  - "%excite*"
  - "script bash"
  - "ZETA_CONV"
  - "tâche MPI"
  - "calculs ab-initio"

questions:
  - "Qu'est-ce que le logiciel CFOUR et quelles sont ses principales applications en chimie quantique ?"
  - "Quelles sont les conditions à accepter et la procédure à suivre pour obtenir l'accès à CFOUR sur les grappes de calcul ?"
  - "Quels sont les fichiers d'entrée requis pour exécuter une tâche avec CFOUR et quelles informations contiennent-ils ?"
  - "Quelles sont les différences de configuration Slurm entre la tâche séquentielle et la tâche MPI présentées dans les scripts ?"
  - "Quels modules environnementaux spécifiques doivent être chargés pour exécuter correctement la version MPI de CFOUR ?"
  - "Où peut-on consulter le manuel officiel et les fonctionnalités du programme CFOUR selon les références fournies ?"
  - "What are the specific convergence thresholds defined for the SCF, CC, LINEQ, and ZETA parameters?"
  - "What type of computational process is initiated by the %excite* directive?"
  - "What do the numerical values (1 1 1 7 0 8 0 1.0) represent regarding the excited state configurations or transitions?"
  - "Quelles sont les différences de configuration Slurm entre la tâche séquentielle et la tâche MPI présentées dans les scripts ?"
  - "Quels modules environnementaux spécifiques doivent être chargés pour exécuter correctement la version MPI de CFOUR ?"
  - "Où peut-on consulter le manuel officiel et les fonctionnalités du programme CFOUR selon les références fournies ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# CFOUR

## Introduction

[CFOUR](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.HomePage) (pour *coupled-cluster techniques for computational chemistry*) est un ensemble logiciel qui permet d’effectuer des calculs de chimie quantique de haut niveau sur les atomes et les molécules. Le principal intérêt de CFOUR réside dans la quantité de méthodes *ab-initio* qu’il offre pour le calcul des propriétés atomiques et moléculaires. La plupart des approches basées sur la théorie des perturbations Møller-Plesset (MP) et sur l’approximation de clusters couplés (CC) sont disponibles, et plusieurs de ces approches permettent la dérivation analytique.

CFOUR n’est pas un programme commercial et son développement se fait par l’apport constant d’améliorations et de nouvelles techniques. Consultez [le site web](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.HomePage) pour plus de détails.

## Limites de la licence

L'Alliance a conclu un [accord de licence](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.Download) avec le [professeur Jürgen Gauss](https://www.tc.uni-mainz.de/prof-dr-juergen-gauss/) qui représente les développeurs de CFOUR.

Pour utiliser la version disponible sur nos grappes, vous devez faire parvenir les énoncés suivants au [soutien technique](../support/technical_support.md) :

1.  J’utiliserai CFOUR pour la recherche académique uniquement.
2.  Je ne copierai pas le logiciel CFOUR, ni le rendrai disponible à une autre personne.
3.  Je citerai correctement l'Alliance et les articles de CFOUR dans mes publications (voir la licence pour les détails).
4.  J’accepte que l’entente d’utilisation de CFOUR puisse être en tout temps annulée par les développeurs de CFOUR ou par l'Alliance.
5.  J’informerai l'Alliance de toute dérogation aux énoncés précédents.

À la réception de cette déclaration, nous vous donnerons accès à l’application.

## Module

Pour accéder à la version MPI de CFOUR, [chargez le module](../programming/utiliser_des_modules.md) ainsi :

```bash
module load intel/2023.2.1 openmpi/4.1.5 cfour-mpi/2.1
```

Pour la version séquentielle, le module est chargé ainsi :

```bash
module load intel/2023.2.1 cfour/2.1
```

Les utilisateurs peuvent échanger de l’information dans un forum CFOUR. Consultez les renseignements pour vous inscrire à la [liste d’envoi](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.MailingList).

## Exemples de scripts

Vous devez avoir au moins le fichier [ZMAT](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.InputFileZMAT) contenant toute l'information sur la géométrie, la méthode à employer, les ensembles de données de base, etc. Le deuxième fichier est [GENBAS](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.Basis-setFileGENBAS) ; il contient l'information sur les ensembles de données de base qui sont disponibles. Si GENBAS ne se trouve pas dans le répertoire à partir duquel la tâche est lancée, CFOUR crée un lien symbolique et utilise le fichier existant qui se trouve dans le module. Ce fichier se trouve dans ` $EBROOTCFOUR/basis/GENBAS `.

=== "fichier ZMAT"

    ```txt title="ZMAT"
    Acetylene, CCSD/DZP excited-state geometry optimization
    C                                                                              
    C 1 RCC*
    H 1 RCH* 2 A*
    H 2 RCH* 1 A* 3 D180
                                                                                   
    RCC=1.36
    RCH=1.08
    A=124.
    D180=180.
                                                                                   
    *ACES2(CALC=CCSD,BASIS=DZP,EXCITE=EOMEE                                     
    ESTATE_CONV=10,CONV=10,SCF_CONV=10,CC_CONV=10,LINEQ_CONV=10,ZETA_CONV=10)                                      
                                                                                   
    %excite*                                                                       
    1                                                                              
    1                                                                              
    1 7 0 8 0 1.0                         
    ```

=== "tâche séquentielle"

    ```bash title="run_cfour_serial.sh"
    #!/bin/bash
    #SBATCH --account=def-someacct   # replace this with your own account
    #SBATCH --ntasks=1
    #SBATCH --mem-per-cpu=2500M      # memory; default unit is megabytes.
    #SBATCH --time=0-00:30           # time (DD-HH:MM).

    # Load the module:

    module load intel/2023.2.1 cfour/2.1

    echo "Starting run at: `date`"

    CFOUROUTPUT="cfour-output.txt"
    export CFOUR_NUM_CORES=1

    xcfour > ${CFOUROUTPUT} 

    # Clean the symlink:
    if [[ -L "GENBAS" ]]; then unlink GENBAS; fi

    echo "Program finished with exit code $? at: `date`"
    ```

=== "tâche MPI"

    ```bash title="run-cfour-mpi.sh"
    #!/bin/bash
    #SBATCH --account=def-someacct   # replace this with your own account
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=2500M      # memory; default unit is megabytes.
    #SBATCH --time=0-00:30           # time (DD-HH:MM).

    # Load the module:

    module load intel/2023.2.1  openmpi/4.1.5 cfour-mpi/2.1

    echo "Starting run at: `date`"

    CFOUROUTPUT="cfour-output.txt"
    export CFOUR_NUM_CORES=${SLURM_NTASKS}

    xcfour > ${CFOUROUTPUT} 

    # Clean the symlink:
    if [[ -L "GENBAS" ]]; then unlink GENBAS; fi

    echo "Program finished with exit code $? at: `date`"
    ```

## Références

*   [Manuel](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.Manual)
*   [Fonctionnalités](http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.Features)