---
title: "MRCC/fr"
slug: "mrcc"
lang: "fr"

source_wiki_title: "MRCC/fr"
source_hash: "e64ebcb1426adee55c594d80f8503d6c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:21:03.794713+00:00"

tags:
  - software
  - computationalchemistry

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

## Introduction

MRCC est une suite de programmes de chimie quantique fonctionnelle *ab initio* et de densité pour les calculs de structure électronique de haute précision, développée et maintenue par le groupe de recherche en chimie quantique du département de chimie physique et de science des matériaux de la TU Budapest. Ayant comme particularité l'utilisation d'outils de programmation automatisés, MRCC a permis le développement de routines de manipulation de tenseurs indépendantes du nombre d'indices des tenseurs correspondants, simplifiant ainsi considérablement la mise en œuvre générale des méthodes de chimie quantique. En appliquant les outils automatisés, plusieurs modèles et techniques de chimie quantique d'une grande complexité ont été mis en œuvre jusqu'à présent, notamment des méthodes arbitraires de cluster couplé (CC) et d'interaction de configuration (CI) à référence unique, des approches CC multiréférence, les énergies dérivées CC et CI, et les approches CC de fonctions de réponse et de perturbation arbitraires.

## Limites de la licence

L'Alliance a signé un accord de licence avec le professeur Mihaly Kallay, qui représente les développeurs du logiciel MRCC.

Afin d'utiliser la version actuellement installée sur nos systèmes, vous devez accepter certaines conditions. Écrivez au soutien technique en joignant la déclaration suivante&nbsp;:

1.  Mon utilisation de MRCC se limitera à la recherche universitaire.
2.  Je ne copierai pas le logiciel MRCC ni le rendrai disponible à une autre personne.
3.  Je citerai correctement les articles originaux liés au MRCC et à l'Alliance dans mes publications. Pour plus de détails, [voir cette page](https://www.mrcc.hu/index.php/citation).
4.  Je comprends que l'accord d'utilisation de la suite MRCC peut être résilié par l'une des parties&nbsp;: les développeurs du MRCC ou l'Alliance.
5.  J'informerai l'Alliance de tout changement dans la déclaration ci-dessus.

## Module

La version MRCC du 2023-08-28 est disponible sur toutes les grappes en chargeant un module.

```bash
module load intel/2023.2.1  openmpi/4.1.5 mrcc/20230828
```

Le module prend en charge OpenMP et MPI. Une fois le module chargé, vous pouvez accéder à la base et à tous les binaires listés ci-dessous.

```bash
[ ~]$ module load intel/2023.2.1  openmpi/4.1.5 mrcc/20230828
[ ~]$ ls $EBROOTMRCC/bin/
ccsd      cis                      dmrcc      drpa      goldstone  minp      mrcc      mulli   ovirt  qmmod  scf_mpi  xmrcc
ccsd_mpi  dirac_mointegral_export  dmrcc_mpi  drpa_mpi  integ      mp2f12    mrcc_mpi  orbloc  prop   scf    uccsd    xmrcc_mpi
```

## Exemples de scripts

(en préparation)

## Comment citer

Comme indiqué dans la licence, vous êtes invités à citer les articles originaux dans vos publications. Pour plus d'informations, [voir cette page](https://www.mrcc.hu/index.php/citation).

## Documentation

*   [documentation officielle MRCC](https://www.mrcc.hu/index.php/documentation)
*   [forum MRCC](https://www.mrcc.hu/index.php/forum)