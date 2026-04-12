---
title: "Building a Software Carpentry style lesson on the wiki/fr"
slug: "building_a_software_carpentry_style_lesson_on_the_wiki"
lang: "fr"

source_wiki_title: "Building a Software Carpentry style lesson on the wiki/fr"
source_hash: "67766df556e4fa4c012525633ed434c5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:51:48.068810+00:00"

tags:
  []

keywords:
  - "tutoriels"
  - "syntaxe Markdown"
  - "gabarits"
  - "wiki"
  - "Software Carpentry"

questions:
  - "Quels sont les avantages d'héberger des tutoriels Software Carpentry sur un wiki selon le texte ?"
  - "Quels sont les différents gabarits (templates) disponibles pour structurer le contenu des leçons ?"
  - "Quelle est la syntaxe à utiliser pour intégrer ces boîtes de formatage spécifiques dans le wiki ?"
  - "Quels sont les avantages d'héberger des tutoriels Software Carpentry sur un wiki selon le texte ?"
  - "Quels sont les différents gabarits (templates) disponibles pour structurer le contenu des leçons ?"
  - "Quelle est la syntaxe à utiliser pour intégrer ces boîtes de formatage spécifiques dans le wiki ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Il peut être intéressant d'utiliser notre wiki pour présenter des tutoriels Software Carpentry. GitHub héberge des leçons de Software Carpentry comme [celle-ci](http://swcarpentry.github.io/shell-novice/); elles sont préparées avec la syntaxe Markdown qui offre plusieurs gabarits préformatés. L'hébergement d'un tutoriel sur un wiki a aussi l'avantage d'en permettre aisément la traduction. Nous présentons ici quelques gabarits utiles.

## Prérequis

La boîte de prérequis typique de SWC peut être obtenue en utilisant le gabarit `{{Prerequisites}}`. Par exemple, le code suivant :

```text
{{Prerequisites
  |title=Prerequisites for this lesson
  |content=
This lesson requires you to first know X.
}}
```

donne la boîte suivante :

!!! warning "Prérequis pour cette leçon"
    Cette leçon exige que vous connaissiez d'abord X.

## Préparation

La boîte de « préparation » de SWC peut être obtenue en utilisant le gabarit `{{Getready}}`. Par exemple, le code suivant :

```text
{{Getready
  |title=Getting ready for this lesson
  |content=
You should download the following files prior to starting the lesson.
}}
```

donne la boîte suivante :

!!! info "Préparation pour cette leçon"
    Vous devriez télécharger les fichiers suivants avant de commencer la leçon.

## Objectifs d'apprentissage

La boîte d'« objectifs » de SWC peut être obtenue en utilisant le gabarit `{{Objectives}}`. Par exemple, le code suivant :

```text
{{Objectives
  |title=Learning Objectives
  |content=
* You will learn A
* You will also learn B
}}
```

donne la boîte suivante :

!!! success "Objectifs d'apprentissage"
    * Vous apprendrez A
    * Vous apprendrez également B

## Mises en évidence

La boîte de « mise en évidence » de SWC peut être obtenue en utilisant le gabarit `{{Callout}}`. Par exemple, le code suivant :

```text
{{Callout
  |title=Using auto completion
  |content=
You can use the <TAB> key to auto complete.
}}
```

donne la boîte suivante :

!!! tip "Utilisation de l'autocomplétion"
    Vous pouvez utiliser la touche <kbd>TAB</kbd> pour l'autocomplétion.

## Défi

La boîte de « défi » de SWC peut être obtenue en utilisant le gabarit `{{Challenge}}`. Par exemple, le code suivant :

```text
{{Challenge
  |title=Practicing using the commands.
  |content=
Assuming a ...
}}
```

donne la boîte suivante :

!!! question "Pratique des commandes"
    En supposant qu'un...