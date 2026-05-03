---
title: "Trillium Open OnDemand Quickstart/fr"
slug: "trillium_open_ondemand_quickstart"
lang: "fr"

source_wiki_title: "Trillium Open OnDemand Quickstart/fr"
source_hash: "8dc0bdaedf2e97b0900e75959a7df13d"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:49:19.579877+00:00"

tags:
  []

keywords:
  - "Trillium"
  - "Débogage"
  - "Open OnDemand"
  - "Globus"
  - "statistiques de performance"
  - "tâche"
  - "Interfaces graphiques"
  - "variable d'environnement"
  - "notification des quotas"
  - "fenêtre de terminal"
  - "lancer une application"
  - "exécuter des commandes"
  - "journalisation des erreurs"
  - "Open Composer"
  - "My Interactive Sessions"
  - "Octave"
  - "Suivi des tâches"
  - "script du modèle"
  - "CPU Intel CascadeLake"
  - "limites demandées"
  - "matériel"
  - "ordonnanceur"
  - "bouton Globus"
  - "se connecter"
  - "environnement virtuel Python"
  - "soumission de tâches"
  - "accès via terminal"
  - "Job ID"
  - "Modules logiciels"
  - "nœud"
  - "Slurm"
  - "gestion des fichiers"
  - "Sessions interactives"
  - "JupyterHub"
  - "suivi des tâches"
  - "chemin d'accès"
  - "GPU NVIDIA H100"
  - "Applications installées"
  - "navigateur Open OnDemand"
  - "Trillium Desktop"
  - "Accès via terminal"
  - "mettre fin à la tâche"
  - "Applications interactives"
  - "binaires"
  - "limites"
  - "Ordonnanceur Slurm"
  - "licence"
  - "interface web de Globus"

questions:
  - "Comment doit-on procéder pour rendre fonctionnels les noyaux d'environnement virtuel Python existants sur le site OnDemand de Trillium ?"
  - "Quelles sont les étapes et les méthodes d'authentification requises pour se connecter au portail Open OnDemand ?"
  - "Quelles sont les limites de taille pour le téléversement de fichiers via le navigateur Open OnDemand et quelle alternative est recommandée pour les fichiers plus volumineux ?"
  - "Comment fonctionne l'interface d'Open Composer pour configurer et soumettre une tâche en lots sur la grappe Trillium ?"
  - "Quelles adaptations spécifiques l'utilisateur doit-il apporter aux scripts modèles avant de les soumettre à l'ordonnanceur ?"
  - "Comment peut-on effectuer le suivi de l'état des tâches soumises et consulter leurs statistiques de performance ?"
  - "Où se trouve le bouton permettant d'accéder à l'interface web de Globus ?"
  - "Quelles informations d'identification sont requises pour se connecter à son compte Globus ?"
  - "Quel sera le chemin d'accès affiché dans Globus par rapport à celui du navigateur Open OnDemand ?"
  - "Que se passe-t-il lorsque l'utilisateur clique sur les différentes colonnes de l'interface ?"
  - "Dans quelles situations spécifiques le message \"Not found or not permitted\" apparaît-il ?"
  - "Quelle est la fonction de l'option \"Application\" concernant le script du modèle ?"
  - "Quelles sont les étapes pour modifier un script déjà soumis et quelles applications sont actuellement prises en charge par Open Composer ?"
  - "Comment peut-on utiliser l'interface de suivi pour consulter l'état, filtrer et obtenir des informations détaillées sur les tâches actives ou en attente ?"
  - "Quelle est la procédure pour configurer les paramètres, lancer, accéder au terminal et mettre fin à une application interactive depuis le navigateur web ?"
  - "Quelles sont les applications interactives déjà installées et comment faire une demande pour en ajouter de nouvelles ?"
  - "Comment utiliser l'application Trillium Desktop pour exécuter l'interface graphique d'un logiciel non listé, comme Octave ou Blender ?"
  - "Quelle est la méthode pour charger les modules requis et trouver les exécutables d'une application spécifique via le terminal dans l'environnement de bureau distant ?"
  - "Comment ouvrir une fenêtre de terminal dans le navigateur pour exécuter des commandes sur le nœud ?"
  - "Comment identifier visuellement le bouton situé à côté de \"Host\" permettant de lancer ce terminal ?"
  - "Quelle est la procédure exacte pour mettre fin à une tâche depuis la page \"My Interactive Sessions\" ?"
  - "Quelle commande doit-on lancer pour consulter la liste des binaires d'Octave via sa variable d'environnement ?"
  - "Dans quel environnement de bureau l'interface graphique d'Octave est-elle présentée selon la figure 11 ?"
  - "Quel mode d'accès alternatif au système est introduit à la fin du texte ?"
  - "Comment accéder au terminal web et rechercher les modules logiciels disponibles sur la grappe Trillium via Open OnDemand ?"
  - "Quelle est la procédure à suivre pour consulter les journaux d'erreurs d'une tâche interactive et demander de l'assistance en cas de problème ?"
  - "Quelles sont les principales améliorations et différences techniques offertes par Open OnDemand comparativement à l'ancien système JupyterHub ?"
  - "Comment les deux systèmes se différencient-ils en matière de notification des quotas utilisateurs et de journalisation des erreurs ?"
  - "Quelle est la configuration matérielle exacte du premier environnement décrit ?"
  - "Quelles sont les différentes options de processeurs (CPU) et de cartes graphiques (GPU) proposées dans le second environnement ?"
  - "Pourquoi les limites d'utilisation de JupyterHub peuvent-elles être temporairement dépassées ?"
  - "Quelle action doit être effectuée concernant les limites avant de lancer une application ?"
  - "Quelle condition préalable liée à la licence est exigée des utilisateurs ?"

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

!!! important "Important"
    En raison du changement de système d’exploitation et de pile logicielle, vos noyaux d’environnement virtuel Python existants risquent de ne pas fonctionner immédiatement sur le site OnDemand. Vous devriez pouvoir activer vos environnements Python dans un terminal Trillium (voir [Accès via terminal](#accès-via-terminal) ci-dessous), avec tous les modules Trillium requis chargés, puis exécuter la commande **`venv2jup`** pour les rendre fonctionnels.

## Introduction

Ce guide décrit les étapes de base pour démarrer avec le portail Open OnDemand de SciNet.

Open OnDemand (OOD) est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources informatiques, telles que JupyterLab, R Studio et Visual Studio Code. Elle vous permet d'interagir avec Trillium via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information, consultez [https://openondemand.org](https://openondemand.org).

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et allez à la page https://ondemand.scinet.utoronto.ca. Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou YubiKey. La connexion étant établie, le tableau de bord Open OnDemand sera affiché. Vous pourrez alors accéder aux différents outils et applications disponibles.

## Gestion des fichiers

La plateforme Open OnDemand propose un navigateur qui permet de gérer vos fichiers et répertoires dans le système de fichiers. Pour y accéder, cliquez sur l'onglet *Fichiers* et sélectionnez le répertoire à gérer dans le menu déroulant (`HOME`, `SCRATCH` ou `PROJECT`). Le navigateur sera affiché et vous pourrez :

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et répertoires
*   Supprimer des fichiers et répertoires
*   Modifier des fichiers existants

Vous pouvez aussi faire afficher les quotas de stockage en cliquant sur le lien *Quotas de stockage* sous l'onglet *Fichiers*.

### Téléverser des fichiers

La taille maximale des fichiers que vous pouvez téléverser est présentement de 10Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez [Globus](../getting-started/globus.md). Un bouton Globus se trouve en haut à droite dans l'interface. Cliquez sur ce bouton pour faire afficher l'interface web de Globus où vous pourrez vous connecter avec votre nom d'utilisateur et votre mot de passe pour votre compte. Le chemin d'accès affiché dans le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

## Soumettre une tâche

Open OnDemand offre également une interface qui permet de soumettre des tâches en lots à Trillium. Ceci peut s'avérer utile lorsque vous avez besoin de plus de ressources que celles fournies par les tâches interactives, par exemple un accès exclusif à 192 cœurs et 755Go de mémoire sur un nœud de calcul de Trillium.

L'application [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) offre plusieurs scripts modèles que vous pouvez soumettre directement à l'ordonnanceur. Elle offre aussi sous l'onglet *Historique*, une interface pour faire le suivi des tâches que vous avez soumises.
Vous avez accès à Open Composer sous le menu déroulant *Tâches* ou en cliquant sur un modèle de script.

Une fois le modèle sélectionné, la page de soumission de tâche est affichée. Celle-ci est en deux parties : les paramètres de la tâche à gauche et le script à droite. Les paramètres vous permettent de contrôler les ressources utilisées, comme le nombre de nœuds, le nombre de tâches par nœud, la durée d'exécution et le nom du fichier de sortie. Le script affiche le texte qui sera soumis à l'ordonnanceur. Toute modification apportée aux paramètres se reflète automatiquement dans le script. Vous pouvez également modifier le script directement.

Les champs dans le haut de la page servent à modifier la manière dont la tâche sera soumise.

*   *Emplacement du script* indique le répertoire dans lequel le script sera sauvegardé et la tâche sera exécutée.
*   *Nom du script* indique le nom du fichier qui contient le script pour la tâche.
*   *Nom de la tâche* indique le nom de la tâche tel qu'il sera dans la file d'attente.
*   *Grappe* permet de choisir la grappe sur laquelle la tâche sera soumise, par exemple Trillium (par défaut) ou Trillium-GPU. En sélectionnant Trillium-GPU, un paramètre s'ajoutera pour demander des ressources GPU.

Une fois que votre script est bien défini, cliquez sur le bouton *Soumettre* pour soumettre la tâche à l'ordonnanceur et enregistrer le script dans *Emplacement du script*. Si tout se passe bien, un message de confirmation sera affiché, avec l'identifiant de la tâche.

Remarque : Les scripts modèles sont des exemples de base que vous devrez adapter à vos besoins spécifiques, notamment en chargeant les modules requis et en spécifiant les fichiers d’entrée/sortie. Le script doit également respecter les limites imposées par l'ordonnanceur Slurm. Voir [Restrictions particulières à Trillium](../clusters/trillium_quickstart.md#restrictions-particulières-à-trillium) pour plus d’information sur la rédaction des scripts.

### Suivi des tâches dans Open Composer

Sous l'onglet *Historique* se trouve la liste de toutes vos tâches, avec leur état (en attente, en cours d'exécution, terminée, échec). Pour raffiner une recherche, utilisez le champ *Filtre* ou cliquez dans les cases à cocher ci-dessous. En cliquant sur les différentes colonnes, des informations spécifiques à chaque tâche seront affichées.

*   *ID de la tâche* affiche la tâche dans [my.SciNet](https://my.scinet.utoronto.ca/) avec les statistiques de performance et des détails au sujet de Slurm. Le message « Introuvable ou non permis » paraît si la tâche est encore en attente ou si elle a été supprimée.
*   *Application* affiche une fenêtre pour modifier le script du modèle utilisé.
*   *Emplacement du script* ouvre une fenêtre de l'endroit où se trouve le script. Cliquez sur le petit icône de terminal pour ouvrir un terminal au même endroit.
*   *Nom du script* affiche le script soumis à l'ordonnanceur.

Pour modifier ou soumettre de nouveau une tâche déjà soumise, cliquez sur le script dans la colonne *Nom du script* puis sur *Charger les paramètres*. La page de soumission de la tâche sera affichée et vous pourrez faire les modifications voulues.

### Applications prises en charge

Présentement, Open Composer prend en charge les applications suivantes pour l'ordonnanceur Slurm :

*   [MPI](../software/mpi.md)
*   [OpenMP](../programming/openmp.md)
*   Hybrid MPI/OpenMP
*   [Python](../software/python.md)
*   [R](../software/r.md)
*   [VASP](../software/vasp.md)

## Suivi des tâches

Pour obtenir un aperçu de toutes vos tâches en attente, utilisez l'interface de suivi des tâches. Sous l'onglet *Tâches*, sélectionnez *Tâches actives*. Vous pouvez utiliser le champ de texte *Filtre* en haut à droite. Pour trier une colonne, cliquez sur son en-tête, par exemple par statut (en cours, terminée, échec, etc.). Cliquez sur le bouton à gauche d'une tâche pour obtenir des informations supplémentaires, telles que l'heure de début et de fin, la liste des nœuds et le compte auquel se rapporte l'utilisation des ressources. Pour afficher toutes les tâches en attente, cliquez sur le menu déroulant en haut à droite et sélectionnez *Toutes les tâches*. Une vue plus détaillée de vos tâches est disponible sur [le portail mySciNet](https://my.scinet.utoronto.ca).

## Applications interactives

Open OnDemand offre aussi des applications interactives exécutables directement depuis votre navigateur web. Sous l'onglet *Applications interactives*, sélectionnez l'application voulue dans le menu déroulant. Ceci affiche la page de soumission des tâches, où vous pouvez choisir les paramètres de votre tâche, par exemple :

*   durée de la tâche (en heures)
*   nombre de cœurs demandé
*   quantité de mémoire allouée (en Go)
*   ressources GPU ([Le seul profil MIG](../programming/multi-instance_gpu.md) disponible présentement est **h100_1.10** qui offre 10Go de mémoire et 1/8^e^ de la puissance d'un GPU NVIDIA H100 entier.)
*   courriel indiquant le début de la tâche

Après avoir sélectionné les paramètres de votre tâche, cliquez sur le bouton *Lancer* pour l'ajouter à la file d'attente. La page *Mes sessions interactives* sera affichée où vous pouvez consulter l'état de votre tâche (en file d'attente, en cours d'exécution ou terminée). Une fois la tâche affectée à un nœud et en cours d'exécution, cliquez sur le bouton *Se connecter à ...* pour lancer l'application. Celle-ci s'ouvre dans un nouvel onglet où vous pouvez travailler avec la tâche comme si elle était exécutée localement.

Pour accéder au terminal du nœud sur lequel l'application s'exécute, par exemple pour en surveiller les performances, cliquez sur le bouton situé à côté de *Hôte* commençant par `>_`. Une fenêtre de terminal s'ouvrira alors dans votre navigateur où vous pouvez exécuter directement des commandes sur le nœud.

Si vous souhaitez mettre fin à la tâche pour une quelconque raison, vous pouvez le faire en cliquant sur le bouton rouge *Supprimer* dans le panneau de la tâche, sur la page *Mes sessions interactives*.

### Applications installées

Les applications suivantes sont prises en charge :

*   [JupyterLab/Notebook](https://jupyter.org)
*   [Rstudio](https://posit.co/products/open-source/rstudio/?sid=1)
*   [VSCode](https://code.visualstudio.com)
*   Bureau Trillium
*   [ParaView](https://www.paraview.org)
*   [Forge DDT/MAP](https://www.linaroforge.com)
*   [MATLAB](https://www.mathworks.com/products/matlab.html)
*   [Ovito](https://www.ovito.org)
*   [SAS](https://www.sas.com/en_ca/home.html)^4^
*   [Stata](https://www.stata.com)^4^
*   [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer)

Pour faire installer d'autres applications, écrivez à [support@scinet.utoronto.ca](mailto:support@scinet.utoronto.ca).

## Interfaces graphiques

Si vous souhaitez exécuter un logiciel doté d'une interface graphique et qui n'est pas installé comme application interactive, par exemple Octave ou Blender, vous pouvez utiliser l'application *Bureau Trillium*. Cette application fournit un environnement de bureau à distance accessible via votre navigateur web. Dans l'exemple suivant, nous exécutons l'interface graphique d'Octave.

1.  Sous l'onglet *Applications interactives*, sélectionnez *Bureau Trillium* dans le menu déroulant.
2.  Dans la page de soumission des tâches qui s'affiche, choisissez le nombre de cœurs et la quantité de mémoire à allouer à votre session, ainsi que la durée de la tâche (en heures). Cliquez ensuite sur le bouton *Lancer* pour ajouter votre tâche à la file d'attente.
3.  La page *Mes sessions interactives* sera affichée. Une fois votre tâche en cours d'exécution, vous pourrez améliorer la qualité et la compression de l'image de la session de bureau. Dépendant de la vitesse de votre connexion Internet, vous pouvez réduire ces paramètres pour améliorer les performances et la réactivité du bureau. Cliquez sur le bouton *Se connecter au Bureau Trillium* pour lancer l'environnement de bureau distant dans un nouvel onglet.
    *   Une fois que l'environnement de bureau est chargé, ouvrez une fenêtre de terminal à l'aide du raccourci sur le bureau et chargez les modules nécessaires à Octave.
        ```bash
        module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
        ```
    *   Lancez ensuite l'interface graphique d'Octave en saisissant `octave --gui` dans la fenêtre de terminal.

L'interface graphique d'Octave devrait maintenant apparaître dans l'environnement de bureau distant. Vous pouvez utiliser cette méthode pour exécuter d'autres applications graphiques; assurez-vous simplement de charger les modules appropriés avant de lancer l'application. Les applications peuvent avoir différentes méthodes pour lancer leur interface graphique; veuillez consulter la documentation pour chacune des applications. Pour voir la liste des binaires installés pour une application particulière en consultant sa variable d'environnement, ici pour la liste des binaires Octave, lancez
`ls $EBROOTOCTAVE/bin`

## Accès via terminal

Si vous préférez utiliser un terminal pour interagir avec la grappe, Open OnDemand met à votre disposition un terminal web pour accéder à l'interface ligne de commande. Pour ce faire, rendez-vous dans l'onglet *Grappes* et sélectionnez *Accès Shell Trillium*. Une nouvelle fenêtre de terminal s'ouvrira alors dans votre navigateur, où vous pouvez exécuter des commandes comme dans une session de terminal classique.

## Modules logiciels

Trillium offre plusieurs logiciels accessibles via des modules. Ces modules peuvent être chargés dans vos sessions interactives, votre terminal ou vos scripts de tâches dans Open Composer. Vous pouvez consulter les modules disponibles et leurs versions grâce à l'application *Navigateur de modules*, sous l'onglet *Grappes* de la barre de navigation. Le navigateur de modules fournit également une commande à exécuter dans le terminal pour charger un module spécifique, ce qui peut s'avérer utile lors de la rédaction de scripts de tâches.

## Débogage

Si vous rencontrez des erreurs lors de l'utilisation d'une tâche interactive, vous pouvez consulter les fichiers de journalisation. Pour y accéder, rendez-vous sous l'onglet *Mes sessions interactives* et sélectionnez votre session active. Cliquez sur le lien `output.log` pour ouvrir un nouvel onglet affichant la sortie de votre tâche. Ce fichier contient la sortie standard et les messages d'erreur générés par la tâche, ce qui peut vous aider à identifier les problèmes qui seraient survenus pendant la session. Si vous avez besoin d'assistance, cliquez sur le bouton de soutien qui se trouve dans la carte de la session. Veuillez inclure le fichier `output.log` et toute autre information pertinente afin de nous permettre de vous aider plus efficacement.

## Comparaison avec JupyterHub

| fonctionnalité | JupyterHub (hors service définitivement) | Open OnDemand |
| :------------- | :--------------------------------------- | :------------ |
| authentification | mot de passe | mot de passe et authentification multifacteur |
| première installation | 2017 | 2025 |
| plus récente mise à jour | 2021 | 2025 |
| supporte | Jupyter Notebook, JupyterLab (R, Python, Julia) | Jupyter Notebook, JupyterLab (R, Python), Rstudio, VSCode, Bureau, SAS^4^, Stata^4^, ParaView, Forge DDT/MAP, MATLAB |
| arrêt et reprise plus tard | oui | oui^1^ |
| terminal de commande | non | oui |
| gestion des fichiers | oui (limitée) | oui |
| suivi des tâches | non | oui |
| soumission des tâches | non | oui |
| maximum de cœurs | 8 cœurs^2^ | 20 cœurs (8 pour mémoire forte)^3^ |
| maximum de mémoire | 48 Go^2^ | 85 Go (500 Go pour mémoire forte)^3^ |
| maximum de durée | 3 jours^2^ | 3 jours^3^ |
| système d'exploitation | CentOS 7 | RockyLinux 9 |
| piles logicielles | NiaEnv, CCEnv | CCEnv |
| notification des problèmes de système | non | oui |
| notification des quotas de l'utilisateur | non | oui |
| journalisation des erreurs | non | oui |
| matériel | 1 x CPU de 40 Intel "CascadeLake" cœurs à 2.5 GHz, 1To de RAM | 62 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 180Go de RAM (par défaut)<br>3 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 1To de RAM (mémoire forte)<br>4 x GPU NVIDIA H100 80GB<br>1x CPU de 6 cœurs AMD EPYC 9654 à 2.4 GHz, 810Go de RAM |

^1^ À l'intérieur des limites demandées.

^2^ Parce que les limites pour JupyterHub n'ont pas été implémentées très strictement, elles peuvent temporairement être surpassées.

^3^ Demander les limites avant de lancer une application.

^4^ Vous devez détenir une licence.