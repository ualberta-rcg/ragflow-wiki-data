---
title: "Metrix/fr"
slug: "metrix"
lang: "fr"

source_wiki_title: "Metrix/fr"
source_hash: "f04e64ee2de05b5fa2512dfa2dd82be6"
last_synced: "2026-10-04T02:27:33.201522+00:00"
last_processed: "2026-10-04T03:12:29.362300+00:00"

tags:
  []

keywords:
  - "sauts multiples"
  - "paramètre Tensor"
  - "multiplications et convolutions de matrices multidimensionnelles"
  - "script de soumission"
  - "portail Metrix"
  - "quotas des systèmes de fichiers"
  - "opérations en virgule flottante FP64 FP32 FP16"
  - "utilisation des ressources"
  - "disque local"
  - "ressources allouées vs utilisées"
  - "filtrer par statut"
  - "recherche par numéro de tâche"
  - "statistiques des tâches"
  - "visualisation en temps réel"
  - "graphique CPU"
  - "SM occupancy"
  - "mémoire GPU"
  - "systèmes de fichiers"
  - "commandes d’écriture"
  - "tâche CPU"
  - "tâches récentes"
  - "communication MPI"
  - "IOPS et bande passante"
  - "système de fichiers Lustre"
  - "GPU gaspillé"
  - "valeur autour de 50 %"
  - "tâches en cours"
  - "navigation entre les pages"
  - "cycles d'accès du GPU"
  - "CPU gaspillé"
  - "bande passante GPU"
  - "graphique IOPS et bande passante"
  - "job array"
  - "IOPS disque local"
  - "tâche GPU"
  - "IOPS"
  - "statistiques d'un compte CPU"
  - "GPU"
  - "Statistiques d'un compte GPU"
  - "opérations d’entrée/sortie (IOPS)"
  - "mémoire gaspillée"
  - "utilisation des ressources par utilisateur"
  - "bande passante"

questions:
  - "Quels types de ressources et de statistiques le portail Metrix permet‑il de visualiser en temps réel pour les usagers de l’Alliance ?"
  - "Comment accéder aux détails d’une tâche spécifique depuis l’onglet « Sommaire utilisateur » du portail Metrix ?"
  - "Quelles options de visualisation temporelle (semaine, jour, heure) sont proposées pour les graphiques dans les différents onglets du portail ?"
  - "Quels filtres de statut sont proposés pour trier les tâches affichées ?"
  - "Comment rechercher une tâche précise par numéro ou par nom dans l’interface ?"
  - "Quelle option permet de naviguer rapidement entre les pages en effectuant des sauts multiples ?"
  - "Comment accéder aux informations du script de soumission et de la commande de soumission d’une tâche CPU depuis la page de la tâche ?"
  - "Quels indicateurs et graphiques sont disponibles pour suivre l’utilisation des ressources (CPU, mémoire, processus/threads, I/O, bande passante) d’une tâche, et comment les interpréter ?"
  - "Où et comment consulter les informations de l’ordonnanceur ainsi que les statistiques du nœud complet liées à votre compte CPU ?"
  - "Quels types d’opérations sont illustrés par les deux graphiques présentés (IOPS et bande passante) et sur quel support de stockage s’appliquent‑ils ?"
  - "Comment évoluent le nombre d’opérations d’entrée/sortie par seconde (IOPS) et la bande passante du disque local au cours du temps selon les graphiques ?"
  - "En quoi la lecture/écriture sur le système de fichiers Lustre et la communication MPI entre nœuds peuvent‑elles influencer les mesures d’IOPS et de bande passante affichées ?"
  - "Quels éléments sont présentés sur la page d’une tâche GPU et comment accéder aux détails du script et de la commande de soumission ?"
  - "Comment interpréter les différents graphiques de ressources (CPU, Mémoire, Processus/threads, système de fichiers) affichés pour une tâche GPU ?"
  - "Quels indicateurs de performance GPU (SM actif, SM occupancy, Tensor, FP64/FP32/FP16) sont attendus et que signifient leurs valeurs idéales ?"
  - "Quels indicateurs graphiques permettent de suivre l’utilisation et la performance du GPU (mémoire, cycles d’accès, puissance, bande passante PCIe/NVLink) ?"
  - "Comment les statistiques d’un compte CPU sont‑elles présentées et quels aspects de l’utilisation sont détaillés (cœurs demandés, priorité, applications, usage par utilisateur, cœurs et mémoire gaspillés) ?"
  - "Quels graphiques sont disponibles pour surveiller les ressources du nœud complet, notamment la bande passante réseau, les IOPS, l’utilisation du disque local et la puissance consommée ?"
  - "Quelle valeur d’utilisation du GPU est généralement attendue selon le texte ?"
  - "Pourquoi le paramètre « Tensor » doit‑il être le plus élevé possible ?"
  - "Comment le type d’opération en virgule flottante (FP64, FP32 ou FP16) affecte‑t‑il l’activité observée sur le GPU ?"
  - "Que représente le graphique situé à gauche dans la visualisation de votre activité sur les systèmes de fichiers ?"
  - "Quelle donnée est affichée à droite du graphique et comment est‑elle mesurée ?"
  - "Où pouvez‑vous consulter la liste des dernières tâches effectuées pour l’ensemble du groupe ?"
  - "Quels indicateurs sont fournis pour suivre l’utilisation et le gaspillage des GPU, CPU et mémoire au sein d’un groupe d’utilisateurs ?"
  - "Comment les statistiques des machines virtuelles du cloud sont‑elles présentées et quelles métriques peuvent‑on consulter pour chaque instance ?"
  - "De quelle manière le tableau des tâches en cours et les graphiques d’activité du système de fichiers permettent‑ils de surveiller la charge et les performances du compte GPU ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Aperçu

Le portail Metrix est un site web destiné aux usagers de l'Alliance. Il exploite les informations collectées sur les nœuds de calcul et les serveurs de gestion pour générer, de manière interactive, des données permettant aux usagers de suivre en temps réel leur utilisation des ressources (CPU, GPU, mémoire, système de fichiers).

| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| :------ | :--------------------------------------- |
| Narval  | [https://metrix.narval.alliancecan.ca](https://metrix.narval.alliancecan.ca)   |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)         |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca)          |
| Vulcan  | [https://metrix.vulcan.alliancecan.ca](https://metrix.vulcan.alliancecan.ca)   |

**Performance des systèmes de fichiers**

Des indicateurs sur les bandes passantes et les opérations sur les métadonnées sont offerts, avec des options de visualisation pour la dernière semaine, le dernier jour et la dernière heure.

**Nœuds de connexion**

Les statistiques d’utilisation des CPU, de la mémoire, de la charge système et du réseau sont présentées ici, avec les options de visualisation suivantes : dernière semaine, dernier jour et dernière heure.

**Ordonnancement**

Cette section présente des statistiques sur les cœurs et les GPU alloués de la grappe, avec les options de visualisation suivantes : dernière semaine, dernier jour et dernière heure.

**Logiciels scientifiques**

Les logiciels les plus utilisés avec les cœurs CPU et les GPU sont présentés.

**Nœuds de transfert de données**

Les statistiques de bande passante des nœuds de transfert de données sont présentées dans cette section.

## Sommaire usager

Sous l'onglet « Sommaire usager », vous trouverez vos quotas des différents systèmes de fichiers, suivis de vos 10 dernières tâches. Vous pouvez en sélectionner une par son numéro pour accéder à la page détaillée. De plus, en cliquant sur le lien **(Plus de détails)**, vous serez redirigé directement vers l'onglet **Statistiques des tâches**, où vous retrouverez toutes vos tâches.

## Statistiques des tâches

La première section affiche votre utilisation actuelle (cœurs CPU, mémoire et GPU). Ces statistiques représentent la moyenne des ressources utilisées par l’ensemble des tâches en cours d’exécution. Vous pouvez comparer facilement les ressources qui vous sont allouées à celles que vous utilisez réellement.

Une moyenne des derniers jours est aussi présentée.

Ensuite, vous avez une représentation de votre activité sur les systèmes de fichiers. Le nombre d’opérations d’écriture sur disque que vous avez effectuées (*input/output operations per second* (IOPS)) est affiché, de même que la quantité de données transférées vers les serveurs sur une période donnée (bande passante).

La section suivante présente l’ensemble des tâches que vous avez déjà lancées, qui sont actuellement en cours d’exécution ou en attente. On peut filtrer les tâches par statut (OOM, *completed*, *running*, etc.). Il est aussi possible d'effectuer une recherche par numéro de tâche (*Job ID*) ou par nom. Enfin, une option vous permet de naviguer rapidement entre les pages en effectuant des sauts multiples.

### Page d'une tâche CPU

Le nom de la tâche, son numéro, votre nom d'usager et son statut sont affichés en haut de page. Les détails de votre script de soumission s'affichent en cliquant sur le bouton **Voir le script de la tâche**. Si la tâche a été lancée en mode interactif, le script de soumission ne sera pas disponible.

Le répertoire de travail et la commande de soumission sont accessibles en cliquant sur le bouton **Voir la commande de soumission**.

La section suivante est dédiée aux informations de l'ordonnanceur. Vous pouvez accéder à la page de suivi de votre compte CPU en cliquant sur le numéro de votre compte.

Dans la section **Ressources**, vous pouvez obtenir un aperçu initial de l'utilisation des ressources de votre tâche en comparant les colonnes **Alloués** et **Utilisés** pour les différents paramètres listés.

La section **CPU** vous permet de visualiser, au fil du temps, les cœurs CPU que vous avez demandés. Sur le côté droit, vous pouvez sélectionner ou désélectionner les différents cœurs selon vos besoins. Notez que pour des tâches très courtes, cette visualisation n'est pas disponible.

La section **Mémoire** vous permet de visualiser, au fil du temps, l'utilisation de la mémoire que vous avez demandée.

La section **Processus et fils d'exécution** (*Process and threads*) vous permet d'observer différents paramètres liés aux processus et aux fils d'exécution. Idéalement, pour une tâche multifils (*multithreading*), l'addition du paramètre **Fils d'exécution actifs** (*Running threads*) et **Fils d'exécution en veille** (*Sleeping threads*) ne devrait pas dépasser deux fois le nombre de cœurs demandé. Cela dit, il est tout à fait normal d'avoir quelques processus en mode « dormant » (*Sleeping threads*) pour certains types de programmes (Java, Matlab, logiciels commerciaux ou programmes complexes). Les applications du programme exécutées au fil du temps sont aussi présentées comme paramètre.

Les sections suivantes représentent l'utilisation du système de fichiers pour la tâche en cours et non pour le nœud complet. Le nombre d’opérations d’entrée/sortie par seconde (IOPS) est affiché, de même que le débit de transfert de données entre la tâche et le système de fichiers au fil du temps. Ces informations permettent d’identifier les périodes d’activité intense ou de faible utilisation du système de fichiers.

Pour les statistiques des ressources du nœud au complet, sachez qu'elles peuvent être imprécises si le nœud est partagé entre plusieurs usagers. L'évolution de la bande passante utilisée par la tâche au fil du temps, en lien avec les logiciels, les licences, etc., est présentée. De plus, l’évolution de la bande passante réseau utilisée par une tâche ou un ensemble de tâches via le réseau Infiniband, au fil du temps, est illustrée. On peut y observer les périodes de transfert massif de données (ex. : lecture/écriture sur un système de fichiers Lustre, communication MPI entre nœuds).

L’évolution du nombre d’opérations d’entrée/sortie par seconde (IOPS) effectuées sur le disque local au fil du temps est affichée. L'évolution de la bande passante utilisée sur le disque local au fil du temps, c’est-à-dire la quantité de données lues ou écrites par seconde, est également présentée.

La représentation de l’utilisation de l’espace disque local est offerte.

La représentation de la puissance utilisée est offerte.

### Page d'une tâche CPU (vecteur de tâches, *job array*)

La page d'une tâche CPU dans un vecteur de tâches est identique à celle d'une tâche CPU régulière, à l'exception de la section **Autres tâches du vecteur** (*Other jobs in the array*). Le tableau liste les autres numéros de tâches faisant partie du même vecteur de tâches, ainsi que des informations sur leur statut, leur nom, leur heure de début et leur heure de fin.

### Page d'une tâche GPU

En haut de page, vous avez le nom de la tâche, son numéro, votre nom d'usager ainsi que le statut. Les détails de votre script de soumission s'affichent en cliquant sur le bouton **Voir le script de la tâche**. Si vous avez lancé une tâche interactive, le script de soumission n'est pas disponible.

Le répertoire et la commande de soumission sont accessibles en cliquant sur le bouton **Voir la commande de soumission**.

La section suivante est réservée aux informations de l'ordonnanceur. Vous pouvez accéder à la page de votre compte GPU en cliquant sur le numéro de votre compte.

Dans la section **Ressources**, vous pouvez obtenir un premier aperçu de l'utilisation des ressources de votre tâche en comparant les colonnes **Alloués** et **Utilisés** pour les différents paramètres listés.

La section **CPU** vous permet de visualiser l'utilisation des cœurs CPU demandés au fil du temps. Sur le côté droit, vous pouvez sélectionner ou désélectionner les différents cœurs selon vos besoins. Notez que pour des tâches très courtes, cette visualisation n'est pas disponible.

La section **Mémoire** vous permet de visualiser l'utilisation dans le temps de la mémoire que vous avez demandée pour les CPU.

La section **Processus et fils d'exécution** (*Process and threads*) vous permet d'observer différents paramètres liés aux processus et aux fils d'exécution.

Les sections suivantes représentent l'utilisation du système de fichiers pour la tâche en cours et non pour le nœud complet. Le nombre d’opérations d’entrée/sortie par seconde (IOPS) est affiché, de même que le débit de transfert de données entre la tâche et le système de fichiers au fil du temps. Ces informations permettent d’identifier les périodes d’activité intense ou de faible utilisation du système de fichiers.

La section **GPU** représente votre utilisation des GPU. Le paramètre **Multiprocésseurs de diffusion actifs** (*Streaming Multiprocessors* (SM) *active*) indique le pourcentage de temps pendant lequel le GPU exécute un *warp* (un groupe de *threads* consécutifs) dans la dernière fenêtre d’échantillonnage. Cette valeur devrait idéalement se situer autour de 80 %. Pour le **Taux d'occupation des SM** (*SM occupancy*) (défini comme le rapport entre le nombre de *warps* affectés à un SM et le nombre maximal de *warps* qu’un SM peut gérer), une valeur autour de 50 % est généralement attendue. Concernant le paramètre **Tensor**, la valeur devrait être la plus élevée possible. Idéalement, votre code devrait exploiter cette partie du GPU, optimisée pour les multiplications et convolutions de matrices multidimensionnelles. Enfin, pour les opérations en virgule flottante (*Floating Point*) FP64, FP32 et FP16, vous devriez observer une activité significative sur un seul de ces types, selon la précision utilisée par votre code.

La mémoire utilisée par le GPU est affichée. De plus, une visualisation des cycles d'accès du GPU à la mémoire est offerte, représentant le pourcentage de cycles pendant lesquels l’interface mémoire de l’appareil est active pour envoyer ou recevoir des données.

La puissance GPU affiche l’évolution de la consommation énergétique (en watts) du GPU au fil du temps.

La bande passante GPU sur le bus PCIe (*PCI Express*, pour *Peripheral Component Interconnect Express*) est présentée. De même que la bande passante GPU sur le bus NVLink. Le bus NVLink est une technologie développée par NVIDIA pour permettre une communication ultra-rapide entre plusieurs GPU.

Pour les statistiques des ressources du nœud au complet, sachez qu'elles peuvent être imprécises si le nœud est partagé entre plusieurs usagers. L'évolution de la bande passante utilisée par la tâche au fil du temps, en lien avec les logiciels, les licences, etc., est présentée. De plus, l’évolution de la bande passante réseau utilisée par une tâche ou un ensemble de tâches via le réseau Infiniband, au fil du temps, est illustrée. On peut y observer les périodes de transfert massif de données (ex. : lecture/écriture sur un système de fichiers Lustre, communication MPI entre nœuds).

L’évolution du nombre d’opérations d’entrée/sortie par seconde (IOPS) effectuées sur le disque local au fil du temps est affichée. L'évolution de la bande passante utilisée sur le disque local au fil du temps, c’est-à-dire la quantité de données lues ou écrites par seconde, est également présentée.

La représentation de l’utilisation de l’espace disque local est offerte.

La représentation de la puissance utilisée est offerte.

## Statistiques d'un compte

La section **Statistiques d'un compte** regroupe l'utilisation de votre groupe dans deux sous-sections : CPU et GPU.

### Statistiques d'un compte CPU

Vous y trouverez la somme des demandes de votre groupe pour les cœurs CPU, ainsi que leur utilisation correspondante au cours des derniers mois. Vous pouvez également suivre l'évolution de votre priorité, qui varie en fonction de votre utilisation.

Les applications les plus couramment utilisées sont affichées.

L'utilisation des ressources par chacun des usagers de votre groupe peut être consultée.

L’évolution dans le temps des cœurs CPU gaspillés par chaque usager du groupe est présentée.

L’utilisation de la mémoire par chacun des usagers de votre groupe peut être consultée.

La mémoire gaspillée par chaque usager est représentée.

Ensuite, vous avez une représentation de votre activité sur les systèmes de fichiers. Le nombre de commandes d’écriture sur disque que vous avez effectuées (*input/output operations per second* (IOPS)) est affiché. La quantité de données transférées vers les serveurs sur une période donnée (bande passante) est également visible.

Une liste des dernières tâches qui ont été effectuées pour l'ensemble du groupe est disponible.

### Statistiques d'un compte GPU

Vous retrouvez ici la somme des demandes GPU de votre groupe, ainsi que l'utilisation correspondante au cours des derniers mois. Vous pouvez également suivre l’évolution de votre priorité, qui varie en fonction de votre utilisation.

Les applications les plus couramment utilisées sont représentées.

L’utilisation des ressources par chacun des usagers de votre groupe peut être consultée.

La quantité de GPU gaspillés par usager, au fil du temps, est représentée.

Les cœurs CPU alloués et utilisés dans vos tâches GPU sont présentés.

Cette section illustre le gaspillage des CPU dans le cadre de vos tâches GPU.

Vous pouvez visualiser l'utilisation de la mémoire pour chaque usager de votre groupe.

La mémoire gaspillée par chaque usager est illustrée.

Ensuite, vous avez une représentation de votre activité sur les systèmes de fichiers. Le nombre de commandes d’écriture sur disque que vous avez effectuées (*input/output operations per second* (IOPS)) est affiché. La quantité de données transférées vers les serveurs sur une période donnée (bande passante) est également visible.

Voici la liste des dernières tâches effectuées au niveau de votre groupe.

## Statistiques du cloud

Le tableau **Vos instances** présente l'ensemble des machines virtuelles associées à un compte. La colonne **Saveur** fait référence au [type de machine virtuelle](../cloud/virtual_machine_flavors.md). La colonne **UUID** correspond à un identifiant unique attribué à chaque machine virtuelle.

Chaque machine virtuelle dispose de ses propres statistiques d'utilisation (cœurs CPU, mémoire, bande passante disque, IOPS disque et bande passante réseau) affichables pour le dernier mois, la dernière semaine, le dernier jour ou la dernière heure.