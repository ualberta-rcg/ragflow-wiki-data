---
title: "Parallel I/O introductory tutorial/fr"
slug: "parallel_i_o_introductory_tutorial"
lang: "fr"

source_wiki_title: "Parallel I/O introductory tutorial/fr"
source_hash: "9b99cca60ecd23d6eafbfb13f4ca647d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:51:45.089008+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Ce tutoriel abordera les défis liés à la gestion de grandes quantités de données en calcul haute performance (CHP), ainsi qu'une variété de stratégies d'E/S parallèle pour effectuer des entrées/sorties (E/S) à grande échelle avec des tâches parallèles. Nous décrirons notamment l'utilisation de MPI-IO et des bibliothèques d'E/S parallèles telles que NetCDF et HDF5.

## Problèmes et objectifs

De nombreux problèmes actuels nécessitent de grandes exécutions parallèles sur de grandes machines à mémoire distribuée (grappes). En général, trois activités d'E/S importantes sont impliquées dans ces calculs :

1.  L'application doit lire le jeu de données initial ou les conditions initiales à partir d'un ou plusieurs fichiers.
2.  L'état de l'application peut devoir être écrit dans un fichier pour redémarrer l'application en cas de défaillance. C'est ce qu'on appelle la [point de contrôle](points-de-controle.md).
3.  Les résultats doivent être stockés pour les exécutions ultérieures ou le post-traitement.

La figure ci-dessous illustre un simple aperçu du problème du goulot d'étranglement de l'E/S lorsque de nombreux CPU sont utilisés dans une tâche parallèle. La [loi d'Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law) stipule que l'accélération d'un programme parallèle est limitée par le temps nécessaire à la fraction séquentielle du programme. Ainsi, si la partie E/S de l'application fonctionne séquentiellement comme illustré, la performance du code ne sera pas aussi bonne que souhaité.

!!! warning "Défi de l'E/S efficace"
    Une E/S efficace sans surcharger le système de stockage – même un système de stockage haute performance – est un véritable défi.

*   **Temps d'exécution total = Temps de calcul + Temps de communication + Temps d'E/S**
*   Optimisez toutes les composantes de l'équation ci-dessus pour obtenir les meilleures performances!
*   Les opérations individuelles de chargement et de stockage sont plus coûteuses en temps que les opérations arithmétiques individuelles.
*   Dans certains cas, le temps d'exécution total est dominé par le temps d'E/S. C'est notre objectif principal dans cet article.

## Taux d'accès au disque au fil du temps

Dans les systèmes de calcul haute performance (CHP), les systèmes liés à l'E/S sont souvent lents par rapport aux autres composantes. La figure ci-dessous montre comment la vitesse relative de deux composantes importantes a évolué au cours de plusieurs décennies. De 1956 à 2014, la vitesse de stockage (la ligne violette) a augmenté d'un peu plus de 4 ordres de grandeur. En moins de la moitié de ce temps (de 1993 à 2014), la vitesse des superordinateurs les plus performants au monde (la ligne verte) a augmenté de plus de cinq ordres de grandeur. Cette divergence explique que nous pouvons produire des données à un rythme beaucoup plus rapide que nous ne pouvons les stocker. Il est donc nécessaire de porter une attention particulière à la manière de stocker les données de manière appropriée.

## Comment calculer la vitesse d'E/S

Avant de poursuivre, nous devons nous assurer de bien comprendre deux mesures de performance. Premièrement, il y a les "IOPs". Les IOPs signifient les opérations d'E/S par seconde. L'opération inclut la lecture/écriture, et ainsi de suite. Les IOPs sont l'inverse de la latence (pensez à la période (latence) et à la fréquence (IOPs)). Et il y a aussi la "bande passante d'E/S". La bande passante est définie comme la "quantité que vous lisez/écrivez". Je crois que vous êtes tous assez habitués à cette terminologie grâce à votre connexion Internet à la maison ou au bureau. Quoi qu'il en soit, voici un tableau d'informations pour plusieurs périphériques d'E/S. Comme vous pouvez le constater, les SSD haut de gamme sur PCI Express peuvent atteindre jusqu'à 1 Go d'IOPs. Cependant, ce type de périphérique est encore très coûteux et ne convient donc pas aux systèmes de supercalcul de plusieurs centaines de téraoctets.

Une chose que je voudrais souligner est que les systèmes de fichiers parallèles sont optimisés pour une E/S efficace par plusieurs utilisateurs sur plusieurs machines/nœuds. Ainsi, cela ne se traduit pas par des performances "supercomputing" en matière d'E/S.

*   **IOPs** = Opérations d'entrée/sortie par seconde (lecture/écriture/ouverture/fermeture/recherche) ; essentiellement l'inverse de la latence.
*   **Bande passante d'E/S** = quantité lue/écrite.

Les systèmes de fichiers parallèles (distribués) sont optimisés pour une E/S efficace par plusieurs utilisateurs sur plusieurs machines/nœuds, mais ne se traduisent pas par des performances "supercomputing".

*   temps d'accès au disque + communication sur le réseau (bande passante limitée, nombreux utilisateurs)

## Pile logicielle et matérielle d'E/S

*   Matériel d'E/S --> Système de fichiers parallèle --> Intergiciel d'E/S --> Bibliothèque d'E/S de haut niveau --> Application

Pour organiser l'E/S parallèle, il existe plusieurs couches d'abstraction à garder à l'esprit. Commençons par le bas. Il y a le matériel d'E/S, qui est un ensemble physique ou des disques durs attachés à la grappe. Par-dessus, nous exécutons un système de fichiers parallèle.

Sur la plupart des systèmes nationaux, nous utilisons Lustre, un système de fichiers open source. L'objectif du système de fichiers parallèle est de maintenir les partitions logiques et de fournir un accès efficace aux données. Ensuite, nous avons un intergiciel d'E/S au-dessus du système de fichiers parallèle. Il organise l'accès depuis de nombreux processus en optimisant l'E/S en deux phases, l'E/S sur disque et le flux de données sur le réseau, et il fournit également un criblage des données en convertissant de nombreuses petites requêtes d'E/S non contiguës en moins de requêtes plus grandes. Ensuite, il y aurait une bibliothèque d'E/S de haut niveau comme HDF5, NetCDF, etc. Ce qu'elle fait, c'est qu'elle mappe les abstractions d'application aux abstractions de stockage d'E/S en termes de structures de données du code. Ainsi, les données sont stockées directement sur le disque en appelant cette bibliothèque, et cette bibliothèque est implémentée pour fonctionner de manière très efficace. Il est préférable d'utiliser ce type de bibliothèques puisque nous supportons à la fois HDF5 et NetCDF. Vous pourriez également utiliser un intergiciel d'E/S qui est MPI-IO. Dans la présentation d'aujourd'hui, je me concentrerai davantage sur MPI-IO qui fait partie de MPI-2. Cependant, je discuterai également des avantages et des inconvénients des différentes approches. Et puis, comme vous pouvez le voir, il y a l'application qui est principalement votre programme, et votre programme décidera d'utiliser une bibliothèque d'E/S de haut niveau ou un intergiciel d'E/S.

## Système de fichiers parallèle

Sur les systèmes nationaux, nous disposons d'un système de fichiers parallèle conçu pour évoluer efficacement jusqu'à des dizaines de milliers de nœuds de calcul. Pour de meilleures performances, les fichiers peuvent être répartis (striped) sur plusieurs disques. Cela signifie que le fichier ne réside pas sur un seul disque dur, mais sur plusieurs disques, de sorte que pendant qu'un disque dur effectue une opération de lecture, un autre disque peut renvoyer les données au programme.

Afin d'éviter que deux processus différents ou plus n'accèdent au même fichier, les systèmes de fichiers parallèles utilisent des verrous (locks) pour gérer ce type d'accès concurrent aux fichiers. Ce qui se passe réellement, c'est que les fichiers sont découpés en unités de 'verrou' et dispersés sur plusieurs disques durs. Ensuite, les nœuds clients, qui sont des nœuds de calcul, obtiennent des verrous sur les unités auxquelles ils accèdent avant que l'E/S ne se produise.

*   Les fichiers peuvent être répartis sur plusieurs disques pour de meilleures performances.
*   Les **verrous** sont utilisés pour gérer l'accès concurrent aux fichiers dans la plupart des systèmes de fichiers parallèles.
    *   Les fichiers sont découpés en unités de 'verrou' (dispersées sur de nombreux disques).
    *   Les nœuds clients obtiennent des verrous sur les unités auxquelles ils accèdent avant que l'E/S ne se produise.
    *   Permet la mise en cache sur les clients.
    *   Les verrous sont récupérés des clients lorsque d'autres souhaitent y accéder.

La partie la plus importante que nous devrions savoir est que le système de fichiers parallèle est optimisé pour stocker de grands fichiers partagés qui peuvent être potentiellement accessibles depuis de nombreux nœuds de calcul. Il affiche donc de très faibles performances pour stocker de nombreux fichiers de petite taille. Comme vous l'avez peut-être appris lors de notre séminaire pour les nouveaux utilisateurs, nous recommandons fortement aux utilisateurs de ne pas générer des millions de petits fichiers.

De plus, la manière dont vous lisez et écrivez, le format de votre fichier, le nombre de fichiers dans un répertoire, et la fréquence de votre commande `ls` affectent tous les utilisateurs! Très souvent, nous recevons un billet signalant que l'utilisateur ne peut même pas exécuter `ls` dans son répertoire `/work`. Dans la plupart des cas, cette situation est causée par un utilisateur effectuant des activités d'E/S très élevées dans le répertoire, ce qui ralentit évidemment le système.
Le système de fichiers est partagé sur le réseau Ethernet d'une grappe : marteler le système de fichiers peut nuire aux communications des processus, principalement liées à la communication MPI. Cela affecte également les autres.

Veuillez noter que les systèmes de fichiers ne sont pas infinis : bande passante, IOPs, nombre de fichiers, espace, etc.

*   Optimisé pour les grands fichiers partagés.
*   Faible performance avec de nombreuses petites lectures/écritures (IOPs élevés) : Ne stockez pas des millions de petits fichiers.
*   Votre utilisation affecte tout le monde! (Différent du cas avec le CPU et la RAM qui ne sont pas partagés).
*   Facteurs critiques : la manière dont vous lisez/écrivez, le format de fichier, le nombre de fichiers dans un répertoire et la fréquence par seconde.
*   Le système de fichiers est partagé sur le réseau Ethernet d'une grappe : une E/S intense peut empêcher les processus de communiquer.
*   Les systèmes de fichiers sont LIMITÉS : bande passante, IOPs, nombre de fichiers, espace, etc.

## Bonnes pratiques pour l'E/S

Quelles seraient les bonnes pratiques pour l'E/S?

Premièrement, il est toujours recommandé de planifier vos besoins en données, par exemple, quelle quantité sera générée, combien vous devez sauvegarder et où les conserver.

Sur les systèmes nationaux, les différents systèmes de fichiers (home, project, scratch) ont des quotas différents. Les données `scratch` sont également soumises à une expiration. Pour plus de détails, consultez [ce document](https://alliancecan.ca/en/services/advanced-research-computing/national-services/storage). Tenez compte de ces limites avant de soumettre une tâche.

Et veuillez minimiser l'utilisation des commandes `ls` ou `du`, surtout dans un répertoire contenant de nombreux fichiers.

Vérifiez régulièrement votre utilisation du disque avec la commande `quota`. De plus, veuillez prendre en compte les signaux d'avertissement qui devraient inciter à une réflexion approfondie lorsque vous avez plus de 100 000 fichiers dans votre espace et une taille moyenne de fichier de données inférieure à 100 Mo (si vous écrivez beaucoup de données).

Veuillez faire un "ménage" régulièrement pour maintenir un nombre raisonnable de fichiers et un quota. Les commandes `gzip` et `tar` sont très populaires pour compresser plusieurs fichiers et les regrouper. Ainsi, vous pourriez réduire le nombre de fichiers en utilisant ces commandes.

*   Planifiez vos besoins en données : Quelle quantité générerez-vous? Combien avez-vous besoin de sauvegarder? Où les conserverez-vous?
*   Surveillez et contrôlez l'utilisation : Minimisez l'utilisation des commandes du système de fichiers comme `ls` et `du` dans les grands répertoires.
*   Vérifiez régulièrement votre utilisation du disque avec `quota`.
*   Avertissement!
    *   plus de 100 000 fichiers dans votre espace
    *   taille moyenne des fichiers de données inférieure à 100 Mo pour une sortie importante
*   Faites le "ménage" (gzip, tar, supprimer) régulièrement.

## Formats de données

### ASCII

Premièrement, il y a le format ASCII, ou comme certains l'appellent, le format 'texte'. C'est un format de fichier lisible par l'humain, mais il n'est pas efficace. Il est donc bon pour une petite entrée ou un fichier de paramètres pour exécuter un code. Le format ASCII utilise une plus grande quantité de stockage que les autres types de formats et, automatiquement, il coûte plus cher pour les opérations de lecture/écriture. Vous pouvez vérifier l'implémentation de votre code si vous trouvez `fprintf` dans le code C ou la commande `open` avec l'option `formatted` dans le code FORTRAN.

*   **ASCII** = **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange (Code standard américain pour l'échange d'informations)
    *   **Avantages** : lisible par l'humain, portable (indépendant de l'architecture).
    *   **Inconvénients** : stockage inefficace (13 octets par flottant simple précision, 22 octets par double précision, plus les délimiteurs), coûteux pour la lecture/écriture.

```c
fprintf() en C
```

```fortran
open(6,file='test',form='formatted');write(6,*) en F90
```

### Binaire

Le format binaire est beaucoup plus "économique" au sens computationnel que l'ASCII. L'ASCII est de 13 octets pour la simple précision et de 22 octets pour la double précision. Le tableau montre une expérience d'écriture de 128 millions de doubles à différents emplacements : `/scratch` et `/tmp` sur le système GPCS de SciNet. Comme vous pouvez le constater, il est évident que l'écriture binaire prend beaucoup moins de temps que le format ASCII.

| Format  | /scratch | /tmp (disque) |
|:--------|:---------|:--------------|
| ASCII   | 173 s    | 260 s         |
| Binaire | 6 s      | 20 s          |

*   **Avantages** : stockage efficace (4 octets par flottant simple précision, 8 octets par double précision, pas de délimiteurs), lecture/écriture efficace.
*   **Inconvénients** : il faut connaître le format pour lire, portabilité (endianness).

```c
fwrite() en C
```

```fortran
open(6,file='test',form='unformatted'); write(6) en F90
```

### Métadonnées (XML)

Bien que le format binaire fonctionne bien et soit efficace, il peut parfois être nécessaire de stocker des informations supplémentaires telles que le nombre de variables dans le tableau, les dimensions et la taille du tableau, etc. Les métadonnées sont donc utiles pour décrire le binaire. En cas de transmission des fichiers binaires à quelqu'un d'autre ou à d'autres programmes, il serait très utile d'inclure ces informations et d'utiliser le format de métadonnées. Incidemment, cela peut également être réalisé en utilisant des bibliothèques de haut niveau telles que HDF5 et NetCDF.

*   Encode les données sur les données : nombre et noms des variables, leurs dimensions et tailles, endianness, propriétaire, date, liens, commentaires, etc.

### Base de données

Le format de données de base de données est bon pour de nombreux petits enregistrements. L'utilisation de la base de données simplifie grandement l'organisation et l'analyse des données. CHARENTE supporte trois progiciels de bases de données différents. Ce n'est cependant pas très courant dans la simulation numérique.

*   Approche de stockage très puissante et flexible.
*   L'organisation et l'analyse des données peuvent être grandement simplifiées.
*   Performances améliorées en matière de recherche / tri en fonction de l'utilisation.
*   Logiciels open source : SQLite (sans serveur), PostgreSQL, MySQL.

### Bibliothèques de jeux de données scientifiques standard

Il existe des bibliothèques de jeux de données scientifiques standard. Comme mentionné dans la diapositive précédente, ces bibliothèques sont très efficaces non seulement pour stocker de grands tableaux de manière efficace, mais elles incluent également des descriptions de données pour lesquelles le format de métadonnées est bon. De plus, les bibliothèques offrent une portabilité des données entre les plateformes et les langages, ce qui signifie que les binaires générés sur une machine peuvent être lus sur d'autres machines sans problème. Les bibliothèques stockent automatiquement les données avec compression. Cela peut être extrêmement utile. Par exemple, si vous exécutez une simulation à grande échelle et que vous devez stocker un grand jeu de données, en particulier avec de nombreuses valeurs répétitives comme le zéro, alors les bibliothèques peuvent compresser ces valeurs répétitives efficacement afin que vous puissiez économiser considérablement le stockage des données.

*   **HDF5** = Hierarchical Data Format (Format de données hiérarchique)
*   **NetCDF** = Network Common Data Format (Format de données commun en réseau)
*   Standards ouverts et bibliothèques open source.
*   Offrent une portabilité des données entre les plateformes et les langages.
*   Stockent les données en binaire avec compression optionnelle.
*   Incluent une description des données.
*   Offrent en option l'E/S parallèle.

## E/S sérielle et parallèle

Dans les grands calculs parallèles, votre jeu de données est distribué sur de nombreux processeurs/nœuds. Comme le montre la figure de droite, par exemple, le domaine de calcul est décomposé en plusieurs blocs de travail, et chaque nœud prend une allocation. Par conséquent, chaque nœud calculera le domaine alloué et essaiera de stocker les données sur le disque. Malheureusement, dans ce cas, l'utilisation d'un système de fichiers parallèle n'est pas suffisante – vous devez organiser vous-même l'E/S parallèle. Cela sera discuté sous peu. Pour le format de fichier, il existe quelques options, comme un binaire brut sans information de métadonnées ou l'utilisation de bibliothèques de haut niveau (HDF5/NetCDF).

*   Dans les grands calculs parallèles, votre jeu de données est distribué sur de nombreux processeurs/nœuds.
*   Dans ce cas, l'utilisation d'un système de fichiers parallèle ne suffit pas – vous devez organiser vous-même l'E/S parallèle.
*   Les données peuvent être écrites en binaire brut, HDF5 et NetCDF.

## E/S sérielle (CPU unique)

Lorsque vous essayez d'écrire vos données de la mémoire de plusieurs nœuds de calcul vers un seul fichier sur le disque, il y aurait plusieurs approches. L'approche la plus simple consiste à désigner un "porte-parole" pour collecter toutes les données des autres membres de la communication. Une fois les données entièrement collectées par communication, elles sont écrites dans un fichier comme une E/S sérielle normale. C'est une solution très simple et facile à implémenter, mais il y a plusieurs problèmes. Premièrement, la bande passante pour l'écriture est limitée par le débit d'un seul client, et cela s'applique également à la limite de mémoire. Deuxièmement, le temps d'opération augmente linéairement avec la quantité de données ou la taille du problème, et de plus, il augmente avec le nombre de processus membres, car il faudra plus de temps pour collecter toutes les données sur un seul nœud ou CPU. Par conséquent, ce type d'approche ne peut pas évoluer.

!!! success "Avantages"
    *   Trivialement simple pour de petites E/S.
    *   Certaines bibliothèques d'E/S ne sont pas parallèles.

!!! failure "Inconvénients"
    *   Bande passante limitée par le débit qu'un seul client peut maintenir.
    *   Il peut ne pas y avoir suffisamment de mémoire sur un nœud pour contenir toutes les données.
    *   Ne pourra pas évoluer (goulot d'étranglement intégré).

## E/S sérielle (N processeurs)

Ce que vous pouvez faire à la place est d'organiser chaque processus participant pour effectuer une E/S sérielle. En d'autres termes, tous les processus effectuent des E/S vers des fichiers individuels. C'est quelque peu plus efficace que le modèle précédent, mais jusqu'à une certaine limite.

Premièrement, lorsque vous avez beaucoup de données, vous vous retrouverez avec de nombreux fichiers. Un fichier par processeur. Si vous exécutez un calcul de grande envergure avec de nombreuses itérations et de nombreuses variables, une seule exécution de simulation pourrait générer plus d'un millier de fichiers de sortie. Dans ce cas, comme nous l'avons discuté précédemment, le système de fichiers parallèle fonctionne mal. Encore une fois, nous avons passé en revue les bonnes pratiques d'E/S et des centaines de milliers de fichiers sont fortement interdits.

Deuxièmement, les données de sortie doivent souvent être post-traitées dans un seul fichier. C'est une étape supplémentaire et ce serait certainement assez inefficace. De plus, lorsque chaque processeur essaie d'accéder au disque en même temps, une E/S non coordonnée peut engorger le système de fichiers (verrous de fichiers!).

!!! success "Avantages"
    *   Pas de communication ou de coordination inter-processus nécessaire.
    *   Potentiellement une meilleure évolutivité que l'E/S séquentielle unique.

!!! failure "Inconvénients"
    *   À mesure que le nombre de processus augmente, beaucoup de (petits) fichiers, ne pourra pas évoluer.
    *   Les données doivent souvent être post-traitées en un seul fichier.
    *   Une E/S non coordonnée peut engorger le système de fichiers (verrous de fichiers!).

## E/S parallèle (N processus vers/depuis 1 fichier)

La meilleure approche est d'effectuer une E/S parallèle appropriée. Ainsi, chaque processus participant écrit les données simultanément dans un seul fichier en utilisant l'E/S parallèle. La seule chose dont vous devez être conscient est que vous voudrez peut-être effectuer cette E/S parallèle de manière coordonnée. Sinon, cela engorgera le système de fichiers.

!!! success "Avantages"
    *   Un seul fichier (bon pour la visualisation, la gestion des données, le stockage).
    *   Les données peuvent être stockées de manière canonique.
    *   Éviter le post-traitement pourra évoluer si cela est fait correctement.

!!! failure "Inconvénients"
    *   Une E/S non coordonnée engorgera le système de fichiers (verrous de fichiers!).
    *   Nécessite plus de conception et de réflexion.

## L'E/S parallèle doit être collective!

Par exemple, un intergiciel parallèle tel que MPI-IO propose différents types d'options d'écriture coordonnées ou non coordonnées. Une fois qu'une écriture coordonnée, comme l'E/S collective, est appelée, l'intergiciel parallèle saura quels processus et quels disques seront impliqués. Ensuite, l'intergiciel parallèle trouvera des opérations optimisées dans les couches logicielles inférieures pour une meilleure efficacité.

*   Les opérations d'**E/S indépendante** ne spécifient que ce qu'un seul processus fera.
*   L'**E/S collective** est un accès coordonné au stockage par un groupe de processus.
*   Les fonctions sont appelées par tous les processus participant à l'E/S.
*   Permet au système de fichiers d'en savoir plus sur l'accès dans son ensemble, plus d'optimisation dans les couches logicielles inférieures, de meilleures performances.

## Techniques d'E/S parallèle

C'est une partie de la norme MPI-2. Ainsi, MPI-IO est bon pour écrire un fichier binaire brut. Comme vous pouvez le lire sur cette diapositive, les bibliothèques de haut niveau telles que HDF5 et NetCDF sont construites au-dessus de MPI-IO. Par conséquent, vous devriez de toute façon avoir MPI-IO.

*   **MPI-IO** : partie E/S parallèle de la norme MPI-2 (1996).
*   **HDF5** (Hierarchical Data Format) : construit au-dessus de MPI-IO.
*   **Parallel NetCDF** (Network Common Data Format) : construit au-dessus de MPI-IO.

### MPI-IO

MPI-IO est disponible sur nos systèmes en tant que module par défaut, OpenMPI. MPI-IO exploite des analogies avec MPI ; l'écriture/lecture vers/depuis un fichier serait très similaire à la pratique d'envoi/réception de messages MPI si vous avez une certaine expérience avec MPI. Par exemple, l'accès aux fichiers est regroupé via un communicateur dans MPI. Le communicateur est un groupe pour le passage de messages dans MPI. Des types de données MPI définis par l'utilisateur sont également disponibles.

*   Fait partie de la norme MPI-2.
*   ROMIO est l'implémentation de MPI-IO dans OpenMPI (par défaut sur nos systèmes), MPICH2.
*   Le seul intergiciel d'E/S parallèle largement disponible pour le calcul scientifique.
*   MPI-IO exploite des analogies avec MPI :
    *   écriture, envoi de message
    *   lecture, réception de message
    *   accès aux fichiers regroupé via un communicateur : opérations collectives
    *   types de données MPI définis par l'utilisateur, par exemple pour une disposition de données non contiguë
    *   toutes les fonctionnalités via des appels de fonction

#### Opérations MPI-IO de base en C

```c
int MPI_File_open ( MPI_Comm comm, char* filename, int amode, MPI_Info info, MPI_File* fh)
int MPI_File_seek ( MPI_File fh, MPI_Offset offset, int to)
// met à jour le pointeur de fichier individuel
int MPI_File_set_view ( MPI_File fh, MPI_Offset offset, MPI_Datatype etype, MPI_Datatype filetype, char* datarep, MPI_Info info)
// modifie la vue d'un processus sur les données dans le fichier
// etype est le type de données élémentaire
int MPI_File_read ( MPI_File fh, void* buf, int count, MPI_Datatype datatype, MPI_Status* status)
int MPI_File_write (MPI_File fh, void* buf, int count, MPI_Datatype datatype, MPI_Status* status)
int MPI_File_close ( MPI_File* fh)
```

Voici un simple squelette pour les opérations MPI-IO en C. Comme un code MPI, il a `MPI_File_open` et `close` au début et à la fin. Il y a `File_write` et `File_read`. Et aussi, il y a `MPI_File_seek` qui est utilisé pour mettre à jour le pointeur de fichier individuel. Cela sera discuté en détail sous peu.

`MPI_File_set_view` sert à assigner des régions du fichier à des processus distincts.
Les vues de fichier sont spécifiées à l'aide d'un triplet - (déplacement, etype et filetype) - qui est passé à `MPI_File_set_view`.

*   `displacement` = nombre d'octets à sauter depuis le début du fichier.
*   `etype` = unité d'accès aux données (peut être n'importe quel type de données de base ou dérivé).
*   `filetype` = spécifie quelle portion du fichier est visible pour le processus.

#### Opérations MPI-IO de base en F90

```fortran
MPI_FILE_OPEN (integer comm, character[] filename, integer amode, integer info, integer fh, integer ierr)
MPI_FILE_SEEK (integer fh, integer(kind=MPI_OFFSET_KIND) offset, integer whence, integer ierr)
! met à jour le pointeur de fichier individuel
MPI_FILE_SET_VIEW (integer fh, integer(kind=MPI_OFFSET_KIND) offset, integer etype, integer filetype, character[] datarep, integer info, integer ierr)
! modifie la vue d'un processus sur les données dans le fichier
! etype est le type de données élémentaire
MPI_FILE_READ (integer fh, type buf, integer count, integer datatype, integer[MPI_STATUS_SIZE] status, integer ierr)
MPI_FILE_WRITE (integer fh, type buf, integer count, integer datatype, integer[MPI_STATUS_SIZE] status, integer ierr)
MPI_FILE_CLOSE (integer fh)
```

#### L'ouverture d'un fichier requiert...

L'ouverture d'un fichier requiert un communicateur, un nom de fichier et un descripteur de fichier pour toutes les références futures au fichier. Et aussi, elle requiert un mode d'accès au fichier `amode`. Il existe plusieurs modes différents, comme `MPI_MODE_WRONLY` qui signifie "écriture seule". Vous pouvez les combiner en utilisant l'opérateur "ou" binaire (`|`) en C ou l'addition (`+`) en FORTRAN.

```c
MPI_MODE_RDONLY                         // Lecture seule
MPI_MODE_RDWR                           // Lecture et écriture
MPI_MODE_WRONLY                         // Écriture seule
MPI_MODE_CREATE                         // Crée le fichier s'il n'existe pas
MPI_MODE_EXCL                           // Erreur si le fichier existe et est en cours de création
MPI_MODE_DELETE_ON_CLOSE                // Supprime le fichier à la fermeture
MPI_MODE_UNIQUE_OPEN                    // Le fichier ne doit pas être ouvert ailleurs
MPI_MODE_SEQUENTIAL                     // Le fichier doit être accédé séquentiellement
MPI_MODE_APPEND                         // Positionne tous les pointeurs de fichier à la fin
```

*   Combinez-les en utilisant l'opérateur "ou" binaire (`|`) en C ou l'addition (`+`) en FORTRAN.
*   L'argument `info` est généralement défini à `MPI_INFO_NULL`.

#### Exemple en C

```c
MPI_FILE fh ;
MPI_File_open (MPI_COMM_WORLD, "test.dat" ,MPI_MODE_RDONLY, MPI_INFO_NULL,&fh );
// ... lire des données ici ...
MPI_File_close(&fh ) ;
```

#### Exemple en F90

```fortran
integer :: fh,ierr
call MPI_FILE_OPEN(MPI_COMM_WORLD,"test.dat", MPI_MODE_RDONLY, MPI_INFO_NULL, fh, ierr)
! ... lire des données ici ...
call MPI_FILE_CLOSE(fh, ierr )
```

#### Lecture/Écriture de données contiguës

Ainsi, imaginons écrire un fichier à partir de quatre processus différents. Comme le montre la figure, chaque processus écrira ses données dans une portion désignée du même fichier. L'écriture se déroule de manière contiguë, du processus 0 au processus 3.

#### Exemple en C

En gros, nous initialisons MPI et plusieurs tableaux de variables. En utilisant `MPI_Comm_rank`, chaque processus aura son propre rang ou ID de processus. En utilisant `for (i=0)`, le tableau `a` est défini avec son rang pour une taille de tableau de 10. Par exemple, sur le processus 3, un tableau de 10 caractères '3' sera créé.

```c
MPI_File_open (MPI_COMM_WORLD, "data.out" , MPI_MODE_CREATE|MPI_MODE_WRONLY, MPI_INFO_NULL, &fh);
```

Nous avons défini le communicateur et le nom de fichier `data.out`. Pour le mode, nous avons combiné "écriture seule" et "créer le fichier s'il n'existe pas". Ensuite, nous définons l'offset (décalage) où chaque processus commence à écrire. Comme vous pouvez le voir, le processus 0 commence au début et le processus 1 est le suivant de manière contiguë.

```c
MPI_Offset displace = rank*n*sizeof(char);
```

Ainsi, l'offset sera calculé en multipliant `rang * taille du tableau * sizeof(char)`. Maintenant, nous sommes prêts à assigner les régions d'écriture à chaque processus en utilisant `MPI_File_set_view`. Le déplacement est défini, `etype` et `filetype` sont définis comme `MPI_CHAR`. "native" signifie que les données dans cette représentation sont stockées dans un fichier exactement comme elles le sont en mémoire. Ensuite, nous commandons l'écriture en utilisant `MPI_File_write`.

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {

int rank, i; char a[10];
MPI_Offset n = 10; MPI_File fh ; MPI_Status status ;

MPI_Init(&argc, &argv);

MPI_Comm_rank(MPI_COMM_WORLD, &rank);

for (i=0; i<10; i++)
a[i] = (char)( '0' + rank);  // e.g. on processor 3 creates a[0:9]='3333333333'

MPI_File_open (MPI_COMM_WORLD, "data.out", MPI_MODE_CREATE|MPI_MODE_WRONLY, MPI_INFO_NULL, &fh);
MPI_Offset displace = rank*n*sizeof(char); // start of the view for each processor

MPI_File_set_view (fh , displace , MPI_CHAR, MPI_CHAR, "native" ,MPI_INFO_NULL);
// note that etype and filetype are the same

MPI_File_write(fh, a, n, MPI_CHAR, &status);

MPI_File_close(&fh ) ;

MPI_Finalize ( ) ;

return 0;
}
```

#### Résumé : MPI-IO

Comme vous l'avez peut-être remarqué, son implémentation semble assez simple. Il doit y avoir beaucoup de matériel avancé utilisant MPI-IO, mais cela semble un peu au-delà de la portée de ce séminaire. Donc, en résumé, MPI-IO fait partie de la bibliothèque standard MPI-2, et il est très largement installé sur presque tous les systèmes HPC avec les versions MPI modernes. Nous avons installé OpenMPI, qui prend en charge MPI-IO sur toutes nos grappes. MPI-IO ne nécessite pas l'installation de bibliothèques supplémentaires, mais malheureusement, il écrit des données brutes dans le fichier. Il n'est donc pas portable entre les plateformes, difficile d'ajouter de nouvelles variables et n'inclut pas de description de données.

### NetCDF

**NetCDF** = **Net**work **C**ommon **D**ata **F**ormat (Format de données commun en réseau)

NetCDF est l'un des paquets les plus populaires pour le stockage de données. En gros, NetCDF couvre tout ce que MPI-IO ne peut pas prendre en charge. Il utilise MPI-IO en arrière-plan, mais au lieu de spécifier le décalage, il vous suffit d'appeler NetCDF et d'indiquer les tableaux que vous souhaitez stocker. Ensuite, NetCDF s'en chargera et essaiera de les stocker de manière contiguë. Dans NetCDF, les données sont stockées en binaire et, comme mentionné précédemment, il prend en charge l'auto-description, les métadonnées dans l'en-tête et la portabilité entre différentes architectures, ainsi que la compression optionnelle. L'un des meilleurs points par rapport à HDF5 est que NetCDF prend en charge une variété de logiciels de visualisation tels que Paraview. Nous avons NetCDF en série et en parallèle sur nos systèmes.

*   Format pour stocker de grands tableaux, utilise MPI-IO en arrière-plan.
*   Bibliothèques pour C/C++, Fortran 77/90/95/2003, Python, Java, R, Ruby, etc.
*   Données stockées en binaire.
*   Autodescriptif, métadonnées dans l'en-tête (peuvent être interrogées par des utilitaires).
*   Portable entre différentes architectures.
*   Compression optionnelle.
*   Utilise MPI-IO, optimisé pour les performances.
*   NetCDF parallèle.

#### Exemple en C

```c
#include <stdlib.h>
#include <stdio.h>
#include <netcdf.h>
#define FILE_NAME "simple_xy.nc"
#define NDIMS 2
#define NX 3
#define NY 4
int main() {
int ncid, x_dimid, y_dimid, varid;
int dimids[NDIMS];
int data_out[NX][NY];
int x, y, retval;
for (x = 0; x < NX; x++)
     for (y = 0; y < NY; y++)
          data_out[x][y] = x * NY + y;
retval = nc_create(FILE_NAME, NC_CLOBBER, &ncid);
retval = nc_def_dim(ncid, "x", NX, &x_dimid);
retval = nc_def_dim(ncid, "y", NY, &y_dimid);
dimids[0] = x_dimid;
dimids[1] = y_dimid;
retval = nc_def_var(ncid, "data", NC_INT, NDIMS, dimids, &varid);
retval = nc_enddef(ncid);
retval = nc_put_var_int(ncid, varid, &data_out[0][0]);
retval = nc_close(ncid);
return 0;
}
```

### HDF5

**HDF5** = **H**ierarchical **D**ata **F**ormat (Format de données hiérarchique)

HDF5 est également un outil très populaire pour le stockage de données. Il prend en charge la plupart des fonctionnalités de NetCDF, telles que le format de fichier auto-descriptif pour les grands jeux de données, et utilise également MPI-IO en arrière-plan. Fondamentalement, HDF5 est plus général que NetCDF, avec une description orientée objet des jeux de données, des groupes, des attributs, des types, des espaces de données et des listes de propriétés. Nous avons HDF5 en série et en parallèle sur nos systèmes.

*   Format de fichier auto-descriptif pour les grands jeux de données, utilise MPI-IO en arrière-plan.
*   Bibliothèques pour C/C++, Fortran 90, Java, Python, R.
*   Plus général que NetCDF, avec une description orientée objet des jeux de données, des groupes, des attributs, des types, des espaces de données et des listes de propriétés.
*   Le contenu du fichier peut être organisé en un système de fichiers de type Unix `/chemin/vers/la/ressource`.
    *   jeux de données contenant des images/tableaux/tableaux multidimensionnels homogènes.
    *   groupes contenant des structures pouvant contenir des jeux de données et d'autres groupes.
*   Les informations d'en-tête peuvent être interrogées par des utilitaires.
*   Compression optionnelle (bonne pour les tableaux avec de nombreux éléments similaires).
*   Nous fournissons HDF5 en série et en parallèle.

## Références

*   [https://www.nhr.kit.edu/userdocs/horeka/parallel_IO/](https://www.nhr.kit.edu/userdocs/horeka/parallel_IO/)
*   [https://hpc-forge.cineca.it/files/CoursesDev/public/2017/Parallel_IO_and_management_of_large_scientific_data/Roma/MPI-IO_2017.pdf](https://hpc-forge.cineca.it/files/CoursesDev/public/2017/Parallel_IO_and_management_of_large_scientific_data/Roma/MPI-IO_2017.pdf)
*   [https://janth.home.xs4all.nl/MPIcourse/PDF/08_MPI_IO.pdf](https://janth.home.xs4all.nl/MPIcourse/PDF/08_MPI_IO.pdf)
*   [https://events.prace-ri.eu/event/176/contributions/59/attachments/170/326/Advanced_MPI_II.pdf](https://events.prace-ri.eu/event/176/contributions/59/attachments/170/326/Advanced_MPI_II.pdf)
*   [https://www.cscs.ch/fileadmin/user_upload/contents_publications/tutorials/fast_parallel_IO/MPI-IO_NS.pdf](https://www.cscs.ch/fileadmin/user_upload/contents_publications/tutorials/fast_parallel_IO/MPI-IO_NS.pdf)