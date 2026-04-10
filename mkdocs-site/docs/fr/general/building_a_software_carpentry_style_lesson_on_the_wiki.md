---
title: "Building a Software Carpentry style lesson on the wiki/fr"
slug: "building_a_software_carpentry_style_lesson_on_the_wiki"
lang: "fr"

source_wiki_title: "Building a Software Carpentry style lesson on the wiki/fr"
source_hash: "67766df556e4fa4c012525633ed434c5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:00:50.044528+00:00"

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

Il peut être intéressant d'utiliser notre wiki pour présenter des tutoriels Software Carpentry. GitHub héberge des leçons de Software Carpentry comme [celle-ci](http://swcarpentry.github.io/shell-novice/); elles sont préparées avec la syntaxe Markdown qui offre plusieurs gabarits préformatés. L'hébergement d'un tutoriel sur un wiki a aussi l'avantage d'en permettre aisément la traduction. Nous présentons ici quelques gabarits utiles.

## Prérequis
L'encadré typique de prérequis SWC peut être obtenu en utilisant le gabarit `{{Prerequisites}}`. Par exemple, le code suivant
```text
{{Prerequisites
  |title=Prerequisites for this lesson
  |content=
This lesson requires you to first know X.
}}
```
donne l'encadré suivant:
!!! info "Prérequis pour cette leçon"
    Cette leçon exige que vous connaissiez d'abord X.

## Préparation
L'encadré "préparation" SWC peut être obtenu en utilisant le gabarit `{{Getready}}`. Par exemple, le code suivant
```text
{{Getready
  |title=Getting ready for this lesson
  |content=
You should download the following files prior to starting the lesson.
}}
```
donne l'encadré suivant:
!!! tip "Préparation pour cette leçon"
    Vous devriez télécharger les fichiers suivants avant de commencer la leçon.

## Objectifs d'apprentissage
L'encadré "objectifs" SWC peut être obtenu en utilisant le gabarit `{{Objectives}}`. Par exemple, le code suivant
```text
{{Objectives
  |title=Learning Objectives
  |content=
* You will learn A
* You will also learn B
}}
```
donne l'encadré suivant:
!!! info "Objectifs d'apprentissage"
    * Vous apprendrez A
    * Vous apprendrez également B

## Encadrés
L'encadré "encadré" SWC peut être obtenu en utilisant le gabarit `{{Callout}}`. Par exemple, le code suivant
```text
{{Callout
  |title=Using auto completion
  |content=
You can use the <TAB> key to auto complete.
}}
```
donne l'encadré suivant:
!!! note "Utilisation de l'autocomplétion"
    Vous pouvez utiliser la touche <kbd>TAB</kbd> pour l'autocomplétion.

## Défi
L'encadré "défi" SWC peut être obtenu en utilisant le gabarit `{{Challenge}}`. Par exemple, le code suivant
```text
{{Challenge
  |title=Practicing using the commands.
  |content=
Assuming a ...
}}
```
donne l'encadré suivant:
!!! question "Pratiquer l'utilisation des commandes"
    En supposant un ...