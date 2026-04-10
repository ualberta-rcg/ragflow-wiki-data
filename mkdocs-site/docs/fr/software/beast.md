---
title: "BEAST/fr"
slug: "beast"
lang: "fr"

source_wiki_title: "BEAST/fr"
source_hash: "9b878f7c40303297e7588d9feccf74cb"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:50:20.605449+00:00"

tags:
  - software

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

## Description

[BEAST](http://www.beast2.org/) est une application multiplateforme pour l’analyse bayésienne MCMC de séquences moléculaires, spécifiquement pour les phylogénies enracinées chronologiques inférées par des modèles d’horloge moléculaire stricte ou relaxée. On l’utilise comme méthode de reconstruction de phylogénies, mais BEAST est aussi un environnement de test pour les hypothèses sur l’évolution sans conditionnement d’une topologie arborescente. MCMC est utilisée pour faire la moyenne d’une partie d’un arbre pour que chacun des arbres reçoive un poids proportionnel à sa probabilité antérieure.

BEAST peut utiliser la bibliothèque hautement performante [beagle-lib](https://github.com/beagle-dev/beagle-lib) pour effectuer les calculs à la base des bibliothèques phylogénétiques bayésiennes ou utilisant l’estimation du *maximum de similitude*.

## Utilisation

Charger le module BEAST avec `module load beast` charge également les modules dépendants `beagle-lib` et `java` et configure la variable d’environnement `EBROOTBEAST` pour la diriger vers le répertoire qui contient les fichiers de l’application.

### Extensions

BEAST est installé sans paquets d'extension. Pour les ajouter à votre répertoire `/home`, utilisez les commandes suivantes :

*   `packagemanager` pour les versions à partir de 2.5.1;
*   `addonmanager` pour les versions antérieures.

!!! note "Gestion des paquets d'extension"
    La commande à utiliser pour gérer les paquets d'extension dépend de la version de BEAST.

#### BEAST version 2.5.x et ultérieure

```bash
module load beast/2.5.1
packagemanager -list
```

| Nom     | État d'installation | Dernière version | Dépendances | Description                           |
| :------ | :------------------ | :--------------- | :---------- | :------------------------------------ |
| BEAST   | 2.5.1               | 2.5.0            |             | Cœur de BEAST                         |
| bacter  | NA                  | 2.2.0            |             | Inférence d'ARG bactérien.            |
| BADTRIP | NA                  | 1.0.0            |             | Inférence du temps de transmission pour [...] |
| [...]   |                     |                  |             |                                       |
| SNAPP   | NA                  | 1.4.1            |             | Phylogénies SNP et AFLP               |
| [...]   |                     |                  |             |                                       |

```bash
packagemanager -add SNAPP
```
Le paquet SNAPP est installé dans `~/.beast/2.5/SNAPP`.

```bash
packagemanager -list
```

| Nom     | État d'installation | Dernière version | Dépendances | Description                           |
| :------ | :------------------ | :--------------- | :---------- | :------------------------------------ |
| BEAST   | 2.5.1               | 2.5.0            |             | Cœur de BEAST                         |
| [...]   |                     |                  |             |                                       |
| SNAPP   | 1.4.1               | 1.4.1            |             | Phylogénies SNP et AFLP               |
| [...]   |                     |                  |             |                                       |

#### BEAST version 2.4.x et antérieure

```bash
module load beast/2.4.0
addonmanager -list
```

| Nom     | État d'installation | Dernière version | Dépendances | Description                                          |
| :------ | :------------------ | :--------------- | :---------- | :--------------------------------------------------- |
| BEAST   | 2.4.0               | 2.4.8            |             | Cœur de BEAST                                        |
| bacter  | non installé        | 1.2.3            |             | Inférence d'ARG bactérien.                           |
| BASTA   | non installé        | 2.3.2            |             | Approximation bayésienne du coalescent structuré.    |
| [...]   |                     |                  |             |                                                      |
| SNAPP   | non installé        | 1.3.0            |             | Phylogénies SNP et AFLP                              |
| [...]   |                     |                  |             |                                                      |

```bash
addonmanager -add SNAPP
```
Le paquet SNAPP est installé dans `~/.beast/2.4/SNAPP`.

```bash
addonmanager -list
```

| Nom     | État d'installation | Dernière version | Dépendances | Description                                          |
| :------ | :------------------ | :--------------- | :---------- | :--------------------------------------------------- |
| BEAST   | 2.4.0               | 2.4.8            |             | Cœur de BEAST                                        |
| [...]   |                     |                  |             |                                                      |
| SNAPP   | 1.3.0               | 1.3.0            |             | Phylogénies SNP et AFLP                              |
| [...]   |                     |                  |             |                                                      |

Pour plus d’information, voyez la section *Machines serveur* dans [http://www.beast2.org/managing-packages/](http://www.beast2.org/managing-packages/).

### Script simple

```sh title="simple_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=2000M

module load beast/2.6.3

beast input_beast.xml
```

### Script demandant plus de mémoire

```sh title="high_memory_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=4000M

# Augmentez la mémoire maximale ici si nécessaire :
# La variable "BEAST_MEM" doit être de 250 Mo inférieure à "--mem="
BEAST_MEM="-Xmx3750M"

module load beast/2.6.3

# Définir les variables pour localiser BEAST et BEAGLE-lib
BEAST_LIB="${EBROOTBEAST}/lib"
BEAST_EXTRA_LIBS="${BEAST_LIB}:${BEAGLE_LIB}"
export LD_LIBRARY_PATH="${BEAGLE_LIB}:${LD_LIBRARY_PATH}"

# Construire une longue commande Java :
CMD="java -Xms256m ${BEAST_MEM}"                                           # définir la mémoire
CMD="$CMD -Djava.library.path=${BEAST_EXTRA_LIBS}"                         # pointer vers les bibliothèques
CMD="$CMD -cp ${BEAST_LIB}/launcher.jar beast.app.beastapp.BeastLauncher" # programme à exécuter

echo ".................................."
echo "La commande Java est \"${CMD}\""
echo ".................................."

# Exécuter la commande :
$CMD -beagle  input_beast.xml
```

## Références
[BEAST](http://www.beast2.org/)