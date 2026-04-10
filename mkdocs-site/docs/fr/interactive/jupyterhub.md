---
title: "JupyterHub/fr"
tags:
  []

keywords:
  []
---

JupyterHub est le meilleur système pour que plusieurs personnes puissent utiliser simultanément Jupyter Notebook, qu'il s'agisse d'un groupe dans un contexte d'enseignement ou de recherche, ou dans une entreprise de science des données.
<ref>http://jupyterhub.readthedocs.io/en/latest/index.html</ref>

JupyterHub offre une version préconfigurée de JupyterLab et/ou Jupyter Notebook; pour plus d'information sur les options de configuration, consultez la [page Jupyter](jupyter-fr.md).

=Initiatives de l'Alliance=

Notre réseau comprend quelques <i>hubs</i> qui permettent l'accès aux ressources de calcul de pointe.

<span id="JupyterHub_on_clusters"></span>
## JupyterHub sur une grappe 

Utilisez votre nom d'utilisateur et votre mot de passe de de votre compte avec l'Alliance pour vous connecter aux grappes suivantes&nbsp;:[<sup>‡</sup>](#clusters_note.md).
{| class="wikitable"
|-
! JupyterHub !! Commentaires
|-
| <b>[Fir](https://jupyterhub.fir.alliancecan.ca/)</b> || Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web.
|-
| <b>[Narval](https://jupyterhub.narval.alliancecan.ca/)</b> || Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web.
|-
| <b>[Rorqual](https://jupyterhub.rorqual.alliancecan.ca/)</b>|| Donne accès aux serveurs JupyterLab générés par des tâches interactives qui sont lancées à même l’interface web.
|}

Certaines grappes permettent l'accès à JupyterLab via Open OnDemand. Ppour plus d'information, voir [JupyterLab](jupyterlab-fr.md). 

<b><sup id="clusters_note">‡</sup>  Les nœuds de calcul sur lesquels les noyaux (<i>kernels</i>) Jupyter sont activés n'ont pas accès à l'internet.</b> En conséquence, vous pouvez seulement copier des fichiers vers et à partir de votre propre ordinateur. Vous ne pouvez pas télécharger du code ou des données de l'internet par exemple avec `git clone` ou `pip install` si le <i>wheel</i> ne se trouve pas dans notre <i>[wheelhouse](available-python-wheels-fr.md)</i>. Aussi, des problèmes pourraient survenir si votre code effectue des téléchargements ou des téléversements, dans le cas par exemple de l'apprentissage machine où les données sont souvent téléchargées à partir du code.

<span id="JupyterHub_for_universities_and_schools"></span>
## JupyterHub pour les universités et les écoles 

* En collaboration avec l'Alliance et [Cybera](http://www.cybera.ca), le [Pacific Institute for the Mathematical Sciences](https://www.pims.math.ca) offre des hubs infonuagiques aux établissements d'enseignement. Chacun peut avoir son propre hub auquel les utilisateurs accèdent via leur compte d'établissement. Les hubs sont hébergés par notre [service infonuagique](cloud-fr.md) et servent essentiellement à des fins de formation. Les établissements souhaitant obtenir un hub peuvent consulter [Syzygy](http://syzygy.ca).

<span id="Server_options"></span>
= Options pour le serveur =

[thumb|Options pour le serveur sur Béluga](file:jupyterhub_server_options.png.md)
Une fois la connexion établie et selon la configuration de JupyterHub, le navigateur web est redirigé vers
<b>a)</b> un serveur Jupyter précédemment lancé,
<b>b)</b> un nouveau serveur Jupyter possédant des options par défaut, ou
<b>c)</b> un formulaire permettant de configurer les options du serveur Jupyter avant d'appuyer sur le bouton <i>Start</i>.
Dans tous les cas, c'est l'équivalent d'accéder aux ressources demandées via  [une tâche interactive](running_jobs-fr#tâches_interactives.md) sur la grappe correspondante.

<b>Important :</b> Sur chaque grappe, une seule tâche interactive à la fois obtient une plus haute priorité pour commencer à l'intérieur de quelques secondes ou quelques minutes. Ceci inclut les tâches exécutées via `salloc`, `srun` et les tâches JupyterHub. Si vous avez une autre tâche interactive en exécution sur la grappe où se trouve JupyterHub, votre nouvelle session Jupyter pourrait ne pas commencer avant la limite de 5 minutes.

<span id="Compute_resources"></span>
## Ressources de calcul

Par exemple, les options pour [JupyterHub sur Béluga](https://jupyterhub.beluga.computecanada.ca/) sont :
* <i>Account</i> : vous pouvez utiliser un compte de calcul de type `def-*`, `rrg-*`, `rpp-*` ou `ctb-*` auquel vous avez accès;
* <i>Time (hours)</i> : nombre d'heures requises pour la session;
* <i>Number of cores</i> : nombre de CPU réservés sur un seul nœud;
* <i>Memory (MB)</i> : limite de mémoire vive totale pour toute la session; 
* *GPU configuration* (optionnel) : au moins un GPU;
* <i>[Interface utilisateur](jupyterhub-fr#interface_utilisateur.md)</i> (voir ci-dessous).

<span id="User_interface"></span>
## Interface utilisateur 

JupyterHub permet d'avoir accès à un serveur à la fois, mais plusieurs interfaces peuvent être offertes sous <i>User Interface</i>&nbsp;:
* <b>[JupyterLab](jupyterhub-fr#jupyterlab.md)</b> (interface moderne) : cette interface Jupyter est la plus recommandée pour le prototypage interactif et la visualisation des données;
* Jupyter Notebook (interface classique) : cette interface offre beaucoup de fonctionnalités, mais la plupart des utilisateurs choisissent désormais [JupyterLab](jupyterhub-fr#jupiterlab.md) qui est une meilleure plateforme et qui possède beaucoup plus de caractéristiques;
* Terminal (pour un terminal unique) : cette interface donne accès à un terminal connecté à un compte à distance, ce qui se compare à se connecter à un serveur via SSH.

Remarque : JupiterHub peut aussi être configuré pour afficher une interface spécifique, par exemple dans le cas d'un événement spécial.

= JupyterLab =

La description de l'interface JupyterLab se trouve maintenant à la [page JupyterLab](jupyterlab-fr.md).

<span id="Troubleshooting"></span>
<div class="mw-translate-fuzzy">
= Messages d'erreur =
</div>

<span id="&quot;Spawn_failed:_Timeout&quot;"></span>
<div class="mw-translate-fuzzy">
## Spawn failed: Timeout 
</div>

Les erreurs avec JupyterHub sont généralement causées par l'ordonnanceur de tâches sous-jacent qui ne répond pas ou qui est incapable de trouver les ressources appropriées pour votre session, par exemple

[thumb|upright=1.1|JupyterHub - Spawn failed: Timeout](file:jupyterhub-spawn-failed-timeout.png.md)
* Au lancement d'une nouvelle session, JupyterHub soumet automatiquement à la grappe une nouvelle  [tâche interactive](running_jobs-fr#tâches_interactives.md). Si la tâche ne démarre pas dans les cinq prochaines minutes, ce message est affiché et la session est annulée.
** Comme c'est le cas pour toutes les tâches interactives sur une grappe, le fait de demander plus de temps d'exécution peut entraîner une attente plus longue avant que la tâche puisse démarrer, ce qui peut aussi se produire quand vous demandez un GPU ou trop de cœurs CPU. Assurez-vous de demander uniquement les ressources dont vous avez besoin. 
** Si vous avez une autre tâche interactive sur la même grappe, votre session Jupyter sera placée en file d'attente avec les autres tâches en lots. Si c'est possible, arrêtez ou annulez les autres tâches interactives avant d'utiliser JupyterHub.
** Il est possible qu'aucune ressource ne soit disponible à ce moment. Vérifiez si un problème est rapporté dans la page de l'[État des systèmes](https://status.alliancecan.ca/) et essayez de nouveau plus tard.

<span id="&quot;Authentication_error:_Error_403&quot;"></span>
<div class="mw-translate-fuzzy">
## Erreur d'authentification 403 
</div>

Cette erreur survient quand votre compte ou votre accès à la grappe n'est plus valide.
# Vérifiez si votre [<b>compte a été renouvelé et qu'il est actif</b>](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/gestion-de-compte/renouvellements-de-compte)
# Assurez-vous  [<b>d'avoir activé votre accès à la grappe.</b>](https://ccdb.alliancecan.ca/me/access_services)

## Startup hangs 

If JupyterHub posts the message "Your server is starting up.  You will be redirected automatically when it's ready for you" and stays there indefinitely:
* Check for the problems described above under "Spawn failed: Timeout".
* If none of those seem to apply, log on to the cluster with an ordinary SSH client (since JH doesn't work).
* Use `sq` to identify the Slurm job corresponding to your JupyterHub session.
* Cancel the Slurm job with `scancel`.
* Delete hidden Jupyter files with 
<source>
 cd ~
 rm -r .local/share/jupyter
 rm -r .jupyter
</source>
* Try again.  (Jupyter will recreate the hidden files.)

<span id="References"></span>
= Références =