---
title: "Trillium Open OnDemand Quickstart/fr"
slug: "trillium_open_ondemand_quickstart"
lang: "fr"

source_wiki_title: "Trillium Open OnDemand Quickstart/fr"
source_hash: "0157b79150638af43254db6f20c16aa2"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T23:03:15.882912+00:00"

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

Cette page décrit le service Open OnDemand sur Trillium. Pour l'information générale sur les instances Open OnDemand sur nos grappes, voir [Open OnDemand](open_ondemand.md).

## Porter un environnement virtuel sur Open OnDemand

!!! warning "Important"
    **En raison du changement de système d’exploitation et de pile logicielle, vos noyaux d’environnement virtuel Python existants risquent de ne pas fonctionner immédiatement sur le site OnDemand. Vous devriez pouvoir activer vos environnements Python dans un terminal Trillium (voir [Accès via terminal](#accès-via-terminal) ci-dessous), avec tous les modules Trillium requis chargés, puis exécuter la commande `venv2jup` pour les rendre fonctionnels. Pour toutes les instructions, voir [Configurer JupyterLab](#configurer-jupyterlab).**

## Introduction

Ce guide décrit les étapes de base pour démarrer avec le portail Open OnDemand de SciNet.

Open OnDemand (OOD) est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources informatiques, telles que JupyterLab, R Studio et Visual Studio Code. Elle vous permet d'interagir avec Trillium via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information, consultez [https://openondemand.org](https://openondemand.org).

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et allez à la page https://ondemand.scinet.utoronto.ca. Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou YubiKey. La connexion étant établie, le tableau de bord Open OnDemand sera affiché. Vous pourrez alors accéder aux différents outils et applications disponibles.

*   [Tableau de bord, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=fmks5--qaAfm6Zat&t=1316)

## Gestion des fichiers

La plateforme Open OnDemand propose un navigateur qui permet de gérer vos fichiers et répertoires dans le système de fichiers. Pour y accéder, cliquez sur l'onglet **Fichiers** et sélectionnez le répertoire à gérer dans le menu déroulant (`HOME`, `SCRATCH` ou `PROJECT`). Vous pourrez alors :

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et répertoires
*   Supprimer des fichiers et répertoires
*   Modifier des fichiers existants

Vous pouvez aussi faire afficher les quotas de stockage en cliquant sur le lien **Quotas de stockage** sous l'onglet **Fichiers**.

### Téléverser des fichiers

La taille maximale des fichiers que vous pouvez téléverser est présentement de 10Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez [Globus](../getting-started/globus.md). Un bouton Globus se trouve en haut à droite de l'interface. Cliquez sur ce bouton pour faire afficher l'interface web de Globus où vous pourrez vous connecter avec votre nom d'utilisateur et votre mot de passe pour votre compte. Le chemin d'accès affiché dans le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

*   [Navigateur, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=e6Z2PvHRsCVmTKAQ&t=1510)

## Applications interactives

Open OnDemand offre aussi des applications interactives exécutables directement depuis votre navigateur web. Sous l'onglet **Applications interactives**, sélectionnez l'application voulue dans le menu déroulant. Ceci affiche la page de soumission des tâches, où vous pouvez choisir les paramètres de votre tâche, par exemple :

*   durée de la tâche (en heures)
*   nombre de cœurs demandé
*   quantité de mémoire allouée (en Go)
*   ressources GPU (Le seul [profil MIG](../programming/multi-instance_gpu.md) disponible présentement est **h100_1.10** qui offre 10Go de mémoire et 1/8^e^ de la puissance d'un GPU NVIDIA H100 entier.)
    [Demander un GPU, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=64jipPoV-5ZzQpky&t=3025)
*   courriel indiquant le début de la tâche

Après avoir sélectionné les paramètres de votre tâche, cliquez sur le bouton **Lancer** pour l'ajouter à la file d'attente. La page **Mes sessions interactives** sera affichée où vous pouvez consulter l'état de votre tâche (en file d'attente, en cours d'exécution ou terminée). Une fois la tâche affectée à un nœud et en cours d'exécution, cliquez sur le bouton **Se connecter à...** pour lancer l'application. Celle-ci s'ouvre dans un nouvel onglet où vous pouvez travailler avec la tâche comme si elle était exécutée localement.

Pour accéder au terminal du nœud sur lequel l'application s'exécute, par exemple pour en surveiller les performances, cliquez sur le bouton situé à côté de `Host` commençant par `>_`. Une fenêtre de terminal s'ouvrira alors dans votre navigateur où vous pouvez exécuter directement des commandes sur le nœud.

Si vous souhaitez mettre fin à la tâche pour une quelconque raison, vous pouvez le faire en cliquant sur le bouton rouge **Annuler** dans le panneau de la tâche, sur la page **Mes sessions interactives**.

*   [Applications interactives, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=9Fapd_d6jiNT6QqA&t=2118)

### Applications installées

Les applications suivantes sont prises en charge :

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

*   [JupyterLab, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=Xxvu96XYVMNHocq8&t=2469)
*   [Bureau, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)

### Configurer JupyterLab

Il y a deux façons d'exécuter JupyterLab.

**Option 1** : Utiliser Python 3 par défaut (ipykernel)

Le noyau par défaut inclut les paquets Python préinstallés suivants : numpy, redis, jwcrypto, jupyterlmod, matplotlib, h5py, cython, pandas, ipympl, jupyterlab_favorites et jupyter-resource-usage. Vous pouvez démarrer une session JupyterLab avec ce noyau et utiliser ces paquets sans configuration supplémentaire. Si vous souhaitez utiliser d'autres paquets, vous pouvez charger les modules requis avant de démarrer votre noyau via l'onglet **Modules logiciels**, situé à l'extrême gauche de l'interface. Si votre noyau est déjà en cours d'exécution, vous devrez l'arrêter puis le redémarrer pour que les modifications soient prises en compte. Pour ce faire, cliquez sur `Kernel > Shut Down Kernel` dans le menu du haut.

Pour utiliser un paquet Python qui n'est pas installé par défaut ou qui n'est pas inclus en tant que module logiciel, vous pouvez créer un environnement virtuel Python avec les paquets requis installés et l'exécuter en tant que noyau JupyterLab (voir l'option 2 ci-dessous).

**Option 2** : Travailler dans un [environnement virtuel Python](../software/python.md) que vous avez créé.

À partir d'un terminal (lancé soit dans JupyterLab, soit en cliquant sur `Cluster→ Accès à l'interface Trillium` dans la barre de navigation OnDemand), vous pouvez créer votre propre environnement virtuel Python et installer les paquets nécessaires. Par exemple, pour créer un environnement virtuel nommé `myenv` et installer le paquet numpy, exécutez :

```bash
[username@tri-login01]$ module load python/3.14.2
[username@tri-login01]$ virtualenv --no-download ~/.virtualenvs/myenv
[username@tri-login01]$ source ~/.virtualenvs/myenv/bin/activate
```

```bash
(myenv)[username@tri-login01]$ pip install numpy
```

Pour convertir cela en noyau JupyterLab, exécutez la commande suivante à partir de l'environnement virtuel activé.

```bash
(myenv)[username@tri-login01]$ venv2jup
```

Au lancement d'une session JupyterLab, votre environnement virtuel `myenv` apparaîtra comme option du noyau.

## Interfaces graphiques

Si vous souhaitez exécuter un logiciel doté d'une interface graphique et qui n'est pas installé comme application interactive, par exemple Octave, vous pouvez utiliser l'application **Bureau Trillium**. Cette application fournit un environnement de bureau à distance accessible via votre navigateur web. Dans l'exemple suivant, nous exécutons l'interface graphique d'Octave.

1.  Sous l'onglet **Applications interactives**, sélectionnez **Bureau Trillium** dans le menu déroulant.
2.  Dans la page de soumission des tâches qui s'affiche, choisissez le nombre de cœurs et la quantité de mémoire à allouer à votre session, ainsi que la durée de la tâche (en heures). Cliquez ensuite sur le bouton **Lancer** pour ajouter votre tâche à la file d'attente.
3.  La page **Mes sessions interactives** sera affichée. Une fois votre tâche en cours d'exécution, vous pourrez améliorer la qualité et la compression de l'image de la session de bureau. Dépendant de la vitesse de votre connexion Internet, vous pouvez réduire ces paramètres pour améliorer les performances et la réactivité du bureau. Cliquez sur le bouton **Se connecter au bureau Trillium** pour lancer l'environnement de bureau distant dans un nouvel onglet.
    *   Une fois que l'environnement de bureau est chargé, ouvrez une fenêtre de terminal à l'aide du raccourci sur le bureau et chargez les modules nécessaires à Octave.
        ```bash
        $ module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 octave/7.2.0
        ```
    *   Lancez ensuite l'interface graphique d'Octave en saisissant `octave --gui` dans la fenêtre de terminal.

L'interface graphique d'Octave devrait maintenant apparaître dans l'environnement de bureau distant. Vous pouvez utiliser cette méthode pour exécuter d'autres applications graphiques; assurez-vous simplement de charger les modules appropriés avant de lancer l'application. Les applications peuvent avoir différentes méthodes pour lancer leur interface graphique; veuillez consulter la documentation pour chacune des applications. Pour voir la liste des binaires installés pour une application particulière en consultant sa variable d'environnement, ici pour la liste des binaires Octave, lancez `ls $EBROOTOCTAVE/bin`.

*   [Interface Octave, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)

## Soumettre une tâche

Open OnDemand offre également une interface qui permet de soumettre des tâches en lots à Trillium. Ceci peut s'avérer utile lorsque vous avez besoin de plus de ressources que celles fournies par les tâches interactives, par exemple un accès exclusif à 192 cœurs et 755Go de mémoire sur un nœud de calcul de Trillium.

L'application [Open Composer](https://github.com/RIKEN-RCCS/OpenComposer) offre plusieurs scripts modèles que vous pouvez soumettre directement à l'ordonnanceur. Elle offre aussi sous l'onglet **Historique**, une interface pour faire le suivi des tâches que vous avez soumises.
Vous avez accès à Open Composer sous le menu déroulant **Tâches** ou en cliquant sur un modèle de script.

Une fois le modèle sélectionné, la page de soumission de tâche est affichée. Celle-ci est en deux parties : les paramètres de la tâche à gauche et le script à droite. Les paramètres vous permettent de contrôler les ressources utilisées, comme le nombre de nœuds, le nombre de tâches par nœud, la durée d'exécution et le nom du fichier de sortie. Le script affiche le texte qui sera soumis à l'ordonnanceur. Toute modification apportée aux paramètres se reflète automatiquement dans le script. Vous pouvez également modifier le script directement.

Les champs dans le haut de la page servent à modifier la manière dont la tâche sera soumise.

*   `Script Location` indique le répertoire dans lequel le script sera sauvegardé et la tâche sera exécutée.
*   `Script Name` indique le nom du fichier qui contient le script pour la tâche.
*   `Job Name` indique le nom de la tâche tel qu'il sera dans la file.
*   `Cluster` permet de choisir la grappe sur laquelle la tâche sera soumise, par exemple Trillium (par défaut) ou Trillium-GPU. En sélectionnant Trillium-GPU, un paramètre s'ajoutera pour demander des ressources GPU.

Une fois que votre script est bien défini, cliquez sur le bouton **Soumettre** pour soumettre la tâche à l'ordonnanceur et enregistrer le script dans l'**Emplacement du script**. Si tout se passe bien, un message de confirmation sera affiché, avec l'identifiant de la tâche.

Remarque : Les scripts modèles sont des exemples de base que vous devrez adapter à vos besoins spécifiques, notamment en chargeant les modules requis et en spécifiant les fichiers d’entrée/sortie. Le script doit également respecter les limites imposées par l'ordonnanceur Slurm. Voir [Restrictions particulières à Trillium](../clusters/trillium_quickstart.md#restrictions-particulières-à-trillium) pour plus d’information sur la rédaction des scripts.

Pour des instructions détaillées sur Open Composer, voir [le manuel d'utilisation](https://riken-rccs.github.io/OpenComposer/docs/manual.html).

*   [Open Composer, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=r5vcEw-lgM7xSJ6_&t=4263)

### Suivi des tâches dans Open Composer

Sous l'onglet **Historique** se trouve la liste de toutes vos tâches, avec leur état (en attente, en cours d'exécution, terminée, échec). Pour raffiner une recherche, utilisez le champ **Filtre** ou cliquez dans les cases à cocher ci-dessous. En cliquant sur les différentes colonnes, des informations spécifiques à chaque tâche seront affichées.

*   `Job ID` affiche la tâche dans [my.SciNet](https://my.scinet.utoronto.ca/) avec les statistiques de performance et des détails au sujet de Slurm. Le message `Not found or not permitted` paraît si la tâche est encore en attente ou si elle a été supprimée.
*   `Application` affiche une fenêtre pour modifier le script du modèle utilisé.
*   `Script Location` ouvre une fenêtre de l'endroit où se trouve le script. Cliquez sur la petite icône de terminal pour ouvrir un terminal au même endroit.
*   `Script Name` affiche le script soumis à l'ordonnanceur.

Pour modifier ou soumettre de nouveau une tâche déjà soumise, cliquez sur le script dans la colonne `Script Name` puis sur **Charger les paramètres**. La page de soumission de la tâche sera affichée et vous pourrez faire les modifications voulues.

### Applications prises en charge

Présentement, Open Composer prend en charge les applications suivantes pour l'ordonnanceur Slurm :

*   [MPI](../software/mpi.md)
*   [OpenMP](../programming/openmp.md)
*   Hybride MPI/OpenMP
*   [Python](../software/python.md)
*   [R](../software/r.md)
*   [VASP](../software/vasp.md)

## Suivi des tâches

Pour obtenir un aperçu de toutes vos tâches en attente, utilisez l'interface de suivi des tâches. Sous l'onglet **Tâches**, sélectionnez **Tâches actives**. Vous pouvez utiliser le champ de texte **Filtre** en haut à droite. Pour trier une colonne, cliquez sur son en-tête, par exemple par statut (en cours, terminée, échec, etc.). Cliquez sur le bouton à gauche d'une tâche pour obtenir des informations supplémentaires, telles que l'heure de début et de fin, la liste des nœuds et le compte auquel se rapporte l'utilisation des ressources. Pour afficher toutes les tâches en attente, cliquez sur le menu déroulant en haut à droite et sélectionnez **Toutes les tâches**. Une vue plus détaillée de vos tâches est disponible sur [le portail myscinet](https://my.scinet.utoronto.ca).

*   [Tâches actives, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=rf_JMYBFz9ytpkR_&t=1818)

## Accès via terminal

Si vous préférez utiliser un terminal pour interagir avec la grappe, Open OnDemand met à votre disposition un terminal web pour accéder à l'interface ligne de commande. Pour ce faire, rendez-vous dans l'onglet **Grappes** et sélectionnez **Accès shell Trillium**. Une nouvelle fenêtre de terminal s'ouvrira alors dans votre navigateur, où vous pouvez exécuter des commandes comme dans une session de terminal classique.

*   [Terminal, tutoriel vidéo de SciNet (en anglais)](https://youtu.be/XRozBBKwA8c?si=REh17mvUn8q50iys&t=1904)

## Modules logiciels

Trillium offre plusieurs logiciels accessibles via des modules. Ces modules peuvent être chargés dans vos sessions interactives, votre terminal ou vos scripts de tâches dans Open Composer. Vous pouvez consulter les modules disponibles et leurs versions grâce à l'application **Navigateur de modules**, sous l'onglet **Grappes** de la barre de navigation. Le navigateur de modules fournit également une commande à exécuter dans le terminal pour charger un module spécifique, ce qui peut s'avérer utile lors de la rédaction de scripts de tâches.

## Débogage

Si vous rencontrez des erreurs lors de l'utilisation d'une tâche interactive, vous pouvez consulter les fichiers de journalisation. Pour y accéder, rendez-vous sous l'onglet **Mes sessions interactives** et sélectionnez votre session active. Cliquez sur le lien `output.log` pour ouvrir un nouvel onglet affichant la sortie de votre tâche. Ce fichier contient la sortie standard et les messages d'erreur générés par la tâche, ce qui peut vous aider à identifier les problèmes qui seraient survenus pendant la session. Si vous avez besoin d'assistance, un bouton pour soumettre une demande de soutien se trouve dans la carte de la session. Veuillez inclure le fichier `output.log` et toute autre information pertinente afin de nous permettre de vous aider plus efficacement.

## Dépannage

### État de session indéterminé, erreur "Votre session est dans un mauvais état."

Cette erreur survient quand le processus de calcul perd la trace de la session Open OnDemand, par exemple pendant des travaux de maintenance lorsque les nœuds de calcul et l'ordonnanceur sont relancés.

**Solution**

Cette procédure peut échouer si l'ordonnanceur n'est pas en fonction.

1.  Cliquez sur le bouton **Annuler**.
2.  Consultez le fichier *output.log* pour lire les messages d'erreur ou les avis de maintenance, s'il y a lieu.
3.  Soumettez votre session de nouveau.

Si ceci ne fonctionne pas, cliquez sur le bouton **Soumettre une demande de soutien** et joignez le fichier *output.log*; notre équipe technique examinera le problème.

## Tutoriels

Vidéos de SciNet (en anglais)
*   [Tableau de bord](https://youtu.be/XRozBBKwA8c?si=fmks5--qaAfm6Zat&t=1316)
*   [Navigateur](https://youtu.be/XRozBBKwA8c?si=e6Z2PvHRsCVmTKAQ&t=1510)
*   [Tâches interactives](https://youtu.be/XRozBBKwA8c?si=9Fapd_d6jiNT6QqA&t=2118)
*   [JupyterLab](https://youtu.be/XRozBBKwA8c?si=Xxvu96XYVMNHocq8&t=2469)
*   [Bureau](https://youtu.be/XRozBBKwA8c?si=qvh56f5fvJpp5jrg&t=3117)
*   [Soumettre des tâches avec Open Composer](https://youtu.be/XRozBBKwA8c?si=r5vcEw-lgM7xSJ6_&t=4263)
*   [Terminal](https://youtu.be/XRozBBKwA8c?si=REh17mvUn8q50iys&t=1904)
*   [Suivi des tâches](https://youtu.be/XRozBBKwA8c?si=rf_JMYBFz9ytpkR_&t=1818)

## Comparaison avec JupyterHub

| Fonctionnalité | JupyterHub (hors service définitivement) | Open OnDemand |
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
| matériel | 1 x CPU de 40 Intel "CascadeLake" cœurs à 2.5 GHz, 1To de RAM | 62 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 180Go de RAM (par défaut)<br>3 x CPU de 40 cœurs Intel CascadeLake à 2.5 GHz, 1To de RAM (mémoire forte)<br>4 x GPU NVIDIA H100 80GB<br>1 x CPU9 de 6 cœurs AMD EPYC 9654 CPU à 2.4 GHz, 810Go de RAM |

^1^ À l'intérieur des limites demandées.

^2^ Parce que les limites pour JupyterHub n'ont pas été implémentées très strictement, elles peuvent temporairement être surpassées.

^3^ Demander les limites avant de lancer une application.

^4^ Vous devez détenir une licence.