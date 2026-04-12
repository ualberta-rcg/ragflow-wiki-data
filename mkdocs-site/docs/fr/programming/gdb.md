---
title: "GDB/fr"
slug: "gdb"
lang: "fr"

source_wiki_title: "GDB/fr"
source_hash: "57fb6a872a699b0f381fdd7a14625dad"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:20:07.791956+00:00"

tags:
  []

keywords:
  - "firefox"
  - "structures de la STL"
  - "fichier core"
  - "backtrace"
  - "libxul.so"
  - "XRE_main"
  - "pile d'appels"
  - "debugging session"
  - "core-file"
  - "points d'arrêt"
  - "gdb"
  - "GDB"
  - "logiciel"
  - "débogueur"
  - "commandes"
  - "débogage"
  - "xulrunner"
  - "program.cpp"
  - "processus existant"
  - "erreur de segmentation"
  - "Segmentation fault"
  - "signal 11"

questions:
  - "Quel est le rôle principal du débogueur GDB et pour quel type de problème est-il recommandé d'utiliser Valgrind à la place ?"
  - "Quelle option de compilation doit-on utiliser pour que GDB puisse décoder les symboles et fournir des informations précises sur la source du bogue ?"
  - "Comment doit-on procéder pour analyser une erreur de segmentation à l'aide d'un fichier \"core\" lorsque le bogue survient tardivement dans l'exécution du programme ?"
  - "Comment peut-on trouver le numéro d'un processus en cours d'exécution afin de le déboguer ?"
  - "Quelle est la commande à utiliser pour attacher le débogueur GDB à un processus existant ?"
  - "Quelle commande permet d'afficher la pile d'appels en cours une fois le débogueur attaché ?"
  - "What specific signal and error caused the program to terminate?"
  - "On which line of code and within which function did the crash occur?"
  - "What missing debug information packages does the debugger suggest installing?"
  - "What specific application and process ID are being debugged in this session?"
  - "Which sequence of function calls is shown in the provided stack trace snippet?"
  - "What action does the user confirm at the end of the debugging prompt?"
  - "Quelles sont les principales commandes de GDB permettant de contrôler l'exécution d'un programme et d'inspecter ses variables ?"
  - "Comment peut-on configurer GDB pour afficher correctement le contenu des structures de la librairie standard du C++ (STL) ?"
  - "Quelles ressources supplémentaires sont recommandées dans le texte pour approfondir l'apprentissage et l'utilisation de GDB ?"
  - "Quelles sont les principales commandes de GDB permettant de contrôler l'exécution d'un programme et d'inspecter ses variables ?"
  - "Comment peut-on configurer GDB pour afficher correctement le contenu des structures de la librairie standard du C++ (STL) ?"
  - "Quelles ressources supplémentaires sont recommandées dans le texte pour approfondir l'apprentissage et l'utilisation de GDB ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[GDB](https://www.gnu.org/software/gdb/) (pour *GNU Project Debugger*) est un débogueur pour dépister les problèmes dans les logiciels.

## Description
Avec un débogueur, il est possible de trouver rapidement la cause d'un problème dans un logiciel.
Le cas d'utilisation typique est de trouver les [erreurs de segmentation](https://fr.wikipedia.org/wiki/Erreur_de_segmentation).
Si vous désirez trouver un problème de mémoire (par exemple, une [fuite de mémoire](https://fr.wikipedia.org/wiki/Fuite_de_m%C3%A9moire)), il est recommandé d'utiliser [Valgrind](../software/valgrind.md).

## Cas d'utilisation
### Trouver la cause d'une erreur de segmentation directement avec le débogueur
Dans cette section, le programme suivant est utilisé :

```cpp title="program.cpp"
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char**argv) {
	
	vector<int> numbers;

	int iterator = 1000;

	while(iterator --) {
		numbers.push_back(iterator);
	}

	cout << numbers[1000000] << endl;

	return 0;
}
```

Ce programme génère une erreur de segmentation lorsqu'on l'exécute.

```bash
g++ -g program.cpp -o program
```

```bash
./program
```

```text
Segmentation fault (core dumped)
```

On peut alors l'exécuter à l'intérieur du débogueur.

!!! tip "Conseil de compilation"
    On a compilé avec l'option `-g` pour permettre au débogueur de décoder les symboles et fournir davantage d'information sur la source du bogue.

On exécute l'application à l'intérieur du débogueur comme suit :

```bash
gdb ./program
(gdb) run
Starting program: /home/seb/program ./program

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400c17 in main (argc=2, argv=0x7fffffffda88) at program.cpp:15
15		cout << numbers[1000000] << endl;
Missing separate debuginfos, use: debuginfo-install glibc-2.16-31.fc18.x86_64 libgcc-4.7.2-8.fc18.x86_64 libstdc++-4.7.2-8.fc18.x86_64

(gdb) bt
#0  0x0000000000400c17 in main (argc=2, argv=0x7fffffffda88) at program.cpp:15
```

Ici, l'erreur est causée par la ligne 15. Le code accède à l'indice 1000000, mais le tableau contient seulement 1000 éléments.

### Trouver la cause d'une erreur de segmentation avec un fichier `core`
Dans cet exemple, on utilise le programme de la section précédente, mais sans utiliser le débogueur directement. Ceci est utile pour un bogue qui se produit longtemps après le début de l'exécution du programme.

Afin de trouver la cause de l'erreur de segmentation, il faut générer un fichier `core`. Pour ce faire, il faut activer la création de tels fichiers.

```bash
ulimit -c unlimited
```

En exécutant à nouveau le même programme, un fichier `core` sera écrit.

```bash
./program
```

```text
Segmentation fault (core dumped)
```

```bash
file core.18158
```

```text
core.18158: ELF 64-bit LSB core file x86-64, version 1 (SYSV), SVR4-style, from './program'
```

En utilisant l'exécutable `program` et le fichier `core`, il est possible de tracer l'exécution jusqu'à l'erreur.

```bash
gdb -q ./program
Reading symbols from /home/seb/program...done.

(gdb) core-file core.18246
[New LWP 18246]
Core was generated by './program'.
Program terminated with signal 11, Segmentation fault.
#0  0x0000000000400c17 in main (argc=1, argv=0x7fff2315c848) at
program.cpp:15
15              cout << numbers[1000000] << endl;
Missing separate debuginfos, use: debuginfo-install
glibc-2.16-31.fc18.x86_64 libgcc-4.7.2-8.fc18.x86_64
libstdc++-4.7.2-8.fc18.x86_64

(gdb) bt
#0  0x0000000000400c17 in main (argc=1, argv=0x7fff2315c848) at
program.cpp:15
```

On obtient alors le même résultat qu'en ayant exécuté le code à l'intérieur du débogueur.

### Attacher le débogueur à un processus existant
Il est possible de déboguer un processus existant, par exemple une tâche qui s'exécute sur un nœud de calcul. Pour ce faire, il faut d'abord trouver le numéro du processus.

```bash
ps aux | grep firefox | grep -v grep
```

```text
seb      12691  6.4  7.5 1539672 282656 ?      Sl   08:53   6:48 /usr/lib64/firefox/firefox http://www.google.ca/
```

Ensuite, il est possible d'attacher le débogueur directement.

```bash
gdb attach 12691
```

Après avoir fait cette commande, beaucoup d'information sera imprimée.

Plusieurs commandes de débogage sont disponibles. L'une des commandes utiles est `backtrace`, ou `bt`.
Cette commande permet d'afficher la pile d'appels en cours.

```bash
(gdb) bt
#0  0x00000033646e99ad in poll () from /lib64/libc.so.6
#1  0x0000003db86849f3 in PollWrapper(_GPollFD*, unsigned int, int) () from /usr/lib64/firefox/xulrunner/libxul.so
#2  0x0000003366e47d24 in g_main_context_iterate.isra.24 () from /lib64/libglib-2.0.so.0
#3  0x0000003366e47e44 in g_main_context_iteration () from /lib64/libglib-2.0.so.0
#4  0x0000003db86849a2 in nsAppShell::ProcessNextNativeEvent(bool) () from /usr/lib64/firefox/xulrunner/libxul.so
#5  0x0000003db869a7d1 in nsBaseAppShell::DoProcessNextNativeEvent(bool, unsigned int) () from /usr/lib64/firefox/xulrunner/libxul.so
#6  0x0000003db869a8ea in nsBaseAppShell::OnProcessNextEvent(nsIThreadInternal*, bool, unsigned int) () from /usr/lib64/firefox/xulrunner/libxul.so
#7  0x0000003db89810c2 in nsThread::ProcessNextEvent(bool, bool*) () from /usr/lib64/firefox/xulrunner/libxul.so
#8  0x0000003db89563eb in NS_ProcessNextEvent(nsIThread*, bool) () from /usr/lib64/firefox/xulrunner/libxul.so
#9  0x0000003db873056f in mozilla::ipc::MessagePump::Run(base::MessagePump::Delegate*) () from /usr/lib64/firefox/xulrunner/libxul.so
#10 0x0000003db89a4ab7 in MessageLoop::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#11 0x0000003db869a1b3 in nsBaseAppShell::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#12 0x0000003db857d92d in nsAppStartup::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#13 0x0000003db7d18f4a in XREMain::XRE_mainRun() () from /usr/lib64/firefox/xulrunner/libxul.so
#14 0x0000003db7d1b007 in XREMain::XRE_main(int, char**, nsXREAppData const*) () from /usr/lib64/firefox/xulrunner/libxul.so
#15 0x0000003db7d1b259 in XRE_main () from /usr/lib64/firefox/xulrunner/libxul.so
#16 0x0000000000402c23 in do_main(int, char**, nsIFile*) ()
#17 0x0000000000402403 in main ()
(gdb) quit
A debugging session is active.

Inferior 1 [process 12691] will be detached.

Quit anyway? (y or n) y
Detaching from program: /usr/lib64/firefox/firefox, process 12691
```

## Utilisation plus poussée
Dans les sections précédentes, nous avons utilisé les commandes `run` et `backtrace`. Plusieurs autres commandes sont disponibles pour déboguer en mode interactif, soit en contrôlant l'exécution du programme. Il est par exemple possible d'établir des points d'arrêt sur des fonctions ou des lignes de code ou encore lors d'une modification d'une variable. Lorsque l'exécution est interrompue, il est possible d'analyser l'état du programme en affichant la valeur de certaines variables. Le tableau qui suit présente les principales commandes.

*Principales commandes de GDB*

| Commande            | Raccourci | Argument                 | Description                                                  |
| :------------------ | :-------- | :----------------------- | :----------------------------------------------------------- |
| `run` / `kill`      | `r` / `k` | -                        | Démarre/arrête l'exécution du programme                      |
| `where` / `backtrace` | `bt`      | -                        | Affiche la pile d'appels                                     |
| `break`             | `b`       | `src.c:numéro_de_ligne` ou `fonction` | Crée un point d'arrêt à la ligne de code ou à la fonction spécifiée |
| `watch`             | -         | `nom_de_variable`        | Arrête l'exécution lorsque la variable est modifiée          |
| `continue`          | `c`       | -                        | Continue l'exécution après un point d'arrêt                  |
| `step`              | `s`       | -                        | Exécute l'opération suivante                                 |
| `print`             | `p`       | `nom_de_variable`        | Affiche le contenu d'une variable                            |
| `list`              | `l`       | `src.c:numéro`           | Affiche la ligne de code spécifiée                           |

### Afficher les structures de la STL
Par défaut, GDB n'affiche pas très bien le contenu des structures de la bibliothèque standard du C++ (STL). Plusieurs solutions sont documentées [ici](https://sourceware.org/gdb/wiki/STLSupport). La solution la plus simple est probablement [celle-ci](http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF), qui consiste à copier [ce fichier](http://www.yolinux.com/TUTORIALS/src/dbinit_stl_views-1.03.txt) dans votre répertoire personnel, sous le nom `~/.gdbinit`.

## Ressources complémentaires
* [Site web GDB](http://www.sourceware.org/gdb/)
* [Tutoriel GDB](http://oucsace.cs.ohiou.edu/~bhumphre/gdb.html)
* [Document du TACC sur le débogage et le profilage](http://goo.gl/rLPvR0)