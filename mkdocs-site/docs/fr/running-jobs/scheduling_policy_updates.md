---
title: "Scheduling policy updates/fr"
slug: "scheduling_policy_updates"
lang: "fr"

source_wiki_title: "Scheduling policy updates/fr"
source_hash: "33ffec18cf1d571e261bc49319d29337"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:52:08.612788+00:00"

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

Vous trouverez ici les changements apportés à [nos politiques en matière d'ordonnancement](job_scheduling_policies.md) qui sont susceptibles de modifier le comportement des commandes `sbatch`, `salloc` et `srun` dans les scripts de soumission des tâches.

## Comptes

### Allocations de ressources

* Activation des comptes pour le concours d'allocation des ressources de 2026
  * Fir, 2026-04-06
  * Nibi, 2026-04-06
  * Narval, 2026-04-07
  * Rorqual, 2026-04-07

### Autres changements

* Disponibilité des sous-allocations
  * Fir, 2026-04-06
  * Nibi, 2026-04-06
  * Narval, 2026-04-07
  * Rorqual, 2026-04-07

## Tâches avec CPU

(aucune mise à jour depuis le 1er mai 2026)

## Tâches avec GPU

* Toutes les demandes doivent spécifier [un modèle de GPU](using_gpus_with_slurm.md) ou [un modèle d'instance](../programming/multi-instance_gpu.md).
  * Fir, 2026-04-06
  * Nibi, 2026-04-06
  * Narval, (bientôt disponible)
  * Rorqual, 2026-04-17
* Il n'est pas possible de demander plus d'une [multi-instance](../programming/multi-instance_gpu.md) pour une même tâche.
  * Fir, 2026-04-06
  * Nibi, 2026-04-06
  * Narval, (bientôt disponible)
  * Rorqual, 2026-04-17