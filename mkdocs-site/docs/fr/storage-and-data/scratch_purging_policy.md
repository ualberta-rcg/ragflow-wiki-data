---
title: "Scratch purging policy/fr"
slug: "scratch_purging_policy"
lang: "fr"

source_wiki_title: "Scratch purging policy/fr"
source_hash: "969d9f12a88691d702b86a5e103f0dd3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:23:50.248510+00:00"

tags:
  []

keywords:
  - "espace /scratch"
  - "dépassement de quota"
  - "délai de grâce"
  - "âge d'un fichier"
  - "suppression de fichiers"
  - "fichiers purgés"
  - "liens symboliques"
  - "noms de fichiers"
  - "chemin complet"
  - "mis à jour"
  - "copier un dossier"
  - "purge automatique"
  - "lien symbolique"
  - "purge de fichiers"

questions:
  - "Quels sont les critères utilisés pour déterminer si un fichier doit être automatiquement supprimé de l'espace /scratch sur la majorité des grappes ?"
  - "En quoi la politique de gestion de l'espace de stockage sur la grappe Nibi diffère-t-elle de la procédure standard de purge ?"
  - "Comment les utilisateurs peuvent-ils consulter la liste de leurs fichiers programmés pour la purge et quelles mesures doivent-ils prendre pour les conserver ?"
  - "Comment le calendrier d'accès et de modification des fichiers influence-t-il leur purge potentielle ?"
  - "Comment le système détermine-t-il l'âge exact d'un fichier et quelles pratiques de contournement sont interdites ?"
  - "Quelle est la méthode recommandée pour copier de manière sécurisée un dossier contenant des liens symboliques depuis l'espace /scratch ?"
  - "Que signifie la présence d'un fichier à votre nom dans le répertoire mentionné ?"
  - "Quelles informations détaillées peut-on trouver à l'intérieur de ce fichier ?"
  - "À quelles dates précises de chaque mois ce fichier est-il mis à jour ?"
  - "Comment le calendrier d'accès et de modification des fichiers influence-t-il leur purge potentielle ?"
  - "Comment le système détermine-t-il l'âge exact d'un fichier et quelles pratiques de contournement sont interdites ?"
  - "Quelle est la méthode recommandée pour copier de manière sécurisée un dossier contenant des liens symboliques depuis l'espace /scratch ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Gestion et types de stockage](storage-and-file-management.md)*

Sur nos grappes, le système de fichiers `/scratch` sert au stockage rapide et temporaire des données utilisées en cours d'exécution. Pour leur part, les données qui doivent être stockées à long terme et les données de référence sont enregistrées dans l'espace `/project` ou dans une des zones d'archivage; voir les [types de stockage](storage-and-file-management.md#types-de-stockage). Pour toujours garder suffisamment d'espace `/scratch`, les fichiers de plus de 60 jours sont supprimés périodiquement en fonction de leur âge. Notez que c'est l'âge d'un fichier qui détermine s'il sera purgé et non l'endroit où il se trouve dans `/scratch`; le fait de déplacer un fichier dans un autre répertoire de `/scratch` ne l'empêchera pas d'être supprimé.

!!! note "Remarque"
    Nibi ne purge pas les fichiers comme les autres grappes ([voir ci-dessous](#nibi)).

L'avantage du mécanisme basé sur les quotas est de vous laisser le plein contrôle et d'empêcher que certains fichiers particuliers d'une collection disparaissent en raison d'un âge quelque peu différent.

## Procédure

### Fir, Narval, Rorqual, Trillium

À la fin de chaque mois, les fichiers susceptibles d'être supprimés le 15 du mois suivant sont repérés. Si vous possédez au moins un de ces fichiers, un message d'avertissement s'affiche au début du mois et vous recevez un avis par courriel; cet avis contient aussi un fichier qui liste tous les fichiers susceptibles d'être supprimés. Vous avez donc deux semaines pour copier vers `/project` ou un autre emplacement tous les fichiers que vous voulez conserver.

Le 12 du mois, un dernier courriel de notification vous est envoyé; il contient une évaluation actualisée des fichiers susceptibles d'être supprimés le 15. Vous disposez ainsi de 72 heures pour les déplacer. Le 15 au soir, tous les fichiers qui restent dans `/scratch` dont les valeurs pour `ctime` et `atime` datent de plus de 60 jours sont supprimés. Ces notifications sont un service offert à nos utilisateurs; vous êtes cependant responsable de veiller à ce que les fichiers de plus de 60 jours ne se trouvent pas dans l'espace `/scratch`.
Une fois vos données déplacées, veuillez supprimer les fichiers et répertoires d'origine dans `/scratch` au lieu de les laisser en attente de la purge automatique.

### Nibi

*   Si vous utilisez moins de 1 To (limite souple), vous n'avez rien à faire et aucun fichier ne sera automatiquement supprimé.
*   Lorsque vous dépassez cette *limite souple*, une condition de dépassement de quota est déclenchée, qui inclut un délai de grâce de 60 jours.
*   À l'expiration de ce délai, la procédure de dépassement de quota s'applique et interdit toute nouvelle allocation. Ceci fait que vos fichiers sont toujours accessibles, mais l'ajout ou l'augmentation de la taille des fichiers échouera et générera une erreur.
*   Pour résoudre ce problème, votre utilisation doit être modifiée et être sous la limite souple de 1 To, ce qui *remet le compteur du délai de grâce à zéro*.
*   Il existe également un quota ferme de 20 To. Ceci signifie que, même avec un délai de grâce de 60 jours, vous ne pouvez pas dépasser 20 To dans `/scratch`.

## Fichiers à être purgés

*   Sur Fir et Narval, allez à `**/scratch/to_delete/**` et localisez le fichier à votre nom.
*   Sur Trillium, allez à `**/scratch/t/to_delete/**` ou établissez un lien symbolique (`symlink`) vers `**/scratch/t/todelete/current**`.

S'il y a un fichier à votre nom, certains de vos fichiers sont susceptibles d'être purgés. Ce fichier contient la liste des noms de fichiers avec le chemin complet et possiblement d'autres renseignements comme la taille, atime, ctime, etc. Ce fichier est seulement mis à jour le 1er et le 12e jour de chaque mois.

Si vous accédez à un ou plusieurs fichiers ou les lisez, les déplacez ou les supprimez entre le 1er et le 11 du mois, aucune modification ne sera faite à la liste avant le 12.

Si un fichier avec votre nom existe avant le 11 mais pas le 12, aucun de vos fichiers n'est susceptible d'être purgé.

Si vous accédez à un ou plusieurs fichiers ou les lisez, les déplacez ou les supprimez après le 12 du mois, vous devrez confirmer si les fichiers peuvent ou non être purgés le 15 (voir ci-dessous).

## Connaître l'âge d'un fichier

L'âge d'un fichier est déterminé par la plus récente valeur entre
*   `atime`, le moment du dernier accès et
*   `ctime`, le moment de la dernière modification.

Vous pouvez obtenir ces valeurs avec la commande

```bash
stat <nom_de_fichier>
```

La valeur de (`mtime`) n'est pas utilisée car elle peut désigner une date lointaine dans le passé qui a été modifiée par vous ou par les programmes que vous utilisez (tels que les logiciels de contrôle de versions ou de système de construction comme Git ou Make).

## Mauvaises pratiques

Il demeure cependant possible de fausser l'âge des fichiers avec l'exécution périodique de la commande récursive `touch`. Notre équipe technique dispose toutefois de moyens pour détecter ce genre de pratique et les utilisateurs qui s'y prêtent seront priés de retirer ces fichiers de l'espace `/scratch`.

## Copier un dossier avec des liens symboliques de manière sécuritaire

Dans la plupart des cas, `cp` ou `rsync` seront suffisants pour copier des données de `/scratch` vers votre projet. Mais si vous avez des liens symboliques (`symlink`) dans `/scratch`, les copier posera problème car ils continueront de pointer vers `/scratch`. Pour éviter cela, vous pouvez utiliser `tar` pour faire une archive de vos fichiers sur `/scratch`, et ensuite l'extraire dans votre projet. Vous pouvez le faire d'un seul coup avec

```bash
cd /scratch/.../vos_donnees
mkdir /project/.../vos_donnees
tar -cf - ./* | tar -C /project/.../vos_donnees -xf -