---
title: "Trillium Open OnDemand Quickstart/fr"
slug: "trillium_open_ondemand_quickstart"
lang: "fr"

source_wiki_title: "Trillium Open OnDemand Quickstart/fr"
source_hash: "aa0884a2244ec1401f7fca7f89b9112e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:08:26.895165+00:00"

tags:
  []

keywords:
  - "node"
  - "interface web"
  - "binaries"
  - "détenir une licence"
  - "implémentées strictement"
  - "Intel CascadeLake"
  - "job submission"
  - "application"
  - "hardware"
  - "Open Composer"
  - "Globus"
  - "History tab"
  - "submitted jobs"
  - "browser tab"
  - "limites demandées"
  - "Open OnDemand"
  - "Interactive Sessions"
  - "Software modules"
  - "bouton Globus"
  - "Interactive Apps"
  - "terminal access"
  - "Accès via terminal"
  - "monitor performance"
  - "Job monitoring"
  - "Slurm job script"
  - "environment variable"
  - "environnement virtuel"
  - "lancer une application"
  - "Interactive sessions"
  - "Trillium"
  - "error logs"
  - "Octave"
  - "filter jobs"
  - "user quota alerts"
  - "Interactive applications"
  - "Slurm Job"
  - "Graphical User Interface"
  - "téléverser des fichiers"
  - "JupyterHub"
  - "Trillium Desktop"
  - "job status"
  - "explorateur de fichiers"
  - "system issue alerts"
  - "Jupyter Hub"
  - "gestion des fichiers"

questions:
  - "Comment doit-on procéder pour rendre fonctionnels les environnements virtuels Python existants sur le site OnDemand de Trillium ?"
  - "Quelles sont les étapes et les méthodes d'authentification requises pour se connecter au portail Open OnDemand ?"
  - "Quelles sont les fonctionnalités offertes par l'explorateur de fichiers et quelle alternative est recommandée pour téléverser des fichiers de plus de 10 Go ?"
  - "Quel est le rôle principal de l'application Open Composer pour la soumission de tâches en lots sur la grappe Trillium ?"
  - "Quels paramètres spécifiques peuvent être configurés dans l'interface avant de soumettre un script de tâche au planificateur ?"
  - "Comment les utilisateurs peuvent-ils surveiller l'état de leurs tâches soumises et filtrer les résultats dans l'onglet Historique ?"
  - "Où se trouve le bouton permettant d'accéder à Globus dans l'explorateur de fichiers ?"
  - "Quels identifiants doivent être utilisés pour se connecter à l'interface web de Globus ?"
  - "Quel est le lien entre le chemin d'accès affiché dans Open OnDemand et celui ouvert dans Globus ?"
  - "How can a user navigate to monitor their submitted jobs in Open Composer?"
  - "What are the specific statuses that can be displayed for jobs in the History tab?"
  - "How can users filter their job list and access more detailed information about individual jobs?"
  - "How can a user modify and resubmit a previously run job using the Open Composer interface?"
  - "What tools and filters are available in the job monitoring interface to track and view details of active jobs?"
  - "What parameters can be configured when launching an interactive application, and how do you connect to the session once it starts?"
  - "Comment peut-on annuler une tâche interactive à partir de la page des sessions ?"
  - "Quelles sont les applications actuellement prises en charge et quelle est la procédure pour en faire installer de nouvelles ?"
  - "Quelles sont les étapes à suivre pour lancer un logiciel avec interface graphique (comme Octave) en utilisant l'environnement Trillium Desktop ?"
  - "How does the application behave when it is opened in a new browser tab?"
  - "For what purposes might a user need terminal access to the node running the application?"
  - "What specific steps must a user take to open the terminal window within their browser?"
  - "Comment peut-on afficher la liste des binaires d'Octave à l'aide des variables d'environnement ?"
  - "Quelle interface spécifique est présentée dans la Figure 10 pour l'utilisation d'Octave ?"
  - "Quelle méthode d'accès alternative au système est illustrée par la Figure 11 ?"
  - "How do users access the web-based command-line terminal and browse available software modules in Trillium?"
  - "What is the process for debugging errors in an interactive session and what specific details should be provided to SciNet support?"
  - "What are the primary differences in features, resource limits, and hardware between Open OnDemand and the decommissioned Jupyter Hub?"
  - "Which of the compared systems supports system issue alerts, user quota alerts, and error logs?"
  - "How does the hardware capacity, specifically regarding CPU cores and RAM, differ between the two environments?"
  - "What are the exact specifications of the NVIDIA GPU hardware available in the second configuration?"
  - "Pourquoi les limites de JupyterHub peuvent-elles être temporairement surpassées ?"
  - "Que faut-il faire concernant les limites avant de lancer une application ?"
  - "Quelle condition préalable est exigée concernant la licence d'utilisation ?"
  - "Pourquoi les limites de JupyterHub peuvent-elles être temporairement surpassées ?"
  - "Que faut-il faire concernant les limites avant de lancer une application ?"
  - "Quelle condition préalable est exigée concernant la licence d'utilisation ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page décrit le service Open OnDemand sur Trillium. Pour l'information générale sur les instances Open OnDemand sur nos grappes, voir [Open OnDemand](open_ondemand.md).

## Porter un environnement virtuel sur Open OnDemand

!!! important
    **IMPORTANT** : En raison du changement de système d’exploitation et de pile logicielle, vos noyaux d’environnement virtuel Python existants risquent de ne pas fonctionner immédiatement sur le site OnDemand. Vous devriez pouvoir activer vos environnements Python dans un terminal Trillium (voir ci-dessous [Accès via terminal](#accès-via-terminal)), avec tous les modules Trillium requis chargés, puis exécuter la commande **`venv2jup`** pour les rendre fonctionnels.

## Introduction

Ce guide décrit les étapes de base pour démarrer avec le portail Open OnDemand de SciNet.

Open OnDemand (OOD) est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources informatiques, telles que Jupyter Lab, R Studio et Visual Studio Code. Elle vous permet d'interagir avec Trillium via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information, consultez le site web [https://openondemand.org](https://openondemand.org).

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et allez à la page [https://ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca). Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou YubiKey. La connexion étant établie, le tableau de bord Open OnDemand sera affiché. Vous pourrez alors accéder aux différents outils et applications disponibles.

## Gestion des fichiers

La plateforme Open OnDemand propose un explorateur permettant de gérer vos fichiers et répertoires dans le système de fichiers. Pour y accéder, cliquez sur l'onglet **Fichiers** et sélectionnez le répertoire à gérer dans le menu déroulant (`HOME`, `SCRATCH` ou `PROJECT`). L'explorateur de fichiers sera affiché et vous pourrez :

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et répertoires
*   Supprimer des fichiers et répertoires
*   Modifier des fichiers existants

Les quotas de stockage peuvent aussi être affichés en cliquant sur le lien **Quotas de stockage** dans l'onglet **Fichiers**.

### Téléverser des fichiers

La taille maximale des fichiers à téléverser est présentement de 10 Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez [Globus](../getting-started/globus.md). Un bouton **Globus** est disponible en haut à droite de l'explorateur de fichiers. Cliquez sur ce bouton pour faire afficher l'interface web de Globus où vous pourrez vous connecter avec votre nom d'utilisateur et votre mot de passe avec l'Alliance. Le chemin d'accès affiché dans le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

## Soumettre une tâche

Open OnDemand offre également une interface permettant de soumettre des tâches en lots à Trillium. Ceci peut s'avérer utile lorsque vous avez besoin de plus de ressources que celles fournies par les tâches interactives, par exemple un accès exclusif à 192 cœurs et 755 Go de mémoire sur un nœud de calcul Trillium.

L'application [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) offre une suite de scripts de modèles de tâches Slurm qui peuvent être soumis directement au planificateur Trillium. Elle fournit également une interface pour surveiller vos tâches soumises, via l'onglet **Historique**. Vous pouvez accéder à Open Composer en naviguant dans le menu déroulant **Tâches** et en sélectionnant **Open Composer** ou en cliquant sur l'un des modèles de tâches Slurm, par exemple **Tâche Slurm MPI**, **Tâche Slurm OpenMP** et **Tâche Slurm MPI/OpenMP hybride**.

Une fois que vous avez sélectionné un modèle de tâche, vous serez dirigé vers la page de soumission de tâche. Celle-ci est divisée entre les paramètres de tâche à gauche et le script de tâche lui-même à droite. Les paramètres de tâche vous permettent de contrôler les ressources que votre tâche utilisera, telles que le nombre de nœuds, le nombre de tâches par nœud, le temps d'exécution (`wall clock time`) et le nom du fichier de sortie. La section du script de tâche affiche le script qui sera soumis au planificateur. Toute modification apportée aux paramètres de tâche sera automatiquement reflétée dans le script de tâche. Vous pouvez également modifier le script de tâche directement si vous le souhaitez.

Les champs supplémentaires en haut de la page vous permettent de modifier la manière dont votre tâche est soumise :

*   **Emplacement du script** (`Script Location`) : Spécifie le répertoire où le script de tâche sera sauvegardé et d'où votre tâche sera exécutée.
*   **Nom du script** (`Script Name`) : Spécifie le nom du fichier de script de tâche.
*   **Nom de la tâche** (`Job Name`) : Spécifie le nom de la tâche qui apparaîtra dans la file d'attente des tâches.
*   **Grappe** (`Cluster`) : Vous permet de changer la grappe à laquelle soumettre votre tâche, par exemple Trillium (par défaut) ou Trillium-GPU. La sélection de Trillium-GPU fournira un paramètre de tâche supplémentaire pour demander des ressources GPU.

Une fois que vous êtes satisfait de votre script de tâche, cliquez sur le bouton **Soumettre** pour soumettre la tâche au planificateur et enregistrer votre script à l'**Emplacement du script**. Si votre tâche a été soumise avec succès, vous verrez un message de confirmation en haut de la page avec votre ID de tâche.

!!! note "Note"
    Les scripts de modèles fournis dans Open Composer sont des exemples de base pour vous aider à démarrer. Vous devrez modifier davantage le script de tâche pour l'adapter à vos besoins spécifiques, comme le chargement des modules requis et la spécification des fichiers d'entrée/sortie. Le script de tâche doit toujours se conformer aux limites définies par le planificateur Slurm de Trillium. Veuillez consulter la [documentation de Trillium](https://docs.alliancecan.ca/wiki/Trillium_Quickstart#Trillium_specific_restrictions) pour plus d'informations sur la rédaction des scripts de tâche.

### Suivi des tâches dans Open Composer

Pour surveiller vos tâches soumises dans Open Composer, naviguez vers l'onglet **Historique**. Ceci affichera une liste de toutes vos tâches soumises, ainsi que leur statut : En file d'attente (`Queued`), En cours d'exécution (`Running`), Terminée (`Completed`), Échouée (`Failed`). Vous pouvez filtrer les tâches en utilisant la boîte de texte **Filtre** en haut à droite ou en utilisant les cases à cocher ci-dessous. Cliquer sur différents champs de colonne donnera différentes informations sur la tâche :

*   **ID de tâche** (`Job ID`) : Ouvre la tâche dans [my.SciNet](https://my.scinet.utoronto.ca/), qui affiche les statistiques de performance et des informations Slurm plus détaillées sur la tâche. Note : my.SciNet peut afficher « Introuvable ou non autorisé » si la tâche n'a pas encore démarré ou a été annulée.
*   **Application** (`Application`) : Ouvre l'éditeur de script de tâche du modèle que vous avez utilisé.
*   **Emplacement du script** (`Script Location`) : Ouvre une fenêtre d'explorateur de fichiers OOD à l'emplacement du script de tâche. Cliquer sur la petite icône de terminal ouvrira un terminal à l'emplacement du script de tâche.
*   **Nom du script** (`Script Name`) : Affiche le script de tâche qui a été soumis au planificateur.

Pour resoumettre ou modifier une tâche précédemment exécutée, cliquez sur le script de tâche sous la colonne **Nom du script** et cliquez sur **Charger les paramètres** (`Load Parameters`). Ceci vous ramènera à la page de soumission de tâche où d'autres modifications peuvent être apportées à la tâche.

### Applications prises en charge

Présentement, Open Composer prend en charge les applications suivantes :

*   Tâche Slurm MPI
*   Tâche Slurm OpenMP
*   Tâche Slurm MPI/OpenMP hybride
*   Tâche Slurm Python
*   Tâche Slurm R
*   Tâche Slurm VASP

## Suivi des tâches

Pour obtenir un aperçu de toutes vos tâches en file d'attente, vous pouvez utiliser l'interface de suivi des tâches. Naviguez vers l'onglet **Tâches** et sélectionnez **Tâches actives** (`Active Jobs`). Vous pouvez filtrer les tâches en utilisant la boîte de texte **Filtre** en haut à droite. Les colonnes peuvent également être triées en cliquant sur les en-têtes de colonne, par exemple vous pouvez trier par statut de tâche (en cours d'exécution, terminée, échouée, etc.). Cliquer sur `>` à gauche d'une tâche vous montrera plus de détails sur celle-ci, comme l'heure de début/fin, la liste des nœuds et le compte facturé, etc. Vous voudrez peut-être aussi afficher toutes les tâches en file d'attente, vous pouvez le faire en cliquant sur le menu déroulant en haut à droite et en sélectionnant **Toutes les tâches** (`All Jobs`). Une vue plus détaillée de vos tâches peut toujours être trouvée en utilisant le [portail myscinet](https://my.scinet.utoronto.ca).

### Applications interactives

Open OnDemand propose également des applications interactives qui peuvent être exécutées directement depuis votre navigateur web. Pour accéder aux applications, naviguez vers l'onglet **Applications interactives** (`Interactive Apps`) et sélectionnez l'application que vous souhaitez exécuter dans le menu déroulant. Cela vous mènera ensuite à la page de soumission de tâche où vous pourrez choisir des paramètres de tâche tels que :

*   Durée de la tâche en heures
*   Nombre de cœurs
*   Quantité de mémoire à allouer (Go)
*   Ressources GPU (**Note** : Seul le profil **h100_1.10** [MIG](https://docs.alliancecan.ca/wiki/Multi-Instance_GPU) est actuellement disponible, il fournit 10 Go de mémoire et 1/8 des ressources de calcul d'un GPU NVIDIA H100 complet.)
*   M'avertir par courriel lorsque la tâche démarre

Lorsque vous avez choisi vos paramètres de tâche, cliquez sur le bouton **Lancer** (`Launch`) pour soumettre votre tâche à la file d'attente. Vous serez dirigé vers la page **Mes sessions interactives** (`My Interactive Sessions`) où vous pourrez voir le statut de votre tâche, c'est-à-dire en file d'attente, en cours d'exécution ou terminée. Une fois que la tâche a été assignée à un nœud et est en cours d'exécution, vous pouvez cliquer sur le bouton **Se connecter à...** (`Connect to ...`) pour lancer l'application. L'application s'ouvrira dans un nouvel onglet de votre navigateur, et vous pourrez interagir avec elle comme si elle s'exécutait localement.

Si vous souhaitez un accès terminal au nœud où l'application est en cours d'exécution, pour surveiller les performances par exemple, vous pouvez cliquer sur le bouton à côté de **Hôte** (`Host`) commençant par `>_`. Ceci ouvrira une fenêtre de terminal dans votre navigateur où vous pourrez exécuter des commandes directement sur le nœud.

Si pour une raison quelconque vous souhaitez annuler la tâche, vous pouvez le faire en cliquant sur le bouton rouge **Supprimer** (`Delete`) dans le panneau de tâche de la page **Mes sessions interactives**.

### Applications installées

Les applications suivantes sont prises en charge :

*   [Jupyter Lab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Trillium Desktop
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [SAS](https://www.sas.com/en_ca/home.html)<sup>4</sup>
*   [Stata](https://www.stata.com)<sup>4</sup>
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

Pour faire installer d'autres applications, écrivez à [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

## Interfaces graphiques

Si vous souhaitez exécuter un logiciel doté d'une interface graphique utilisateur (IGU) et qui n'est pas encore installé comme application interactive, tel qu'Octave ou Blender, vous pouvez le faire en utilisant l'application **Trillium Desktop**. Cette application fournit un environnement de bureau à distance auquel vous pouvez accéder via votre navigateur web. Dans l'exemple suivant, nous allons exécuter l'IGU d'Octave :

1.  Naviguez vers l'onglet **Applications interactives** et sélectionnez **Trillium Desktop** dans le menu déroulant.
2.  Vous serez dirigé vers la page de soumission de tâche. Choisissez le nombre de cœurs et la quantité de mémoire que vous souhaitez allouer pour votre session en plus de la durée de votre tâche en heures. Cliquez ensuite sur le bouton **Lancer** pour soumettre votre tâche à la file d'attente.
3.  Ceci vous mènera à la page **Mes sessions interactives**. Une fois votre tâche en cours d'exécution, vous avez la possibilité d'améliorer la **Qualité d'image** (`Image Quality`) et la **Compression d'image** (`Image Compression`) de la session de bureau. Selon la vitesse de votre connexion Internet, vous pouvez réduire ces paramètres pour améliorer les performances et la réactivité du bureau. Cliquez sur le bouton **Se connecter au bureau Trillium** (`Connect to Trillium Desktop`) pour lancer l'environnement de bureau à distance dans un nouvel onglet.
4.  Une fois l'environnement de bureau chargé, ouvrez une fenêtre de terminal en utilisant le raccourci du bureau et chargez les modules requis pour Octave :
    ```bash
    module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
    ```
5.  Lancez maintenant l'IGU d'Octave en tapant `octave --gui` dans la fenêtre de terminal.

Vous devriez maintenant voir l'IGU d'Octave apparaître dans l'environnement de bureau à distance. Vous pouvez utiliser cette méthode pour exécuter d'autres applications IGU également, assurez-vous simplement de charger les modules appropriés avant de lancer l'application. Les applications peuvent avoir différentes façons de lancer leur IGU, veuillez donc vous référer à la documentation de l'application pour plus d'informations. Vous pouvez voir la liste des binaires installés pour une application donnée en consultant sa variable d'environnement, par exemple exécutez `ls $EBROOTOCTAVE/bin` pour voir la liste des binaires d'Octave.

## Accès via terminal

Parfois, vous préférerez peut-être utiliser un terminal pour interagir avec Trillium, Open OnDemand fournit un terminal basé sur le web que vous pouvez utiliser pour accéder à l'interface de ligne de commande. Pour accéder au terminal, naviguez vers l'onglet **Grappes** (`Clusters`) et sélectionnez **Accès Shell Trillium** (`Trillium Shell Access`). Ceci ouvrira un nouvel onglet dans votre navigateur avec une fenêtre de terminal où vous pourrez exécuter des commandes comme vous le feriez dans une session de terminal ordinaire.

## Modules logiciels

Trillium dispose d'une grande variété de logiciels accessibles via des modules. Ils peuvent être chargés dans vos sessions interactives, votre terminal ou vos scripts de tâche dans Open Composer. Vous pouvez consulter les modules disponibles et leurs versions en utilisant l'application **Navigateur de modules** (`Module Browser`), accessible depuis l'onglet **Grappes** dans la barre de navigation. Le navigateur de modules fournit également une commande que vous pouvez exécuter dans le terminal pour charger un module particulier, ce qui peut être utile lors de la rédaction de scripts de tâche par exemple.

## Débogage

Si vous rencontrez des erreurs lors de l'utilisation d'une tâche interactive Open OnDemand, vous pouvez consulter les journaux pour plus d'informations. Pour accéder aux journaux, naviguez vers l'onglet **Mes sessions interactives** et trouvez votre session active. Cliquez sur le lien `output.log` pour ouvrir un onglet séparé qui affiche la sortie de votre tâche. Ce fichier contient la sortie standard et les messages d'erreur générés par la tâche, ce qui peut vous aider à identifier tout problème survenu pendant la session. Lorsque vous soumettez un billet au support SciNet, veuillez inclure le fichier `output.log`, votre **ID de session** (`Session ID`), qui est affiché comme une longue chaîne de caractères, par exemple `8feb45fa-bc65-4846-8398-2a73c1bf8e5a`, et toute autre information pertinente pour nous aider à vous assister plus efficacement.

## Comparaison avec Jupyter Hub

| Fonctionnalité              | Jupyter Hub (retiré du service)             | Open OnDemand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------------- | :------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentification            | mot de passe                                | mot de passe + MFA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Première installation       | 2017                                        | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dernière mise à jour        | 2021                                        | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Prend en charge           | Jupyter Notebook, JupyterLab (R, Python, Julia) | Jupyter Notebook, JupyterLab (R, Python), Rstudio, VSCode, Desktop, SAS<sup>4</sup>, Stata<sup>4</sup>, ParaView, Forge DDT/MAP, MATLAB                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Démarrer et continuer plus tard | Oui                                         | Oui<sup>1</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Terminal de commande        | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Gestion des fichiers        | Oui (limité)                                | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Suivi des tâches           | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Soumission des tâches       | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Limite de cœurs            | 8 cœurs<sup>2</sup>                           | 20 cœurs (8 pour la mémoire haute performance)<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Limite de mémoire           | 48 Go<sup>2</sup>                             | 85 Go (500 Go pour la mémoire haute performance)<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Limites de temps            | 3 jours<sup>2</sup>                           | 3 jours<sup>3</sup>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Système d'exploitation      | CentOS 7                                    | RockyLinux 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pile logicielle             | NiaEnv, CCEnv                               | CCEnv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Alertes de problèmes système | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Alertes de quota utilisateur | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Journaux d'erreurs         | Non                                         | Oui                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Matériel                    | 1 x CPU avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 1 To de RAM | 62 x CPU avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 180 Go de RAM (par défaut)<br>3 x CPU avec 40 cœurs Intel "CascadeLake" à 2,5 GHz, 1 To de RAM (mémoire haute performance)<br>4 x GPU NVIDIA H100 de 80 Go, avec un CPU AMD EPYC 9654 à 96 cœurs à 2,4 GHz, 810 Go de RAM |

<sup>1</sup> À l'intérieur des limites demandées.

<sup>2</sup> Parce que les limites pour JupyterHub n'ont pas été implémentées très strictement, elles peuvent temporairement être dépassées.

<sup>3</sup> Demander les limites avant de lancer une application.

<sup>4</sup> Vous devez détenir une licence.