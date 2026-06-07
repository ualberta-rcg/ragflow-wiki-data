---
title: "Metrix/fr"
slug: "metrix"
lang: "fr"

source_wiki_title: "Metrix/fr"
source_hash: "75cf031f6aabccaea8adf051e213caef"
last_synced: "2026-06-07T00:07:37.701416+00:00"
last_processed: "2026-06-07T00:22:26.654585+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

# Aperçu

Le portail Metrix est un site web destiné aux usagers de l'Alliance. Il exploite les informations collectées sur les nœuds de calcul et les serveurs de gestion pour générer, de manière interactive, des données permettant aux usagers de suivre en temps réel leur utilisation des ressources (CPU, GPU, mémoire, système de fichiers).

| Rorqual | [https://metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca) |
| :------ | :------------------------------------------------------------------------- |
| Narval  | [http://metrix.narval.alliancecan.ca](http://metrix.narval.alliancecan.ca)   |
| Nibi    | [https://portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)         |
| tamIA   | [https://portail.tamia.ecpia.ca](https://portail.tamia.ecpia.ca)           |
| Vulcan  | [http://metrix.vulcan.alliancecan.ca](http://metrix.vulcan.alliancecan.ca) |

**Performance des systèmes de fichiers**

Les bandes passantes et les opérations sur les métadonnées sont présentées, accompagnées des options de visualisation suivantes : dernière semaine, dernier jour et dernière heure.

**Nœuds de connexion**

Les statistiques d’utilisation des CPU, de la mémoire, de la charge système et du réseau sont présentées dans cet onglet, avec les options de visualisation suivantes : dernière semaine, dernier jour et dernière heure.

**Ordonnancement**

Cet onglet présente des statistiques sur les cœurs et les GPU alloués de la grappe, avec les options de visualisation suivantes : dernière semaine, dernier jour et dernière heure.

**Logiciels scientifiques**

Les logiciels les plus utilisés avec les cœurs CPU et les GPU sont présentés.

**Nœuds de transfert de données**

Les statistiques de bande passante des nœuds de transfert de données sont présentées dans cet onglet.

# Sommaire utilisateur

Sous l'onglet Sommaire utilisateur, vous trouverez vos quotas des différents systèmes de fichiers, suivis de vos 10 dernières tâches. Vous pouvez en sélectionner une par son numéro et accéder à la page détaillée. De plus, en cliquant sur le bouton **(Plus de détails)**, vous serez redirigé directement vers l'onglet **Statistiques des tâches**, où vous retrouverez toutes vos tâches.

# Statistiques des tâches

Le premier bloc affiche votre utilisation actuelle (Cœurs CPU, mémoire et GPU). Ces statistiques représentent la moyenne des ressources utilisées par l’ensemble des tâches en cours d’exécution. Vous pouvez comparer facilement les ressources qui vous sont allouées à celles que vous utilisez réellement.

Vous avez ensuite accès à une moyenne des derniers jours.

Vous avez ensuite une représentation de votre activité sur les systèmes de fichiers. À gauche, le nombre de commandes d’écriture sur disque que vous avez effectuées est affiché (input/output operations per second (IOPS)). À droite, vous voyez la quantité de données transférées vers les serveurs sur une période donnée (Bande passante).

La section suivante présente l’ensemble des tâches que vous avez déjà lancées, qui sont actuellement en cours d’exécution ou en attente. En haut à gauche, vous pouvez filtrer les tâches par statut (OOM, completed, running, etc.). En haut à droite, vous pouvez effectuer une recherche par numéro de tâche (ID de tâche) ou par nom. Enfin, en bas à droite, une option vous permet de naviguer rapidement entre les pages en effectuant des sauts multiples.

## Page d'une tâche CPU

En haut, vous avez le nom de la tâche, son numéro, votre nom d'utilisateur ainsi que le statut. Les détails de votre script de soumission s'affichent en cliquant sur le bouton **Voir le script de la tâche**. Si la tâche a été lancée en mode interactif, le script de soumission ne sera pas disponible.

Le répertoire de travail et la commande de soumission sont accessibles en cliquant sur le bouton **Voir la commande de soumission**.

La prochaine section est dédiée aux informations de l'ordonnanceur. Vous pouvez accéder à la page de suivi de votre compte CPU en cliquant sur le numéro de votre compte.

Dans la section **Ressources**, vous pouvez obtenir un aperçu initial de l'utilisation des ressources de votre tâche en comparant les colonnes **Alloués** et **Utilisés** pour les différents paramètres listés.

La section **CPU** vous permet de visualiser, dans le temps, les cœurs CPU que vous avez demandés. Vous pouvez sélectionner ou désélectionner les différents cœurs selon vos besoins. Notez que pour les tâches très courtes, ces données ne sont pas disponibles.

La section **Mémoire** vous permet de visualiser, dans le temps, l'utilisation de la mémoire que vous avez demandée.

La section **Process and threads** vous permet d'observer différents paramètres liés aux processus et aux fils d'exécution. Idéalement, pour une tâche multifils (multithreading), l'addition du paramètre **Running threads** et **Sleeping threads** ne devrait pas dépasser deux fois le nombre de cœurs demandé. Cela dit, il est tout à fait normal d'avoir quelques processus en mode **dormant** (*Sleeping threads*) pour certains types de programmes (Java, Matlab, logiciels commerciaux ou programmes complexes). Les applications du programme exécutées au fil du temps sont également affichées.

Les sections suivantes représentent l'utilisation du système de fichiers pour la tâche en cours et non pour le nœud au complet. À gauche, le nombre d’opérations d’entrée/sortie par seconde (IOPS) est affiché. À droite, le débit de transfert de données entre la tâche et le système de fichiers au fil du temps est illustré. Cette section permet d’identifier les périodes d’activité intense ou de faible utilisation du système de fichiers.

Pour les statistiques des ressources du nœud au complet, sachez qu'elles peuvent être imprécises si le nœud est partagé entre plusieurs utilisateurs. L'évolution de la bande passante utilisée par la tâche au fil du temps, en lien avec les logiciels, les licences, etc., est illustrée. L'évolution de la bande passante réseau utilisée par une tâche ou un ensemble de tâches via le réseau Infiniband, au fil du temps, est également représentée. On peut y observer les périodes de transfert massif de données (ex. : lecture/écriture sur un système de fichiers (Lustre), communication MPI entre nœuds).

L’évolution du nombre d’opérations d’entrée/sortie par seconde (IOPS) effectuées sur le disque local au fil du temps est illustrée. L’évolution de la bande passante utilisée sur le disque local au fil du temps, c’est-à-dire la quantité de données lues ou écrites par seconde, est aussi présentée.

L’utilisation de l’espace disque local est représentée.

La puissance utilisée est représentée.

## Page d'une tâche CPU (vecteur de tâches, *job array*)

La page d'une tâche CPU dans un vecteur de tâches est identique à celle d'une tâche CPU régulière, à l'exception de la section *Other jobs in the array*. Cette section liste les autres numéros de tâches faisant partie du même vecteur de tâches, ainsi que des informations sur leur statut, leur nom, leur heure de début et leur heure de fin.

## Page d'une tâche GPU

En haut de page, vous avez le nom de la tâche, son numéro, votre nom d'utilisateur ainsi que le statut. Les détails de votre script de soumission s'affichent en cliquant sur le bouton **Voir le script de la tâche**. Si vous avez lancé une tâche interactive, le script de soumission n'est pas disponible.

Le répertoire et la commande de soumission sont accessibles en cliquant sur le bouton **Voir la commande de soumission**.

La section suivante est réservée aux informations de l'ordonnanceur. Vous pouvez accéder à la page de votre compte GPU en cliquant sur le numéro de votre compte.

Dans la section **Ressources**, vous pouvez obtenir un premier aperçu de l'utilisation des ressources de votre tâche en comparant les colonnes **Alloués** et **Utilisés** pour les différents paramètres listés.

La section **CPU** vous permet de visualiser l'utilisation des cœurs CPU demandés au fil du temps. Vous pouvez sélectionner ou désélectionner les différents cœurs selon vos besoins. Notez que pour les tâches très courtes, ces données ne sont pas disponibles.

La section **Mémoire** vous permet de visualiser l'utilisation dans le temps de la mémoire que vous avez demandée pour les CPU.

La section **Process and threads** vous permet d'observer différents paramètres liés aux processus et aux fils d'exécution.

Les sections suivantes représentent l'utilisation du système de fichiers pour la tâche en cours et non pour le nœud au complet. À gauche, le nombre d’opérations d’entrée/sortie par seconde (IOPS) est affiché. À droite, le débit de transfert de données entre la tâche et le système de fichiers au fil du temps est illustré. Cette section permet d’identifier les périodes d’activité intense ou de faible utilisation du système de fichiers.

La section **GPU** représente votre utilisation des GPU. Le paramètre *Streaming Multiprocessors* (SM) actif indique le pourcentage de temps pendant lequel le GPU exécute un warp (un groupe de *threads* consécutifs) dans la dernière fenêtre d’échantillonnage. Cette valeur devrait idéalement se situer autour de 80 %. Pour le *SM occupancy* (défini comme le rapport entre le nombre de warps affectés à un SM et le nombre maximal de warps qu’un SM peut gérer), une valeur autour de 50 % est généralement attendue. Concernant le paramètre *Tensor*, la valeur devrait être la plus élevée possible. Idéalement, votre code devrait exploiter cette partie du GPU, optimisée pour les multiplications et convolutions de matrices multidimensionnelles. Enfin, pour les opérations en virgule flottante (*Floating Point*) FP64, FP32 et FP16, vous devriez observer une activité significative sur un seul de ces types, selon la précision utilisée par votre code.

La mémoire utilisée par le GPU est indiquée. Les cycles d'accès du GPU à la mémoire sont également affichés, représentant le pourcentage de cycles pendant lesquels l’interface mémoire de l’appareil est active pour envoyer ou recevoir des données.

La puissance GPU affiche l’évolution de la consommation énergétique (en watts) du GPU au fil du temps.

La bande passante GPU sur le bus PCIe (ou **PCI Express**, pour *Peripheral Component Interconnect Express*) est présentée, de même que la bande passante GPU sur le bus NVlink. Le bus NVLink est une technologie développée par NVIDIA pour permettre une communication ultra-rapide entre plusieurs GPU.

Pour les statistiques des ressources du nœud au complet, sachez qu'elles peuvent être imprécises si le nœud est partagé entre plusieurs utilisateurs. L'évolution de la bande passante utilisée par la tâche au fil du temps, en lien avec les logiciels, les licences, etc., est illustrée. L'évolution de la bande passante réseau utilisée par une tâche ou un ensemble de tâches via le réseau Infiniband, au fil du temps, est également représentée. On peut y observer les périodes de transfert massif de données (ex. : lecture/écriture sur un système de fichiers (Lustre), communication MPI entre nœuds).

L’évolution du nombre d’opérations d’entrée/sortie par seconde (IOPS) effectuées sur le disque local au fil du temps est illustrée. L’évolution de la bande passante utilisée sur le disque local au fil du temps, c’est-à-dire la quantité de données lues ou écrites par seconde, est aussi présentée.

L’utilisation de l’espace disque local est représentée.

La puissance utilisée est représentée.

# Statistiques d'un compte

La section **Statistiques d'un compte** regroupe l'utilisation de votre groupe dans deux sous-sections : CPU et GPU.

## Statistiques d'un compte CPU

Vous y trouverez la somme des demandes de votre groupe pour les cœurs CPU, ainsi que leur utilisation correspondante au cours des derniers mois. Vous pouvez également suivre l'évolution de votre priorité, qui varie en fonction de votre utilisation.

Les applications les plus couramment utilisées sont présentées.

Vous pouvez consulter ici l'utilisation des ressources par chacun des utilisateurs de votre groupe.

L’évolution dans le temps des cœurs CPU gaspillés par chaque utilisateur du groupe est affichée.

Vous pouvez consulter ici l’utilisation de la mémoire par chacun des utilisateurs de votre groupe.

La mémoire gaspillée par chaque utilisateur est représentée.

Vous avez ensuite une représentation de votre activité sur les systèmes de fichiers. À gauche, le nombre de commandes d’écriture sur disque que vous avez effectuées est affiché (input/output operations per second (IOPS)). À droite, vous voyez la quantité de données transférées vers les serveurs sur une période donnée (Bande passante).

Vous avez une liste des dernières tâches qui ont été effectuées pour l'ensemble du groupe.

## Statistiques d'un compte GPU

Vous retrouvez ici la somme des demandes GPU de votre groupe, ainsi que l'utilisation correspondante au cours des derniers mois. Vous pouvez également suivre l’évolution de votre priorité, qui varie en fonction de votre utilisation.

Les applications les plus couramment utilisées sont présentées.

Vous pouvez consulter ici l’utilisation des ressources par chacun des utilisateurs de votre groupe.

L'évolution dans le temps de la quantité de GPU gaspillés par utilisateur est présentée.

Vous avez ensuite les cœurs CPU alloués et utilisés dans vos tâches GPU.

Le gaspillage des CPU dans le cadre de vos tâches GPU est illustré.

Vous pouvez visualiser ici l'utilisation de la mémoire pour chaque utilisateur de votre groupe.

La mémoire gaspillée par chaque utilisateur est illustrée.

Vous avez ensuite une représentation de votre activité sur les systèmes de fichiers. À gauche, le nombre de commandes d’écriture sur disque que vous avez effectuées est affiché (input/output operations per second (IOPS)). À droite, vous voyez la quantité de données transférées vers les serveurs sur une période donnée (Bande passante).

Voici la liste des dernières tâches effectuées au niveau de votre groupe.

# Statistiques du cloud

Le premier tableau « Vos instances » présente l'ensemble des machines virtuelles associées à un compte. La colonne « Saveur » fait référence au [type de machine virtuelle](../cloud/virtual_machine_flavors.md). La colonne « UUID » correspond à un identifiant unique attribué à chaque machine virtuelle.

Chaque machine virtuelle dispose ensuite de ses propres statistiques d'utilisation (Cœurs CPU, Mémoire, Bande passante disque, IOPS disque et Bande passante réseau) qui peuvent être affichées pour le dernier mois, la dernière semaine, le dernier jour ou la dernière heure.