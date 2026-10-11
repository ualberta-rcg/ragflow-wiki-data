---
title: "Cloud/fr"
slug: "cloud"
lang: "fr"

source_wiki_title: "Cloud/fr"
source_hash: "afb9f77b1438b14a1f66bd4ce52bed5f"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:26:59.707053+00:00"

tags:
  - cloud

keywords:
  - "environnements virtuels"
  - "sécurité des instances"
  - "demande"
  - "nuage"
  - "quota des ressources"
  - "création d'une machine virtuelle"
  - "infrastructure IaaS"
  - "Terraform"
  - "nom du projet"
  - "gestion des ressources cloud"
  - "droits d'accès"
  - "traitement par lots"
  - "projet de calcul"
  - "projet infonuagique"
  - "snapshots"

questions:
  - "Quels sont les avantages et les inconvénients d’utiliser une infrastructure IaaS (cloud) pour vos projets de recherche ?"
  - "Dans quels cas est‑il recommandé de privilégier les ressources nationales (superordinateur, traitement par lots) plutôt que le cloud ?"
  - "Quelles sont les étapes et les informations requises pour obtenir ou créer un projet cloud et une allocation de ressources sur la plateforme Alliance Can ?"
  - "Quelles informations devez‑vous fournir lorsqu’on vous demande de créer un nouveau projet ou d’augmenter le quota des ressources ?"
  - "Quelles sont vos responsabilités en tant que propriétaire d’un projet concernant la gestion, la sécurité et la maintenance des machines virtuelles ?"
  - "Où pouvez‑vous trouver les guides et ressources pour créer, configurer et dépanner une machine virtuelle sur les plateformes cloud (Arbutus, Béluga, etc.) ?"
  - "Comment peut‑on identifier le nom du projet ainsi que le nuage où il se trouve ?"
  - "Quelles sont les étapes à suivre pour préparer une demande d’accès à un projet de calcul ou persistant ?"
  - "Qui est responsable de confirmer le droit d’accès au projet ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nous offrons une infrastructure [IaaS](https://fr.wikipedia.org/wiki/Cloud_computing#Services) pour la création et l'exploitation d'[environnements virtuels](https://fr.wikipedia.org/wiki/Virtualisation).

Dans un nuage, une ou plusieurs instances (ou MV pour *machine virtuelle*) sont habituellement créées. Avec les privilèges d'administrateur, vous pouvez installer et exécuter tous les programmes nécessaires à votre projet, qu'il s'agisse d'analyser des données en physique des particules ou encore d'opérer un service Web à l'intention de la recherche en littérature ou en sciences humaines.

!!! info "Avantages et inconvénients de l'infonuagique"
    L'avantage est que vous disposez d'un contrôle total sur les applications installées (la pile logicielle). L'inconvénient, par contre, est que vous devez posséder une certaine expérience dans la gestion d'un ordinateur et dans l'installation des applications.

Il est facile de créer des instantanés (*snapshots*) de vos instances pour en faire des copies, ce qui permet de disposer de versions avec différentes fonctionnalités ou de relancer la même instance en cas de panne de courant, par exemple.

!!! tip "Infonuagique ou grappes de calcul?"
    Si vos tâches s'intègrent bien dans un environnement de [traitement par lots](https://fr.wikipedia.org/wiki/Traitement_par_lots) géré par un [ordonnanceur](https://docs.computecanada.ca/wiki/What_is_a_scheduler%3F/fr) sur un [superordinateur](https://fr.wikipedia.org/wiki/Superordinateur), il serait préférable d'utiliser les [autres ressources](../clusters/national_systems.md) qui sont plus disponibles et dont les logiciels sont déjà configurés pour les besoins courants. De plus, certains outils, dont [Apptainer](../software/containers/apptainer.md), peuvent aisément être utilisés pour exécuter des piles logicielles personnalisées dans des conteneurs sur nos grappes de calcul.

    Cependant, si Apptainer ou le traitement par lots ne satisfont pas vos exigences, optez pour l'infonuagique.

## Obtenir un projet dans l'environnement infonuagique
*   [Assurez-vous de bien comprendre vos responsabilités](cloud_shared_security_responsibility_model.md) par rapport à la [protection de votre projet](https://docs.alliancecan.ca/wiki/Cloud_shared_security_responsibility_model/fr) et celle d'une infrastructure partagée par plusieurs.
*   Si vous ne possédez pas de compte, voyez [ces directives](https://docs.alliancecan.ca/wiki/Apply_for_a_CCDB_account/fr).
*   Un [projet](managing_your_cloud_resources_with_openstack.md#projets) est une allocation de ressources qui vous permet de créer des instances infonuagiques.
*   Si vous êtes chercheuse ou chercheur principal et possédez une allocation de ressources infonuagiques (voir la page [Concours pour l'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/concours-pour-lallocation-de-ressources)), vous devriez déjà avoir un projet; voyez les renseignements ci-dessous. Si ce n'est pas le cas ou que vous avez des doutes, contactez le [soutien technique](../support/technical_support.md).
*   Autrement, remplissez le formulaire [Projets infonuagiques et allocations par le service d'accès rapide](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr) pour
    *   obtenir l'accès à un projet existant; pour connaître les renseignements que vous devrez fournir, voyez ci-dessous,
    *   dans le cas d'une chercheuse ou d'un chercheur principal,
        *   demander la création d'un nouveau projet et une allocation de ressources par le [service d'accès rapide](cloud_ras_allocations.md),
        *   demander une hausse du quota de ressources pour un projet existant.
*   Les demandes sont généralement traitées dans les 48 heures ouvrables.

### Préparer votre demande
*   Pour accéder à un projet de calcul ou à un projet persistant, vous devez connaître le nom du projet et le nuage où il se trouve; voyez [comment trouver le nom du projet](managing_your_cloud_resources_with_openstack.md#projets) et la [liste de nos ressources infonuagiques](#ressources-infonuagiques). La chercheuse ou le chercheur principal doit confirmer son droit d'accéder au projet.
*   Si vous demandez la création d'un nouveau projet ou une augmentation du quota des ressources pour un projet existant, vous devez :
    *   expliquer pourquoi vous demandez des ressources infonuagiques,
    *   expliquer pourquoi les grappes de calcul de haute performance (CHP) ne conviennent pas à votre projet,
    *   décrire les méthodes de maintenance et de sécurité qui seront mises en place (voir [cette page](security_considerations_when_running_a_vm.md)).
*   Une chercheuse ou un chercheur principal peut être propriétaire d'au plus trois projets et la somme des quotas doit respecter les limites établies (voir les limites sur [cette page](cloud_ras_allocations.md)). Elle ou il peut être propriétaire à la fois d'allocations pour des projets de calcul et des projets persistants.

## Créer une machine virtuelle
*   [Comment créer manuellement votre première machine virtuelle](cloud_quick_start.md)
*   [Glossaire technique](cloud_technical_glossary.md)
*   [Choix du type de stockage](cloud_storage_options.md)
*   [Dépannage de problèmes communs](cloud_troubleshooting_guide.md)

## Vos responsabilités
Pour chacun de vos projets, vous êtes responsable de :
*   [Créer et gérer vos instances](managing_your_cloud_resources_with_openstack.md)
*   [Assurer la sécurité et la mise à jour des logiciels de vos instances](cloud_shared_security_responsibility_model.md)
*   [Définir les groupes de sécurité pour l'accès à votre réseau](managing_your_cloud_resources_with_openstack.md#groupes-de-sécurité)
*   [Créer les comptes des utilisateurs](managing_your_linux_vm.md)
*   [Appliquer les meilleures pratiques](vm_best_practices.md)
*   [Assurer la sécurité de vos instances](security_considerations_when_running_a_vm.md)
*   [Faire des copies de sécurité de vos instances](backing_up_your_vm.md)

## Sujets avancés
Si vous avez plus d'expérience, vous pouvez :
*   [Créer automatiquement vos instances](automating_vm_creation.md)
*   Coder votre infrastructure avec [Terraform](terraform.md)

## Cas d'utilisation
*   [Configurer un serveur de données ou un serveur Web](configuring_a_data_or_web_server.md)
*   [Utiliser les vGPU](using_cloud_vgpus.md)
*   [Utiliser les GPU](cloud.md)
*   [Utiliser une interface graphique](setting_up_gui_desktop_on_a_vm.md)
*   [Utiliser IPv6 dans le nuage Arbutus](using_ipv6_in_cloud.md)

## Ressources infonuagiques
*   [Nuage Béluga](https://beluga.cloud.computecanada.ca)
*   [Arbutus (depuis le 7 avril 2026)](https://arbutus.alliancecan.ca)
*   [Arbutus (*Legacy Arbutus*, configuration d'avant le renouvellement de l'infrastructure)](https://arbutus.cloud.computecanada.ca)
*   [Nuage Nibi](https://nibi.cloud.alliancecan.ca)
*   [Nuage Cedar](http://cedar.cloud.computecanada.ca)

L'information sur le matériel et les versions OpenStack se trouve sur la page des [ressources infonuagiques](cloud_resources.md).
L'état des ressources et les activités planifiées de maintenance et de mise à jour sont décrits sur la page [État des ressources](../support/system_status.md).

## Assistance
Si vous avez des questions sur ce service, écrivez au [soutien technique](../support/technical_support.md).