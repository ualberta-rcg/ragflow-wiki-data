---
title: "CPLEX/fr"
slug: "cplex"
lang: "fr"

source_wiki_title: "CPLEX/fr"
source_hash: "00dc0af68f1910aaa081d1cad4a6d4c2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:13:24.813841+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) est un logiciel d'optimisation développé par IBM qui est disponible aux utilisatrices et utilisateurs universitaires via le programme [Academic Initiative](https://www.ibm.com/academic/home).

## Téléchargement

Pour pouvoir utiliser CPLEX sur une grappe du Centre de Calcul Avancé (CCA), [vous devez d'abord vous inscrire auprès d'IBM](https://www.ibm.com/academic/home) puis télécharger votre version personnelle du logiciel. Si vous avez le choix entre plusieurs architectures, choisissez *Linux x86-64*.

## Installation

Le fichier est une archive exécutable qui effectuera l'installation en posant quelques questions. Pour exécuter l'archive, vous devez taper la commande suivante :

```bash
bash ./cplex_studioXYZ.linux-x86.bin
```

Pour accéder au logiciel, vous pouvez créer des modules personnels. Les modules sont habituellement créés et placés dans une arborescence de répertoires. Pour que vos modules soient trouvés, vous devez modifier le fichier de configuration `$HOME/.bashrc` pour qu'il pointe vers la racine de cette arborescence, en ajoutant la ligne suivante :

```bash
export MODULEPATH=$HOME/modulefiles:$MODULEPATH
```

Ensuite, vous devez créer une structure de répertoires pour y placer votre nouveau module cplex :

```bash
mkdir -p $HOME/modulefiles/mycplex
```

Dans ce répertoire, vous allez créer un fichier (par exemple `$HOME/modulefiles/mycplex/12.8.0`) portant le numéro de la version que vous avez téléchargée précédemment (le XYZ) et qui contient ceci :

```sh title="cplex_module.sh"
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
```

Ajustez les lignes qui correspondent aux variables `cplexversion` et `studio_root` afin qu'elles aient les bonnes valeurs : la version téléchargée et le chemin d'accès pour ce logiciel (c'est-à-dire le chemin que vous avez spécifié lors de l'extraction de l'archive).

## Java

Si vous utilisez Java, vous aurez quelques étapes supplémentaires. Tout d'abord, dans votre fichier `.bashrc`, vous pouvez ajouter la ligne suivante :

```bash
export CLASSPATH=.
```

qui permettra de trouver votre code lors de l'exécution.

Ensuite, vous devrez modifier la bibliothèque dynamique de CPLEX. Cherchez cette bibliothèque dans l'arborescence du répertoire d'installation, faites-en une copie et exécutez la commande suivante :

```bash
setrpaths.sh --path libcplex1280.so
```

!!! attention "Manque de mémoire"
    Il est possible que lors de votre compilation, vous ayez un message d'erreur en raison d'un manque de mémoire. Si c'est le cas, vous devrez demander un nœud de calcul interactif pour pouvoir effectuer la compilation.

Par exemple :

```bash
salloc --time=1:0:0 --ntasks=1 --mem-per-cpu=8G
```

## Python

Après avoir effectué l'installation de [CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) comme indiqué dans la section précédente, vous devez tout d'abord charger CPLEX :

```bash
module load mycplex/<version>
```

Pour installer les paquets de CPLEX, tels que `docplex`, nous vous suggérons de le faire à partir d'un [environnement virtuel](python-fr.md#creer-et-utiliser-un-environnement-virtuel).

Une fois l'environnement virtuel activé, vous devrez aller dans le répertoire `$STUDIO_ROOT/python` et ensuite vous pourrez effectuer l'installation de la bibliothèque avec la commande suivante :

```bash
(ENV) [nom@serveur ~]$ python setup.py install
```

L'installation des paquets CPLEX doit se faire sur le nœud de tête, puisqu'ils ne sont pas disponibles sur notre [pile logicielle](available-python-wheels-fr.md).