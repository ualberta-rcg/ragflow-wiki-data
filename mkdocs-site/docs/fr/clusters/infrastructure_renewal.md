---
title: "Infrastructure renewal/fr"
slug: "infrastructure_renewal"
lang: "fr"

source_wiki_title: "Infrastructure renewal/fr"
source_hash: "b040f0a7aca7bf32b61431fc277d662a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:05:10.382805+00:00"

tags:
  []

keywords:
  - "compilation de codes"
  - "Systèmes nationaux de l'Alliance"
  - "mise à niveau"
  - "MIG"
  - "installation"
  - "utilisation des GPU"
  - "Multifactor Authentication"
  - "soutien technique"
  - "logiciels"
  - "Rorqual"
  - "Accès aux données"
  - "mise à jour"
  - "grappe de formation"
  - "MPS"
  - "État des systèmes"
  - "mises à niveau GPU"
  - "arrêts de service"
  - "Grappes de calcul"
  - "Arbutus Cloud"
  - "mises à jour"
  - "utilisation du GPU"
  - "Mise hors service"
  - "infrastructure de calcul"
  - "cours en ligne"
  - "grappe Fir"
  - "webinaires"
  - "grappe de calcul"
  - "Decommissioning"
  - "sites hôtes nationaux"
  - "transition"
  - "utilisation de Slurm"
  - "nouveaux systèmes"
  - "grands ensembles de données"
  - "formation en ligne"
  - "Béluga compute service"
  - "migration des données"
  - "technologies NVIDIA"
  - "matériel"
  - "migration"
  - "Transition"
  - "outils et logiciels"
  - "Espaces de stockage"

questions:
  - "Quels sont les objectifs principaux et l'échéancier prévus pour la mise à jour de l'infrastructure de calcul informatique ?"
  - "Quels nouveaux systèmes remplaceront les anciennes grappes de calcul telles que Béluga, Cedar et Graham ?"
  - "Quels impacts cette transition aura-t-elle sur les services en cours et quelles actions sont requises de la part des utilisateurs pour la migration ?"
  - "What is the expected timeline for the decommissioning of the Béluga compute service?"
  - "Which new system deployment resulted in the permanent shutdown of the Béluga service?"
  - "What security authentication method is associated with accessing the Arbutus Cloud?"
  - "Quelles sont les dates clés et les étapes prévues pour la fermeture définitive des espaces de stockage et des anciennes grappes de calcul comme Béluga ?"
  - "Comment les utilisateurs pourront-ils accéder à leurs données et soumettre de nouvelles tâches suite à la mise hors service des grappes Cedar et Graham ?"
  - "Quel sera l'impact de cette transition sur les allocations de ressources (RAC) et quelles formations sont mises à disposition pour accompagner les utilisateurs ?"
  - "Quels sont les principaux langages et technologies de calcul haute performance (comme OpenMP, MPI ou Python HPC) présentés dans ce cours ?"
  - "Quelles compétences pratiques les participants acquièrent-ils concernant l'utilisation de Slurm et la gestion des ressources ?"
  - "À quel public cette formation est-elle destinée et sous quel format logistique s'est-elle déroulée ?"
  - "Quels sont les nouveaux noms et les capacités des systèmes nationaux mis à niveau, et comment les utilisateurs peuvent-ils migrer vers ces nouvelles infrastructures comme Trillium ?"
  - "Quelles techniques et outils spécifiques sont présentés pour optimiser les flux de travail impliquant de très grands ensembles de données ?"
  - "Comment les utilisateurs peuvent-ils mesurer et améliorer l'efficacité de leurs tâches sur des GPU modernes en utilisant des technologies comme MPS et MIG ?"
  - "Quelles sont les caractéristiques matérielles et les meilleures pratiques d'utilisation de la nouvelle grappe Fir ?"
  - "Comment les utilisateurs peuvent-ils s'adapter à la diminution du nombre de GPU lors de la transition vers les nouveaux modèles NVIDIA H100 ?"
  - "Quelles sont les mesures prévues pour la migration et la sécurité des données des utilisateurs pendant les arrêts de service et la transition des systèmes ?"
  - "Quelles sont les causes principales qui empêchent de saturer ou d'utiliser pleinement un GPU selon le texte ?"
  - "Quelles technologies spécifiques de NVIDIA ce cours permet-il d'apprendre pour optimiser l'utilisation du GPU ?"
  - "Quel est le format de cette formation et quelles sont les conditions requises pour pouvoir y accéder ?"
  - "Où les événements survenant pendant l'installation et la transition seront-ils signalés ?"
  - "Comment les utilisateurs seront-ils tenus au courant des nouvelles informations et des mises à jour ?"
  - "Qui faut-il contacter pour obtenir des réponses sur la transition et pourquoi cette aide pourrait-elle être limitée ?"
  - "Comment la transition vers les nouveaux systèmes affectera-t-elle la compatibilité et la disponibilité des applications et des logiciels commerciaux ?"
  - "Faut-il s'attendre à des interruptions de service simultanées sur plusieurs systèmes pendant la migration ?"
  - "Que deviendra le matériel retiré de l'infrastructure et est-il possible pour les utilisateurs de l'acheter ?"
  - "Comment la transition vers les nouveaux systèmes affectera-t-elle la compatibilité et la disponibilité des applications et des logiciels commerciaux ?"
  - "Faut-il s'attendre à des interruptions de service simultanées sur plusieurs systèmes pendant la migration ?"
  - "Que deviendra le matériel retiré de l'infrastructure et est-il possible pour les utilisateurs de l'acheter ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Importante mise à jour de notre infrastructure de calcul informatique de pointe

L'importante mise à jour de notre infrastructure de calcul informatique de pointe, qui se fera à partir de l'hiver 2024-2025, permettra d’améliorer nos services de calcul de haute performance et nos services infonuagiques pour soutenir la recherche au Canada. La mise en service de la plupart des nouveaux systèmes est prévue pour l'été de 2025. Le contenu de la présente page sera mis à jour au fur et à mesure que les informations sont disponibles.

Près de 80 % de nos équipements qui approchent de leur fin de vie seront remplacés. Le nouveau matériel offrira une vitesse de traitement plus rapide, une plus grande capacité de stockage et une fiabilité améliorée.

## Documentation des systèmes

| **Documentation** | **Système remplacé** |
| :---------------- | :------------------- |
| [Arbutus](arbutus.md) | [nuage](cloud.md) (aucun changement à cette infrastructure virtuelle) |
| [Rorqual](rorqual.md) | [Béluga](beluga.md) |
| [Fir](fir.md) | [Cedar](cedar.md) |
| [Trillium](trillium.md) | Niagara et [Mist](mist.md) |
| [Nibi](nibi.md) | [Graham](graham.md) |

## Capacité des systèmes, baisses et arrêts de services

Pendant l'installation et la transition vers les nouveaux systèmes, nous devrons sans doute suspendre ou diminuer les services en raison de contraintes d'alimentation électrique ou d'espace. Veuillez tenir compte de ces possibilités dans la planification de votre programme de recherche, des soutenances de thèse ou de mémoire, etc.

[Cliquez ici pour la liste des travaux terminés](infrastructure-renewal-completed-events.md).

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| janvier 2026 | 20 juin 2026 | en cours | Béluga | fermeture définitive | Le service de calcul **Béluga**, qui a été arrêté lors du déploiement de **Rorqual**, ne sera pas remis en service. Aucune restauration ou réactivation n'est prévue. |

!!! info "Mise à jour : Nuage Arbutus"

Le **nuage Arbutus** amélioré est maintenant en production et accessible aux récipiendaires des RAC 2026–2027.

**Mesures à prendre**

*   Les récipiendaires des RAC et les utilisateurs des RAS ayant une allocation 2025–2026 sur l'ancien Arbutus sont responsables de la migration des ressources existantes avant le 31 août 2026.
*   La migration peut commencer dès que l'accès au nouveau nuage Arbutus est disponible.
*   Les allocations RAC 2025–2026 resteront actives sur l'ancien Arbutus pendant la période de migration.
*   Les projets avec des allocations RAS nuage Arbutus existantes doivent soumettre une demande à [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca) pour être ajoutés à la file d'attente d'approvisionnement. L'approvisionnement est effectué en vrac et des retards peuvent survenir avant que l'accès ne soit disponible.

**Ce qui change**

*   Le nouveau nuage Arbutus introduit l'authentification unique (SSO) avec authentification multifacteur (MFA).
*   Les utilisateurs doivent sélectionner « S'authentifier en utilisant l'Alliance de recherche numérique du Canada » lors de la connexion.

**Documentation**

*   [Guide de migration Arbutus](https://docs.alliancecan.ca/wiki/Arbutus_Migration_Guide)
*   [Authentification multifacteur](https://docs.alliancecan.ca/wiki/Multifactor_authentication)

Pour y accéder : [nuage Arbutus](https://arbutus.alliancecan.ca/)

### Fermeture des espaces de stockage

*   **Janvier 2026** – Les quotas pour le stockage sur `/project`, `/home`, `/scratch` et `/nearline` seront diminués pour permettre uniquement la suppression ou l'archivage des données. Ceci laisse une période de six mois pour effectuer l'extraction et la migration des fichiers.
*   **28 février 2026** – Fermeture définitive du stockage sur `/scratch`. Les fichiers importants doivent être déplacés avant cette date.
*   **20 juin 2026** – L'accès aux données ne sera plus possible.

!!! note "Remarque"
Le nuage Béluga (`beluga-cloud`) est une infrastructure distincte et ne sera pas touchée par la fermeture définitive de la grappe de calcul Béluga.

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| 30 septembre 2025 | | en cours | Niagara | mise hors service | La grappe Niagara a été fermée définitivement le 30 septembre 2025. |

Pour des détails sur la transition, voir [Transition de Niagara vers Trillium](transition-from-niagara-to-trillium.md).

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| 16 septembre 2025 | | en cours | Mist | mise hors service | La grappe Mist a été fermée définitivement le 16 septembre 2025. |

Pour vos nouveaux travaux, veuillez utiliser Trillium (voir [Trillium : Guide de démarrage](trillium-quickstart.md)).

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| 12 septembre 2025 | | en cours | Cedar | mise hors service | La grappe Cedar a été fermée définitivement le 12 septembre 2025. |

### Accès aux données

*Les fichiers stockés sur Cedar sont disponibles sur Fir puisque les deux grappes partagent les mêmes systèmes de fichiers; aucune action n'est requise de votre part.

À compter du 12 septembre, veuillez soumettre vos tâches sur une autre grappe de notre [nouvelle infrastructure nationale](national-systems.md), y compris Fir.

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| 1er septembre 2025 | | en cours | Graham | mise hors service | La grappe Graham a été fermée définitivement le 1er septembre 2025. |

### Accès aux données

*Les fichiers stockés sur Graham sont aussi disponibles sur Nibi puisque les deux grappes partagent les mêmes systèmes de fichiers; aucune action n'est requise de votre part.

À compter du 1er septembre, veuillez soumettre vos tâches sur une autre grappe de notre [nouvelle infrastructure nationale](national-systems.md), y compris Nibi.

## Compétition pour l'Allocation de Ressources (RAC)

La [Compétition pour l'Allocation de Ressources](resource-allocation-competition.md) sera impactée par cette transition, mais le processus de demande demeure le même.

Les allocations 2024-2025 resteront en vigueur sur les grappes en voie de retrait tant que chaque grappe sera en service. Les allocations 2025-2026 seront mises en œuvre partout une fois que toutes les nouvelles grappes seront en service.

Puisque les anciennes grappes seront majoritairement hors service avant que toutes les nouvelles ne soient disponibles, si vous détenez une allocation RAC pour 2024 et une autre pour 2025, vous connaîtrez une période où aucune des deux allocations ne vous sera accessible. Vous pourrez effectuer des calculs avec votre allocation par défaut (`def-xxxxxx`) sur chaque nouvelle grappe dès sa mise en service, mais les allocations RAC 2025 ne seront disponibles que lorsque toutes les nouvelles grappes seront en service.

## Outils de formation

D'autres ressources de formation sont disponibles via [Explora](https://explora.alliancecan.ca).

| **Titre** | **Organisation** | **Présenté par** | **Date** | **Description** | **Public cible** | **Format** | **Inscription** |
| :-------- | :--------------- | :--------------- | :------- | :-------------- | :------------- | :--------- | :------------ |
| Introduction au HPC sur les grappes de l'Alliance (en trois parties de 2 heures chacune) | Université Simon-Fraser / Groupe de l’IRN de la C.-B. | Alex Razoumov | les jeudis 25 septembre, 2 octobre et 9 octobre, 10 h HP | Introduction au calcul de haute performance sur les grappes de l'Alliance : matériel; outils et logiciels; coup d'œil sur OpenMP, MPI, HPC Python (Dask, Ray), Chapel, Julia; compilation de codes séquentiels/partagés/distribués; utilisation de Slurm (en lots et interactivement), étalonnage (**benchmarking**), soumission de plusieurs tâches, estimation des ressources nécessaires, gestion des permissions. Inclut des démos et des exercices pratiques sur une grappe de formation. | Utilisatrices et utilisateurs nouveaux ou potentiels | webinaires (3 parties de 2 heures chacune) | Passé |
| [HPC105: Intro to SciNet and Trillium](https://education.scinet.utoronto.ca/enrol/index.php?id=1389) | SciNet | Équipe de formation SciNet | en tout temps (mise à jour le 25 août 2025) | Formation autonome sur les systèmes de SciNet ([Trillium](trillium.md)) : configuration de votre compte, première connexion, exécution de tâches de calcul. Pour les utilisatrices et utilisateurs de Niagara et Mist, cette formation montre comment migrer vers Trillium. | Utilisatrices et utilisateurs potentiels de [Trillium](trillium.md) et nouveaux utilisateurs et utilisatrices de SciNet | Formation autonome en ligne (environ 4 heures) | [Cliquez ici pour commencer la formation/ Vous devez détenir un compte avec l'Alliance dans CCDB](https://education.scinet.utoronto.ca/enrol/index.php?id=1389). |
| [Migrating to the upgraded national systems](https://youtu.be/nRX8zTIVEXk) | SHARCNET | Sergey Mashchenko | mercredi 30 juillet 2025, 12 h HAE | La plupart des systèmes nationaux de l'Alliance ont connu une mise à niveau majeure au cours du printemps et de l'été. Ils ont été reconstruits de A à Z avec du matériel moderne, ce qui a augmenté considérablement la capacité de calcul, de mémoire et de stockage. Les grappes mises à niveau ont de nouveaux noms : Graham est devenue Nibi, Béluga est devenue Rorqual, Cedar est devenue Fir, Niagara est devenue Trillium. La grappe Narval n'a pas été modifiée. Certains des systèmes mis à niveau sont déjà en ligne, mais pas encore à pleine capacité. Il est prévu de les rendre tous disponibles d'ici la fin juillet.<br><br> Ce webinaire veut répondre aux préoccupations et aux questions des utilisateurs des systèmes existants. Quel sera l'impact des mises à niveau sur mon flux de travail? Y a-t-il des changements significatifs dans la planification des tâches et des systèmes de fichiers? Comment optimiser la capacité de calcul accrue des grappes mises à niveau, notamment en raison de l'augmentation du nombre de CPU par nœud? Le changement le plus important touchera le traitement des données par GPU; le webinaire abordera ce sujet en détail. <br><br> Une période de questions sera réservée à la fin; n'hésitez pas à nous faire part de vos questions et préoccupations. | Utilisateurs potentiels des systèmes mis à niveau | webinaire; les enregistrements et le contenu des webinaires SHARCNET précédents sont disponibles sur [http://youtube.sharcnet.ca](http://youtube.sharcnet.ca). | Passé |
| Workflow Hacks for Large Datasets in HPC | Université Simon-Fraser / Groupe de l’IRN de la C.-B. | Alex Razoumov | mardi 20 mai 2025, 10 h HP | Au fil des ans, nous avons animé des webinaires sur des outils permettant d'améliorer considérablement les flux de travail comprenant de grands ensembles de données. Dans cette session, nous traiterons de certains de ces précieux outils :<ul><li>**Visualisation in situ** : permet le rendu interactif de grands tableaux en mémoire sans avoir à les stocker sur disque.</li><li>**Compression de données 3D avec perte** : réduit la taille des ensembles de données 3D jusqu'à 100 fois sans artefacts visibles, ce qui est idéal pour le stockage et l'archivage.</li><li>**Stockage distribué** : permet de gérer de grandes quantités de données sur plusieurs emplacements.</li><li>**DAR (Disk ARchhiver)** : alternative à TAR moderne et performante qui offre indexation, archivage différentiel et extraction plus rapide.</li></ul> | Utilisateurs qui travaillent avec de grands ensembles de données | webinaire ; <br>les enregistrements et le contenu des webinaires précédents sont disponibles sur [https://training.westdri.ca](https://training.westdri.ca). | Passé |
| [Maîtriser l'efficacité des GPU](https://training.sharcnet.ca/courses/enrol/index.php?id=210) (en anglais) | SHARCNET | Sergey Mashchenko | en tout temps | Ce cours en ligne que vous suivez à votre rythme offre une formation de base sur l'utilisation des GPU sur nos [systèmes nationaux](https://training.sharcnet.ca/courses/mod/glossary/showentry.php?eid=86&displayformat=dictionary). Les GPU modernes (tels que NVIDIA A100 et H100) sont des ressources massivement parallèles et très coûteuses. La plupart des tâches GPU ne sont pas en mesure d'utiliser ces GPU efficacement, soit en raison de la taille du problème trop petite pour saturer le GPU, soit en raison du modèle d'utilisation intermittent (en rafale) du GPU. Vous apprendrez à mesurer l'utilisation du GPU par vos tâches à utiliser les deux technologies NVIDIA - **MPS** (*Multi-Process Service*) et **MIG** (*Multi-Instance GPU*) pour améliorer l'utilisation du GPU. | Utilisatrices et utilisateurs potentiels des systèmes mis à niveau | Cours en ligne d'une heure avec certificat | [Accédez au cours ici (un compte avec l'Alliance est requis)](https://training.sharcnet.ca/courses/enrol/index.php?id=210) |
| Introduction to the Fir cluster (en anglais) | Université Simon-Fraser / West DRI | Alex Razoumov | 16 septembre 2025 | La nouvelle grappe Fir de l'Université Simon-Fraser est entrée en fonction en août 2025. Nous présenterons un aperçu de la grappe et de son matériel; les différents systèmes de fichiers et leur usage recommandé; les politiques de soumission des tâches; et les meilleures pratiques sur l'utilisation de la grappe | Utilisatrices et utilisateurs de la grappe [Fir](fir.md) | webinaire <br>Les enregistrements et le matériel des webinaires précédents se trouvent [West DRI – Démarrage (HPC)](https://training.westdri.ca/getting-started/#high-performance-computing). | Passé |
| [Guide de survie pour les futures mises à niveau des GPU](https://youtu.be/pxY3G3BhwyA) (en anglais) | SHARCNET | Sergey Mashchenko | EN LIGNE | Nos systèmes nationaux subiront des mises à niveau importantes dans les prochains mois. En particulier, les anciens GPU (P100, V100) seront remplacés par les nouveaux GPU H100 de NVIDIA. La puissance de calcul totale des GPU augmentera d'un facteur de 3,5, mais le nombre de GPU diminuera considérablement, passant de 3200 à 2100. Ceci posera un défi important, car la pratique habituelle consistant à utiliser un GPU entier pour chaque processus ou rang MPI ne sera plus possible dans la plupart des cas. Heureusement, NVIDIA propose deux technologies puissantes pour atténuer cette situation : **MPS** (Multi-Process Service) et **MIG** (Multi-Instance GPU). Nous discuterons de ces deux technologies et de la manière dont elles peuvent être utilisées sur nos grappes. Nous verrons comment déterminer l'approche qui fonctionnera le mieux pour un code particulier et une démonstration sera effectuée à la fin. | Utilisatrices et utilisateurs potentiels des systèmes mis à niveau, ou devant utiliser une quantité importante de ressources H100 (par exemple, plusieurs GPU à la fois et/ou pour plus de 24 heures d'exécution) | [vidéo](https://youtu.be/pxY3G3BhwyA) et [diapositives](https://helpwiki.sharcnet.ca/wiki/images/1/1d/MIG_MPS.pdf) (durée, 1 heure) | (présentation faite le 20 novembre 2024 de 12 h à 13 h) |

## Foire aux questions

### Mes données seront-elles migrées sur leur nouveau système?

La migration des données est la responsabilité de chacun des sites hôtes nationaux; vous recevrez l'information sur les actions à prendre.

### Mes fichiers seront-ils supprimés si le centre de données qui héberge mon système ferme pendant la transition?

Non, vos fichiers ne seront pas supprimés. Pendant les activités de renouvellement, chaque site hôte national migrera les données /project et /home du système de stockage existant vers le nouveau système de stockage quand il sera installé. Ces migrations se produisent généralement pendant les arrêts de services, mais les détails spécifiques peuvent varier selon le site. Chaque site hôte national vous informera de toute action susceptible d'avoir un effet sur vos travaux.
De plus, les systèmes de bandes pour les sauvegardes et les données /nearline ne sont pas remplacés, donc les sauvegardes et les données /nearline resteront inchangées.
Pour d'autres questions techniques, écrivez à [notre soutien technique](technical-support.md).

### Les arrêts de service sont-ils prévisibles?

Chacun des sites hôtes nationaux gère les arrêts de service qui seront requis pendant l'installation et la transition; ils seront rapportés sur [notre page web sur l'État des systèmes](https://status.alliancecan.ca). La présente page wiki sera modifiée au fur et à mesure que l'information est disponible et vous recevrez périodiquement par courriel des avis et des mises à jour.

### Qui peut répondre à mes questions sur la transition?

Le [soutien technique](technical-support.md) tentera de vous informer, mais il se peut que l'information ne leur soit pas encore connue.

### Les nouveaux systèmes sont-ils compatibles avec mes tâches et mes applications?

Règle générale, oui. Il est possible que certaines applications doivent être recompilées ou reconfigurées selon les nouveaux CPU et GPU. Vous recevrez l'information au fur et à mesure de la transition.

### Les logiciels sur les systèmes existants seront-ils toujours disponibles?

Oui, notre [environnement logiciel standard](standard-software-environments.md) sera disponible sur les nouveaux systèmes.

### Les logiciels commerciaux sous licence seront-ils migrés sur les nouveaux systèmes?

Oui. Dans la mesure du possible, vous aurez le même accès pour ce type d'application (Gaussian, AMS/ADF, etc.). Les fournisseurs pourraient modifier les conditions, mais le risque est faible. Nous vous informerons des cas susceptibles de se présenter.

### Les arrêts de service seront-ils échelonnés?

Nous ferons tout ce qui est possible pour limiter les arrêts de service qui se chevauchent, mais comme nous sommes très contraints par les calendriers de livraison et les délais de financement, il y aura probablement des périodes où plusieurs de nos systèmes seront hors ligne simultanément. Nous vous en informerons le plus tôt possible.

### Est-il possible d'acheter le matériel qui sera retiré de l'infrastructure?

La grande partie de l'équipement est la propriété des établissements hôtes qui s'en départissent selon les standards que chacun établit. En règle générale, le matériel est acheminé au recyclage. Contactez l'établissement hôte pour savoir s'il existe la possibilité de vous en procurer.