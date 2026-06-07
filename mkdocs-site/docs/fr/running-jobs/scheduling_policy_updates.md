---
title: "Scheduling policy updates/fr"
slug: "scheduling_policy_updates"
lang: "fr"

source_wiki_title: "Scheduling policy updates/fr"
source_hash: "1959b0f310d301275cdd3de646225640"
last_synced: "2026-06-07T00:07:37.701416+00:00"
last_processed: "2026-06-07T00:22:42.080202+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

!!! note "EN PRÉPARATION"
Cette page a pour but de noter les changements aux [politiques d'ordonnancement des tâches](job_scheduling_policies.md) qui pourraient modifier le comportement des commandes de soumission de tâches (comme `sbatch`, `salloc`, `srun`).

## Comptes

### Allocations RAC

*   Comptes RAC 2026 activés
    *   Fir : 2026-04-06
    *   Nibi : 2026-04-06
    *   Narval : 2026-04-07
    *   Rorqual : 2026-04-07

### Autres mises à jour de comptes

*   Sous-allocations disponibles
    *   Fir : 2026-04-06
    *   Nibi : 2026-04-06
    *   Narval : 2026-04-07
    *   Rorqual : 2026-04-07

## Tâches CPU

(aucune en date du 1er mai 2026)

## Tâches GPU

*   Toutes les requêtes GPU doivent [spécifier un modèle de GPU](using_gpus_with_slurm.md#introduction) ou un [modèle d'instance](../programming/multi-instance_gpu.md).
    *   Fir : 2026-04-06
    *   Nibi : 2026-04-06
    *   Narval : (à venir bientôt)
    *   Rorqual : 2026-04-17
*   Seulement une [instance MIG](../programming/multi-instance_gpu.md) peut être demandée à la fois.
    *   Fir : 2026-04-06
    *   Nibi : 2026-04-06
    *   Narval : (à venir bientôt)
    *   Rorqual : 2026-04-17