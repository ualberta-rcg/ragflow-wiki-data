---
title: "Cloud RAS Allocations/fr"
slug: "cloud_ras_allocations"
lang: "fr"

source_wiki_title: "Cloud RAS Allocations/fr"
source_hash: "bdb35bbda8d7eaaf915238587835ad3c"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:54:54.319033+00:00"

tags:
  - cloud

keywords:
  - "instances de calcul"
  - "quota de ressources"
  - "Instances"
  - "Mémoire RAM (Go)"
  - "Stockage système de fichier partagé"
  - "Stockage objet"
  - "Stockage persistant"
  - "Instantanés de volume"
  - "instances persistantes"
  - "vGPU"
  - "Adresses IP flottantes"
  - "Demander une allocation de ressources"
  - "Volumes"
  - "service d'accès rapide"

questions:
  - "Quels sont les différents types d’instances (calcul, persistantes, vGPU) proposés par le service d’accès rapide et quelles sont leurs spécificités ?"
  - "Quelles sont les limites maximales de ressources (vCPU, vGPU, nombre d’instances, volumes, snapshots, RAM) attribuées aux instances de calcul et aux instances persistantes ?"
  - "Comment peut‑on demander des ressources supplémentaires ou prolonger la durée de vie d’une instance au‑delà des allocations du service d’accès rapide ?"
  - "Quel volume de stockage persistant et de stockage système de fichiers partagé est alloué par défaut (en To) ?"
  - "Quelle est la durée d’allocation standard des ressources et à quel moment s’effectue le renouvellement automatique ?"
  - "Comment peut‑on soumettre une demande d’allocation de ressources via le service d’accès rapide ?"
  - "Quel est le quota indiqué pour les vGPU (UGR‑année) dans le tableau ?"
  - "Comment le texte précise‑t‑il la nature du quota pour les instances, volumes et instantanés de volume ?"
  - "Quelle quantité de mémoire RAM (en Go) est allouée selon les valeurs présentées ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page fait partie de la documentation sur le [service infonuagique](cloud.md).

Votre compte vous donne accès à une petite quantité de ressources de calcul, de stockage et de ressources infonuagiques. Avec le service d'accès rapide, vous pouvez utiliser immédiatement ces ressources pour expérimenter ou pour travailler. Le service d'accès rapide convient à plusieurs groupes de recherche. Si vous avez besoin d'une plus grande quantité de ressources, vous pouvez présenter une demande au [concours pour l'allocation de ressources](../policies/rac_application_guide.md). Les chercheuses principales et chercheurs principaux à qui des ressources ont été allouées par suite du concours peuvent aussi demander des ressources par le service d'accès rapide.

Les ressources infonuagiques vous permettent de créer des **instances** (aussi appelées *machines virtuelles* ou *VM* pour *virtual machine*). Il existe deux options :

*   **Instances de calcul** : celles-ci ont une durée de vie limitée dans le temps et font généralement un usage constant et intensif de CPU ; elles sont parfois nommées *instances batch*. Dans certains cas, les activités de production exigent plusieurs instances de calcul. Ces dernières ont une durée de vie maximale d'**un mois** ; une fois la limite atteinte, elles sont désactivées et vous devez faire le nettoyage de vos instances et télécharger les données qui doivent être conservées. Il est possible d'obtenir une prolongation de la durée de vie, dépendant de la disponibilité des ressources.
*   **Instances persistantes** : ces instances n'ont pas une durée de vie finie et servent entre autres pour les serveurs web ou les serveurs de bases de données. Règle générale, elles offrent un service persistant et utilisent moins de capacité CPU que les instances de calcul.
*   **vGPU** : Arbutus a présentement des GPU H100 au gabarit **g1-12gb-c3-35gb-125** qui sont disponibles pour le service d'accès rapide. Ils ont 12 Go de mémoire GPU, 3 vCPU, 35 Go de mémoire système et 125 Go de stockage éphémère. D'autres gabarits sont disponibles pour les allocations via concours et nous vous invitons à suggérer les combinaisons que vous jugez utiles. Pour plus d'information sur comment configurer une machine virtuelle pour utiliser des vGPU, voir [Utilisation de vGPU dans le cloud](using_cloud_vgpus.md).

## Quantité maximale de ressources

| Attributs | Instance de calcul[^1] | Instance persistante[^1] |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Demande faite par                 | Chercheuse principale ou chercheur principal                                                                                                                                           | Chercheuse principale ou chercheur principal                                                                                                                                                        |
| vCPU (voir [Gabarits d'instances](virtual_machine_flavors.md)) | 80                                                                                                                                                                                     | 25                                                                                                                                                                                                  |
| vGPU (UGR-année)[^2]              | 1.8                                                                                                                                                                                    | 1.8                                                                                                                                                                                                 |
| Instances[^3]                     | 20                                                                                                                                                                                     | 10                                                                                                                                                                                                  |
| Volumes[^3]                       | 2                                                                                                                                                                                      | 10                                                                                                                                                                                                  |
| Instantanés de volume[^3]         | 2                                                                                                                                                                                      | 10                                                                                                                                                                                                  |
| Mémoire RAM (Go)                  | 300                                                                                                                                                                                    | 50                                                                                                                                                                                                  |
| Adresses IP flottantes            | 2                                                                                                                                                                                      | 2                                                                                                                                                                                                   |
| Stockage persistant (To)          | 10                                                                                                                                                                                     | 10                                                                                                                                                                                                  |
| Stockage système de fichier partagé (To)[^2] | 10                                                                                                                                                                                     | 10                                                                                                                                                                                                  |
| Stockage objet (To)[^2]           | 10                                                                                                                                                                                     | 10                                                                                                                                                                                                  |
| Durée par défaut                  | 1 an[^4] (pour l'allocation de projet), 1 mois (pour l'instance)                                                                                                                     | 1 an (renouvelable)[^4]                                                                                                                                                                             |
| Renouvellement par défaut         | Avril[^4]                                                                                                                                                                              | Avril[^4]                                                                                                                                                                                           |

## Demander une allocation de ressources par le service d'accès rapide

Veuillez [remplir ce formulaire](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr).

## Notes

[^1]: Vous pouvez demander une allocation de calcul et une allocation persistante pour partager un même projet. Les deux allocations se partagent le stockage qui est limité à 10 To par type de stockage. Il n'y a pas de limite au nombre de renouvellements annuels qu'une chercheuse principale ou un chercheur principal peut demander via le service d'accès rapide ; toutefois, les allocations sont faites sur la base des ressources disponibles et ne sont pas garanties. Les demandes faites avant le 1er janvier se terminent en mars de l'année suivante ; leur durée peut donc dépasser un an. La durée des demandes faites entre mai et décembre est de moins d'un an. Les renouvellements prennent effet en avril.
[^2]: Uniquement sur Arbutus, cette ressource limitée est allouée dépendant de la disponibilité.
[^3]: Ceci n'est pas une limite ferme, mais plutôt un quota pour les métadonnées. Vous pouvez demander plus de ces ressources sans passer par les concours.
[^4]: Pour correspondre à la période d'allocation des ressources d'avril à mars.