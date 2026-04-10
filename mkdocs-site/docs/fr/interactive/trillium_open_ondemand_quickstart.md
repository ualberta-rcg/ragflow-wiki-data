---
title: "Trillium Open OnDemand Quickstart/fr"
slug: "trillium_open_ondemand_quickstart"
lang: "fr"

source_wiki_title: "Trillium Open OnDemand Quickstart/fr"
source_hash: "aa0884a2244ec1401f7fca7f89b9112e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:05:52.491864+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Cette page décrit le service Open OnDemand sur Trillium. Pour l'information générale sur les instances Open OnDemand sur nos grappes, voir [Open OnDemand](open-ondemand.md).

## Porter un environnement virtuel sur Open OnDemand

!!! important
    **IMPORTANT : En raison du changement de système d’exploitation et de pile logicielle, vos noyaux d’environnement virtuel Python existants risquent de ne pas fonctionner immédiatement sur le site OnDemand. Vous devriez pouvoir activer vos environnements Python dans un terminal Trillium (voir ci-dessous [Accès via terminal](#accès-via-terminal)), avec tous les modules Trillium requis chargés, puis exécuter la commande `venv2jup` pour les rendre fonctionnels.**

## Introduction

Ce guide décrit les étapes de base pour démarrer avec le portail Open OnDemand de SciNet.

Open OnDemand (OOD) est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources informatiques, telles que Jupyter Lab, R Studio et Visual Studio Code. Elle vous permet d'interagir avec Trillium via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information, consultez le [site web openondemand.org](https://openondemand.org).

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et allez à la page [https://ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca). Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou YubiKey. La connexion étant établie, le tableau de bord Open OnDemand sera affiché. Vous pourrez alors accéder aux différents outils et applications disponibles.

## Gestion des fichiers

La plateforme Open OnDemand propose un explorateur permettant de gérer vos fichiers et répertoires dans le système de fichiers. Pour y accéder, cliquez sur l'onglet **Files** et sélectionnez le répertoire à gérer dans le menu déroulant (`HOME`, `SCRATCH` ou `PROJECT`). L'explorateur de fichiers sera affiché et vous pourrez :

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et répertoires
*   Supprimer des fichiers et répertoires
*   Modifier des fichiers existants

Les quotas de stockage peuvent aussi être affichés en cliquant sur le lien **Storage Quotas** dans l'onglet **Files**.

### Téléverser des fichiers

La taille maximale des fichiers à téléverser est présentement de 10 Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez [Globus](globus.md). Un bouton Globus est disponible en haut à droite de l'explorateur de fichiers. Cliquez sur ce bouton pour faire afficher l'interface web de Globus où vous pourrez vous connecter avec votre nom d'utilisateur et votre mot de passe avec l'Alliance. Le chemin d'accès affiché dans le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

## Soumettre une tâche

Open OnDemand offre également une interface permettant de soumettre des tâches en lots à Trillium. Ceci peut s'avérer utile lorsque vous avez besoin de plus de ressources que celles fournies par les tâches interactives, par exemple un accès exclusif à 192 cœurs et 755 Go de mémoire sur un nœud de calcul Trillium.

L'application [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) offre une série de scripts de modèles de tâches Slurm qui peuvent être soumis directement à l'ordonnanceur de Trillium. Elle fournit également une interface pour suivre vos tâches soumises, via l'onglet **History**. Vous pouvez accéder à Open Composer en naviguant dans le menu déroulant **Jobs** et en sélectionnant **Open Composer** ou en cliquant sur l'un des modèles de tâches Slurm, par exemple **MPI Slurm Job**, **OpenMP Slurm Job** et **Hybrid MPI/OpenMP Slurm Job**.

Une fois que vous avez sélectionné un modèle de tâche, vous serez dirigé vers la page de soumission de tâche. Cette page est divisée entre les paramètres de la tâche à gauche et le script de tâche lui-même à droite. Les paramètres de tâche vous permettent de contrôler les ressources que votre tâche utilisera, comme le nombre de nœuds, le nombre de tâches par nœud, le temps d'exécution (`wall clock time`) et le nom du fichier de sortie. La section du script de tâche affiche le script qui sera soumis à l'ordonnanceur. Toute modification apportée aux paramètres de tâche sera automatiquement reflétée dans le script de tâche. Vous pouvez également modifier le script de tâche directement si vous le souhaitez.

Les champs supplémentaires en haut de la page vous permettent de modifier la façon dont votre tâche est soumise :

*   **Script Location** : spécifie le répertoire où le script de tâche sera sauvegardé et d'où votre tâche sera exécutée.
*   **Script Name** : spécifie le nom du fichier du script de tâche.
*   **Job Name** : spécifie le nom de la tâche qui apparaîtra dans la file d'attente des tâches.
*   **Cluster** : vous permet de choisir le cluster auquel soumettre votre tâche, par exemple Trillium (par défaut) ou Trillium-GPU. La sélection de Trillium-GPU fournira un paramètre de tâche supplémentaire pour demander des ressources GPU.

Lorsque vous êtes satisfait de votre script de tâche, cliquez sur le bouton **Submit** pour soumettre la tâche à l'ordonnanceur et sauvegarder votre script dans le **Script Location**. Si votre tâche a été soumise avec succès, un message de confirmation apparaîtra en haut de la page avec l'identifiant de votre tâche.

Note : Les scripts modèles fournis dans Open Composer sont des exemples de base pour vous aider à démarrer. Vous devrez modifier davantage le script de tâche pour l'adapter à vos besoins spécifiques, comme le chargement des modules requis et la spécification des fichiers d'entrée/sortie. Le script de tâche doit toujours respecter les limites définies par l'ordonnanceur Slurm de Trillium. Veuillez consulter la [documentation de Trillium](https://docs.alliancecan.ca/wiki/Trillium_Quickstart#Trillium_specific_restrictions) pour plus d'informations sur la rédaction des scripts de tâche.

### Suivi des tâches dans Open Composer

Pour suivre vos tâches soumises dans Open Composer, naviguez vers l'onglet **History**. Ceci affichera une liste de toutes vos tâches soumises, ainsi que leur statut : Queued (En attente), Running (En cours d'exécution), Completed (Terminé), Failed (Échoué). Vous pouvez filtrer les tâches en utilisant la boîte de texte **Filter** en haut à droite ou en utilisant les cases à cocher ci-dessous. Cliquer sur différents champs de colonne donnera des informations différentes sur la tâche :

*   **Job ID** : ouvre la tâche dans [my.SciNet](https://my.scinet.utoronto.ca/), qui affiche des statistiques de performance et des informations Slurm plus détaillées sur la tâche. Note : my.SciNet peut afficher 'Not found or not permitted' si la tâche n'a pas encore démarré ou a été annulée.
*   **Application** : ouvre l'éditeur de script de tâche du modèle que vous avez utilisé.
*   **Script Location** : ouvre une fenêtre de l'explorateur de fichiers OOD à l'emplacement du script de tâche. Cliquer sur la petite icône de terminal ouvrira un terminal à l'emplacement du script de tâche.
*   **Script Name** : affiche le script de tâche qui a été soumis à l'ordonnanceur.

Pour soumettre à nouveau ou modifier une tâche précédemment exécutée, cliquez sur le script de tâche sous la colonne **Script Name** et cliquez sur **Load Parameters**. Cela vous ramènera à la page de soumission de tâche où des modifications supplémentaires pourront être apportées à la tâche.

### Applications prises en charge

Présentement, Open Composer prend en charge les applications suivantes :

*   MPI Slurm Job
*   OpenMP Slurm Job
*   Hybrid MPI/OpenMP Slurm Job
*   Python Slurm Job
*   R Slurm Job
*   VASP Slurm Job

## Suivi des tâches

Pour obtenir un aperçu de toutes vos tâches en file d'attente, vous pouvez utiliser l'interface de suivi des tâches. Naviguez vers l'onglet **Jobs** et sélectionnez **Active Jobs**. Vous pouvez filtrer les tâches en utilisant la boîte de texte **Filter** en haut à droite. Les colonnes peuvent également être triées en cliquant sur les en-têtes de colonne; par exemple, vous pouvez trier par statut de tâche (Running, Completed, Failed, etc.). Cliquer sur `>` à gauche d'une tâche vous montrera plus de détails sur celle-ci, comme l'heure de début/fin, la liste des nœuds et le compte facturé, etc. Vous voudrez peut-être aussi afficher toutes les tâches en file d'attente; vous pouvez le faire en cliquant sur le menu déroulant en haut à droite et en sélectionnant **All Jobs**. Une vue plus détaillée de vos tâches peut toujours être trouvée en utilisant le [portail myscinet](https://my.scinet.utoronto.ca).

### Applications interactives

Open OnDemand propose également des applications interactives qui peuvent être exécutées directement depuis votre navigateur web. Pour accéder aux applications, naviguez vers l'onglet **Interactive Apps** et sélectionnez l'application que vous souhaitez exécuter à partir du menu déroulant. Cela vous mènera ensuite à la page de soumission de tâche où vous pourrez choisir des paramètres de tâche tels que :

*   Durée de la tâche en heures
*   Nombre de cœurs
*   Quantité de mémoire à allouer (Go)
*   Ressources GPU (**Note** : seul le profil [MIG h100_1.10](https://docs.alliancecan.ca/wiki/Multi-Instance_GPU) est actuellement disponible, lequel fournit 10 Go de mémoire et 1/8 des ressources de calcul d'un GPU NVIDIA H100 complet.)
*   M'avertir par courriel lorsque la tâche démarre

Lorsque vous avez choisi vos paramètres de tâche, cliquez sur le bouton **Launch** pour soumettre votre tâche à la file d'attente. Vous serez dirigé vers la page **My Interactive Sessions** où vous pourrez voir le statut de votre tâche, c'est-à-dire En attente (`queued`), En cours d'exécution (`running`) ou Terminé (`completed`). Une fois qu'un nœud a été attribué à la tâche et qu'elle est en cours d'exécution, vous pouvez cliquer sur le bouton **Connect to ...** pour lancer l'application. L'application s'ouvrira dans un nouvel onglet de votre navigateur, et vous pourrez interagir avec elle comme si elle s'exécutait localement.

Si vous souhaitez accéder au terminal du nœud où l'application s'exécute, par exemple pour surveiller les performances, vous pouvez cliquer sur le bouton situé à côté de **Host**, commençant par `>_`. Cela ouvrira une fenêtre de terminal dans votre navigateur où vous pourrez exécuter des commandes directement sur le nœud.

Si, pour une raison quelconque, vous souhaitez arrêter la tâche, vous pouvez le faire en cliquant sur le bouton rouge **Delete** dans le panneau de la tâche sur la page **My Interactive Sessions**.

### Applications installées

Les applications suivantes sont prises en charge :

*   [Jupyter Lab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Trillium Desktop
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [SAS](https://www.sas.com/en_ca/home.html)
*   [Stata](https://www.stata.com)
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

Pour faire installer d'autres applications, écrivez à [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

## Interfaces graphiques

Si vous souhaitez exécuter un logiciel doté d'une interface utilisateur graphique (GUI) qui n'est pas encore installé comme application interactive, tel qu'Octave ou Blender, vous pouvez le faire en utilisant l'application **Trillium Desktop**. Cette application fournit un environnement de bureau à distance auquel vous pouvez accéder via votre navigateur web. Dans l'exemple suivant, nous allons exécuter l'interface graphique d'Octave :

1.  Naviguez vers l'onglet **Interactive Apps** et sélectionnez **Trillium Desktop** dans le menu déroulant.
2.  Vous serez dirigé vers la page de soumission de tâche. Choisissez le nombre de cœurs et la quantité de mémoire que vous souhaitez allouer pour votre session, en plus de la durée de votre tâche en heures. Cliquez ensuite sur le bouton **Launch** pour soumettre votre tâche à la file d'attente.
3.  Cela vous mènera à la page **My Interactive Sessions**. Une fois votre tâche en cours d'exécution, vous avez la possibilité d'améliorer la **Image Quality** et la **Image Compression** de la session de bureau. Selon la vitesse de votre connexion Internet, vous pouvez réduire ces paramètres pour améliorer les performances et la réactivité du bureau. Cliquez sur le bouton **Connect to Trillium Desktop** pour lancer l'environnement de bureau à distance dans un nouvel onglet.
4.  Une fois l'environnement de bureau chargé, ouvrez une fenêtre de terminal à l'aide du raccourci du bureau et chargez les modules requis pour Octave :
    ```bash
    $ module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
    ```
5.  Lancez maintenant l'interface graphique d'Octave en tapant `octave --gui` dans la fenêtre du terminal.

Vous devriez maintenant voir l'interface graphique d'Octave apparaître dans l'environnement de bureau à distance. Vous pouvez utiliser cette méthode pour exécuter d'autres applications graphiques également, assurez-vous simplement de charger les modules appropriés avant de lancer l'application. Les applications peuvent avoir différentes façons de lancer leur interface graphique, veuillez donc consulter la documentation de l'application pour plus d'informations. Vous pouvez voir la liste des binaires installés pour une application donnée en consultant sa variable d'environnement, par exemple, exécutez `ls $EBROOTOCTAVE/bin` pour voir la liste des binaires d'Octave.

## Accès via terminal

Parfois, vous préférerez peut-être utiliser un terminal pour interagir avec Trillium. Open OnDemand fournit un terminal web que vous pouvez utiliser pour accéder à l'interface de ligne de commande. Pour accéder au terminal, naviguez vers l'onglet **Clusters** et sélectionnez **Trillium Shell Access**. Cela ouvrira un nouvel onglet dans votre navigateur avec une fenêtre de terminal où vous pourrez exécuter des commandes comme vous le feriez dans une session de terminal normale.

## Modules logiciels

Trillium dispose d'une grande variété de logiciels accessibles via des modules. Ils peuvent être chargés dans vos sessions interactives, votre terminal ou vos scripts de tâche dans Open Composer. Vous pouvez consulter les modules disponibles et leurs versions à l'aide de l'application **Module Browser**, accessible depuis l'onglet **Clusters** de la barre de navigation. Le navigateur de modules fournit également une commande que vous pouvez exécuter dans le terminal pour charger un module particulier, ce qui peut être utile lors de la rédaction de scripts de tâche, par exemple.

## Débogage

Si vous rencontrez des erreurs lors de l'utilisation d'une tâche interactive Open OnDemand, vous pouvez consulter les journaux pour plus d'informations. Pour accéder aux journaux, naviguez vers l'onglet **My Interactive Sessions** et trouvez votre session active. Cliquez sur le lien `output.log` pour ouvrir un nouvel onglet affichant la sortie de votre tâche. Ce fichier contient les messages de sortie standard et d'erreur générés par la tâche, ce qui peut vous aider à identifier tout problème survenu pendant la session. Lorsque vous soumettez un ticket au support de SciNet, veuillez inclure le fichier `output.log`, votre **Session ID**, affiché comme une longue chaîne de caractères, par exemple **8feb45fa-bc65-4846-8398-2a73c1bf8e5a**, ainsi que toute autre information pertinente pour nous aider plus efficacement.

## Comparaison avec Jupyter Hub

| Caractéristique             | Jupyter Hub (hors service)                           | Open OnDemand                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------- | :--------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentification            | mot de passe                                         | mot de passe + MFA                                                                                                                                                                                                                                                                                                                                                                                            |
| Première installation       | 2017                                                 | 2025                                                                                                                                                                                                                                                                                                                                                                                                          |
| Dernière mise à jour        | 2021                                                 | 2025                                                                                                                                                                                                                                                                                                                                                                                                          |
| Prend en charge             | Jupyter Notebook, JupyterLab (R, Python, Julia)      | Jupyter Notebook, JupyterLab (R, Python), Rstudio, VSCode, Desktop, SAS[^4], Stata[^4], ParaView, Forge DDT/MAP, MATLAB                                                                                                                                                                                                                                                                                         |
| Démarrer et reprendre plus tard | Oui                                                  | Oui[^1]                                                                                                                                                                                                                                                                                                                                                                                                       |
| Terminal de commandes       | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Gestion des fichiers        | Oui (limitée)                                        | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Suivi des tâches            | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Soumission de tâches        | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Limite de cœurs             | 8 cœurs[^2]                                          | 20 cœurs (8 pour la haute mémoire)[^3]                                                                                                                                                                                                                                                                                                                                                                        |
| Limite de mémoire           | 48 Go[^2]                                            | 85 Go (500 Go pour la haute mémoire)[^3]                                                                                                                                                                                                                                                                                                                                                                      |
| Limites de temps            | 3 jours[^2]                                          | 3 jours[^3]                                                                                                                                                                                                                                                                                                                                                                                                   |
| Système d'exploitation      | CentOS 7                                             | RockyLinux 9                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pile logicielle             | NiaEnv, CCEnv                                        | CCEnv                                                                                                                                                                                                                                                                                                                                                                                                         |
| Alertes de problèmes système | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Alertes de quota utilisateur | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Journaux d'erreurs          | Non                                                  | Oui                                                                                                                                                                                                                                                                                                                                                                                                           |
| Matériel                    | 1 processeur avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 1 To de RAM | 62 processeurs avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 180 Go de RAM (par défaut)<br>3 processeurs avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 1 To de RAM (haute mémoire)<br>4 GPU NVIDIA H100 80 Go, avec un processeur AMD EPYC 9654 à 96 cœurs à 2,4 GHz, 810 Go de RAM |

[^1]: À l'intérieur des limites demandées.
[^2]: Parce que les limites pour JupyterHub n'ont pas été implémentées très strictement, elles peuvent temporairement être surpassées.
[^3]: Demander les limites avant de lancer une application.
[^4]: Vous devez détenir une licence.