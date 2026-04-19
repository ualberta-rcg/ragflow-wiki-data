---
title: "Infrastructure renewal/fr"
slug: "infrastructure_renewal"
lang: "fr"

source_wiki_title: "Infrastructure renewal/fr"
source_hash: "dae20552ffbad1482492c8194e666b48"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:52:20.774541+00:00"

tags:
  []

keywords:
  - "technologies NVIDIA"
  - "retrait du matériel"
  - "infrastructure de calcul informatique de pointe"
  - "systèmes nationaux"
  - "compilation de codes"
  - "compatibilité des applications"
  - "renouvellement de l'infrastructure"
  - "soutien technique"
  - "OpenMP"
  - "SciNet et Trillium"
  - "MPI"
  - "grands ensembles de données"
  - "migration des données"
  - "mises à jour"
  - "grappe Fir"
  - "cours en ligne"
  - "migration de systèmes"
  - "services infonuagiques"
  - "Quotas pour le stockage"
  - "page wiki"
  - "mise hors service"
  - "utilisation du GPU"
  - "Multi-Instance GPU"
  - "Rorqual"
  - "arrêts de service"
  - "logiciels commerciaux"
  - "HPC Python"
  - "Migration des fichiers"
  - "nouveaux systèmes"
  - "utilisation des GPU"
  - "Multi-Process Service"
  - "calcul de haute performance"
  - "mise à niveau des GPU"
  - "Janvier 2026"
  - "utilisation de Slurm"
  - "formation autonome"
  - "transition"
  - "Fermeture des espaces de stockage"
  - "allocation de ressources"
  - "État des systèmes"
  - "grappe de calcul"

questions:
  - "Quels sont les principaux avantages apportés par le renouvellement de l'infrastructure de calcul informatique de pointe ?"
  - "Quels sont les nouveaux systèmes mis en place et quels anciens équipements remplacent-ils ?"
  - "Quelles actions spécifiques les utilisateurs doivent-ils entreprendre pour gérer la migration vers le nouveau nuage Arbutus et la fermeture définitive du système Béluga ?"
  - "Quel système remplace l'ancien et quelle est la politique concernant la réactivation de ce dernier ?"
  - "Quelles restrictions spécifiques seront appliquées aux quotas des espaces de stockage en janvier 2026 ?"
  - "De quel délai les utilisateurs disposent-ils pour effectuer l'extraction et la migration de leurs données ?"
  - "Quelles sont les dates de mise hors service des anciennes grappes de calcul et comment les utilisateurs doivent-ils gérer la transition de leurs données ?"
  - "De quelle manière la transition vers la nouvelle infrastructure nationale affectera-t-elle la disponibilité des allocations de ressources pour les chercheurs ?"
  - "Quels outils de formation et webinaires sont proposés pour aider les utilisateurs à se familiariser avec le calcul de haute performance sur les systèmes de l'Alliance ?"
  - "Quels sont les nouveaux noms des grappes de calcul suite à la mise à niveau des systèmes nationaux et comment les utilisateurs peuvent-ils s'y préparer ?"
  - "Quels outils spécifiques sont présentés pour optimiser les flux de travail et la gestion des grands ensembles de données en calcul haute performance ?"
  - "Quelles technologies permettent d'améliorer l'efficacité et l'utilisation des ressources GPU modernes, souvent sous-exploitées par les tâches standards ?"
  - "Quelles sont les technologies de calcul haute performance (HPC) et les langages de programmation présentés dans ce cours ?"
  - "Quelles compétences pratiques liées à l'utilisation de Slurm et à la gestion des tâches sur une grappe de calcul les participants vont-ils acquérir ?"
  - "À quel public s'adresse cette formation et sous quel format a-t-elle été dispensée ?"
  - "Quelles sont les raisons principales expliquant la sous-utilisation d'un GPU selon le texte ?"
  - "Quelles technologies NVIDIA le cours permet-il de maîtriser pour optimiser l'utilisation du GPU ?"
  - "Quelles sont les modalités pratiques du cours (public cible, durée, certification et conditions d'accès) ?"
  - "Quelles sont les caractéristiques, les systèmes de fichiers et les meilleures pratiques abordés lors de l'introduction à la nouvelle grappe Fir ?"
  - "Comment les technologies MPS et MIG de NVIDIA aideront-elles les utilisateurs à faire face à la réduction du nombre total de GPU lors des prochaines mises à niveau matérielles ?"
  - "Quelles sont les procédures prévues pour la migration et la conservation des données des utilisateurs lors des arrêts de service liés au renouvellement des systèmes ?"
  - "Où les problèmes survenant pendant l'installation et la transition seront-ils rapportés ?"
  - "Comment les utilisateurs seront-ils tenus informés des avis et des mises à jour concernant la situation ?"
  - "À qui faut-il s'adresser pour poser des questions sur la transition et pourquoi leurs réponses pourraient-elles être incomplètes ?"
  - "Comment la transition vers les nouveaux systèmes affectera-t-elle la compatibilité et la disponibilité des logiciels existants et commerciaux ?"
  - "Faut-il s'attendre à des interruptions de service simultanées lors de la mise en place de la nouvelle infrastructure ?"
  - "Quelle est la procédure à suivre pour tenter d'acquérir le matériel informatique qui sera retiré et remplacé ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Importante mise à jour de notre infrastructure de calcul informatique de pointe

Le renouvellement de notre infrastructure de calcul informatique de pointe s'est amorcé à l'hiver 2024-2025 et de nouveaux systèmes ont été mis en production au cours de 2025 jusqu'en début de 2026. Ces changements ont amélioré nos services de calcul de haute performance et nos services infonuagiques pour soutenir la recherche au Canada. Dans certains cas, les activités de migration et de mise hors service sont toujours en cours. Le contenu de la présente page sera mis à jour au fur et à mesure que les informations sont disponibles.

Le renouvellement de l'infrastructure a remplacé près de 80 % de nos équipements proches de leur fin de vie. Les nouveaux systèmes offriront une vitesse de traitement plus rapide, une plus grande capacité de stockage et une fiabilité améliorée.

## Documentation des systèmes

| **Documentation** | **Système remplacé** |
| :---------------- | :------------------- |
| [Arbutus](arbutus.md) | [nuage](../cloud/cloud.md) (aucun changement à cette infrastructure virtuelle) |
| [Rorqual](rorqual.md) | [Béluga](béluga.md) |
| [Fir](../software/fir.md) | [Cedar](cedar.md) |
| [Trillium](trillium.md) | Niagara et [Mist](../software/mist.md) |
| [Nibi](nibi.md) | [Graham](graham.md) |

## Capacité des systèmes, baisses et arrêts de services
Pendant l'installation et la transition vers les nouveaux systèmes, nous devrons sans doute suspendre ou diminuer les services en raison de contraintes d'alimentation électrique ou d'espace. 
Veuillez tenir compte de ces possibilités dans la planification de votre programme de recherche, des soutenances de thèse ou de mémoire, etc.

[Cliquez ici pour la liste des travaux terminés](infrastructure_renewal_completed_events.md).

| **Début** | **Fin** | **État** | **Système** | **Type** | **Description** |
| :-------- | :------ | :------- | :---------- | :------- | :-------------- |
| 2026-04-07 | 2026-08-31 | en cours | Arbutus | Mises à jour/ Migration | Le nouveau nuage Arbutus est maintenant en production et les ressources allouées par le concours pour 2026-2027 sont disponibles. <br><br> !!! note "Mesures à prendre" <br>     * Si vos allocations accordées suite au concours pour 2025-2026 ou allouées via le service d'accès rapide se trouvent sur le nuage d’avant les améliorations, vous avez la responsabilité de migrer vos ressources avant le 31 août 2026. <br>     * Les migrations peuvent commencer dès que vous aurez accès au nouveau nuage Arbutus. <br>     * Pendant la migration, les allocations accordées suite au concours resteront actives sur le nuage d’avant les améliorations. <br>     * Si vos allocations accordées via le service d’accès rapide se trouvent sur le nuage d’avant les améliorations, vous devez soumettre une demande à cloud@tech.alliancecan.ca pour que votre projet soit ajouté à la file d'attente de provisionnement pour le nouveau nuage. Le provisionnement se fera en lots; certains délais d'accès sont possibles. <br><br> !!! tip "Nouveautés" <br>     * La sécurité est renforcée par un processus d'authentification à signature unique (SSO, **single sign-on**) et l’authentification multifacteur. <br>     * À la connexion, sélectionnez *Authenticate using Digital Research Alliance of Canada*. <br><br> !!! info "Documentation" <br>     * [Migration vers Arbutus](https://docs.alliancecan.ca/wiki/Arbutus_Migration_Guide/fr) <br>     * [Authentification multifacteur](https://docs.alliancecan.ca/wiki/Multifactor_authentication/fr) <br><br> Accès via [Arbutus Cloud](https://arbutus.alliancecan.ca/) |
| 2026-01 | 2026-06-20 | en cours | Béluga | fermeture définitive | Le service de calcul **Béluga** a été remplacé par **Rorqual**; aucune restauration ni réactivation n'est prévue. <br><br> !!! warning "Fermeture des espaces de stockage" <br>     * **Janvier 2026** – Les quotas pour le stockage sur `/project`, `/home`, `/scratch` et `/nearline` seront diminués pour permettre uniquement la suppression ou l'archivage des données. Ceci laisse une période de six mois pour effectuer l'extraction et la migration des fichiers. <br>     * **2026-02-28** – Fermeture définitive du stockage sur `/scratch`. Les fichiers importants doivent être déplacés avant cette date. <br>     * **2026-06-20** – L'accès aux données ne sera plus possible. <br><br> !!! note "Remarque" <br>     Le nuage Béluga (``beluga-cloud``) est une infrastructure distincte et ne sera pas touchée par la fermeture définitive de la grappe de calcul Béluga. |
| 2025-09-30 | 2025-09-30 | terminé | Niagara | mise hors service | La grappe Niagara a été fermée définitivement le 30 septembre 2025. <br><br> Pour des détails sur la transition, voir [Transition de Niagara vers Trillium](transition_from_niagara_to_trillium.md). |
| 2025-09-16 | 2025-09-30 | terminé | Mist | mise hors service | La grappe Mist a été fermée définitivement le 16 septembre 2025. <br><br> Pour vos nouveaux travaux, veuillez utiliser Trillium (voir [Trillium : Guide de démarrage](trillium_quickstart.md)). |
| 2025-09-12 | 2025-09-12 | terminé | Cedar | mise hors service | La grappe Cedar a été fermée définitivement le 12 septembre 2025. <br><br> **Accès aux données** <br> Les fichiers stockés sur Cedar sont disponibles sur Fir puisque les deux grappes partagent les mêmes systèmes de fichiers; aucune action n'est requise de votre part. <br><br> À compter du 12 septembre, veuillez soumettre vos tâches sur une autre grappe de notre [nouvelle infrastructure nationale](national_systems.md), y compris Fir. |
| 2025-09-01 | 2025-09-02 | terminé | Graham | mise hors service | La grappe Graham a été fermée définitivement le 1er septembre 2025. <br><br> **Accès aux données** <br> Les fichiers stockés sur Graham sont aussi disponibles sur Nibi puisque les deux grappes partagent les mêmes systèmes de fichiers; aucune action n'est requise de votre part. <br><br> À compter du 1er septembre, veuillez soumettre vos tâches sur une autre grappe de notre [nouvelle infrastructure nationale](national_systems.md), y compris Nibi. |

## Concours pour l'allocation de ressources
[Le concours pour l'allocation de ressources](https://www.alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources) sera touché par cette transition. Toutefois, le processus pour soumettre une demande reste inchangé. Toutes les allocations 2025-2026 seront disponibles une fois que toutes les grappes seront en service. 
Pour la plupart, les grappes qui seront remplacées cesseront d'être disponibles avant que toutes les nouvelles grappes soient en fonction. Si vous avez à la fois des allocations 2024 et des allocations 2025, il y aura une période pendant laquelle vous n'aurez accès à aucune ressource. Cependant, vous pourrez utiliser votre allocation par défaut (``def-xxxxxx``) sur une nouvelle grappe dès sa mise en service. Rappelons que les allocations 2025 ne seront disponibles que lorsque toutes les nouvelles grappes sont en service.

## Outils de formation

D'autres ressources de formation sont disponibles via [Explora](https://explora.alliancecan.ca).

| **Titre** | **Organisation** | **Présenté par** | **Date** | **Description** | **Public cible** | **Format** | **Inscription** |
| :-------- | :--------------- | :---------------- | :------- | :-------------- | :--------------- | :--------- | :-------------- |
| Introduction to HPC on Alliance Clusters (en trois parties de 2 heures chacune) | Université Simon-Fraser/Groupe de l’IRN de la C.-B. | Alex Razoumov | Les jeudis 25 septembre, 2 octobre et 9 octobre, 10h HP | Introduction au calcul de haute performance sur les grappes de l'Alliance : matériel; outils et logiciels; coup d'œil sur `OpenMP`, `MPI`, `HPC Python` (**Dask**, **Ray**), `Chapel`, `Julia`; compilation de codes séquentiels/partagés/distribués; utilisation de `Slurm` (en lots et interactivement), étalonnage (**benchmarking**), soumission de plusieurs tâches, estimation des ressources nécessaires, gestion des permissions. Inclut des démos et des exercices pratiques sur une grappe de formation. | Utilisatrices et utilisateurs nouveaux ou potentiels | webinaires (3 parties de 2 heures chacune) | Passé |
| [HPC105: Intro to SciNet and Trillium](https://education.scinet.utoronto.ca/enrol/index.php?id=1389) | SciNet | Équipe de formation SciNet | en tout temps (mise à jour le 25 août 2025) | Formation autonome sur les systèmes de SciNet (Trillium) : configuration de votre compte, première connexion, exécution de tâches de calcul. Pour les utilisatrices et utilisateurs de Niagara et Mist, cette formation montre comment migrer vers [Trillium](trillium.md). | Utilisatrices et utilisateurs potentiels de [Trillium](trillium.md) et nouveaux utilisateurs et utilisatrices de SciNet | Formation autonome en ligne (environ 4 heures) | [Cliquez ici pour commencer la formation/ Vous devez détenir un compte avec l'Alliance dans CCDB](https://education.scinet.utoronto.ca/enrol/index.php?id=1389). |
| [Migrating to the upgraded national systems](https://youtu.be/nRX8zTIVEXk) | SHARCNET | Sergey Mashchenko | Mercredi 30 juillet 2025, 12h HAE | La plupart des systèmes nationaux de l'Alliance ont connu une mise à niveau majeure au cours du printemps et de l'été. Ils ont été reconstruits de A à Z avec du matériel moderne, ce qui a augmenté considérablement la capacité de calcul, de mémoire et de stockage. Les grappes mises à niveau ont de nouveaux noms : Graham est devenue Nibi, Béluga est devenue Rorqual, Cedar est devenue Fir, Niagara est devenue Trillium. La grappe Narval n'a pas été modifiée. Certains des systèmes mis à niveau sont déjà en ligne, mais pas encore à pleine capacité. Il est prévu de les rendre tous disponibles d'ici la fin juillet.<br><br>Ce webinaire veut répondre aux préoccupations et aux questions des utilisateurs des systèmes existants. Quel sera l'impact des mises à niveau sur mon flux de travail? Y a-t-il des changements significatifs dans la planification des tâches et des systèmes de fichiers? Comment optimiser la capacité de calcul accrue des grappes mises à niveau, notamment en raison de l'augmentation du nombre de CPU par nœud? Le changement le plus important touchera le traitement des données par GPU; le webinaire abordera ce sujet en détail. <br><br>Une période de questions sera réservée à la fin; n'hésitez pas à nous faire part de vos questions et préoccupations. | Utilisateurs potentiels des systèmes mis à niveau | webinaire; les enregistrements et le contenu des webinaires SHARCNET précédents sont disponibles sur [http://youtube.sharcnet.ca](http://youtube.sharcnet.ca). | Passé |
| Workflow Hacks for Large Datasets in HPC | Université Simon-Fraser /Groupe de l’IRN de la C.-B. | Alex Razoumov | Mardi 20 mai 2025, 10h HP | Au fil des ans, nous avons animé des webinaires sur des outils permettant d'améliorer considérablement les flux de travail comprenant de grands ensembles de données. Dans cette session, nous traiterons de certains de ces précieux outils :<br>    * **Visualisation in situ :** permet le rendu interactif de grands tableaux en mémoire sans avoir à les stocker sur disque.<br>    * **Compression de données 3D avec perte :** réduit la taille des ensembles de données 3D jusqu'à 100 fois sans artefacts visibles, ce qui est idéal pour le stockage et l'archivage.<br>    * **Stockage distribué :** permet de gérer de grandes quantités de données sur plusieurs emplacements.<br>    * **DAR (Disk ARchhiver) :** alternative à TAR moderne et performante qui offre indexation, archivage différentiel et extraction plus rapide. | Utilisateurs qui travaillent avec de grands ensembles de données | webinaire ; <br> les enregistrements et le contenu des webinaires précédents sont disponibles sur [https://training.westdri.ca](https://training.westdri.ca). | Passé |
| [Mastering GPU Efficiency](https://training.sharcnet.ca/courses/enrol/index.php?id=210) (en anglais) | SHARCNET | Sergey Mashchenko | en tout temps | Ce cours en ligne que vous suivez à votre rythme offre une formation de base sur l'utilisation des GPU sur nos [systèmes nationaux](https://training.sharcnet.ca/courses/mod/glossary/showentry.php?eid=86&displayformat=dictionary). Les GPU modernes (tels que `NVIDIA A100` et `H100`) sont des ressources massivement parallèles et très coûteuses. La plupart des tâches GPU ne sont pas en mesure d'utiliser ces GPU efficacement, soit en raison de la taille du problème trop petite pour saturer le GPU, soit en raison du modèle d'utilisation intermittent (en rafale) du GPU. Vous apprendrez à mesurer l'utilisation du GPU par vos tâches à utiliser les deux technologies NVIDIA - MPS (**Multi-Process Service**) et MIG (**Multi-Instance GPU**) pour améliorer l'utilisation du GPU. | Utilisatrices et utilisateurs potentiels des systèmes mis à niveau | Cours en ligne d'une heure avec certificat | [Accédez au cours ici (un compte avec l'Alliance est requis)](https://training.sharcnet.ca/courses/enrol/index.php?id=210) |
| Introduction to the Fir cluster (en anglais) | Université Simon-Fraser / West DRI | Alex Razoumov | 16 septembre 2025 | La nouvelle grappe Fir de l'Université Simon-Fraser est entrée en fonction en août 2025. Nous présenterons un aperçu de la grappe et de son matériel; les différents systèmes de fichiers et leur usage recommandé; les politiques de soumission des tâches; et les meilleures pratiques sur l'utilisation de la grappe | Utilisatrices et utilisateurs de la grappe [Fir](../software/fir.md) | webinaire <br> Les enregistrements et le matériel des webinaires précédents se trouvent [West DRI – Getting Started (HPC)](https://training.westdri.ca/getting-started/#high-performance-computing). | Passé |
| [Survival guide for the upcoming GPU upgrades](https://youtu.be/pxY3G3BhwyA) (en anglais) | SHARCNET | Sergey Mashchenko | EN LIGNE | Nos systèmes nationaux subiront des mises à niveau importantes dans les prochains mois. En particulier, les anciens GPU (`P100`, `V100`) seront remplacés par les nouveaux GPU `H100` de NVIDIA. La puissance de calcul totale des GPU augmentera d'un facteur de 3,5, mais le nombre de GPU diminuera considérablement, passant de 3200 à 2100. Ceci posera un défi important, car la pratique habituelle consistant à utiliser un GPU entier pour chaque processus ou rang `MPI` ne sera plus possible dans la plupart des cas. Heureusement, NVIDIA propose deux technologies puissantes pour atténuer cette situation : MPS (**Multi-Process Service**) et MIG (**Multi-Instance GPU**). Nous discuterons de ces deux technologies et de la manière dont elles peuvent être utilisées sur nos grappes. Nous verrons comment déterminer l'approche qui fonctionnera le mieux pour un code particulier et une démonstration sera effectuée à la fin. | Utilisatrices et utilisateurs potentiels des systèmes mis à niveau, ou devant utiliser une quantité importante de ressources `H100` (par exemple, plusieurs GPU à la fois et/ou pour plus de 24 heures d'exécution) | [vidéo](https://youtu.be/pxY3G3BhwyA) et [diapositives](https://helpwiki.sharcnet.ca/wiki/images/1/1d/MIG_MPS.pdf) (durée, 1 heure) | (présentation faite le 20 novembre 2024 de 12h à 13h) |

## Foire aux questions

### Mes données seront-elles migrées sur leur nouveau système?
La migration des données est la responsabilité de chacun des sites hôtes nationaux; vous recevrez l'information sur les actions à prendre.

### Mes fichiers seront-ils supprimés si le centre de données qui héberge mon système ferme pendant la transition?
Non, vos fichiers ne seront pas supprimés. Pendant les activités de renouvellement, chaque site hôte national migrera les données `/project` et `/home` du système de stockage existant vers le nouveau système de stockage quand il sera installé. Ces migrations se produisent généralement pendant les arrêts de services, mais les détails spécifiques peuvent varier selon le site. Chaque site hôte national vous informera de toute action susceptible d'avoir un effet sur vos travaux.
De plus, les systèmes de bandes pour les sauvegardes et les données `/nearline` ne sont pas remplacés, donc les sauvegardes et les données `/nearline` resteront inchangées.
Pour d'autres questions techniques, écrivez à [notre soutien technique](../support/technical_support.md).

### Les arrêts de service sont-ils prévisibles?
Chacun des sites hôtes nationaux gère les arrêts de service qui seront requis pendant l'installation et la transition; ils seront rapportés sur [notre page web sur l'État des systèmes](https://status.alliancecan.ca). La présente page wiki sera modifiée au fur et à mesure que l'information est disponible et vous recevrez périodiquement par courriel des avis et des mises à jour.

### Qui peut répondre à mes questions sur la transition?
Le [soutien technique](../support/technical_support.md) tentera de vous informer, mais il se peut que l'information ne leur soit pas encore connue.

### Les nouveaux systèmes sont-ils compatibles avec mes tâches et mes applications?
Règle générale, oui. Il est possible que certaines applications doivent être recompilées ou reconfigurées selon les nouveaux CPU et GPU. Vous recevrez l'information au fur et à mesure de la transition.

### Les logiciels sur les systèmes existants seront-ils toujours disponibles?
Oui, notre [environnement logiciel standard](../programming/standard_software_environments.md) sera disponible sur les nouveaux systèmes.

### Les logiciels commerciaux sous licence seront-ils migrés sur les nouveaux systèmes?
Oui. Dans la mesure du possible, vous aurez le même accès pour ce type d'application (Gaussian, AMS/ADF, etc.). Les fournisseurs pourraient modifier les conditions, mais le risque est faible. Nous vous informerons des cas susceptibles de se présenter.

### Les arrêts de service seront-ils échelonnés?
Nous ferons tout ce qui est possible pour limiter les arrêts de service qui se chevauchent, mais comme nous sommes très contraints par les calendriers de livraison et les délais de financement, il y aura probablement des périodes où plusieurs de nos systèmes seront hors ligne simultanément. Nous vous en informerons le plus tôt possible.

### Est-il possible d'acheter le matériel qui sera retiré de l'infrastructure?
La grande partie de l'équipement est la propriété des établissements hôtes qui s'en départissent selon les standards que chacun établit. En règle générale, le matériel est acheminé au recyclage. Contactez l'établissement hôte pour savoir s'il existe la possibilité de vous en procurer.