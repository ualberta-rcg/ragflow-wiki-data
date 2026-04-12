---
title: "Parallel I/O introductory tutorial/fr"
slug: "parallel_i_o_introductory_tutorial"
lang: "fr"

source_wiki_title: "Parallel I/O introductory tutorial/fr"
source_hash: "9b99cca60ecd23d6eafbfb13f4ca647d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:19:55.646480+00:00"

tags:
  []

keywords:
  - "File system performance"
  - "Database"
  - "large shared files"
  - "MPI_File_set_view"
  - "parallel filesystems"
  - "contiguous data"
  - "computing nodes"
  - "variable arrays"
  - "High-end I/O library"
  - "HPC"
  - "Data storage formats"
  - "data storage"
  - "MPI-IO"
  - "supercomputing systems"
  - "parallel I/O"
  - "single file"
  - "NetCDF"
  - "metadata"
  - "Parallel filesystem"
  - "MPI_File_write"
  - "MPI_Comm_rank"
  - "caching on clients"
  - "Data formats"
  - "Object-oriented description"
  - "Parallel I/O"
  - "I/O middleware"
  - "Large datasets"
  - "efficient I/O"
  - "MPI_File_seek"
  - "Serial I/O"
  - "SSDs"
  - "parallel filesystem"
  - "parallel calculations"
  - "Shared cluster"
  - "storing data"
  - "coordinated fashion"
  - "Scientific dataset libraries"
  - "Concurrent file access"
  - "ASCII"
  - "Offset"
  - "small size files"
  - "Unix-like filesystem"
  - "PCI Express"
  - "open standards"
  - "HDF5"
  - "MPI_File_read"
  - "Disk usage"
  - "Metadata"
  - "data distribution"
  - "filesystem"
  - "participating process"
  - "Binary format"
  - "MPI-IO operations"
  - "contiguous fashion"
  - "process id"
  - "Self-describing"
  - "Self-describing file format"
  - "human readable"
  - "inefficient storage"
  - "file access mode"
  - "read/write operation"
  - "I/O best practices"
  - "I/O bottleneck"
  - "MPI_File_open"
  - "File striping"
  - "Parallel filesystems"
  - "datasets"
  - "MPI"
  - "formatted"
  - "Collective I/O"

questions:
  - "What are the three primary I/O activities required during large parallel calculations on distributed-memory machines?"
  - "Why does I/O frequently become a performance bottleneck in High-Performance Computing systems compared to computation speed?"
  - "How do IOPs and I/O Bandwidth differ when measuring the performance of storage devices?"
  - "What are the different layers of abstraction in the I/O software and hardware stack, and what is the specific function of each layer?"
  - "How do parallel filesystems use file striping and locking mechanisms to manage concurrent access across multiple computing nodes?"
  - "Why do parallel filesystems perform poorly when storing many small files, and what type of file storage are they actually optimized for?"
  - "Why are top-of-the-line PCI Express SSDs currently considered unsuitable for large-scale supercomputing systems despite their high performance?"
  - "What is the primary optimization goal of parallel filesystems in a computing environment?"
  - "Why does the use of parallel filesystems not necessarily result in raw \"supercomputing\" I/O performance?"
  - "How does the filesystem manage client caching and lock reclamation when multiple nodes require access?"
  - "What specific types of files and access patterns is the parallel filesystem optimized to handle?"
  - "Why are users strongly advised against generating millions of small-sized files on this system?"
  - "How do individual user I/O activities, such as reading/writing many small files or frequently using the 'ls' command, affect the overall performance of a shared cluster file system?"
  - "What are the recommended best practices for managing data generation, storage quotas, and file housekeeping to prevent system slowdowns?"
  - "What are the advantages and disadvantages of using the ASCII format for data storage and read/write operations compared to other formats?"
  - "What does the acronym ASCII stand for, and what are its main advantages?"
  - "Why is ASCII considered to have inefficient storage and expensive read/write operations?"
  - "How can you identify the use of ASCII formatted operations within C or FORTRAN code?"
  - "What are the primary advantages and disadvantages of using binary format compared to ASCII for data storage?"
  - "Why is it important to use metadata (XML) or database formats when storing, organizing, and sharing data?"
  - "What specific benefits do standard scientific dataset libraries like HDF5 and NetCDF offer for large-scale data management?"
  - "What are the main drawbacks of using a single \"spokesperson\" node to handle all I/O operations in a parallel calculation?"
  - "Why does the strategy of having each processor write to its own individual file fail to scale effectively in large simulations?"
  - "How does coordinated parallel I/O to a single file resolve the performance and filesystem issues encountered in serial I/O approaches?"
  - "What are HDF5 and NetCDF, and how do they contribute to dramatically saving data storage?"
  - "What key features do these open-standard formats provide regarding data portability, compression, and description?"
  - "How do these data formats support and implement serial and parallel I/O operations?"
  - "What is the recommended approach for handling multiple processes writing to a single file?"
  - "How do participating processes interact with the data and the file during parallel I/O?"
  - "What is the primary risk to the filesystem if the parallel I/O is not properly coordinated?"
  - "What are the primary advantages of using collective I/O operations over independent I/O in parallel computing?"
  - "How do high-level data format libraries like HDF5 and Parallel NetCDF relate to the underlying MPI-IO standard?"
  - "In what ways does MPI-IO leverage existing MPI concepts, such as communicators and message passing analogies, to manage file access?"
  - "What functions are required at the beginning and end of an MPI-IO code skeleton?"
  - "Which MPI functions are used to perform the actual reading and writing of files?"
  - "What is the specific purpose of the MPI_File_seek function mentioned in the text?"
  - "What are the three components of the triplet used in MPI_File_set_view, and what does each component represent?"
  - "What arguments are required to open a file in MPI, and how can multiple file access modes be combined in C and FORTRAN?"
  - "How does MPI-IO manage the process of writing contiguous data to a single shared file from multiple different processes?"
  - "How does the file writing proceed among the processes described in the text?"
  - "Which MPI function is utilized in the C example to determine the unique rank or ID of each process?"
  - "How are the variable arrays initialized and populated based on the process rank in the given example?"
  - "How does MPI-IO manage concurrent file writing by multiple processes using offsets and file views?"
  - "What are the main limitations of using raw MPI-IO for data storage across different computing platforms?"
  - "How does NetCDF overcome the shortcomings of MPI-IO while still utilizing it under the hood?"
  - "What are the key characteristics and advantages of using the NetCDF format for storing large data arrays?"
  - "How do individual processes calculate their offsets and assign specific writing regions when using MPI-IO in the provided C example?"
  - "How does the Hierarchical Data Format (HDF5) compare to NetCDF in terms of its general structure and data description capabilities?"
  - "How does NetCDF utilize and improve upon the capabilities of MPI-IO?"
  - "What is the process and format used by NetCDF to store data arrays?"
  - "What specific features make NetCDF data self-describing and portable across different architectures?"
  - "What are the key object-oriented components used by HDF5 to describe large datasets?"
  - "Which programming languages have library support for HDF5, and what underlying technology does it utilize?"
  - "How does HDF5 compare to NetCDF, and what specific versions are available on the described systems?"
  - "How is the file content structured and organized within the described system?"
  - "What specific types of data can be stored in the datasets?"
  - "What additional features and execution modes does the HDF5 system offer according to the text?"
  - "How is the file content structured and organized within the described system?"
  - "What specific types of data can be stored in the datasets?"
  - "What additional features and execution modes does the HDF5 system offer according to the text?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ce tutoriel aborde les défis liés à la gestion de grandes quantités de données en calcul haute performance (CHP) et présente diverses stratégies d'E/S parallèles pour effectuer des opérations d'entrée/sortie (E/S) à grande échelle avec des tâches parallèles. Nous décrirons notamment l'utilisation de MPI-IO et de bibliothèques d'E/S parallèles telles que NetCDF et HDF5.

## Problèmes et objectifs

Bon nombre des problèmes actuels nécessitent de grandes exécutions parallèles sur des machines à mémoire distribuée (grappes) de grande taille. De manière générale, trois activités d'E/S importantes sont impliquées dans ces calculs :

1.  L'application doit lire l'ensemble de données initial ou les conditions de départ à partir d'un ou plusieurs fichiers.
2.  L'état de l'application peut devoir être écrit dans un fichier pour redémarrer l'application en cas de défaillance. C'est ce qu'on appelle la [création de points de contrôle](../running-jobs/points_de_contrôle.md).
3.  Les résultats doivent être stockés pour des exécutions ultérieures ou pour le post-traitement.

La figure ci-dessous illustre un aperçu simple du problème du goulot d'étranglement des E/S lors de l'utilisation de nombreux processeurs dans une tâche parallèle. [La loi d'Amdahl](https://fr.wikipedia.org/wiki/Loi_d%27Amdahl) stipule que l'accélération d'un programme parallèle est limitée par le temps nécessaire à la fraction séquentielle du programme. Ainsi, si la partie E/S de l'application fonctionne de manière séquentielle comme illustré, la performance du code ne sera pas aussi bonne qu'espérée.

!!! note
    *Réaliser des E/S efficaces sans surcharger le système de stockage – même un système de stockage haute performance – est un défi.*

*   **Temps d'exécution total = Temps de calcul + Temps de communication + Temps d'E/S**
*   Optimisez toutes les composantes de l'équation ci-dessus pour obtenir la meilleure performance!
*   Les opérations individuelles de chargement et de stockage prennent plus de temps que les opérations arithmétiques individuelles.
*   Dans certains cas, le temps d'exécution total est dominé par le temps d'E/S. C'est notre objectif dans cet article.

### Débits d'accès au disque au fil du temps

Dans les systèmes de calcul haute performance (CHP), les systèmes d'E/S sont souvent lents par rapport aux autres composantes. La figure ci-dessous illustre l'évolution de la vitesse relative de deux composantes importantes sur plusieurs décennies. De 1956 à 2014, la vitesse de stockage (la ligne violette) a augmenté d'un peu plus de 4 ordres de grandeur. En moins de la moitié de cette période (de 1993 à 2014), la vitesse des superordinateurs les plus puissants au monde (la ligne verte) a augmenté de plus de cinq ordres de grandeur. Cette divergence explique que nous pouvons produire des données à un rythme beaucoup plus rapide que nous ne pouvons les stocker. Par conséquent, il est essentiel de porter une attention particulière à la manière appropriée de stocker les données.

### Comment calculer la vitesse d'E/S

Avant de poursuivre, assurons-nous de bien comprendre les deux mesures de performance suivantes. Premièrement, il y a les « IOPs ». Les IOPs signifient « Input/Output Operations Per Second » (opérations d'entrée/sortie par seconde). Ces opérations incluent la lecture, l'écriture, etc., et les IOPs sont l'inverse de la latence (pensez à la période (latence) et à la fréquence (IOPs)). Ensuite, il y a la « Bande passante d'E/S ». La bande passante est définie comme la « quantité de données que vous lisez/écrivez ». Je crois que vous êtes tous habitués à cette terminologie grâce à votre connexion Internet à la maison ou au bureau. Quoi qu'il en soit, voici un tableau d'information pour plusieurs périphériques d'E/S. Comme vous pouvez le constater, les SSD haut de gamme sur PCI Express peuvent atteindre jusqu'à 1 Giga-IOPs. Cependant, ces appareils sont encore très coûteux, ce qui ne convient pas aux systèmes de supercalcul de plusieurs centaines de téraoctets.

Une chose que j'aimerais souligner est que les systèmes de fichiers parallèles sont optimisés pour des E/S efficaces par plusieurs utilisateurs sur plusieurs machines/nœuds. Par conséquent, ils ne se traduisent pas par une performance « supercalcul » en matière d'E/S.

*   **IOPs** = Opérations d'entrée/sortie par seconde (lecture/écriture/ouverture/fermeture/recherche) ; essentiellement l'inverse de la latence
*   **Bande passante d'E/S** = quantité de données lues / écrites
*   Les systèmes de fichiers parallèles (distribués) sont optimisés pour des E/S efficaces par plusieurs utilisateurs sur plusieurs machines/nœuds, mais ne procurent pas une performance de « supercalcul ».
    *   temps d'accès au disque + communication sur le réseau (bande passante limitée, nombreux utilisateurs)

### Pile logicielle et matérielle d'E/S

*   Matériel d'E/S --> Système de fichiers parallèle --> Intergiciel d'E/S --> Bibliothèque d'E/S haut de gamme --> Application

Lorsqu'il s'agit d'organiser les E/S parallèles, plusieurs couches d'abstraction doivent être prises en compte. Tout d'abord, commençons par le bas. Il y a le matériel d'E/S, qui est un ensemble physique de disques durs ou une baie de disques connectés à la grappe. Par-dessus, nous utilisons un système de fichiers parallèle.

Sur la plupart des systèmes nationaux, nous utilisons Lustre, un système de fichiers open source. L'objectif du système de fichiers parallèle est de maintenir les partitions logiques et de fournir un accès efficace aux données. Ensuite, nous avons un intergiciel d'E/S au-dessus du système de fichiers parallèle. Il organise l'accès depuis de nombreux processus en optimisant les E/S en deux phases, les E/S sur disque et le flux de données sur le réseau, et il fournit également un « tamisage » des données en convertissant de nombreuses petites requêtes d'E/S non contiguës en un nombre réduit de requêtes plus volumineuses. Ensuite, il y aurait une bibliothèque d'E/S haut de gamme comme HDF5, NetCDF, etc. Son rôle est de mapper les abstractions d'application aux abstractions de stockage d'E/S en termes de structures de données du code. Ainsi, les données sont stockées directement sur le disque en appelant cette bibliothèque, et cette bibliothèque est conçue pour fonctionner de manière très efficace. Il est préférable d'utiliser ce type de bibliothèques, car nous supportons à la fois HDF5 et NetCDF. Vous pourriez également utiliser l'intergiciel d'E/S qu'est MPI-IO. Dans la présentation d'aujourd'hui, je me concentrerai davantage sur MPI-IO, qui fait partie de MPI-2. Cependant, je discuterai également des avantages et des inconvénients des différentes approches. Et puis, comme vous pouvez le constater, il y a l'application, qui est principalement votre programme, et c'est votre programme qui décidera d'utiliser une bibliothèque d'E/S haut de gamme ou un intergiciel d'E/S.

## Système de fichiers parallèle

Sur les systèmes nationaux, nous disposons d'un système de fichiers parallèle conçu pour évoluer efficacement jusqu'à des dizaines de milliers de nœuds de calcul. Pour de meilleures performances, les fichiers peuvent être répartis (striped) sur plusieurs disques. Cela signifie que le fichier ne réside pas sur un seul disque dur, mais sur plusieurs disques, de sorte que pendant qu'un disque dur effectue une opération de lecture, un autre disque peut renvoyer les données au programme.

Afin d'éviter que deux ou plusieurs processus différents accèdent au même fichier, les systèmes de fichiers parallèles utilisent des mécanismes de verrouillage pour gérer ce type d'accès concurrentiel aux fichiers. Ce qui se passe, c'est que les fichiers sont divisés en unités de « verrou » et dispersés sur plusieurs disques durs. Ensuite, les nœuds clients (qui sont des nœuds de calcul) obtiennent des verrous sur les unités auxquelles ils accèdent avant que l'E/S ne se produise.

*   Les fichiers peuvent être répartis sur plusieurs disques pour de meilleures performances.
*   Des **verrous** sont utilisés pour gérer l'accès concurrentiel aux fichiers dans la plupart des systèmes de fichiers parallèles.
    *   Les fichiers sont découpés en unités de « verrou » (dispersées sur de nombreux disques).
    *   Les nœuds clients obtiennent des verrous sur les unités auxquelles ils accèdent avant que l'E/S ne se produise.
    *   Permet la mise en cache sur les clients.
    *   Les verrous sont récupérés des clients lorsque d'autres souhaitent y accéder.

La partie la plus importante à retenir est que le système de fichiers parallèle est optimisé pour le stockage de fichiers partagés volumineux, potentiellement accessibles depuis de nombreux nœuds de calcul. Par conséquent, il présente de très mauvaises performances pour le stockage de nombreux fichiers de petite taille. Comme cela vous a probablement été dit lors de notre séminaire pour les nouveaux utilisateurs, nous recommandons fortement aux utilisateurs de ne pas générer des millions de petits fichiers.

De plus, la manière dont vous lisez et écrivez, votre format de fichier, le nombre de fichiers dans un répertoire et la fréquence de vos commandes `ls` affectent tous les utilisateurs! Assez souvent, nous recevons un ticket signalant qu'un utilisateur ne peut même pas exécuter `ls` dans son répertoire `/work`. La plupart de ces situations sont causées par un utilisateur qui effectue des activités d'E/S très intenses dans le répertoire, ce qui ralentit évidemment le système. Le système de fichiers est partagé sur le réseau Ethernet d'une grappe : solliciter excessivement le système de fichiers peut nuire aux communications entre processus, qui sont principalement liées à la communication MPI. Cela affecte également les autres utilisateurs.

Veuillez noter que les systèmes de fichiers ne sont pas infinis : bande passante, IOPs, nombre de fichiers, espace, etc.

*   Optimisé pour les fichiers partagés volumineux.
*   Mauvaise performance avec de nombreuses petites lectures/écritures (IOPs élevés) : Ne stockez pas des millions de petits fichiers.
*   Votre utilisation affecte tout le monde! (Différent des cas du CPU et de la RAM qui ne sont pas partagés)
*   Facteurs critiques : votre façon de lire/écrire, le format de fichier, le nombre de fichiers dans un répertoire et la fréquence par seconde.
*   Le système de fichiers est partagé sur le réseau Ethernet d'une grappe : les E/S intenses peuvent empêcher la communication entre les processus.
*   Les systèmes de fichiers sont LIMITÉS : bande passante, IOPs, nombre de fichiers, espace, etc.

### Meilleures pratiques pour les E/S

Quelles seraient les meilleures pratiques pour les E/S?

Tout d'abord, il est toujours recommandé de planifier vos besoins en données : quelle quantité sera générée, combien devez-vous conserver et où les stocker.

Sur les systèmes nationaux, les différents systèmes de fichiers (`home`, `project`, `scratch`) ont des quotas différents. Les données `scratch` sont également sujettes à expiration. Pour plus de détails, consultez [ce document](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/services-nationaux/stockage). Tenez compte de ces limites avant de soumettre une tâche.

Veuillez également minimiser l'utilisation des commandes `ls` ou `du`, surtout dans un répertoire contenant de nombreux fichiers.

Vérifiez régulièrement votre utilisation du disque avec la commande `quota`. De plus, soyez attentif aux signaux d'avertissement qui devraient inciter à une réflexion approfondie lorsque vous avez plus de 100 000 fichiers dans votre espace et une taille moyenne de fichier de données inférieure à 100 Mo (si vous écrivez beaucoup de données).

Effectuez régulièrement un « ménage » pour maintenir un nombre raisonnable de fichiers et de quotas. Les commandes `gzip` et `tar` sont très populaires pour compresser et regrouper plusieurs fichiers. Ainsi, vous pourriez réduire le nombre de fichiers en utilisant ces commandes.

*   Planifiez vos besoins en données : Combien en générerez-vous? Combien devez-vous sauvegarder? Où les conserverez-vous?
*   Surveillez et contrôlez l'utilisation : Minimisez l'utilisation des commandes du système de fichiers comme `ls` et `du` dans les grands répertoires.
*   Vérifiez régulièrement votre utilisation du disque avec `quota`.
*   !!! warning
    *   **Avertissement!**
        *   plus de 100 000 fichiers dans votre espace
        *   taille moyenne des fichiers de données inférieure à 100 Mo pour une sortie volumineuse
*   Faites le « ménage » (gzip, tar, supprimer) régulièrement.

## Formats de données

### ASCII

Tout d'abord, il y a le format ASCII, ou certains l'appellent le format « texte ». C'est un format de fichier lisible par l'humain, mais inefficace. Il est donc idéal pour un petit fichier d'entrée ou de paramètres pour exécuter un code. Le format ASCII utilise une plus grande quantité de stockage que les autres types de formats et, automatiquement, il coûte plus cher en opérations de lecture/écriture. Vous pourriez vérifier votre implémentation de code si vous trouvez `fprintf` dans le code C ou la commande `open` avec l'option `formatted` dans le code FORTRAN.

*   **ASCII** = **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange (Code Américain Standard pour l'Échange d'Information)
*   avantages : lisible par l'humain, portable (indépendant de l'architecture)
*   inconvénients : stockage inefficace (13 octets par flottant simple précision, 22 octets par double précision, plus les délimiteurs), coûteux pour la lecture/écriture

```
fprintf() en C
open(6,file='test',form='formatted');write(6,*) en F90
```

### Binaire

Le format binaire est beaucoup plus « économique » en termes de calcul que l'ASCII. L'ASCII utilise 13 octets pour la simple précision et 22 pour la double précision. Le tableau présente une expérience d'écriture de 128 millions de nombres double précision à différents emplacements : `/scratch` et `/tmp` sur le système GPCS de SciNet. Comme vous pouvez le constater, il est évident que l'écriture binaire prend beaucoup moins de temps que le format ASCII.

| Format  | /scratch | /tmp (disque) |
| :------ | :------- | :------------ |
| ASCII   | 173 s    | 260 s         |
| Binaire | 6 s      | 20 s          |

*   avantages : stockage efficace (4 octets par flottant simple précision, 8 octets par double précision, pas de délimiteurs), lecture/écriture efficace
*   inconvénients : il faut connaître le format pour lire, portabilité (endianness)

```
fwrite() en C
open(6,file='test',form='unformatted'); write(6) en F90
```

### Métadonnées (XML)

Bien que le format binaire fonctionne bien et soit efficace, il peut parfois être nécessaire de stocker des informations supplémentaires telles que le nombre de variables dans un tableau, ses dimensions et sa taille, etc. Les métadonnées sont donc utiles pour décrire le binaire. Si vous transmettez des fichiers binaires à quelqu'un d'autre ou à d'autres programmes, il serait très utile d'inclure ces informations et d'utiliser le format de métadonnées. Incidemment, cela peut également être réalisé en utilisant des bibliothèques haut de gamme comme HDF5 et NetCDF.

*   Encode des données sur les données : nombre et noms des variables, leurs dimensions et tailles, endianness, propriétaire, date, liens, commentaires, etc.

### Base de données

Le format de données de base de données est idéal pour de nombreux petits enregistrements. L'utilisation d'une base de données peut grandement simplifier l'organisation et l'analyse des données. CHARENTE prend en charge trois différents progiciels de base de données. Cependant, ce n'est pas très courant dans la simulation numérique.

*   approche de stockage très puissante et flexible
*   l'organisation et l'analyse des données peuvent être grandement simplifiées
*   performances améliorées en matière de recherche/tri selon l'utilisation
*   logiciels open source : SQLite (sans serveur), PostgreSQL, MySQL

### Bibliothèques de jeux de données scientifiques standard

Il existe des bibliothèques de jeux de données scientifiques standard. Comme mentionné dans la diapositive précédente, ces bibliothèques sont très efficaces non seulement pour stocker de grands tableaux de manière efficiente, mais elles incluent également des descriptions de données que le format de métadonnées gère bien. De plus, ces bibliothèques offrent une portabilité des données entre différentes plateformes et langages, ce qui signifie que les binaires générés sur une machine peuvent être lus sur d'autres machines sans problème. Les bibliothèques stockent automatiquement les données avec compression. Cela peut être extrêmement utile. Par exemple, si vous exécutez une simulation à grande échelle et que vous devez stocker un grand ensemble de données, notamment avec de nombreuses valeurs répétées comme le zéro, alors les bibliothèques peuvent compresser ces valeurs répétées efficacement, ce qui vous permet de réduire considérablement le stockage des données.

*   HDF5 = Hierarchical Data Format (Format de données hiérarchique)
*   NetCDF = Network Common Data Format (Format de données commun de réseau)
*   Normes ouvertes et bibliothèques open source
*   Offrent une portabilité des données entre les plateformes et les langages
*   Stockent les données en binaire avec compression optionnelle
*   Incluent une description des données
*   Offrent optionnellement des E/S parallèles

## E/S séquentielles et parallèles

Dans les calculs parallèles à grande échelle, votre jeu de données est distribué sur de nombreux processeurs/nœuds. Comme illustré à droite, par exemple, le domaine de calcul est décomposé en plusieurs blocs de travail, et chaque nœud prend en charge une allocation. Par conséquent, chaque nœud calculera le domaine alloué et tentera de stocker les données sur le disque. Malheureusement, dans ce cas, l'utilisation d'un système de fichiers parallèle ne suffit pas – vous devez organiser vous-même les E/S parallèles. Cela sera discuté sous peu. Pour le format de fichier, il existe quelques options, comme un binaire brut sans information de métadonnées ou l'utilisation de bibliothèques haut de gamme (HDF5/NetCDF).

*   Dans les calculs parallèles à grande échelle, votre jeu de données est distribué sur de nombreux processeurs/nœuds.
*   Dans ce cas, l'utilisation d'un système de fichiers parallèle ne suffit pas – vous devez organiser vous-même les E/S parallèles.
*   Les données peuvent être écrites en binaire brut, HDF5 et NetCDF.

### E/S séquentielles (Un seul CPU)

Lorsque vous tentez d'écrire vos données de la mémoire de plusieurs nœuds de calcul vers un seul fichier sur le disque, plusieurs approches sont possibles. L'approche la plus simple consiste à désigner un « porte-parole » pour collecter toutes les données des autres membres de la communication. Une fois que les données sont entièrement collectées via la communication, elles sont écrites dans un fichier comme une E/S séquentielle normale. C'est une solution très simple et facile à implémenter, mais elle présente plusieurs problèmes. Premièrement, la bande passante d'écriture est limitée par le débit d'un seul client, et cela s'applique également à la limite de mémoire. Deuxièmement, le temps d'opération augmente linéairement avec la quantité de données ou la taille du problème, et de plus, il augmente avec le nombre de processus membres, car il faudra plus de temps pour collecter toutes les données sur un seul nœud ou CPU. Par conséquent, ce type d'approche ne peut pas passer à l'échelle.

*   **Avantages :**
    *   trivialement simple pour les petites E/S
    *   certaines bibliothèques d'E/S ne sont pas parallèles
*   **Inconvénients :**
    *   bande passante limitée par le débit qu'un seul client peut maintenir
    *   peut ne pas avoir suffisamment de mémoire sur un nœud pour contenir toutes les données
    *   ne passera pas à l'échelle (goulot d'étranglement intégré)

### E/S séquentielles (N processeurs)

Ce que vous pouvez faire à la place est d'organiser chaque processus participant pour effectuer une E/S séquentielle. En d'autres termes, tous les processus effectuent des E/S vers des fichiers individuels. C'est quelque peu plus efficace que le modèle précédent, mais jusqu'à une certaine limite.

Premièrement, lorsque vous avez beaucoup de données, vous vous retrouverez avec de nombreux fichiers. Un fichier par processeur. Si vous exécutez un calcul de grande envergure avec de nombreuses itérations et de nombreuses variables, même une seule exécution de simulation pourrait générer plus d'un millier de fichiers de sortie. Dans ce cas, comme nous l'avons déjà mentionné, le système de fichiers parallèle présente de faibles performances. Nous avons de nouveau examiné les meilleures pratiques en matière d'E/S, et des centaines de milliers de fichiers sont fortement déconseillés.

Deuxièmement, les données de sortie doivent souvent être post-traitées en un seul fichier. Il s'agit d'une étape supplémentaire qui serait certainement assez inefficace. De plus, lorsque chaque processeur tente d'accéder au disque à peu près au même moment, des E/S non coordonnées peuvent submerger le système de fichiers (verrous de fichiers!).

*   **Avantages :**
    *   aucune communication ou coordination inter-processus nécessaire
    *   évolutivité potentiellement meilleure que les E/S séquentielles uniques
*   **Inconvénients :**
    *   à mesure que le nombre de processus augmente, beaucoup de (petits) fichiers, ne passera pas à l'échelle
    *   les données doivent souvent être post-traitées en un seul fichier
    *   les E/S non coordonnées peuvent submerger le système de fichiers (verrous de fichiers!)

### E/S parallèles (N processus vers/depuis 1 fichier)

La meilleure approche consiste à effectuer des E/S parallèles appropriées. Ainsi, chaque processus participant écrit les données simultanément dans un seul fichier en utilisant les E/S parallèles. La seule chose dont vous devez être conscient est que vous voudrez peut-être effectuer ces E/S parallèles de manière coordonnée. Sinon, cela submergera le système de fichiers.

*   **Avantages :**
    *   un seul fichier (bon pour la visualisation, la gestion des données, le stockage)
    *   les données peuvent être stockées de manière canonique
    *   éviter le post-traitement passera à l'échelle si cela est fait correctement
*   **Inconvénients :**
    *   les E/S non coordonnées submergeront le système de fichiers (verrous de fichiers!)
    *   nécessite plus de conception et de réflexion

### Les E/S parallèles doivent être collectives!

Par exemple, les intergiciels parallèles comme MPI-IO offrent plusieurs types d'options d'écriture coordonnées ou non coordonnées. Une fois qu'une écriture coordonnée, telle qu'une E/S collective, est appelée, l'intergiciel parallèle saura quels processus et disques seront impliqués. Ensuite, l'intergiciel parallèle trouvera des opérations optimisées dans les couches logicielles inférieures pour une meilleure efficacité.

*   Les opérations d'**E/S indépendantes** spécifient uniquement ce qu'un seul processus fera.
*   Les **E/S collectives** sont un accès coordonné au stockage par un groupe de processus.
*   Les fonctions sont appelées par tous les processus participant aux E/S.
*   Permet au système de fichiers d'en savoir plus sur l'accès global, plus d'optimisation dans les couches logicielles inférieures, de meilleures performances.

## Techniques d'E/S parallèles

Cela fait partie de la norme MPI-2. Ainsi, MPI-IO est idéal pour écrire un fichier binaire brut. Comme vous pouvez le lire sur cette diapositive, les bibliothèques haut de gamme telles que HDF5 et NetCDF sont construites sur MPI-IO. Par conséquent, vous devriez de toute façon disposer de MPI-IO.

*   MPI-IO : partie des E/S parallèles de la norme MPI-2 (1996)
*   HDF5 (Hierarchical Data Format), construit sur MPI-IO
*   Parallel NetCDF (Network Common Data Format), construit sur MPI-IO

### MPI-IO

MPI-IO est disponible sur nos systèmes en tant que module par défaut, OpenMPI. MPI-IO exploite les analogies avec MPI ; l'écriture/lecture vers/depuis un fichier serait très similaire à la pratique d'envoi/réception MPI si vous avez une certaine expérience avec MPI. Par exemple, l'accès aux fichiers est regroupé via un communicateur dans MPI. Le communicateur est un groupe pour le passage de messages dans MPI. Des types de données MPI définis par l'utilisateur sont également disponibles.

*   Fait partie de la norme MPI-2
*   ROMIO est l'implémentation de MPI-IO dans OpenMPI (par défaut sur nos systèmes), MPICH2
*   Le seul intergiciel d'E/S parallèles pour le calcul scientifique largement disponible
*   MPI-IO exploite les analogies avec MPI
    *   écriture, envoi de message
    *   lecture, réception de message
    *   accès aux fichiers regroupé via un communicateur : opérations collectives
    *   types de données MPI définis par l'utilisateur, p. ex. pour la disposition de données non contiguës
    *   toutes les fonctionnalités via des appels de fonction

#### Opérations MPI-IO de base en C

```c
int MPI_File_open ( MPI_Comm comm, char* filename, int amode, MPI_Info info, MPI_File* fh); 
int MPI_File_seek ( MPI_File fh, MPI_Offset offset, int to); // met à jour le pointeur de fichier individuel
int MPI_File_set_view ( MPI_File fh, MPI_Offset offset, MPI_Datatype etype, MPI_Datatype filetype, char* datarep, MPI_Info info); 
// modifie la vue du processus sur les données dans le fichier
// etype est le type de donnée élémentaire
int MPI_File_read ( MPI_File fh, void* buf, int count, MPI_Datatype datatype, MPI_Status* status); 
int MPI_File_write (MPI_File fh, void* buf, int count, MPI_Datatype datatype, MPI_Status* status); 
int MPI_File_close ( MPI_File* fh); 
```

Voici un squelette simple pour les opérations MPI-IO en C. Comme un code MPI, il comporte `MPI_File_open` et `close` au début et à la fin. Il y a `File_write` et `File_read`. Et aussi, il y a `MPI_File_seek` qui est utilisé pour mettre à jour le pointeur de fichier individuel. Cela sera discuté en détail sous peu.

`MPI_File_set_view` est utilisé pour assigner des régions du fichier à des processus distincts. Les vues de fichier sont spécifiées à l'aide d'un triplet – (déplacement, `etype`, et `filetype`) – qui est passé à `MPI_File_set_view`.

*   déplacement = nombre d'octets à ignorer depuis le début du fichier
*   `etype` = unité d'accès aux données (peut être n'importe quel type de donnée de base ou dérivé)
*   `filetype` = spécifie quelle portion du fichier est visible par le processus

#### Opérations MPI-IO de base en F90

```fortran
MPI_FILE_OPEN (integer comm, character[] filename, integer amode, integer info, integer fh, integer ierr) 
MPI_FILE_SEEK (integer fh, integer(kind=MPI_OFFSET_KIND) offset, integer whence, integer ierr) 
! met à jour le pointeur de fichier individuel
MPI_FILE_SET_VIEW (integer fh, integer(kind=MPI_OFFSET_KIND) offset, integer etype, integer filetype, character[] datarep, integer info, integer ierr)
! modifie la vue du processus sur les données dans le fichier 
! etype est le type de donnée élémentaire
MPI_FILE_READ (integer fh, type buf, integer count, integer datatype, integer[MPI_STATUS_SIZE] status, integer ierr) 
MPI_FILE_WRITE (integer fh, type buf, integer count, integer datatype, integer[MPI_STATUS_SIZE] status, integer ierr) 
MPI_FILE_CLOSE (integer fh)
```

#### L'ouverture d'un fichier nécessite...

L'ouverture d'un fichier nécessite un communicateur, un nom de fichier et un descripteur de fichier pour toutes les références futures au fichier. De plus, elle requiert un mode d'accès au fichier (`amode`). Il existe plusieurs modes différents, comme `MPI_MODE_WRONLY` qui signifie « écriture seule ». Vous pouvez les combiner en utilisant l'opérateur « ou » bit à bit (`|`) en C ou l'addition (`+`) en FORTRAN.

*   Communicateur
*   Nom de fichier
*   Descripteur de fichier, pour toutes les références futures au fichier
*   Mode d'accès au fichier (`amode`), composé de combinaisons de :

```
MPI_MODE_RDONLY              Lecture seule
MPI_MODE_RDWR                Lecture et écriture
MPI_MODE_WRONLY              Écriture seule
MPI_MODE_CREATE              Créer le fichier s'il n'existe pas
MPI_MODE_EXCL                Erreur si le fichier à créer existe déjà
MPI_MODE_DELETE_ON_CLOSE     Supprimer le fichier à la fermeture
MPI_MODE_UNIQUE_OPEN         Le fichier ne doit pas être ouvert ailleurs
MPI_MODE_SEQUENTIAL          Le fichier doit être accédé séquentiellement
MPI_MODE_APPEND              Positionner tous les pointeurs de fichier à la fin
```

*   Combinez-les en utilisant l'opérateur « ou » bit à bit (`|`) en C ou l'addition (`+`) en FORTRAN.
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

#### Lecture/écriture de données contiguës

Imaginons l'écriture d'un fichier à partir de quatre processus différents. Comme le montre la figure, chaque processus écrira ses données dans une portion désignée du même fichier. L'écriture se déroule de manière contiguë du processus 0 au processus 3.

#### Exemple en C

En gros, nous initialisons MPI et plusieurs tableaux de variables. En utilisant `MPI_Comm_rank`, chaque processus aura son propre rang ou identifiant de processus. En utilisant `for (i=0)`, le tableau `a` est défini avec son rang pour une taille de tableau de 10. Par exemple, sur le processus 3, un tableau de 10 caractères '3' est créé.

```c
MPI_File_open (MPI_COMM_WORLD, "data.out" , MPI_MODE_CREATE|MPI_MODE_WRONLY, MPI_INFO_NULL, &fh);
```

Nous avons défini le communicateur et le nom de fichier « data.out ». Pour le mode, nous avons combiné « écriture seule » (`MPI_MODE_WRONLY`) et « créer le fichier s'il n'existe pas » (`MPI_MODE_CREATE`). Ensuite, nous définons le décalage (offset) où chaque processus commence à écrire. Comme vous pouvez le voir, le processus 0 commence au début et le processus 1 est le suivant, de manière contiguë.

```c
MPI_Offset displace = rank * n * sizeof(char);
```

Ainsi, le décalage (offset) sera calculé en multipliant `rank * taille_du_tableau * sizeof(char)`. Nous sommes maintenant prêts à assigner les régions d'écriture à chaque processus en utilisant `MPI_File_set_view`. Le déplacement (`displacement`) est défini, `etype` et `filetype` sont définis comme `MPI_CHAR`. « native » signifie que les données dans cette représentation sont stockées dans un fichier exactement comme elles le sont en mémoire. Ensuite, nous exécutons la commande d'écriture à l'aide de `MPI_File_write`.

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, i; 
    char a[10];
    MPI_Offset n = 10; 
    MPI_File fh; 
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    for (i = 0; i < 10; i++) {
        a[i] = (char)('0' + rank); // e.g. on processor 3 creates a[0:9]='3333333333'
    }

    MPI_File_open(MPI_COMM_WORLD, "data.out", MPI_MODE_CREATE | MPI_MODE_WRONLY, MPI_INFO_NULL, &fh); 
    MPI_Offset displace = rank * n * sizeof(char); // start of the view for each processor

    MPI_File_set_view(fh, displace, MPI_CHAR, MPI_CHAR, "native", MPI_INFO_NULL); 
    // note that etype and filetype are the same

    MPI_File_write(fh, a, n, MPI_CHAR, &status);
    
    MPI_File_close(&fh);
    MPI_Finalize();
    return 0;
}
```

#### Résumé : MPI-IO

Comme vous l'avez peut-être remarqué, son implémentation semble assez directe. Il doit exister beaucoup de matériel avancé utilisant MPI-IO, mais cela semble un peu au-delà de la portée de ce séminaire. Donc, en résumé, MPI-IO fait partie de la bibliothèque standard MPI-2 et est très largement installé sur presque tous les systèmes de calcul haute performance (CHP) avec des versions modernes de MPI. Nous avons installé OpenMPI, qui prend en charge MPI-IO sur toutes nos grappes. MPI-IO ne nécessite pas l'installation de bibliothèques supplémentaires, mais malheureusement, il écrit des données brutes dans un fichier. Il n'est donc pas portable entre les plateformes, il est difficile d'ajouter de nouvelles variables et il n'inclut pas de description des données.

### NetCDF

**N**etwork **C**ommon **D**ata **F**ormat

NetCDF est l'un des progiciels les plus populaires pour le stockage de données. Essentiellement, NetCDF comble toutes les lacunes de MPI-IO. Il utilise MPI-IO en arrière-plan, mais au lieu de spécifier le décalage, il suffit d'appeler NetCDF et d'indiquer les tableaux que vous souhaitez stocker. NetCDF s'en chargera alors et tentera de les stocker de manière contiguë. Dans NetCDF, les données sont stockées en binaire et, comme mentionné précédemment, il prend en charge l'auto-description, les métadonnées dans l'en-tête, la portabilité entre différentes architectures et une compression optionnelle. Un des meilleurs points par rapport à HDF5 est que NetCDF prend en charge une variété de progiciels de visualisation tels que Paraview. Nous disposons des versions sérielles et parallèles de NetCDF sur nos systèmes.

*   Format pour stocker de grands tableaux, utilise MPI-IO en arrière-plan.
*   Bibliothèques pour C/C++, Fortran 77/90/95/2003, Python, Java, R, Ruby, etc.
*   Données stockées en binaire.
*   Auto-descriptif, métadonnées dans l'en-tête (peuvent être interrogées par des utilitaires).
*   Portable entre différentes architectures.
*   Compression optionnelle.
*   Utilise MPI-IO, optimisé pour la performance.
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

    for (x = 0; x < NX; x++) {
        for (y = 0; y < NY; y++) {
            data_out[x][y] = x * NY + y;
        }
    }
    
    // Créer un nouveau fichier NetCDF
    retval = nc_create(FILE_NAME, NC_CLOBBER, &ncid); 
    // Définir les dimensions
    retval = nc_def_dim(ncid, "x", NX, &x_dimid); 
    retval = nc_def_dim(ncid, "y", NY, &y_dimid);
    dimids[0] = x_dimid;
    dimids[1] = y_dimid;
    // Définir la variable
    retval = nc_def_var(ncid, "data", NC_INT, NDIMS, dimids, &varid); 
    // Fin de la phase de définition
    retval = nc_enddef(ncid);
    // Écrire les données
    retval = nc_put_var_int(ncid, varid, &data_out[0][0]);
    // Fermer le fichier
    retval = nc_close(ncid);

    return 0; 
}
```

### HDF5

**H**ierarchical **D**ata **F**ormat

HDF5 est également un outil très populaire pour le stockage de données. Il prend en charge la plupart des fonctionnalités de NetCDF, telles que le format de fichier auto-descriptif pour les grands jeux de données, et utilise également MPI-IO en arrière-plan. Fondamentalement, HDF5 est plus général que NetCDF, avec une description orientée objet des jeux de données, des groupes, des attributs, des types, des espaces de données et des listes de propriétés. Nous disposons des versions sérielles et parallèles de HDF5 sur nos systèmes.

*   Format de fichier auto-descriptif pour les grands jeux de données, utilise MPI-IO en arrière-plan.
*   Bibliothèques pour C/C++, Fortran 90, Java, Python, R.
*   Plus général que NetCDF, avec une description orientée objet des jeux de données, des groupes, des attributs, des types, des espaces de données et des listes de propriétés.
*   Le contenu des fichiers peut être organisé comme un système de fichiers de type Unix : `/chemin/vers/la/ressource`.
    *   jeux de données contenant des images/tableaux/matrices multidimensionnelles homogènes
    *   groupes contenant des structures pouvant contenir des jeux de données et d'autres groupes
*   Les informations d'en-tête peuvent être interrogées par des utilitaires.
*   Compression optionnelle (utile pour les tableaux contenant de nombreux éléments similaires).
*   Nous fournissons HDF5 sériel et parallèle.

## Références

*   https://www.nhr.kit.edu/userdocs/horeka/parallel_IO/
*   https://hpc-forge.cineca.it/files/CoursesDev/public/2017/Parallel_IO_and_management_of_large_scientific_data/Roma/MPI-IO_2017.pdf
*   https://janth.home.xs4all.nl/MPIcourse/PDF/08_MPI_IO.pdf
*   https://events.prace-ri.eu/event/176/contributions/59/attachments/170/326/Advanced_MPI_II.pdf
*   https://www.cscs.ch/fileadmin/user_upload/contents_publications/tutorials/fast_parallel_IO/MPI-IO_NS.pdf