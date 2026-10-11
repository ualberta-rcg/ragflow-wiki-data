---
title: "Trillium/fr"
slug: "trillium"
lang: "fr"

source_wiki_title: "Trillium/fr"
source_hash: "b5cf0c30d90b2b3880d4c1934a92c466"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:39:55.758255+00:00"

tags:
  []

keywords:
  - "système de fichiers VAST haute performance"
  - "excédent de chaleur réutilisé"
  - "réseau Infiniband Nvidia NDR 400 Gbit/s"
  - "grappe Trillium"
  - "capacité effective de 29Po"
  - "authentification multifacteur"
  - "sous-grappe de GPU"
  - "ordonnancement"
  - "GPU multi‑instances (MIG) non possibles"
  - "RStudio"
  - "refroidisseurs à sec"
  - "JupyterLab"
  - "Open OnDemand"
  - "PUE sous 1.03"
  - "ressources de la sous-grappe de CPU"
  - "nœuds entiers de 192 cœurs"
  - "circuit fermé"
  - "refroidissement eau 35‑40 °C PUE < 1.03"
  - "VS Code"
  - "nœuds GPU NVidia H100/H200"
  - "stockage parallèle 29 pétaoctets"
  - "Trillium"
  - "archivage HPSS 114Po"
  - "Open OnDemand (JupyterLab"
  - "RStudio)"
  - "efficacité énergétique"

questions:
  - "Quels sont les différents types de nœuds (CPU et GPU) disponibles sur la grappe Trillium et quelles sont leurs spécifications principales (nombre de cœurs, mémoire, processeurs et cartes graphiques) ?"
  - "Comment le système de refroidissement à eau de 35‑40 °C assure‑t‑il une efficacité énergétique élevée (PUE < 1,03) et la réutilisation de la chaleur excédentaire ?"
  - "Quels services d’accès aux données et d’interaction (stockage parallèle, collections Globus, Open OnDemand, portails, nœuds de copie) sont mis à disposition des utilisateurs de Trillium ?"
  - "Quels sont les principales caractéristiques du système de fichiers VAST (capacité, bande passante, IOPS, protocoles d’accès) ?"
  - "Quelles sont les limites et les règles d’utilisation des espaces de stockage /home, /project, /scratch et /nearline pour les utilisateurs ?"
  - "Comment les utilisateurs doivent‑ils se connecter à Trillium (authentification, clés SSH, MFA) et quels sont les accès autorisés (internet, Open OnDemand) ?"
  - "Quelle est la plage de température de l'eau mentionnée et quels avantages cela procure-t-elle ?"
  - "Comment le système de refroidissement décrit atteint-il un indicateur PUE inférieur à 1,03 ?"
  - "De quelle manière l'excédent de chaleur est-il réutilisé pour réduire l'empreinte écologique ?"
  - "Quels outils et environnements de développement (JupyterLab, VS Code, RStudio, MATLAB, ParaView, DDT) sont accessibles via Open OnDemand sur Trillium ?"
  - "Comment Open OnDemand remplace-t-il JupyterHub dans la configuration de Trillium ?"
  - "Quelles fonctionnalités supplémentaires, comme le terminal et la soumission de tâches à l’ordonnanceur, Open OnDemand met‑il à disposition des utilisateurs ?"
  - "Comment les ressources de la sous‑grappe de CPU sont‑elles allouées aux travaux ?"
  - "De quelle manière les ressources de la sous‑grappe de GPU sont‑elles attribuées, et quelles restrictions s’appliquent‑elles (notamment concernant les instances MIG) ?"
  - "Où les utilisateurs peuvent‑ils obtenir des informations complémentaires sur l’ordonnancement sur Trillium ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Résumé rapide de Trillium

<div class="table-container">
| Caractéristique | Détails |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disponibilité** | 7 août 2025 |
| **Nœuds de connexion** | * sous-grappe de CPU, `trillium.alliancecan.ca`<br>* sous-grappe de GPU, `trillium-gpu.alliancecan.ca` |
| **Collections Globus** | [alliancecan#trillium](https://app.globus.org/file-manager?origin_id=ad462f99-8436-42b4-adc6-3644e36c1b67) (système de fichiers)<br>[alliancecan#hpss](https://app.globus.org/file-manager?origin_id=c55ce750-19d6-4a42-9c30-6a58f06bec7a) (archive/nearline) |
| **Nœuds de copie (rsync, scp, sftp,...)** | `tri-dm{1,2,3,4}.scinet.utoronto.ca` |
| **Nœuds d'automatisation** | * sous-grappe de CPU, `robot{1,2,3,4}.scinet.utoronto.ca`<br>* sous-grappe de GPU, `trig-robot1.scinet.utoronto.ca` |
| **Open OnDemand** | [ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (inclut JupyterLab) |
| **Portail** | [my.scinet.utoronto.ca](https://my.scinet.utoronto.ca) |
</div>

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

<div class="table-container">
| Nœud de connexion | Quantité de nœuds | Cœurs par nœud | Mémoire disponible par nœud | Processeur(s) | GPU(s) |
| :----------------------------------- | :--------------- | :------------- | :-------------------------- | :------------------------------------------------------------------ | :-------------------------------------------------------------------------- |
| `trillium.alliancecan.ca` (sous-grappe de CPU) | 1224 | 192 | 749G ou 767000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.6 GHz, cache L3 de 384Mo | - |
| `trillium-gpu.alliancecan.ca` (sous-grappe de GPU) | 63 | 96 | 749G ou 767000M | 1 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, cache L3 de 384Mo | 4 x NVidia H100 SXM (80Go de mémoire), connexion via NVLink |
| `trillium-gpu.alliancecan.ca` (sous-grappe de GPU) | 1 | 96 | 1498G ou 1534000M | 2 x AMD EPYC 9455 (Zen 5) @ 3.15 GHz, 256MB cache L3 | 4 x NVidia H200 SXM (141GB memory), connected via NVLink |
| `trillium-gpu.alliancecan.ca` (sous-grappe de GPU) | 52 | 96 | 2000G ou 2048000M | 2 x Intel 8558P @ 2.7 GHz, 260MB cache L3 | 8 x NVidia B200 SXM (180 GB memory), connected via NVLink |
</div>

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

Il ne faut pas présumer que Trillium fonctionne comme les autres grappes. Bien que la conformité soit élevée, il y a certaines différences en matière de conception et de politiques parce que Trillium a été conçue pour le calcul à grande échelle.

La description donnée ici n'est pas complète; pour les détails, voir [Trillium : Guide de démarrage](trillium_quickstart.md).

### Se connecter

*   Il n'est pas possible de se connecter avec un mot de passe; vous devez utiliser [des clés SSH](../getting-started/ssh_keys.md) et [l'authentification multifacteur](../getting-started/multifactor_authentication.md).
*   Les sous-grappes de CPU et de GPU n'ont pas les mêmes nœuds de connexion ni les mêmes nœuds d'automatisation.

### Accès à l'internet

*   Il n'est pas possible de se connecter à l'internet à partir d'un nœud de calcul.
*   Cependant, les applications interactives Open OnDemand ont accès à l'internet.

### Espace /home

*   Votre répertoire `$HOME` peut contenir jusqu'à 100Go ou 1 million de fichiers.
*   Les tâches de calcul ne peuvent pas écrire dans `$HOME`.
*   Cependant, les applications interactives Open OnDemand peuvent écrire dans `$HOME`.

### Espace /project

*   Les liens vers vos espaces /project se trouvent dans le répertoire `$HOME/links`.
*   Par défaut, votre compte fournit un espace /project de 1To pour votre groupe.
*   Il n'est pas possible d'obtenir plus d'espace /project via le service d'accès rapide.
*   Les tâches de calcul ne peuvent pas écrire dans `$PROJECT`.

### Espace /scratch

*   Le quota est de 25To pour chaque utilisateur; cependant, vous devriez supprimer les données non utilisées.
*   Aucune procédure de purge n'est établie; cependant, une politique de purge pourrait éventuellement être adoptée.

### Espace /nearline

*   Sur Trillium, le stockage /nearline n'est pas monté sur les nœuds; pour y accéder, il faut soumettre une tâche sur la partition Slurm [HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS) ou encore via [Globus](../getting-started/globus.md).

### Espace disque local

*   Les nœuds de Trillium n'offrent pas de stockage local.
*   Dans certains cas vous pouvez utiliser le disque RAM; pour ce faire, la variable d'environnement `$SLURM_TMPDIR` pointe sur un répertoire du disque RAM.

### Accès via Open OnDemand (OOD)

*   En remplacement de JupyterHub, Trillium est configurée avec [Open OnDemand](../interactive/trillium_open_ondemand_quickstart.md) qui prend en charge plusieurs applications utilisées dans votre navigateur, par exemple JupyterLab, VS Code, RStudio, MATLAB, ParaView et le débogueur DDT. Open OnDemand fournit aussi un terminal et peut être utilisé pour soumettre des tâches à l’ordonnanceur.

### Ordonnancement

*   Les ressources de la sous-grappe de CPU sont allouées par nœuds entiers de 192 cœurs.
*   Les ressources de la sous-grappe de GPU sont allouées par nœuds entiers ou par GPU entiers; les GPU multi-instances (MIG) ne sont pas possibles.

Pour plus d'information sur l'ordonnancement, voir [Trillium : Guide de démarrage](trillium_quickstart.md).