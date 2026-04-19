---
title: "Trillium/fr"
slug: "trillium"
lang: "fr"

source_wiki_title: "Trillium/fr"
source_hash: "359a1b131fdf9c748b843cf9a27ed99f"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:08:04.648628+00:00"

tags:
  []

keywords:
  - "stockage unifié"
  - "Réseau haute performance"
  - "NVMe"
  - "Guide de démarrage"
  - "Stockage parallèle"
  - "sous-grappe de GPU"
  - "capacité effective"
  - "Trillium Quickstart"
  - "Nœuds CPU et GPU"
  - "Efficacité énergétique"
  - "Trillium"
  - "nœuds de calcul"
  - "ordonnancement"
  - "bande passante"
  - "sous-grappe de CPU"
  - "information"
  - "Ordonnancement"
  - "Grappe Trillium"
  - "espace de stockage"
  - "IOPS"
  - "nœuds entiers"
  - "Open OnDemand"

questions:
  - "Quelles sont les caractéristiques matérielles et les capacités du réseau haute performance des nœuds CPU et GPU de la grappe Trillium ?"
  - "Quelles sont les spécifications techniques et les performances de lecture et d'écriture du système de stockage unifié VAST ?"
  - "Comment le système de refroidissement de Trillium fonctionne-t-il pour optimiser l'efficacité énergétique et réduire l'empreinte écologique ?"
  - "Quelles sont les méthodes d'authentification et de connexion requises pour accéder à la grappe Trillium ?"
  - "Quelles sont les règles, restrictions et quotas spécifiques aux différents espaces de stockage (home, project, scratch, nearline) ?"
  - "Comment les ressources de calcul (CPU et GPU) sont-elles allouées lors de l'ordonnancement des tâches ?"
  - "Quelle est la différence entre la capacité de stockage effective et la capacité de mémoire flash brute de ce système ?"
  - "Quelles sont les performances de cet ensemble de stockage en matière de bande passante pour la lecture et l'écriture ?"
  - "Combien d'opérations d'entrée/sortie par seconde (IOPS) ce système peut-il traiter en lecture et en écriture ?"
  - "Quelles sont les fonctionnalités et les logiciels fournis par l'interface Open OnDemand ?"
  - "Comment l'ordonnanceur alloue-t-il les ressources pour la sous-grappe de CPU ?"
  - "Quelles sont les règles et les restrictions d'allocation concernant la sous-grappe de GPU ?"
  - "Sur quel sujet spécifique le texte propose-t-il d'obtenir des informations supplémentaires ?"
  - "Quel est le nom du guide recommandé pour approfondir ce sujet ?"
  - "Quelle action le lecteur est-il invité à faire s'il souhaite en savoir plus ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Clé | Valeur |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------- |
| Disponibilité                        | 7 août 2025                                                                                              |
| Nœuds de connexion                   | * sous-grappe de CPU, **trillium.alliancecan.ca**<br>* sous-grappe de GPU, **trillium-gpu.alliancecan.ca** |
| Collections Globus                   | * **[alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67)** (système de fichiers)<br>* **[alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a)** (archive/nearline) |
| Nœuds de copie (rsync, scp, sftp,...) | **tri-dm{1,2,3,4}.scinet.utoronto.ca**                                                                  |
| Nœuds d'automatisation               | * sous-grappe de CPU, **robot{1,2,3,4}.scinet.utoronto.ca**<br>* sous-grappe de GPU, **trig-robot1.scinet.utoronto.ca** |
| Open OnDemand                        | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (inclut JupyterLab)                 |
| Portail                              | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca)                                                 |

La grappe Trillium est conçue pour prendre en charge des tâches massivement parallèles. Construite par Lenovo Canada, elle est hébergée par SciNet à l'Université de Toronto.

L'utilisation de Trillium est semblable à celle des autres grappes nationales avec cependant certaines particularités. Pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

Si vous aviez accès à Niagara, nous vous encourageons fortement à prendre connaissance de la page [Transition de Niagara vers Trillium](transition_from_niagara_to_trillium.md).

## Stockage
Stockage parallèle : 29 pétaoctets, SSD NVMe de VAST Data.

## Réseau haute performance
*   Réseautique Infiniband Nvidia NDR
    *   400 Gbit/s pour les nœuds CPU
    *   800 Gbit/s pour les nœuds GPU
    *   réseau entièrement non bloquant; les nœuds peuvent communiquer entre eux simultanément sur toute la bande passante

## Caractéristiques des nœuds

| Nœud de connexion                 | Nœuds | Cœurs | Mémoire disponible | CPU                                                  | GPU                                                               |
| :-------------------------------- | :---- | :---- | :----------------- | :--------------------------------------------------- | :---------------------------------------------------------------- |
| **trillium.alliancecan.ca**       | 1224  | 192   | 749G ou 767000M    | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, cache L3 de 384Mo |                                                                   |
| trillium-**gpu**.alliancecan.ca | 63    | 96    | 749G ou 767000M    | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, cache L3 de 384Mo | 4 x NVidia H100 SXM (80Go de mémoire), connexion via NVLink |

## Données techniques

### Refroidissement et efficacité énergétique

Le refroidissement se fait par une eau de 35 à 40 °C, ce qui a les effets suivants :

*   indicateur d'efficacité énergétique (PUE) sous 1.03;
*   refroidisseurs à sec en circuit fermé, sans tours d'évaporation et consommation de nouvelle eau;
*   excédent de chaleur réutilisé pour le chauffage d'installations voisines afin de minimiser l'empreinte écologique.

### Système de stockage

Le système de fichiers VAST haute performance est composé d'un ensemble de stockage unifié de 29Po soutenu par NVMe avec les caractéristiques suivantes :

*   capacité effective de 29Po (dédupliquée via VAST);
*   capacité de mémoire flash brute de 16.7PB;
*   bande passante de 714Go/s en lecture et de 275Go/s en écriture;
*   10 millions d'IOPS en lecture et 2 millions d'IOPS en écriture;
*   protocoles d'accès POSIX et S3 avec un espace de noms unifié;
*   48 CBoxes et 14 DBoxes pour les services de données.

### Sauvegarde et archivage

L'archivage sur ruban /nearline HPSS dispose de 114Po additionnels.

*   Archivage en deux copies dans des bibliothèques géographiquement distinctes;
*   utilisé à des fins de sauvegarde et d'archivage;
*   sauvegardes gérées par le logiciel Atempo.

## Particularités

Il ne faut pas présumer que Trillium fonctionne comme les autres grappes.
Bien que la conformité soit élevée, il y a certaines différences en matière de conception et de politiques parce que Trillium a été conçue pour le calcul à grande échelle.

La description donnée ici n'est pas complète; pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

### Se connecter

*   Il n'est pas possible de se connecter avec un mot de passe; vous devez utiliser [des clés SSH](../getting-started/ssh_keys.md) et [l'authentification multifacteur](../getting-started/multifactor_authentication.md).
*   Les sous-grappes de CPU et de GPU n'ont pas les mêmes nœuds de connexion ni les mêmes nœuds d'automatisation.

### Accès à l'internet
*   Il n'est pas possible de se connecter à l'internet à partir d'un nœud de calcul.
*   Cependant, les applications interactives OnDemand ont accès à l'internet.

### Espace /home

*   Votre répertoire `$HOME` peut contenir jusqu'à 100Go ou 1 million de fichiers.
*   Les tâches de calcul ne peuvent pas écrire dans `$HOME`.
*   Cependant, les applications interactives OnDemand peuvent écrire dans `$HOME`.

### Espace /project

*   Les liens vers vos espaces `/project` se trouvent dans le répertoire `$HOME/links`.
*   Par défaut, votre compte fournit un espace `/project` de 1To pour votre groupe.
*   Il n'est pas possible d'obtenir plus d'espace `/project` via le service d'accès rapide.

les tâches de calcul ne peuvent pas écrire dans `$PROJECT`

### Espace /scratch

*   Le quota est de 25To pour chaque utilisateur; cependant, vous devriez supprimer les données non utilisées.
*   Aucune procédure de purge n'est établie; cependant, une politique de purge pourrait éventuellement être adoptée.

### Espace /nearline

*   Sur Trillium, le stockage `/nearline` n'est pas monté sur les nœuds; pour y accéder, il faut soumettre une tâche sur la partition Slurm [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) ou encore via [Globus](../getting-started/globus.md).

### Espace disque local

*   Les nœuds de Trillium n'offrent pas de stockage local.
*   Dans certains cas vous pouvez utiliser le disque RAM; pour ce faire, la variable d'environnement `$SLURM_TMPDIR` pointe sur un répertoire du disque RAM.

### Accès via Open OnDemand (OOD)

*   En remplacement de JupyterHub, Trillium est configurée avec [Open OnDemand](../interactive/trillium_open_ondemand_quickstart.md) qui prend en charge plusieurs applications utilisées dans votre navigateur, par exemple JupyterLab, VS Code, RStudio, MATLAB, ParaView et le débogueur DDT. Open OnDemand fournit aussi un terminal et peut être être utilisé pour soumettre des tâches à l’ordonnanceur.

### Ordonnancement

*   Les ressources de la sous-grappe de CPU sont allouées par nœuds entiers de 192 cœurs.
*   Les ressources de la sous-grappe de GPU sont allouées par nœuds entiers ou par GPU entiers; les GPU multi-instances (MIG) ne sont pas possibles.

Pour plus d'information sur l'ordonnancement, voir [Trillium : Guide de démarrage](trillium_quickstart.md).