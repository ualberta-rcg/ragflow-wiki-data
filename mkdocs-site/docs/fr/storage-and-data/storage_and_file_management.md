---
title: "Storage and file management/fr"
slug: "storage_and_file_management"
lang: "fr"

source_wiki_title: "Storage and file management/fr"
source_hash: "c50e4d13b20cdb6cfd594879f6ce7d06"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:57:24.738769+00:00"

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

## Introduction

Nous offrons de nombreuses options de stockage capables de répondre aux besoins de domaines extrêmement variés. Selon vos besoins et votre usage particulier, vous avez le choix parmi différentes solutions allant du stockage à long terme au stockage local temporaire à haute vitesse. Dans la plupart des cas, nos [systèmes de fichiers](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers) sont des ressources partagées et devraient être utilisés de manière responsable; en effet, des dizaines et même des centaines d'utilisateurs peuvent être affectés par une seule personne qui se comporte de manière irréfléchie. Ces systèmes de fichiers sont conçus pour le stockage d'un nombre limité de très grands fichiers, habituellement de type binaire puisque les très gros fichiers texte (centaines de Mo et plus) ne sont pas facilement lisibles par un être humain; pour cette raison, vous devriez éviter de stocker des milliers de petits fichiers de quelques mégaoctets, particulièrement dans le même répertoire. Une meilleure approche serait d'utiliser des commandes telles que `tar` ou `zip` pour convertir un répertoire de plusieurs petits fichiers en un très grand fichier d'archive; consultez [Archivage et compression de fichiers](archiving_and_compressing_files.md).

Il est de votre responsabilité de vérifier depuis quand vos données sont stockées. Le rôle de la plupart des systèmes de fichiers n'est pas d'offrir un service d'archivage à long terme; vous devez donc déplacer les fichiers et répertoires qui ne sont plus utilisés vers un autre endroit, que ce soit sur votre ordinateur personnel ou une autre ressource de stockage que vous contrôlez. Le transfert de grandes quantités de données se fait généralement avec [Globus](../getting-started/globus.md).

Prenez note que les ressources de stockage ne sont pas pour vos données personnelles, mais bien pour les données de recherche.

Lorsque votre compte est créé sur une grappe, votre répertoire *home* contient des références à vos espaces [project](project_layout.md) et *scratch* via des [liens symboliques](https://fr.wikipedia.org/wiki/Lien_symbolique), des raccourcis vers ces autres systèmes de fichiers à partir de votre répertoire *home*. Notez que ces liens symboliques peuvent apparaître seulement quelques heures après votre première connexion. Vous possédez vos propres espaces *home* et *scratch*, alors que l'espace *project* est partagé par le groupe de recherche. Ce groupe peut être constitué d'utilisateurs qui possèdent des comptes liés à celui du chercheur principal ou de comptes de membres d'une [allocation de ressources](../running-jobs/resource_allocation_competition.md). Un utilisateur peut donc avoir accès à plusieurs espaces *project* différents associés à une ou plusieurs chercheuses ou chercheurs principaux et les répertoires *project* de son répertoire *home* contiennent les liens symboliques vers ces différents espaces *project*. Tous les comptes ont accès à un ou plusieurs espaces *project*. Le répertoire `projects` dans votre compte contient un lien symbolique vers chaque espace *project* auquel vous avez accès.
*   Pour un utilisateur dont le compte est lié à un seul compte de chercheur principal, l'espace *project* par défaut est le même espace *project* par défaut que celui du compte du chercheur principal.
*   Pour un utilisateur dont le compte est lié à plusieurs comptes, l'espace *project* par défaut est le même que celui du chercheur principal qui possède le plus grand nombre de comptes qui lui sont associés.

Tous les utilisateurs peuvent vérifier l'espace disque disponible et l'espace disque utilisé par les systèmes de fichiers *project*, *home* et *scratch* avec l'utilitaire en ligne de commande `diskusage_report`, disponible sur les grappes. Pour ce faire, connectez-vous à la grappe par SSH; à l'invite, entrez `diskusage_report` puis appuyez sur la touche *Enter*. L'utilitaire produit un rapport semblable à ceci :

```console
# diskusage_report
                   Description                Space           # of files
                 Home (username)         280 kB/47 GB              25/500k
              Scratch (username)         4096 B/18 TB              1/1000k
       Project (def-username-ab)       4096 B/9536 GB              2/500k
          Project (def-username)       4096 B/9536 GB              2/500k
```

Pour un rapport plus détaillé, utilisez l'outil [Diskusage Explorer](diskusage_explorer.md).

## Types de stockage

Nos ressources comprennent divers systèmes de fichiers pour le stockage; assurez-vous d'utiliser l'espace approprié pour un besoin particulier. Nous présentons ici les principaux systèmes de fichiers de notre infrastructure, quelques-unes de leurs caractéristiques et les besoins pour lesquels ils sont conçus.
*   **HOME** : Il peut sembler logique de stocker tous vos fichiers et d'effectuer tous vos travaux dans votre répertoire *home*; pourtant, le quota pour ce répertoire est relativement petit et la performance est limitée pour la lecture et l'écriture de grandes quantités de données. Ce répertoire est plus approprié pour le code source, les petits fichiers de paramètres et les scripts de soumission des tâches.
*   **PROJECT** : Le quota pour l'espace *project* est beaucoup plus grand et bien adapté au [partage de données](sharing_data.md) entre les membres d'un groupe puisque, contrairement à *home* ou *scratch*, il est relié à un compte de professeur et non à celui d'un utilisateur particulier. Les données enregistrées ici doivent être relativement statiques, c'est-à-dire qu'elles seront modifiées rarement au cours d'un mois; le fait de modifier souvent ces données ou de renommer ou déplacer souvent des fichiers pourrait représenter une charge trop forte pour le système de sauvegarde sur bande.
*   **SCRATCH** : Ce type de stockage s'avère le meilleur choix pour les opérations intensives de lecture/écriture de gros fichiers (> 100Mo par fichier). Sachez toutefois qu'il faut copier les données importantes ailleurs parce qu'il n'y a pas de copie de sauvegarde sur *scratch* et que les fichiers plus anciens sont susceptibles d'être [purgés](scratch_purging_policy.md). Cet espace ne devrait être utilisé que pour les fichiers temporaires comme les fichiers de point de contrôle (*checkpoint files*), les données en sortie d'une tâche ou les autres données qui peuvent être facilement recréées.

!!! warning
    **N'utilisez pas SCRATCH pour stocker tous vos fichiers. Cet espace est conçu pour les fichiers temporaires que vous pouvez perdre sans trop de conséquences.**

*   **NEARLINE** : Ceci est un système de fichiers sur bande pour stocker les données inactives. Les jeux de données auxquels vous ne prévoyez pas d'accéder avant plusieurs mois sont de bons candidats pour y être stockés. Pour plus d'information, consultez la page [Stockage nearline](using_nearline_storage.md).
*   **SLURM_TMPDIR** : Pendant qu'une tâche est en cours d'exécution, la variable d'environnement `$SLURM_TMPDIR` contient le chemin unique vers un répertoire temporaire d'un système de fichier local rapide sur chacun des nœuds de calcul réservés pour cette tâche. Ce répertoire est supprimé avec son contenu quand la tâche se termine et donc cette variable devrait uniquement être utilisée pour des fichiers temporaires utilisés pendant l'exécution de la tâche. L'avantage de ce système de fichiers est que la performance est meilleure puisqu'il se trouve localement sur le nœud de calcul. Il convient particulièrement aux grandes collections de petits fichiers (< 1 Mo par fichier). Les tâches partagent cet espace sur chaque nœud et la capacité disponible dépend des caractéristiques techniques de chacun. Pour plus d'information, voir [Stockage local sur les nœuds de calcul](using_node-local_storage.md).

## Consommation de l'espace project par utilisateur

Pour home et scratch, la commande `diskusage_report` donne l'utilisation de l'espace et des inodes pour chaque utilisateur alors que pour /project, elle donne plutôt le quota total du groupe, incluant donc tous les fichiers des membres. Puisque les fichiers qui appartiennent à un utilisateur peuvent se trouver partout dans project, il est difficile d'obtenir la quantité exacte de fichiers et la quantité de fichiers par utilisateur ou par projet quand un utilisateur a accès à plusieurs projets. Une estimation de l'utilisation de l'espace et des inodes par un utilisateur dans l'espace project total peut toutefois être obtenue avec la commande

```bash
lfs quota -u $USER /project
```

De plus, une estimation de la quantité de fichiers dans un répertoire (et ses sous-répertoires) peut être obtenue avec la commande `lfs find`, par exemple

```bash
lfs find <chemin_vers_le_répertoire> -type f | wc -l
```

## Meilleures pratiques

*   Nettoyez régulièrement les données dans les espaces *project* et *scratch* puisque ces systèmes de fichiers sont utilisés pour d'immenses collections de données.
    *   Documentez vos fichiers avec des [Fichiers README](readme_files.md).
    *   Pour les fichiers qui peuvent être supprimés :
        1.  créez un répertoire temporaire, par exemple `toDelete`;
        2.  déplacez les fichiers à supprimer dans ce répertoire;
        3.  **vérifiez** le contenu du répertoire `toDelete`;
        4.  supprimez `toDelete` récursivement.
    *   Si possible, évitez d’utiliser les caractères `*` et `/` dans vos commandes `rm`.
        *   Naviguez vers le répertoire parent qui contient les éléments à supprimer. Vérifiez qu’il s’agit du bon répertoire.
        *   Si le répertoire contient un [makefile](../programming/make.md), il se pourrait que les caractères `*` et `/` se trouvent dans vos commandes `rm`; il faut bien tester ces commandes.
    *   Dans les scripts de l’interpréteur, si les commandes `rm` contiennent des variables d’environnement, chacune doit être testée avant utilisation. Les variables vides ou non définies peuvent causer des erreurs graves et chaque valeur entrée doit être vérifiée pour éliminer la possibilité d’un usage malveillant ou erroné du script.
*   Utilisez uniquement des fichiers au format texte de moins de quelques mégaoctets.
*   Autant que possible, réservez le stockage *scratch* et le stockage local pour les fichiers temporaires. Pour le stockage local, vous pouvez utiliser le répertoire temporaire `$SLURM_TMPDIR` créé par [l'ordonnanceur](../running-jobs/running_jobs.md) à cet effet.
*   Si le programme doit chercher à l'intérieur d'un fichier, il est plus rapide de lire le fichier au complet d'abord.
*   Si certains fichiers non utilisés doivent être conservés, [archivez-les et compressez-les](archiving_and_compressing_files.md) et si possible, copiez-les ailleurs, par exemple dans [le système de fichiers nearline](using_nearline_storage.md).
*   Pour plus de renseignements sur la gestion d'un grand nombre de fichiers, nous recommandons la lecture de [cette page](handling_large_collections_of_files.md), particulièrement si vous êtes limité par le quota sur le nombre de fichiers.
*   Il est possible que vous ayez des problèmes, peu importe le type d'accès parallèle en lecture à des fichiers dans un système de fichiers comme *home*, *scratch* et *project*; pour contrer ceci, utilisez un outil spécialisé comme [MPI-IO](https://en.wikipedia.org/wiki/Message_Passing_Interface#I/O).
*   Si les solutions de stockage offertes ne conviennent pas à vos besoins, contactez le [soutien technique](../support/technical_support.md).

## Quotas et politiques

Afin que tous les utilisateurs puissent disposer de suffisamment d'espace, des quotas et des politiques sont imposés sur les copies de sauvegarde et la purge automatique de certains systèmes de fichiers.

Sur nos grappes, chaque utilisateur dispose par défaut d'un accès aux espaces *home* et *scratch* et chaque groupe dispose par défaut de 1To d'espace *project*.
Pour une légère augmentation des espaces *project* et *scratch*, utilisez le [service d'accès rapide](../policies/rapid_access_service.md). Pour une augmentation importante des espaces projet, faites une demande dans le cadre du [concours pour l'allocation de ressources](../running-jobs/resource_allocation_competition.md).

Pour connaître votre utilisation des quotas pour les systèmes de fichiers sur nos grappes, utilisez la commande [`diskusage_report`](storage_and_file_management.md#introduction).

=== "Fir"

### Caractéristiques des systèmes de fichiers

|                 | Quota par défaut               | Basé sur Lustre | Copié pour sauvegarde | Purgé                                              | Disponible par défaut | Monté sur les nœuds de calcul |
| :-------------- | :----------------------------- | :-------------- | :-------------------- | :------------------------------------------------- | :-------------------- | :---------------------------- |
| /home           | 50Go et 500K fichiers par utilisateur[^1] | oui             | oui                   | non                                                | oui                   | oui                           |
| /scratch        | 20To et 1M fichiers par utilisateur | oui             | non                   | Les fichiers de 60 jours sont purgés.[^2]          | oui                   | oui                           |
| /project        | 1To et 500K fichiers par groupe[^3] | oui             | oui                   | non                                                | oui                   | oui                           |
| /nearline       | 2To et 5000 fichiers par groupe[^4] | oui             | oui                   | non                                                | oui                   | non                           |

Depuis le 1er avril 2024, le service d’accès rapide permet des quotas plus élevés pour les espaces /project et /nearline; pour plus d’information, voir la section *Stockage* dans [Service d'accès rapide](../policies/rapid_access_service.md). Si vous avez besoin de plus de stockage que ce qui est offert par le service d’accès rapide, vous devrez présenter une demande au [concours pour l'allocation de ressources](../running-jobs/resource_allocation_competition.md).

=== "Nibi"

### Caractéristiques des systèmes de fichiers

|                 | Quota par défaut                  | Basé sur Lustre | Copié pour sauvegarde | Purgé | Disponible par défaut | Monté sur les nœuds de calcul |
| :-------------- | :-------------------------------- | :-------------- | :-------------------- | :---- | :-------------------- | :---------------------------- |
| /home           | 50Go et 500K fichiers par utilisateur[^1] | non             | oui                   | non   | oui                   | oui                           |
| /scratch        | 20To ferme/ 1To souple et 1M fichiers par utilisateur[^5] | non             | non                   | non   | oui                   | oui                           |
| /project        | 1To et 500K fichiers par groupe[^3] | non             | oui                   | non   | oui                   | oui                           |
| /nearline       | 10To et 5000 fichiers par groupe[^4] | oui             | oui                   | non   | oui                   | non                           |

Depuis le 1er avril 2024, le service d’accès rapide permet des quotas plus élevés pour les espaces /project et /nearline; pour plus d’information, voir la section *Stockage* dans [Service d'accès rapide](../policies/rapid_access_service.md). Si vous avez besoin de plus de stockage que ce qui est offert par le service d’accès rapide, vous devrez présenter une demande au [concours pour l'allocation de ressources](../running-jobs/resource_allocation_competition.md).

=== "Narval et Rorqual"

### Caractéristiques des systèmes de fichiers

|                 | Quota par défaut               | Basé sur Lustre | Copié pour sauvegarde | Purgé                                | Disponible par défaut | Monté sur les nœuds de calcul |
| :-------------- | :----------------------------- | :-------------- | :-------------------- | :----------------------------------- | :-------------------- | :---------------------------- |
| /home           | 50Go et 500K fichiers par utilisateur[^1] | oui             | oui                   | non                                  | oui                   | oui                           |
| /scratch        | 20To et 1M fichiers par utilisateur | oui             | non                   | Les fichiers de plus de 60 jours sont purgés.[^6] | oui                   | oui                           |
| /project        | 1To et 500K fichiers par groupe[^7] | oui             | oui                   | non                                  | oui                   | oui                           |
| /nearline       | 1To et 5000 fichiers par groupe[^4] | oui             | oui                   | non                                  | oui                   | non                           |

Depuis le 1er avril 2024, le service d’accès rapide permet des quotas plus élevés pour les espaces /project et /nearline; pour plus d’information, voir la section *Stockage* dans [Service d'accès rapide](../policies/rapid_access_service.md). Si vous avez besoin de plus de stockage que ce qui est offert par le service d’accès rapide, vous devrez présenter une demande au [concours pour l'allocation de ressources](../running-jobs/resource_allocation_competition.md).

=== "Trillium"

### Caractéristiques des systèmes de fichiers

| Système de fichiers | Quota                                                                           | Expiration     | Copié pour sauvegarde | Sur nœuds de connexion | Sur nœuds de calcul |
| :------------------ | :------------------------------------------------------------------------------ | :------------- | :-------------------- | :--------------------- | :------------------ |
| $HOME               | 100Go et 1M fichiers par utilisateur                                            |                | oui                   | oui                    | lecture seule       |
| $SCRATCH            | 25To et 10M fichiers par utilisateur                                            | [à déterminer] | non                   | oui                    | oui                 |
| $PROJECT            | via le concours pour l'allocation de ressources; 1To et 2M fichiers via allocation par défaut |                | oui                   | oui                    | lecture seule       |
| $ARCHIVE            | via le concours pour l'allocation de ressources                                 |                | dual-copy             | non                    | non                 |

*   Il n'y a pas de stockage local sur les nœuds de calcul.
*   L'espace Archive (ou /nearline) se trouve sur [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS).
*   La copie de sauvegarde est un instantané du contenu et non une archive de toutes les données qui y ont été enregistrées.

=== "Killarney"

### Caractéristiques des systèmes de fichiers

| Système de fichiers | Catégorie de Quota                                      | Valeur de Quota      | Durée  | Copié pour sauvegarde | Sur nœuds de connexion | Sur nœuds de calcul |
| :------------------ | :------------------------------------------------------ | :------------------- | :----- | :-------------------- | :--------------------- | :------------------ |
| $HOME               |                                                         | 50 Go par utilisateur |        | oui                   | oui                    | oui                 |
| $SCRATCH            | Chaires en IA CIFAR                                     | 2 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 1 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 500 Go par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 250 Go par utilisateur | 2 mois | non                   | oui                    | oui                 |
| $PROJECT            | Chaires en IA CIFAR                                     | 5 To                 |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 2 To                 |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 1 To                 |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 500 Go               |        | oui                   | oui                    | oui                 |

*   Tous les systèmes de fichiers sont servis à partir du stockage VastData.
*   Une sauvegarde signifie un instantané récent, et non une archive de toutes les données qui ont jamais existé.
*   Pour plus d'information, voir la [politique de purge automatique](scratch_purging_policy.md).

=== "TamIA"

### Caractéristiques des systèmes de fichiers

| Système de fichiers | Catégorie de Quota                                      | Valeur de Quota      | Durée  | Copié pour sauvegarde | Sur nœuds de connexion | Sur nœuds de calcul |
| :------------------ | :------------------------------------------------------ | :------------------- | :----- | :-------------------- | :--------------------- | :------------------ |
| $HOME               |                                                         | 25 Go par utilisateur |        | non                   | oui                    | oui                 |
| $SCRATCH            | Chaires en IA CIFAR                                     | 2 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 1 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 500 Go par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 500 Go par utilisateur | 2 mois | non                   | oui                    | oui                 |
| $PROJECT            | Chaires en IA CIFAR                                     | 5 To                 |        | non                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 2 To                 |        | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 500 Go               |        | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 500 Go               |        | non                   | oui                    | oui                 |

*   Pour plus d'information, voir la [politique de purge automatique](scratch_purging_policy.md).

=== "Vulcan"

### Caractéristiques des systèmes de fichiers

| Système de fichiers | Catégorie de Quota                                      | Valeur de Quota      | Durée  | Copié pour sauvegarde | Sur nœuds de connexion | Sur nœuds de calcul |
| :------------------ | :------------------------------------------------------ | :------------------- | :----- | :-------------------- | :--------------------- | :------------------ |
| $HOME               |                                                         | 50 Go par utilisateur |        | oui                   | oui                    | oui                 |
| $SCRATCH            | Chaires en IA CIFAR                                     | 5 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 5 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 5 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 5 To par utilisateur | 2 mois | non                   | oui                    | oui                 |
| $PROJECT            | Chaires en IA CIFAR                                     | 12,5 To              |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral de l'Institut d'IA         | 10 To                |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral, au sein d'un programme d'IA | 7,5 To               |        | oui                   | oui                    | oui                 |
|                     | Membres du corps professoral, appliquant l'IA à d'autres domaines | 5 To                 |        | oui                   | oui                    | oui                 |

*   Pour plus d'information, voir la [politique de purge automatique](scratch_purging_policy.md).

Les espaces *home* et *project* sont sauvegardés chaque soir; les copies sont conservées pour 30 jours et les fichiers supprimés sont conservés pour 60 jours de plus. Remarquez que ceci est différent de l'âge limite pour la purge des fichiers de l'espace *scratch*. Pour récupérer une version antérieure d'un fichier ou d'un répertoire, contactez le [soutien technique](../support/technical_support.md) en mentionnant le chemin complet pour le ou les fichiers et la date de la version.

## Pour plus d'information

*   [Diskusage Explorer](diskusage_explorer.md)
*   [Répertoire project](project_layout.md)
*   [Stockage /nearline](using_nearline_storage.md)
*   [Partage de données](sharing_data.md)
*   [Transfert de données](../getting-started/transferring_data.md)
*   [Lustre](tuning_lustre.md)
*   [Archivage et compression de fichiers](archiving_and_compressing_files.md)
*   [Travailler avec un grand nombre de fichiers](handling_large_collections_of_files.md)
*   [Entrées/Sorties parallèles : tutoriel](parallel_i_o_introductory_tutorial.md)

## Notes

[^1]: Ce quota est fixe et ne peut pas être changé.
[^2]: Pour plus d'information, voir [la politique de purge automatique](scratch_purging_policy.md).
[^3]: L'espace /project peut être augmenté à 40To par groupe en recourant au [service d'accès rapide](../policies/rapid_access_service.md), pourvu que le quota pour l'espace /project soit au minimum 1To et que le total pour les quatre grappes d'usage général soit au maximum 43To. La demande doit être faite par le chercheur principal responsable pour le groupe en s'adressant au [soutien technique](../support/technical_support.md).
[^4]: Cet espace peut être augmenté à 100To par groupe, réparti sur toutes nos grappes d'usage général, en utilisant le service d'accès rapide. La chercheuse principale ou le chercheur principal doit en faire la demande en écrivant au [soutien technique](../support/technical_support.md).
[^5]: Le quota souple pour chaque chercheur est de 1To. Ici, le terme *quota souple* signifie que vous pouvez temporairement dépasser la limite de 1To pendant 60 jours. Par la suite, aucun fichier supplémentaire ne peut être ajouté. Les fichiers peuvent être écrits de nouveau après qu'un nombre suffisant de fichiers ont été déplacés ou supprimés pour que l'espace /scratch total soit en dessous de 1To. Pour plus d'information, voir [la politique de purge automatique](scratch_purging_policy.md).
[^6]: Voir [la politique de purge automatique](scratch_purging_policy.md).
[^7]: L'espace /project peut être augmenté à 40To par groupe via le service d'accès rapide. Cependant, le quota pour l'espace /project doit être de plus de 1To et le total sur toutes les grappes d'usage général ne doit pas dépasser 43To. La demande doit être faite par le chercheur principal responsable pour le groupe en s'adressant au [soutien technique](../support/technical_support.md).