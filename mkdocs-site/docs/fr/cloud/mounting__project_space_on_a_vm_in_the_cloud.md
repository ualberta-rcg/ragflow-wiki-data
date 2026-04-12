---
title: "Mounting /project space on a VM in the cloud/fr"
slug: "mounting__project_space_on_a_vm_in_the_cloud"
lang: "fr"

source_wiki_title: "Mounting /project space on a VM in the cloud/fr"
source_hash: "73b98ed2ac4bfd2e0bb68507924bfa01"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:31:14.855462+00:00"

tags:
  - cloud

keywords:
  - "Instance virtuelle"
  - "SSHFS"
  - "sécurité"
  - "clé SSH"
  - "espace projet"

questions:
  - "Quel outil permet à une instance virtuelle d'accéder aux systèmes de fichiers de l'espace projet ?"
  - "Comment les utilisateurs peuvent-ils interagir avec le répertoire configuré via SSHFS dans leur instance ?"
  - "Quelles sont les exigences de sécurité spécifiques à respecter concernant les mots de passe et les clés SSH ?"
  - "Quel outil permet à une instance virtuelle d'accéder aux systèmes de fichiers de l'espace projet ?"
  - "Comment les utilisateurs peuvent-ils interagir avec le répertoire configuré via SSHFS dans leur instance ?"
  - "Quelles sont les exigences de sécurité spécifiques à respecter concernant les mots de passe et les clés SSH ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Nous décrivons ici comment une instance virtuelle peut accéder aux systèmes de fichiers de [l'espace projet](../storage-and-data/project_layout.md). Avec nos [nuages](cloud.md), les instances infonuagiques ne peuvent directement accéder les grappes de CHP. Pour avoir accès aux fichiers de l'espace projet à partir d'une instance virtuelle, utilisez SSHFS et respectez les exigences particulières.

## SSHFS

SSHFS permet de configurer votre répertoire `/project` dans votre instance. Ces répertoires sont semblables aux autres types de répertoires et vous pouvez y accéder par les commandes Linux régulières.

Pour plus d'informations, consultez [cette référence sur SSHFS](https://wiki.archlinux.org/index.php/SSHFS).

## Exigences particulières

!!! warning "Exigences de sécurité"
    Pour éviter les problèmes de sécurité, respectez les exigences suivantes :

    *   NE CONSERVEZ PAS votre mot de passe en texte brut dans l'instance.
    *   Créez une clé SSH EXCLUSIVEMENT pour SSHFS. N'utilisez pas la clé SSH qui sert à vous connecter.
    *   Gardez votre instance à jour et n'ouvrez que les ports sécuritaires qui sont nécessaires.