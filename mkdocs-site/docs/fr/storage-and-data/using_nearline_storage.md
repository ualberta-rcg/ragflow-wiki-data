---
title: "Using nearline storage/fr"
slug: "using_nearline_storage"
lang: "fr"

source_wiki_title: "Using nearline storage/fr"
source_hash: "a9d78aa6f89cce7697f16af1507edb3f"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:15:19.187315+00:00"

tags:
  []

keywords:
  - "programme d'archivage"
  - "disque"
  - "dar"
  - "données inactives"
  - "tar et dar"
  - "transfert de données"
  - "HPSS"
  - "fichiers archive"
  - "arrière-plan"
  - "lfs hsm_state"
  - "stockage sur ruban"
  - "lfs hsm_restore"
  - "/nearline"
  - "ruban"
  - "fichier"
  - "session SSH"
  - "multiplexeur de terminal"
  - "hierarchical storage manager"
  - "copie sur ruban"
  - "transfert de fichiers"
  - "tmux"

questions:
  - "Quelles sont les règles et restrictions concernant la taille des fichiers à stocker sur le système /nearline ?"
  - "Pourquoi est-il fortement recommandé de créer un fichier d'index lors du regroupement de fichiers dans une archive ?"
  - "Pourquoi le système /nearline n'est-il pas accessible depuis les nœuds de calcul et quelles sont les meilleures pratiques pour y exécuter de longs transferts de données ?"
  - "Pourquoi est-il recommandé de désactiver l'interactivité avec l'option `-Q` lors de l'utilisation de la commande `dar` sans terminal ?"
  - "Quels sont les avantages économiques et techniques du stockage sur ruban (/nearline) par rapport aux disques traditionnels et aux SSD ?"
  - "Comment évolue le cycle de vie d'un fichier sur /nearline et quelles commandes permettent de vérifier son état de stockage actuel ?"
  - "Quels problèmes peuvent survenir lors de l'exécution d'un programme d'archivage long via une session SSH ?"
  - "Comment peut-on laisser un programme s'exécuter en arrière-plan après la fermeture d'une session pour y revenir ultérieurement ?"
  - "Quels outils spécifiques sont recommandés pour exécuter des commandes comme tar ou dar sans risquer de les interrompre ?"
  - "À quoi sert la commande lfs hsm_state décrite dans le texte ?"
  - "Que signifie l'abréviation \"hsm\" selon le document ?"
  - "Comment peut-on différencier un fichier qui se trouve uniquement sur disque d'un fichier en cours de copie sur ruban grâce aux résultats de la commande ?"
  - "Comment peut-on vérifier l'état d'archivage d'un fichier sur ruban et forcer sa restauration sur disque ?"
  - "Quelles sont les différences de politiques de rétention et de suppression des fichiers entre les grappes Béluga et Nibi pour le service /nearline ?"
  - "Quelles sont les différentes méthodes disponibles pour transférer ou accéder à ses fichiers d'archivage HPSS sur la grappe Trillium ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le système de fichiers /nearline utilise de l'espace de stockage sur ruban et sert à conserver **les données inactives**, par exemple les ensembles de données que vous n'avez pas besoin d'utiliser pendant des mois.

## Restrictions et meilleures pratiques

### Taille des fichiers

S'il n'est pas efficace de récupérer des petits fichiers enregistrés sur ruban, récupérer de très gros fichiers pose d'autres problèmes. Nous vous demandons d'observer les règles suivantes :

*   les fichiers de moins de ~10Go devraient être rassemblés dans des fichiers archive (*tarballs*) avec [tar](a_tutorial_on__tar.md) ou un autre [outil semblable](archiving_and_compressing_files.md);
*   les fichiers de plus de 4To devraient être divisés en parts de 1To avec un outil comme [la commande `split`](a_tutorial_on__tar.md#fractionner-des-fichiers);
*   NE COPIEZ PAS DE PETITS FICHIERS SUR /NEARLINE, à l'exception des index (voir *Créer un index* ci-dessous).

### Choisir entre tar et dar

Utilisez [tar](a_tutorial_on__tar.md) ou [dar](dar.md) pour créer un fichier archive.

Gardez les fichiers sources dans leur système de fichiers d'origine. Ne copiez pas les fichiers sources sur /nearline avant de créer l'archive.

Créez l'archive directement sur /nearline. Ceci ne nécessite pas d'espace de stockage supplémentaire et est plus efficace que de créer l'archive sur /scratch ou /project et de la copier ensuite sur /nearline.

Si vous avez plusieurs centaines de Go de données, les options `-M (--multi-volume)` et `-L (--tape-length)` de `tar` peuvent être utilisées pour produire des fichiers archive de taille convenable. Par contre avec `dar`, vous pouvez utiliser l'option `-s (--slice)`.

#### Créer un index

Quand des fichiers sont regroupés, avec tar par exemple, il devient difficile de repérer un fichier particulier. Plutôt que de récupérer une grande collection enregistrée sur ruban pour seulement quelques fichiers, vous pourriez construire un index au moment où la collection est créée. Avec tar, vous pouvez ajouter l'option `verbose` pour obtenir plus de détails.

```bash
tar cvvf /nearline/def-sponsor/user/mycollection.tar /project/def-sponsor/user/something > /nearline/def-sponsor/user/mycollection.index
```

Si l'archive vient d'être créée, la commande suivante (avec tar dans cet exemple) crée l'index :

```bash
tar tvvf /nearline/def-sponsor/user/mycollection.tar > /nearline/def-sponsor/user/mycollection.index
```

Même s'il s'agit souvent de petits fichiers, les fichiers d'index peuvent être enregistrés sur /nearline.

### Pas d'accès à partir des nœuds de calcul

Puisque l'obtention de données sur /nearline peut prendre un certain temps (voir la section *Fonctionnement* ci-dessous), nous ne permettons pas que les tâches y lisent des données. /nearline n'est pas monté sur les nœuds de calcul.

### Utiliser un nœud de copie, si possible

Comme la création de fichiers archive exige beaucoup des ressources, il est préférable d'utiliser un nœud de copie (DTN) plutôt qu'un nœud de connexion si vous pouvez vous connecter à la grappe par un nœud DTN. En l'absence d'un nœud de copie, utilisez un nœud de connexion.

### Utiliser un multiplexeur de terminal

L'archivage de collections volumineuses de fichiers peut prendre plusieurs heures, voire même plusieurs jours. Votre session SSH peut être interrompue avant la fin du programme d'archivage, ou vous pouvez vouloir fermer votre session, laisser le programme s'exécuter en arrière-plan et y revenir plus tard. Pour éviter ce genre de problème, exécutez `tar` ou `dar` dans [un multiplexeur de terminal](../running-jobs/prolonging_terminal_sessions.md#multiplexeur-de-terminal) tel que `tmux`.

### Utiliser `dar` en mode non interactif

Dans un terminal, `dar` est en mode interactif et demande de confirmer certaines opérations. Sans terminal, `dar` est en mode non interactif et suppose une réponse négative à toutes les questions. Nous recommandons de désactiver explicitement l'interactivité avec `dar -Q`. Ceci est particulièrement utile lors de l'exécution de `dar` dans un multiplexeur de terminal sans surveillance. Voir [la page Dar](dar.md) pour plus d'informations.

## Avantages

Les avantages du stockage sur ruban par rapport aux disques et aux SSD (*solid-state drives*) sont :
*   le coût par unité de données stockée est moindre;
*   la capacité de stockage peut être facilement augmentée par l'achat de rubans additionnels;
*   la consommation énergétique par unité de données stockée est effectivement nulle.

Par conséquent, nous pouvons offrir beaucoup plus de capacité de stockage sur /nearline que sur /project. De plus, le fait de ne pas stocker de données inactives sur /project allège la charge et améliore la performance.

## Fonctionnement

1.  À sa création ou quand il est d'abord copié sur /nearline, le fichier existe uniquement sur disque et non sur ruban.
2.  Après un certain temps (environ une journée) et si le fichier remplit certains critères, il est copié sur ruban et se trouve alors sur disque et sur ruban.
3.  Un peu plus tard, la copie sur disque peut être supprimée et le fichier est sur ruban seulement.
4.  Quand un tel fichier est rappelé, il est copié du ruban au disque et revient au deuxième état.

Quand un fichier est entièrement copié sur ruban (ou *virtualisé*), il demeure visible dans la liste des fichiers du répertoire. Si une opération de lecture est faite sur le fichier virtuel, le ruban doit être trouvé dans la bibliothèque et la copie doit se faire sur le disque, ce qui prend du temps et bloque le processus qui tente de faire la lecture. Selon la taille du fichier et les demandes au système de stockage sur ruban, ceci peut nécessiter entre moins d'une minute et plus d'une heure.

### Transférer des données à partir de /nearline

Pendant le [transfert de vos données](../getting-started/transferring_data.md) avec [Globus](../getting-started/globus.md) ou tout autrement, les données exclusivement sur ruban seront automatiquement restaurées sur disque à leur simple lecture. Cependant, puisque l'accès aux données sur ruban est relativement lent, chaque restauration de fichier ralentira le transfert de quelques minutes à quelques heures. Par conséquent, il faut s'attendre à ce que les transferts à partir de /nearline prennent plus de temps.

Pour avoir un aperçu de l'état des fichiers dans vos espaces /nearline, **certaines grappes** peuvent présenter un sommaire avec la commande

```bash
diskusage_report --nearline --per_user --all_users
```

Les différentes valeurs de `Location` sont :
*   `On disk and tape` : les données sont disponibles sur disque.
*   `Modified, will be archived again` : la dernière version des données est sur disque.
*   `Archiving in progress` : les données sont en train d'être copiées ou déplacées sur ruban.
*   `On tape` : les données sont seulement sur ruban.

Ensuite, la commande `lfs hsm_state` permet de savoir si un fichier est sur ruban ou encore sur disque (l'abréviation hsm signifie *hierarchical storage manager*).

```bash
#  <FILE> se trouve seulement sur disque.
$ lfs hsm_state <FILE>
<FILE>:  (0x00000000)

# <FILE> est présentement copié sur ruban.
$ lfs hsm_state <FILE>
<FILE>: [...]: exists, [...]

# <FILE> se trouve à la fois sur disque et sur ruban.
$ lfs hsm_state <FILE>
<FILE>: [...]: exists archived, [...]

# <FILE> se trouve sur ruban et n'est plus sur disque; ouvrir ce fichier prendra plus de temps.
$ lfs hsm_state <FILE>
<FILE>: [...]: released exists archived, [...]
```

Vous pouvez forcer le rappel d'un fichier sur ruban sans le lire avec la commande `lfs hsm_restore <FILE>`.

### Spécificités de chaque grappe

=== "Béluga"
    L'accès au répertoire /nearline se fait par les nœuds de connexion et les DTN (*Data Transfer Nodes*).

    Enregistrez vos fichiers dans votre répertoire `~/nearline/PROJECT`. Ils seront copiés sur ruban après un certain temps (24 heures en date de février 2019). Si le fichier n’est pas modifié pendant un certain temps (24 heures en date de février 2019), la copie sur disque sera supprimée, virtualisant ainsi le fichier sur ruban.

    Lorsque vous supprimez un fichier de `~/nearline` volontairement ou par accident, la copie sur ruban est conservée pour 60 jours. Pour restaurer ces fichiers, vous devez contacter le [soutien technique](../support/technical_support.md) en mentionnant le chemin complet et la version (avec la date), de la même manière que vous procéderiez pour restaurer une [copie de sauvegarde](storage_and_file_management.md#quotas-et-politiques). Il est donc important que vous conserviez une copie de la structure complète de votre espace /nearline. La commande `ls -R > ~/nearline_contents.txt` lancée du répertoire `~/nearline/PROJECT` vous permettra de voir où sont situés les fichiers dans votre espace /nearline.

=== "Nibi"
    Le service /nearline est semblable à celui de Béluga, sauf que :
    1. la création de la première copie sur bande des données pourrait prendre plus que 24 heures,
    2. la copie sur disque ne sera pas effacée (pour ne laisser que la copie sur bande) avant 60 jours.

=== "Narval"
    Le service /nearline est semblable à celui de Béluga.

=== "Trillium"
    HPSS est le service /nearline pour Trillium.
    Les méthodes d'accès sont :

    1. Dans une des partitions archive, soumettre une tâche à l’ordonnanceur Slurm avec les commandes HPSS `htar` ou `hsi`; pour des exemples, voyez la [documentation HPSS](https://docs.scinet.utoronto.ca/index.php/HPSS). Travailler avec des scripts offre l’avantage de pouvoir automatiser les transferts; il s’agit de la meilleure méthode si vous utilisez HPSS régulièrement. Vos fichiers HPSS se trouvent dans le répertoire `$ARCHIVE`, qui est semblable à `$PROJECT`, mais où */project* est remplacé par */archive*.

    2. Utiliser le nœud VFS (*virtual file system*) par la commande `salloc --time=1:00:00 -pvfsshort` quand vous avez peu de fichiers HPSS. Vos fichiers HPSS se trouvent dans le répertoire `$ARCHIVE`, qui est semblable à `$PROJECT`, mais où */project* est remplacé par */archive*.

    3. Utilisez [Globus](../getting-started/globus.md) pour transférer vos fichiers HPSS avec le point de chute (*endpoint*) **alliancecan#hpss**. Cette méthode est utile pour un usage occasionnel ou pour les transferts entre HPSS et les autres sites.