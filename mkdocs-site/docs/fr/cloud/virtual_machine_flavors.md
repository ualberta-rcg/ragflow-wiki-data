---
title: "Virtual machine flavors/fr"
slug: "virtual_machine_flavors"
lang: "fr"

source_wiki_title: "Virtual machine flavors/fr"
source_hash: "c6455608ee44ef5eddd0d260a0b5e398"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:44:01.810138+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

*Page enfant de [Service infonuagique](service-infonuagique.md)*

!!! note "Gabarits OpenStack"
    Les gabarits (*flavors*) OpenStack pour le matériel virtuel définissent plusieurs paramètres, incluant le nombre de cœurs, la capacité de mémoire vive et d'espace disque. Ceci permet à l'utilisateur de sélectionner le type d'instance qui convient, tout comme il choisirait un serveur physique.

    Consultez le [*NetApp OpenStack Deployment and Operations Guide*](http://netapp.github.io/openstack-deploy-ops-guide/icehouse/content/section_nova-key-concepts.html).

## Afficher les gabarits disponibles

Vous pouvez voir les gabarits que vous pouvez sélectionner pour votre projet dans le tableau de bord Horizon ou en entrant la commande ci-dessous avec le [client de ligne de commande OpenStack](openstack-command-line-clients.md).

```bash
openstack flavor list --sort-column RAM
```

!!! tip
    Si vous avez besoin d'un gabarit qui n'est pas affiché, écrivez à nuage@tech.alliancecan.ca.

## Nomenclature des gabarits

Les gabarits ont des noms semblables à :
*   `c2-7.5gb-92`
*   `p1-0.75gb`
*   `g1-8gb-c4-22gb`

Par convention, le préfixe « c » désigne « calcul » (*compute*), le préfixe « p » désigne « persistant » (*persistent*) et le préfixe « g » désigne « vGPU ». Le préfixe est suivi du nombre de CPU ou GPU virtuels, d'un tiret, puis de la quantité de mémoire vive. Si le nom du gabarit comprend un deuxième tiret, il est suivi de la taille du disque éphémère secondaire, en gigaoctets. Dans le cas d'un vGPU, le gabarit est inclus à la suite de l'information sur ce vGPU.

## Gabarits de type « c »

*   conviennent aux tâches de développement, de test et les tâches d'une durée d'exécution limitée;
*   sont démarrés à partir d'une image de format [qcow2](https://fr.wikipedia.org/wiki/Qcow2);
*   les disques de la machine virtuelle résident localement sur le matériel qui exécute l'instance et ne sont pas redondants (voir [RAID 0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0));
*   le disque racine est typiquement de 20 Go;
*   un disque éphémère secondaire pour le stockage des données est créé et supprimé avec l'instance;
*   dans le cas d’Arbutus, ces gabarits conviennent aux tâches faisant un usage intense des CPU puisqu'ils ne les surexploitent pas.

## Gabarits de type « p »

*   conviennent aux tâches dont la durée d'exécution est indéterminée;
*   le disque racine n'est pas prédéfini;
*   les gabarits devraient être [démarrés depuis un volume](working-with-volumes.md#démarrer-depuis-un-volume);
*   nous recommandons un volume d'au moins 20 Go pour le disque racine persistant;
*   dans le cas d’Arbutus, ces gabarits sont sur des nœuds de calcul avec redondance élevée (disque et réseau) et ils surexploitent le CPU; ils conviennent donc aux serveurs web, aux serveurs de bases de données et aux instances qui font généralement peu usage du CPU ou encore ont un usage irrégulier.