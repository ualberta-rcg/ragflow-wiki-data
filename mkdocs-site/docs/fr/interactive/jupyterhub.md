---
title: "JupyterHub/fr"
slug: "jupyterhub"
lang: "fr"

source_wiki_title: "JupyterHub/fr"
source_hash: "2a11a45c52568114482d4fdd3044778c"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:46:01.562796+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

JupyterHub est le meilleur système pour que plusieurs personnes puissent utiliser simultanément Jupyter Notebook, qu'il s'agisse d'un groupe dans un contexte d'enseignement ou de recherche, ou dans une entreprise de science des données.

JupyterHub offre une version préconfigurée de JupyterLab et/ou Jupyter Notebook; pour plus d'information sur les options de configuration, consultez la [page Jupyter](../software/jupyter.md).

!!! warning "Exécution de notebooks"
    Jupyter Lab et les notebooks conviennent à tes tâches interactives **brèves** pour tester, déboguer ou visualiser rapidement les données (quelques minutes). Pour des analyses plus longues, il faut utiliser [une tâche non interactive avec sbatch](../running-jobs/running_jobs.md#soumettre-des-tâches-avec-sbatch).
    Voir aussi [Exécution de notebooks en scripts Python](../getting-started/advanced_jupyter_configuration.md#exécution-de-notebooks-en-scripts-python) ci-dessous.

# Initiatives de l'Alliance

Notre réseau comprend quelques *hubs* qui permettent l'accès aux ressources de calcul de pointe.

## JupyterHub sur une grappe

Utilisez votre nom d'utilisateur et votre mot de passe de votre compte avec l'Alliance pour vous connecter aux grappes suivantes :

| JupyterHub | Commentaires |
| :--------- | :----------- |
| **[Fir](https://jupyterhub.fir.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |
| **[Narval](https://jupyterhub.narval.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |
| **[Rorqual](https://jupyterhub.rorqual.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |

!!! note
    Les nœuds de calcul sur lesquels les noyaux (*kernels*) Jupyter sont activés n'ont pas accès à l'internet. En conséquence, vous pouvez seulement copier des fichiers vers et à partir de votre propre ordinateur. Vous ne pouvez pas télécharger du code ou des données de l'internet par exemple avec `git clone` ou `pip install` si le *wheel* ne se trouve pas dans notre *[wheelhouse](../programming/available_python_wheels.md)*. Aussi, des problèmes pourraient survenir si votre code effectue des téléchargements ou des téléversements, dans le cas par exemple de l'apprentissage machine où les données sont souvent téléchargées à partir du code.

Certaines grappes permettent l'accès à JupyterLab via Open OnDemand. Pour plus d'information, voir [JupyterLab](jupyterlab.md).

## JupyterHub pour les universités et les écoles

*   En collaboration avec l'Alliance et [Cybera](http://www.cybera.ca), le [Pacific Institute for the Mathematical Sciences](https://www.pims.math.ca) offre des hubs infonuagiques aux établissements d'enseignement. Chacun peut avoir son propre hub auquel les utilisateurs accèdent via leur compte d'établissement. Les hubs sont hébergés par notre [service infonuagique](../cloud/cloud.md) et servent essentiellement à des fins de formation. Les établissements souhaitant obtenir un hub peuvent consulter [Syzygy](http://syzygy.ca).

# Options pour le serveur

Une fois la connexion établie et selon la configuration de JupyterHub, le navigateur web est redirigé vers
**a)** un serveur Jupyter précédemment lancé,
**b)** un nouveau serveur Jupyter possédant des options par défaut, ou
**c)** un formulaire permettant de configurer les options du serveur Jupyter avant d'appuyer sur le bouton *Démarrer*.
Dans tous les cas, c'est l'équivalent d'accéder aux ressources demandées via [une tâche interactive](../running-jobs/running_jobs.md#tâches-interactives) sur la grappe correspondante.

**Important :** Sur chaque grappe, une seule tâche interactive à la fois obtient une plus haute priorité pour commencer à l'intérieur de quelques secondes ou quelques minutes. Ceci inclut les tâches exécutées via `salloc`, `srun` et les tâches JupyterHub. Si vous avez une autre tâche interactive en exécution sur la grappe où se trouve JupyterHub, votre nouvelle session Jupyter pourrait ne pas commencer avant la limite de 5 minutes.

## Ressources de calcul

Par exemple, les options pour [JupyterHub sur Béluga](https://jupyterhub.beluga.computecanada.ca/) sont :
*   *Compte* : vous pouvez utiliser un compte de calcul de type `def-*`, `rrg-*`, `rpp-*` ou `ctb-*` auquel vous avez accès;
*   *Durée (heures)* : nombre d'heures requises pour la session;
*   *Nombre de cœurs* : nombre de CPU réservés sur un seul nœud;
*   *Mémoire (Mo)* : limite de mémoire vive totale pour toute la session;
*   *Configuration GPU* (optionnel) : au moins un GPU;
*   *[Interface utilisateur](#interface-utilisateur)* (voir ci-dessous).

## Interface utilisateur

JupyterHub permet d'avoir accès à un serveur à la fois, mais plusieurs interfaces peuvent être offertes sous *Interface utilisateur* :
*   **[JupyterLab](#jupyterlab)** (interface moderne) : cette interface Jupyter est la plus recommandée pour le prototypage interactif et la visualisation des données;
*   Jupyter Notebook (interface classique) : cette interface offre beaucoup de fonctionnalités, mais la plupart des utilisateurs choisissent désormais [JupyterLab](#jupyterlab) qui est une meilleure plateforme et qui possède beaucoup plus de caractéristiques;
*   Terminal (pour un terminal unique) : cette interface donne accès à un terminal connecté à un compte à distance, ce qui se compare à se connecter à un serveur via SSH.

Remarque : JupyterHub peut aussi être configuré pour afficher une interface spécifique, par exemple dans le cas d'un événement spécial.

# JupyterLab

La description de l'interface JupyterLab se trouve maintenant à la [page JupyterLab](jupyterlab.md).

# Messages d'erreur

## *Spawn failed: Timeout*

Les erreurs avec JupyterHub sont généralement causées par l'ordonnanceur de tâches sous-jacent qui ne répond pas ou qui est incapable de trouver les ressources appropriées pour votre session, par exemple :
*   Au lancement d'une nouvelle session, JupyterHub soumet automatiquement à la grappe une nouvelle [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives). Si la tâche ne démarre pas dans les cinq prochaines minutes, ce message est affiché et la session est annulée.
    *   Comme c'est le cas pour toutes les tâches interactives sur une grappe, le fait de demander plus de temps d'exécution peut entraîner une attente plus longue avant que la tâche puisse démarrer, ce qui peut aussi se produire quand vous demandez un GPU ou trop de cœurs CPU. Assurez-vous de demander uniquement les ressources dont vous avez besoin.
    *   Si vous avez une autre tâche interactive sur la même grappe, votre session Jupyter sera placée en file d'attente avec les autres tâches en lots. Si c'est possible, arrêtez ou annulez les autres tâches interactives avant d'utiliser JupyterHub.
    *   Il est possible qu'aucune ressource ne soit disponible à ce moment. Vérifiez si un problème est rapporté dans la page de l'[État des systèmes](https://status.alliancecan.ca/) et essayez de nouveau plus tard.

## *Authentication error: Error 403*

Cette erreur survient quand votre compte ou votre accès à la grappe n'est plus valide.
1.  Vérifiez si votre [**compte a été renouvelé et qu'il est actif**](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/gestion-de-compte/renouvellements-de-compte)
2.  Assurez-vous [**d'avoir activé votre accès à la grappe.**](https://ccdb.alliancecan.ca/me/access_services)

## Suspension au démarrage

Si JupyterHub affiche le message *Your server is starting up. You will be redirected automatically when it's ready for you*,
*   vérifiez si votre problème correspond à un de ceux qui sont décrits dans *Spawn failed: Timeout* plus haut;
*   si aucun de ces problèmes ne semble s'appliquer, connectez-vous à la grappe avec un client SSH standard (puisque JupyterHub ne fonctionne pas);
*   utilisez `sq` pour identifier la tâche Slurm correspondant à votre session JupyterHub;
*   annulez la tâche Slurm avec `scancel`;
*   supprimez les fichiers cachés de Jupyter avec
    ```bash
    cd ~
    rm -r .local/share/jupyter
    rm -r .jupyter
    ```
*   essayez de nouveau (Jupyter recréera les fichiers cachés).

# Références

*   [Documentation officielle de JupyterHub](http://jupyterhub.readthedocs.io/en/latest/index.html)