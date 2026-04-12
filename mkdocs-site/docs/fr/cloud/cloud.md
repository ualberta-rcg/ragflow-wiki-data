---
title: "Cloud/fr"
slug: "cloud"
lang: "fr"

source_wiki_title: "Cloud/fr"
source_hash: "66ef40f8cf81cd3d90acf173d7b27d51"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:17:58.861650+00:00"

tags:
  - cloud

keywords:
  - "machine virtuelle"
  - "OpenStack"
  - "Infonuagique"
  - "Projet infonuagique"
  - "Allocation de ressources"
  - "Environnements virtuels"
  - "quota des ressources"
  - "projet de calcul"
  - "sécurité"
  - "projet persistant"
  - "chercheur principal"
  - "ressources infonuagiques"
  - "Infrastructure IaaS"
  - "nom du projet"

questions:
  - "Quels sont les avantages et les inconvénients de l'utilisation des instances virtuelles par rapport aux ressources de traitement par lots sur un superordinateur ?"
  - "Quelles sont les responsabilités en matière de sécurité et les compétences techniques requises pour gérer un projet dans cet environnement infonuagique ?"
  - "Quelles sont les étapes à suivre et les informations nécessaires pour demander la création d'un projet ou accéder à une allocation de ressources existante ?"
  - "Quelles informations et justifications doivent être fournies lors de la demande d'un nouveau projet infonuagique ou d'une augmentation de quota ?"
  - "Quelles sont les responsabilités incombant aux utilisateurs pour la gestion, la sécurité et la sauvegarde de leurs machines virtuelles ?"
  - "Quels sont les cas d'utilisation pris en charge par le service et quelles sont les infrastructures infonuagiques disponibles pour les héberger ?"
  - "Quelles informations préalables sont requises pour accéder à un projet de calcul ou persistant ?"
  - "Où peut-on trouver les instructions pour identifier le nom du projet et les ressources infonuagiques ?"
  - "Qui est responsable de confirmer le droit d'accès au projet ?"
  - "Quelles informations et justifications doivent être fournies lors de la demande d'un nouveau projet infonuagique ou d'une augmentation de quota ?"
  - "Quelles sont les responsabilités incombant aux utilisateurs pour la gestion, la sécurité et la sauvegarde de leurs machines virtuelles ?"
  - "Quels sont les cas d'utilisation pris en charge par le service et quelles sont les infrastructures infonuagiques disponibles pour les héberger ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Nous offrons une infrastructure [IaaS](https://fr.wikipedia.org/wiki/Cloud_computing#Services) pour la création et l'exploitation d'[environnements virtuels](https://fr.wikipedia.org/wiki/Virtualisation).

Dans un nuage, une ou plusieurs instances (ou VM pour *virtual machine*) sont habituellement créées. Avec les privilèges d'administrateur, vous pouvez installer et exécuter tous les programmes nécessaires à votre projet, qu'il s'agisse d'analyser des données en physique des particules ou encore opérer un service Web à l'intention de la recherche en littérature ou en sciences humaines. L'avantage est que vous disposez d'un contrôle total sur les applications installées (la pile logicielle). L'inconvénient par contre est que vous devez posséder une certaine expérience dans la gestion d'un ordinateur et dans l'installation des applications.

Il est facile de créer des instantanés (*snapshots*) de vos instances pour en faire des copies; ceci permet de disposer de versions avec différentes fonctionnalités ou de relancer la même instance en cas de panne de courant, par exemple.

Si vos tâches s'intègrent bien dans un environnement de [traitement par lots](https://fr.wikipedia.org/wiki/Traitement_par_lots) géré par un [ordonnanceur](https://docs.computecanada.ca/wiki/What_is_a_scheduler%3F/fr) sur un [superordinateur](https://fr.wikipedia.org/wiki/Superordinateur), il serait préférable d'utiliser les [autres ressources](../clusters/national_systems.md) qui sont plus disponibles et dont les logiciels sont déjà configurés pour les besoins courants. De plus, certains outils dont [Apptainer](../software/containers/apptainer.md) peuvent aisément être utilisés pour exécuter des piles logicielles personnalisées dans des conteneurs sur nos grappes de calcul.

Si Apptainer ou le traitement par lots ne satisfont pas vos exigences, optez pour l'infonuagique.

## Obtenir un projet dans l'environnement infonuagique
*   [Assurez-vous de bien comprendre vos responsabilités](cloud_shared_security_responsibility_model.md) par rapport à la [protection de votre projet](https://docs.alliancecan.ca/wiki/Cloud_shared_security_responsibility_model/fr) et celle d'une infrastructure partagée par plusieurs.
*   Si vous ne possédez pas de compte, voyez [ces directives](https://docs.alliancecan.ca/wiki/Apply_for_a_CCDB_account/fr).
*   Un [projet](managing_your_cloud_resources_with_openstack.md#projets) est une allocation de ressources qui vous permet de créer des instances infonuagiques.
*   Si vous êtes chercheuse ou chercheur principal et possédez une allocation de ressources infonuagiques (voir la page [Concours pour l'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/concours-pour-lallocation-de-ressources)), vous devriez déjà avoir un projet; voyez les renseignements ci-dessous. Si ce n'est pas le cas ou que vous avez des doutes, contactez le [soutien technique](../support/technical_support.md).
*   Autrement, remplissez le formulaire [Projets infonuagiques et allocations par le service d'accès rapide](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgUpyTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr) pour
    *   obtenir l'accès à un projet existant; pour connaître les renseignements que vous devrez fournir, voyez ci-dessous,
    *   dans le cas d'une chercheuse ou d'un chercheur principal,
        *   demander la création d'un nouveau projet et une allocation de ressources par le [service d'accès rapide](cloud_ras_allocations.md),
        *   demander une hausse du quota de ressources pour un projet existant.
*   Les demandes sont généralement traitées dans les 48 heures ouvrables.

### Préparer votre demande
*   Pour accéder à un projet de calcul ou à un projet persistant, vous devez connaître le nom du projet et le nuage où il se trouve; voyez [comment trouver le nom du projet](managing_your_cloud_resources_with_openstack.md#projets) et la [liste de nos ressources infonuagiques](cloud.md#ressources-infonuagiques). La chercheuse ou le chercheur principal doit confirmer son droit d'accéder au projet.
*   Si vous demandez la création d'un nouveau projet ou une augmentation du quota des ressources pour un projet existant, vous devez :
    *   expliquer pourquoi vous demandez des ressources infonuagiques,
    *   expliquer pourquoi les grappes de CHP ne conviennent pas à votre projet,
    *   décrire les méthodes de maintenance et de sécurité qui seront mises en place (voir [cette page](security_considerations_when_running_a_vm.md)).
*   Une chercheuse ou un chercheur principal peut être propriétaire d'au plus trois projets et la somme des quotas doit respecter les limites établies (voir les limites sur [cette page](cloud_ras_allocations.md)). Elle ou il peut être propriétaire à la fois d'allocations pour des projets de calcul et des projets persistants.

## Créer une machine virtuelle
*   [Comment créer manuellement votre première machine virtuelle](cloud_quick_start.md)
*   [Glossaire technique](cloud_technical_glossary.md)
*   [Choix du type de stockage](cloud_storage_options.md)
*   [Dépannage de problèmes communs](cloud_troubleshooting_guide.md)

## Vos responsabilités
Pour chacun de vos projets, vous êtes responsable de
*   [Créer et gérer vos instances](managing_your_cloud_resources_with_openstack.md)
*   [Assurer la sécurité et la mise à jour des logiciels de vos instances](cloud_shared_security_responsibility_model.md)
*   [Définir les groupes de sécurité pour l'accès à votre réseau](managing_your_cloud_resources_with_openstack.md#groupes-de-securite)
*   [Créer les comptes des utilisateurs](managing_your_linux_vm.md)
*   [Appliquer les meilleures pratiques](vm_best_practices.md)
*   [Assurer la sécurité de vos instances](security_considerations_when_running_a_vm.md)
*   [Faire des copies de sécurité de vos instances](backing_up_your_vm.md)

## Sujets avancés
Si vous avez plus d'expérience, vous pouvez
*   [Créer automatiquement vos instances](automating_vm_creation.md)
*   Coder votre infrastructure avec [Terraform](terraform.md)

## Cas d'utilisation
*   [Configurer un serveur de données ou un serveur Web](configuring_a_data_or_web_server.md)
*   [Utiliser les vGPU](using_cloud_vgpus.md)
*   [Utiliser les GPU](using-cloud-gpu.md)
*   [Utiliser une interface graphique](setting_up_gui_desktop_on_a_vm.md)
*   [Utiliser IPv6 dans le nuage Arbutus](using_ipv6_in_cloud.md)

## Ressources infonuagiques

*   [Nuage Béluga](https://beluga.cloud.computecanada.ca)
*   [Nuage Arbutus](https://arbutus.cloud.computecanada.ca); [voir la documentation](arbutus-user-documentation.md)
*   [Nibi](https://nibi.cloud.alliancecan.ca)
*   [Nuage Cedar](http://cedar.cloud.computecanada.ca)

L'information sur le matériel et les versions OpenStack se trouve sur la page des [ressources infonuagiques](cloud_resources.md).
L'état des ressources et les activités planifiées de maintenance et de mise à jour sont décrits sur la page wiki [État des ressources](../support/system_status.md).

## Assistance
Si vous avez des questions sur ce service, écrivez au [soutien technique](../support/technical_support.md).