---
title: "Perl/fr"
slug: "perl"
lang: "fr"

source_wiki_title: "Perl/fr"
source_hash: "f7d0853eaf65785edf7c6e39fe131a00"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:23:32.327199+00:00"

tags:
  - software

keywords:
  - "CPAN"
  - "Tests=311"
  - "make install"
  - "installation info"
  - "All tests successful"
  - "t/game.t"
  - "Perl5"
  - "Files=13"
  - "Chess"
  - "installation de paquets"
  - "wallclock secs"
  - "langage de programmation"
  - "Perl"
  - "Calcul Canada"

questions:
  - "Quelles sont les principales forces et faiblesses du langage de programmation Perl selon le texte ?"
  - "Comment peut-on trouver et charger une version spécifique de l'interpréteur Perl sur les serveurs de Calcul Canada ?"
  - "Quelles sont les étapes de configuration initiale requises pour installer des paquets Perl dans son répertoire personnel à l'aide de l'outil CPAN ?"
  - "What specific Perl module version and associated components were successfully installed?"
  - "What is the directory path where the manual pages for the chess pieces were placed?"
  - "Which build tool and command were used to execute the installation process?"
  - "What specific domain or type of application is being evaluated by this test suite?"
  - "What was the final outcome of the test execution and how many total tests were run?"
  - "How much wallclock time and CPU resources were consumed during the testing process?"
  - "What specific Perl module version and associated components were successfully installed?"
  - "What is the directory path where the manual pages for the chess pieces were placed?"
  - "Which build tool and command were used to execute the installation process?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description
[Perl](http://www.perl.org) est un langage de programmation libre et interprété qui possède plusieurs paquets développés au fil de plus de 25 années d'existence. Selon [cet article](http://www.cio.com/article/175450/You_Used_Perl_to_Write_WHAT_), ses forces sont la manipulation des chaînes de caractères, l'accès aux bases de données ainsi que sa portabilité. Ses faiblesses sont sa faible performance et la facilité avec laquelle on peut écrire du code illisible. En effet, par conception, Perl offre plusieurs façons de réaliser la même tâche. Plusieurs programmeurs ont adopté ce langage et produisent du code très compact, mais souvent quasi illisible.

## Charger l'interpréteur
Perl est installé par défaut sur les serveurs de l'Alliance de recherche numérique du Canada (l'Alliance, anciennement Calcul Canada). Voyez les versions disponibles avec :

```bash
module spider perl
```

et chargez une version comme ceci :

```bash
module load perl/5.36.1
```

## Installer les paquets
Plusieurs paquets Perl peuvent être installés via le site [Comprehensive Perl Archive Network](http://www.cpan.org/) avec l'outil `cpan`.

!!! attention "Vérification initiale"
    Assurez-vous d'abord que l'initialisation est correcte afin de pouvoir installer les paquets dans votre *répertoire personnel* (*home*).

### Configuration initiale pour installer le module
Lors de la première exécution de la commande `cpan`, vous devez décider si la configuration doit se faire de façon automatique. Répondez `yes`.

```bash
cpan
```

```
...

Would you like me to configure as much as possible automatically? [yes]
...
What approach do you want?  (Choose 'local::lib', 'sudo' or 'manual')
 [local::lib]
...
```

L'utilitaire `cpan` demandera si vous voulez ajouter certaines variables d'environnement au fichier `.bashrc`; acceptez l'ajout. Entrez ensuite la commande `quit` via l'interface pour quitter `cpan`.

!!! attention "Redémarrage nécessaire"
    Avant d'installer un module Perl, redémarrez l'interpréteur pour activer les nouveaux paramètres.

### Installation de paquets
Lorsque la configuration initiale est terminée, vous pouvez installer n'importe lequel des 25 000 paquets et plus offerts par CPAN, par exemple :

```bash
cpan
```

```
Terminal does not support AddHistory.

cpan shell -- CPAN exploration and modules installation (v2.11)
Enter 'h' for help.

cpan[1]> install Chess
...
Running install for module 'Chess'
Fetching with LWP:
http://www.cpan.org/authors/id/B/BJ/BJR/Chess-0.6.2.tar.gz
Fetching with LWP:
http://www.cpan.org/authors/id/B/BJ/BJR/CHECKSUMS
Checksum for /home/stubbsda/.cpan/sources/authors/id/B/BJ/BJR/Chess-0.6.2.tar.gz ok
Scanning cache /home/stubbsda/.cpan/build for sizes
............................................................................DONE
'YAML' not installed, will not store persistent state
Configuring B/BJ/BJR/Chess-0.6.2.tar.gz with Makefile.PL
Checking if your kit is complete...
Looks good
...
Running make for B/BJ/BJR/Chess-0.6.2.tar.gz
...
Running make test
PERL_DL_NONLAZY=1 "/cvmfs/soft.computecanada.ca/nix/store/g8ds64pbnavscf7n754pjlx5cp1mkkv1-perl-5.22.2/bin/perl" "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness(0, 'blib/lib', 'blib/arch')" t/*.t
t/bishop.t ......... ok
t/board.t .......... ok
t/checkmate.t ...... ok
t/game.t ........... ok
t/king.t ........... ok
t/knight.t ......... ok
t/movelist.t ....... ok
t/movelistentry.t .. ok
t/pawn.t ........... ok
t/piece.t .......... ok
t/queen.t .......... ok
t/rook.t ........... ok
t/stalemate.t ...... ok
All tests successful.
Files=13, Tests=311,  3 wallclock secs ( 0.14 usr  0.05 sys +  2.49 cusr  0.20 csys =  2.88 CPU)
Result: PASS
...
Installing /home/stubbsda/perl5/man/man3/Chess::Piece::Knight.3
Installing /home/stubbsda/perl5/man/man3/Chess.3
Installing /home/stubbsda/perl5/man/man3/Chess::Piece::Bishop.3
Installing /home/stubbsda/perl5/man/man3/Chess::Board.3
Appending installation info to /home/stubbsda/perl5/lib/perl5/x86_64-linux-thread-multi/perllocal.pod
  BJR/Chess-0.6.2.tar.gz
  /cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin/make install  -- OK
cpan[2]>