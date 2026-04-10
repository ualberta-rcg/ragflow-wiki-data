---
title: "Mounting /project space on a VM in the cloud/fr"
slug: "mounting__project_space_on_a_vm_in_the_cloud"
lang: "fr"

source_wiki_title: "Mounting /project space on a VM in the cloud/fr"
source_hash: "73b98ed2ac4bfd2e0bb68507924bfa01"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:58:58.465496+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Introduction

Nous décrivons ici comment une instance virtuelle peut accéder aux systèmes de fichiers de [l'espace projet](project-layout.md). Avec nos [nuages](cloud.md), les instances infonuagiques ne peuvent directement accéder les grappes de CHP. Pour avoir accès aux fichiers de l'espace projet à partir d'une instance virtuelle, utilisez SSHFS et respectez les exigences particulières.

## SSHFS

SSHFS permet de configurer votre répertoire `/project` dans votre instance. Ces répertoires sont semblables aux autres types de répertoires et vous pouvez y accéder par les commandes Linux régulières.

Pour des informations, consultez [la référence](https://wiki.archlinux.org/index.php/SSHFS).

## Exigences particulières

!!! warning "Pour éviter les problèmes de sécurité, respectez les exigences suivantes :"
    *   NE CONSERVEZ PAS votre mot de passe en texte brut dans l'instance.
    *   Créez une clé SSH EXCLUSIVEMENT pour SSHFS. N'utilisez pas la clé SSH qui sert à vous connecter.
    *   Gardez votre instance à jour et n'ouvrez que les ports sécuritaires qui sont nécessaires.