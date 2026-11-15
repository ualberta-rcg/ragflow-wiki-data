---
title: "Using a resource allocation/fr"
slug: "using_a_resource_allocation"
lang: "fr"

source_wiki_title: "Using a resource allocation/fr"
source_hash: "fe0ce97949d520930613b9dbfde6d44b"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:50:52.568239+00:00"

tags:
  []

keywords:
  - "option --account"
  - "allocation de ressources"
  - "rôle parrainé"
  - "RAP (Resource Allocation Project)"
  - "Partage de données"
  - "allocation active de ressources infonuagiques"
  - "Gestionnaire"
  - "compte"
  - "grappes d'usage général"
  - "demander un compte"
  - "RAPI"
  - "CCDB.alliancecan.ca"
  - "Globus"
  - "espace /project"
  - "projet"
  - "concours pour l'allocation de ressources"
  - "RAP"
  - "désactiver un rôle"
  - "OpenStack"
  - "ajouter des membres"
  - "Répertoire project"
  - "service d’accès rapide"
  - "CCDB AllianceCAN"
  - "utilisateur"
  - "Resource Allocation Project (RAP)"
  - "portail CCDB"
  - "plateformes et portails"
  - "allocation de stockage"
  - "déplacer les données"
  - "allocation de calcul"
  - "utilisateurs parrainés"
  - "parrainage"

questions:
  - "Quels sont les deux types de projets RAP et quelles différences existent entre leurs créations, leurs identifiants (RAPI) et les quotas qui leur sont appliqués ?"
  - "Comment les utilisateurs parrainés doivent‑ils obtenir un compte Alliance et quelles sont les règles concernant le partage de comptes ?"
  - "À quel moment la période d’allocation des ressources débute‑t‑elle habituellement et comment les résultats du concours sont‑ils communiqués aux chercheur·e·s principaux ?"
  - "Quelle est la procédure à suivre pour que le parrain confirme la création d’un compte par courriel ?"
  - "Existe‑t‑il une limite au nombre de personnes pouvant être parrainées, et quelles sont les conditions d’engagement requises ?"
  - "Où peut‑on obtenir des informations complémentaires sur la demande et la gestion de compte sur le portail d’Alliance Can ?"
  - "Qui peut accéder aux ressources allouées et comment ajouter ou gérer les membres d’un RAP via le portail CCDB ?"
  - "Comment spécifier le compte de groupe lors de la soumission d’une tâche de calcul et quelle différence existe‑t‑il entre les projets de concours d’allocation et les projets standards ?"
  - "Quelle procédure est recommandée pour transférer de grandes quantités de données vers une grappe et comment le répertoire /project est‑il structuré et utilisé pour le stockage alloué ?"
  - "Qui peut utiliser une allocation et quelles sont les étapes pour ajouter de nouveaux membres à un projet RAP ?"
  - "Comment soumettre des tâches de calcul en précisant le compte (option --account) lorsqu’on collabore avec plusieurs chercheurs principaux ?"
  - "Quel outil est recommandé pour transférer de larges volumes de données vers le stockage /nearline et comment identifier son allocation de stockage /project ?"
  - "Où peut‑on consulter les informations détaillées sur la structure du projet et le partage des données ?"
  - "Quel est le format du répertoire /project attribué par défaut, incluant le nom du chercheur principal ?"
  - "Dans quels cas doit‑on déplacer les données du répertoire /project vers un autre répertoire du projet pour les plateformes, portails ou groupes de recherche ?"
  - "Comment ajouter un membre (ou un co‑chercheur principal) à votre projet RAP via le portail CCDB d’Alliance Can ?"
  - "Quels droits d’accès sont automatiquement accordés aux membres ajoutés à un projet RAP, notamment concernant les projets OpenStack ?"
  - "Comment attribuer, modifier ou retirer le rôle de Gestionnaire à un membre du projet RAP ?"
  - "Qu’est‑ce qu’un RAP et pourquoi est‑il indispensable pour se connecter au nuage ?"
  - "Comment les ressources allouées via le service d’accès rapide sont‑elles automatiquement associées au RAP par défaut ?"
  - "Comment désactiver un rôle sponsorisé et quel impact cela a‑t‑il sur l’appartenance de l’utilisateur au RAP par défaut ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction au concours pour l'allocation de ressources

Cette page est préparée à l'intention des chercheuses principales et chercheurs principaux qui ont fait une demande au [concours pour l'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-l%E2%80%99allocation-de-ressources). Les demandes sont examinées par des pairs et celles qui reçoivent une allocation obtiennent un accès prioritaire aux ressources de calcul et de stockage en plus de disposer d'une quantité de ressources supérieure à ce qu'il est possible d'obtenir par le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide).

Il y a deux processus de demande, selon que l'allocation est pour
*   des ressources pour un groupe de recherche ou
*   des ressources pour une plateforme ou un portail de recherche.

La période d'allocation des ressources débute habituellement à la première semaine d'avril; le résultat de votre demande devrait vous parvenir en mars. Vous et les utilisatrices et utilisateurs que vous parrainez pouvez utiliser les ressources qui vous sont allouées dès le début de la période d'allocation.

## Projets, groupes et allocations

Les ressources sont allouées pour des projets qui portent le nom de **RAP** (pour *Resource Allocation Project*); un RAP est identifié par un RAPI (son identifiant) et le nom du groupe de recherche.

Il y a deux principaux types de RAP :
*   Le RAP par défaut est créé automatiquement à l'activation d'un rôle de chercheuse ou chercheur principal. Les quotas par défaut et les quotas reliés au service d'accès rapide et aux ressources infonuagiques s'appliquent à ce type de RAP. Les chercheurs principaux et les utilisateurs qu'ils parrainent peuvent se prévaloir de l'usage opportuniste des ressources de calcul avec l'ordre de priorité par défaut, soit le niveau le plus bas. La syntaxe du RAPI est au format `abc-123-aa`; un nom de groupe au format `def-profuntel` y est associé.
*   Le RAP par allocation est créé quand des ressources sont allouées dans le cadre du concours pour l'allocation de ressources. La syntaxe du RAPI est au format `abc-123-ab` et un nom de groupe y est associé. Le nom de groupe pour les ressources aux plateformes et portails est au format `rpp-profuntel`; pour les ressources aux groupes de recherche, `rrg-profuntel`; pour les ressources infonuagiques, `cpp-profuntel` (plateformes et portails) ou `crg-profuntel` (groupes de recherche).

Il est possible d'obtenir plus d'une allocation. Chaque allocation est identifiée par le nom de la ressource (par exemple `nibi-cpu`, `nibi-gpu` ou `nibi-storage`) et sa quantité; le format est `abc-123-aa-001`.

Les RAPI, noms de groupe et allocations sont affichés dans [le portail CCDB](https://ccdb.alliancecan.ca). Pour plus de détails, voyez [Comptes et projets](running_jobs.md#comptes-et-projets).

Pour les détails sur le RAP, consultez la [foire aux questions sur la CCDB](../getting-started/frequently_asked_questions_about_the_ccdb.md).

## Utilisateurs parrainés

Un compte avec l'Alliance est détenu **par une personne**. Il est formellement interdit de partager un compte avec une autre personne. La chercheuse principale ou le chercheur principal doit parrainer chacun des étudiants, employés et collaborateurs qui utiliseront les ressources; chacun devra obtenir son propre compte. Pour obtenir un compte, ils doivent s'enregistrer avec [le formulaire dans la CCDB](https://ccdb.alliancecan.ca); ils devront fournir le CCRI de la personne qui les parraine et celle-ci recevra un courriel lui demandant de confirmer que la personne qui ouvre un compte est parrainée par lui. Il n'y a pas de limite au nombre de personnes pouvant être parrainées; cependant, il devrait s’agir d’utilisateurs qui collaborent effectivement au projet de façon continue. Pour plus d'information, consultez [Demander un compte](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/gestion-de-compte/demander-un-compte).

# Caractéristiques des grappes

Les grappes d'usage général sont [Rorqual](../clusters/rorqual.md), [Fir](../software/fir.md), [Nibi](../clusters/nibi.md) et [Narval](../clusters/narval.md). Il se peut que les ressources qui vous sont allouées soient situées sur plus d'un type de grappe, par exemple sur [Trillium](../clusters/trillium.md) et sur une grappe d'usage général.

=== "Grappes d'usage général"

#### Qui peut utiliser l'allocation?

!!! note
    L'information dans la présente section touche les allocations obtenues dans le cadre du concours pour l'allocation des ressources.

Par défaut, les personnes désignées comme étant parrainées dans votre dossier CCDB ont accès aux ressources qui vous sont allouées; il en est de même pour les co-chercheuses et co-chercheurs.

Au besoin, vous pouvez sélectionner celles et ceux qui peuvent utiliser votre allocation. Pour ce faire,

1.  Connectez-vous à [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/).
2.  Sous *Mon compte*, sélectionnez *Gérer l'appartenance aux projets (RAPI)*. La page [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members) sera affichée. Dans la liste déroulante *Projet (RAP)*, sélectionnez le RAP auquel vous voulez ajouter des membres.
3.  Dans la section *Ajouter des membres*, entrez le CCRI du membre que vous voulez ajouter. Le nom du nouveau membre sera dorénavant surligné en jaune.
4.  Quand un nouveau chercheur principal est ajouté comme membre, les co-chercheurs et les utilisateurs parrainés peuvent être ajoutés en même temps. Dans la section *Ajouter des membres*, cliquez sur *Plusieurs membres* pour faire afficher la liste des rôles qui ne sont pas déjà membres. Si l'utilisateur que vous voulez ajouter ne se trouve pas dans la liste, cliquez sur *Annuler* pour retourner à la page *Gérer l'appartenance aux projets* et entrez le CCRI du membre (voir l'étape 3).

Les membres d'un RAP constituent un groupe pour LDAP. Il s'agit du groupe d'utilisatrices et utilisateurs qui peuvent soumettre des tâches dans le cadre du RAPI (l'identifiant du RAP) et qui peuvent partager des fichiers sous Unix.

#### Utiliser une allocation de calcul

En soumettant une tâche de calcul à l’ordonnanceur, l’utilisateur doit indiquer le nom de son groupe pour l’option `--account`. Dans le cas de tâches pour les projets présentés aux concours d’allocation de ressources, le nom de groupe est celui qui correspond à l’allocation, par exemple `--account=rrg-nom-ab`. Pour les autres projets, le nom de groupe par défaut doit être utilisé, soit `--account=def-nom`.

Pour plus de détails, voyez [Comptes et projets](running_jobs.md#comptes-et-projets).

#### Utiliser une allocation de stockage

Pour transférer de larges quantités de données à une de nos grappes, nous recommandons fortement d’utiliser [Globus](../getting-started/globus.md).

##### `/project`

Une allocation de stockage `/project` dans une grappe d'usage général se présente comme un répertoire au format `/project/<nom>`, par exemple `/project/rrg-nom-ab`; un quota lui est associé pour déterminer la quantité de données qui peuvent y être stockées. Les fichiers pour le projet décrit dans la demande d'allocation de ressources devraient y être enregistrés par tous les utilisateurs parrainés. Pour plus d'information, consultez [Répertoire project](../storage-and-data/project_layout.md) et [Partage de données](../storage-and-data/sharing_data.md).

Vous disposerez aussi par défaut d'un espace /project au format `/project/def-<nomchercheurprincipal>`. Si les données sont en rapport avec le projet décrit dans la demande, vous pourriez vouloir déplacer les données de `/project` vers le répertoire `/project` pour les plateformes et portails ou pour les groupes de recherche.

##### `/nearline`

Consultez [Stockage nearline](../storage-and-data/using_nearline_storage.md).

=== "Trillium"

#### Qui peut utiliser l'allocation?

Par défaut, les utilisatrices et utilisateurs qui ont un rôle parrainé par vous peuvent avoir accès aux ressources qui vous sont allouées. Ceci comprend aussi les co-chercheuses et co-chercheurs principaux mentionnés dans votre demande.

Au besoin, vous pouvez sélectionner les ceux et celles qui peuvent utiliser votre allocation. Pour ce faire,

1.  Connectez-vous à [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/).
2.  Sous *Mon compte*, sélectionnez *Gérer l'appartenance aux projets (RAPI)*. La page [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members) sera affichée. Dans la liste déroulante *Projet (RAP)*, sélectionnez le RAP auquel vous voulez ajouter des membres.
3.  Dans la section *Ajouter des membres*, entrez le CCRI du membre que vous voulez ajouter. Le nom du nouveau membre sera dorénavant surligné en jaune.
4.  Quand un nouveau chercheur principal est ajouté comme membre, les co-chercheurs et les utilisateurs parrainés peuvent être ajoutés en même temps. Dans la section *Ajouter des membres*, cliquez sur *Plusieurs membres* pour faire afficher la liste des rôles qui ne sont pas déjà membres. Si l'utilisateur que vous voulez ajouter ne se trouve pas dans la liste, cliquez sur *Annuler* pour retourner à la page *Gérer l'appartenance aux projets* et entrez le CCRI du membre (voir l'étape 3).

Les utilisateurs pour un RAP sont groupés sous LDAP (*Lightweight Directory Access Protocol*). Ce groupe d'utilisateurs peut soumettre des tâches dans le cadre d'un RAPI (identifiant du RAP) et partager des fichiers du même groupe Unix.

#### Utiliser une allocation de calcul

Les tâches soumises à l’ordonnanceur sont assignées à l’allocation du chercheur principal. Dans le cas où l’utilisateur collabore avec plusieurs chercheurs principaux (donc à des groupes différents), le nom du groupe particulier doit être employé pour l’option `--account`.

Pour plus de détails, voyez [Comptes et projets](running_jobs.md#comptes-et-projets).

#### Utiliser une allocation de stockage

Pour transférer de larges quantités de données à une grappe de l'Alliance, nous recommandons fortement d’utiliser [Globus](../getting-started/globus.md).

##### `/project`

Pour repérer votre allocation de stockage `/project`, utilisez la variable d'environnement `$PROJECT`.

##### `/nearline`

Les allocations `/nearline` se trouvent dans HPSS. Consultez [Stockage nearline](../storage-and-data/using_nearline_storage.md).

=== "Nuages"

Les ressources infonuagiques allouées via le service d’accès rapide utilisent le RAP par défaut.

Les ressources infonuagiques allouées via le concours utilisent un RAP dont la convention pour les noms de groupe diffère de celle des RAP par défaut. Les noms pour les groupes de recherche sont au format `cpp-profuntel` pour les ressources aux plateformes et portails et `crg-profuntel` pour les plateformes et portails.

#### Qui peut utiliser l'allocation?

Si vous avez une allocation active de ressources infonuagiques, vous devriez déjà avoir un RAP et ainsi pouvoir vous connecter au nuage.

*   Les ressources allouées via le service d’accès rapide utilisent le RAP par défaut. Les utilisatrices et utilisateurs qui ont un rôle parrainé par vous sont toujours membres de votre RAP par défaut; le fait de confirmer le parrainage d’un utilisateur en fait un membre de votre RAP par défaut. Il est cependant possible de désactiver un rôle en tout temps.
*   Dans le cas des ressources allouées via le concours, seul le chercheur principal est membre du RAP. Il peut cependant ajouter un membre qu’il parraine ou tout autre utilisateur actif de l'Alliance. Les ressources ne peuvent être utilisées que par les membres ajoutés à votre RAP.

Au besoin, vous pouvez sélectionner les ceux et celles qui peuvent utiliser votre allocation. Pour ce faire,

1.  Connectez-vous à [https://ccdb.alliancecan.ca/](https://ccdb.alliancecan.ca/).
2.  Sous *Mon compte*, sélectionnez *Gérer l'appartenance aux projets (RAPI)*. La page [https://ccdb.alliancecan.ca/resource_allocation_projects/members](https://ccdb.alliancecan.ca/resource_allocation_projects/members) sera affichée. Dans la liste déroulante *Projet (RAP)*, sélectionnez le RAP auquel vous voulez ajouter des membres.
3.  Dans *Ajouter des membres*, cliquez sur *Plusieurs membres* pour faire afficher la page où vous pourrez ajouter les co-chercheurs principaux et leurs rôles parrainés.
4.  Si le nom que vous voulez ajouter ne paraît pas dans la liste, cliquez sur *Annuler* pour retourner à la page *Gérer l'appartenance aux projets*. Dans la section *Ajouter des membres*, entrez le CCRI dans le champ *Ajouter un membre avec son CCRI*.
5.  L'étape 4 vous permet d'ajouter un co-chercheur principal associé qui n'aurait pas été mentionné dans votre demande de ressources. Une fois que le co-chercheur est ajouté comme membre, vous pouvez utiliser la méthode décrite à l'étape 3 pour ajouter ses rôles parrainés.

!!! warning
    *   Les membres ajoutés au projet ont automatiquement accès aux ressources. En tout temps, il est possible de supprimer des membres de la liste ou de donner ou enlever à un membre la responsabilité de Gestionnaire.
    *   Les membres de votre projet infonuagique ont accès complet à vos projets OpenStack. Pour l'information sur ces projets, consultez Projets dans la page OpenStack.

Pour savoir comment vous connecter et utiliser un nuage en particulier, consultez [Service infonuagique](../cloud/cloud.md). Si vous avez besoin d'aide, contactez le [soutien technique](../support/technical_support.md).