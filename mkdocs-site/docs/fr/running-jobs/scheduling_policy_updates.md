---
title: "Scheduling policy updates/fr"
slug: "scheduling_policy_updates"
lang: "fr"

source_wiki_title: "Scheduling policy updates/fr"
source_hash: "29b293a62e8c81441c53c4a1d54d6963"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:04:38.677772+00:00"

tags:
  []

keywords:
  - "CPU jobs"
  - "job scheduling policies"
  - "RAC allocations"
  - "sub-allocations"
  - "GPU jobs"

questions:
  - "Quel est l'objectif principal de cette page concernant les politiques d'ordonnancement des tâches ?"
  - "À quelles dates les comptes de l'allocation RAC 2026 et les sous-allocations seront-ils activés sur les différentes grappes (fir, nibi, narval, rorqual) ?"
  - "Quelles sont les nouvelles règles et restrictions spécifiques qui s'appliquent aux demandes de tâches GPU (comme les limites MIG et l'indication du modèle) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "En préparation"
Cette page vise à consigner les changements apportés aux politiques d'ordonnancement des tâches qui pourraient modifier le comportement des commandes de soumission de tâches (`sbatch`, `salloc`, `srun`).

## Modifications liées aux comptes

### Allocations RAC

*   Activation des comptes RAC 2026
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: 2026-04-07
    *   rorqual: 2026-04-07

### Autres modifications des politiques relatives aux comptes

*   Sous-allocations activées
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
    *   narval: 2026-04-07
    *   rorqual: 2026-04-07

## Modifications liées aux tâches CPU

(Aucune pour le moment)

## Modifications liées aux tâches GPU

*   Vous ne pouvez pas demander plusieurs GPU multi-instances (MIG) dans une même tâche.
    *   fir : 2026-04-06
    *   nibi : 2026-04-06
*   Activation des sous-allocations
    *   fir : 2026-04-06
    *   nibi : 2026-04-06
*   Activation des nouveaux comptes par suite du concours d'allocation des ressources pour 2026
    *   fir: 2026-04-06
    *   nibi: 2026-04-06
*   Pour toutes les demandes de GPU, vous devez en indiquer le modèle.
    *   fir : 2026-04-06
    *   nibi : 2026-04-06