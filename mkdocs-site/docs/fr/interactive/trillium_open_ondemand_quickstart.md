---
title: "Trillium Open OnDemand Quickstart/fr"
slug: "trillium_open_ondemand_quickstart"
lang: "fr"

source_wiki_title: "Trillium Open OnDemand Quickstart/fr"
source_hash: "d200f33c27debc85b9e1752428a9449a"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:56:26.874640+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

Cette page décrit le service Open OnDemand sur Trillium. Pour de l'information générale sur les instances Open OnDemand sur nos grappes, voir [Open OnDemand](open_ondemand.md).

## Environnements virtuels Python

!!! warning "Environnements virtuels Python"
    En raison du changement de système d’exploitation et de pile logicielle, vos noyaux d’environnement virtuel Python existants risquent de ne pas fonctionner immédiatement sur le site OnDemand. Vous devriez pouvoir activer vos environnements Python dans un terminal Trillium (voir [Accès via terminal](#accès-via-terminal) ci-dessous), avec tous les modules Trillium requis chargés, puis exécuter la commande `venv2jup` pour les rendre fonctionnels.

## Introduction

Ce guide décrit les étapes de base pour démarrer avec le portail Open OnDemand de SciNet.

Open OnDemand (OOD) est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources informatiques, telles que JupyterLab, RStudio et Visual Studio Code. Elle vous permet d'interagir avec Trillium via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information, consultez [https://openondemand.org](https://openondemand.org).

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et allez à la page https://ondemand.scinet.utoronto.ca. Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou YubiKey. La connexion étant établie, vous accéderez au tableau de bord Open OnDemand, à partir duquel vous pourrez accéder aux différents outils et applications disponibles.

*   [Tableau de bord, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=fmks5--qaAfm6Zat&t=1316)

## Gestion des fichiers

La plateforme Open OnDemand propose un navigateur de fichiers pour gérer vos fichiers et répertoires dans le système de fichiers. Pour y accéder, cliquez sur l'onglet *Fichiers* (*Files*) et sélectionnez le répertoire à gérer dans le menu déroulant (comme `HOME`, `SCRATCH` ou `PROJECT`). Une fois le navigateur de fichiers ouvert, vous pourrez :

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et répertoires
*   Supprimer des fichiers et répertoires
*   Modifier des fichiers existants

Vous pouvez aussi consulter les quotas de stockage en cliquant sur le lien *Quotas de stockage* (*Storage Quotas*) sous l'onglet *Fichiers* (*Files*).

### Téléverser des fichiers

La taille maximale des fichiers que vous pouvez téléverser est présentement de 10 Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez [Globus](../getting-started/globus.md). Vous trouverez un bouton d'accès à Globus en haut à droite de l'interface. En cliquant dessus, l'interface web de Globus s'affichera, vous permettant de vous connecter avec votre nom d'utilisateur et votre mot de passe pour votre compte. Le chemin d'accès affiché dans le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

*   [Navigateur, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=e6Z2PvHRsCVmTKAQ&t=1510)

## Applications interactives

Open OnDemand offre également des applications interactives exécutables directement depuis votre navigateur web. Sous l'onglet *Applications interactives* (*Interactive Apps*), sélectionnez l'application désirée dans le menu déroulant. Ceci affichera la page de soumission des tâches, où vous pourrez choisir les paramètres de votre tâche, par exemple :

*   durée de la tâche (en heures)
*   nombre de cœurs demandé
*   quantité de mémoire allouée (en Go)
*   ressources GPU (le seul [profil MIG](../programming/multi-instance_gpu.md) disponible présentement est **h100_1.10**, qui offre 10 Go de mémoire et 1/8<sup>e</sup> de la puissance d'un GPU NVIDIA H100 entier.)
    *   [Demander un GPU, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=64jipPoV-5ZzQpky&t=3025)
*   courriel indiquant le début de la tâche

Après avoir sélectionné les paramètres de votre tâche, cliquez sur le bouton *Lancer* (*Launch*) pour l'ajouter à la file d'attente. La page *Mes sessions interactives* (*My Interactive Sessions*) s'affichera, où vous pourrez consulter l'état de votre tâche (en file d'attente, en cours d'exécution ou terminée). Une fois la tâche affectée à un nœud et en cours d'exécution, cliquez sur le bouton *Se connecter à...* (*Connect to...*) pour lancer l'application. Celle-ci s'ouvrira dans un nouvel onglet, vous permettant de travailler avec la tâche comme si elle était exécutée localement.

Pour accéder au terminal du nœud sur lequel l'application s'exécute, par exemple pour en surveiller les performances, cliquez sur le bouton situé à côté de *Hôte* (*Host*) et commençant par `>_`. Une fenêtre de terminal s'ouvrira alors dans votre navigateur, vous permettant d'exécuter directement des commandes sur le nœud.

Si vous souhaitez mettre fin à la tâche pour une quelconque raison, vous pouvez le faire en cliquant sur le bouton rouge *Supprimer* (*Delete*) dans le panneau de la tâche, sur la page *Mes sessions interactives* (*My Interactive Sessions*).

*   [Applications interactives, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=9Fapd_d6jiNTQqA&t=2118)

### Applications installées

Les applications suivantes sont prises en charge :

*   [JupyterLab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Trillium Desktop
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [Ovito](https://www.ovito.org)
*   [SAS](https://www.sas.com/en_ca/home.html)<sup>4</sup>
*   [Stata](https://www.stata.com)<sup>4</sup>
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

Pour demander l'installation d'autres applications, veuillez écrire à [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

*   [JupyterLab, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=Xxvu96XYVMNHocq8&t=2469)
*   [Bureau, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)

## Interfaces graphiques

Si vous souhaitez exécuter un logiciel doté d'une interface graphique (GUI) qui n'est pas installé comme application interactive, par exemple Octave ou Blender, vous pouvez utiliser l'application *Bureau Trillium* (*Trillium Desktop*). Cette application fournit un environnement de bureau à distance accessible via votre navigateur web. L'exemple suivant décrit l'exécution de l'interface graphique d'Octave.

1.  Sous l'onglet *Applications interactives* (*Interactive Apps*), sélectionnez *Bureau Trillium* (*Trillium Desktop*) dans le menu déroulant.
2.  Dans la page de soumission des tâches qui s'affiche, choisissez le nombre de cœurs et la quantité de mémoire à allouer à votre session, ainsi que la durée de la tâche (en heures). Cliquez ensuite sur le bouton *Lancer* (*Launch*) pour ajouter votre tâche à la file d'attente.
3.  La page *Mes sessions interactives* (*My Interactive Sessions*) s'affichera. Une fois votre tâche en cours d'exécution, vous pourrez améliorer la qualité et la compression de l'image de la session de bureau. Selon la vitesse de votre connexion Internet, vous pouvez réduire ces paramètres pour améliorer les performances et la réactivité du bureau. Cliquez sur le bouton *Se connecter au Bureau Trillium* (*Connect to Trillium Desktop*) pour lancer l'environnement de bureau distant dans un nouvel onglet.
    *   Une fois que l'environnement de bureau est chargé, ouvrez une fenêtre de terminal à l'aide du raccourci sur le bureau et chargez les modules nécessaires à Octave :
        ```bash
        module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
        ```
    *   Lancez ensuite l'interface graphique d'Octave en saisissant `octave --gui` dans la fenêtre de terminal.

L'interface graphique d'Octave devrait maintenant apparaître dans l'environnement de bureau distant. Vous pouvez utiliser cette méthode pour exécuter d'autres applications graphiques; assurez-vous simplement de charger les modules appropriés avant de lancer l'application. Les applications peuvent avoir différentes méthodes pour lancer leur interface graphique; veuillez consulter la documentation propre à chaque application. Pour voir la liste des binaires installés pour une application particulière en consultant sa variable d'environnement (par exemple, pour la liste des binaires Octave), lancez :

```bash
ls $EBROOTOCTAVE/bin
```

*   [Interface Octave, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)

## Soumettre une tâche

Open OnDemand offre également une interface qui permet de soumettre des tâches en lots à Trillium. Ceci peut s'avérer utile lorsque vous avez besoin de plus de ressources que celles fournies par les tâches interactives, par exemple un accès exclusif à 192 cœurs et 755 Go de mémoire sur un nœud de calcul de Trillium.

L'application [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) offre plusieurs scripts modèles que vous pouvez soumettre directement à l'ordonnanceur. Sous l'onglet *Historique* (*History*), elle propose aussi une interface pour faire le suivi des tâches que vous avez soumises. Vous avez accès à Open Composer sous le menu déroulant *Tâches* (*Jobs*) ou en cliquant sur un modèle de script.

Une fois le modèle sélectionné, la page de soumission de tâche s'affiche. Elle est divisée en deux parties : les paramètres de la tâche à gauche et le script à droite. Les paramètres vous permettent de contrôler les ressources utilisées, comme le nombre de nœuds, le nombre de tâches par nœud, la durée d'exécution et le nom du fichier de sortie. Le script affiche le texte qui sera soumis à l'ordonnanceur. Toute modification apportée aux paramètres se reflète automatiquement dans le script. Vous pouvez également modifier le script directement.

Les champs dans le haut de la page servent à modifier la manière dont la tâche sera soumise.

*   *Emplacement du script* (*Script Location*) indique le répertoire dans lequel le script sera sauvegardé et la tâche sera exécutée.
*   *Nom du script* (*Script Name*) indique le nom du fichier qui contient le script de la tâche.
*   *Nom de la tâche* (*Job Name*) indique le nom de la tâche tel qu'il apparaîtra dans la file d'attente.
*   *Grappe* (*Cluster*) permet de choisir la grappe sur laquelle la tâche sera soumise, par exemple Trillium (par défaut) ou Trillium-GPU. En sélectionnant Trillium-GPU, un paramètre s'ajoutera pour demander des ressources GPU.

Une fois que votre script est bien défini, cliquez sur le bouton *Soumettre* (*Submit*) pour soumettre la tâche à l'ordonnanceur et enregistrer le script dans l'*Emplacement du script* (*Script Location*). Si tout se passe bien, un message de confirmation s'affichera, avec l'identifiant de la tâche.

Remarque : Les scripts modèles sont des exemples de base que vous devrez adapter à vos besoins spécifiques, notamment en chargeant les modules requis et en spécifiant les fichiers d’entrée/sortie. Le script doit également respecter les limites imposées par l'ordonnanceur Slurm. Voir [Restrictions particulières à Trillium](../clusters/trillium_quickstart.md#restrictions-particulières-à-trillium) pour plus d’information sur la rédaction des scripts.

*   [Open Composer, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=r5vcEw-lgM7xSJ6_&t=4263)

### Suivi des tâches dans Open Composer

Sous l'onglet *Historique* (*History*) se trouve la liste de toutes vos tâches, avec leur état (en attente, en cours d'exécution, terminée, échec). Pour affiner une recherche, utilisez le champ *Filtre* (*Filter*) ou cliquez dans les cases à cocher ci-dessous. En cliquant sur les différentes colonnes, des informations spécifiques à chaque tâche s'afficheront.

*   *ID de la tâche* (*Job ID*) affiche la tâche dans [my.SciNet](https://my.scinet.utoronto.ca/) avec les statistiques de performance et des détails au sujet de Slurm. Le message *Non trouvé ou non autorisé* (*Not found or not permitted*) apparaît si la tâche est encore en attente ou si elle a été supprimée.
*   *Application* affiche une fenêtre pour modifier le script du modèle utilisé.
*   *Emplacement du script* (*Script Location*) ouvre une fenêtre de l'endroit où se trouve le script. Cliquez sur la petite icône de terminal pour ouvrir un terminal au même endroit.
*   *Nom du script* (*Script Name*) affiche le script soumis à l'ordonnanceur.

Pour modifier ou soumettre de nouveau une tâche déjà soumise, cliquez sur le script dans la colonne *Nom du script* (*Script Name*), puis sur *Charger les paramètres* (*Load Parameters*). La page de soumission de la tâche s'affichera et vous pourrez effectuer les modifications voulues.

### Applications prises en charge

Présentement, Open Composer prend en charge les applications suivantes pour l'ordonnanceur Slurm :

*   [MPI](../software/mpi.md)
*   [OpenMP](../programming/openmp.md)
*   Hybrid MPI/OpenMP
*   [Python](../software/python.md)
*   [R](../software/r.md)
*   [VASP](../software/vasp.md)

## Suivi des tâches

Pour obtenir un aperçu de toutes vos tâches en attente, utilisez l'interface de suivi des tâches. Sous l'onglet *Tâches* (*Jobs*), sélectionnez *Tâches actives* (*Active Jobs*). Vous pouvez utiliser le champ de texte *Filtre* (*Filter*) en haut à droite. Pour trier une colonne, cliquez sur son en-tête, par exemple par statut (en cours, terminée, échec, etc.). Cliquez sur le bouton à gauche d'une tâche pour obtenir des informations supplémentaires, telles que l'heure de début et de fin, la liste des nœuds et le compte auquel se rapporte l'utilisation des ressources. Pour afficher toutes les tâches en attente, cliquez sur le menu déroulant en haut à droite et sélectionnez *Toutes les tâches* (*All Jobs*). Une vue plus détaillée de vos tâches est disponible sur [le portail mySciNet](https://my.scinet.utoronto.ca).

*   [Tâches actives, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=rf_JMYBFz9ytpkR_&t=1818)

## Accès via terminal

Si vous préférez utiliser un terminal pour interagir avec la grappe, Open OnDemand met à votre disposition un terminal web pour accéder à l'interface en ligne de commande. Pour ce faire, rendez-vous dans l'onglet *Grappes* (*Clusters*) et sélectionnez *Accès Shell Trillium* (*Trillium Shell Access*). Une nouvelle fenêtre de terminal s'ouvrira alors dans votre navigateur, où vous pourrez exécuter des commandes comme dans une session de terminal classique.

*   [Terminal, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=REh17mvUn8q50iys&t=1904)

## Modules logiciels

Trillium offre plusieurs logiciels accessibles via des modules. Ces modules peuvent être chargés dans vos sessions interactives, votre terminal ou vos scripts de tâches dans Open Composer. Vous pouvez consulter les modules disponibles et leurs versions grâce à l'application *Navigateur de modules* (*Module Browser*), sous l'onglet *Grappes* (*Clusters*) de la barre de navigation. Le navigateur de modules fournit également une commande à exécuter dans le terminal pour charger un module spécifique, ce qui peut s'avérer utile lors de la rédaction de scripts de tâches.

## Débogage

Si vous rencontrez des erreurs lors de l'utilisation d'une tâche interactive, vous pouvez consulter les fichiers de journalisation. Pour y accéder, rendez-vous sous l'onglet *Mes sessions interactives* (*My Interactive Sessions*) et sélectionnez votre session active. Cliquez sur le lien `output.log` pour ouvrir un nouvel onglet affichant la sortie de votre tâche. Ce fichier contient la sortie standard et les messages d'erreur générés par la tâche, ce qui peut vous aider à identifier les problèmes survenus pendant la session. Si vous avez besoin d'assistance, cliquez sur le bouton de soutien qui se trouve dans la carte de la session. Veuillez inclure le fichier `output.log` et toute autre information pertinente afin de nous permettre de vous aider plus efficacement.

## Tutoriels

Vidéos de SciNet (en anglais)

*   [Tableau de bord](https://youtu.be/XRozBBKwA8c?si=fmks5--qaAfm6Zat&t=1316)
*   [Navigateur](https://youtu.be/XRozBBKwA8c?si=e6Z2PvHRsCVmTKAQ&t=1510)
*   [Tâches interactives](https://youtu.be/XRozBBKwA8c?si=9Fapd_d6jiNTQqA&t=2118)
*   [JupyterLab](https://youtu.be/XRozBBKwA8c?si=Xxvu96XYVMNHocq8&t=2469)
*   [Bureau](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)
*   [Soumettre des tâches avec Open Composer](https://youtu.be/XRozBBKwA8c?si=r5vcEw-lgM7xSJ6_&t=4263)
*   [Terminal](https://youtu.be/XRozBBKwA8c?si=REh17mvUn8q50iys&t=1904)
*   [Suivi des tâches](https://youtu.be/XRozBBKwA8c?si=rf_JMYBFz9ytpkR_&t=1818)

## Comparaison avec JupyterHub

| fonctionnalité                  | JupyterHub (hors service définitivement)       | Open OnDemand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------------------------------ | :--------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authentification                | mot de passe                                   | mot de passe et authentification multifacteur                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| première installation           | 2017                                           | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| plus récente mise à jour       | 2021                                           | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| supporte                        | Jupyter Notebook, JupyterLab (R, Python, Julia) | Jupyter Notebook, JupyterLab (R, Python), RStudio, VSCode, Desktop, SAS<sup>4</sup>, Stata<sup>4</sup>, ParaView, Forge DDT/MAP, MATLAB                                                                                                                                                                                                                                                                                                                                                         |
| arrêt et reprise plus tard     | oui                                            | oui<sup>1</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| terminal de commande            | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| gestion des fichiers            | oui (limitée)                                  | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| suivi des tâches                | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| soumission des tâches           | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| maximum de cœurs                | 8 cœurs<sup>2</sup>                            | 20 cœurs (8 pour mémoire forte)<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| maximum de mémoire              | 48 Go<sup>2</sup>                              | 85 Go (500 Go pour mémoire forte)<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| maximum de durée                | 3 jours<sup>2</sup>                            | 3 jours<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| système d'exploitation          | CentOS 7                                       | RockyLinux 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| piles logicielles               | NiaEnv, CCEnv                                  | CCEnv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| notification des problèmes de système | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| notification des quotas de l'utilisateur | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| journalisation des erreurs      | non                                            | oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| matériel                        | 1 x CPU de 40 Intel "CascadeLake" cœurs à 2.5 GHz, 1 To de RAM | 62 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 180 Go de RAM (par défaut)<br>3 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 1 To de RAM (mémoire forte)<br> 4 x GPU NVIDIA H100 80 Go<br> 1 x CPU de 6 cœurs AMD EPYC 9654 à 2.4 GHz, 810 Go de RAM |

<sup>1</sup> À l'intérieur des limites demandées.

<sup>2</sup> Parce que les limites pour JupyterHub n'ont pas été implémentées très strictement, elles peuvent temporairement être surpassées.

<sup>3</sup> Demander les limites avant de lancer une application.

<sup>4</sup> Vous devez détenir une licence.