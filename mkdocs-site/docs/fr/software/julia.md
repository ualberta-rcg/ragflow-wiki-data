---
title: "Julia/fr"
slug: "julia"
lang: "fr"

source_wiki_title: "Julia/fr"
source_hash: "7e48659cd92f310e19a5f5d4b8eae686"
last_synced: "2026-04-12T20:37:21.366223+00:00"
last_processed: "2026-04-12T20:42:59.619184+00:00"

tags:
  - software

keywords:
  - "paquet Julia"
  - "GPU"
  - "dépendances binaires"
  - "CUDA"
  - "Nœuds alloués"
  - "quantité de fichiers"
  - "quota"
  - "Apptainer"
  - "répertoire /home"
  - "code parallèle"
  - "Base.Threads"
  - "Julia"
  - "gestionnaire de paquets"
  - "environnement virtuel Python"
  - "JULIA_DEPOT_PATH"
  - "PyCall.jl"
  - "grappes"
  - "paquets"
  - "grappe"
  - "nœud de calcul GPU"
  - "processus multiples"
  - "chemin du dépôt"
  - "Comportement des fils"
  - "calcul parallèle"
  - "Interface MPI"
  - "CUDA.jl"
  - "Gadfly.jl"
  - "boîte à outils CUDA"

questions:
  - "Comment le système de gestion des paquets de Julia gère-t-il les dépendances binaires et le stockage des différentes versions ?"
  - "Quelle erreur particulière affecte l'installation de paquets sur la grappe Narval et comment peut-on la contourner ?"
  - "Pourquoi l'installation de paquets Julia dans le répertoire personnel (/home) risque-t-elle de poser un problème de quota de fichiers ?"
  - "Quel est le risque principal encouru lors de l'installation de plusieurs paquets Julia dans le répertoire /home ?"
  - "Combien d'espace disque et de fichiers l'installation du paquet Gadfly.jl occupe-t-elle à elle seule ?"
  - "Quelle proportion du quota maximal de fichiers est consommée par l'installation d'un paquet de traçage comme Gadfly.jl ?"
  - "Pourquoi et comment modifier l'emplacement du dépôt Julia personnel (JULIA_DEPOT_PATH) ou utiliser un conteneur Apptainer ?"
  - "Quelle est la procédure recommandée pour configurer le paquet PyCall.jl avec un environnement virtuel Python tout en évitant l'utilisation de Miniconda ?"
  - "Comment configurer un script de tâche pour exécuter du code Julia en parallèle sur plusieurs processus au sein d'une grappe de calcul ?"
  - "Comment configurer et exécuter un programme Julia en parallèle sur plusieurs nœuds à l'aide d'un fichier d'hôtes ou de l'interface MPI ?"
  - "Quelles variables d'environnement permettent de gérer le comportement des fils d'exécution (threads) dans Julia, telles que leur nombre, leur affinité ou leur mise en veille ?"
  - "Quel paquet est recommandé par le document pour programmer et utiliser des processeurs graphiques (GPU) avec Julia ?"
  - "Où peut-on consulter la documentation du paquet PyCall.jl mentionnée dans le texte ?"
  - "Quel calcul mathématique est effectué par le code parallèle Julia sur la grappe de calcul ?"
  - "Quelles sont les ressources matérielles (tâches, cœurs, mémoire) allouées par le script bash fourni ?"
  - "Pourquoi faut-il configurer Julia pour utiliser la boîte à outils locale de CUDA et quelle commande permet de le faire ?"
  - "Comment peut-on vérifier la version de CUDA et tester le bon fonctionnement de l'installation avec un tableau de données ?"
  - "Quelles ressources vidéo sont proposées à la fin du document pour approfondir ses connaissances sur Julia et le calcul parallèle ?"
  - "Pourquoi est-il fortement conseillé de consulter la documentation avant de modifier la configuration par défaut de `Base.Threads` dans Julia ?"
  - "Quel paquet sert d'interface de programmation standard pour l'utilisation des GPU avec Julia ?"
  - "Quelles sont les étapes à suivre pour installer correctement le paquet CUDA.jl sur le système ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Julia](https://julialang.org) est un langage de programmation conçu pour être performant, facile d'utilisation et portable. Sur nos grappes, vous pouvez l'utiliser en installant un [module](../programming/utiliser_des_modules.md).

# Installer des paquets

La première fois que vous ajoutez un paquet à un projet Julia (avec `Pkg.add` ou en mode paquet), le paquet ajouté sera téléchargé, installé dans `~/.julia` et précompilé. Le même paquet peut être ajouté à plusieurs projets, auquel cas les données dans `~/.julia` seront réutilisées. Des versions différentes d'un même paquet peuvent être ajoutées à des projets différents; les versions requises des paquets coexisteront dans `~/.julia`. En comparaison avec Python, les projets Julia remplacent les environnements virtuels en évitant la duplication du code.

**À partir de Julia 1.6,** les paquets Julia incluent leurs dépendances binaires, par exemple les bibliothèques. Il n'est donc pas nécessaire de charger un module logiciel, ce qui de toute façon n'est pas recommandé.

**Jusqu'à Julia 1.5,** des problèmes pourraient survenir si un paquet dépend de binaires fournis par le système. Par exemple, [JLD](https://github.com/JuliaIO/JLD.jl) dépend d'une bibliothèque HDF5 fournie par le système. Sur un ordinateur personnel, Julia tentera d'installer une telle dépendance en utilisant [yum](https://en.wikipedia.org/wiki/Yum_(software)) ou [apt](https://en.wikipedia.org/wiki/APT_(Debian)) avec [sudo](https://en.wikipedia.org/wiki/Sudo). Ceci ne fonctionnera pas sur nos grappes; il faudra plutôt fournir des informations supplémentaires pour permettre au gestionnaire de paquet de Julia (Pkg) de trouver la bibliothèque HDF5.

```bash
module load gcc/7.3.0 hdf5 julia/1.4.1
julia
```
```julia
using Libdl
push!(Libdl.DL_LOAD_PATH, ENV["HDF5_DIR"] * "/lib")
using Pkg
Pkg.add("JLD")
using JLD
```

En supprimant la ligne `Libdl.DL_LOAD_LOAD_PATH` dans cet exemple, il n'y aurait pas de problème sur Graham parce que la bibliothèque HDF5 est installée pour tout le système, ce qui n'est pas le cas avec Cedar. La meilleure solution pour tous nos systèmes est donc d'utiliser le contenu de l'exemple. Chargez d'abord le [module](../programming/utiliser_des_modules.md) approprié et utilisez la variable d'environnement définie par le module (ici `HDF5_DIR`) pour étendre `Libdl.DL_LOAD_PATH`. Ceci fonctionne de la même manière sur tous les systèmes.

Notez que le paquet JLD que nous utilisons ici a été remplacé par [JLD2](https://juliapackages.com/p/jld2) qui ne nécessite plus une bibliothèque HDF5 installée sur le système, ce qui le rend plus portable.

## Sur la grappe Narval

!!! warning "Attention"
    Sur Narval, il arrive parfois que Julia plante quand un paquet est installé dans le répertoire /home en raison d'un bogue dans le logiciel de gestion du système de fichiers. À l'étape de la précompilation, Julia se termine à cause d'une erreur de segmentation.

    Jusqu'à ce que ce problème soit résolu, nous vous recommandons d'utiliser le répertoire /project pour votre *dépôt* Julia.

## Modifier le chemin du dépôt

Un grand nombre de fichiers sont créés quand vous installez un paquet Julia dans votre répertoire /home. Par exemple, dans un répertoire `~/.julia` vide (sans paquet installé), le seul fait d'installer le paquet de traçage `Gadfly.jl` occupe environ 96 Mo avec près de 37 000 fichiers, soit 7 % de la quantité maximale de fichiers permise par votre quota. Si vous installez plusieurs paquets Julia, vous pourriez donc dépasser votre quota.

Pour éviter ceci, vous pouvez enregistrer votre *dépôt* Julia personnel (avec les paquets, bases de registres, fichiers précompilés, etc.) dans un endroit différent, comme votre espace /project. Par exemple, `alice` qui est membre du projet `def-bob` pourrait ajouter ce qui suit à son fichier `~/.bashrc` :

```bash
export JULIA_DEPOT_PATH="/project/def-bob/alice/julia:$JULIA_DEPOT_PATH"
```

Ceci utilisera de préférence le répertoire `/project/def-bob/alice/julia`. Les fichiers dans `~/.julia` seront toujours pris en compte et `~/.julia` sera toujours utilisé pour certains fichiers tels votre historique de commandes. Si vous déplacez votre dépôt dans un autre endroit, il est préférable de supprimer d'abord le dépôt `~/.julia` existant, s'il y a lieu :

```bash
rm -rf $HOME/.julia
```

Vous pouvez aussi créer une image [Apptainer](containers/apptainer.md) avec une version particulière de Julia et un choix de paquets, tout en redirigeant JULIA_DEPOT_PATH dans le conteneur. Vous perdez ainsi l’avantage offert par les modules Julia que nous avons optimisés, par contre la performance des entrées/sorties sera potentiellement meilleure puisque le fichier du conteneur (.sif) rassemble un très grand nombre de petits fichiers. La reproductibilité est aussi améliorée car le conteneur fonctionnera tel quel, n’importe où. De plus, puisque vous avez plein contrôle sur la création du conteneur, vous pourrez tester les versions construites chaque soir (*nightly builds*) sans devoir modifier votre installation locale de Julia ou encore rassembler vos propres dépendances.

# Appeler Python avec PyCall.jl

Le paquet PyCall.jl peut servir d'interface entre Julia et Python; dans ce cas, la variable d'environnement `PYTHON` doit être définie comme étant l'exécutable Python dans votre environnement virtuel Python. Sur nos grappes, nous recommandons [l'utilisation d'environnements Python](python.md). Une fois qu'un environnement est activé, vous pouvez l'utiliser dans PyCall.jl.

```bash
source "$HOME/myenv/bin/activate"
julia
```
```julia
using Pkg, PyCall
ENV["PYTHON"] = joinpath(ENV["VIRTUAL_ENV"], "bin", "python")
Pkg.build("PyCall")
```

Nous vous conseillons fortement d'éviter le comportement par défaut de PyCall.jl qui est d'utiliser une distribution Miniconda à l'intérieur de votre environnement Julia. [Anaconda et les autres distributions similaires](anaconda.md) ne conviennent pas sur nos grappes.

Prenez note que si vous ne créez pas un environnement virtuel comme décrit ci-dessus, PyCall utilisera par défaut l’installation Python du système d’exploitation, ce qu’il faut éviter. PyCall invoquera Conda.jl mais ne reconnaîtra pas le chemin correct à moins que vous ayez reconstruit avec `ENV["PYTHON"]=""`. De plus, sans compter les incompatibilités possibles avec la pile logicielle, l'installateur Miniconda créera plusieurs fichiers dans JULIA_DEPOT_PATH et vous pourriez voir des problèmes de quota et de performance si le chemin par défaut est `~/.julia`.

Pour plus d'information, voir [la documentation pour PyCall.jl](https://github.com/JuliaPy/PyCall.jl)

# Travailler avec plusieurs processus sur une grappe

Dans l'exemple suivant, du code parallèle Julia est utilisé pour calculer `pi` avec 100 cœurs sur les nœuds d'une grappe.

```bash
# Fichier : run_julia_pi.sh
#!/bin/bash
#SBATCH --ntasks=100
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1024M
#SBATCH --time=0-00:10

srun hostname -s > hostfile
sleep 5
julia --machine-file ./hostfile ./pi_p.jl 1000000000000
```

Dans cet exemple, la commande
`srun hostname -s > hostfile`
génère une liste des noms des nœuds alloués et ajoute cette liste au fichier texte `hostfile`. Ensuite, la commande

`julia --machine-file ./hostfile ./pi_p.jl 1000000000000`
démarre un processus Julia principal et 100 processus de travail sur les nœuds spécifiés dans `hostfile` et lance le programme `pi_p.jl` en parallèle.

# Interface MPI

Assurez-vous que la MPI de Julia est configurée pour utiliser nos bibliothèques MPI : lancez

```bash
module load StdEnv julia
```
Lancez ensuite Julia puis, à partir de Julia, lancez :

```julia
import Pkg
Pkg.add("MPIPreferences")
using MPIPreferences
MPIPreferences.use_system_binary(;extra_paths=[joinpath(ENV["EBROOTOPENMPI"],"lib64")])
Pkg.add("MPI")
```

Pour l'utiliser par la suite, lancez (pour deux processus) :

```bash
module load StdEnv julia
mpirun -np 2 julia hello.jl
```

Le code `hello.jl` est :

```julia
using MPI
MPI.Init()
comm = MPI.COMM_WORLD
print("Hello world, I am rank $(MPI.Comm_rank(comm)) of $(MPI.Comm_size(comm))\n")
MPI.Barrier(comm)
```

# Configurer le comportement des fils

Vous pouvez limiter le nombre de fils utilisés par Julia en configurant JULIA_NUM_THREADS=k; par exemple pour un processus unique pour une tâche de 12 CPU par tâche, k serait égal à 12.
Il est habituel que le nombre de fils soit égal au nombre de processeurs; ceci est toutefois abordé dans la page [Scalabilité](../running-jobs/scalability.md).
De plus, vous pouvez *attacher* des fils à un cœur en configurant JULIA_EXCLUSIVE à une valeur autre que zéro. Comme décrit dans la [documentation](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_EXCLUSIVE), ceci enlève au système d'exploitation l'attribution des fils en les attachant aux cœurs en fonction de leur affinité. Dépendant des calculs effectués par les fils, ceci peut améliorer la performance quand il y a des informations précises sur les modes d'accès aux caches ou que le système d'exploitation attribue les fils de manière non voulue. La configuration de JULIA_EXCLUSIVE fonctionne uniquement si votre tâche a un accès exclusif aux nœuds et que tous les cœurs CPU ont été alloués à votre tâche. Puisque l'ordonnanceur Slurm attache les processus et les fils aux cœurs CPU, le fait de demander à Julia de *réattacher* les fils n'améliorera peut-être pas la performance.

La variable [JULIA_THREAD_SLEEP_THRESHOLD](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_THREAD_SLEEP_THRESHOLD) contrôle le nombre de nanosecondes après lesquelles un fil qui est en rotation (*spinning*) est programmé pour dormir. Une valeur infinie exprimée par une chaîne de caractères indique que le fil en rotation ne doit jamais dormir. Il peut être utile de modifier cette variable quand plusieurs fils se disputent fréquemment une ressource partagée; il serait alors peut-être préférable d'éliminer plus rapidement des fils en rotation. Dans un contexte de forte concurrence, les fils en rotation ne feraient qu'augmenter la charge sur les CPU. De la même manière, quand une ressource est rarement sollicitée, une basse latence peut se produire si on refuse aux fils de dormir, c'est-à-dire que le seuil est défini comme étant infini.

Il va sans dire que ces valeurs ne devraient être configurées qu'après avoir profilé les problèmes potentiels de concurrence. Puisque Julia et particulièrement ses `Base.Threads` évoluent très rapidement, vous devriez toujours consulter la documentation pour vous assurer que le fait de modifier la configuration par défaut aura effectivement le résultat désiré.

# Utiliser les GPU

L'interface de programmation habituelle pour travailler avec les GPU est le paquet CUDA.jl. Vous pouvez l'installer avec le gestionnaire de paquets Julia. Téléchargez d'abord le paquet sur un nœud de connexion.

```bash
# sur un nœud de connexion!
module load cuda/12.9 julia/1.11.3
julia
```
```julia
ENV["JULIA_PKG_PRECOMPILE_AUTO"]=0
import Pkg; Pkg.add("CUDA")
```

**Tout ce qui suit doit être fait sur un nœud de calcul GPU.** Il est possible que la boîte à outils CUDA téléchargée lors de l'installation ne fonctionne pas avec le pilote CUDA qui est installé. Pour éviter ce problème, configurez Julia pour utiliser la boîte à outils locale de CUDA avec :

```julia
using CUDA
CUDA.set_runtime_version!(v"version_of_cuda", local_toolkit=true)
```
où `version_of_cuda` est 12.2, si `cuda/12.2` est chargé.

Après avoir redémarré Julia, vous pouvez vérifier si la version CUDA est la bonne avec :

```julia
CUDA.versioninfo()
```
Résultat attendu :
```
CUDA runtime 12.6, local installation
...
```

Pour tester l'installation, lancez :

```julia
a = CuArray([1,2,3])
```
Résultat attendu :
```
3-element CuArray{Int64, 1, CUDA.Mem.DeviceBuffer}:
 1
 2
 3
```
```julia
a.+=1
```
Résultat attendu :
```
3-element CuArray{Int64, 1, CUDA.Mem.DeviceBuffer}:
 2
 3
 4
```

# Plus d'information

Webinaires produits par SHARCNET :
* [Julia: A first perspective (47 minutes)](https://youtu.be/gKxs0L2Ac4I)
* [Julia: A second perspective (57 minutes)](https://youtu.be/-QuqSOUbY6Q)
* [Julia: A third perspective - parallel computing explained (65 minutes)](https://youtu.be/HWLV6oTmfO8)
* Julia: Parallel computing revisited (en préparation)