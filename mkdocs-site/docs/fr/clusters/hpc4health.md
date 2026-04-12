---
title: "HPC4Health/fr"
slug: "hpc4health"
lang: "fr"

source_wiki_title: "HPC4Health/fr"
source_hash: "93193de40f40ed81402c7ce1ff70130c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:53:54.164892+00:00"

tags:
  []

keywords:
  - "allocation de ressources"
  - "HPC4Health"
  - "concours 2020"
  - "données de santé"
  - "infrastructure de calcul"

questions:
  - "Qu'est-ce que le consortium HPC4Health et en quoi consiste son projet pilote pour les concours de 2020 ?"
  - "Quelles sont les conditions d'admissibilité et les exigences de sécurité pour qu'un projet de recherche puisse utiliser cette plateforme ?"
  - "Quelles sont les capacités techniques de l'infrastructure allouée (processeurs, mémoire, stockage) et comment sont gérées les sauvegardes de données ?"
  - "Qu'est-ce que le consortium HPC4Health et en quoi consiste son projet pilote pour les concours de 2020 ?"
  - "Quelles sont les conditions d'admissibilité et les exigences de sécurité pour qu'un projet de recherche puisse utiliser cette plateforme ?"
  - "Quelles sont les capacités techniques de l'infrastructure allouée (processeurs, mémoire, stockage) et comment sont gérées les sauvegardes de données ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Contexte

Dans le cadre des concours de 2020, il y aura un projet pilote pour l’allocation de ressources sur une grappe fournie par HPC4Health.

HPC4Health est un consortium de services de santé du University Health Network et du centre hospitalier The Hospital for Sick Children de Toronto. L'organisation construit et maintient une infrastructure virtuelle de calcul avec de hauts niveaux de sécurité.

Le service sera configuré selon les standards de Calcul Canada (Slurm, CVMFS); sur demande, des configurations techniques particulières pourraient être considérées.

!!! note "Disponibilité et soutien"
    La disponibilité et le soutien ne sont pas encore pleinement déterminés; ils pourraient être modifiés au courant de l’année d’allocation, mais la plateforme devrait recevoir le même soutien que les autres sites hôtes.

## Admissibilité

!!! info "Consultation"
    Pour qu’une demande soit considérée, il faut d’abord obtenir une consultation avec HPC4Health; pour ce faire, contactez [rac@calculcanada.ca](mailto:rac@calculcanada.ca).

Les conditions d'admissibilité sont :
*   de signer une entente de collaboration avec le University Health Network;
*   de ne pas servir de réseau d’information sur la santé conformément à la *Loi sur la protection des renseignements personnels sur la santé* (LPRPS), c’est-à-dire, de ne pas utiliser les services pour partager les données avec des collaborateurs ou sur le web;
*   d'utiliser une double authentification pour se connecter aux services.

Avant que l’allocation ne soit implémentée, les utilisateurs devront rencontrer l'équipe de HPC4Health pour signer l'entente de collaboration et confirmer qu'ils ne sont pas fournisseurs de services de santé.

Les projets admissibles sont dans le domaine de la santé où les données utilisées en recherche incluent des ensembles de données confidentielles dont l’utilisation est réservée au système informatique de chaque établissement; des données anonymes, mais sensibles; ou des données qui sont difficilement anonymisées (par exemple, les séquences complètes des génomes). HPC4Health collaborera avec les utilisateurs, les comités d’éthique de la recherche et les services juridiques pour que les besoins spécifiques soient comblés.

## Infrastructure disponible pour les concours de 2020

HPC4Health rendra disponibles 500 cœurs CPU et 60To d'espace de stockage.

Caractéristiques des nœuds de calcul :

*   7 nœuds de calcul avec 38 cœurs et mémoire vive de 230Go
*   7 nœuds de calcul avec 38 cœurs et mémoire vive de 125Go
*   10 interconnexions GE
*   60To d'espace évolutif de stockage NFS (*network file system*)

!!! warning "Gestion des sauvegardes"
    Il revient aux utilisateurs de faire leurs propres copies de sauvegarde; ce service (sauvegarde sur bandes) n'est pas fourni par HPC4Health.