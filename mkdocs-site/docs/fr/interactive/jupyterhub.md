---
title: "JupyterHub/fr"
slug: "jupyterhub"
lang: "fr"

source_wiki_title: "JupyterHub/fr"
source_hash: "0be961c356da783dfe9faccee33b590c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:17:07.791206+00:00"

tags:
  []

keywords:
  - "ressources de calcul"
  - "Béluga"
  - "file d'attente"
  - "Erreur d'authentification 403"
  - "ressources"
  - "État des systèmes"
  - "grappes"
  - "Slurm job"
  - "serveur Jupyter"
  - "accès à la grappe"
  - "interface utilisateur"
  - "serveurs Jupyter"
  - "Options pour le serveur"
  - "tâche interactive"
  - "cœurs CPU"
  - "tâches interactives"
  - "JupyterHub"
  - "Syzygy"
  - "JupyterLab"

questions:
  - "Pour quels types de tâches l'utilisation de JupyterHub est-elle recommandée par rapport à la soumission de tâches non interactives avec sbatch ?"
  - "Quelle restriction réseau importante s'applique aux nœuds de calcul des grappes de l'Alliance et quelles en sont les conséquences pour l'installation de paquets ou le téléchargement de données ?"
  - "Comment les établissements d'enseignement peuvent-ils obtenir et accéder à leur propre environnement JupyterHub infonuagique à des fins de formation ?"
  - "Quelles sont les options de ressources de calcul qu'un utilisateur peut configurer avant de démarrer une session JupyterHub ?"
  - "Quelles sont les différentes interfaces utilisateur disponibles dans JupyterHub et quelles sont leurs particularités ?"
  - "Quelles sont les causes principales de l'erreur \"Spawn failed: Timeout\" et comment peut-on éviter ce problème lors du lancement d'une session ?"
  - "Quelle ressource externe est mentionnée pour obtenir des informations sur le hub ?"
  - "Que se passe-t-il dans le navigateur web une fois la connexion à JupyterHub établie ?"
  - "Quelles sont les deux premières options de serveur Jupyter vers lesquelles un utilisateur peut être redirigé ?"
  - "Quelles demandes de ressources peuvent causer un délai d'attente plus long avant le démarrage d'une tâche ?"
  - "Quelle est la conséquence d'avoir une autre tâche interactive en cours sur la même grappe lors de l'ouverture d'une session Jupyter ?"
  - "Que recommande-t-on de faire avec les autres tâches interactives avant d'utiliser JupyterHub ?"
  - "Que doit-on faire si aucune ressource n'est disponible lors d'une tentative de connexion ?"
  - "Quelles sont les causes de l'erreur d'authentification 403 et comment peut-on la résoudre ?"
  - "Quelles étapes faut-il suivre pour débloquer une session JupyterHub dont le démarrage reste bloqué indéfiniment ?"
  - "Que doit-on faire si aucune ressource n'est disponible lors d'une tentative de connexion ?"
  - "Quelles sont les causes de l'erreur d'authentification 403 et comment peut-on la résoudre ?"
  - "Quelles étapes faut-il suivre pour débloquer une session JupyterHub dont le démarrage reste bloqué indéfiniment ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

JupyterHub est le meilleur système pour que plusieurs personnes puissent utiliser simultanément Jupyter Notebook, qu'il s'agisse d'un groupe dans un contexte d'enseignement ou de recherche, ou dans une entreprise de science des données.

JupyterHub offre une version préconfigurée de JupyterLab et/ou Jupyter Notebook; pour plus d'information sur les options de configuration, consultez [la page Jupyter](../software/jupyter.md).

!!! warning "Exécution de notebooks"
    Jupyter Lab et les notebooks conviennent à vos tâches interactives **brèves** pour tester, déboguer ou visualiser rapidement les données (quelques minutes). Pour des analyses plus longues, il faut utiliser [une tâche non interactive avec sbatch](../running-jobs/running_jobs.md#soumettre-des-taches-avec-sbatch).
    Voir aussi [Exécution de notebooks en scripts Python](../getting-started/advanced_jupyter_configuration.md#execution-de-notebooks-en-scripts-python) ci-dessous.

## Initiatives de l'Alliance

Notre réseau comprend quelques *hubs* qui permettent l'accès aux ressources de calcul de pointe.

## JupyterHub sur une grappe

Utilisez votre nom d'utilisateur et votre mot de passe de votre compte avec l'Alliance pour vous connecter aux grappes suivantes&nbsp;:[<sup>‡</sup>](#clusters_note).

| JupyterHub | Commentaires |
| :--------- | :----------- |
| **[Fir](https://jupyterhub.fir.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |
| **[Narval](https://jupyterhub.narval.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |
| **[Rorqual](https://jupyterhub.rorqual.alliancecan.ca/)** | Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web. |

Certaines grappes permettent l'accès à JupyterLab via Open OnDemand. Pour plus d'information, voir [JupyterLab](jupyterlab.md).

**<sup id="clusters_note">‡</sup> Les nœuds de calcul sur lesquels les noyaux (*kernels*) Jupyter sont activés n'ont pas accès à l'internet.** En conséquence, vous pouvez seulement copier des fichiers vers et à partir de votre propre ordinateur. Vous ne pouvez pas télécharger du code ou des données de l'internet par exemple avec `git clone` ou `pip install` si le *wheel* ne se trouve pas dans notre *[wheelhouse](../programming/available_python_wheels.md)*. Aussi, des problèmes pourraient survenir si votre code effectue des téléchargements ou des téléversements, dans le cas par exemple de l'apprentissage machine où les données sont souvent téléchargées à partir du code.

## JupyterHub pour les universités et les écoles

*   En collaboration avec l'Alliance et [Cybera](http://www.cybera.ca), le [Pacific Institute for the Mathematical Sciences](https://www.pims.math.ca) offre des hubs infonuagiques aux établissements d'enseignement. Chacun peut avoir son propre hub auquel les utilisateurs accèdent via leur compte d'établissement. Les hubs sont hébergés par notre [service infonuagique](../cloud/cloud.md) et servent essentiellement à des fins de formation. Les établissements souhaitant obtenir un hub peuvent consulter [Syzygy](http://syzygy.ca).

## Options pour le serveur

Une fois la connexion établie et selon la configuration de JupyterHub, le navigateur web est redirigé vers
**a)** un serveur Jupyter précédemment lancé,
**b)** un nouveau serveur Jupyter possédant des options par défaut, ou
**c)** un formulaire permettant de configurer les options du serveur Jupyter avant d'appuyer sur le bouton *Démarrer*.
Dans tous les cas, c'est l'équivalent d'accéder aux ressources demandées via [une tâche interactive](../running-jobs/running_jobs.md#taches-interactives) sur la grappe correspondante.

**Important :** Sur chaque grappe, une seule tâche interactive à la fois obtient une plus haute priorité pour commencer à l'intérieur de quelques secondes ou quelques minutes. Ceci inclut les tâches exécutées via `salloc`, `srun` et les tâches JupyterHub. Si vous avez une autre tâche interactive en exécution sur la grappe où se trouve JupyterHub, votre nouvelle session Jupyter pourrait ne pas commencer avant la limite de 5 minutes.

## Ressources de calcul

Par exemple, les options pour [JupyterHub sur Béluga](https://jupyterhub.beluga.computecanada.ca/) sont :
*   *Compte* : vous pouvez utiliser un compte de calcul de type `def-*`, `rrg-*`, `rpp-*` ou `ctb-*` auquel vous avez accès;
*   *Durée (heures)* : nombre d'heures requises pour la session;
*   *Nombre de cœurs* : nombre de CPU réservés sur un seul nœud;
*   *Mémoire (Mo)* : limite de mémoire vive totale pour toute la session;
*   *Configuration GPU* (optionnel) : au moins un GPU;
*   [Interface utilisateur](#interface-utilisateur) (voir ci-dessous).

## Interface utilisateur

JupyterHub permet d'avoir accès à un serveur à la fois, mais plusieurs interfaces peuvent être offertes sous *Interface utilisateur*&nbsp;:
*   **[JupyterLab](#jupyterlab)** (interface moderne) : cette interface Jupyter est la plus recommandée pour le prototypage interactif et la visualisation des données;
*   Jupyter Notebook (interface classique) : cette interface offre beaucoup de fonctionnalités, mais la plupart des utilisateurs choisissent désormais [JupyterLab](#jupyterlab) qui est une meilleure plateforme et qui possède beaucoup plus de caractéristiques;
*   Terminal (pour un terminal unique) : cette interface donne accès à un terminal connecté à un compte à distance, ce qui se compare à se connecter à un serveur via SSH.

Remarque : JupyterHub peut aussi être configuré pour afficher une interface spécifique, par exemple dans le cas d'un événement spécial.

## JupyterLab

La description de l'interface JupyterLab se trouve maintenant à la [page JupyterLab](jupyterlab.md).

## Messages d'erreur

## Échec du démarrage : Délai d'attente dépassé

Les erreurs avec JupyterHub sont généralement causées par l'ordonnanceur de tâches sous-jacent qui ne répond pas ou qui est incapable de trouver les ressources appropriées pour votre session, par exemple

*   Au lancement d'une nouvelle session, JupyterHub soumet automatiquement à la grappe une nouvelle [tâche interactive](../running-jobs/running_jobs.md#taches-interactives). Si la tâche ne démarre pas dans les cinq prochaines minutes, ce message est affiché et la session est annulée.
    *   Comme c'est le cas pour toutes les tâches interactives sur une grappe, le fait de demander plus de temps d'exécution peut entraîner une attente plus longue avant que la tâche puisse démarrer, ce qui peut aussi se produire quand vous demandez un GPU ou trop de cœurs CPU. Assurez-vous de demander uniquement les ressources dont vous avez besoin.
    *   Si vous avez une autre tâche interactive sur la même grappe, votre session Jupyter sera placée en file d'attente avec les autres tâches en lots. Si c'est possible, arrêtez ou annulez les autres tâches interactives avant d'utiliser JupyterHub.
    *   Il est possible qu'aucune ressource ne soit disponible à ce moment. Vérifiez si un problème est rapporté dans la page de l'[État des systèmes](https://status.alliancecan.ca/) et essayez de nouveau plus tard.

## Erreur d'authentification 403

Cette erreur survient quand votre compte ou votre accès à la grappe n'est plus valide.
1.  Vérifiez si votre [**compte a été renouvelé et qu'il est actif**](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/gestion-de-compte/renouvellements-de-compte)
2.  Assurez-vous [**d'avoir activé votre accès à la grappe.**](https://ccdb.alliancecan.ca/me/access_services)

## Démarrage figé

Si JupyterHub affiche le message "Votre serveur est en cours de démarrage. Vous serez redirigé automatiquement lorsqu'il sera prêt." et qu'il reste indéfiniment :
*   Vérifiez les problèmes décrits ci-dessus sous « Échec du démarrage : Délai d'attente dépassé ».
*   Si aucune de ces situations ne semble s'appliquer, connectez-vous à la grappe avec un client SSH ordinaire (puisque JupyterHub ne fonctionne pas).
*   Utilisez `sq` pour identifier la tâche Slurm correspondant à votre session JupyterHub.
*   Annulez la tâche Slurm avec `scancel`.
*   Supprimez les fichiers cachés de Jupyter avec

```bash
cd ~
rm -r .local/share/jupyter
rm -r .jupyter
```

*   Réessayez. (Jupyter recréera les fichiers cachés.)

## Références