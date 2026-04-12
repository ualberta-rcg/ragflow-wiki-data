---
title: "MPI/fr"
slug: "mpi"
lang: "fr"

source_wiki_title: "MPI/fr"
source_hash: "8593fded8a4c91b25bbb60f80c158f6f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:52:46.262260+00:00"

tags:
  - software

keywords:
  - "MPI_Send et MPI_Recv"
  - "log output"
  - "Fortran"
  - "Hello World"
  - "communication"
  - "message reçu"
  - "modèle SPMD"
  - "interblocage"
  - "communication séquentielle"
  - "synchronisation"
  - "MPI_Init"
  - "16"
  - "langage C"
  - "world.recv"
  - "envoi-réception"
  - "blocage"
  - "Calcul Canada"
  - "arguments en ligne de commande"
  - "MPI_Finalize"
  - "world.send"
  - "envoi"
  - "mémoire distribuée"
  - "MPI_Send"
  - "communication collective"
  - "communicateur"
  - "argument status"
  - "Fortran 2008"
  - "IDRIS"
  - "réception"
  - "programme MPI"
  - "processus"
  - "MPI_SEND"
  - "MPI_Status"
  - "Institut du développement et des ressources en informatique scientifique"
  - "mémoire partagée"
  - "size"
  - "processus en attente"
  - "couples pair-impair"
  - "MPI_FINALIZE"
  - "mpi_f08"
  - "Formation MPI"
  - "boucle"
  - "outmessage"
  - "rang"
  - "compilation"
  - "message"
  - "programme parallèle"
  - "rank"
  - "programmation parallèle"
  - "Open MPI"
  - "informatique scientifique"
  - "C"
  - "appels bloquants"
  - "process ID"
  - "Message Passing Interface"
  - "phello3"
  - "process"
  - "mémoire tampon"
  - "erreur de segmentation"
  - "enveloppes de compilateurs"
  - "MPI_Recv"
  - "interfaces avec Fortran C et C++"
  - "erreur de la fonction"
  - "opérateur modulo"
  - "type de données"
  - "tutoriel"
  - "Hello world"
  - "MPI_COMM_WORLD"
  - "MPI"
  - "appel bloqué"

questions:
  - "Quelles sont les principales différences entre les modèles de programmation parallèle à mémoire partagée et à mémoire distribuée ?"
  - "Pourquoi la gestion de la communication représente-t-elle le défi majeur dans la conception de programmes parallèles ?"
  - "Qu'est-ce que la norme MPI et quels avantages offre-t-elle pour le développement dans un environnement à mémoire distribuée ?"
  - "Comment les erreurs de segmentation sont-elles gérées et déboguées dans ce contexte ?"
  - "Pourquoi un programme MPI donne-t-il l'impression d'être plus complexe qu'un programme à communication implicite ?"
  - "Quelle pratique est recommandée pour optimiser la vitesse de calcul d'un programme MPI ?"
  - "Qu'est-ce que le modèle d'exécution SPMD utilisé par MPI et comment permet-il d'attribuer un comportement différent à chaque instance ?"
  - "Quels sont les scripts de compilation (wrappers) recommandés pour compiler un programme MPI selon le langage de programmation choisi ?"
  - "Quelle fonction doit être appelée en premier lieu pour coordonner les instances MPI et comment les erreurs de cette fonction sont-elles retournées en C et en Fortran ?"
  - "Quels sont les arguments passés à la fonction MPI_Init en langage C et que représentent-ils ?"
  - "Comment la valeur de retour des fonctions MPI est-elle utilisée en C ?"
  - "Comment les erreurs sont-elles retournées par les routines MPI en Fortran et dans quel cas cet argument est-il optionnel ?"
  - "Quel est le rôle de la fonction MPI_Finalize et à quel moment est-il recommandé de l'appeler dans le cycle de vie d'un programme ?"
  - "Quelle est la différence entre les fonctions MPI_Comm_size et MPI_Comm_rank, et comment les valeurs de rang sont-elles attribuées aux processus ?"
  - "Qu'est-ce qu'un communicateur dans le contexte de MPI et que représente spécifiquement MPI_COMM_WORLD ?"
  - "Pourquoi n'est-il pas nécessaire d'introduire des énoncés conditionnels dans le code pour que chaque processus s'exécute correctement ?"
  - "Comment s'explique le fait que les sorties générées par les différents processus ne soient pas ordonnées selon leur rang lors de l'exécution ?"
  - "Quelle est la formule utilisée pour déterminer le destinataire du message de chaque processus lors de l'étape de communication en boucle ?"
  - "Quelle est la plage de valeurs possibles pour le rang d'un processus ?"
  - "Comment définit-on un « communicateur » dans le contexte de l'argument comm ?"
  - "Que représente spécifiquement le communicateur prédéfini MPI_COMM_WORLD ?"
  - "Quel message spécifique chaque processus doit-il transmettre à son voisin ?"
  - "Comment le dernier processus de rang N-1 procède-t-il pour boucler la boucle de communication ?"
  - "Quelle expression mathématique permet de définir de manière concise le rang du processus destinataire ?"
  - "Quels sont les principaux arguments nécessaires pour configurer et utiliser la fonction d'envoi de données MPI_Send ?"
  - "Quel est le rôle de l'argument datatype défini par la norme MPI et comment assure-t-il la compatibilité entre différentes architectures ?"
  - "Quelle est la particularité de la fonction de réception MPI_Recv par rapport à l'envoi, notamment en ce qui concerne l'argument status ?"
  - "Comment l'argument status est-il défini différemment dans les langages C et Fortran lors de l'utilisation de MPI_Recv ?"
  - "Quel est le rôle principal de l'argument status une fois que la fonction MPI_Recv a terminé son exécution ?"
  - "Pourquoi est-il indispensable d'inclure l'argument status dans les instructions de programmation malgré son absence dans les exemples fournis ?"
  - "Quelles sont les différences de syntaxe et de paramètres pour la fonction de réception MPI selon les langages de programmation illustrés ?"
  - "Comment un processus détermine-t-il mathématiquement le rang du processus auquel il doit envoyer un message et celui dont il doit en recevoir un ?"
  - "Quel est le fonctionnement global du programme parallèle fourni en exemple lors de l'utilisation conjointe de MPI_Send et MPI_Recv ?"
  - "How does the code calculate the target process for sending and the source process for receiving messages?"
  - "What specific information is formatted into the `outmessage` string before it is sent?"
  - "What is the exact format of the console output when a process successfully receives a message?"
  - "Quel est le problème de conception caché lié à l'utilisation de la fonction MPI_Send dans ce programme ?"
  - "Pourquoi le programme risque-t-il de se bloquer indéfiniment si la mémoire tampon n'est pas utilisée ?"
  - "Comment les bibliothèques des systèmes de Calcul Canada gèrent-elles l'envoi de messages et quelles sont les limites de cette approche ?"
  - "Quel est le rôle de la mémoire tampon dans le comportement bloquant des fonctions MPI_Send et MPI_Recv ?"
  - "Pourquoi l'exécution simultanée de MPI_Send par deux processus communicants crée-t-elle une situation à risque d'interblocage ?"
  - "Comment la stratégie des couples pair-impair permet-elle d'assurer la fiabilité du code et d'éviter les impasses ?"
  - "Pourquoi l'utilisation de `MPI_Send` peut-elle entraîner une attente indéfinie de tous les processus ?"
  - "Pour quelle raison le modèle de conception basé sur les mémoires tampons des systèmes de Calcul Canada est-il considéré comme non fiable ?"
  - "Quelles sont les conséquences pour le programme si la mémoire tampon de la bibliothèque est absente ou vient à être saturée ?"
  - "Comment la méthode des couples pair-impair organise-t-elle la communication séquentielle entre les processus ?"
  - "Quel est l'ordre d'exécution spécifique des actions d'envoi et de réception pour les processus pairs par rapport aux processus impairs ?"
  - "Quel problème majeur de synchronisation est éliminé grâce à cette approche en deux temps ?"
  - "What is the overall purpose and communication topology of the provided MPI programs?"
  - "Why do the programs use an even/odd conditional check based on the process rank for the send and receive operations?"
  - "How do the different language implementations (C, C++ with Boost, and Fortran) differ in their approach to constructing and formatting the outgoing message string?"
  - "What is the purpose of the MPI_SEND and MPI_FINALIZE subroutines in the provided code snippet?"
  - "How does the program utilize the rank and recvfrom variables when printing the received message?"
  - "What specific module and variable declarations are introduced in the Fortran 2008 version of the phello3 program?"
  - "Pourquoi le programme applique-t-il un ordre d'envoi et de réception différent selon que le rang du processus est pair ou impair ?"
  - "Pour quelle raison l'exécution du programme avec un nombre impair de processus ne provoque-t-elle aucun risque d'interblocage ?"
  - "Quelles commandes permettent de compiler et d'exécuter ce code MPI, et que démontre le résultat affiché dans la console ?"
  - "Quel est le rôle exact des enveloppes de compilateurs (comme mpicc ou mpifort) fournies par les bibliothèques MPI ?"
  - "Comment l'option `--showme` d'Open MPI permet-elle de vérifier l'interaction avec les différents modules de compilateurs (Intel, GCC) chargés dans l'environnement ?"
  - "Quels sont les concepts avancés et les autres considérations à explorer pour développer des applications parallèles robustes avec MPI ?"
  - "What is the total number of processes running in this system according to the log messages?"
  - "Which specific process numbers are explicitly recorded as sending a \"Hello, world!\" message in this text snippet?"
  - "What is the relationship between the bracketed identifiers, such as [P_13], and the process numbers that follow them?"
  - "Quels langages de programmation sont abordés dans l'ouvrage publié par MIT Press en 1999 ?"
  - "Quel auteur propose un livre de tutoriel sur la programmation parallèle avec MPI utilisant spécifiquement le langage C ?"
  - "Quels sont les auteurs et les institutions associés aux tutoriels en ligne recommandés pour l'apprentissage de MPI ?"
  - "Quel institut propose la formation mentionnée dans le texte ?"
  - "Quel est le sujet principal de la formation accessible via le lien fourni ?"
  - "Dans quelle langue cette formation sur MPI est-elle dispensée ?"
  - "Quel institut propose la formation mentionnée dans le texte ?"
  - "Quel est le sujet principal de la formation accessible via le lien fourni ?"
  - "Dans quelle langue cette formation sur MPI est-elle dispensée ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

> To pull a bigger wagon it is easier to add more oxen than to find (or build) a bigger ox. [traduction libre, *Pour tirer une plus grosse charrette, il est plus facile d'ajouter des bœufs que de trouver un plus gros bœuf.*]
> — Gropp, Lusk & Skjellum, *Using MPI*

Pour construire une maison le plus rapidement possible, on n'engage pas la personne qui peut faire tout le travail plus rapidement que les autres. On distribue plutôt le travail parmi autant de personnes qu'il faut pour que les tâches se fassent en même temps, d'une manière *parallèle*. Cette solution est valide aussi pour les problèmes numériques. Comme il y a une limite à vitesse d'exécution d'un processeur, la fragmentation du problème permet d'assigner des tâches à exécuter en parallèle par plusieurs processeurs. Cette approche sert autant la vitesse du calcul que les exigences élevées en mémoire.

L'aspect le plus important dans la conception et le développement de programmes parallèles est la communication. Ce sont les exigences de la communication qui créent la complexité. Pour que plusieurs travailleurs accomplissent une tâche en parallèle, ils doivent pouvoir communiquer. De la même manière, plusieurs processus logiciels qui travaillent chacun sur une partie d'un problème ont besoin de valeurs qui sont ou seront calculées par d'autres processus.

Il y a deux modèles principaux en programmation parallèle : les programmes à mémoire partagée et les programmes à mémoire distribuée.

Dans le cas d'une parallélisation avec mémoire partagée (SMP pour *shared memory parallelism*), les processeurs voient tous la même image mémoire, c'est-à-dire que la mémoire peut être adressée globalement et tous les processeurs y ont accès. Sur une machine SMP, les processeurs communiquent de façon implicite; chacun des processeurs peut lire et écrire en mémoire et les autres processeurs peuvent y accéder et les utiliser. Le défi ici est la cohérence des données puisqu'il faut veiller à ce que les données ne soient modifiées que par un seul processus à la fois.

Pour sa part, la parallélisation avec mémoire distribuée s'apparente à une grappe, un ensemble d'ordinateurs reliés par un réseau de communication dédié. Dans ce modèle, les processus possèdent chacun leur propre mémoire et ils peuvent être exécutés sur plusieurs ordinateurs distincts. Les processus communiquent par messages : un processus utilise une fonction pour envoyer un message et l'autre processus utilise une autre fonction pour recevoir le message. Le principal défi ici est d'avoir le moins de communications possible. Même les réseaux avec les connexions physiques les plus rapides transmettent les données beaucoup plus lentement qu'un simple ordinateur : l'accès mémoire se mesure habituellement en centièmes de nanosecondes alors que les réseaux y accèdent généralement en microsecondes.

Nous discuterons ici uniquement de la programmation avec mémoire distribuée sur grappe, avec MPI.

## Qu'est-ce que MPI?

MPI (*message passing interface*) est en réalité une norme avec des sous-routines, fonctions, objets et autres éléments pour développer des programmes parallèles dans un environnement à mémoire distribuée. MPI est implémentée dans plusieurs bibliothèques, notamment Open MPI, Intel MPI, MPICH et MVAPICH. La norme décrit comment MPI est appelé par Fortran, C et C++, mais il existe aussi des interfaces pour plusieurs autres langages (Boost.MPI, mpi4py, Rmpi, etc.). La version MPI 3.0 ne prend plus en charge les interfaces C++, mais vous pouvez utiliser les interfaces C de C++ ou [Boost MPI](https://www.boost.org/doc/libs/1_71_0/doc/html/mpi.html). Les exemples avec Python utilisent le MPI du paquet Python [MPI4py](../programming/mpi4py.md).

Puisque MPI est une norme ouverte sans droits exclusifs, un programme MPI peut facilement être porté sur plusieurs ordinateurs différents. Les programmes MPI peuvent être exécutés concurremment sur plusieurs cœurs à la fois et offrent une parallélisation efficace, permettant une bonne [scalabilité](../running-jobs/scalability.md). Puisque chaque processus possède sa propre plage mémoire, certaines opérations de débogage s'en trouvent simplifiées; en ayant des plages mémoire distinctes, les processus n’auront aucun conflit d’accès à la mémoire comme c'est le cas en mémoire partagée. Aussi, en présence d'une erreur de segmentation, le fichier *core* résultant peut être traité par des outils standards de débogage série. Le besoin de gérer la communication et la synchronisation de façon explicite donne par contre l'impression qu'un programme MPI est plus complexe qu'un autre programme où la gestion de la communication serait implicite. Il est cependant recommandé de restreindre les communications entre processus pour favoriser la vitesse de calcul d'un programme MPI.

Nous verrons plus loin quelques-uns de ces points et proposerons des stratégies de solution; les références mentionnées au bas de cette page sont aussi à consulter.

## Principes de base
Dans ce tutoriel, nous présenterons le développement d'un code MPI en C, C++, Fortran et Python, mais les différents principes de communication s'appliquent à tout langage qui possède une interface avec MPI. Notre but ici est de paralléliser le programme simple "Hello World" utilisé dans les exemples.

=== "C"
    ````c linenums="1" title="hello.c"
    #include <stdio.h>

    int main()
    {
        printf("Hello, world!\n");

        return(0);
    }
    ````

=== "C++"
    ````cpp linenums="1" title="hello.cpp"
    #include <iostream>
    using namespace std;

    int main()
    {
        cout << "Hello, world!" << endl;
        return 0;
    }
    ````

=== "Fortran"
    ````f90 linenums="1" title="hello.f90"
    program hello

        print *, 'Hello, world!'

    end program hello
    ````

=== "Python"
    ````python linenums="1" title="hello.py"
    print('Hello, world!')
    ````

Pour compiler et exécuter le programme :

```bash
vi hello.c
cc -Wall hello.c -o hello
./hello
```
```text
Hello, world!
```

### Modèle SPMD
La parallélisation MPI utilise le modèle d'exécution SPMD (*single program multiple data*), où plusieurs instances s'exécutent en même temps. Chacune des instances est un processus auquel est assigné un numéro unique qui représente son rang; l'instance peut obtenir son rang lorsqu'elle est lancée. Afin d'attribuer un comportement différent à chaque instance, on utilisera habituellement un énoncé conditionnel *if*.

### Cadre d'exécution
Un programme MPI doit comprendre le fichier d'en-tête approprié ou utiliser le modèle approprié (`mpi.h` pour C/C++, `mpif.h`, `use mpi`, ou `use mpi_f08` pour Fortran, sachant que `mpif.h` est fortement déconseillé et `mpi_f08` recommandé pour Fortran 2008). Il peut donc être compilé puis relié à l'implémentation MPI de votre choix. Dans la plupart des cas, l'implémentation possède un script pratique qui enveloppe l'appel au compilateur (*compiler wrapper*) et qui configure adéquatement `include` et `lib`, entre autres pour relier les indicateurs. Nos exemples utilisent les scripts de compilation suivants :
*   pour le C, `mpicc`
*   pour le Fortran, `mpifort` (recommandé) ou `mpif90`
*   pour le C++, `mpiCC` ou `mpicxx`

Une fois les instances lancées, elles doivent se coordonner, ce qui se fait en tout premier lieu par l'appel d'une fonction d'initialisation :

=== "C"
    ```c
    int MPI_Init(int *argc, char **argv[]);
    ```

=== "Boost (C++)"
    ```cpp
    boost::mpi::environment(int &, char **&, bool = true);
    ```

=== "Fortran"
    ```fortran
    MPI_INIT(IERR)
    INTEGER :: IERR
    ```

=== "Fortran 2008"
    ```fortran
    MPI_Init(ierr)
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr
    ```

=== "Python (mpi4py)"
    ```python
    # importing automatically initializes MPI with mpi4py
    MPI.Init()
    ```

En C, les arguments de `MPI_Init` pointent vers les variables `argc` et `argv` qui sont les arguments en ligne de commande. Comme pour toutes les fonctions MPI en C, la valeur retournée représente l'erreur de la fonction. En Fortran, les routines MPI retournent l'erreur dans l'argument `IERR`, ce qui est optionnel avec `use mpi_f08`.

On doit aussi appeler la fonction `MPI_Finalize` pour faire un nettoyage avant la fin du programme, le cas échéant :

=== "C"
    ```c
    int MPI_Finalize(void);
    ```

=== "Boost (C++)"
    Nothing needed

=== "Fortran"
    ```fortran
    MPI_FINALIZE(IERR)
    INTEGER :: IERR
    ```

=== "Fortran 2008"
    ```fortran
    MPI_Finalize(ierr)
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr
    ```

=== "Python (mpi4py)"
    ```python
    # mpi4py installs a termination hook so there is no need to explicitly call MPI.Finalize.
    MPI.Finalize()
    ```

Règle générale, il est recommandé d'appeler `MPI_Init` au tout début du programme et `MPI_Finalize` à la toute fin.

=== "C"
    ````c linenums="1" title="phello0.c"
    #include <stdio.h>
    #include <mpi.h>

    int main(int argc, char *argv[])
    {
        MPI_Init(&argc, &argv);

        printf("Hello, world!\n");

        MPI_Finalize();
        return(0);
    }
    ````

=== "Boost (C++)"
    ````cpp linenums="1" title="phello0.cpp"
    #include <iostream>
    #include <boost/mpi.hpp>
    using namespace std;
    using namespace boost;

    int main(int argc, char *argv[])
    {
        mpi::environment env(argc, argv);
        cout << "Hello, world!" << endl;
        return 0;
    }
    ````

=== "Fortran"
    ````f90 linenums="1" title="phello0.f90"
    program phello0

        use mpi
        implicit none

        integer :: ierror

        call MPI_INIT(ierror)
        print *, 'Hello, world!'
        call MPI_FINALIZE(ierror)

    end program phello0
    ````

=== "Fortran 2008"
    ````f90 linenums="1" title="phello0.f90"
    program phello0

        use mpi_f08
        implicit none

        call MPI_Init()
        print *, 'Hello, world!'
        call MPI_Finalize()

    end program phello0
    ````

=== "Python (mpi4py)"
    ````python linenums="1" title="phello0.py"
    from mpi4py import MPI
    print('Hello, world!')
    ````

### Fonctions *rank* et *size*
Le programme pourrait être exécuté tel quel, mais le résultat ne serait pas très convaincant puisque chacun des processus produirait le même message. Nous allons plutôt faire en sorte que chaque processus fasse afficher la valeur de son rang et le nombre total de processus en opération.

=== "C"
    ```c
    int MPI_Comm_size(MPI_Comm comm, int *nproc);
    int MPI_Comm_rank(MPI_Comm comm, int *myrank);
    ```

=== "Boost (C++)"
    ```cpp
    int mpi::communicator::size();
    int mpi::communicator::rank();
    ```

=== "Fortran"
    ```fortran
    MPI_COMM_SIZE(COMM, NPROC, IERR)
    INTEGER :: COMM, NPROC, IERR

    MPI_COMM_RANK(COMM, RANK, IERR)
    INTEGER :: COMM, RANK, IERR
    ```

=== "Fortran 2008"
    ```fortran
    MPI_Comm_size(comm, size, ierr)
    TYPE(MPI_Comm), INTENT(IN) :: comm
    INTEGER, INTENT(OUT) :: size
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr

    MPI_Comm_rank(comm, rank, ierr)
    TYPE(MPI_Comm), INTENT(IN) :: comm
    INTEGER, INTENT(OUT) :: rank
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr
    ```

=== "Python (mpi4py)"
    ```python
    MPI.Intracomm.Get_rank(self)

    MPI.Intracomm.Get_size(self)
    ```

Le paramètre de sortie `nproc` est donné à la fonction `MPI_Comm_size` afin d'obtenir le nombre de processus en opération. De même, le paramètre de sortie `myrank` est donné à la fonction `MPI_Comm_rank` afin d'obtenir la valeur du rang du processus actuel. Le rang du premier processus a la valeur de 0 au lieu de 1; pour N processus, les valeurs de rang vont donc de 0 à (N-1) inclusivement. L'argument `comm` est un *communicateur*, soit un ensemble de processus pouvant s'envoyer entre eux des messages. Dans nos exemples, nous utilisons la valeur de `MPI_COMM_WORLD`, soit un communicateur prédéfini par MPI et qui représente l'ensemble des processus lancés par la tâche. Nous n'abordons pas ici le sujet des communicateurs créés par programmation; voyez plutôt la liste des autres sujets en bas de page.

Utilisons maintenant ces fonctions pour que chaque processus produise le résultat voulu. Notez que, puisque les processus effectuent tous le même appel de fonction, il n'est pas nécessaire d'introduire des énoncés conditionnels.

=== "C"
    ````c linenums="1" title="phello1.c"
    #include <stdio.h>
    #include <mpi.h>

    int main(int argc, char *argv[])
    {
        int rank, size;

        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);

        printf("Hello, world! "
                "from process %d of %d\n", rank, size);

        MPI_Finalize();
        return(0);
    }
    ````

=== "Boost (C++)"
    ````cpp linenums="1" title="phello1.cpp"
    #include <iostream>
    #include <boost/mpi.hpp>
    using namespace std;
    using namespace boost;

    int main(int argc, char *argv[])
    {
        mpi::environment env(argc, argv);
        mpi::communicator world;

        cout << "Hello, world! from process " << world.rank() << " of " << world.size() << endl;
        return 0;
    }
    ````

=== "Fortran"
    ````f90 linenums="1" title="phello1.f90"
    program phello1

        use mpi
        implicit none

        integer :: rank, size, ierror

        call MPI_INIT(ierror)
        call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)
        call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

        print *, 'Hello from process ', rank, ' of ', size

        call MPI_FINALIZE(ierror)

    end program phello1
    ````

=== "Fortran 2008"
    ````f90 linenums="1" title="phello1.f90"
    program phello1

        use mpi_f08
        implicit none

        integer :: rank, size

        call MPI_Init()
        call MPI_Comm_size(MPI_COMM_WORLD, size)
        call MPI_Comm_rank(MPI_COMM_WORLD, rank)

        print *, 'Hello from process ', rank, ' of ', size

        call MPI_Finalize(ierror)

    end program phello1
    ````

=== "Python (mpi4py)"
    ````python linenums="1" title="phello1.py"
    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    print('Hello from process %d of %d'%(rank, size))
    ````

Compilez maintenant ce programme et faites-le exécuter avec 2, 4 et 8 processus. Vous remarquerez que le résultat produit par chacun des processus dépend de la valeur de ses variables locales et que le résultat final est la concaténation de la sortie standard (*stdout*) de tous les processus. Vous constaterez sans doute que les sorties produites par les processus ne sont pas nécessairement ordonnées selon leur rang : il n'est pas possible de prévoir l'ordre en sortie.
```bash
vi phello1.c
mpicc -Wall phello1.c -o phello1
mpirun -np 4 ./phello1
```
```text
Hello, world! from process 0 of 4
Hello, world! from process 2 of 4
Hello, world! from process 1 of 4
Hello, world! from process 3 of 4
```

Pour compiler avec Boost :
```bash
mpic++ --std=c++11 phello1.cpp -lboost_mpi-mt -lboost_serialization-mt -o phello1
```

Avec la version Python, vous n'avez pas besoin de compiler, mais vous pouvez exécuter avec
```bash
mpirun -np 4 python phello1.py
```

### Communication
Nous avons maintenant une version parallèle de ''Hello World'', mais sans communication entre les processus. Voyons ensuite cet aspect.

Nous demandons à chaque processus de transmettre au processus suivant le mot ''hello''. Le processus de rang `i` envoie son message au processus de rang `i+1` et le dernier processus de rang `N-1` envoie son message au processus de rang `0` pour boucler la boucle. Exprimé concisément, ''le processus `i` envoie au processus `(i+1)%N`'' où il y a `N` processus et où `%` est l'opérateur modulo.

MPI offre plusieurs fonctions pour échanger des données dans un grand nombre de relations entre processus (1,1; 1,n; n,1; n,n). Les fonctions les plus simples sont cependant celles qui échangent une ou plusieurs instances de données du même type de base, soit les fonctions `MPI_Send` et `MPI_Recv`.

Un processus envoie des données par la fonction `MPI_Send`. Examinons notre exemple :
*   `message` est un pointeur vers un vecteur de données à envoyer;
*   `count` représente le nombre d'instances contiguës de type `datatype` est le type des données;
*   `dest` est le rang du processus cible;
*   `tag` est un identifiant entier défini par le programmeur et associé au type de message à envoyer, ce qui est utile pour distinguer les différentes communications entre les processus. Cependant, puisque cet identifiant n'est toujours pas utile à notre exemple, nous choisissons la valeur arbitraire 0;
*   `MPI_COMM_WORLD` est le communicateur représentant tous les processus lancés par `mpirun`.

=== "C"
    ```c
    int MPI_Send
    (
        void *message,           /* reference to data to be sent */
        int count,               /* number of items in message */
        MPI_Datatype datatype,   /* type of item in message */
        int dest,                /* rank of process to receive message */
        int tag,                 /* programmer specified identifier */
        MPI_Comm comm            /* communicator */
    );
    ```

=== "Boost (C++)"
    ```cpp
    template<typename T> void mpi::communicator::send(
      int dest,                  /* rank of process to receive message */
      int tag,                          /* programmer specified identified */
      const T & value              /* message */
    ) const;
    ```

=== "Fortran"
    ```fortran
    MPI_SEND(MESSAGE, COUNT, DATATYPE, DEST, TAG, COMM, IERR)
    <type> MESSAGE(*)
    INTEGER :: COUNT, DATATYPE, DEST, TAG, COMM, IERR
    ```

=== "Fortran 2008"
    ```fortran
    MPI_Send(message, count, datatype, dest, tag, comm, ierr)
    TYPE(*), DIMENSION(..), INTENT(IN) :: message
    INTEGER, INTENT(IN) :: count, dest, tag
    TYPE(MPI_Datatype), INTENT(IN) :: datatype
    TYPE(MPI_Comm), INTENT(IN) :: comm
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr
    ```

=== "Python (mpi4py)"
    ```python
    # For general Python objects (pickled)
    MPI.Intracomm.send(self, obj, int dest, int tag=0)

    # For numpy arrays (fast)
    MPI.Intracomm.Send(self, buf, int dest, int tag=0)
    ```

Remarquez que l'argument `datatype` qui identifie le type des données contenues dans le *buffer* `message` est une variable définie par la norme MPI. Ceci assure une couche de compatibilité entre les processus opérant sur des architectures où le format natif des données serait différent. Il est possible d'utiliser de nouveaux types de données, mais nous nous limitons ici aux types définis nativement par MPI. En langage C : `MPI_CHAR`, `MPI_FLOAT`, `MPI_SHORT`, `MPI_INT`, etc.
En Fortran : `MPI_CHARACTER`, `MPI_INTEGER`, `MPI_REAL`, etc. Pour la liste complète des types de données, consultez la section Références en bas de page.

À la fonction de réception `MPI_Recv`, on ajoute l'argument `status` : en C, l'argument réfère à une structure allouée `MPI_Status` et en Fortran, l'argument contient une matrice `MPI_STATUS_SIZE` de nombres entiers ou, pour `mpi_f08`, une variable dérivée `TYPE(MPI_Status)`. À son retour, `MPI_Recv` contiendra de l'information sur le message reçu. Nos exemples ne montrent pas cet argument, mais il doit faire partie des instructions.

=== "C"
    ```c
    int MPI_Recv
    (
        void *message,           /* reference to buffer for received data */
        int count,               /* number of items to be received */
        MPI_Datatype datatype,   /* type of item to be received */
        int source,              /* rank of process from which to receive */
        int tag,                 /* programmer specified identifier */
        MPI_Comm comm            /* communicator */
        MPI_Status *status       /* stores info. about received message */
    );
    ```

=== "Boost (C++)"
    ```cpp
    template<typename T> status mpi::communicator::recv(
      int source,                  /* rank of process from which to receive */
      int tag,                          /* programmer specified identified */
      const T & value               /* message */
    ) const;
    ```

=== "Fortran"
    ```fortran
    MPI_RECV(MESSAGE, COUNT, DATATYPE, SOURCE, TAG, COMM, STATUS, IERR)
    <type> :: MESSAGE(*)
    INTEGER :: COUNT, DATATYPE, SOURCE, TAG, COMM, STATUS(MPI_STATUS_SIZE), IERR
    ```

=== "Fortran 2008"
    ```fortran
    MPI_Recv(message, count, datatype, source, tag, comm, status, ierr)
    TYPE(*), DIMENSION(..) :: message
    INTEGER, INTENT(IN) :: count, source, tag
    TYPE(MPI_Datatype), INTENT(IN) :: datatype
    TYPE(MPI_Comm), INTENT(IN) :: comm
    TYPE(MPI_Status) :: status
    INTEGER, OPTIONAL, INTENT(OUT) :: ierr
    ```

=== "Python (mpi4py)"
    ```python
    # For general Python objects (pickled)
    MPI.Intracomm.recv(self, buf=None, int source=ANY_SOURCE, int tag=ANY_TAG, Status status=None)

    # For numpy arrays (fast)
    MPI.Intracomm.Recv(self, buf, int source=ANY_SOURCE, int tag=ANY_TAG, Status status=None)
    ```

Dans notre cas simple avec `MPI_Send` et `MPI_Recv`, le processus qui envoie doit connaître le rang du processus qui reçoit et vice versa. Rappelons-nous des règles mathématiques suivantes :
*   `(rank + 1) % size` est le processus auquel on envoie
*   `(rank + size - 1) % size` est le processus duquel on reçoit
Modifions maintenant notre programme parallèle.

=== "C"
    ````c linenums="1" title="phello2.c"
    #include <stdio.h>
    #include <mpi.h>

    #define BUFMAX 81

    int main(int argc, char *argv[])
    {
        char outbuf[BUFMAX], inbuf[BUFMAX];
        int rank, size;
        int sendto, recvfrom;
        MPI_Status status;

        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);

        sprintf(outbuf, "Hello, world! from process %d of %d", rank, size);

        sendto = (rank + 1) % size;
        recvfrom = (rank + size - 1) % size;

        MPI_Send(outbuf, BUFMAX, MPI_CHAR, sendto, 0, MPI_COMM_WORLD);
        MPI_Recv(inbuf, BUFMAX, MPI_CHAR, recvfrom, 0, MPI_COMM_WORLD, &status);

        printf("[P_%d] process %d said: \"%s\"]\n", rank, recvfrom, inbuf);

        MPI_Finalize();
        return(0);
    }
    ````

=== "Boost (C++)"
    ````cpp linenums="1" title="phello.cpp"
    #include <iostream>
    #include <string>
    #include <boost/mpi.hpp>

    using namespace std;
    using namespace boost;

    int main(int argc, char *argv[])
    {
        mpi::environment env(argc, argv);
        mpi::communicator world;
        int rank = world.rank();
        int size = world.size();

        string outmessage = "Hello, world! from process " + to_string(rank) + " of " + to_string(size);
        string inmessage;
        int sendto = (rank + 1) % size;
        int recvfrom = (rank + size - 1) % size;

        cout << outmessage << endl;

        world.send(sendto,0,outmessage);
        world.recv(recvfrom,0,inmessage);

        cout << "[P_" << rank << "] process " << recvfrom << " said: \"" << inmessage << "\"" << endl;
        return 0;
    }
    ````

=== "Fortran"
    ````f90 linenums="1" title="phello2.f90"
    program phello2

        implicit none
        use mpi
        integer, parameter :: BUFMAX=81
        character(len=BUFMAX) :: outbuf, inbuf, tmp
        integer :: rank, num_procs, ierr
        integer :: sendto, recvfrom
        integer :: status(MPI_STATUS_SIZE)

        call MPI_INIT(ierr)
        call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)
        call MPI_COMM_SIZE(MPI_COMM_WORLD, num_procs, ierr)

        outbuf = 'Hello, world! from process '
        write(tmp,'(i2)') rank
        outbuf = outbuf(1:len_trim(outbuf)) // tmp(1:len_trim(tmp))
        write(tmp,'(i2)') num_procs
        outbuf = outbuf(1:len_trim(outbuf)) // ' of ' // tmp(1:len_trim(tmp))

        sendto = mod((rank + 1), num_procs)
        recvfrom = mod((rank + num_procs - 1), num_procs)

        call MPI_SEND(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD, ierr)
        call MPI_RECV(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status, ierr)

        print *, 'Process', rank, ': Process', recvfrom, ' said:', inbuf

        call MPI_FINALIZE(ierr)

    end program phello2
    ````

=== "Fortran 2008"
    ````f90 linenums="1" title="phello2.f90"
    program phello2

        implicit none
        use mpi_f08
        integer, parameter :: BUFMAX=81
        character(len=BUFMAX) :: outbuf, inbuf, tmp
        integer :: rank, num_procs
        integer :: sendto, recvfrom
        type(MPI_Status) :: status

        call MPI_Init()
        call MPI_Comm_rank(MPI_COMM_WORLD, rank)
        call MPI_Comm_size(MPI_COMM_WORLD, num_procs)

        outbuf = 'Hello, world! from process '
        write(tmp,'(i2)') rank
        outbuf = outbuf(1:len_trim(outbuf)) // tmp(1:len_trim(tmp))
        write(tmp,'(i2)') num_procs
        outbuf = outbuf(1:len_trim(outbuf)) // ' of ' // tmp(1:len_trim(tmp))

        sendto = mod((rank + 1), num_procs)
        recvfrom = mod((rank + num_procs - 1), num_procs)

        call MPI_Send(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD)
        call MPI_Recv(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status)

        print *, 'Process', rank, ': Process', recvfrom, ' said:', inbuf

        call MPI_Finalize()

    end program phello2
    ````

=== "Python (mpi4py)"
    ````python linenums="1" title="phello2.py"
    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    outbuf = "Hello, world! from process %d of %d" % (rank, size)

    sendto = (rank + 1) % size;
    recvfrom = (rank + size - 1) % size;

    comm.send(outbuf, dest=sendto, tag=0)
    inbuf = comm.recv(source=recvfrom, tag=0)

    print('[P_%d] process %d said: "%s"]' % (rank, recvfrom, inbuf))
    ````

Compilez ce programme et faites-le exécuter avec 2, 4 et 8 processus. Le fonctionnement semble approprié, mais il y a cependant un problème caché. En effet, la norme MPI n'offre aucune garantie que `MPI_Send` retournera avant que le message ait été livré. Dans la plupart des implémentations, les données sont mises en mémoire temporaire par `MPI_Send` et retournent sans attendre d'être livrées. Par contre, si la mémoire tampon n'était pas utilisée, notre code bloquerait. Chaque processus appellerait `MPI_Send` et attendrait que le processus voisin appelle `MPI_Recv`. Puisque le processus voisin serait aussi en attente d'une réponse de `MPI_Send`, tous les processus seraient indéfiniment en attente. Les bibliothèques des systèmes de Calcul Canada utilisent les *buffers* puisque notre code n'a pas bloqué; ce modèle de conception n'est toutefois pas fiable. Sans mémoire tampon offerte par la bibliothèque, le programme pourrait faire défaut, et malgré la mémoire tampon, un appel pourrait être bloqué si celle-ci est saturée.

```bash
mpicc -Wall phello2.c -o phello2
mpirun -np 4 ./phello2
```
```text
[P_0] process 3 said: "Hello, world! from process 3 of 4"]
[P_1] process 0 said: "Hello, world! from process 0 of 4"]
[P_2] process 1 said: "Hello, world! from process 1 of 4"]
[P_3] process 2 said: "Hello, world! from process 2 of 4"]
```

### Éviter les impasses

Dans la norme MPI, les appels `MPI_Send` et `MPI_Recv` sont des appels bloquants. `MPI_Send` ne retourne pas tant qu'il n'est pas sécuritaire pour le module qui appelle de modifier le contenu de la mémoire tampon. De même, `MPI_Recv` ne retourne pas tant que tout le contenu du message ne se trouve pas dans la mémoire tampon.

Le message est reçu, que la bibliothèque MPI offre ou non l’accès à une mémoire tampon. À la réception des données, le contenu du message est placé dans la mémoire tampon identifiée par l’appel et ce dernier est bloqué jusqu’à ce que `MPI_Recv` retourne. Par contre, `MPI_Send` n’a pas besoin d’être bloqué si la bibliothèque offre une mémoire tampon; dès que les données sont copiées de leur lieu d’origine, ce dernier peut être modifié et l’appel peut retourner. Ceci explique pourquoi notre exemple ne mène pas à une impasse malgré le fait que chacun des processus appelle `MPI_Send` en premier. Puisque la norme MPI ne requiert pas l'usage de la mémoire tampon et que notre code en dépend, nous considérons le programme comme étant à risque d'une impasse.

Un programme qui ne serait pas à risque en serait un dont le bon fonctionnement ne requiert pas l’usage d’une mémoire tampon, comme illustré ici :

#### Interblocage
```c
...
    if (rank == 0)
    {
        MPI_Recv(from 1);
        MPI_Send(to 1);
    }
    else if (rank == 1)
    {
        MPI_Recv(from 0);
        MPI_Send(to 0);
    }
...
```
Dans les deux cas, l'appel de réception est lancé avant l'appel d'envoi correspondant : il y a ainsi interblocage causé par `MPI_Recv`.

#### Situation à risque
```c
...
    if (rank == 0)
    {
        MPI_Send(to 1);
        MPI_Recv(from 1);
    }
    else if (rank == 1)
    {
        MPI_Send(to 0);
        MPI_Recv(from 0);
    }
...
```
Dans cet exemple, le programme pourrait fonctionner adéquatement si la bibliothèque permet l'usage d'une mémoire tampon. Si ce n'est pas le cas, ou si le contenu des messages dépasse la capacité de la mémoire tampon, `MPI_Send` fera bloquer le code, créant ainsi une impasse. L'exemple suivant présente une solution.

#### Code fiable
```c
...
    if (rank == 0)
    {
        MPI_Send(to 1);
        MPI_Recv(from 1);
    }
    else if (rank == 1)
    {
        MPI_Recv(from 0);
        MPI_Send(to 0);
    }
...
```
L’envoi est ici couplé avec la réception, sans usage d'une mémoire tampon. Le processus pourrait être arrêté momentanément en attente de l’appel correspondant, mais il n’y aura pas interblocage.

Comment peut-on s’assurer que notre code est correct? Une solution commode est d'utiliser des couples pair-impair et de procéder en deux temps. Dans notre exemple, la communication se fait séquentiellement d'un incrément vers la droite; notre code devrait donc être juste si tous les processus pairs exécutent l'envoi suivi de la réception et que tous les processus impairs exécutent la réception suivie de l'envoi. Les couples envoi-réception sont bien définis et la possibilité d'interblocage est éliminée.

=== "C"
    ````c linenums="1" title="phello3.c"
    #include <stdio.h>
    #include <mpi.h>

    #define BUFMAX 81

    int main(int argc, char *argv[])
    {
        char outbuf[BUFMAX], inbuf[BUFMAX];
        int rank, size;
        int sendto, recvfrom;
        MPI_Status status;


        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);

        sprintf(outbuf, "Hello, world! from process %d of %d", rank, size);

        sendto = (rank + 1) % size;
        recvfrom = ((rank + size) - 1) % size;

        if (!(rank % 2))
        {
            MPI_Send(outbuf, BUFMAX, MPI_CHAR, sendto, 0, MPI_COMM_WORLD);
            MPI_Recv(inbuf, BUFMAX, MPI_CHAR, recvfrom, 0, MPI_COMM_WORLD, &status);
        }
        else
        {
            MPI_Recv(inbuf, BUFMAX, MPI_CHAR, recvfrom, 0, MPI_COMM_WORLD, &status);
            MPI_Send(outbuf, BUFMAX, MPI_CHAR, sendto, 0, MPI_COMM_WORLD);
        }

        printf("[P_%d] process %d said: \"%s\"]\n", rank, recvfrom, inbuf);

        MPI_Finalize();

        return(0);
    }
    ````

=== "Boost (C++)"
    ````cpp linenums="1" title="phello3.cpp"
    #include <iostream>
    #include <string>
    #include <boost/mpi.hpp>

    using namespace std;
    using namespace boost;

    int main(int argc, char *argv[])
    {
        mpi::environment env(argc, argv);
        mpi::communicator world;
        int rank = world.rank();
        int size = world.size();

        string outmessage = "Hello, world! from process " + to_string(rank) + " of " + to_string(size);
        string inmessage;
        int sendto = (rank + 1) % size;
        int recvfrom = (rank + size - 1) % size;

        cout << outmessage << endl;

        if (!(rank % 2)) {
            world.send(sendto,0,outmessage);
            world.recv(recvfrom,0,inmessage);
        }
        else {
            world.recv(recvfrom,0,inmessage);
            world.send(sendto,0,outmessage);
        }

        cout << "[P_" << rank << "] process " << recvfrom << " said: \"" << inmessage << "\"" << endl;
        return 0;
    }
    ````

=== "Fortran"
    ````f90 linenums="1" title="phello3.f90"
    program phello3


        implicit none
        use mpi

        integer, parameter :: BUFMAX=81
        character(len=BUFMAX) :: outbuf, inbuf, tmp
        integer :: rank, num_procs, ierr
        integer :: sendto, recvfrom
        integer :: status(MPI_STATUS_SIZE)

        call MPI_INIT(ierr)
        call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)
        call MPI_COMM_SIZE(MPI_COMM_WORLD, num_procs, ierr)

        outbuf = 'Hello, world! from process '
        write(tmp,'(i2)') rank
        outbuf = outbuf(1:len_trim(outbuf)) // tmp(1:len_trim(tmp))
        write(tmp,'(i2)') num_procs
        outbuf = outbuf(1:len_trim(outbuf)) // ' of ' // tmp(1:len_trim(tmp))

        sendto = mod((rank + 1), num_procs)
        recvfrom = mod(((rank + num_procs) - 1), num_procs)

        if (MOD(rank,2) == 0) then
            call MPI_SEND(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD, ierr)
            call MPI_RECV(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status, ierr)
        else
            call MPI_RECV(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status, ierr)
            call MPI_SEND(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD, ierr)
        endif

        print *, 'Process', rank, ': Process', recvfrom, ' said:', inbuf

        call MPI_FINALIZE(ierr)

    end program phello3
    ````

=== "Fortran 2008"
    ````f90 linenums="1" title="phello3.f90"
    program phello3


        implicit none
        use mpi_f08

        integer, parameter :: BUFMAX=81
        character(len=BUFMAX) :: outbuf, inbuf, tmp
        integer :: rank, num_procs
        integer :: sendto, recvfrom
        type(MPI_Status) :: status

        call MPI_Init()
        call MPI_Comm_rank(MPI_COMM_WORLD, rank)
        call MPI_Comm_size(MPI_COMM_WORLD, num_procs)

        outbuf = 'Hello, world! from process '
        write(tmp,'(i2)') rank
        outbuf = outbuf(1:len_trim(outbuf)) // tmp(1:len_trim(tmp))
        write(tmp,'(i2)') num_procs
        outbuf = outbuf(1:len_trim(outbuf)) // ' of ' // tmp(1:len_trim(tmp))

        sendto = mod((rank + 1), num_procs)
        recvfrom = mod(((rank + num_procs) - 1), num_procs)

        if (MOD(rank,2) == 0) then
            call MPI_Send(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD)
            call MPI_Recv(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status)
        else
            call MPI_RECV(inbuf, BUFMAX, MPI_CHARACTER, recvfrom, 0, MPI_COMM_WORLD, status)
            call MPI_SEND(outbuf, BUFMAX, MPI_CHARACTER, sendto, 0, MPI_COMM_WORLD)
        endif

        print *, 'Process', rank, ': Process', recvfrom, ' said:', inbuf

        call MPI_Finalize()

    end program phello3
    ````

=== "Python (mpi4py)"
    ````python linenums="1" title="phello3.py"
    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    outbuf = "Hello, world! from process %d of %d" % (rank, size)

    sendto = (rank + 1) % size;
    recvfrom = ((rank + size) - 1) % size;

    if rank % 2 == 0:
        comm.send(outbuf, dest=sendto, tag=0)
        inbuf = comm.recv(source=recvfrom, tag=0)
    else:
        inbuf = comm.recv(source=recvfrom, tag=0)
        comm.send(outbuf, dest=sendto, tag=0)

    print('[P_%d] process %d said: "%s"]' % (rank, recvfrom, inbuf))
    ````

À première vue, il semblerait qu'un nombre impair de processus puisse poser un problème. En effet, le processus pair 0 lance un envoi alors que l'autre processus pair N-1 tente de lancer une réception. Cependant, l'envoi fait par le processus 0 est correctement apparié à la réception lancée par le processus 1; puisque le processus impair 1 commence par une réception, la transaction sera sûrement complétée. Sur ce, le processus 0 reçoit le message du processus 1; il pourrait y avoir un certain délai (minime), mais il n'y a pas de risque d'interblocage.

```bash
mpicc -Wall phello3.c -o phello3
mpirun -np 16 ./phello3
```
```text
[P_1] process 0 said: "Hello, world! from process 0 of 16"]
[P_2] process 1 said: "Hello, world! from process 1 of 16"]
[P_5] process 4 said: "Hello, world! from process 4 of 16"]
[P_3] process 2 said: "Hello, world! from process 2 of 16"]
[P_9] process 8 said: "Hello, world! from process 8 of 16"]
[P_0] process 15 said: "Hello, world! from process 15 of 16"]
[P_12] process 11 said: "Hello, world! from process 11 of 16"]
[P_6] process 5 said: "Hello, world! from process 5 of 16"]
[P_13] process 12 said: "Hello, world! from process 12 of 16"]
[P_8] process 7 said: "Hello, world! from process 7 of 16"]
[P_7] process 6 said: "Hello, world! from process 6 of 16"]
[P_14] process 13 said: "Hello, world! from process 13 of 16"]
[P_10] process 9 said: "Hello, world! from process 9 of 16"]
[P_4] process 3 said: "Hello, world! from process 3 of 16"]
[P_15] process 14 said: "Hello, world! from process 14 of 16"]
[P_11] process 10 said: "Hello, world! from process 10 of 16"]
```
Plusieurs modèles sont décrits dans la page Web [Introduction and Overview](http://www.mcs.anl.gov/research/projects/mpi/mpi-standard/mpi-report-1.1/node64.htm#Node64). Nous vous recommandons d'utiliser la fonction de communication qui s'applique à votre situation, plutôt que de la créer par vous-même.

## Enveloppes de compilateurs

Les paquets des bibliothèques MPI offrent généralement des enveloppes (*wrappers*) pour les compilateurs. Ce ne sont pas des compilateurs, mais ces enveloppes appellent d'autres compilateurs tout en s'assurant que le compilateur reçoive les indicateurs spécifiques à MPI.

Voici une liste partielle :

*   `mpicc` pour C
*   `mpicxx` pour C++
*   `mpifort` et/ou `mpif77` et/ou `mpif90` pour Fortran

Avec Open MPI, ces enveloppes ont l'option `--showme` qui imprime le nom du compilateur qui sera appelé et les options qui y seront ajoutées.

!!! note "Remarque"
    Notre pile logicielle contient plusieurs modules du même paquet Open MPI (par exemple `openmpi/4.0.3`) qui ont été construits avec des compilateurs différents et qui prennent en charge ou non CUDA. Les enveloppes de compilateurs MPI utiliseront toujours le compilateur et la version du compilateur que vous avez chargés avec la commande `module load`.

Par exemple, si vous avez chargé les modules `intel/2020.1.217` et `openmpi/4.0.3` :
````bash title="Exemple de mpicc --showme"
mpicc -showme
````
````text
icc -I/cvmfs/.../intel2020/openmpi/4.0.3/include -L/cvmfs/.../intel2020/openmpi/4.0.3/lib -lmpi
````

Si vous avez chargé les modules `gcc/9.3.0` et `openmpi/4.0.3` :
````bash title="Exemple de mpicc --showme"
mpicc -showme
````
````text
gcc -I/.../gcc9/openmpi/4.0.3/include -L/cvmfs/.../gcc9/openmpi/4.0.3/lib -lmpi
````

## Autres considérations
Nous avons abordé la conception et la syntaxe de programmes MPI; il y a cependant beaucoup d'autres éléments à considérer dans le développement d'applications parallèles robustes avec MPI. Sans être exhaustive, la liste suivante en donne un aperçu.
*   [variantes de `MPI_Send`/`MPI_Recv`](http://www.mcs.anl.gov/research/projects/mpi/mpi-standard/mpi-report-1.1/node40.htm#Node40)
*   [communication collective](http://www.mcs.anl.gov/research/projects/mpi/mpi-standard/mpi-report-1.1/node64.htm)
*   [communicateurs](http://mpitutorial.com/tutorials/introduction-to-groups-and-communicators/) et topologies
*   [communication unilatérale](http://wgropp.cs.illinois.edu/courses/cs598-s16/lectures/lecture34.pdf) et fonctionnalités de MPI-2
*   [types de données dérivés](http://www.mcs.anl.gov/research/projects/mpi/mpi-standard/mpi-report-1.1/node54.htm#Node54)
*   performance
*   débogage
*   [tutoriel Boost MPI (en français)](https://drive.google.com/file/d/0B4bveu7i2jOyeVR5VGlxV1g1MDQ/view)

## Lectures recommandées
*   GROPP, William, Ewing LUSK et Anthony SKJELLUM. *Using MPI: Portable Parallel Programming with the Message-Passing Interface*, 2e éd, MIT Press, 1999.
    *   information complète sur les interfaces avec Fortran, C et C++
*   PACHECO, Peter S., *Parallel Programming with MPI*, Morgan Kaufmann, 1997.
    *   tutoriel avec langage C
*   BARNEY, Blaise [*Message Passing Interface (MPI)*](https://computing.llnl.gov/tutorials/mpi/), Lawrence Livermore National Labs.
*   KENDALL, Wes, et autres. [mpitutorial.com](http://mpitutorial.com/tutorials/)
*   Institut du développement et des ressources en informatique scientifique, [*Formation "MPI"*](http://www.idris.fr/formations/mpi/) (en français).