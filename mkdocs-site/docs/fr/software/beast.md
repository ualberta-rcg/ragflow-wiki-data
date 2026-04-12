---
title: "BEAST/fr"
slug: "beast"
lang: "fr"

source_wiki_title: "BEAST/fr"
source_hash: "9b878f7c40303297e7588d9feccf74cb"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:41:14.287807+00:00"

tags:
  - software

keywords:
  - "BEAGLE-lib"
  - "Server machines"
  - "input_beast.xml"
  - "extensions"
  - "SNAPP"
  - "beagle-lib"
  - "Commande Java"
  - "SBATCH"
  - "Script simple"
  - "BEAST"
  - "BEAST2"
  - "Script demandant plus de mémoire"
  - "analyse bayésienne MCMC"
  - "phylogénies"

questions:
  - "À quoi sert principalement l'application BEAST et quelles méthodes d'analyse utilise-t-elle ?"
  - "Comment charger le module BEAST dans son environnement et quelles dépendances sont chargées simultanément ?"
  - "Quelles commandes doivent être utilisées pour installer des extensions selon la version de BEAST (antérieure ou supérieure à 2.5.1) ?"
  - "Quel est l'objectif principal du script bash fourni et quelle version du logiciel BEAST utilise-t-il ?"
  - "Comment la variable de mémoire Java (`BEAST_MEM`) doit-elle être configurée par rapport à la mémoire demandée au système (`--mem-per-cpu`) ?"
  - "De quelle manière les chemins d'accès aux bibliothèques, comme BEAGLE, sont-ils définis et intégrés dans la commande d'exécution Java ?"
  - "À quoi sert le paquet SNAPP mentionné dans le texte ?"
  - "Où peut-on trouver des informations supplémentaires sur la gestion des paquets BEAST2 pour les machines serveurs ?"
  - "Quels sont les paramètres d'allocation de ressources définis dans l'en-tête du script simple fourni ?"
  - "Quel est l'objectif principal du script bash fourni et quelle version du logiciel BEAST utilise-t-il ?"
  - "Comment la variable de mémoire Java (`BEAST_MEM`) doit-elle être configurée par rapport à la mémoire demandée au système (`--mem-per-cpu`) ?"
  - "De quelle manière les chemins d'accès aux bibliothèques, comme BEAGLE, sont-ils définis et intégrés dans la commande d'exécution Java ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

[BEAST](http://www.beast2.org/) est une application multiplateforme pour l’analyse bayésienne MCMC de séquences moléculaires, spécifiquement pour les phylogénies enracinées chronologiques inférées par des modèles d’horloge moléculaire stricte ou relaxée. On l’utilise comme méthode de reconstruction de phylogénies, mais BEAST est aussi un environnement de test pour les hypothèses sur l’évolution sans conditionnement d’une topologie arborescente. La méthode MCMC est utilisée pour faire la moyenne d’une partie d’un arbre afin que chacun des arbres reçoive un poids proportionnel à sa probabilité antérieure.

BEAST peut utiliser la [bibliothèque de haute performance beagle-lib](https://github.com/beagle-dev/beagle-lib) pour effectuer les calculs à la base des bibliothèques phylogénétiques bayésiennes ou utilisant l’estimation du maximum de vraisemblance.

## Utilisation

Le chargement du module BEAST avec `module load beast` charge également les modules dépendants `beagle-lib` et `java`, et configure la variable d’environnement `EBROOTBEAST` pour la diriger vers le répertoire qui contient les fichiers de l’application.

### Extensions

BEAST est installé sans paquets d'extension. Pour les ajouter à votre répertoire personnel, utilisez les commandes suivantes :
*   `packagemanager` pour les versions de BEAST 2.5.1 et ultérieures;
*   `addonmanager` pour les versions antérieures à 2.5.1.

=== "BEAST 2.5.x et versions ultérieures"

    ```bash
    module load beast/2.5.1
    packagemanager -list
    ```

    | Nom     | Statut d'installation | Dernière version | Dépendances | Description
    | :------ | :-------------------- | :--------------- | :---------- | :----------------------------------
    | BEAST   | 2.5.1                 | 2.5.0            |             | Cœur de BEAST
    | bacter  | N/A                   | 2.2.0            |             | Inférence d'ARG bactériens.
    | BADTRIP | N/A                   | 1.0.0            |             | Inférence du temps de transmission pour [...]
    | SNAPP   | N/A                   | 1.4.1            |             | Phylogénies SNP et AFLP
    
    ```bash
    packagemanager -add SNAPP
    ```

    Le paquet SNAPP est installé dans `~/.beast/2.5/SNAPP`.

    ```bash
    packagemanager -list
    ```

    | Nom     | Statut d'installation | Dernière version | Dépendances | Description
    | :------ | :-------------------- | :--------------- | :---------- | :----------------------------------
    | BEAST   | 2.5.1                 | 2.5.0            |             | Cœur de BEAST
    | SNAPP   | 1.4.1                 | 1.4.1            |             | Phylogénies SNP et AFLP

=== "BEAST 2.4.x et versions antérieures"

    ```bash
    module load beast/2.4.0
    addonmanager -list
    ```

    | Nom     | Statut d'installation | Dernière version | Dépendances | Description
    | :------ | :-------------------- | :--------------- | :---------- | :--------------------------------------------
    | BEAST   | 2.4.0                 | 2.4.8            |             | Cœur de BEAST
    | bacter  | non installé          | 1.2.3            |             | Inférence d'ARG bactériens.
    | BASTA   | non installé          | 2.3.2            |             | Approximation bayésienne structurée du coalescent
    | SNAPP   | non installé          | 1.3.0            |             | Phylogénies SNP et AFLP

    ```bash
    addonmanager -add SNAPP
    ```

    Le paquet SNAPP est installé dans `~/.beast/2.4/SNAPP`.

    ```bash
    addonmanager -list
    ```

    | Nom     | Statut d'installation | Dernière version | Dépendances | Description
    | :------ | :-------------------- | :--------------- | :---------- | :--------------------------------------------
    | BEAST   | 2.4.0                 | 2.4.8            |             | Cœur de BEAST
    | SNAPP   | 1.3.0                 | 1.3.0            |             | Phylogénies SNP et AFLP

Pour plus d'informations, consultez la section *Machines serveurs* à l'adresse suivante : http://www.beast2.org/managing-packages/.

### Script de base

```bash title="simple_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=2000M

module load beast/2.6.3

beast input_beast.xml
```

### Script nécessitant plus de mémoire

```bash title="high_memory_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=4000M

# Augmenter la mémoire maximale ici si nécessaire :
# "BEAST_MEM" doit être de 250 Mo inférieur à "--mem="
BEAST_MEM="-Xmx3750M"

module load beast/2.6.3

# Définir les variables pour localiser BEAST et BEAGLE-lib
BEAST_LIB="${EBROOTBEAST}/lib"
BEAST_EXTRA_LIBS="${BEAST_LIB}:${BEAGLE_LIB}"
export LD_LIBRARY_PATH="${BEAGLE_LIB}:${LD_LIBRARY_PATH}"

# Construire une longue commande Java :
CMD="java -Xms256m ${BEAST_MEM}"                                           # définir la mémoire
CMD="$CMD -Djava.library.path=${BEAST_EXTRA_LIBS}"                         # indiquer les bibliothèques
CMD="$CMD -cp ${BEAST_LIB}/launcher.jar beast.app.beastapp.BeastLauncher" # programme à exécuter

echo ".................................."
echo "La commande Java est : \"${CMD}\""
echo ".................................."

# Exécuter la commande :
$CMD -beagle  input_beast.xml
```

## Références

*   [BEAST](http://www.beast2.org/)