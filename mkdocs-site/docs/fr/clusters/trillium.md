---
title: "Trillium/fr"
slug: "trillium"
lang: "fr"

source_wiki_title: "Trillium/fr"
source_hash: "85e3147cf054ca7cc7da741065b33fc6"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:16:41.805873+00:00"

tags:
  []

keywords:
  - "GPU NVidia H100 SXM"
  - "grappe Trillium"
  - "MATLAB"
  - "29Po"
  - "espace /project de 1 To"
  - "protocoles d'accès POSIX et S3"
  - "stockage parallèle 29 pétaoctets"
  - "ordonnancement des nœuds CPU et GPU"
  - "ordonnancement"
  - "Ordonnancement"
  - "Guide de démarrage"
  - "réseau Infiniband Nvidia NDR 400 Gbit/s / 800 Gbit/s"
  - "voir"
  - "Trillium Quickstart"
  - "RStudio"
  - "stockage unifié"
  - "information"
  - "refroidissement à eau 35‑40 °C avec PUE < 1.03"
  - "Open OnDemand"
  - "GPU multi‑instances (MIG) non possibles"
  - "authentification multifacteur"
  - "10 millions d'IOPS"
  - "NVMe"
  - "bande passante de 714 Go/s"

questions:
  - "Quelles sont les spécifications principales des nœuds CPU et GPU du cluster Trillium (nombre de cœurs, mémoire, processeurs et GPU) ?"
  - "Comment le système de stockage VAST Data du cluster est‑il configuré en termes de capacité effective, bande passante et performances IOPS ?"
  - "Quels sont les mécanismes de refroidissement du cluster Trillium et son indicateur d’efficacité énergétique (PUE), ainsi que la réutilisation de la chaleur excédentaire ?"
  - "Quels protocoles d’accès et quels quotas de stockage sont disponibles sur Trillium pour les espaces /home, /project, /scratch et /nearline ?"
  - "Comment les utilisateurs doivent‑ils s’authentifier et quelles sont les restrictions d’accès à Internet et aux nœuds de calcul sur le système ?"
  - "Quels outils d’accès à distance (Open OnDemand, JupyterLab, VS Code, etc.) et quelles règles d’ordonnancement (allocation CPU/GPU) sont proposés aux utilisateurs de Trillium ?"
  - "Quelle est la capacité effective de stockage après déduplication et comment est‑elle obtenue ?"
  - "Quelles sont les performances en bande passante et en IOPS du système en lecture et en écriture ?"
  - "Quelle est la capacité brute de mémoire flash du système et quel type de technologie de stockage (NVMe) utilise‑t‑il ?"
  - "Quels environnements de développement et de visualisation sont accessibles via Open OnDemand sur le système ?"
  - "De quelle manière Open OnDemand permet‑il de soumettre des tâches à l’ordonnanceur ?"
  - "Comment les ressources des sous‑grappes CPU et GPU sont‑elles allouées, et quelles limitations s’appliquent aux GPU ?"
  - "Où peut‑on trouver des informations supplémentaires sur l'ordonnancement ?"
  - "Quel document est indiqué comme guide de démarrage pour Trillium ?"
  - "À quoi renvoie le lien « Trillium : Guide de démarrage » dans ce contexte ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Disponibilité | 7 août 2025 |
|---|---|
| Nœuds de connexion | * sous-grappe de CPU, **`trillium.alliancecan.ca`** <br> * sous-grappe de GPU, **`trillium-gpu.alliancecan.ca`** |
| Collections Globus | [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67) (système de fichiers) <br> [alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) (archive/nearline) |
| Nœuds de copie | `tri-dm{1,2,3,4}.scinet.utoronto.ca` (rsync, scp, sftp,...) |
| Nœuds d'automatisation | * sous-grappe de CPU, `robot{1,2,3,4}.scinet.utoronto.ca` <br> * sous-grappe de GPU, `trig-robot1.scinet.utoronto.ca` |
| Open OnDemand | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (inclut JupyterLab) |
| Portail | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca) |

La grappe Trillium est conçue pour prendre en charge des tâches massivement parallèles. Construite par Lenovo Canada, elle est hébergée par SciNet à l'Université de Toronto.

L'utilisation de Trillium est semblable à celle des autres grappes nationales, avec cependant certaines particularités. Pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

Si vous aviez accès à Niagara, nous vous encourageons fortement à prendre connaissance de la page [Transition de Niagara vers Trillium](transition_from_niagara_to_trillium.md).

## Stockage
Stockage parallèle : 29 pétaoctets, SSD NVMe de VAST Data.

## Réseau haute performance
* Réseautique Infiniband Nvidia NDR
    * 400 Gbit/s pour les nœuds CPU
    * 800 Gbit/s pour les nœuds GPU
    * réseau entièrement non bloquant; les nœuds peuvent communiquer entre eux simultanément sur toute la bande passante

## Caractéristiques des nœuds

| Nœud de connexion | Nœuds | Cœurs par nœud | Mémoire disponible | Processeurs (CPU) | Accélérateurs (GPU) |
|---|---|---|---|---|---|
| `trillium.alliancecan.ca` | 1224 | 192 | 749 Go ou 767000 Mo | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, cache L3 de 384 Mo | - |
| `trillium-gpu.alliancecan.ca` | 63 | 96 | 749 Go ou 767000 Mo | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, cache L3 de 384 Mo | 4 x NVidia H100 SXM (80 Go de mémoire), connexion via NVLink |

## Données techniques

### Refroidissement et efficacité énergétique

Le refroidissement se fait par une eau de 35 à 40 °C, ce qui a les effets suivants :

* indicateur d'efficacité énergétique (PUE) sous 1.03;
* refroidisseurs à sec en circuit fermé, sans tours d'évaporation et consommation de nouvelle eau;
* excédent de chaleur réutilisé pour le chauffage d'installations voisines afin de minimiser l'empreinte écologique.

### Système de stockage

Le système de fichiers VAST haute performance est composé d'un ensemble de stockage unifié de 29 Po soutenu par NVMe avec les caractéristiques suivantes :

* capacité effective de 29 Po (dédupliquée via VAST);
* capacité de mémoire flash brute de 16,7 Po;
* bande passante de 714 Go/s en lecture et de 275 Go/s en écriture;
* 10 millions d'IOPS en lecture et 2 millions d'IOPS en écriture;
* protocoles d'accès POSIX et S3 avec un espace de noms unifié;
* 48 CBoxes et 14 DBoxes pour les services de données.

### Sauvegarde et archivage

L'archivage sur ruban /nearline HPSS dispose de 114 Po additionnels.

* Archivage en deux copies dans des bibliothèques géographiquement distinctes;
* utilisé à des fins de sauvegarde et d'archivage;
* sauvegardes gérées par le logiciel Atempo.

## Particularités

Il ne faut pas présumer que Trillium fonctionne comme les autres grappes. Bien que la conformité soit élevée, il y a certaines différences en matière de conception et de politiques parce que Trillium a été conçue pour le calcul à grande échelle.

La description donnée ici n'est pas complète; pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

### Se connecter

* Il n'est pas possible de se connecter avec un mot de passe; vous devez utiliser [des clés SSH](../getting-started/ssh_keys.md) et [l'authentification multifacteur](../getting-started/multifactor_authentication.md).
* Les sous-grappes de CPU et de GPU n'ont pas les mêmes nœuds de connexion ni les mêmes nœuds d'automatisation.

### Accès à l'internet

* Il n'est pas possible de se connecter à l'internet à partir d'un nœud de calcul.
* Cependant, les applications interactives OnDemand ont accès à l'internet.

### Espace /home

* Votre répertoire `$HOME` peut contenir jusqu'à 100 Go ou 1 million de fichiers.
* Les tâches de calcul ne peuvent pas écrire dans `$HOME`.
* Cependant, les applications interactives OnDemand peuvent écrire dans `HOME`.

### Espace /project

* Les liens vers vos espaces /project se trouvent dans le répertoire `$HOME/links`.
* Par défaut, votre compte fournit un espace /project de 1 To pour votre groupe.
* Il n'est pas possible d'obtenir plus d'espace /project via le service d'accès rapide.
* Les tâches de calcul ne peuvent pas écrire dans `$PROJECT`.

### Espace /scratch

* Le quota est de 25 To pour chaque utilisateur; cependant, vous devriez supprimer les données non utilisées.
* Aucune procédure de purge n'est établie; cependant, une politique de purge pourrait éventuellement être adoptée.

### Espace /nearline

* Sur Trillium, le stockage /nearline n'est pas monté sur les nœuds; pour y accéder, il faut soumettre une tâche sur la partition Slurm [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) ou encore via [Globus](../getting-started/globus.md).

### Espace disque local

* Les nœuds de Trillium n'offrent pas de stockage local.
* Dans certains cas, vous pouvez utiliser le disque RAM; pour ce faire, la variable d'environnement `$SLURM_TMPDIR` pointe sur un répertoire du disque RAM.

### Accès via Open OnDemand (OOD)

* En remplacement de JupyterHub, Trillium est configurée avec [OpenOnDemand](../interactive/trillium_open_ondemand_quickstart.md) qui prend en charge plusieurs applications utilisées dans votre navigateur, par exemple JupyterLab, VS Code, RStudio, MATLAB, ParaView et le débogueur DDT. Open OnDemand fournit aussi un terminal et peut être utilisé pour soumettre des tâches à l’ordonnanceur.

### Ordonnancement

* Les ressources de la sous-grappe de CPU sont allouées par nœuds entiers de 192 cœurs.
* Les ressources de la sous-grappe de GPU sont allouées par nœuds entiers ou par GPU entiers; les GPU multi-instances (MIG) ne sont pas possibles.

Pour plus d'information sur l'ordonnancement, voir [Trillium : Guide de démarrage](trillium_quickstart.md).