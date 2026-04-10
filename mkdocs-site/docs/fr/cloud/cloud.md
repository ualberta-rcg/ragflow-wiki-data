---
title: "Cloud/fr"
tags:
  - cloud

keywords:
  []
---

Nous offrons une infrastructure [IaaS](https://fr.wikipedia.org/wiki/Cloud_computing#Services) pour la création et l'exploitation d'[environnements virtuels](https://fr.wikipedia.org/wiki/Virtualisation).

Dans un nuage, une ou plusieurs instances (ou VM pour <i>virtual machine</i>) sont habituellement créées. Avec les privilèges d'administrateur, vous pouvez installer et exécuter tous les programmes nécessaires à votre projet, qu'il s'agisse d'analyser des données en physique des particules ou encore opérer un service Web à l'intention de la recherche en littérature ou en sciences humaines. L'avantage est que vous disposez d'un contrôle total sur les applications installées (la pile logicielle). L'inconvénient par contre est que vous devez posséder une certaine expérience dans la gestion d'un ordinateur et dans l'installation des applications.

Il est facile de créer des instantanés (<i>snapshots</i>) de vos instances pour en faire des copies; ceci permet de disposer de versions avec différentes fonctionnalités ou de relancer la même instance en cas de panne de courant, par exemple.

Si vos tâches s'intègrent bien dans un environnement de [traitement par lots](https://fr.wikipedia.org/wiki/Traitement_par_lots) géré par un [ordonnanceur](https://docs.computecanada.ca/wiki/What_is_a_scheduler%3F/fr) sur un [superordinateur](https://fr.wikipedia.org/wiki/Superordinateur), il serait préférable d'utiliser les [autres ressources](national-systems-fr.md) qui sont plus disponibles et dont les logiciels sont déjà configurés pour les besoins courants. De plus, certains outils dont [Apptainer](apptainer-fr.md) peuvent aisément être utilisés pour exécuter des piles logicielles personnalisées dans des conteneurs sur nos grappes de calcul.

Si Apptainer ou le traitement par lots ne satisfont pas vos exigences, optez pour l'infonuagique.

## Obtenir un projet dans l'environnement infonuagique
* [Assurez-vous de bien comprendre vos responsabilités](cloud-shared-security-responsibility-model-fr.md) par rapport à la [protection de votre projet](https://docs.alliancecan.ca/wiki/Cloud_shared_security_responsibility_model/fr) et celle d'une infrastructure partagée par plusieurs.
* Si vous ne possédez pas de compte, voyez [ces directives](https://docs.alliancecan.ca/wiki/Apply_for_a_CCDB_account/fr).	
* Un [projet](managing_your_cloud_resources_with_openstack-fr#projets.md) est une allocation de ressources qui vous permet de créer des instances infonuagiques.
* Si vous êtes chercheuse ou chercheur principal et possédez une allocation de ressources infonuagiques (voir la page [Concours pour l'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/concours-pour-lallocation-de-ressources)), vous devriez déjà avoir un projet; voyez les renseignements ci-dessous. Si ce n'est pas le cas ou que vous avez des doutes, contactez le [soutien technique](technical-support-fr.md).
* Autrement, remplissez le formulaire [Projets infonuagiques et allocations par le service d'accès rapide](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr) pour
** obtenir l'accès à un projet existant; pour connaître les renseignements que vous devrez fournir, voyez ci-dessous,
** dans le cas d'une chercheuse ou d'un chercheur principal,
*** demander la création d'un nouveau projet et une allocation de ressources par le [service d'accès rapide](cloud_ras_allocations-fr.md),
*** demander une hausse du quota de ressources pour un projet existant.

* Les demandes sont généralement traitées dans les 48 heures ouvrables.

### Préparer votre demande
* Pour accéder à un projet de calcul ou à un projet persistant, vous devez connaître le nom du projet et le nuage où il se trouve; voyez [comment trouver le nom du projet](managing_your_cloud_resources_with_openstack-fr#projets.md) et la [liste de nos ressources infonuagiques](cloud-fr#ressources_infonuagiques.md). La chercheuse ou le chercheur principal doit confirmer son droit d'accéder au projet. 
* Si vous demandez la création d'un nouveau projet ou une augmentation du quota des ressources pour un projet existant, vous devez ː
**expliquer pourquoi vous demandez des ressources infonuagiques,
**expliquer pourquoi les grappes de CHP ne conviennent pas à votre projet,
**décrire les méthodes de maintenance et de sécurité qui seront mises en place (voir [cette page](security_considerations_when_running_a_vm-fr.md)).
*Une chercheuse ou un chercheur principal peut être propriétaire d'au plus trois projets et la somme des quotas doit respecter les limites établies (voir les limites sur [cette page](cloud_ras_allocations-fr.md)). Elle ou il peut être propriétaire à la fois d'allocations pour des projets de calcul et des projets persistants.

## Créer une machine virtuelle
* [Comment créer manuellement votre première machine virtuelle](cloud-quick-start-fr.md)
* [Glossaire technique](cloud_technical_glossary-fr.md)
* [Choix du type de stockage](cloud_storage_options-fr.md)
* [Dépannage de problèmes communs](cloud-troubleshooting-guide-fr.md)

## Vos responsabilités
Pour chacun de vos projets, vous êtes responsable de
* 
[Créer de gérer vos instances](managing_your_cloud_resources_with_openstack-fr.md)
*[Assurer la sécurité et la mise à jour des logiciels de vos instances](cloud_shared_security_responsibility_model-fr.md)
*[Définir les groupes de sécurité pour l'accès à votre réseau](managing_your_cloud_resources_with_openstack-fr#groupes_de_sécurité.md)
*[Créer les comptes des utilisateurs](managing_your_linux_vm.md)
*[Appliquer les meilleures pratiques](vm-best-practices-fr.md)
*[Assurer la sécurité de vos instances](security_considerations_when_running_a_vm-fr.md)
*[Faire des copies de sécurité de vos instances](backing_up_your_vm-fr.md)

## Sujets avancés
Si vous avez plus d'expérience, vous pouvez
*[Créer automatiquement vos instances](automating_vm_creation-fr.md)
*Coder votre infrastructure avec [Terraform](terraform-fr.md)
## Cas d'utilisation
*[Configurer un serveur de données ou un serveur Web](configuring-a-data-or-web-server-fr.md)
*[Utiliser les vGPU](using-cloud-vgpus-fr.md)
*[Utiliser les GPU](using-cloud-gpu.md)
*[Utiliser une interface graphique](setting-up-gui-desktop-on-a-vm.md)
*[Utiliser IPv6 dans le nuage Arbutus](using-ipv6-in-cloud-fr.md)

<div class="mw-translate-fuzzy">
## Ressources infonuagiques 

* [Nuage Béluga](https://beluga.cloud.computecanada.ca)
* [Nuage Arbutus](https://arbutus.cloud.computecanada.ca); [voir la documentation](arbutus-user-documentation.md)
* [Nibi](https://nibi.cloud.alliancecan.ca)
* [Nuage Cedar](http://cedar.cloud.computecanada.ca)

L'information sur le matériel et les versions OpenStack se trouve sur la page des [ressources infonuagiques](cloud_resources-fr.md).
L'état des ressources et les activités planifiées de maintenance et de mise à jour sont décrits sur la page wiki [État des ressources](system_status-fr.md).
</div>

## Assistance
Si vous avez des questions sur ce service, écrivez au [soutien technique](technical-support-fr.md).