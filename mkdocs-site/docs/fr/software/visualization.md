---
title: "Visualization/fr"
tags:
  - software

keywords:
  []
---

<span id="Popular_visualization_packages"></span>
## Paquets populaires

### ParaView 
[ParaView](http://www.paraview.org) est un outil d'usage général de visualisation tridimensionnelle pour les domaines scientifiques. 
Ce logiciel libre fonctionne sous Linux, Windows et Mac; traite la plupart des formats de données; offre plusieurs modes de rendu; utilise les scripts Python; et peut gérer des dizaines de milliers de processeurs pour produire des rendus à partir de grands ensembles de données.

* [page wiki de l'Alliance](paraview-fr.md)
* [documentation](http://www.paraview.org/documentation)
* [gallery](http://www.paraview.org/gallery)
* [wiki](http://www.paraview.org/Wiki/ParaView)
* [Python scripting](http://www.paraview.org/Wiki/ParaView/Python_)

### VisIt 
Semblable à ParaView, le logiciel libre d'usage général [VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/) est un outil d'analyse et de visualisation tridimensionnelle, capable d'opérer sur un poste de travail ou dans un environnement CHP avec des dizaines de milliers de processeurs.

* [page wiki de l'Alliance](visit-fr.md)
* [VisIt website](https://visit-dav.github.io/visit-website)
* [VisIt gallery](https://visit-dav.github.io/visit-website/examples) 
* [user community wiki](http://www.visitusers.org/)
* [tutorials](http://www.visitusers.org/index.php?title=VisIt_Tutorial) avec [sample datasets](http://www.visitusers.org/index.php?title=Tutorial_Data)

### VMD 
[VMD](http://www.ks.uiuc.edu/Research/vmd) est un logiciel libre pour afficher, animer et analyser les grands systèmes moléculaires en mode tridimensionnel. C'est un outil de visualisation multiplateforme (macOS X, Linux, Windows) qui accepte les scripts Tcl et Python. Capable d'intégrer un grand nombre de plugiciels (*plugins*), l'application permet de travailler avec plusieurs formats de données moléculaires.

* [page wiki de l'Alliance](vmd-fr.md)
* [VMD User's Guide](http://www.ks.uiuc.edu/Research/vmd/current/ug)

### VTK 
VTK (*Visualization Toolkit*) est une boîte à outils logiciels 3D ouverts pour le traitement des images et la visualisation. Comprenant une bibliothèque de classes C++ et d'interfaces pour plusieurs langages interprétés dont Tcl/Tk, Java et Python, VTK a servi de base à plusieurs excellents logiciels de visualisation comme ParaView et VisIt.

* [page wiki de l'Alliance](vtk-fr.md)
* [tutorials](https://itk.org/Wiki/VTK/Tutorials)

### YT 
YT est une bibliothèque Python pour l'analyse et la visualisation de données volumétriques multirésolution. Développée au départ pour les données de simulation en astrophysique, elle peut traiter toutes les données uniformes multirésolution sur les particules et dans des maillages non structurés cartésiens et curvilignes.

* [page wiki de l'Alliance](yt-fr.md)

<span id="Visualization_on_Alliance_systems"></span>
## Utiliser nos grappes 

Il existe plusieurs options de travail à distance. Règle générale, pour un rendu interactif, nous recommandons autant que possible la visualisation **client-serveur** avec des nœuds interactifs ou de haute priorité. Pour une visualisation non interactive, nous recommandons les tâches en lot avec des nœuds de calcul réguliers.

D'autres options moins efficaces sont la redirection X11 et VNC qui, dans le cas de certains paquets, sont les seules options d'interface utilisateur à distance.

<span id="Client-server_interactive_visualization"></span>
### Visualisation interactive client-serveur

En mode client-serveur (avec ParaView et VisIt), les données sont traitées sur la grappe à distance avec le rendu sur CPU ou GPU, alors que vous travaillez avec une interface utilisateur client sur votre ordinateur. Pour configurer la visualisation client-serveur, voyez les pages [ParaView](paraview-fr.md) et [VisIt](visit-fr.md).

<span id="Remote_windows_with_X11-forwarding"></span>
### Fenêtres à distance avec redirection X11 

Règle générale, il faut éviter la redirection X11 pour le traitement graphique intensif puisqu'il y a beaucoup d'interactions et que la vitesse est moindre qu'avec VNC (ci-dessous). Par contre, dans certains cas, vous pouvez vous connecter à nos grappes via SSH par X11, comme indiqué ci-dessous. Un serveur X doit être installé sur votre ordinateur.

<tabs>
<tab name="Rorqual, Fir, Nibi, Narval">

Connectez-vous à la grappe avec l'indicateur ` -X/-Y` pour la redirection X11. Vous pouvez démarrer votre application graphique dans le nœud de connexion (pour les petites visualisations).

   module load vmd
   vmd

Vous pouvez aussi demander des ressources interactives avec un nœud de calcul (visualisations d'envergure).

  salloc --time=1:00:0 --ntasks=1 --mem=3500 --account=def-someprof --x11

Une fois que la tâche est en exécution, démarrez l'application graphique à l'intérieur de la tâche.

  module load vmd
  vmd

</tab>
<tab name="Trillium">

Puisque le temps d'exécution dans les nœuds de connexion est limité, vous pourriez demander une tâche test afin de disposer de plus de temps pour explorer et visualiser vos données. Un avantage serait que vous auriez accès à 40 cœurs sur chacun des nœuds demandés. Pour utiliser une session de visualisation interactive, suivez les directives ci-dessous.

<ol>
<li> Connectez-vous via SSH à trillium.alliancecan.ca avec l'indicateur `-X/-Y` pour la redirection X11.
<li> Demandez une tâche interactive.</li>
   debugjob
Ceci vous connectera à un nœud, par exemple "niaXYZW".
<li> Démarrez l'application graphique (ici, VMD). </li>

   module load vmd
   vmd

<li> Quittez la session de débogage.
</ol>

</tab>
</tabs>

<span id="Remote_off-screen_windows_via_Xvfb"></span>
=== Écrans virtuels avec Xvfb === 

Certaines applications insistent pour afficher les résultats sous forme graphique, mais il n'est pas vraiment nécessaire de les voir parce qu'ils sont enregistrés dans un fichier. 
Pour travailler sans l'affichage des graphiques, la tâche peut être soumise par lots sur un CPU ou un GPU; pour ceci, exécutez l'application avec les commandes Xvfb (<i>X virtual framebuffer</i>) suivantes&nbsp;:

  xvfb-run <name-of-application>

si vous travaillez avec un CPU

  xvfb-run vglrun -d egl <name-of-application>

si vous travaillez avec un GPU. Dans ce cas, vous devez réserver un GPU (voir [Ordonnancement Slurm des tâches exécutées avec GPU](using_gpus_with_slurm-fr.md)). Remarquez que si le GPU est surchargé, il pourrait ne pas être plus rapide qu'un CPU. L'étalonnage est donc important pour éviter d'utiliser des GPU qui sont plus coûteux.

<span id="Start_a_remote_desktop_via_VNC"></span>
### Connexion à distance par VNC 

Il peut souvent être utile de démarrer une interface utilisateur graphique pour certaines applications comme MATLAB, mais faire ceci par redirection X peut ralentir de beaucoup la connexion au serveur. Nous recommandons d'utiliser VNC pour démarrer et se connecter à distance. Pour plus d'information, voyez la [page VNC](vnc-fr.md).

<span id="Visualization_training"></span>
= Formation =

Si vous êtes intéressé à organiser un atelier à votre établissement, écrivez à [mailto:support@tech.alliancecan.ca].

### Ateliers d'une journée ou demi-journée 
* [VisIt workshop](https://docs.alliancecan.ca/mediawiki/images/5/5d/Visit201606.pdf), HPCS 2016 à Edmonton, <i>Marcelo Ponce</i> et <i>Alex Razoumov</i>
* [ParaView workshop](https://docs.alliancecan.ca/mediawiki/images/6/6c/Paraview201707.pdf), juillet 2017, <i>Alex Razoumov</i>
* [Gnuplot, xmgrace, remote visualization tools (X-forwarding and VNC), python's matplotlib](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-I.pdf) , école d'été 2016 en Ontario, <i>Marcelo Ponce</i> (SciNet, Université de Toronto) 
* [Brief overview of ParaView & VisIt](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-II.pdf) école d'été 2016 en Ontario, <i>Marcelo Ponce</i> (SciNet, Université de Toronto)

<span id="Webinars_and_other_short_presentations"></span>
### Séminaires Web et autres brèves présentations 

La page [Visualization Resources du partenaire de l'Ouest canadien](https://training.westdri.ca/tools/visualization) présente des diapositives et des vidéos de plusieurs webinaires&nbsp;:

* YT series: “Using YT for analysis and visualization of volumetric data” (Part 1) et "Working with data objects in YT” (Part 2)
* “Scientific visualization with Plotly”
* “Novel Visualization Techniques from the 2017 Visualize This Challenge”
* “Data Visualization on Compute Canada’s Supercomputers”; recettes et démos client-serveur avec ParaView et scripts batch ParaView sur partitions CPU et GPU de nos grappes de calcul
* “Using ParaViewWeb for 3D Visualization and Data Analysis in a Web Browser”
* “Scripting and other advanced topics in VisIt visualization”
* “CPU-based rendering with OSPRay”
* “3D graphs with NetworkX, VTK, and ParaView”
* “Graph visualization with Gephi”

Autres présentations :

* [Remote Graphics on SciNet's GPC system (Client-Server and VNC)](https://oldwiki.scinet.utoronto.ca/wiki/images/5/51/Remoteviz.pdf), rencontre du SciNet User Group d'octobre 2015, <i>Ramses van Zon</i> (SciNet, Université de Toronto)
* [VisIt Basics](https://support.scinet.utoronto.ca/education/go.php/242/file_storage/index.php/download/1/files%5B%5D/6399/), rencontre du SciNet User Group de février 2016, <i>Marcelo Ponce</i> (SciNet, Université de Toronto)
* [Intro to Complex Networks Visualization, with Python](https://oldwiki.scinet.utoronto.ca/wiki/images/e/ea/8_ComplexNetworks.pdf), <i>Marcelo Ponce</i> (SciNet, Université de Toronto)
* [Introduction to GUI Programming with Tkinter](https://oldwiki.scinet.utoronto.ca/wiki/images/9/9c/Tkinter.pdf), septembre 2014, <i>Erik Spence</i> (SciNet, Université de Toronto)

<span id="Tips_and_tricks"></span>
## Trucs et astuces 

Vous pouvez ajouter ici vos propres scripts et autres renseignements qui ne se trouvent pas dans la documentation signalée sur cette page. Ils pourraient s'avérer intéressants pour d'autres utilisateurs.

<span id="Regional_and_other_visualization_pages"></span>
## Partenaires régionaux et autres références 

* [<b>Page de l'équipe nationale pour la visualisation</b> (comprend plusieurs exemples)](https://ccvis.netlify.app)
* [Webinaires archivés, Université Simon-Fraser](https://training.westdri.ca/tools/visualization)

### [SciNet, le CHP à l'Université de Toronto](http://www.scinet.utoronto.ca) 
* [Visualization in Niagara](https://docs.scinet.utoronto.ca/index.php/Visualization)
* [visualization software](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Software_and_Libraries#anchor_viz)
* [VNC](https://oldwiki.scinet.utoronto.ca/wiki/index.php/VNC)
* [visualization nodes](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Visualization_Nodes)
* [further resources and viz-tech talks](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Knowledge_Base:_Tutorials_and_Manuals#Visualization)
* [using ParaView](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Using_Paraview)

## Dépannage
Contactez le [soutien technique](technical-support.md).