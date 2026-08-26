---
title: "Cloud RAS Allocations/fr"
slug: "cloud_ras_allocations"
lang: "fr"

source_wiki_title: "Cloud RAS Allocations/fr"
source_hash: "eb553ed8fc0f5785c72951df81cabaf0"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:07:39.991696+00:00"

tags:
  - cloud

keywords:
  - "instances persistantes"
  - "Instances"
  - "Stockage persistant"
  - "quota de ressources"
  - "Mémoire RAM"
  - "Durée par défaut"
  - "Volumes"
  - "Adresses IP flottantes"
  - "Renouvellement par défaut"
  - "service d'accès rapide"
  - "vGPU"
  - "instances de calcul"
  - "Stockage objet"
  - "Instantanés de volume"

questions:
  - "Quels sont les différents types d’instances (calcul, persistantes, vGPU) proposés par le service d’accès rapide et quelles sont leurs spécificités ?"
  - "Comment les chercheurs principaux peuvent‑ils demander des ressources supplémentaires lorsqu’ils dépassent les quotas du service d’accès rapide ?"
  - "Quelles sont les limites maximales de ressources (vCPU, vGPU, nombre d’instances, volumes, snapshots, RAM, etc.) pour les allocations de calcul et les allocations persistantes ?"
  - "Quelle est la quantité d'adresses IP flottantes allouées par défaut ?"
  - "Quels types de stockage sont proposés et quelles sont leurs capacités maximales ?"
  - "Comment et quand doit‑on demander une allocation de ressources via le service d'accès rapide ?"
  - "Quelle est la limite maximale de vGPU (UGR‑année) attribuée dans ce tableau ?"
  - "Quels sont les quotas (soft quotas) indiqués pour les instances, les volumes, les instantanés de volume et la mémoire RAM, et comment peut‑on demander une augmentation de ces ressources ?"
  - "Quelle est la différence entre une « limite ferme » et un « quota souple » tel que mentionné dans les notes du tableau ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

Votre compte vous donne accès à une petite quantité de ressources de calcul, de stockage et de ressources infonuagiques. Avec le service d'accès rapide, vous pouvez utiliser immédiatement ces ressources pour expérimenter ou pour travailler. Le service d'accès rapide convient à plusieurs groupes de recherche. Si vous avez besoin d'une plus grande quantité de ressources, vous pouvez présenter une demande au [concours pour l'allocation de ressources](../policies/rac_application_guide.md). Les chercheuses principales et chercheurs principaux à qui des ressources ont été allouées par suite du concours peuvent aussi demander des ressources par le service d'accès rapide.

Les ressources infonuagiques vous permettent de créer des **instances** (aussi appelées *machines virtuelles* ou *VM* pour *virtual machine*). Il existe deux options :
*   **Instances de calcul** : celles-ci ont une durée de vie limitée dans le temps et font généralement un usage constant et intensif de CPU; elles sont parfois nommées *instances batch*. Dans certains cas, les activités de production exigent plusieurs instances de calcul. Ces dernières ont une durée de vie maximale d'**un mois**; une fois la limite atteinte, elles sont désactivées et vous devez faire le nettoyage de vos instances et télécharger les données qui doivent être conservées. Il est possible d'obtenir une prolongation de la durée de vie, dépendant de la disponibilité des ressources.
*   **Instances persistantes** : ces instances n'ont pas une durée de vie finie et servent entre autres pour les serveurs web ou les serveurs de bases de données. Règle générale, elles offrent un service persistant et utilisent moins de capacité CPU que les instances de calcul.
*   **vGPU** : Arbutus a présentement des GPU H100 au gabarit **g1-12gb-c3-35gb-125** qui sont disponibles pour le service d'accès rapide. Ils ont 12Go de mémoire GPU, 3 vCPUs, 35 Go de mémoire système et 125Go de stockage éphémère. D'autres gabarits sont disponibles pour les allocations via concours et nous vous invitons à suggérer les combinaisons que vous jugez utiles. Pour plus d'information sur comment configurer une machine virtuelle pour utiliser des vGPU, voir [Utilisation de vGPU dans le cloud](using_cloud_vgpus.md).

## Quantité maximale de ressources

| Attributs | Instance de calcul[^1] | Instance persistante[^1] |
| :--------------------------------------- | :---------------------------------------------: | :------------------------------------------------: |
| Demande faite par | Chercheuse principale ou chercheur principal | Chercheuse principale ou chercheur principal |
| vCPU (voir [Gabarits d'instances](virtual_machine_flavors.md)) | 80 | 25 |
| vGPU (UGR-année)[^2] | 1.8 | 1.8 |
| Instances[^3] | 20 | 10 |
| Volumes[^3] | 2 | 10 |
| Instantanés de volume[^3] | 2 | 10 |
| Mémoire RAM (Go) | 300 | 50 |
| Adresses IP flottantes | 2 | 2 |
| Stockage persistant (To) | 10 | 10 |
| Stockage système de fichier partagé (To)[^2] | 10 | 10 |
| Stockage objet (To)[^2] | 10 | 10 |
| Durée par défaut | 1 an[^4] (durée d'un mois) | 1 an (renouvelable)[^4] |
| Renouvellement par défaut | Avril[^4] | Avril[^4] |

## Demander une allocation de ressources par le service d'accès rapide

Veuillez [remplir ce formulaire](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr).

## Notes

[^1]: Vous pouvez demander une allocation de calcul et une allocation persistante pour partager un même projet. Les deux allocations se partagent le stockage qui est limité à 10TB par type de stockage. Il n'y a pas de limite au nombre de renouvellements annuels qu'une chercheuse principale ou un chercheur principal peut demander via le service d'accès rapide; toutefois, les allocations sont faites sur la base des ressources disponibles et ne sont pas garanties. Les demandes faites avant le 1er janvier se terminent en mars de l'année suivante; leur durée peut donc dépasser un an. La durée des demandes faites entre mai et décembre est de moins d'un an. Les renouvellements prennent effet en avril.
[^2]: Uniquement sur Arbutus et sujet aux exigences pour les projets ayant des allocations par suite du concours d'allocation des ressources.
[^3]: Ceci n'est pas une limite ferme mais plutôt un quota pour les métadonnées. Vous pouvez demander plus de ces ressources sans passer par les concours.
[^4]: Pour correspondre à la période d'allocation des ressources d'avril à mars.