---
title: "Perl/fr"
slug: "perl"
lang: "fr"

source_wiki_title: "Perl/fr"
source_hash: "f7d0853eaf65785edf7c6e39fe131a00"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:55:01.823880+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Voici le contenu converti en français québécois :

## Description
[Perl](http://www.perl.org) est un langage de programmation logiciel libre et interprété qui possède plusieurs paquets développés au fil de plus de 25 ans d'existence. De par sa conception, Perl offre plusieurs façons de réaliser la même tâche. Selon [cet article](http://www.cio.com/article/175450/You_Used_Perl_to_Write_WHAT_), ses forces sont la manipulation des chaînes de caractères, l'accès aux bases de données ainsi que sa portabilité. Ses faiblesses sont sa faible performance et la facilité avec laquelle on peut écrire du code illisible. Plusieurs programmeurs ont adopté ce langage et produisent du code très compact, mais souvent quasi illisible.

## Charger l'interpréteur
Perl est installé par défaut sur les serveurs de Calcul Canada. Visualisez les versions disponibles avec :

```bash
module spider perl
```

et chargez une version comme suit :

```bash
module load perl/5.36.1
```

## Installer les paquets
Plusieurs paquets Perl peuvent être installés via le site [Comprehensive Perl Archive Network](http://www.cpan.org/) avec l'outil `cpan`. Assurez-vous d'abord que l'initialisation est correcte afin de pouvoir installer les paquets dans votre dossier personnel (`home`).

### Configuration initiale pour l'installation d'un module
Lors de la première exécution de la commande `cpan`, vous devez décider si la configuration doit s'effectuer automatiquement. Répondez « oui ».

```bash
cpan
# ... (plusieurs lignes de sortie)

Voulez-vous que je configure le plus possible automatiquement? [oui]
# ... (plusieurs lignes de sortie)
Quelle approche voulez-vous? (Choisissez 'local::lib', 'sudo' ou 'manual')
 [local::lib]
# ... (plusieurs lignes de sortie)
```

L'utilitaire `cpan` demandera si vous voulez ajouter certaines variables d'environnement au fichier `.bashrc`; acceptez l'ajout. Saisissez ensuite la commande `quit` via l'interface pour quitter `cpan`. Avant d'installer un module Perl, rechargez votre environnement de shell pour activer les nouveaux paramètres.

### Installation de paquets
Une fois la configuration initiale complétée, vous pouvez installer n'importe lequel des plus de 25 000 paquets offerts par CPAN, par exemple :

```bash
cpan
# Terminal does not support AddHistory.

# cpan shell -- CPAN exploration and modules installation (v2.11)
# Enter 'h' for help.
cpan[1]> install Chess
# ...
# Running install for module 'Chess'
# Fetching with LWP:
# http://www.cpan.org/authors/id/B/BJ/BJR/Chess-0.6.2.tar.gz
# Fetching with LWP:
# http://www.cpan.org/authors/id/B/BJ/BJR/CHECKSUMS
# Checksum for /home/stubbsda/.cpan/sources/authors/id/B/BJ/BJR/Chess-0.6.2.tar.gz ok
# Scanning cache /home/stubbsda/.cpan/build for sizes
# ............................................................................DONE
# 'YAML' not installed, will not store persistent state
# Configuring B/BJ/BJR/Chess-0.6.2.tar.gz with Makefile.PL
# Checking if your kit is complete...
# Looks good
# ...
# Running make for B/BJ/BJR/Chess-0.6.2.tar.gz
# ...
# Running make test
# PERL_DL_NONLAZY=1 "/cvmfs/soft.computecanada.ca/nix/store/g8ds64pbnavscf7n754pjlx5cp1mkkv1-perl-5.22.2/bin/perl" "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness(0, 'blib/lib', 'blib/arch')" t/*.t
# t/bishop.t ......... ok
# t/board.t .......... ok
# t/checkmate.t ...... ok
# t/game.t ........... ok
# t/king.t ........... ok
# t/knight.t ......... ok
# t/movelist.t ....... ok
# t/movelistentry.t .. ok
# t/pawn.t ........... ok
# t/piece.t .......... ok
# t/queen.t .......... ok
# t/rook.t ........... ok
# t/stalemate.t ...... ok
# All tests successful.
# Files=13, Tests=311,  3 wallclock secs ( 0.14 usr  0.05 sys +  2.49 cusr  0.20 csys =  2.88 CPU)
# Result: PASS
# ...
# Installing /home/stubbsda/perl5/man/man3/Chess::Piece::Knight.3
# Installing /home/stubbsda/perl5/man/man3/Chess.3
# Installing /home/stubbsda/perl5/man/man3/Chess::Piece::Bishop.3
# Installing /home/stubbsda/perl5/man/man3/Chess::Board.3
# Appending installation info to /home/stubbsda/perl5/lib/perl5/x86_64-linux-thread-multi/perllocal.pod
#   BJR/Chess-0.6.2.tar.gz
#   /cvmfs/soft.computecanada.ca/nix/var/nix/profiles/16.09/bin/make install  -- OK
cpan[2]>