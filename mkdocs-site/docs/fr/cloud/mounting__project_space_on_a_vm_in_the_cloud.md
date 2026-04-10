---
title: "Mounting /project space on a VM in the cloud/fr"
tags:
  - cloud

keywords:
  []
---

### Introduction

Nous décrivons ici comment une instance virtuelle peut accéder aux systèmes de fichiers de [l'espace projet](project-layout-fr.md). Avec nos [nuages](cloud-fr.md), les instances infonuagiques ne peuvent directement accéder les grappes de CHP. Pour avoir accès aux fichiers de l'espace projet à partir d'une instance virtuelle, utilisez SSHFS et respectez les exigences particulières.

### SSHFS

SSHFS permet de configurer votre répertoire `/project` dans votre instance. Ces répertoires sont semblables aux autres types de répertoires et vous pouvez y accéder par les commandes Linux régulières.

Pour des informations, consultez la référence https://wiki.archlinux.org/index.php/SSHFS.

<span id="Requirements"></span>
### Exigences particulières

Pour éviter les problèmes de sécurité, respectez les exigences suivantes :

* NE CONSERVEZ PAS votre mot de passe en texte brut dans l'instance.
* Créez une clé SSH EXCLUSIVEMENT pour SSHFS. N'utilisez pas la clé SSH qui sert à vous connecter.
* Gardez votre instance à jour et n'ouvrez que les ports sécuritaires qui sont nécessaires.