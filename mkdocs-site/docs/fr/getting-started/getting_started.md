---
title: "Getting started/fr"
tags:
  []

keywords:
  []
---

## Que voulez-vous faire?
* Si vous ne possédez pas de compte, voyez
** [Demander un compte CCDB](apply_for_a_ccdb_account-fr.md)
** [Authentification multifacteur](multifactor-authentication-fr.md)
** [Foire aux questions sur le portail CCDB](frequently-asked-questions-about-the-ccdb-fr.md).
* Si vous avez de l'expérience en CHP et que vous voulez vous connecter à une grappe, vous voudrez savoir
** quels sont les [systèmes disponibles](getting-started-fr#quels_sont_les_systèmes_disponibles?.md);
** quels sont les [logiciels disponibles](available-software-fr.md);
** comment [utiliser les modules](utiliser-des-modules.md);
** comment [soumettre une tâche](running_jobs-fr.md);
** comment les [systèmes de fichiers](storage-and-file-management-fr.md) sont organisés.
* Pour vous initier au CHP
** apprenez comment vous [connecter à nos grappes de CHP via SSH](ssh-fr.md) ;
** lisez cette [introduction à Linux](linux-introduction-fr.md);
** voyez comment [transférer des données](transferring-data-fr.md), soit vers nos systèmes, soit en provenance de ceux-ci.
* Pour connaître les ressources qui sont disponibles pour une discipline particulière, consultez les guides spécialisés&nbsp;:
** [Intelligence artificielle et apprentissage machine](ai-and-machine-learning-fr.md)
** [Bio-informatique](bioinformatics-fr.md)
** [Simulation biomoléculaire](biomolecular-simulation-fr.md)
** [Chimie computationnelle](computational-chemistry-fr.md)
** [Mécanique des fluides numérique](computational-fluid-dynamics-fr.md)
** [Systèmes d'information géographique](gis-fr.md)
** [Visualisation](visualization-fr.md)
* Si vous avez des centaines de gigaoctets de données à transférer entre les serveurs, lisez à propos du [service de transfert Globus](globus-fr.md).
* Apprenez à installer des modules Python dans un environnement virtuel en lisant la page [Python](python-fr.md), sections <i>Créer et utiliser un environnement virtuel</i> et suivantes.
* Apprenez à [installer des paquets R](r-fr.md).
* Pour utiliser des logiciels qui ne sont pas conçus pour fonctionner sur nos grappes de CHP, vous pourriez utiliser l'[environnement infonuagique](cloud-fr.md).

Pour toute autre question, vous pouvez utiliser le champ de recherche dans le coin supérieur droit de la présente page, consulter [notre documentation technique](technical-documentation-fr.md) ou encore [nous joindre par courriel](technical-support-fr.md).

## Mot de passe et nom d'utilisateur
Votre <b>mot de passe</b> pour vous connecter est le même que celui que vous utilisez pour  [vous connecter à CCDB](https://ccdb.alliancecan.ca/). Votre nom d'utilisateur est affiché au haut de la page d'accueil CCDB.

<span id="What_systems_are_available?"></span>
## Quels sont les systèmes disponibles?

[alt=Screenshot of the "Access Systems" page in CCDB|thumb|500x500px|Dans CCDB, sous l'onglet *Ressources*, cliquez sur *Accès aux systèmes*.](file:access-systems-fr.png.md)

Vous pouvez [demander la permission d'accès](https://ccdb.alliancecan.ca/me/access_systems) à un ou plusieurs de nos systèmes&nbsp;: [Arbutus](cloud-resources-fr.md), [Fir](fir-fr.md), [Narval](narval.md), [Nibi](nibi-fr.md), [Rorqual](rorqual.md) et [Trillium](trillium-fr.md).

* [Arbutus](cloud-resources-fr#nuage_arbutus.md) est un nuage pour configurer et exécuter des instances virtuelles. Pour savoir comment y accéder, voyez [Service infonuagique](cloud-fr.md). 

* Les grappes d'usage général (superordinateurs) [Fir](fir-fr.md), [Narval](narval.md), [Nibi](nibi-fr.md) et [Rorqual](rorqual.md) comportant divers types de nœuds dont certains à large mémoire et d'autres avec accélérateurs comme des GPU. Pour vous y connecter, utilisez [SSH](ssh-fr.md). Un répertoire personnel (/home) est automatiquement créé quand vous vous connectez pour la première fois.

* [Trillium](trillium-fr.md) est une grappe homogène conçue pour les <b>tâches massivement parallèles</b> (plus de 1000 cœurs). 

Pour désigner un superordinateur, nous privilégions le terme *grappe* qui représente mieux l'architecture de nos systèmes; plusieurs ordinateurs distincts (*nœuds*) forment une unité semblable à une grappe.

=Quels sont les systèmes qui répondent à mes besoins?= 
Répondre à cette question n'est pas facile puisqu'ils peuvent subvenir à un large éventail de besoins. Si vous avez besoin de clarifications, n'hésitez pas à communiquer avec le [soutien technique](technical_support-fr.md).

Les questions suivantes nous aideront à identifier les ressources pertinentes :
* Quels sont les logiciels que vous voulez utiliser?
** Les logiciels doivent-ils être sous licence commerciale?
** Les logiciels peuvent-ils opérer sans l'intervention d'un utilisateur? Peuvent-ils être contrôlés par un fichier de commandes ou faut-il passer par une interface graphique?
** Les logiciels peuvent-ils fonctionner sous Linux?
* Pour une tâche type, quels sont les besoins en mémoire, temps, puissance de traitement, accélération, espace de stockage, bande passante sur le réseau, etc.? (fournir une estimation)
* À quelle fréquence ce type de tâche sera-t-il exécuté?

Si vous ne connaissez pas les réponses à ces questions, notre équipe technique peut vous guider et vous indiquer les ressources appropriées.

<span id="What_training_is_available?"></span>
## Quelles sont les activités de formation?

La plupart des ateliers sont organisés par nos partenaires régionaux; ils sont offerts en ligne ou en personne et pour tous les niveaux d'expertise.

* WestDRI (Colombie-Britannique et provinces des Prairies)
** [site web Training Materials](https://training.westdri.ca), cliquez sur l'image pour <i>Upcoming sessions</i> ou explorez le menu de navigation dans le haut de la page
** [UAlberta ARC Bootcamp](https://www.ualberta.ca/information-services-and-technology/research-computing/bootcamps.html)
* [SHARCNET](https://www.sharcnet.ca) (Ontario)
** [Calendar](https://www.sharcnet.ca/my/news/calendar)
** [YouTube](http://youtube.sharcnet.ca/)
** [Online Workshops](https://training.sharcnet.ca/)
* [SciNet](https://www.scinethpc.ca) (Ontario)
** [Education Site](https://education.scinet.utoronto.ca)
** [YouTube](https://www.youtube.com/c/SciNetHPCattheUniversityofToronto)
* [Calcul Québec](https://www.calculquebec.ca/en/) (Québec)
** [Événements](https://calculquebec.eventbrite.ca/)
** [Formation](https://www.calculquebec.ca/services-aux-chercheurs/formation/)
* [ACENET](https://www.ace-net.ca/) (provinces de l'Atlantique)
** [Training](https://www.ace-net.ca/training.html)
** [YouTube](https://www.youtube.com/@ACENETDRI)
Voir aussi la liste des [événements de formation sur Explora](https://explora.alliancecan.ca/events).