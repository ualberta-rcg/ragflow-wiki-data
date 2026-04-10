---
title: "FMRIPrep/fr"
tags:
  - software

keywords:
  []
---

= Chargement =
[fMRIPrep](https://fmriprep.org/en/stable/) est une application [NiPreps](https://www.nipreps.org) pour le prétraitement d'images au format [BIDS](https://bids.neuroimaging.io) obtenues par résonance magnétique. Pour utiliser fMRIPrep sur nos grappes, il faut d'abord charger le module.

<pre>
module load apptainer fmriprep
</pre>

= À propos d'Apptainer =
En ligne de commande, fMRIPrep utilise Apptainer en arrière-plan pour appeler un conteneur dans lequel fMRIPrep est configuré. Les options en ligne de commande sont passées à la commande fMRIPrep dans ce conteneur, mais vous voudrez aussi  modifier le contexte pour Apptainer. Pour ce faire, utilisez les  [variables d'environnement d'Apptainer](https://apptainer.org/docs/user/main/appendix.html) comme dans l'exemple quelques paragraphes plus loin.

= Configuration et téléchargement de TemplateFlow =
Dans le conteneur, fMRIPrep voudra télécharger les gabarits [TemplateFlow](https://www.templateflow.org), mais sera incapable. Il aurait fallu télécharger ces données à l'avance avec

<pre>
module load python git-annex
pip3 install datalad
datalad install -r ///templateflow
</pre>

Chargez Python et git-annex, installez DataLad (préférablement dans un environnement virtuel), et installez l'ensemble de métadonnées de TemplateFlow.  Le téléchargement se fait dans un répertoire partagé du projet par défaut auquel vous êtes associé. Ce répertoire sera semblable à `/lustre03/project/GROUPNAME/shared/templateflow`. Positionnez-vous dans ce répertoire pour télécharger vos sous-ensembles de gabarit.

<pre>
cd /lustre03/project/GROUPNAME/shared/templateflow
datalad get -r tpl-MNI152NLin2009cAsym tpl-OASIS30ANTs 
</pre>

Faites de même pour tous les gabarits que vous voulez rendre disponibles. **REMARQUE : ** le téléchargement des gabarits peut prendre beaucoup de temps, mais '''ces étapes de DataLad ne sont faites qu'une fois'' et les gabarits seront disponibles pour tous les membres de votre groupe tant qu'ils ne sont pas supprimés.  Pour plus d'information, consultez [TemplatFlow archive](https://www.templateflow.org/usage/archive/).
 
= Définition des variables d'environnement Apptainer = 

Nous pouvons maintenant configurer nos variables d'environnement Apptainer et fMRIPrep.

<pre>
export APPTAINERENV_TEMPLATEFLOW_HOME=/lustre03/project/GROUPNAME/shared/templateflow
export APPTAINER_BIND=/path/to/input,/path/to/output,/path/to/output/logs,$APPTAINERENV_TEMPLATEFLOW_HOME
</pre>

Avec `APPTAINERENV_TEMPLATEFLOW_HOME`, nous disons à fMRIPrep où trouver les gabarits TemplateFlow.  Avec `APPTAINER_BIND`, nous disons à Apptainer où trouver les données en entrée, celles en sortie ainsi que les journaux pour que les répertoires appropriés soient montés et rendus disponibles à  fMRIprep dans le conteneur. **ATTENTION :** fMRIPrep gère mal les longs noms de chemins; utilisez donc des noms courts pour vos fichiers et répertoires.

= Lançons enfin l'application =
Nous pouvons maintenant lancer fMRIPrep.

<pre>
fmriprep /path/to/input /path/to/output participant --work-dir /path/to/output
</pre>

Et tout sera parfait. Sauf que ...

= C'est un peu plus compliqué avec FreeSurfer =
Si vous voulez utiliser FreeSurfer avec fMRIPrep, il faudra vous [enregistrer avec FreeSurfer](https://surfer.nmr.mgh.harvard.edu/registration.html), télécharger le fichier de licence, copier ce fichier dans un des répertoires dans `APPTAINER_BIND` et utiliser l'option [`--fs-license-file`](https://fmriprep.org/en/20.2.0/usage.html?highlight=freesurfer#Specific%20options%20for%20FreeSurfer%20preprocessing). Nous n'irons pas dans les détails parce que nous avons confiance en vous!

= Remerciements =
Nous tenons à souligner l'immense contribution de Pierre Rioux au contenu de la présente page.