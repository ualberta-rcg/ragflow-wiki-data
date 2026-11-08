---
title: "Technical documentation/fr"
slug: "technical_documentation"
lang: "fr"

source_wiki_title: "Technical documentation/fr"
source_hash: "a82d11078a19d82e1e2a7d7d4f08998b"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T03:02:17.151163+00:00"

tags:
  []

keywords:
  - "Mécanique des fluides numérique"
  - "Partenaires et services régionaux"
  - "Visualisation"
  - "Systèmes d'information géographique"
  - "Sciences humaines et sociales"
  - "Obtenir du soutien technique"
  - "services infonuagiques"
  - "guides d'utilisation"
  - "Tutoriels de formation autonome"
  - "logiciels disponibles"
  - "Bio-informatique"
  - "Alliance de recherche numérique du Canada"
  - "grappes de calcul"
  - "Intelligence artificielle et apprentissage machine"
  - "Gestion des données de recherche"

questions:
  - "Quels sont les systèmes de calcul nationaux actuellement disponibles et leurs principales caractéristiques ?"
  - "Quels services de stockage, de transfert de données et de cloud sont proposés par l’Alliance ?"
  - "Où peut‑on accéder aux guides d’utilisation et aux ressources d’apprentissage pour les différents systèmes et domaines spécialisés ?"
  - "Quels domaines de recherche sont listés dans le texte ?"
  - "Quels partenaires régionaux et services de formation sont mentionnés pour le calcul scientifique au Canada ?"
  - "Où peut‑on trouver les ressources de formation et les plateformes de calcul avancées indiquées dans le texte ?"
  - "Quels types de ressources d’apprentissage autonome sont proposés dans la section « Tutoriels de formation autonome » ?"
  - "Comment accéder aux guides spécialisés en intelligence artificielle, bio‑informatique, simulation biomoléculaire et chimie computationnelle ?"
  - "Quels services de soutien technique sont offerts aux utilisateurs de ces ressources ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**Bienvenue sur le site de documentation technique de l'Alliance de recherche numérique du Canada (l'Alliance).** Vous trouverez ici l'information relative aux équipements et services nationaux de l'Alliance.

Pour les renseignements sur les équipements et services gérés par nos partenaires régionaux, utilisez les liens de la section *Partenaires et services régionaux* ci-dessous.

!!! note
    Le contenu de ce site se développe de manière évolutive et il est possible que certains liens conduisent à des pages semblables à celle-ci, pour lesquelles le contenu n'est pas encore publié. Le maintien de la documentation est un effort continuel de la part de nos équipes techniques qui veillent à l'enrichir et à l'améliorer; cependant, tous nos utilisateurs sont invités à y collaborer.

## Systèmes et services

### Systèmes

*   [Renouvellement d'infrastructure](../clusters/infrastructure_renewal.md) en 2025
*   **[Grappes d'usage général](../clusters/national_systems.md)**, pour des tâches sur processeur (CPU) ou sur processeur graphique (GPU)
    *   [Fir](../software/fir.md), [Nibi](../clusters/nibi.md), [Narval](../clusters/narval.md) et [Rorqual](../clusters/rorqual.md)
*   [Trillium](../clusters/trillium.md), grappe conçue pour les tâches parallèles intensives
*   Grappes de traitement graphique (GPU), qui font partie de l'Environnement de calcul pan-canadien pour l'intelligence artificielle (ECPIA) :
    *   [Killarney](../clusters/killarney.md), [tamIA](../clusters/tamia.md), [Vulcan](../clusters/vulcan.md)
*   Grappes obsolètes, en fin de vie ou retirées :
    *   [Béluga](../clusters/béluga.md), [Cedar](../clusters/cedar.md), [Graham](../clusters/graham.md), [Niagara](../clusters/national_systems.md)

### Services

*   [Logiciels disponibles](../programming/available_software.md)
*   **[Service infonuagique](../cloud/cloud.md)**
*   [Serveurs de bases de données](../cloud/database_servers.md)
*   [Transfert de fichiers avec Globus](../getting-started/globus.md)
*   [Nextcloud](../cloud/nextcloud.md), stockage infonuagique
*   **[Gestion des données de recherche](https://alliancecan.ca/fr/services/gestion-des-donnees-de-recherche)**
*   **[Logiciels de recherche](https://alliancecan.ca/fr/services/logiciels-de-recherche)**
*   [Services d'informatique quantique](../software/quantum/services_d_informatique_quantique.md)

L'état des services et grappes de calcul est disponible sur ce [site](https://status.alliancecan.ca/).
FAQ : [Foire aux questions](../getting-started/frequently_asked_questions.md)

## Guides d'utilisation

*   **[Guide de démarrage](../getting-started/getting_started.md)**
    *   [Introduction aux nouveaux systèmes nationaux (série de courtes vidéos)](https://docs.computecanada.ca/wiki/Getting_Started_with_the_new_National_Systems/fr)
    *   [Guide de démarrage pour Trillium](../clusters/trillium_quickstart.md)
    *   [Nuage : Guide de démarrage](../cloud/cloud_quick_start.md)
    *   [Comment se connecter avec SSH](../getting-started/ssh.md)
    *   [Introduction à Linux](../getting-started/linux_introduction.md)
*   [Stockage et gestion de fichiers](../storage-and-data/storage_and_file_management.md)
    *   [Transfert de données](../getting-started/transferring_data.md)
    *   [Espace *scratch* : Purge automatique](../storage-and-data/scratch_purging_policy.md)
*   [Directives pour la migration de vos données](../clusters/general_directives_for_migration.md)
*   [Utiliser les modules](../programming/utiliser_des_modules.md) et les [environnements logiciels standards](../programming/standard_software_environments.md) pour accéder aux logiciels
*   **[Exécuter des tâches](../running-jobs/running_jobs.md)**
*   [Installation de logiciels dans votre espace personnel (home)](../getting-started/installing_software_in_your_home_directory.md)
*   [Guide de programmation](../programming/programming_guide.md)
*   [Tutoriels de formation autonome](../support/self-paced_courses.md)
*   [Visualisation](../software/visualization.md)
*   [Obtenir du soutien technique](../support/technical_support.md)

## Guides spécialisés

*   [Intelligence artificielle et apprentissage machine](../software/ai-ml/ai_and_machine_learning.md)
*   [Bio-informatique](../software/bioinformatics/bioinformatics.md)
*   [Simulation biomoléculaire](../software/molecular-sim/biomolecular_simulation.md)
*   [Chimie computationnelle](../software/chemistry/computational_chemistry.md)
*   [Mécanique des fluides numérique](../programming/computational_fluid_dynamics.md)
*   [Systèmes d'information géographique](../software/gis.md)
*   [Sciences humaines et sociales](../getting-started/humanities_and_social_sciences.md)
*   [Gestion des données de recherche](../storage-and-data/research_data_management.md)
*   [Physique subatomique](../software/chemistry/subatomicphysics.md)

## Partenaires et services régionaux

*   [Formation Western](https://training.westdri.ca/)
    *   [Formation UAlberta](https://www.ualberta.ca/information-services-and-technology/research-computing/bootcamps.html)
*   [SHARCNET](https://sharcnet.ca)
*   [SciNet](https://docs.scinet.utoronto.ca/index.php/Main_Page)
*   [Centre de calcul avancé](https://info.cac.queensu.ca/wiki/)
*   [Calcul Québec](https://www.calculquebec.ca/)
*   [ACENET](https://www.ace-net.ca/)
    *   [ACENET, Formation](https://www.acenet.training/)
    *   [ACENET, Wiki technique](https://wiki.ace-net.ca/)