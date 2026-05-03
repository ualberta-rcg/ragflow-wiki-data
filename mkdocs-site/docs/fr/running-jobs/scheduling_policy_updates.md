---
title: "Scheduling policy updates/fr"
slug: "scheduling_policy_updates"
lang: "fr"

source_wiki_title: "Scheduling policy updates/fr"
source_hash: "51915db1e29980145ef5e7c77da8172c"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:46:58.815657+00:00"

tags:
  []

keywords:
  - "job scheduling policies"
  - "GPU multi-instances (MIG)"
  - "RAC allocations"
  - "sous-allocations"
  - "GPU jobs"

questions:
  - "Quel est le but principal de cette page concernant les politiques d'ordonnancement des tâches ?"
  - "Quelles sont les dates d'activation des comptes RAC 2026 et des sous-allocations pour les grappes Fir, Nibi, Narval et Rorqual ?"
  - "Quelles sont les nouvelles règles et restrictions à respecter lors de la demande de ressources pour les tâches GPU ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "EN PRÉPARATION"
Cette page vise à consigner les modifications apportées aux politiques d'ordonnancement des tâches qui pourraient changer le comportement des commandes de soumission de tâches (`sbatch`, `salloc`, `srun`).

## Comptes

### Allocations RAC

* Comptes RAC 2026 activés
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06
    * **Narval** : 2026-04-07
    * **Rorqual** : 2026-04-07

### Autres mises à jour des comptes

* Sous-allocations disponibles
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06
    * **Narval** : 2026-04-07
    * **Rorqual** : 2026-04-07

## Tâches CPU

(aucune en date du 1er mai 2026)

## Tâches GPU

* Vous ne pouvez pas demander plusieurs GPU multi-instances (MIG) dans une même tâche.
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06
* Activation des sous-allocations
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06
* Activation des nouveaux comptes par suite du concours d'allocation des ressources pour 2026
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06
* Pour toutes les demandes de GPU, vous devez en indiquer le modèle.
    * **Fir** : 2026-04-06
    * **Nibi** : 2026-04-06