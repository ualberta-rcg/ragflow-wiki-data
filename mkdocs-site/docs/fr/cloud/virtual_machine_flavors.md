---
title: "Virtual machine flavors/fr"
tags:
  - cloud

keywords:
  []
---

*Page enfant de [Service infonuagique](https://docs.computecanada.ca/wiki/CC-Cloud/fr)*

Vous pouvez voir les gabarits que vous pouvez sélectionner pour votre projet dans le tableau de bord Horizon ou en entrant la commande ci-dessous avec le [client ligne de commande](openstack-command-line-clients-fr.md).

```bash
openstack flavor list --sort-column RAM
```

Si vous avez besoin d'un gabarit qui n'est pas affiché, écrivez à nuage@tech.alliancecan.ca.

Les gabarits ont des noms semblables à
 c2-7.5gb-92
 p1-0.75gb
 g1-8gb-c4-22gb
Par convention, le préfixe c désigne «&nbsp;calcul&nbsp;» (*compute*), le préfixe p désigne «&nbsp;persistant&nbsp;» (*persistent*) et le préfixe g désigne «&nbsp;vGPU&nbsp;». Le préfixe est suivi du nombre de CPU ou GPU virtuels, d'un tiret, puis de la quantité de mémoire vive. Si le nom du gabarit comprend un deuxième tiret, il est suivi de la taille du disque éphémère secondaire, en gigaoctets. Dans le cas d'un vGPU, le gabarit est inclus à la suite de l'information sur ce vGPU.

[thumb|alt=Openstack flavors|Gabarits OpenStack](file:flavors.png.md)

**Gabarits de type c**
*conviennent aux tâches de développement, de test et les tâches d'une durée d'exécution limitée;
*sont démarrés à partir d'une image de format [qcow2](https://fr.wikipedia.org/wiki/Qcow2);
*les disques de la machine virtuelle résident localement sur le matériel qui exécute l'instance et ne sont pas redondants (voir [raid0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0));
*le disque racine est typiquement de 20Go;
*un disque éphémère secondaire pour le stockage des données est créé et supprimé avec l'instance;
*dans le cas d’Arbutus, ces gabarits conviennent aux tâches faisant un usage intense des CPU puisqu'ils ne les surexploitent pas.

**Gabarits de type p**
*conviennent aux tâches dont la durée d'exécution est indéterminée;
*le disque racine n'est pas prédéfini;
*les gabarits devraient être [démarrés depuis un volume](working_with_volumes-fr#démarrer_depuis_un_volume.md);
*nous recommandons un volume d'au moins 20Go pour le disque racine persistant;
*dans le cas d’Arbutus, ces gabarits sont sur des nœuds de calcul avec redondance élevée (disque et réseau) et ils surexploitent le CPU;  ils conviennent donc aux serveurs web, aux serveurs de bases de données et aux instances qui font généralement peu usage du CPU ou encore ont un usage irrégulier.