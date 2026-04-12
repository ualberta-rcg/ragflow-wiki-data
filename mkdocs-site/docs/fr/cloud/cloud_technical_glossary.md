---
title: "Cloud Technical Glossary/fr"
slug: "cloud_technical_glossary"
lang: "fr"

source_wiki_title: "Cloud Technical Glossary/fr"
source_hash: "77277155b40753ab894b71648c4aa530"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:24:02.541786+00:00"

tags:
  - cloud

keywords:
  - "machine virtuelle"
  - "OpenStack"
  - "stockage"
  - "Ceph"
  - "volume"
  - "stockage de type volume"
  - "allocation de ressources"
  - "protocoles S3 et Swift"
  - "vGPU"
  - "espaces de stockage"
  - "infonuagique"
  - "stockage objet"
  - "ressources infonuagiques"
  - "disque virtuel"
  - "stockage cloud persistant"
  - "ressource de calcul infonuagique persistant"
  - "instance"

questions:
  - "Qu'est-ce qu'OpenStack et quel est le rôle de son tableau de bord Horizon dans la gestion des ressources infonuagiques ?"
  - "Quelles sont les différences entre les différents types de stockage mentionnés, tels que le stockage objet, CephFS et le disque local éphémère ?"
  - "Comment les concepts de gabarit, d'image et d'hôte interagissent-ils lors de la création et de l'exécution d'une instance de machine virtuelle ?"
  - "Quelle est la différence entre le Concours pour l'allocation de ressources et le Service d'accès rapide pour l'obtention de ressources infonuagiques ?"
  - "Quels sont les différents types de solutions de stockage décrits dans le texte (tels que S3, SWIFT, système de fichiers partagé et volume) et à quoi servent-ils ?"
  - "Comment les ressources de calcul (vCPU, vGPU) et les règles de réseau (groupes de sécurité) sont-elles appliquées aux machines virtuelles au sein d'un projet ?"
  - "Quels protocoles sont pris en charge pour le stockage offert sur Arbutus ?"
  - "Quel est le rôle de la suite logicielle OpenStack dans la gestion de l'infrastructure matérielle ?"
  - "En quelle unité de mesure l'espace de stockage est-il alloué sur ces systèmes ?"
  - "Comment le système d'exploitation perçoit-il un vGPU lorsqu'il est alloué à une machine virtuelle ?"
  - "Quel terme spécifique l'environnement OpenStack utilise-t-il pour désigner une machine virtuelle active ?"
  - "Qu'est-ce qu'un volume dans le contexte d'OpenStack et comment interagit-il avec une instance ?"
  - "Qu'est-ce que le stockage de type volume et quelle fonctionnalité principale offre-t-il aux instances OpenStack ?"
  - "Quel logiciel est utilisé pour implémenter ce type de stockage cloud persistant ?"
  - "Dans quelle unité de mesure l'espace de ce stockage est-il alloué ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Terme | Définition |
| :---- | :--------- |
| **Apache HTTP Server** | Un logiciel pour l’implémentation de serveurs Web. Voir [https://en.wikipedia.org/wiki/Apache_HTTP_Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server). |
| **CALM** (*cloud account lifecycle management*) | Gestion du cycle de vie d’un compte infonuagique. Notre processus pour gérer l’allocation des ressources infonuagiques. |
| **Ceph** | La plateforme de stockage distribué des données pour nos nuages; inclut le stockage de volumes. |
| [CephFS](cephfs.md) (*Ceph File System*) | Un système de fichiers pour stockage Ceph qui permet de monter des données sur plusieurs machines virtuelles simultanément. Ce service est présentement offert sur Arbutus seulement. Voir [https://docs.ceph.com/en/latest/cephfs/](https://docs.ceph.com/en/latest/cephfs/). |
| **nuage** (*cloud*) | En référence à nos services infonuagiques, forme courte de *nuage IaaS*. |
| **ressource de calcul infonuagique** | Type de ressource allouée pour supporter les instances dont l’exécution est limitée dans le temps et qui requièrent une grande utilisation de CPU et mémoire de manière soutenue. Les noms de gabarits pour ces ressources commencent par la lettre c. Ces ressources sont présentement offertes sur Arbutus, Béluga et Cedar. Comparer à *ressource de calcul infonuagique persistant*. |
| [CVMFS](../software/cvmfs/cvmfs.md) (*CernVM File System*) | Un système de distribution de contenu en lecture seule souvent utilisé pour distribuer des logiciels. |
| **disque local éphémère** | Disque virtuel créé et supprimé avec une instance OpenStack. Ce type de disque est créé au lancement d’une instance quand un volume n’est pas spécifié. |
| **gabarit** (*flavor*) | Terme utilisé dans OpenStack pour désigner une configuration préétablie pour une nouvelle instance. Un gabarit peut définir plusieurs paramètres, par exemple le nombre de cœurs et la capacité de mémoire vive et sur disque. |
| **IP flottante** | Adresse IP qui peut être associée à une instance OpenStack pour permettre aux périphériques externes d’y accéder. |
| **Horizon** | Tableau de bord OpenStack pour la gestion des ressources infonuagiques via un navigateur Web. Voir [https://docs.openstack.org/horizon/latest/](https://docs.openstack.org/horizon/latest/). |
| **hôte** | Serveur physique qui supporte les machines virtuelles. |
| [image](working_with_images.md) | Image d’un disque virtuel utilisée pour créer un volume de démarrage ou un disque éphémère quand une instance OpenStack est créée. |
| **instance** | Les machines virtuelles OpenStack sont appelées *instances*, principalement parce qu'il s'agit d'instances d'une image créée à la demande et configurée au lancement de l’instance. |
| [IPV6](using_ipv6_in_cloud.md) (*Internet Protocol version 6*) | Protocole de communication successeur de IPv4. Voir [https://en.wikipedia.org/wiki/IPv6](https://en.wikipedia.org/wiki/IPv6). |
| [stockage objet](arbutus_object_storage.md) | Le stockage d'objets (ou *stockage basé sur des objets*) est un type de stockage où les données sont gérées comme des objets, par opposition à d'autres architectures comme les systèmes de fichiers qui gèrent les données sous forme de hiérarchie de fichiers ou le stockage des données en tant que blocs. Chaque objet comprend généralement les données elles-mêmes, une quantité variable de métadonnées et un identifiant unique au monde. Présentement offert sur Arbutus seulement sous les protocoles S3 et Swift. Alloué en téraoctets. Voir [https://en.wikipedia.org/wiki/Object_storage](https://en.wikipedia.org/wiki/Object_storage). |
| [OpenStack](managing_your_cloud_resources_with_openstack.md) | La suite logicielle utilisée pour contrôler nos ressources infonuagiques matérielles telles que des ordinateurs, des espaces de stockage et la réseautique. |
| **ressource de calcul infonuagique persistant** | Type de ressource alloué pour supporter les instances qui seront actives indéfiniment et qui utilisent les CPU de façon minimale ou en rafale. Les noms de gabarits pour ces ressources commencent par la lettre p. Ces ressources sont offertes présentement sur Arbutus, Béluga et Cedar. Comparer à *ressource de calcul infonuagique*. |
| **projet** | Dans notre infrastructure, un projet représente une allocation de ressources infonuagiques à un utilisateur ou à un groupe. |
| [Concours pour l’allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources) (en anglais RAC pour *resource allocation competition*) | Notre programme par lequel les chercheuses principales et chercheurs principaux font des demandes de ressources et de calcul. Les demandes sont soumises à un examen scientifique et permettent d’obtenir plus de ressources que ce qui peut être obtenu par le service d’accès rapide. |
| [Service d’accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) (en anglais RAS pour *rapid access service*) | Service par lequel les chercheuses principales et chercheurs principaux peuvent obtenir une petite quantité de ressources infonuagiques et de stockage, sans avoir à présenter une demande au concours pour l'allocation de ressources. |
| **S3** (*Simple Storage Service*) | Un type de stockage objet. Voir [https://en.wikipedia.org/wiki/Amazon_S3](https://en.wikipedia.org/wiki/Amazon_S3). |
| [groupe de sécurité](managing_your_cloud_resources_with_openstack.md#groupes-de-securite) | Ensemble de règles de sécurité qui contrôlent le trafic réseau et peuvent être appliquées dans leur ensemble à une ou plusieurs instances. |
| **portal de service** | Notre infrastructure héberge plusieurs portails de recherche Web qui rendent des outils ou des ensembles de données accessibles à diverses communautés de recherche. De manière générale, ces portails nécessitent peu de ressources de calcul et de stockage, mais ont besoin de l’assistance de notre équipe technique. Par contre, nos ressources infonuagiques sont souvent requises et offrent généralement une adresse IP publique. Contrairement aux autres projets de recherche, les portails ont souvent besoin d’être en ligne sans interruption. |
| **système de fichiers partagé** | Espace de stockage persistant proposé sous la forme d'un système de fichiers compatible Unix pouvant être monté sur plusieurs hôtes dans un projet. Ceci est utile pour partager des données entre plusieurs hôtes. Le service s'exécute sur CephFS et nécessite un pilote Fuse (Windows/Linux) ou le pilote du noyau CephFS (Linux) pour y accéder. Alloué en To. |
| **instantané** | Copie d’un volume OpenStack qui peut être utilisée pour la sauvegarde ou pour lancer une autre instance. |
| **SSL** (*Secure Sockets Layer*) | Protocole de chiffrement des données communiquées sur les réseaux. Ce protocole est maintenant obsolète; dans la mesure du possible, utilisez plutôt le protocole TLS (Transport Layer Security). |
| [SWIFT](using-swift.md) | Un type de stockage objet. Voir [https://wiki.openstack.org/wiki/Swift](https://wiki.openstack.org/wiki/Swift). |
| **tenant** | Terme anglais utilisé occasionnellement pour désigner un projet. |
| **TSL** (*Transport Layer Security*) | Voir *SSL*. |
| **vCPU** (*virtual central processing unit*) | Un vCPU représente une partie ou un partage du CPU physique sous-jacent qui est alloué à une machine virtuelle particulière. |
| [vGPU](using_cloud_vgpus.md) (*virtual graphics processing unit*) | Un ou plusieurs vGPU peuvent être alloués à une machine virtuelle. Le système d’exploitation considère chaque vGPU comme étant un GPU physique. Il pourrait être nécessaire d’effectuer certaines configurations. |
| **machine virtuelle** | Serveur virtuel dans l’infrastructure infonuagique. OpenStack utilise le terme *instance* pour désigner une machine virtuelle active. |
| [volume](working_with_volumes.md) | Ressource de stockage qui peut être attachée à ou détachée d'une instance OpenStack, comme un disque virtuel. |
| **stockage de type volume** | Type de stockage cloud persistant fournissant une fonctionnalité de disque virtuel aux instances OpenStack exécutées dans le nuage. Implémenté avec le logiciel Ceph. Alloué en Go. |