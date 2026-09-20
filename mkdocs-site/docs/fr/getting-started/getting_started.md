---
title: "Getting started/fr"
slug: "getting_started"
lang: "fr"

source_wiki_title: "Getting started/fr"
source_hash: "9706bce48eb0108c3ff4bb3be2a8ac02"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:42:56.414278+00:00"

tags:
  []

keywords:
  - "puissance"
  - "besoins en mémoire"
  - "Vulcan"
  - "tâches parallèles intensives"
  - "logiciels sous licence"
  - "tamIA"
  - "recherche en IA"
  - "compte CCDB"
  - "temps"
  - "activités de formation"
  - "Killarney"
  - "grappes d'usage général"
  - "soutien technique"
  - "systèmes disponibles"
  - "grappe"
  - "environnement infonuagique"
  - "authentification multifacteur"

questions:
  - "Comment créer un compte CCDB et activer l’authentification multifacteur ?"
  - "Quels systèmes de calcul (grappes, cloud, etc.) sont proposés par le CCDB et comment y accéder ?"
  - "Où trouver les guides pour se connecter via SSH, transférer des données, installer des logiciels (Python, R) et utiliser les services comme Globus ou le cloud ?"
  - "Quels critères (logiciels, licences, automatisation, compatibilité Linux, besoins en mémoire, puissance, stockage, bande passante, fréquence d’exécution) devez‑vous préciser pour identifier le système de calcul le plus adapté à vos besoins ?"
  - "Quelles formations et ateliers (en ligne ou en présentiel) sont proposés par les partenaires régionaux tels que WestDRI, SHARCNET, SciNet, Calcul Québec et ACENET, et comment y accéder ?"
  - "Comment contacter le soutien technique pour obtenir de l’aide dans l’évaluation de vos besoins et la sélection des ressources appropriées ?"
  - "Quels types de tâches parallèles intensives le système décrit est‑il capable de gérer, et combien de cœurs sont requis pour ces tâches ?"
  - "Quelles sont les grappes mentionnées (Killarney, tamIA et Vulcan) et à quel environnement de calcul pan‑canadien pour l’intelligence artificielle (ECPIA) appartiennent‑elles ?"
  - "Quel est le but principal de ces grappes au sein de la recherche en intelligence artificielle ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Que voulez-vous faire?

*   Si vous ne possédez pas de compte, voyez
    *   [Demander un compte CCDB](apply_for_a_ccdb_account.md)
    *   [Authentification multifacteur](multifactor_authentication.md)
    *   [Foire aux questions sur le portail CCDB](frequently_asked_questions_about_the_ccdb.md)
*   Si vous avez de l'expérience en CHP et que vous voulez vous connecter à une grappe, vous voudrez savoir
    *   quels sont les [systèmes disponibles](getting_started.md#quels-sont-les-systèmes-disponibles) et comment vous y connecter;
    *   quels sont les [logiciels disponibles](../programming/available_software.md);
    *   comment [utiliser les modules](../programming/utiliser_des_modules.md);
    *   comment [soumettre une tâche](../running-jobs/running_jobs.md);
    *   comment les [systèmes de fichiers](../storage-and-data/storage_and_file_management.md) sont organisés.
*   Pour vous initier au CHP
    *   apprenez comment vous [connecter à nos grappes de CHP via SSH](ssh.md);
    *   lisez cette [introduction à Linux](linux_introduction.md);
    *   voyez comment [transférer des données](transferring_data.md), soit vers nos systèmes, soit en provenance de ceux-ci.
*   Pour connaître les ressources qui sont disponibles pour une discipline particulière, consultez les guides spécialisés:
    *   [Intelligence artificielle et apprentissage machine](../software/ai-ml/ai_and_machine_learning.md)
    *   [Bio-informatique](../software/bioinformatics/bioinformatics.md)
    *   [Simulation biomoléculaire](../software/molecular-sim/biomolecular_simulation.md)
    *   [Chimie computationnelle](../software/chemistry/computational_chemistry.md)
    *   [Mécanique des fluides numérique](../programming/computational_fluid_dynamics.md)
    *   [Systèmes d'information géographique](../software/gis.md)
    *   [Visualisation](../software/visualization.md)
*   Si vous avez des centaines de gigaoctets de données à transférer entre les serveurs, lisez à propos du [service de transfert Globus](globus.md).
*   Apprenez à installer des modules Python dans un environnement virtuel en lisant la page [Python](../software/python.md), sections *Créer et utiliser un environnement virtuel* et suivantes.
*   Apprenez à [installer des paquets R](../software/r.md).
*   Pour utiliser des logiciels qui ne sont pas conçus pour fonctionner sur nos grappes de CHP, vous pourriez utiliser l'[environnement infonuagique](../cloud/cloud.md).

Pour toute autre question, vous pouvez utiliser le champ de recherche dans le coin supérieur droit de la présente page, consulter [notre documentation technique](../general/technical_documentation.md) ou encore [nous joindre par courriel](../support/technical_support.md).

## Mot de passe et nom d'utilisateur

Votre **mot de passe** pour vous connecter est le même que celui que vous utilisez pour [vous connecter au portail CCDB](https://ccdb.alliancecan.ca/). Votre nom d'utilisateur est affiché en haut de la page d'accueil du portail CCDB.

## Quels sont les systèmes disponibles?

Vous pouvez accéder aux systèmes que vous souhaitez utiliser en vous rendant dans le portail [CCDB](https://ccdb.alliancecan.ca/me/access_systems). Une fois connecté, sous l'onglet *Ressources*, cliquez sur *Accès aux systèmes* pour demander la permission.

*   [Arbutus](../cloud/cloud_resources.md#nuage-arbutus) est un nuage pour configurer et exécuter des instances virtuelles. Pour savoir comment y accéder, voyez [Service infonuagique](../cloud/cloud.md).
*   [Fir](../software/fir.md), [Narval](../clusters/narval.md), [Nibi](../clusters/nibi.md) et [Rorqual](../clusters/rorqual.md) sont des **grappes d'usage général** (*superordinateurs*) qui sont composées de différents types de nœuds, incluant des nœuds à grande mémoire et des nœuds avec des accélérateurs comme les GPU.
*   [Trillium](../clusters/trillium.md) est une grappe homogène (*superordinateur*) conçue pour les **tâches parallèles intensives** (>1000 cœurs).
*   [Killarney](../clusters/killarney.md), [tamIA](../clusters/tamia.md) et [Vulcan](../clusters/vulcan.md) sont des grappes de l'Environnement de calcul pan-canadien pour l'intelligence artificielle [(ECPIA)](https://www.alliancecan.ca/fr/nos-services/calcul-informatique-de-pointe/environnement-de-calcul-pan-canadien-pour-lintelligence-artificielle-ecpia) et sont conçues pour la **recherche en IA**.

Pour désigner un superordinateur, nous privilégions le terme *grappe* qui représente mieux l'architecture de nos systèmes; plusieurs ordinateurs distincts (*nœuds*) forment une unité semblable à une grappe.

### Quels sont les systèmes qui répondent à mes besoins?

Répondre à cette question n'est pas facile puisqu'ils peuvent subvenir à un large éventail de besoins. Si vous avez besoin de clarifications, n'hésitez pas à communiquer avec le [soutien technique](../support/technical_support.md).

Les questions suivantes nous aideront à identifier les ressources pertinentes :
*   Quels sont les logiciels que vous voulez utiliser?
    *   Les logiciels doivent-ils être sous licence commerciale?
    *   Les logiciels peuvent-ils opérer sans l'intervention d'un utilisateur? Peuvent-ils être contrôlés par un fichier de commandes ou faut-il passer par une interface graphique?
    *   Les logiciels peuvent-ils fonctionner sous Linux?
*   Pour une tâche type, quels sont les besoins en mémoire, temps, puissance de traitement, accélération, espace de stockage, bande passante sur le réseau, etc.? (fournir une estimation)
*   À quelle fréquence ce type de tâche sera-t-il exécuté?

Si vous ne connaissez pas les réponses à ces questions, notre équipe technique peut vous guider et vous indiquer les ressources appropriées.

## Quelles sont les activités de formation?

La plupart des ateliers sont organisés par nos partenaires régionaux; ils sont offerts en ligne ou en personne et pour tous les niveaux d'expertise.

*   WestDRI (Colombie-Britannique et provinces des Prairies)
    *   [Site web des ressources de formation](https://training.westdri.ca), consultez la section *Upcoming sessions* ou explorez le menu de navigation en haut de la page
    *   [Bootcamps RCG de l'UAlberta](https://www.ualberta.ca/information-services-and-technology/research-computing/bootcamps.html)
*   [SHARCNET](https://www.sharcnet.ca/) (Ontario)
    *   [Calendrier](https://www.sharcnet.ca/my/news/calendar)
    *   [Chaîne YouTube](http://youtube.sharcnet.ca/)
    *   [Ateliers en ligne](https://training.sharcnet.ca/)
*   [SciNet](https://www.scinethpc.ca/) (Ontario)
    *   [Site de formation](https://education.scinet.utoronto.ca)
    *   [Chaîne YouTube](https://www.youtube.com/c/SciNetHPCattheUniversityofToronto)
*   [Calcul Québec](https://www.calculquebec.ca/fr/) (Québec)
    *   [Événements](https://calculquebec.eventbrite.ca/)
    *   [Formation](https://www.calculquebec.ca/services-aux-chercheurs/formation/)
*   [ACENET](https://www.ace-net.ca/) (provinces de l'Atlantique)
    *   [Formation](https://www.ace-net.ca/training.html)
    *   [Chaîne YouTube](https://www.youtube.com/@ACENETDRI)
Voir aussi la liste des [événements de formation sur Explora](https://explora.alliancecan.ca/events).