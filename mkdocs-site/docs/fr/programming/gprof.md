---
title: "Gprof/fr"
slug: "gprof"
lang: "fr"

source_wiki_title: "Gprof/fr"
source_hash: "04c5fe72794ea028d0514fc83a6c2cfc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:45:34.566449+00:00"

tags:
  []

keywords:
  - "gprof"
  - "gmon.out"
  - "compilateur GNU"
  - "statistiques de profilage"
  - "profilage"

questions:
  - "Quel est le rôle principal du profileur GNU gprof et quelles informations permet-il de récolter sur un programme ?"
  - "Quelle option de compilation est indispensable pour permettre la collecte des données de profilage et éviter une erreur lors de l'analyse ?"
  - "Comment génère-t-on le fichier de statistiques final à partir du fichier de données brutes créé après l'exécution du code ?"
  - "Quel est le rôle principal du profileur GNU gprof et quelles informations permet-il de récolter sur un programme ?"
  - "Quelle option de compilation est indispensable pour permettre la collecte des données de profilage et éviter une erreur lors de l'analyse ?"
  - "Comment génère-t-on le fichier de statistiques final à partir du fichier de données brutes créé après l'exécution du code ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Profileur GNU gprof

## Description

[gprof](https://sourceware.org/binutils/docs/gprof/) est une application de profilage qui recueille des informations et compile des statistiques sur votre code. En règle générale, gprof identifie les fonctions et les sous-routines dans le programme et y insère des marqueurs pour mesurer le temps d'exécution de chacune. Quand le programme est exécuté, un fichier de données brutes est créé, puis interprété par gprof pour en extraire des statistiques de profilage.

[gprof](https://sourceware.org/binutils/docs/gprof/) est inclus dans la suite GNU et est accessible via le module `gcc`.

## Préparation du code

### Charger le compilateur

Chargez le compilateur GNU adéquat; par exemple, pour GCC, la commande est :

```bash
module load gcc/7.3.0
```

### Compiler le code

Commencez par compiler votre code avec la fonction de débogage activée. Pour les compilateurs GNU, cela se fait en ajoutant l'option `-pg` à la commande de compilation. Avec cette option, le compilateur génère le code nécessaire pour enregistrer les informations utiles à l'analyse de profilage. Sans elle, les données pour construire un graphe d'appel ne sont pas recueillies, et vous risquez de voir le message d'erreur suivant :

```
gprof: gmon.out file is missing call-graph data
```

### Exécuter le code

Pour exécuter le code, lancez la commande suivante :

```bash
/path/to/your/executable arg1 arg2
```

Exécutez le code de la même façon que vous le feriez sans profilage gprof; la commande d'exécution demeure identique. Une fois le binaire exécuté et terminé sans erreur, le fichier `gmon.out` est créé dans le répertoire de travail actuel. Si, par exemple, votre code modifie le répertoire de travail, `gmon.out` sera alors créé dans ce nouveau répertoire, à condition que le programme ait les permissions nécessaires.

### Obtenir les données de profilage

Dans la commande ci-dessous, gprof est exécuté avec, comme arguments, le nom de l'exécutable et le fichier `gmon.out`. Le fichier `analysis.txt` sera créé dans le répertoire de travail actuel et contiendra toutes les informations de profilage.

```bash
gprof /path/to/your/executable gmon.out > analysis.txt