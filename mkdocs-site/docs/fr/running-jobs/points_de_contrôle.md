---
title: "Points de contrôle/fr"
slug: "points_de_contrôle"
lang: "fr"

source_wiki_title: "Points de contrôle/fr"
source_hash: "81d5af8b3da67a42597bc193ce17d058"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:25:55.814787+00:00"

tags:
  []

keywords:
  - "exécution d'un programme"
  - "dmtcp_launch"
  - "grappes"
  - "simulation"
  - "restart"
  - "resoumission à partir d'un script"
  - "vecteurs de tâches"
  - "points de contrôle"
  - "écriture atomique"
  - "redémarrage"
  - "tâches Slurm"
  - "checkpoint file"
  - "resoumettre une tâche"
  - "dmtcp_restart_script.sh"
  - "calcul de longue durée"

questions:
  - "Pourquoi est-il important de créer des points de contrôle lors de l'exécution de longs programmes sur des grappes de calcul ?"
  - "À quelle fréquence est-il recommandé de générer un fichier de point de contrôle lors de son implémentation ?"
  - "Quelles méthodes peuvent être utilisées pour rendre l'écriture d'un point de contrôle atomique et éviter la corruption des données en cas d'interruption ?"
  - "Dans quel cas de figure est-il nécessaire de morceler un calcul en plusieurs tâches Slurm ?"
  - "Quelle est la première méthode recommandée utilisant les vecteurs de tâches (job arrays) pour gérer ces calculs longs ?"
  - "Quelle est la méthode alternative proposée pour resoumettre une tâche sans utiliser les vecteurs de tâches ?"
  - "How does the script determine whether to start a new simulation or resume an existing one?"
  - "What is the purpose of the parameters used in the `dmtcp_launch` command, specifically the `-i 3600` flag?"
  - "What information is logged by the script after the simulation process concludes?"
  - "Dans quel cas de figure est-il nécessaire de morceler un calcul en plusieurs tâches Slurm ?"
  - "Quelle est la première méthode recommandée utilisant les vecteurs de tâches (job arrays) pour gérer ces calculs longs ?"
  - "Quelle est la méthode alternative proposée pour resoumettre une tâche sans utiliser les vecteurs de tâches ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

L’exécution d’un programme est parfois trop longue pour la durée permise par les systèmes de soumissions qui sont sur les grappes. L’exécution d’un long programme est également tributaire des aléas des systèmes. Un programme ayant une courte durée d’exécution peut aisément être redémarré. Par contre, lorsque l’exécution du programme devient très longue, il est préférable de faire des points de contrôle pour minimiser les chances de perdre plusieurs semaines de calcul. Ceux-ci permettront par la suite le redémarrage du programme.

## Création et chargement d'un point de contrôle
La création et le chargement d'un point de contrôle peuvent déjà être implémentés dans une application que vous utilisez. Il suffit alors d'utiliser cette fonctionnalité et de consulter la documentation à cet effet au besoin.

Cependant, si vous avez accès au code source de l'application et/ou que vous en êtes l'auteur, vous pouvez implémenter la création et le chargement de points de contrôle. À la base:

*   La création d'un fichier de point de contrôle se fait de façon périodique. On suggère des périodes de 2 à 24 heures
*   Pendant l'écriture du fichier, il faut garder en tête que la tâche de calcul peut être interrompue à tout moment, et ce, pour toute sorte de raison technique. Par conséquent:
    *   Il est préférable de ne pas écraser le précédent point de contrôle en créant le nouveau
    *   On peut rendre l'écriture *atomique* en effectuant une opération qui vient confirmer la fin de l'écriture du point de contrôle. Par exemple, on peut initialement nommer le fichier en fonction de la date et l'heure et, finalement, créer un lien symbolique "derniere-version" vers le nouveau fichier de point de contrôle ayant un nom unique. Autre méthode plus avancée : on peut créer un second fichier contenant une somme de hachage du point de contrôle, permettant ainsi de valider l'intégrité du point de contrôle à son éventuel chargement
    *   Une fois l'écriture atomique complétée, on peut décider de supprimer ou non des vieux points de contrôle

## Resoumettre une tâche pour un calcul de longue durée
Si on prévoit qu'un long calcul sera morcelé en plusieurs tâches Slurm, les [deux méthodes recommandées](running-jobs.md#resoumettre-une-tache-pour-un-calcul-de-longue-duree) sont:
*   [l'utilisation de vecteurs de tâches (*job arrays*) Slurm](running-jobs.md#redemarrage-avec-des-vecteurs-de-taches);
*   [la resoumission à partir de la fin du script](running-jobs.md#resoumettre-a-partir-dun-script).