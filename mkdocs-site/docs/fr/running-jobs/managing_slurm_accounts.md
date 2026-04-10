---
title: "Managing Slurm accounts/fr"
slug: "managing_slurm_accounts"
lang: "fr"

source_wiki_title: "Managing Slurm accounts/fr"
source_hash: "6ba4b69611cd51e83a397f8e1f8febe9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:24:09.212852+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

À chaque tâche soumise à [l'ordonnanceur de tâches Slurm](running-jobs.md) est associé un projet d’allocation scientifique (**RAP** pour *Resource Allocation Project*). Le RAP est sélectionné avec l’option `--account` de `sbatch`.
La priorité de la tâche sera déterminée par la part cible du compte comparée à l’utilisation récente, tel que décrit dans la [Politique d'ordonnancement des tâches](job-scheduling-policies.md).

Plusieurs membres d’un groupe de recherche peuvent utiliser le même compte RAP pour soumettre des tâches. L’utilisation des ressources est *facturée* au même compte; l’utilisation faite par chaque membre du groupe a ainsi un effet sur la priorité des tâches de tous les membres. Il peut donc être avantageux de coordonner la soumission des tâches pour améliorer le rendement du projet.

## Pourquoi gérer l’utilisation dans un compte RAP
Quand une tâche est soumise par un utilisateur qui n’a pas déjà utilisé beaucoup de ressources, il arrive que la priorité de cette tâche soit très basse parce que les autres membres du groupe ont récemment effectué beaucoup de travail. Dans un tel cas, ce sont les tâches de tous les utilisateurs du compte RAP qui devront attendre que la juste part (LevelFS) du compte redescende à une valeur concurrentielle. Puisque le principe de juste part s’applique à la fois à *l’intérieur* d’un groupe et *entre* les groupes, les tâches des utilisateurs qui ont moins consommé de ressources auront la priorité une fois que la juste part du compte sera rétablie.

Ceci pourrait ne pas se produire si les différents utilisateurs soumettent des tâches qui ont des exigences radicalement différentes. Si un utilisateur fait exécuter plusieurs petites tâches qui peuvent se glisser dans les trous d’ordonnancement (*backfilling*, *cycle scavenging*), il se pourrait que la vitesse d'exécution soit appréciable, même si la priorité pour les tâches du groupe demeure basse. Les autres utilisateurs du compte RAP auront de la difficulté à faire exécuter des tâches plus exigeantes en ressources.

## Stratégies
Nous vous invitons à discuter des stratégies suivantes lors de vos réunions de travail.
*   Si plusieurs utilisateurs ont des dates d’échéance différentes pour des projets qui requièrent des tâches en rafale (*burst*), il est avantageux de planifier ces tâches pour éviter que leurs priorités n’interfèrent pas à des moments critiques.
*   Utiliser des grappes différentes. Nos grappes d’usage général ont une capacité quasi identique et l’utilisation par chaque compte RAP est comptabilisée de manière distincte sur chacune. L’utilisateur X du groupe Y sur une grappe n’a pas d’effet sur la priorité des tâches soumises par l’utilisateur Z du compte Y sur une autre grappe.
*   Utiliser plusieurs comptes. Les tâches peuvent utiliser les ressources allouées par suite du concours et les ressources offertes par défaut. Les tâches exécutées dans un compte n’ont pas d’effet sur la juste part de l’autre compte.
*   Dans un contexte de collaboration entre plusieurs groupes, chaque chercheuse principale ou chercheur principal peut obtenir son propre compte et les utilisateurs peuvent être répartis dans les différents RAP pour plus d’efficacité.

Si ces stratégies ne sont pas efficaces, contactez le [soutien technique](technical-support.md) et demandez à l’analyste de consulter la documentation interne intitulée [*A group in conflict with itself*](https://wiki.computecanada.ca/staff/Support_FAQ#A_group_in_conflict_with_itself).