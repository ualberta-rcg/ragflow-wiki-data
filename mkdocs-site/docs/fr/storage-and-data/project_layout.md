---
title: "Project layout/fr"
slug: "project_layout"
lang: "fr"

source_wiki_title: "Project layout/fr"
source_hash: "9dbae366e70ab0b5dc7b8c08c586d6e5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:28:00.166650+00:00"

tags:
  []

keywords:
  - "Alliance"
  - "données partagées"
  - "répertoires"
  - "espace scratch"
  - "permissions"
  - "Globus"
  - "espace /project"
  - "espace project"
  - "mauvais groupe"
  - "Disk quota exceeded"
  - "propriété de groupe"
  - "partage de données"
  - "quota de disque"
  - "point de chute commun"
  - "fichiers"
  - "espace de stockage"
  - "espace home"
  - "setgid"
  - "collaboratrice"
  - "fichiers temporaires"
  - "appartenance au groupe"
  - "groupe personnel"

questions:
  - "Comment configurer un répertoire dans l'espace /project pour accorder des droits de lecture et d'écriture à tous les membres d'un groupe ?"
  - "Quels sont les quotas de stockage par défaut pour un espace /project et comment peut-on vérifier l'espace utilisé et disponible ?"
  - "Comment utiliser le bit setgid et la commande newgrp pour gérer l'appartenance de groupe des fichiers et éviter les erreurs de dépassement de quota ?"
  - "Comment la structure des répertoires permet-elle aux membres d'un même groupe de recherche de partager des données et de collaborer dans l'espace `/project` ?"
  - "Quelles sont les méthodes recommandées pour partager des fichiers avec une personne externe au groupe, qu'elle possède ou non un compte sur la grappe ?"
  - "Quelles règles de permissions spécifiques doivent être appliquées sur l'arborescence des fichiers pour garantir qu'un utilisateur externe puisse accéder aux données partagées ?"
  - "Quelle est la cause possible du message d'erreur \"Disk quota exceeded\" selon le texte ?"
  - "Quelles sont les caractéristiques du groupe personnel de l'utilisateur, notamment sa limite de quota ?"
  - "Que doit-on utiliser pour trouver et résoudre ce problème de propriété de groupe pour les fichiers concernés ?"
  - "Comment le partage de données est-il rendu possible pour les chercheurs sans compte avec l'Alliance ?"
  - "Quel outil est utilisé pour créer un point de chute commun destiné au partage de fichiers ?"
  - "Comment Sue peut-elle accorder à Heather les mêmes privilèges d'accès qu'à Bob ?"
  - "À quel type de fichiers l'espace scratch est-il spécifiquement destiné ?"
  - "Quelle est l'utilisation principale recommandée pour l'espace home ?"
  - "Quelles sont les caractéristiques qui rendent l'espace project idéal pour les données partagées ?"
  - "À quel type de fichiers l'espace scratch est-il spécifiquement destiné ?"
  - "Quelle est l'utilisation principale recommandée pour l'espace home ?"
  - "Quelles sont les caractéristiques qui rendent l'espace project idéal pour les données partagées ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de : [Stockage et gestion de fichiers](storage-et-gestion-de-fichiers.md)*
Voir aussi [Message *Disk quota exceeded*](frequently-asked-questions.md#message-disk-quota-exceeded)

Sur nos grappes de calcul, les espaces `/project` sont organisés selon des *groupes*.
L'accès à `/project` se fait habituellement par des liens symboliques à partir de votre répertoire `/home`.
Les liens symboliques se présentent sous le format `$HOME/projects/group_name`, à l'exception des grappes [Rorqual](rorqual.md) et [Trillium](trillium.md) où le chemin est semblable à `$HOME/links/projects/group_name`.

Dans l’espace réservé à un groupe, la chercheuse ou le chercheur principal est propriétaire du répertoire et les membres du groupe ont des permissions de lecture et écriture pour ce répertoire. Cependant, pour tout nouveau fichier enregistré dans le répertoire, les membres du groupe ont par défaut un droit de lecture seulement. Pour que les membres puissent avoir un droit en écriture, la meilleure approche est de créer un répertoire particulier, ainsi :

```bash
mkdir $HOME/projects/def-profname/group_writable
```

suivi de :

```bash
setfacl -d -m g::rwx $HOME/projects/def-profname/group_writable
```

Sur le partage de données, la propriété de fichiers et les listes de contrôle d’accès (ACLs), voyez [Partage de données](https://docs.computecanada.ca/wiki/Sharing_data/fr).

Par défaut, un espace `/project` a un quota de 1 To et 500 000 fichiers; l’espace peut être augmenté jusqu’à 40 To sur demande auprès du [soutien technique](technical-support.md). Si votre groupe dispose de quotas plus élevés par suite du [concours pour l’allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources), vous connaissez le quota qui vous est alloué pour l’année.

!!! note "Important"
    Veuillez noter que l'espace de stockage alloué dépend de la grappe et ne peut, en principe, être utilisé sur une autre grappe.

Pour connaître les espaces utilisés et disponibles, utilisez :

```bash
diskusage_report
```

Pour faire en sorte que les fichiers copiés ou déplacés dans `/project` appartiennent au même groupe et soient comptabilisés dans le quota prévu, il peut être utile d'attribuer le *bit* `setgid` au répertoire approprié. De cette manière, tous les nouveaux fichiers et sous-répertoires ajoutés sous le répertoire en question héritent du même groupe que leur parent; de plus, les sous-répertoires héritent aussi de `setgid`. Cependant, l'appartenance au groupe n'est pas modifiée pour les fichiers et sous-répertoires déjà existants, ce qui se fait par la commande `chgrp`; aussi, tout fichier déplacé dans le répertoire conserve son appartenance de groupe. Pour attribuer `setgid` à un répertoire, utilisez la commande :

```bash
chmod g+s <nom-du-répertoire>
```

Pour attribuer `setgid` aux sous-répertoires existants, utilisez la commande :

```bash
find <nom-du-répertoire> -type d -print0 | xargs -0 chmod g+s
```

Pour plus d'information sur `setgid`, consultez [cette page](https://fr.wikipedia.org/wiki/Setuid#setgid_pour_les_repertoires).

La commande `newgrp` modifie votre groupe par défaut pendant une session interactive; par exemple :

```bash
newgrp rrg-profname-ab
```

Copiez ensuite les données vers le répertoire `/project` approprié. Cependant, le groupe par défaut est modifié uniquement pour cette session; vous devrez utiliser `newgrp` à nouveau pour changer le groupe par défaut à votre prochaine connexion.

Si vous recevez des messages d'erreur *Disk quota exceeded* (voir [Message *Disk quota exceeded*](frequently-asked-questions.md#message-disk-quota-exceeded)), ceci peut très bien être dû au fait que des fichiers sont associés au mauvais groupe, notamment votre groupe personnel, c'est-à-dire le groupe qui porte le même nom que votre nom d'utilisateur et qui a un quota de seulement 2 Mo. Pour trouver et résoudre un problème de propriété de groupe pour ces fichiers, vous pouvez utiliser la commande :

```bash
find <nom-du-répertoire> -group $USER -print0 | xargs -0 chgrp -h <groupe>
```

où `<groupe>` est quelque chose comme `def-profname`, donc un groupe qui possède un quota raisonnable d'un téraoctet ou plus.

## Exemple

Dans notre exemple, Sue est chercheuse principale et Bob est membre de son groupe. Au départ, les répertoires de Sue et Bob semblent structurés de manière identique.

*   `/home/sue/scratch` (lien symbolique)
*   `/home/sue/projects` (répertoire)
*   `/home/bob/scratch` (lien symbolique)
*   `/home/bob/projects` (répertoire)

Cependant, le lien symbolique *scratch* pointe sur des répertoires différents : `/scratch/sue` pour Sue et `/scratch/bob` pour Bob.

En supposant que Bob n'ait qu'un seul rôle défini dans CCDB, le répertoire `project` de Bob aurait le même contenu que les répertoires `project` de Sue, et `projects` pour Bob serait identique à `projects` pour Sue. Aussi, si Sue et Bob n'ont aucun autre rôle et ne sont associés à aucun autre projet, chacun de leur répertoire `projects` ne comprendrait qu'un sous-répertoire, soit `def-sue`.

Chacun de `/home/sue/project`, `/home/bob/project`, `/home/sue/projects/def-sue` et `/home/bob/projects/def-sue` pointerait au même répertoire, soit `/project/<numéro quelconque>`. Ce répertoire est le meilleur endroit où partager les données de Sue et Bob; ils peuvent y créer des répertoires et ont un accès en lecture et en écriture. Ainsi, Sue peut créer un répertoire `foo` :

```bash
cd ~/projects/def-sue
mkdir foo
```

et Bob peut copier des fichiers dans `~/projects/def-sue/foo`, pour que les deux puissent y avoir accès.

En supposant maintenant que Sue ait obtenu des ressources avec de l'espace de stockage suite au concours d'allocation de ressources (comme c'est souvent le cas), il y aurait une autre entrée dans leurs répertoires `projects` respectifs, semblable à :

`~/projects/rrg-sue-ab`

Ce répertoire servirait à stocker et partager les données pour un projet dans le cadre du concours.

Pour partager un fichier avec une utilisatrice qui n’est pas parrainée par la chercheuse principale, par exemple Heather, le plus simple est de configurer les permissions pour que celle-ci puisse lire le répertoire ou le fichier, habituellement par une liste de contrôle des accès (ACL); pour les détails, voyez la page [Partage de données](sharing-data.md). Notez que les permissions pour les systèmes de fichiers peuvent être modifiées pour tous les répertoires ou fichiers, et non seulement pour ceux de votre espace `/project`. Vous pouvez partager un répertoire de votre espace `/scratch` ou encore un seul sous-répertoire particulier de votre espace `/project`.

!!! tip "Bonne pratique"
    Il est recommandé de limiter le partage des fichiers aux espaces `/project` et `/scratch`.

N’oubliez pas que Heather devra probablement avoir accès à plus d’un niveau de la structure du système de fichiers; il faut lui accorder les permissions de lecture et d’écriture pour chacun des répertoires entre `~/projects/def-sue` et le répertoire où sont situés les fichiers à partager. Nous avons supposé que Heather détient un compte sur la grappe en question, mais il est aussi possible de partager des données avec des chercheuses et chercheurs qui n’ont pas de compte avec l'Alliance, en créant un [point de chute commun](globus.md#partage-de-fichiers-avec-globus) dans Globus.

Bien sûr, si Heather devient une collaboratrice régulière de Sue, cette dernière pourrait la parrainer et lui accorder les mêmes accès que ceux accordés à Bob.

En résumé :

*   l'espace `scratch` est utilisé pour les fichiers privés et temporaires
*   l'espace `home` est habituellement utilisé pour un petit nombre de fichiers relativement privés (par exemple des scripts de tâches)
*   l'espace `project` du groupe est habituellement utilisé pour les données partagées puisque cet espace est persistant, sauvegardé et plutôt de grande taille (jusqu'à 40 To et plus si alloué dans le cadre du concours d'allocation de ressources)