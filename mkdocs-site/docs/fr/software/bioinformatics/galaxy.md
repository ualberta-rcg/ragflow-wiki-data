---
title: "Galaxy/fr"
slug: "galaxy"
lang: "fr"

source_wiki_title: "Galaxy/fr"
source_hash: "d7c280058450da5d71ec8dd4ad47b560"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:32:26.357032+00:00"

tags:
  []

keywords:
  - "Galaxy"
  - "passerelle"
  - "fichiers de configuration"
  - "bio-informatique"
  - "clé publique"
  - "Cedar"
  - "serveur Galaxy"
  - "configuration"
  - "soumettre une tâche"
  - "pseudo-compte"
  - "UseGalaxy Canada"
  - "clés SSH"
  - "instance Galaxy"

questions:
  - "Qu'est-ce que la plateforme Galaxy et à quels domaines de recherche est-elle principalement destinée ?"
  - "Quelles sont les principales différences entre l'utilisation directe de UseGalaxy Canada et l'installation d'une instance sur la grappe Cedar ?"
  - "Comment fonctionne le système de pseudo-compte pour gérer la propriété et la modification des fichiers d'une instance Galaxy sur Cedar ?"
  - "Comment doit-on procéder pour démarrer et accéder au serveur Galaxy via la passerelle dédiée ?"
  - "Quelles sont les variables spécifiques du fichier de configuration galaxy.yml qu'il est fortement recommandé de ne pas modifier ?"
  - "Pourquoi est-il déconseillé d'exécuter des tâches localement et comment le fichier job_conf.xml permet-il d'optimiser leur soumission sur la grappe Cedar ?"
  - "Quel type d'action nécessite de se connecter au pseudo-compte sur l'instance Galaxy ?"
  - "Quelles démarches l'utilisateur doit-il effectuer concernant la paire de clés SSH pour préparer sa connexion ?"
  - "Quel est le rôle de l'administrateur pour finaliser l'accès de l'utilisateur au pseudo-compte ?"
  - "Comment doit-on procéder pour démarrer et accéder au serveur Galaxy via la passerelle dédiée ?"
  - "Quelles sont les variables spécifiques du fichier de configuration galaxy.yml qu'il est fortement recommandé de ne pas modifier ?"
  - "Pourquoi est-il déconseillé d'exécuter des tâches localement et comment le fichier job_conf.xml permet-il d'optimiser leur soumission sur la grappe Cedar ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Galaxy est une plateforme web *libre* pour la recherche biomédicale traitant de grandes quantités de données. La plateforme rend la biologie computationnelle plus accessible, sans exiger une grande expérience en programmation ou en administration de systèmes. Conçue au départ pour la recherche en génomique, Galaxy s’adapte aujourd'hui à la plupart des domaines et sert de système de gestion du flux de travail en bio-informatique. [Cette liste de tutoriels](https://training.galaxyproject.org/) présente une bonne vue d’ensemble des possibilités qu’offre Galaxy.

Vous avez deux options pour utiliser Galaxy :
* accéder directement à UseGalaxy Canada,
* demander une instance de Galaxy sur Cedar.

**Tableau comparatif des options**

| Caractéristique      | Accès direct à UseGalaxy Canada        | Instance de Galaxy sur Cedar                 |
| :------------------- | :------------------------------------- | :------------------------------------------- |
| Serveur              | Nuages Béluga et Arbutus               | Cedar                                        |
| Config. Galaxy       | L'administrateur de UseGalaxy Canada   | Vous-même                                     |
| Connaiss. Linux      | Aucune connaissance préalable          | Connaissance avancée                         |
| Gestion/Mises à jour | Notre équipe UseGalaxy Canada          | Vous-même                                     |
| Config. serveur      | Aucune                                 | Vous-même                                     |
| Outils préinstallés  | Synchronisés avec UseGalaxy.eu         | Outils par défaut (sous-ensemble)            |
| Intégration Irida    | Non                                    | Oui                                          |
| Génomes de référence | Contenus dans CVMFS                    | Gérés par vous-même                          |
| Quota                | 500 Go par utilisateur                 | Espace de stockage alloué par concours       |

!!! tip "Recommandation"
    La plateforme UseGalaxy est fortement recommandée pour le traitement de gros fichiers ou pour des tâches qui nécessitent plusieurs CPU ou GPU.

## Accéder directement à UseGalaxy Canada

Pour accéder à UseGalaxy Canada, suivez simplement le lien [https://starthere.usegalaxy.ca](https://starthere.usegalaxy.ca), puis cliquez sur le bouton de connexion via CILogon et sélectionnez votre établissement pour vous authentifier. La plateforme détecte si vous êtes un utilisateur canadien et vous octroie automatiquement une allocation par défaut de 500 Go de stockage.

Le site [starthere.usegalaxy.ca](https://starthere.usegalaxy.ca) fournit toute l’information nécessaire concernant UseGalaxy.ca et Galaxy en général, de même qu’un formulaire si vous avez besoin d’assistance, voulez rapporter un problème, ou encore faire installer de nouveaux outils ou bases de données.

## Demander une instance de Galaxy sur Cedar

Chaque groupe de recherche peut obtenir une instance Galaxy sur la grappe Cedar. Puisque l’installation demande une configuration particulière, [contactez notre équipe technique](technical-support.md).

### Structure du répertoire

L’installation se fait habituellement dans le répertoire `/project` du groupe de recherche. Le nom du répertoire le plus haut est formé par les deux premiers caractères du nom de la chercheuse ou du chercheur principal (CP), auxquels est ajouté *glxy*. Par exemple, pour le CP *davidc*, le nom du répertoire source sera *daglxy* ; le répertoire sera localisé dans `/project/group name/` où `group name` est le nom du groupe par défaut pour ce CP (`def-davidc`). Le répertoire principal pour Galaxy contient un ensemble de sous-répertoires qui est quelque peu différent du paquet Galaxy original, soit :

*   **config** : contient tous les fichiers de configuration pour préparer et optimiser le serveur Galaxy. Dans cette page, nous présenterons seulement les principes de base pour notre environnement de calcul haute performance.
*   **galaxy.log** : ce fichier contient tous les messages générés à l'ouverture et à la fermeture du serveur.
*   **server.log** : ce fichier contient tous les messages générés pendant l'exécution.

### Propriété et modification des fichiers

Tous les fichiers de votre instance Galaxy appartiennent à un *pseudo-compte*, un compte partagé qui est généré par un administrateur au moment de l'installation. Un pseudo-compte n'appartient pas à une personne en particulier, mais à un groupe. Tous les membres du groupe peuvent se connecter au pseudo-compte à l'aide de clés SSH. Le nom du pseudo-compte est le même que celui du répertoire Galaxy supérieur qui est formé comme expliqué ci-dessus (*daglxy*). Pour modifier un fichier de votre instance Galaxy, par exemple les fichiers de configuration, vous devez d'abord vous connecter au pseudo-compte.

!!! important "Connexion au pseudo-compte"
    Pour vous connecter au pseudo-compte, vous devez d'abord générer une paire de clés SSH, stocker votre clé publique quelque part dans votre répertoire personnel et en informer l'administrateur. L'administrateur stockera votre clé publique dans un endroit approprié, après quoi vous pourrez vous connecter au pseudo-compte.

### Gestion du serveur Galaxy

La première chose à faire est de démarrer le serveur Galaxy. Ce serveur **NE DOIT PAS** se trouver sur un nœud de connexion ou sur un nœud de calcul de Cedar. Nous vous recommandons d'utiliser le serveur dédié appelé *passerelle* qui contient un serveur web avec les répertoires `/project` et `/home` pertinents. Pour des raisons de sécurité, vous ne pouvez pas établir de connexion SSH à cette passerelle ; cependant, nous avons conçu une interface sur cette passerelle qui vous permet de démarrer/arrêter votre serveur Galaxy et d'utiliser l'interface web de Galaxy pour communiquer avec le serveur.
Pour démarrer le serveur Galaxy, suivez [https://gateway.cedar.computecanada.ca/](https://gateway.cedar.computecanada.ca/) et cliquez sur le lien Galaxy. Vous devrez entrer votre nom d'utilisateur et votre mot de passe (les mêmes que ceux que vous avez saisis dans votre compte de l'Alliance). Après la procédure d'authentification, la page du gestionnaire de votre serveur Galaxy sera affichée et vous pourrez gérer votre serveur et utiliser l'interface web Galaxy.

### Configuration du serveur Galaxy

La configuration du serveur se fait avec les fichiers du répertoire `config`. Nous n’expliquons pas ici en détail comment configurer et optimiser Galaxy. Nous vous invitons plutôt à consulter [le site web de Galaxy](https://docs.galaxyproject.org/en/master/admin/config.html).

À l’installation, les variables de base sont paramétrées par l’administrateur dans le fichier de configuration `galaxy.yml`. Vous pouvez modifier les autres fichiers et variables de ce fichier, mais nous recommandons fortement de ne pas modifier les variables de base suivantes :

!!! warning "Variables à ne pas modifier"
    Dans le fichier de configuration principal `galaxy.yml` :
    *   `http:` contient le numéro unique de votre port
    *   `database_connection` est le nom de votre base de données Galaxy et de votre serveur de base de données.
    *   `virtualenv` est le chemin pour [l'environnement virtuel Python](python.md#creer-et-utiliser-un-environnement-virtuel) dans la passerelle
    *   `file_path`, `new_file_path`, `tool_config_file`, `shed_tool_config_file`, `tool_dependency_dir`, `tool_data_path`, `visualization_plugins_directory`, `job_working_directory`, `cluster_files_directory`, `template_cache_path`, `citation_cache_data_dir`, `citation_cache_lock_dir` sont les chemins pour les outils, les *ToolSheds* et les dépendances.

Vous pouvez modifier d'autres variables et fichiers dans ce répertoire.

### Utiliser les outils

Il y a deux manières d'utiliser les outils dans une instance de Galaxy :
*   localement, sur la passerelle où le serveur de Galaxy est installé,
*   en [soumettant une tâche](running-jobs.md) sur Cedar.

### Soumettre une tâche

Voici les points à prendre en considération :

*   **Configuration par défaut**
    *   Galaxy utilise `job_conf.xml` pour définir où et comment les tâches sont exécutées.
    *   Par défaut, les tâches sont soumises sur la grappe Cedar.

*   **Ne travaillez pas localement**
    !!! warning "Exécution sur la passerelle"
        Il n'est pas recommandé d'exécuter des tâches sur la passerelle en raison des contraintes de mémoire et de performance.

*   **Personnalisation**
    *   Il est possible que vous deviez ajuster le contenu du fichier *job_conf.xml* selon les exigences des outils, en particulier pour l'allocation de la mémoire et la limite du temps réel d'exécution ; optimiser ces valeurs est essentiel au bon fonctionnement des outils et pour prévenir les pannes dues au manque de ressources.

*   **Tests**
    *   Effectuez des tests pour déterminer la quantité de mémoire et le temps réel d'exécution appropriés pour chacun des outils.