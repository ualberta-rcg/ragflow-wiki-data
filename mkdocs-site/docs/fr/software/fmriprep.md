---
title: "FMRIPrep/fr"
slug: "fmriprep"
lang: "fr"

source_wiki_title: "FMRIPrep/fr"
source_hash: "671d7c339e69364cb761e26c94f664e8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:00:58.405855+00:00"

tags:
  - software

keywords:
  - "Pierre Rioux"
  - "présente page"
  - "fichier de licence"
  - "fMRIPrep"
  - "TemplateFlow"
  - "prétraitement d'images"
  - "APPTAINER_BIND"
  - "--fs-license-file"
  - "répertoires"
  - "immense contribution"
  - "FreeSurfer"
  - "contenu"
  - "souligner"
  - "Apptainer"

questions:
  - "Quel est le rôle d'Apptainer dans l'exécution de fMRIPrep et comment doit-on configurer ses variables d'environnement ?"
  - "Pourquoi est-il nécessaire de télécharger les gabarits TemplateFlow à l'avance avec DataLad avant de lancer le conteneur ?"
  - "Quelles sont les étapes supplémentaires requises pour pouvoir utiliser FreeSurfer conjointement avec fMRIPrep ?"
  - "Qui a contribué de manière significative au contenu de cette page ?"
  - "À quoi Pierre Rioux a-t-il apporté une contribution ?"
  - "Comment les auteurs qualifient-ils l'importance de la contribution de Pierre Rioux ?"
  - "Comment obtenir et télécharger le fichier de licence pour FreeSurfer ?"
  - "Dans quel répertoire spécifique doit-on copier le fichier de licence téléchargé ?"
  - "Quelle option de commande permet de spécifier l'emplacement du fichier de licence lors de l'utilisation ?"
  - "Qui a contribué de manière significative au contenu de cette page ?"
  - "À quoi Pierre Rioux a-t-il apporté une contribution ?"
  - "Comment les auteurs qualifient-ils l'importance de la contribution de Pierre Rioux ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Chargement

[fMRIPrep](https://fmriprep.org/en/stable/) est une application [NiPreps](https://www.nipreps.org) pour le prétraitement d'images au format [BIDS](https://bids.neuroimaging.io) obtenues par résonance magnétique. Pour utiliser fMRIPrep sur nos grappes, il faut d'abord charger le module.

```bash
module load apptainer fmriprep
```

## À propos d'Apptainer

En ligne de commande, fMRIPrep utilise Apptainer en arrière-plan pour appeler un conteneur dans lequel fMRIPrep est configuré. Les options en ligne de commande sont passées à la commande fMRIPrep dans ce conteneur, mais vous voudrez aussi modifier le contexte pour Apptainer. Pour ce faire, utilisez les [variables d'environnement d'Apptainer](https://apptainer.org/docs/user/main/appendix.html) comme dans l'exemple quelques paragraphes plus loin.

## Configuration et téléchargement de TemplateFlow

Dans le conteneur, fMRIPrep voudra télécharger les gabarits [TemplateFlow](https://www.templateflow.org), mais en sera incapable. Il aurait fallu télécharger ces données à l'avance avec :

```bash
module load python git-annex
pip3 install datalad
datalad install -r ///templateflow
```

Chargez Python et git-annex, installez DataLad (préférablement dans un environnement virtuel), et installez l'ensemble de métadonnées de TemplateFlow. Le téléchargement se fait dans un répertoire partagé du projet par défaut auquel vous êtes associé. Ce répertoire sera semblable à `/lustre03/project/GROUPNAME/shared/templateflow`. Positionnez-vous dans ce répertoire pour télécharger vos sous-ensembles de gabarits.

```bash
cd /lustre03/project/GROUPNAME/shared/templateflow
datalad get -r tpl-MNI152NLin2009cAsym tpl-OASIS30ANTs
```

Faites de même pour tous les gabarits que vous voulez rendre disponibles.

!!! note "Remarque"
    Le téléchargement des gabarits peut prendre beaucoup de temps, mais ces étapes de DataLad ne sont faites qu'une seule fois et les gabarits seront disponibles pour tous les membres de votre groupe tant qu'ils ne sont pas supprimés.

Pour plus d'information, consultez [l'archive de TemplateFlow](https://www.templateflow.org/usage/archive/).

## Définition des variables d'environnement d'Apptainer

Nous pouvons maintenant configurer nos variables d'environnement Apptainer et fMRIPrep.

```bash
export APPTAINERENV_TEMPLATEFLOW_HOME=/lustre03/project/GROUPNAME/shared/templateflow
export APPTAINER_BIND=/path/to/input,/path/to/output,/path/to/output/logs,$APPTAINERENV_TEMPLATEFLOW_HOME
```

Avec `APPTAINERENV_TEMPLATEFLOW_HOME`, nous disons à fMRIPrep où trouver les gabarits TemplateFlow. Avec `APPTAINER_BIND`, nous disons à Apptainer où trouver les données en entrée, celles en sortie ainsi que les journaux pour que les répertoires appropriés soient montés et rendus disponibles à fMRIprep dans le conteneur.

!!! warning "Attention"
    fMRIPrep gère mal les chemins d'accès longs; utilisez donc des noms courts pour vos fichiers et répertoires.

## Lancement de l'application

Nous pouvons maintenant lancer fMRIPrep.

```bash
fmriprep /path/to/input /path/to/output participant --work-dir /path/to/output
```

Et tout sera parfait. Sauf que...

## Utilisation de FreeSurfer

Si vous voulez utiliser FreeSurfer avec fMRIPrep, il faudra vous [enregistrer auprès de FreeSurfer](https://surfer.nmr.mgh.harvard.edu/registration.html), télécharger le fichier de licence, copier ce fichier dans un des répertoires dans `APPTAINER_BIND` et utiliser [l'option `--fs-license-file`](https://fmriprep.org/en/20.2.0/usage.html?highlight=freesurfer#Specific%20options%20for%20FreeSurfer%20preprocessing). Nous n'irons pas dans les détails parce que nous avons confiance en vous!

## Remerciements

Nous tenons à souligner l'immense contribution de Pierre Rioux au contenu de cette page.