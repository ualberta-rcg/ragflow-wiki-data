---
title: "Open OnDemand/fr"
slug: "open_ondemand"
lang: "fr"

source_wiki_title: "Open OnDemand/fr"
source_hash: "9185ad9d5b6322ab5ddb3c3f4dcbf670"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:40:30.238709+00:00"

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

## Introduction

Nous décrivons ici les étapes de base pour démarrer avec Open OnDemand (OOD) sur nos systèmes.

Open OnDemand est une plateforme web qui donne accès à un large éventail d'applications scientifiques et de ressources de calcul telles que Jupyter Lab, RStudio et VS Code. Elle vous permet d'interagir avec une de nos grappes via un navigateur web, sans avoir à installer de logiciel sur votre ordinateur local. Vous pourrez gérer des fichiers, soumettre et suivre des tâches, et exécuter des applications de manière interactive. Pour plus d'information sur ce projet, voir [https://openondemand.org](https://openondemand.org). Pour la documentation spécifique à chacune des grappes, voir

*   [Trillium : Guide de démarrage Open OnDemand](trillium-open-ondemand-quickstart.md)
*   [Nibi, Accès via Open OnDemand (OOD)](nibi.md#accès-via-open-ondemand-ood)

## Se connecter au portail Open OnDemand

Pour accéder au portail Open OnDemand, ouvrez un navigateur web et sélectionnez l'instance OnDemand, par exemple : [Trillium](https://ondemand.scinet.utoronto.ca), [Vulcan](vulcan.md) ou [Nibi](https://ondemand.sharcnet.ca). Saisissez votre nom d'utilisateur et votre mot de passe avec l'Alliance, puis effectuez l'authentification multifacteur via Duo ou Yubikey. La connexion étant établie, le tableau de bord Open OnDemand sera affiché. Vous pourrez alors accéder aux différents outils et applications disponibles.

## Gestion des fichiers

Un navigateur de fichiers permet de parcourir vos fichiers et répertoires du système de fichiers. Pour y accéder, cliquez sur l'onglet *Files* et sélectionnez le répertoire dans le menu déroulant (HOME, SCRATCH ou PROJECT). Avec l'interface, vous pouvez

*   Naviguer dans vos répertoires
*   Téléverser et télécharger des fichiers
*   Créer des fichiers et des répertoires
*   Supprimer des fichiers et des répertoires
*   Modifier des fichiers existants

### Téléverser des fichiers

La taille maximale des fichiers à téléverser est présentement de 10Go. Pour téléverser un fichier plus volumineux ou si vous rencontrez des problèmes de téléversement (par exemple, en raison d'une mauvaise connexion Internet), utilisez Globus [Globus](globus.md). Un bouton Globus est disponible en haut à droite de l'explorateur de fichiers. Cliquez sur ce bouton pour faire afficher l'interface web de Globus où vous pourrez vous connecter avec votre nom d'utilisateur et votre mot de passe avec l'Alliance. Le chemin d'accès affiché le navigateur Open OnDemand sera identique à celui ouvert dans Globus.

### Soumettre une tâche

Open OnDemand offre une interface pour soumettre des tâches en lots. Sous l'onglet *Jobs*, sélectionnez *Job Composer* pour faire afficher le formulaire de soumission. Cliquez ensuite sur le bouton *New Job* pour faire afficher les options suivantes :

*   *From Default Template*, pour créer une nouvelle tâche;
*   *From Template*, pour sélectionner une tâche, par exemple MPI et OpenMP;
*   *From Specified Path*, pour utiliser une tâche dans le système de fichiers;
*   *From Selected Job*, pour copier la tâche active.

Vous pouvez spécifier les paramètres de la tâche, tels que le script et le nom du compte avec le bouton *Job Options*. Les autres paramètres, comme le nombre de nœuds, le nombre de cœurs, le temps d'exécution, etc., peuvent être modifiés directement dans le script en cliquant sur le bouton *Open Editor*. Une fois les champs obligatoires remplis, cliquez sur le bouton *Submit*.

Cette page affiche également l'état de votre tâche : en attente, en cours d'exécution ou terminée. Une fois la tâche terminée, vous pouvez consulter les journaux de sortie et d'erreurs en cliquant sur un fichier dans la section *Folder Contents* dans le panneau de droite *Job Details*.

## Suivi des tâches

Pour obtenir une vue d'ensemble de toutes vos tâches en attente, utilisez l'interface de suivi des tâches. Sous l'onglet *Jobs* sélectionnez *Active Jobs*. Vous pouvez utiliser le champ *Filter* en haut à droite. Vous pouvez trier les colonnes en cliquant sur leur en-tête, par exemple par état (en cours, terminée, échouée, etc.). Cliquer sur le symbole > à gauche d'une tâche affiche des informations supplémentaires, telles que l'heure de début et de fin, la liste des nœuds et le compte facturé. Pour afficher toutes les tâches en attente, cliquez sur le menu déroulant en haut à droite et sélectionnez *All Jobs*.

### Applications interactives

Open OnDemand offre aussi des applications interactives exécutables directement depuis votre navigateur web. Sous l'onglet *Interactive Apps*, sélectionnez l'application voulue dans le menu déroulant. Ceci affiche la page de soumission des tâches, où vous pouvez choisir les paramètres de votre tâche, par exemple

*   Durée de la tâche (en heures)
*   Nombre de cœurs
*   Quantité de mémoire à allouer (en Go)
*   Notification par courriel du début de la tâche

Après avoir sélectionné les paramètres de votre tâche, cliquez sur le bouton *Launch* pour l'ajouter à la file d'attente. La page *My Interactive Sessions* sera affichée où vous pouvez consulter l'état de votre tâche (en file d'attente, en cours d'exécution ou terminée). Une fois la tâche affectée à un nœud et en cours d'exécution, cliquez sur le bouton *Connect to ...* pour lancer l'application. Celle-ci s'ouvre dans un nouvel onglet où vous pouvez travailler avec la tâche comme si elle était exécutée localement.

Pour accéder au terminal du nœud sur lequel l'application s'exécute, par exemple pour en surveiller les performances, cliquez sur le bouton situé à côté de *Host* commençant par `>_`. Une fenêtre de terminal s'ouvrira alors dans votre navigateur où vous pouvez exécuter directement des commandes sur le nœud.

Si vous souhaitez mettre fin à la tâche pour une quelconque raison, vous pouvez le faire en cliquant sur le bouton rouge *Delete* dans le panneau de la tâche, sur la page *My Interactive Sessions*.

*   Figure 5 : Formulaire
*   Figure 6 : Ouverture d'une session interactive
*   Figure 7 : Application interactive

## Accès via terminal

Si vous préférez utiliser un terminal pour interagir avec la grappe, Open OnDemand met à votre disposition un terminal web pour accéder à l'interface ligne de commande. Pour ce faire, rendez-vous dans l'onglet *Clusters* et sélectionnez *Cluster_Name Shell Access*. Une nouvelle fenêtre de terminal s'ouvrira alors dans votre navigateur, où vous pouvez exécuter des commandes comme dans une application de terminal.

## Débogage

Si des erreurs surviennent lors de l'utilisation d'une tâche interactive Open OnDemand, vous pouvez consulter les journaux pour obtenir plus d'information. Dans l'onglet *My Interactive Sessions*, sélectionnez votre session active. Cliquez sur le lien `output.log` (voir figure 8) pour ouvrir un nouvel onglet affichant la sortie de votre tâche. Ce fichier contient la sortie standard et les messages d'erreur générés par la tâche, ce qui peut vous aider à identifier les problèmes survenus pendant la session. Lorsque vous soumettez une demande d'assistance au soutien technique de SciNet, veuillez inclure le fichier `output.log`, l'identifiant de la session (une longue chaîne de caractères semblable à `8feb45fa-bc65-4846-8398-2a73c1bf8e5a`) et toute autre information pertinente afin de nous permettre de vous aider plus efficacement.