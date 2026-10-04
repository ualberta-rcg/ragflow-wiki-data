---
title: "VASP/fr"
slug: "vasp"
lang: "fr"

source_wiki_title: "VASP/fr"
source_hash: "e90ee4b22b8be6d6a3544d1f2e3564b0"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:18:32.659928+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "script Slurm"
  - "Utiliser des modules"
  - "sbatch"
  - "ordonnanceur Slurm"
  - "exécutables VASP"
  - "py4vasp"
  - "calculs VASP"
  - "GPU"
  - "interface Python"
  - "GPU p100"
  - "Installation VASP"
  - "tutorial"
  - "système de monitorage"
  - "version 6"
  - "performance"
  - "Getting Started"
  - "vasp_job.sh"
  - "vasp/5.4.4"
  - "recettes VASP"
  - "pseudopotentiels"
  - "télécharger le code source"
  - "chimie computationnelle"
  - "Références"
  - "version 5"
  - "EasyBuild"
  - "site Web de l'équipe de développement"
  - "vasp/6.4.2"
  - "benchmark GPU"
  - "CPU"
  - "exécution de la commande"
  - "StdEnv"
  - "extraction de données"
  - "VASP-6.5.1-iimpi-2023a.eb"
  - "VASP"
  - "module load vasp/6.4.2-gpu"
  - "VASPsol"
  - "modules VASP"
  - "bibliothèques incluses"
  - "StdEnv/2023"
  - "licence VASP"
  - "module load"

questions:
  - "Quelles sont les étapes à suivre pour obtenir et activer une licence VASP au sein d’un groupe de recherche ?"
  - "Comment charger les modules VASP appropriés sur les clusters Fir, Nibi et Trillium afin d’utiliser les versions préconstruites du logiciel ?"
  - "Pourquoi seules l’Université Simon‑Fraser (Fir), l’Université de Waterloo (Nibi) et l’Université de Toronto (Trillium) bénéficient d’une exception d’accès aux licences VASP ?"
  - "Comment charger les modules requis pour exécuter VASP 5.4.4 sur le système Trillium ?"
  - "Quelles sont les commandes de chargement de modules spécifiques à VASP 6.4.2, et comment diffèrent‑elles de celles de VASP 5.4.4 ?"
  - "Où peut‑on consulter la documentation détaillée sur l’utilisation des modules (ex. « Utiliser des modules ») ?"
  - "Quels modules faut‑il charger pour utiliser VASP 6.4.2 (ou la version GPU) sur la sous‑grappe GPU de Trillium ?"
  - "Où sont situés les pseudopotentiels fournis avec VASP et comment y accéder après le chargement du module ?"
  - "Quels exécutables VASP sont disponibles selon la version (4.6, 5.4.1/5.4.4/6.1.0) et le type de calcul (NVT, NPT, points γ, GPU) ?"
  - "Pourquoi la différence de performance entre 1 et 2 GPU est‑elle négligeable dans le système de monitorage décrit ?"
  - "Quelle recommandation est donnée concernant la réalisation de tests sur l’ordinateur destiné à l’usage afin d’économiser les ressources de calcul ?"
  - "Quel ordonnanceur est utilisé dans l’exemple de script pour exécuter VASP en parallèle ?"
  - "Quels sont les paramètres de ressources (nombre de cœurs, mémoire et GPU) demandés dans les scripts vasp_job.sh et vasp_gpu_job.sh ?"
  - "Que signifient les espaces réservés <ACCOUNT>, <VERSION> et <VASP> dans les scripts, et comment les remplacer correctement avant de soumettre une tâche ?"
  - "Comment peut‑on compiler et installer une version personnalisée de VASP sur les grappes en suivant la section «Construire VASP par vous‑même» ?"
  - "Quels environnements et versions de VASP sont répertoriés dans le tableau « Spécification et implémentation de recettes » ?"
  - "Quelles bibliothèques (Wannier, Beef, HDF5, LibXC, ELPA, Libmbd, dft4) sont incluses ou exclues pour chaque recette listée dans le tableau « Bibliothèques incluses » ?"
  - "Où trouver les guides d’installation détaillés pour compiler une version personnalisée de VASP mentionnés dans le texte ?"
  - "Où peut‑on télécharger le code source de VASP mentionné dans le texte ?"
  - "Que montre le deuxième onglet de VASPsol selon la description ?"
  - "Quelle procédure faut‑il suivre pour charger et exécuter VASP après l’installation, et combien de temps l’opération peut‑elle prendre ?"
  - "Quels modules ou fonctionnalités sont activés (indiqués par “oui”) dans la configuration de VASP‑6.5.1‑iimpi‑2023a.eb ?"
  - "Où accéder au guide “Getting Started” référencé sur le site web de l’équipe de développement de VASP ?"
  - "Comment installer et lancer correctement la version VASP‑6.5.1‑iimpi‑2023a.eb décrite dans le texte ?"
  - "Qu’est‑ce que py4vasp et à quel type de calculs est‑il destiné ?"
  - "Comment py4vasp facilite‑t‑il l’extraction de données issues de VASP ?"
  - "Dans quelles catégories (logiciel, chimie computationnelle) ce projet est‑il classé ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

VASP, abréviation de *Vienna ab initio Simulation Package*, est un logiciel servant à modéliser les matériaux à l'échelle atomique avec, par exemple, le calcul des propriétés électroniques et la dynamique moléculaire par mécanique quantique.

## Licence

VASP peut seulement être utilisé par les groupes de recherche ayant obtenu une licence auprès de son développeur, VASP Software GmbH. Votre chercheur principal (PI, professeur) doit s'inscrire sur le [site web de VASP](https://www.vasp.at/) et obtenir une licence.

Quand vous avez votre licence et que vous voulez utiliser les binaires VASP disponibles sur les grappes [Fir](fir.md), [Nibi](../clusters/nibi.md) ou [Trillium](../clusters/trillium.md), écrivez au [soutien technique](../support/technical_support.md) et indiquez :
*   les renseignements sur le détenteur de la licence (votre chercheur principal) :
    *   nom;
    *   courriel;
    *   nom du département et de l'établissement universitaire;
*   les renseignements sur la licence :
    *   la version (5 ou 6);
    *   le **numéro de la licence VASP**;
    *   faites-nous parvenir une mise à jour de la liste des personnes autorisées à utiliser votre licence, par exemple en nous transmettant le dernier courriel reçu de votre gestionnaire de licence à ce sujet.

La licence pour la version 6 vous permet d'utiliser aussi la version 5; par contre, la licence pour la version 5 ne vous permet pas d'utiliser la version 6.

Dépendant de votre licence, vous pouvez installer VASP vous-même. Voir [Construire VASP par vous-même](#construire-vasp-par-vous-même) ci-dessous.

### Pourquoi ?

VASP Software GmbH n'accorde de licences qu'aux groupes employés par une seule et même entité juridique, ce qui est incompatible avec notre mode de fonctionnement. Nous avons tenté de négocier un accord avec le concédant de licence afin de pouvoir installer le logiciel sur toute notre infrastructure, mais sans succès. Veuillez consulter les conditions de votre propre licence, car vous êtes probablement soumis à la même restriction. Cela limite l'assistance que nous pouvons vous offrir pour installer le logiciel.

### Exception pour certains sites

L'Université Simon-Fraser (Fir), l'Université de Waterloo (Nibi) et l'Université de Toronto (Trillium) possèdent des licences VASP, ce qui permet à certains membres du personnel d'avoir accès à des versions spécifiques, de les installer et d'offrir une assistance limitée.

## Utilisation des modules VASP

Pour charger une version préconstruite de VASP sur [Fir](fir.md) et [Nibi](../clusters/nibi.md), les directives sont :

**Pour `vasp/5.4.4`**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
```

**Pour `vasp/6.4.2`**
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

**Pour `vasp/5.4.4`**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load imkl/2023.2.0
module use /opt/software/commercial/modules
module load vasp/5.4.4
```

**Pour `vasp/6.4.2`**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0 hdf5/1.14.2
module use /opt/software/commercial/modules
module load vasp/6.4.2
```
Pour l'information sur comment utiliser Trillium, voir [Trillium : Guide de démarrage](../clusters/trillium_quickstart.md).

**Pour `vasp/6.6.1`**
```bash
module load StdEnv/2023 intel/2025.2.0 intelmpi/2021.16.0 hdf5/1.14.6
module use /opt/software/commercial/modules
module load vasp/6.6.1
```

**Pour `vasp/6.4.2-gpu`** sur la sous-grappe GPU de Trillium,
```bash
module load StdEnv/2023 nvhpc/25.1 cuda/12.6 nccl/2.26.2 imkl/2023.2.0 hdf5/1.14.5
module use /opt/software/commercial/modules
module load vasp/6.4.2-gpu
```
Pour l'information générale sur Trillium, voir [Trillium : Guide de démarrage](../clusters/trillium_quickstart.md).

### Pseudopotentiels

Tous les pseudopotentiels ont été téléchargés à partir du site officiel de VASP sans être décompressés. Ils sont situés dans `$EBROOTVASP/pseudopotentials/` sur Fir et Nibi. Le module VASP doit être chargé pour que vous puissiez avoir accès aux pseudopotentiels.

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

Les fichiers exécutables Vasp-GPU peuvent être utilisés sur les CPU et les GPU. Comme il est beaucoup plus coûteux de faire des calculs de base sur GPU, nous recommandons fortement d’effectuer des essais (*benchmarking*) avec un ou deux GPU pour vous assurer que leur utilisation est optimale.

Considérons l'exemple de Si cristallin qui contient 256 atomes dans une boîte de simulation. La durée de la simulation varie en fonction du nombre de CPU et de GPU utilisés. Il a été observé qu'avec 1 CPU, la performance avec 1 ou 2 GPU est plus de 5 fois meilleure que sans GPU. Cependant, l'amélioration de performance entre 1 et 2 GPU est marginale. Il est donc recommandé d’effectuer des tests de performance (*benchmarking*) sur l'ordinateur que vous utiliserez afin d’optimiser l'utilisation des ressources de calcul.

## Exemple de script

Le script de tâche suivant exécute VASP en parallèle avec l'ordonnanceur Slurm.

```bash title="vasp_job.sh"
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --ntasks=4             # number of MPI processes
#SBATCH --mem-per-cpu=1024M    # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  intelmpi/2019.7.217 vasp/<VERSION>
mpirun <VASP>
```

*   Ce script demande quatre cœurs et 4096Mo de mémoire (4x1024Mo).
*   `<ACCOUNT>` est le nom du compte Slurm; pour connaître la valeur à entrer, consultez [Exécuter des tâches](../running-jobs/running_jobs.md), section *Comptes et projets*.
*   `<VERSION>` est le numéro de version de VASP que vous voulez utiliser : 4.6, 5.4.1, 5.4.4 ou 6.1.0.
*   `<VASP>` est le nom de l'exécutable; voyez la section *Programmes exécutables* ci-dessus pour les exécutables que vous pouvez choisir.

```bash title="vasp_gpu_job.sh"
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --cpus-per-task=1      # number of CPU processes
#SBATCH --gres=gpu:p100:1      # Number of GPU type:p100 (valid type only for cedar)
#SBATCH --mem=3GB              # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  cuda/11.0  openmpi/4.0.3 vasp/<VERSION>
mpirun <VASP>
```

*   Ce script demande un (1) cœur CPU et 1024Mo de mémoire.
*   Ce script demande un (1) GPU de type p100, disponible uniquement sur Cedar; voyez les [types disponibles sur les autres superordinateurs](https://docs.computecanada.ca/wiki/Using_GPUs_with_Slurm/fr#N.C5.93uds_disponibles).
*   La tâche utilise `srun` pour faire exécuter VASP.

VASP utilise quatre fichiers d'entrée, soit INCAR, KPOINTS, POSCAR et POTCAR. Il est préférable de préparer les fichiers d’entrée dans un répertoire différent pour chaque tâche. Pour soumettre la tâche à partir du répertoire, utilisez
`sbatch vasp_job.sh`

Si vous ignorez combien de mémoire votre tâche nécessite, préparez tous vos fichiers d’entrée et exécutez `makeparam` dans une [tâche interactive](../running-jobs/running_jobs.md). Utilisez ensuite la quantité de mémoire obtenue en résultat pour la prochaine exécution. Pour obtenir une meilleure estimation pour les tâches futures, vérifiez quelle est la taille maximale de la pile de mémoire pour les [tâches complétées](../running-jobs/running_jobs.md) et utilisez cette valeur pour demander la quantité de mémoire par processeur.

Si vous voulez utiliser 32 cœurs ou plus, consultez la [politique d'ordonnancement des tâches](../running-jobs/job_scheduling_policies.md), section *Nœuds entiers ou cœurs*.

## Construire VASP par vous-même

Si vous disposez d'une licence VASP et que vous avez accès à du code source VASP, vous pouvez installer plusieurs versions dans votre répertoire `/home` sur toutes nos grappes avec les commandes [EasyBuild](../programming/easybuild.md) suivantes.

```bash
eb -f [RECIPE NAME] --sourcepath=[SOURCEPATH]
```

où `[SOURCEPATH]` est le répertoire contenant le code source de VASP et `[RECIPE NAME]` est le nom de la recette. Le premier onglet du tableau ci-dessous affiche la liste des recettes disponibles ainsi que les fichiers sources requis correspondants. Dans ce tableau, VTSTtools et vaspSOL correspondent respectivement aux extensions Transition State Tools et VASPsol. Le deuxième onglet affiche la liste des bibliothèques incluses dans VASP. Vous pouvez télécharger le code source depuis le [site web de VASP](https://www.vasp.at/). L'exécution de la commande peut prendre plus d'une heure. Une fois l'opération terminée, vous pourrez charger et exécuter VASP à l'aide des commandes `module`, comme expliqué précédemment dans [Utilisation des modules VASP](#utilisation-des-modules-vasp).

Pour construire une version personnalisée de VASP, voir [Installation de logiciels dans votre répertoire /home](../getting-started/installing_software_in_your_home_directory.md), [Installing VASP 5](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X) ou [Installing VASP 6](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X).

=== "Spécification et implémentation de recettes"

| Nom de la recette            | Version | Environnement | Fichier source         | CPU/GPU | VTSTtools | vaspSOL |
| :--------------------------- | :------ | :------------ | :--------------------- | :------ | :-------- | :------ |
| VASP-5.4.4-iimpi-2020a.eb    | 5.4.4   | StdEnv/2020   | vasp.5.4.4.pl2.tgz     | CPU     | oui       | oui     |
| VASP-6.1.2-iimpi-2020a.eb    | 6.1.2   | StdEnv/2020   | vasp.6.1.2_patched.tgz | CPU     | oui       | oui     |
| VASP-6.2.1-iimpi-2020a.eb    | 6.2.1   | StdEnv/2020   | vasp.6.2.1.tgz         | CPU     | oui       | oui     |
| VASP-6.3.0-iimpi-2020a.eb    | 6.3.0   | StdEnv/2020   | vasp.6.3.0.tgz         | CPU     | oui       | oui     |
| VASP-6.3.1-iimpi-2020a.eb    | 6.3.1   | StdEnv/2020   | vasp.6.3.1.tgz         | CPU     | oui       | oui     |
| VASP-5.4.4-iimpi-2023a.eb    | 5.4.4   | StdEnv/2023   | vasp.5.4.4.pl2.tgz     | CPU     | oui       | oui     |
| VASP-6.4.2-iimpi-2023a.eb    | 6.4.2   | StdEnv/2023   | vasp.6.4.2.tar         | CPU     | oui       | oui     |
| VASP-6.4.3-iimpi-2023a.eb    | 6.4.3   | StdEnv/2023   | vasp.6.4.3.tar         | CPU     | oui       | oui     |
| VASP-6.5.0-iimpi-2023a.eb    | 6.5.0   | StdEnv/2023   | vasp.6.5.0.tgz         | CPU     | non       | non     |
| VASP-6.5.1-iimpi-2023a.eb    | 6.5.1   | StdEnv/2023   | vasp.6.5.1.tgz         | CPU     | non       | non     |

=== "Bibliothèques incluses"

| Nom de la recette            | Fonction de Wannier | Beef | HDF5 | LibXC | ELPA | Libmbd | dft4 |
| :--------------------------- | :------------------ | :--- | :--- | :---- | :--- | :----- | :--- |
| VASP-5.4.4-iimpi-2020a.eb    | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.1.2-iimpi-2020a.eb    | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.2.1-iimpi-2020a.eb    | oui                 | oui  | non  | non   | non  | non    | non  |
| VASP-6.3.0-iimpi-2020a.eb    | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.3.1-iimpi-2020a.eb    | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.4.2-iimpi-2023a.eb    | oui                 | oui  | oui  | oui   | non  | non    | non  |
| VASP-6.4.3-iimpi-2023a.eb    | oui                 | oui  | oui  | oui   | non  | non    | oui  |
| VASP-6.5.0-iimpi-2023a.eb    | oui                 | oui  | oui  | oui   | oui  | oui    | oui  |
| VASP-6.5.1-iimpi-2023a.eb    | oui                 | oui  | oui  | oui   | oui  | oui    | oui  |

## Références

*   [Getting Started](https://www.vasp.at/tutorials/latest/part1/), guide sur le site Web de l'équipe de développement.
*   [py4vasp](https://www.vasp.at/py4vasp/latest/), interface Python pour l'extraction de données suite à des calculs avec VASP.