---
title: "Gprof/fr"
slug: "gprof"
lang: "fr"

source_wiki_title: "Gprof/fr"
source_hash: "04c5fe72794ea028d0514fc83a6c2cfc"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:04:35.507538+00:00"

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

# Profileur GNU gprof

## Description
[gprof](https://sourceware.org/binutils/docs/gprof/) est une application de profilage qui collecte de l’information et compile des statistiques sur votre code. De façon générale, gprof trouve les fonctions et les sous-routines dans le programme et y insère des temps de calcul pour chacune. Quand le programme est exécuté, un fichier de données brutes est créé et interprété par gprof qui en tire des statistiques de profilage.

[gprof](https://sourceware.org/binutils/docs/gprof/) est fourni avec la suite GNU et est disponible via le module `gcc`.

## Préparation du code
### Charger le compilateur
Chargez le compilateur GNU approprié; par exemple pour GCC la commande est

```bash
module load gcc/7.3.0
```

### Compiler le code
Compilez d’abord votre code avec la fonction de débogage activée; pour les compilateurs GNU, ceci se fait en ajoutant l’option `-pg` à la commande de compilation. Avec cette option, le compilateur génère du code pour enregistrer l’information qui sert à l’analyse de profilage. Sans cette option, les données pour composer un graphe d’appel ne sont pas collectées et vous pourriez voir le message d’erreur

```
gprof: gmon.out file is missing call-graph data
```

### Exécuter le code
Pour exécuter le code, lancez
```bash
/path/to/your/executable arg1 arg2
```
Faites exécuter le code de la même manière que vous le feriez sans profilage avec gprof; la commande pour l’exécution est la même. Une fois le binaire exécuté et complété sans erreur, le fichier `gmon.out` est créé dans le répertoire courant. Si par exemple votre code change le répertoire courant, `gmon.out` sera créé dans le nouveau répertoire courant, pourvu que le programme dispose des permissions pour ce faire.

### Obtenir les données de profilage
Dans la commande suivante, gprof est exécuté avec en arguments le nom du binaire et le fichier `gmon.out`; le fichier `analysis.txt` sera créé dans le répertoire courant pour contenir toute l’information de profilage.

```bash
gprof /path/to/your/executable gmon.out > analysis.txt