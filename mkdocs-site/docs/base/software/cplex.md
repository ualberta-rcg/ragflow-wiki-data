---
title: "CPLEX"
tags:
  - software

keywords:
  []
---

[CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) est un logiciel d'optimisation développé par IBM qui est disponible aux usagers universitaires via le programme [Academic Initiative](https://www.ibm.com/academic/home). 

==Téléchargement== 
Pour pouvoir utiliser CPLEX sur une grappe de Calcul Canada, [vous devez d'abord vous inscrire avec IBM](https://www.ibm.com/academic/home) puis télécharger votre version personnelle du logiciel.  Si vous avez le choix entre plusieurs architectures, choisissez *Linux x86-64*.

==Installation== 
Le fichier est une archive exécutable qui fera l'installation en posant quelques questions. Pour exécuter l'archive, il faut faire <tt>bash ./cplex_studioXYZ.linux-x86.bin</tt>.

Pour accéder au logiciel, vous pouvez créer des modules personnels. Les modules sont habituellement créés et mis dans une arborescence de répertories. Pour que vos modules soient trouvés, vous devez modifier le fichier de configuration $HOME/.bashrc pour pointer vers la racine de cette arborescence, en ajoutant la ligne suivante:

```bash

```
$HOME/modulefiles:$MODULEPATH}}

Ensuite, il faut créer une structure de répertoires pour y mettre votre nouveau module cplex:

```bash
mkdir -p $HOME/modulefiles/mycplex
```

Dans ce répertoire, vous allez créer un fichier (par exemple <tt>$HOME/modulefiles/mycplex/12.8.0</tt>) ayant le numéro de la version que vous avez téléchargé précédemment (le XYX) et qui contient ceci:

{{Fichier
  |name=cplex_module.sh
  |lang="sh"
  |contents=

#%Module1.0####
##
## cplex
##
proc ModulesHelp { } {
        global cplexversion

        
puts stderr "\tIBM ILOG cplex "
        puts stderr "\tThis module provides configuration for cplex, concert, cpoptimizer and opl"
}

module-whatis   "IBM ILOG cplex (cplex, concert, cpoptimizer, opl). This version doesn't ask for a licence file."

# for Tcl script use only
set     cplexversion        XYZ
set     studio_root          <root path of cplex>
set     cplexroot             $studio_root/cplex
set     concertroot           $studio_root/concert
set     oplroot               $studio_root/opl
set     cpoptimizerroot       $studio_root/cpoptimizer

set cplexbin x86-64_linux
set cplexlib $cplexbin/static_pic
set concertbin x86-64_linux
set concertlib $concertbin/static_pic
set oplbin x86-64_linux
set opllib $oplbin/static_pic
set cpoptimizerbin x86-64_linux
set cpoptimizerlib $cpoptimizerbin/static_pic

prepend-path    PATH         $cplexroot/bin/$cplexbin
prepend-path    PATH         $oplroot/bin/$oplbin
prepend-path    PATH         $cpoptimizerroot/bin/$cpoptimizerbin

prepend-path    CPATH        $cplexroot/include
prepend-path    CPATH        $concertroot/include
prepend-path    CPATH        $oplroot/include
prepend-path    CPATH        $cpoptimizerroot/include

prepend-path -d " "   CPATH_EXPANDED        -I$cplexroot/include
prepend-path -d " "  CPATH_EXPANDED        -I$concertroot/include
prepend-path -d " "   CPATH_EXPANDED        -I$oplroot/include
prepend-path -d " "   CPATH_EXPANDED        -I$cpoptimizerroot/include

prepend-path    LIBRARY_PATH $cplexroot/lib/$cplexlib
prepend-path    LIBRARY_PATH $concertroot/lib/$concertlib
prepend-path    LIBRARY_PATH $oplroot/lib/$opllib
prepend-path    LIBRARY_PATH $oplroot/bin/x86-64_linux/
prepend-path    LIBRARY_PATH $cpoptimizerroot/lib/$cpoptimizerlib

prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$cplexroot/lib/$cplexlib
prepend-path -d " "  LIBRARY_PATH_EXPANDED -L$concertroot/lib/$concertlib
prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$oplroot/lib/$opllib
prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$oplroot/bin/x86-64_linux/
prepend-path -d " "   LIBRARY_PATH_EXPANDED  -L$cpoptimizerroot/lib/$cpoptimizerlib

prepend-path    LD_LIBRARY_PATH      $cplexroot/bin/$cplexbin
prepend-path    LD_LIBRARY_PATH      $oplroot/bin/$oplbin

prepend-path     CLASSPATH $cplexroot/lib/cplex.jar
prepend-path     MATLABPATH $cplexroot/matlab
prepend-path     STUDIO_ROOT $studio_root

}}

Ajustez les lignes qui correspondent aux variables <tt>cplexversion</tt> et <tt>studio_root</tt> afin qu'elles aient les bonnes valeurs : la version téléchargée et du chemin d'accès pour ce logiciel (c'est-à-dire le chemin que vous avez spécifié lors de l'extraction de l'archive).

==Java== 
Si vous utilisez java, vous aurez quelques étapes supplémentaires. Tout d'abord, dans votre fichier .bashrc, vous pouvez ajouter la ligne,

```bash

```
.}}
qui permettra de trouver votre code lors de l'exécution.

Ensuite, vous devrez modifier la librairie dynamique de CPLEX. Cherchez cette librairie dans l'arborescence du répertoire d'installation, faites-en une copie et exécutez la commande:

```bash
setrpaths.sh --path libcplex1280.so
```

Il est possible que lors de votre compilation, vous ayez un message d'erreur à cause d'un manque de mémoire. Si c'est le cas, vous devrez demander un noeud de calcul interactif pour pouvoir faire la compilation.
Par exemple:

```bash

```
1:0:0 --ntasks1 --mem-per-cpu8G}}

==Python== 
Après avoir fait l'installation de [CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) comme indiqué dans la section précédente, il faut tout d'abord charger CPLEX:

```bash
module load mycplex/<version>
```

Pour installer les paquets de CPLEX tel que <tt>docplex</tt>, nous vous suggérons de le faire à partir d'un [environnement virtuel](python-fr#cr.c3.a9er_et_utiliser_un_environnement_virtuel.md). 

Une fois l'environnement virtuel activé, vous devrez aller dans le répertoire <tt>$STUDIO_ROOT/python</tt> et ensuite vous pouvez faire l'installation de la librairie avec la commande: 

```bash
python setup.py install
```

L'installation des paquets CPLEX doivent se faire sur le noeud de tête, puisqu'elles ne sont pas disponibles sur notre [pile logicielle](available_python_wheels-fr.md).