---
title: "Visualization/fr"
slug: "visualization"
lang: "fr"

source_wiki_title: "Visualization/fr"
source_hash: "25ab3249571559bcf565470e0238ba25"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:52:13.588103+00:00"

tags:
  - software

keywords:
  - "YT pour l'analyse de données volumétriques"
  - "VisIt"
  - "visualisation client-serveur"
  - "redirection X11"
  - "tâche interactive"
  - "python's matplotlib"
  - "SciNet"
  - "Gnuplot"
  - "ParaView"
  - "serveur X"
  - "VNC"
  - "fenêtres à distance"
  - "remote visualization tools (X-forwarding and VNC)"
  - "VMD"
  - "Webinaires de visualisation"
  - "xmgrace"
  - "ParaView & VisIt"
  - "traitement graphique intensif"
  - "Xvfb"
  - "workshop visualisation"

questions:
  - "Quels sont les paquets de visualisation populaires présentés et quelles sont leurs principales fonctionnalités ?"
  - "Quelle approche de visualisation interactive client‑serveur est recommandée sur les grappes de l’Alliance, et comment se configure‑t‑elle ?"
  - "Pourquoi la redirection X11 est‑elle généralement déconseillée pour le rendu intensif, et quelles alternatives (comme VNC) sont suggérées ?"
  - "Quelle commande Slurm doit‑on utiliser pour demander une tâche interactive avec support X11 sur les nœuds de calcul ?"
  - "Comment exécuter une application graphique en mode « headless » à l’aide de Xvfb, et quelles différences y a‑t‑il selon que l’on utilise un CPU ou un GPU ?"
  - "Pourquoi et comment privilégier une connexion VNC plutôt que le redirection X11 pour des applications comme MATLAB sur les systèmes Alliance ?"
  - "Pourquoi faut‑il éviter la redirection X11 lors d’un traitement graphique intensif ?"
  - "Quelle solution est proposée comme plus rapide que X11 pour les interactions graphiques à distance ?"
  - "Quelles exigences doit‑on remplir pour pouvoir se connecter aux grappes via SSH avec redirection X11 ?"
  - "What visualization tools and libraries are introduced in the “ss2016_visualization‑I.pdf” course material?"
  - "Who is the instructor of the 2016 summer school in Ontario, and which institution are they affiliated with?"
  - "Which software packages are highlighted in the “ss2016_visualization‑II.pdf” overview, and what is the focus of that session?"
  - "Quels webinaires et présentations courtes sont répertoriés sur la page « Visualization Resources » du partenaire de l’Ouest canadien ?"
  - "Où peut‑on accéder aux scripts, astuces et références supplémentaires mentionnés dans les sections « Trucs et astuces » et « Partenaires régionaux et autres références » ?"
  - "Comment contacter le soutien technique en cas de problème avec les outils ou les ressources de visualisation listés ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Paquets populaires

### ParaView
[ParaView](http://www.paraview.org) est un outil d'usage général de visualisation tridimensionnelle pour les domaines scientifiques. Ce logiciel libre fonctionne sous Linux, Windows et Mac; traite la plupart des formats de données; offre plusieurs modes de rendu; utilise les scripts Python; et peut gérer des dizaines de milliers de processeurs pour produire des rendus à partir de grands ensembles de données.

*   [page wiki de l'Alliance](paraview.md)
*   [documentation](http://www.paraview.org/documentation)
*   [gallery](http://www.paraview.org/gallery)
*   [wiki](http://www.paraview.org/Wiki/ParaView)
*   [Python scripting](http://www.paraview.org/Wiki/ParaView/Python_)

### VisIt
Semblable à ParaView, le logiciel libre d'usage général [VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/) est un outil d'analyse et de visualisation tridimensionnelle, capable d'opérer sur un poste de travail ou dans un environnement CHP avec des dizaines de milliers de processeurs.

*   [page wiki de l'Alliance](visit.md)
*   [VisIt website](https://visit-dav.github.io/visit-website)
*   [VisIt gallery](https://visit-dav.github.io/visit-website/examples)
*   [user community wiki](http://www.visitusers.org/)
*   [tutorials](http://www.visitusers.org/index.php?title=VisIt_Tutorial) avec [sample datasets](http://www.visitusers.org/index.php?title=Tutorial_Data)

### VMD
[VMD](http://www.ks.uiuc.edu/Research/vmd) est un logiciel libre pour afficher, animer et analyser les grands systèmes moléculaires en mode tridimensionnel. C'est un outil de visualisation multiplateforme (macOS X, Linux, Windows) qui accepte les scripts Tcl et Python. Capable d'intégrer un grand nombre de *plugiciels* (*plugins*), l'application permet de travailler avec plusieurs formats de données moléculaires.

*   [page wiki de l'Alliance](vmd.md)
*   [VMD User's Guide](http://www.ks.uiuc.edu/Research/vmd/current/ug)

### VTK
VTK (*Visualization Toolkit*) est une boîte à outils logiciels 3D ouverts pour le traitement des images et la visualisation. Comprenant une bibliothèque de classes C++ et d'interfaces pour plusieurs langages interprétés dont Tcl/Tk, Java et Python, VTK a servi de base à plusieurs excellents logiciels de visualisation comme ParaView et VisIt.

*   [page wiki de l'Alliance](vtk.md)
*   [tutorials](https://itk.org/Wiki/VTK/Tutorials)

### YT
YT est une bibliothèque Python pour l'analyse et la visualisation de données volumétriques multirésolution. Développée au départ pour les données de simulation en astrophysique, elle peut traiter toutes les données uniformes multirésolution sur les particules et dans des maillages non structurés cartésiens et curvilignes.

*   [page wiki de l'Alliance](yt.md)

## Utiliser nos grappes

Il existe plusieurs options de travail à distance. Règle générale, pour un rendu interactif, nous recommandons autant que possible la visualisation **client-serveur** avec des nœuds interactifs ou de haute priorité. Pour une visualisation non interactive, nous recommandons les tâches en lot avec des nœuds de calcul réguliers.

D'autres options moins efficaces sont la redirection X11 et VNC qui, dans le cas de certains paquets, sont les seules options d'interface utilisateur à distance.

### Visualisation interactive client-serveur

En mode client-serveur (avec ParaView et VisIt), les données sont traitées sur la grappe à distance avec le rendu sur CPU ou GPU, alors que vous travaillez avec une interface utilisateur client sur votre ordinateur. Pour configurer la visualisation client-serveur, voyez les pages [ParaView](paraview.md) et [VisIt](visit.md).

### Fenêtres à distance avec redirection X11

!!! warning "Redirection X11"
    Règle générale, il faut éviter la redirection X11 pour le traitement graphique intensif puisqu'il y a beaucoup d'interactions et que la vitesse est moindre qu'avec VNC (ci-dessous). Par contre, dans certains cas, vous pouvez vous connecter à nos grappes via SSH par X11. Un serveur X doit être installé sur votre ordinateur.

=== "Rorqual, Fir, Nibi, Narval"

Connectez-vous à la grappe avec l'indicateur `-X/-Y` pour la redirection X11. Vous pouvez démarrer votre application graphique dans le nœud de connexion (pour les petites visualisations).

```bash
module load vmd
vmd
```

Vous pouvez aussi demander des ressources interactives avec un nœud de calcul (visualisations d'envergure).

```bash
salloc --time=1:00:0 --ntasks=1 --mem=3500 --account=def-someprof --x11
```

Une fois que la tâche est en exécution, démarrez l'application graphique à l'intérieur de la tâche.

```bash
module load vmd
vmd
```

=== "Trillium"

Puisque le temps d'exécution dans les nœuds de connexion est limité, vous pourriez demander une tâche test afin de disposer de plus de temps pour explorer et visualiser vos données. Un avantage serait que vous auriez accès à 40 cœurs sur chacun des nœuds demandés. Pour utiliser une session de visualisation interactive, suivez les directives ci-dessous.

1.  Connectez-vous via SSH à `trillium.alliancecan.ca` avec l'indicateur `-X/-Y` pour la redirection X11.
2.  Demandez une tâche interactive.
    ```bash
    debugjob
    ```
    Ceci vous connectera à un nœud, par exemple "niaXYZW".
3.  Démarrez l'application graphique (ici, VMD).

    ```bash
    module load vmd
    vmd
    ```

4.  Quittez la session de débogage.

### Écrans virtuels avec Xvfb

Certaines applications insistent pour afficher les résultats sous forme graphique, mais il n'est pas vraiment nécessaire de les voir parce qu'ils sont enregistrés dans un fichier. Pour travailler sans l'affichage des graphiques, la tâche peut être soumise par lots sur un CPU ou un GPU; pour ceci, exécutez l'application avec les commandes Xvfb (*X virtual framebuffer*) suivantes :

```bash
xvfb-run <name-of-application>
```

si vous travaillez avec un CPU

```bash
xvfb-run vglrun -d egl <name-of-application>
```

si vous travaillez avec un GPU. Dans ce cas, vous devez réserver un GPU (voir [Ordonnancement Slurm des tâches exécutées avec GPU](../running-jobs/using_gpus_with_slurm.md)).
!!! tip
    Remarquez que si le GPU est surchargé, il pourrait ne pas être plus rapide qu'un CPU. L'étalonnage est donc important pour éviter d'utiliser des GPU qui sont plus coûteux.

### Connexion à distance par VNC

Il peut souvent être utile de démarrer une interface utilisateur graphique pour certaines applications comme MATLAB, mais faire ceci par redirection X peut ralentir de beaucoup la connexion au serveur. Nous recommandons d'utiliser VNC pour démarrer et se connecter à distance. Pour plus d'information, voyez la [page VNC](../interactive/vnc.md).

## Formation

Si vous êtes intéressé à organiser un atelier à votre établissement, écrivez à [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca).

### Ateliers d'une journée ou demi-journée

*   [VisIt workshop](https://docs.alliancecan.ca/mediawiki/images/5/5d/Visit201606.pdf), HPCS 2016 à Edmonton, *Marcelo Ponce* et *Alex Razoumov*
*   [ParaView workshop](https://docs.alliancecan.ca/mediawiki/images/6/6c/Paraview201707.pdf), juillet 2017, *Alex Razoumov*
*   [Gnuplot, xmgrace, remote visualization tools (X-forwarding and VNC), python's matplotlib](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-I.pdf), école d'été 2016 en Ontario, *Marcelo Ponce* (SciNet, Université de Toronto)
*   [Brief overview of ParaView & VisIt](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-II.pdf) école d'été 2016 en Ontario, *Marcelo Ponce* (SciNet, Université de Toronto)

### Séminaires Web et autres brèves présentations

La page [Visualization Resources du partenaire de l'Ouest canadien](https://training.westdri.ca/tools/visualization) présente des diapositives et des vidéos de plusieurs webinaires :

*   YT series: “Using YT for analysis and visualization of volumetric data” (Part 1) et "Working with data objects in YT” (Part 2)
*   “Scientific visualization with Plotly”
*   “Novel Visualization Techniques from the 2017 Visualize This Challenge”
*   “Data Visualization on Compute Canada’s Supercomputers”; recettes et démos client-serveur avec ParaView et scripts batch ParaView sur partitions CPU et GPU de nos grappes de calcul
*   “Using ParaViewWeb for 3D Visualization and Data Analysis in a Web Browser”
*   “Scripting and other advanced topics in VisIt visualization”
*   “CPU-based rendering with OSPRay”
*   “3D graphs with NetworkX, VTK, and ParaView”
*   “Graph visualization with Gephi”

Autres présentations :

*   [Remote Graphics on SciNet's GPC system (Client-Server and VNC)](https://oldwiki.scinet.utoronto.ca/wiki/images/5/51/Remoteviz.pdf), rencontre du SciNet User Group d'octobre 2015, *Ramses van Zon* (SciNet, Université de Toronto)
*   [VisIt Basics](https://support.scinet.utoronto.ca/education/go.php/242/file_storage/index.php/download/1/files%5B%5D/6399/), rencontre du SciNet User Group de février 2016, *Marcelo Ponce* (SciNet, Université de Toronto)
*   [Intro to Complex Networks Visualization, with Python](https://oldwiki.scinet.utoronto.ca/wiki/images/e/ea/8_ComplexNetworks.pdf), *Marcelo Ponce* (SciNet, Université de Toronto)
*   [Introduction to GUI Programming with Tkinter](https://oldwiki.scinet.utoronto.ca/wiki/images/9/9c/Tkinter.pdf), septembre 2014, *Erik Spence* (SciNet, Université de Toronto)

## Trucs et astuces

Vous pouvez ajouter ici vos propres scripts et autres renseignements qui ne se trouvent pas dans la documentation signalée sur cette page. Ils pourraient s'avérer intéressants pour d'autres utilisateurs.

## Partenaires régionaux et autres références

*   [**Page de l'équipe nationale pour la visualisation** (comprend plusieurs exemples)](https://ccvis.netlify.app)
*   [Webinaires archivés, Université Simon-Fraser](https://training.westdri.ca/tools/visualization)

### [SciNet, le CHP à l'Université de Toronto](http://www.scinet.utoronto.ca)

*   [Visualization in Niagara](https://docs.scinet.utoronto.ca/index.php/Visualization)
*   [visualization software](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Software_and_Libraries#anchor_viz)
*   [VNC](https://oldwiki.scinet.utoronto.ca/wiki/index.php/VNC)
*   [visualization nodes](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Visualization_Nodes)
*   [further resources and viz-tech talks](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Knowledge_Base:_Tutorials_and_Manuals#Visualization)
*   [using ParaView](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Using_Paraview)

## Dépannage

Contactez le [soutien technique](../support/technical_support.md).