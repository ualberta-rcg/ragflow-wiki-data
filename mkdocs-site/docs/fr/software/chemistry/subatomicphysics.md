---
title: "SubatomicPhysics/fr"
slug: "subatomicphysics"
lang: "fr"

source_wiki_title: "SubatomicPhysics/fr"
source_hash: "3fbde704e577284ba03a4491d2a769f2"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:46:37.987031+00:00"

tags:
  []

keywords:
  - "Singularity"
  - "liste des images publiées automatiquement"
  - "versions 2.6.1 3.2.0 3.3.0"
  - "ATLAS"
  - "téléchargement local"
  - "image Singularity"
  - "CVMFS"
  - "atlas-grid-centos7"
  - "Tier‑3"
  - "environnement setuid"
  - "HEP_OSLibs"
  - "Graph Driver"
  - "ducc"

questions:
  - "Quels problèmes la configuration CCenv peut‑elle engendrer lorsqu’elle accède aux dépôts CVMFS via Nix et EasyBuild sur les nœuds de calcul de Calcul Canada ?"
  - "Pourquoi l’utilisation de conteneurs Singularity est‑elle recommandée plutôt que les configurations basées sur les paquets HEP_OSLibs pour exécuter les logiciels de physique des hautes énergies sur l’infrastructure CentOS‑7 ?"
  - "Où sont‑elles stockées et comment accéder aux images de conteneurs Singularity pour les projets ATLAS et WLCG, notamment via les dépôts CVMFS et le système DUCC ?"
  - "Où les images Singularity sont‑elles situées selon le texte ?"
  - "Pourquoi l’exécutable Singularity varie‑t‑il selon les sites de Calcul Canada et quelles versions sont généralement proposées ?"
  - "Quelles sont les deux méthodes d’invocation d’un conteneur depuis un dépôt CVMFS et quels bénéfices chacune offre‑t‑elle ?"
  - "Quel rôle joue le plugiciel « Graph Driver » dans l’instanciation d’images depuis CVMFS ?"
  - "Où peut‑on consulter la documentation complète du projet DUCC et la liste des images publiées automatiquement ?"
  - "Comment demander l’ajout d’une image supplémentaire à la liste des images publiées automatiquement ?"

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

Voyez aussi la page Installation d'outils d'analyse interactive pour l'astronomie et la physique des hautes énergies.

La plupart des groupes de physique subatomique expérimentale utilisent les dépôts CVMFS du CERN, du consortium Open Science Grid et des dépôts spécifiques pour chacune des expériences.

La configuration `CCenv` qui est à la disposition des utilisateurs réguliers peut créer des conflits avec certaines configurations de ces dépôts parce que l'accès se fait avec Nix et EasyBuild à partir du dépôt CVMFS `soft.computecanada.ca` de Calcul Canada plutôt que par le logiciel installé sur le système d'exploitation de base des nœuds de calcul.

Les utilisateurs ATLAS trouveront de l'information utile dans les pages du twiki TRIUMF.

!!! note "À noter"
    Utilisez les configurations recommandées pour Tier-3 plutôt que de réinventer les techniques décrites plus bas.

*   [https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/ComputeCanadaTier3s)
*   [https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Containers)

Plusieurs configurations présupposent que les nœuds de base sont configurés avec le paquet [HEP_OSLibs](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/master/README.md), ce qui **n'est pas le cas** de nos nœuds de calcul. Il serait possible de fonctionner avec certaines configurations simples du dépôt `sft.cern.ch`, mais l'approche recommandée est plutôt d'utiliser des conteneurs Singularity où les RPM requis sont installés (voir ci-dessous), ce qui permet en plus d'utiliser plusieurs bases de systèmes d'exploitation (par exemple SL6) sur l'infrastructure CentOS-7 de Calcul Canada.

Pour configurer une vue CentOS7 à partir de `sft.cern.ch` qui comprend les chemins nécessaires aux compilateurs geant4, ROOT, etc. :

```bash
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_95 x86_64-centos7-gcc8-opt
```

Les configurations disponibles de `arch-os-complier` pour LCG_95 sont :
*   `x86_64-centos7-gcc7-dbg`
*   `x86_64-centos7-gcc7-opt`
*   `x86_64-centos7-gcc8-dbg`
*   `x86_64-centos7-gcc8-opt`
*   `x86_64-slc6-gcc62-opt`
*   `x86_64-slc6-gcc7-dbg`
*   `x86_64-slc6-gcc7-opt`
*   `x86_64-slc6-gcc8-dbg`
*   `x86_64-slc6-gcc8-opt`
*   `x86_64-ubuntu1804-gcc7-opt`
*   `x86_64-ubuntu1804-gcc8-dbg`
*   `x86_64-ubuntu1804-gcc8-opt`

Une liste de tous les RPM installés via HEPOS_Libs pour CentOS7 se trouve sur [https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs/blob/7.2.11-3.el7/dependencies/HEP_OSlibs.x86_64.dependencies-recursive-flat.txt).

### Exécution dans un conteneur

En date de mai 2020, nous connaissons deux dépôts principaux pour des images de conteneurs pour les logiciels de physique des hautes énergies; ils sont distribués via les dépôts CVMFS.

*   ATLAS : Les distributions des images Singularity sont bien documentées dans [https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/ADCContainersDeployment)
    *   Images contenues dans un fichier archive unique (*packed images*) : `/cvmfs/atlas.cern.ch/repo/containers/images/singularity/`
    *   Images contenues dans un répertoire (*unpacked images*) : `/cvmfs/atlas.cern.ch/repo/containers/fs/singularity/`

*   WLCG : dépôt (*unpacked repository*). Ce projet de développement utilise [DUCC](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html) pour publier automatiquement dans CVMFS les images de conteneurs d'un registre Docker. Les images sont publiées dans CVMFS selon un format de structure de répertoire standard qui est utilisé par Singularity ainsi que selon le format en couches utilisé par Docker, ce qui permet d'instancier des images directement de CVMFS avec le plugiciel [Graph Driver](https://cvmfs.readthedocs.io/en/stable/cpt-graphdriver.html). Vous trouverez plus de documentation sur ce projet sur [https://github.com/cvmfs/ducc](https://github.com/cvmfs/ducc). La [liste des images publiées automatiquement](https://gitlab.cern.ch/unpacked/sync/blob/master/recipe.yaml) inclut l'image `atlas-grid-centos7`. Vous pouvez demander de fusionner à cette liste une image additionnelle.
    *   Les images sont sous `/cvmfs/unpacked.cern.ch/`.

## Invoquer une image Singularity

L'exécutable Singularity est quelque peu différent selon le site de Calcul Canada parce qu'il est démarré dans un environnement `setuid` par défaut et donc installé ailleurs qu'avec les logiciels CVMFS habituels de Calcul Canada. Plusieurs versions sont disponibles sur chacun des sites et les valeurs par défaut peuvent être modifiées; il est donc préférable d'invoquer la version nécessaire (présentement, ce sont possiblement 2.6.1, 3.2.0 et 3.3.0).

Pour invoquer un conteneur à partir d'un dépôt CVMFS vous pouvez soit le faire directement puisque l'image sera cachée, soit le télécharger localement ce qui peut améliorer la performance, dépendant du système.