---
title: "VASP/fr"
slug: "vasp"
lang: "fr"

source_wiki_title: "VASP/fr"
source_hash: "fb387ba7841e2c862b3dd3e2e880cddf"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:24:56.709360+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "EasyBuild"
  - "fichiers d'entrée"
  - "vasp/6.4.2"
  - "Script de tâche"
  - "modules VASP"
  - "modules"
  - "mémoire"
  - "vasp/5.4.4"
  - "licence"
  - "répertoire /home"
  - "py4vasp"
  - "Slurm"
  - "Implémentation de recettes"
  - "grappes"
  - "Pseudopotentiels"
  - "Vasp-GPU"
  - "Programmes exécutables"
  - "Bibliothèques incluses"
  - "Trillium"
  - "script"
  - "modélisation des matériaux"
  - "charger des modules"
  - "Chimie computationnelle"
  - "ordonnanceur Slurm"
  - "script de tâche"
  - "VASP"
  - "version personnalisée"
  - "exécution en parallèle"
  - "installation de logiciels"

questions:
  - "Qu'est-ce que le logiciel VASP et quelles sont ses principales applications scientifiques ?"
  - "Quelles sont les démarches administratives et les informations requises pour être autorisé à utiliser une licence VASP sur les grappes de calcul ?"
  - "Quelle est la procédure technique à suivre pour charger et utiliser les modules préconstruits de VASP sur les grappes Fir, Nibi et Trillium ?"
  - "Où peut-on consulter des informations supplémentaires concernant l'utilisation des modules ?"
  - "Quelles commandes exactes doivent être exécutées pour charger la version 5.4.4 de VASP sur Trillium ?"
  - "Quels sont les modules spécifiques requis pour utiliser la version 6.4.2 de VASP ?"
  - "Où sont situés les pseudopotentiels VASP sur les serveurs et que faut-il faire pour y avoir accès ?"
  - "Pourquoi est-il fortement recommandé d'effectuer des essais de performance (benchmarking) avant d'utiliser les exécutables Vasp-GPU ?"
  - "Comment doit-on configurer un script de tâche Slurm pour exécuter VASP en parallèle sur la grappe de calcul ?"
  - "Comment configurer un script Slurm pour soumettre une tâche VASP utilisant un GPU ?"
  - "Comment peut-on estimer la quantité de mémoire requise pour une tâche VASP avant son exécution ?"
  - "Quelles sont les conditions et la procédure pour compiler soi-même une version de VASP avec EasyBuild ?"
  - "Quel est le rôle de l'ordonnanceur Slurm dans l'exécution de VASP selon ce document ?"
  - "Quelles sont les ressources matérielles spécifiques (cœurs et mémoire) allouées par ce script ?"
  - "Quels modules logiciels sont nécessaires pour préparer l'environnement d'exécution avant de lancer VASP ?"
  - "Quelles sont les différentes versions de VASP répertoriées et dans quels environnements standard sont-elles implémentées ?"
  - "Comment l'inclusion des bibliothèques et outils externes (tels que HDF5, ELPA, VTSTtools) évolue-t-elle entre les anciennes et les nouvelles versions de VASP ?"
  - "Quelles ressources externes sont mentionnées pour aider les utilisateurs à démarrer avec VASP et à extraire leurs données de calcul ?"
  - "Où peut-on trouver les explications détaillées sur l'utilisation des modules VASP ?"
  - "Dans quel répertoire est-il recommandé d'installer les logiciels pour créer une version personnalisée ?"
  - "Quelles sont les versions spécifiques de VASP pour lesquelles des liens d'installation sont fournis ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

VASP (pour *Vienna ab initio Simulation Package*) est un logiciel servant à modéliser les matériaux à l'échelle atomique avec, par exemple, le calcul des propriétés électroniques et la dynamique moléculaire par mécanique quantique.

## Licence

VASP peut seulement être utilisé par les groupes de recherche ayant obtenu une licence auprès de son développeur, VASP Software GmbH. Votre chercheur principal (PI, professeur) doit s'inscrire sur le [site web de VASP](https://www.vasp.at/) et obtenir une licence.

Quand vous avez votre licence et que vous voulez utiliser les binaires VASP disponibles sur les grappes [Fir](fir.md), [Nibi](../clusters/nibi.md) ou [Trillium](../clusters/trillium.md), écrivez au [soutien technique](../support/technical_support.md) et indiquez :

*   les renseignements sur le détenteur de la licence (votre chercheur principal) :
    *   nom;
    *   courriel;
    *   nom du département et de l'établissement universitaire;
*   les renseignements sur la licence :
    *   la version (4 ou 5);
    *   le **numéro de la licence VASP**;
    *   faites-nous parvenir une mise à jour de la liste des personnes autorisées à utiliser votre licence, par exemple en nous transmettant le dernier courriel reçu de votre gestionnaire de licence à ce sujet.

La licence pour la version 5 vous permet d'utiliser aussi la version 4; par contre, la licence pour la version 4 ne vous permet pas d'utiliser la version 5. De même pour la version 6, vous pouvez utiliser les versions 5 et 4.

Dépendant de votre licence, vous pouvez installer VASP vous-même. Voir [Construire VASP par vous-même](#construire-vasp-par-vous-meme) ci-dessous.

### Pourquoi ?

VASP Software GmbH n'accorde de licences qu'aux groupes employés par une seule et même entité juridique, ce qui est incompatible avec notre mode de fonctionnement. Nous avons tenté de négocier un accord avec le concédant de licence afin de pouvoir installer le logiciel sur toute notre infrastructure, mais sans succès. Veuillez consulter les conditions de votre propre licence, car vous êtes probablement soumis à la même restriction. Cela limite l'assistance que nous pouvons vous offrir pour installer le logiciel.

### Exception pour certains sites

L'Université Simon-Fraser (Fir), l'Université de Waterloo (Nibi) et l'Université de Toronto (Trillium) possèdent des licences VASP, ce qui permet à certains membres du personnel d'avoir accès à des versions spécifiques, de les installer et d'offrir une assistance limitée.

## Utilisation des modules VASP

Pour charger une version préconstruite de VASP sur [Fir](fir.md) et [Nibi](../clusters/nibi.md), les directives sont :

Pour vasp/5.4.4

```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
```

Pour vasp/6.4.2

```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load vasp/6.4.2
```

1.  Pour connaître les versions disponibles, lancez `module spider vasp`.
2.  Sélectionnez votre version et lancez `module spider vasp/<version>` pour connaître les dépendances qui doivent être chargées avec cette version.
3.  Chargez les dépendances et le module VASP, par exemple :

```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load vasp/6.4.2
```

Pour plus d'information, consultez [Utiliser des modules](../programming/utiliser_des_modules.md).

Pour utiliser VASP sur Trillium, chargez les modules comme suit :

Pour vasp/5.4.4

```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load imkl/2023.2.0
module use /opt/software/commercial/modules
module load vasp/5.4.4
```

Pour vasp/6.4.2

```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0 hdf5/1.14.2
module use /opt/software/commercial/modules
module load vasp/6.4.2
```

Pour l'information sur comment utiliser Trillium, voir [Trillium : Guide de démarrage](../clusters/trillium_quickstart.md).

### Pseudopotentiels

Tous les pseudopotentiels ont été téléchargés à partir du site officiel de VASP sans être décompressés. Ils sont situés dans ` $EBROOTVASP/pseudopotentials/` sur Cedar et Graham. Le module VASP doit être chargé pour que vous puissiez avoir accès aux pseudopotentiels.

### Programmes exécutables

**Pour VASP 4.6**, les fichiers exécutables disponibles sont :
*   `vasp` pour les calculs standards de NVT avec des points k non-gamma
*   `vasp-gamma` pour les calculs standards de NVT avec uniquement des points k gamma
*   `makeparam` pour estimer la quantité de mémoire requise pour opérer VASP sur une grappe en particulier

**Pour VASP 5.4.1, 5.4.4 et 6.1.0** (sans CUDA), les fichiers exécutables disponibles sont :
*   `vasp_std` pour les calculs standards de NVT et les points k non-gamma
*   `vasp_gam` pour les calculs standards de NVT avec uniquement des points k gamma
*   `vasp_ncl` pour les calculs de NPT avec des points k non-gamma

**Pour VASP-5.4.4 et 6.1.0 (avec CUDA)**, les fichiers exécutables disponibles sont :
*   `vasp_gpu` pour les calculs standards de NVT et les points K gamma et non-gamma
*   `vasp_gpu_ncl` pour les calculs de NPT avec des points K gamma et non-gamma

Les deux extensions suivantes sont aussi incorporées :
*   [Transition State Tools](http://theory.cm.utexas.edu/vtsttools/)
*   [VASPsol](https://github.com/henniggroup/VASPsol)

Si la version de VASP que vous voulez utiliser n'est pas offerte, vous pouvez soit la construire vous-même (voir ci-dessous) ou demander au [soutien technique](../support/technical_support.md) de la construire et l’installer.

## Vasp-GPU

Les fichiers exécutables Vasp-GPU peuvent être utilisés sur les CPU et les GPU. Comme il est beaucoup plus coûteux de faire des calculs de base sur GPU, nous recommandons fortement d’effectuer des essais (*benchmarking*) avec un ou deux GPU pour vous assurer que leur utilisation est optimale. À titre d'exemple, pour une simulation de Si cristallin avec 256 atomes dans une boîte de simulation, on observe que l'utilisation d'un ou deux GPU, même avec un seul CPU, peut offrir une performance plus de 5 fois supérieure à celle sans GPU. Cependant, la performance ne varie que très peu entre l'utilisation d'un et de deux GPU; en fait, l'utilisation du second GPU pourrait n'être que d'environ 50 % selon nos systèmes de monitorage. Il est donc recommandé d’effectuer ce type de test sur l’ordinateur que vous utiliserez afin d’économiser les ressources de calcul.

## Exemple de script

Le script de tâche suivant exécute VASP en parallèle avec l'ordonnanceur Slurm.

```bash title="Nom du fichier: vasp_job.sh"
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --ntasks=4             # number of MPI processes
#SBATCH --mem-per-cpu=1024M    # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  intelmpi/2019.7.217 vasp/<VERSION>
mpirun <VASP>
```

*   Ce script demande quatre cœurs et 4096 Mo de mémoire (4x1024 Mo).
*   `<ACCOUNT>` est le nom du compte Slurm; pour connaître la valeur à entrer, consultez [Exécuter des tâches](../running-jobs/running_jobs.md), section *Comptes et projets*.
*   `<VERSION>` est le numéro de version de VASP que vous voulez utiliser : 4.6, 5.4.1, 5.4.4 ou 6.1.0.
*   `<VASP>` est le nom de l'exécutable; voyez la section *Programmes exécutables* ci-dessus pour les exécutables que vous pouvez choisir.

```bash title="Nom du fichier: vasp_gpu_job.sh"
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --cpus-per-task=1      # number of CPU processes
#SBATCH --gres=gpu:p100:1      # Number of GPU type:p100 (valid type only for cedar)
#SBATCH --mem=3GB              # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  cuda/11.0  openmpi/4.0.3 vasp/<VERSION>
mpirun <VASP>
```

*   Ce script demande un (1) cœur CPU et 1024 Mo de mémoire.
*   Ce script demande un (1) GPU de type p100, disponible uniquement sur Cedar; voyez les [types disponibles sur les autres superordinateurs](https://docs.computecanada.ca/wiki/Using_GPUs_with_Slurm/fr#N.C5.93uds_disponibles).
*   La tâche utilise `srun` pour faire exécuter VASP.

VASP utilise quatre fichiers d'entrée, soit INCAR, KPOINTS, POSCAR et POTCAR. Il est préférable de préparer les fichiers d'entrée dans un répertoire différent pour chaque tâche. Pour soumettre la tâche à partir du répertoire, utilisez :

```bash
sbatch vasp_job.sh
```

Si vous ignorez combien de mémoire votre tâche nécessite, préparez tous vos fichiers d’entrée et exécutez `makeparam` dans une [tâche interactive](../running-jobs/running_jobs.md). Utilisez ensuite la quantité de mémoire obtenue en résultat pour la prochaine exécution. Pour obtenir une meilleure estimation pour les tâches futures, vérifiez quelle est la taille maximale de la pile de mémoire pour les [tâches complétées](../running-jobs/running_jobs.md) et utilisez cette valeur pour demander la quantité de mémoire par processeur.

Si vous voulez utiliser 32 cœurs ou plus, consultez la [politique d'ordonnancement des tâches](../running-jobs/job_scheduling_policies.md), section *Nœuds entiers ou cœurs*.

## Construire VASP par vous-même

Si vous disposez d'une licence VASP et que vous avez accès à du code source VASP, vous pouvez installer plusieurs versions dans votre répertoire /home sur toutes nos grappes avec les commandes [EasyBuild](../programming/easybuild.md) suivantes.

```bash
eb -f [RECIPE NAME] --sourcepath=[SOURCEPATH]
```

où `[SOURCEPATH]` est le répertoire contenant le code source de VASP et `[RECIPE NAME]` est le nom de la recette. Le premier onglet du tableau ci-dessous affiche la liste des recettes disponibles ainsi que les fichiers sources requis correspondants. Dans ce tableau, VTSTtools et vaspSOL correspondent respectivement aux extensions Transition State Tools et VASPsol. Le deuxième onglet affiche la liste des bibliothèques incluses dans VASP. Vous pouvez télécharger le code source depuis le [site web de VASP](https://www.vasp.at/). L'exécution de la commande peut prendre plus d'une heure. Une fois l'opération terminée, vous pourrez charger et exécuter VASP à l'aide des commandes `module`, comme expliqué précédemment dans [Utilisation des modules VASP](#utilisation-des-modules-vasp).

Pour construire une version personnalisée de VASP, voir [Installation de logiciels dans votre répertoire /home](../getting-started/installing_software_in_your_home_directory.md), [Installing VASP 5](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X) ou [Installing VASP 6](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X).

<div class="tabbed-set" data-tabs="true">
<input checked="checked" id="tabbed-set-0-1" name="tabbed-set-0" type="radio" />
<input id="tabbed-set-0-2" name="tabbed-set-0" type="radio" />
<div class="tabbed-set-labels">
<label for="tabbed-set-0-1">Spécification et implémentation de recettes</label>
<label for="tabbed-set-0-2">Bibliothèques incluses</label>
</div>
<div class="tabbed-set-content">
<div class="tabbed-set-content-item">

| Nom de la recette            | Version | Environnement | Fichier source         | CPU/GPU | VTSTtools | vaspSOL |
| :--------------------------- | :------ | :------------ | :--------------------- | :------ | :-------- | :------ |
| VASP-5.4.4-iimpi-2020a.eb    | 5.4.4   | StdEnv/2023   | vasp.5.4.4.pl2.tgz     | CPU     | oui       | oui     |
| VASP-6.1.2-iimpi-2020a.eb    | 6.1.2   | StdEnv/2020   | vasp.6.1.2_patched.tgz | CPU     | oui       | oui     |
| VASP-6.2.1-iimpi-2020a.eb    | 6.2.1   | StdEnv/2020   | vasp.6.2.1.tgz         | CPU     | oui       | oui     |
| VASP-6.3.0-iimpi-2020a.eb    | 6.3.0   | StdEnv/2020   | vasp.6.3.0.tgz         | CPU     | oui       | oui     |
| VASP-6.3.1-iimpi-2020a.eb    | 6.3.1   | StdEnv/2020   | vasp.6.3.1.tgz         | CPU     | oui       | oui     |
| VASP-6.4.2-iimpi-2023a.eb    | 6.4.2   | StdEnv/2023   | vasp.6.4.2.tar         | CPU     | oui       | oui     |
| VASP-6.4.3-iimpi-2023a.eb    | 6.4.3   | StdEnv/2023   | vasp.6.4.3.tar         | CPU     | oui       | oui     |
| VASP-6.5.0-iimpi-2023a.eb    | 6.5.0   | StdEnv/2023   | vasp.6.5.0.tgz         | CPU     | non       | non     |
| VASP-6.5.1-iimpi-2023a.eb    | 6.5.1   | StdEnv/2023   | vasp.6.5.1.tgz         | CPU     | non       | non     |

</div>
<div class="tabbed-set-content-item">

| Nom de la recette         | Fonction de Wannier | Beef | HDF5 | LibXC | ELPA | Libmbd | dft4 |
| :------------------------ | :------------------ | :--- | :--- | :---- | :--- | :----- | :--- |
| VASP-5.4.4-iimpi-2020a.eb | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.1.2-iimpi-2020a.eb | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.2.1-iimpi-2020a.eb | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.3.0-iimpi-2020a.eb | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.3.1-iimpi-2020a.eb | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.4.2-iimpi-2023a.eb | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.4.3-iimpi-2023a.eb | oui                 | oui  | oui  | oui   | non  | non    | oui  |
| VASP-6.5.0-iimpi-2023a.eb | oui                 | oui  | oui  | oui   | oui  | oui    | oui  |
| VASP-6.5.1-iimpi-2023a.eb | oui                 | oui  | oui  | oui   | oui  | oui    | oui  |

</div>
</div>

## Références

*   [Getting Started](https://www.vasp.at/tutorials/latest/part1/), guide sur le site Web de l'équipe de développement.
*   [py4vasp](https://www.vasp.at/py4vasp/latest/), interface Python pour l'extraction de données suite à des calculs avec VASP.