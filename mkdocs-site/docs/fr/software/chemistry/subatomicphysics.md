---
title: "SubatomicPhysics/fr"
slug: "subatomicphysics"
lang: "fr"

source_wiki_title: "SubatomicPhysics/fr"
source_hash: "d8a38ab47174feb0b0b7b73ad7dd1c83"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:42:55.898717+00:00"

tags:
  []

keywords:
  - "instancier des images"
  - "CVMFS"
  - "dépôt CVMFS"
  - "physique subatomique"
  - "conteneur"
  - "atlas-grid-centos7"
  - "DUCC"
  - "image Singularity"
  - "conteneurs Singularity"
  - "ATLAS"
  - "exécutable Singularity"
  - "physique des hautes énergies"
  - "Calcul Canada"
  - "plugiciel Graph Driver"

questions:
  - "Pourquoi la configuration standard CCenv de Calcul Canada peut-elle créer des conflits avec les dépôts CVMFS utilisés en physique subatomique ?"
  - "Quelle est l'approche recommandée pour pallier l'absence du paquet HEP_OSLibs sur les nœuds de calcul ?"
  - "Quels sont les deux principaux dépôts distribués via CVMFS pour accéder aux images de conteneurs en physique des hautes énergies ?"
  - "Où les images Singularity sont-elles stockées par défaut sur le système ?"
  - "Pourquoi la méthode pour invoquer l'exécutable Singularity diffère-t-elle selon les sites de Calcul Canada (comme Cedar, Graham et Niagara) ?"
  - "Quelles sont les deux approches possibles pour invoquer un conteneur à partir d'un dépôt CVMFS et comment influencent-elles la performance ?"
  - "Quel plugiciel est utilisé pour instancier des images directement à partir de CVMFS ?"
  - "Où peut-on consulter la documentation supplémentaire concernant le projet DUCC ?"
  - "Comment peut-on ajouter une image additionnelle à la liste des images publiées automatiquement ?"
  - "Où les images Singularity sont-elles stockées par défaut sur le système ?"
  - "Pourquoi la méthode pour invoquer l'exécutable Singularity diffère-t-elle selon les sites de Calcul Canada (comme Cedar, Graham et Niagara) ?"
  - "Quelles sont les deux approches possibles pour invoquer un conteneur à partir d'un dépôt CVMFS et comment influencent-elles la performance ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Logiciels de physique subatomique et de physique des hautes énergies

Cette page est préparée par l’équipe nationale de physique subatomique. Sa dernière mise à jour est en date de juillet 2021.

Voyez aussi la page [Astronomy and High Energy Physics Interactive Analysis Facility](astronomy-and-high-energy-physics-interactive-analysis-facility.md).

La plupart des groupes de physique subatomique expérimentale utilisent les dépôts CVMFS du CERN, du consortium Open Science Grid et des dépôts spécifiques pour chacune des expériences.

La configuration `CCenv` qui est à la disposition des utilisateurs réguliers peut créer des conflits avec certaines configurations de ces dépôts parce que l'accès se fait avec Nix et EasyBuild à partir du dépôt CVMFS `soft.computecanada.ca` de Calcul Canada plutôt que par le logiciel installé sur le système d'exploitation de base des nœuds de calcul.

Les utilisateurs ATLAS trouveront de l'information utile dans les pages du twiki TRIUMF.

!!! note "Note importante"
    Utilisez les configurations recommandées pour Tier-3 plutôt que de réinventer les techniques décrites plus bas.

*   [https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s)
*   [https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers)

Plusieurs configurations présupposent que les nœuds de base sont configurés avec le paquet [HEP_OSLibs](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/master/README.md), ce qui **n'est pas le cas** de nos nœuds de calcul. Il serait possible de fonctionner avec certaines configurations simples du dépôt `sft.cern.ch`, mais l'approche recommandée est plutôt d'utiliser des conteneurs Singularity où les RPM requis sont installés (voir ci-dessous), ce qui permet en plus d'utiliser plusieurs bases de systèmes d'exploitation (par exemple SL6) sur l'infrastructure CentOS-7 de Calcul Canada.

Pour configurer une vue CentOS7 à partir de `sft.cern.ch` qui comprend les chemins nécessaires aux compilateurs geant4, ROOT, etc. :

```bash
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_95 x86_64-centos7-gcc8-opt
```

Les configurations disponibles de `arch-os-compiler` pour LCG_95 sont :
*   x86_64-centos7-gcc7-dbg
*   x86_64-centos7-gcc7-opt
*   x86_64-centos7-gcc8-dbg
*   x86_64-centos7-gcc8-opt
*   x86_64-slc6-gcc62-opt
*   x86_64-slc6-gcc7-dbg
*   x86_64-slc6-gcc7-opt
*   x86_64-slc6-gcc8-dbg
*   x86_64-slc6-gcc8-opt
*   x86_64-ubuntu1804-gcc7-opt
*   x86_64-ubuntu1804-gcc8-dbg
*   x86_64-ubuntu1804-gcc8-opt

(Une liste de tous les RPM installés via HEP_OSLibs pour CentOS7 se trouve sur [https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt).)

### Exécution dans un conteneur

En date de mai 2020, nous connaissons deux dépôts principaux pour des images de conteneurs pour les logiciels de physique des hautes énergies; ils sont distribués via les dépôts CVMFS.

*   ATLAS : Les distributions des images Singularity sont bien documentées dans [https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment)
    *   Images contenues dans un fichier archive unique (*packed images*) : `/cvmfs/atlas.cern.ch/repo/containers/images/singularity/`
    *   Images contenues dans un répertoire (*unpacked images*) : `/cvmfs/atlas.cern.ch/repo/containers/fs/singularity/`

*   WLCG : dépôt (*unpacked repository*). Ce projet de développement utilise [DUCC](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html) pour publier automatiquement dans CVMFS les images de conteneurs d'un registre Docker. Les images sont publiées dans CVMFS selon un format de structure de répertoire standard qui est utilisé par Singularity ainsi que selon le format en couches utilisé par Docker, ce qui permet d'instancier des images directement de CVMFS avec le plugiciel [Graph Driver](https://cvmfs.readthedocs.io/en/stable/cpt-graphdriver.html). Vous trouverez plus de documentation sur ce projet sur [https://github.com/cvmfs/ducc](https://github.com/cvmfs/ducc). La [liste des images publiées automatiquement](https://gitlab.cern.ch/unpacked/sync/blob/master/recipe.yaml) inclut l'image `atlas-grid-centos7`. Vous pouvez demander de fusionner à cette liste une image additionnelle.
    *   Les images sont sous `/cvmfs/unpacked.cern.ch/`.

## Invoquer une image Singularity

L'exécutable Singularity est quelque peu différent selon le site de Calcul Canada parce qu'il est démarré dans un environnement `setuid` par défaut et donc installé ailleurs qu'avec les logiciels CVMFS habituels de Calcul Canada. Plusieurs versions sont disponibles sur chacun des sites et les valeurs par défaut peuvent être modifiées; il est donc préférable d'invoquer la version nécessaire (présentement, ce sont possiblement 2.6.1, 3.2.0 et 3.3.0).

Pour Cedar :
```bash
/opt/software/singularity-x.x.x
```

Pour Graham :
```bash
/opt/software/singularity-x.x.x
```

Pour Niagara :
```bash
module load singularity
/opt/singularity/2
```

Pour invoquer un conteneur à partir d'un dépôt CVMFS, vous pouvez soit le faire directement puisque l'image sera cachée, soit la télécharger localement ce qui peut améliorer la performance, dépendamment du système.