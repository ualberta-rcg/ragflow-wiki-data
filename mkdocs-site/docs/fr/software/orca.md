---
title: "ORCA/fr"
slug: "orca"
lang: "fr"

source_wiki_title: "ORCA/fr"
source_hash: "d6e0417a85771b5dcc375e9210df4df3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:19:56.809976+00:00"

tags:
  - software
  - computationalchemistry

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

## Introduction
ORCA est un logiciel d'utilisation générale en chimie quantique qui offre souplesse, efficacité et facilité d'utilisation; l'outil est particulièrement utile pour la modélisation des propriétés spectroscopiques de molécules à couches de valence non remplie. ORCA permet d'employer un grand nombre de méthodes dont la théorie de la fonctionnelle de la densité (DFT) et autres méthodes *ab initio* de corrélation simple ou multiple. L'outil traite également les effets environnementaux et relativistes.

## Droit d'utilisation
Pour utiliser les modules exécutables ORCA préconstruits:
1.  Remplissez le formulaire d'inscription que vous trouverez sur https://orcaforum.kofo.mpg.de/.
2.  Vous recevrez par courriel un premier message pour confirmer votre adresse de courriel et activer le compte; suivez les directives de ce courriel.
3.  Quand votre inscription sera faite, vous recevrez **un deuxième courriel** avec la mention *registration for ORCA download and usage has been completed*.
4.  Faites parvenir une copie du **deuxième courriel** au [soutien technique](technical-support.md).

## Versions

### ORCA 6

Le module **orca/6.0.1** est disponible dans l'environnement **StdEnv/2023**; pour le charger, lancez

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 orca/6.0.1
```

Il y a aussi le module **orca/6.0.0**. Cependant, la plus récente version **orca/6.0.1** a corrigé des bogues de la version **6.0.0**.

!!! note "Remarque"
    Cette version de ORCA inclut xtb 6.7.1.

### ORCA 5

Les versions 5.0.1 à 5.0.3 comportaient des bogues qui ont été éliminés dans la version 5.0.4, notamment [un problème qui touchait les gradients de dispersion D4](https://orcaforum.kofo.mpg.de/viewtopic.php?f=56&t=9985). Nous vous recommandons donc d'utiliser la version 5.0.4 plutôt que des versions 5.0.x moins récentes. Les versions 5.0.1, 5.0.2 et 5.0.3 se trouvent dans notre pile logicielle, mais pourraient éventuellement être enlevées.

Chargez la version 5.0.4 avec

```bash
module load StdEnv/2020 gcc/10.3.0 openmpi/4.1.1 orca/5.0.4
```

### ORCA 4

Chargez la version 4.2.1 avec

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 orca/4.2.1
```

ou

```bash
module load nixpkgs/16.09 gcc/7.3.0 openmpi/3.1.4 orca/4.2.1
```

## Configuration des fichiers en entrée

En plus des mots clés qui sont nécessaires à l'exécution d'une simulation, assurez-vous de configurer les paramètres suivants:

*   quantité de CPU
*   maxcore

## Utilisation
Pour connaître les versions disponibles, lancez **module spider orca**.
Pour les détails en rapport avec un module spécifique (incluant les directives pour l'ordre dans lequel charger les modules requis), utilisez le nom complet du module, par exemple `module spider orca/4.0.1.2`.

Pour les directives générales, consultez [Utiliser des modules](utiliser-des-modules.md).

### Soumettre des tâches
Pour les directives générales, consultez [Exécuter des tâches](running-jobs.md).

!!! note "NOTE"
    Si certains exécutables ORCA présentent des problèmes avec MPI, vous pouvez essayer de définir les variables suivantes:

    ```bash
    export OMPI_MCA_mtl='^mxm'
    export OMPI_MCA_pml='^yalla'
    ```

Le script suivant utilise [MPI](mpi.md). Veuillez noter que, contrairement à la plupart des programmes MPI, ORCA n'est pas démarré avec une commande parallèle telle que `mpirun` ou `srun`, mais nécessite le chemin complet vers le programme, qui est indiqué par `$EBROOTORCA`.

```bash title="run_orca.sh"
#!/bin/bash
#SBATCH --account=def-youPIs
#SBATCH --ntasks=8                 # cpus, the nprocs defined in the input file
#SBATCH --mem-per-cpu=3G           # memory per cpu
#SBATCH --time=00-03:00            # time (DD-HH:MM)
#SBATCH --output=benzene.log       # output .log file

module load StdEnv/2020  gcc/9.3.0  openmpi/4.0.3
module load orca/4.2.1
$EBROOTORCA/orca benzene.inp
```
Voici un exemple du fichier d’entrée benzene.inp:
```text title="benzene.inp"
# Benzene RHF Opt Calculation
%pal nprocs 8 end
! RHF TightSCF PModel
! opt

* xyz 0 1
     C    0.000000000000     1.398696930758     0.000000000000
     C    0.000000000000    -1.398696930758     0.000000000000
     C    1.211265339156     0.699329968382     0.000000000000
     C    1.211265339156    -0.699329968382     0.000000000000
     C   -1.211265339156     0.699329968382     0.000000000000
     C   -1.211265339156    -0.699329968382     0.000000000000
     H    0.000000000000     2.491406946734     0.000000000000
     H    0.000000000000    -2.491406946734     0.000000000000
     H    2.157597486829     1.245660462400     0.000000000000
     H    2.157597486829    -1.245660462400     0.000000000000
     H   -2.157597486829     1.245660462400     0.000000000000
     H   -2.157597486829    -1.245660462400     0.000000000000
*
```

### Notes
*   Pour que le programme fonctionne efficacement et utilise toutes les ressources ou les cœurs requis par votre tâche, ajoutez la ligne `%pal nprocs <ncores> end` au fichier en sortie, comme dans l'exemple ci-dessus. Remplacez `<ncores>` par le nombre de cœurs que vous avez spécifié dans votre script.

*   Si vous voulez redémarrer un calcul, supprimez le fichier `*.hostnames` (par exemple `benzene.hostnames` dans l'exemple ci-dessus) avant de soumettre la tâche suivante; autrement, la tâche échouera probablement, ce qui produira le message d'erreur `All nodes which are allocated for this job are already filled.`

### (2019-09-06) Correctif temporaire au sujet de l'incohérence des versions OpenMPI
Lors de certains types de calculs (en particulier DLPNO-STEOM-CCSD), il est possible que des erreurs critiques surviennent. Ceci pourrait se produire si vous utilisez une version moins récente de `OpenMPI` (par exemple `3.1.2` comme suggéré par 'module' pour `orca/4.1.0` et `4.2.0`) que celle officiellement recommandée (soit `3.1.3` pour `orca/4.1.0` et `3.1.4` pour `orca/4.2.0`). Pour résoudre ce problème, vous pouvez personnaliser la version de `OpenMPI`.

Les deux commandes suivantes personnalisent `openmpi/3.1.4` pour `orca/4.2.0`:
```bash
module load gcc/7.3.0
eb OpenMPI-3.1.2-GCC-7.3.0.eb --try-software-version=3.1.4
```
Une fois ceci terminé, chargez `openmpi` avec
```bash
module load openmpi/3.1.4
```
Vous pouvez maintenant installer manuellement les binaires `orca/4.2.0` à partir du forum officiel dans le répertoire `/home`, après avoir effectué l'enregistrement dans le forum ORCA officiel et avoir obtenu l'accès à l'application ORCA sur nos grappes.

!!! note "Autres notes de l'auteur"
    Ce correctif peut être appliqué dans l'attente de la mise à jour officielle de `OpenMPI` sur nos grappes. Une fois que cette mise à jour aura été faite, n'oubliez pas de supprimer les binaires installés manuellement.

    La commande de compilation ne semble pas s'appliquer à `openmpi/2.1.x`.

## Utilisation de NBO

Vous devez avoir accès à NBO pour pouvoir l'utiliser avec ORCA. NBO n'est pas un module distinct sur nos grappes, mais il est possible d'y avoir accès via les modules Gaussian qui sont installés sur [Cedar](cedar.md) et [Graham](graham.md). Pour pouvoir utiliser NBO avec ORCA, vous devez donc avoir accès à ORCA et [aussi à Gaussian](gaussian.md#licence).

### Exemple de script

Le nom du fichier d'entrée (dans le prochain exemple *orca_input.inp*) doit contenir le mot-clé **NBO**.

```bash title="run_orca-nbo.sh"
#!/bin/bash
#SBATCH --account=def-youPIs
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-3:00:00

# Load the modules:

module load StdEnv/2020  gcc/10.3.0  openmpi/4.1.1 orca/5.0.4
module load gaussian/g16.c01

export GENEXE=`which gennbo.i4.exe`
export NBOEXE=`which nbo7.i4.exe`

${EBROOTORCA}/orca orca_input.inp > orca_output.out
```

## Références

*   [ORCA tutorials](https://www.orcasoftware.de/tutorials_orca/)
*   [ORCA Forum](https://orcaforum.kofo.mpg.de/app.php/portal)