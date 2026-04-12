---
title: "MATLAB/fr"
slug: "matlab"
lang: "fr"

source_wiki_title: "MATLAB/fr"
source_hash: "a55541f636df68d33bc7f194b24c975d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:37:07.104435+00:00"

tags:
  - software

keywords:
  - "Cluster Profile Manager"
  - "licence externe"
  - "MATLAB"
  - "MATLAB Compiler"
  - "soumettre une tâche"
  - "documentation"
  - "programme séquentiel"
  - "sbatch"
  - "Parallel Computing Toolbox"
  - "ressources externes"
  - "exécuter des tâches"
  - "ccSBATCH"
  - "Slurm"
  - "parpool"
  - "Auto-apprentissage"
  - "grappes"
  - "MathWorks"
  - "compilateur mcc"
  - "tâches parallèles"
  - "local_cluster_jobs"
  - "MathWorks Slurm Plugin"
  - "Module d'extension pour Slurm"
  - "fichier .dat"
  - "problème avec SSH"
  - "MATLAB Parallel Server"
  - "ordinateur local"
  - "profil parallèle local"
  - "ordonnanceur"
  - "outil de validation"
  - "configuration de grappe"
  - "exécution en parallèle"
  - "exemples de scripts"
  - "calculs d'envergure"
  - "calcul parallèle"

questions:
  - "Quelles sont les deux méthodes principales pour utiliser MATLAB sur les grappes et comment diffèrent-elles au niveau des exigences de licence ?"
  - "Comment peut-on vérifier la disponibilité d'une licence externe et quelles sont les étapes pour la configurer sur les serveurs ?"
  - "Pourquoi est-il nécessaire de créer un lien symbolique du répertoire `.matlab` vers `/scratch` avant de soumettre des calculs d'envergure à l'ordonnanceur ?"
  - "Quelle commande permet de charger et d'exécuter MATLAB en mode batch sans interface graphique ?"
  - "Quels sont les critères de durée et de mémoire qui définissent un calcul MATLAB d'envergure ?"
  - "Quelle est la procédure obligatoire à suivre si les ressources requises par le programme dépassent ces limites ?"
  - "Comment soumettre et exécuter un script MATLAB standard à l'aide de l'ordonnanceur Slurm ?"
  - "Quelle est la méthode recommandée pour configurer et exécuter du code MATLAB en parallèle sur plusieurs cœurs d'un même nœud ?"
  - "Quel problème de corruption de fichiers peut survenir lors du lancement simultané de plusieurs tâches parallèles et comment le résoudre ?"
  - "Quelle situation provoque le conflit de lecture et d'écriture lors de l'initialisation de parpool ?"
  - "Quelles sont les conséquences exactes de ce conflit sur les fichiers et le profil parallèle local ?"
  - "Quelle est la solution recommandée pour résoudre ce problème une fois qu'il s'est produit ?"
  - "Comment configurer un profil parallèle unique pour chaque tâche MATLAB afin d'éviter les conflits d'exécution ?"
  - "Quelles sont les étapes requises pour compiler un code MATLAB et l'exécuter correctement sur les serveurs avec les bibliothèques Runtime (MCR) ?"
  - "Pour quelle raison technique n'est-il plus possible de soumettre des tâches MATLAB parallèles à partir d'une interface locale depuis mai 2023 ?"
  - "Quelles sont les informations spécifiques requises pour configurer le profil de grappe (cluster) pour Narval ou Rorqual dans MATLAB ?"
  - "Quels fichiers de l'extension Slurm doivent être modifiés après l'installation et quelles commandes faut-il y insérer ?"
  - "Quelle est la procédure recommandée pour valider l'installation au lieu d'utiliser l'outil par défaut \"Cluster Profile Manager\" ?"
  - "Pourquoi est-il actuellement impossible de soumettre une tâche à partir d'un ordinateur local avec MATLAB ?"
  - "Quelles sont les raisons pour lesquelles la procédure du module d'extension pour Slurm ne fonctionne plus ?"
  - "Pourquoi la procédure a-t-elle été conservée dans la documentation malgré l'absence de solution actuelle ?"
  - "Quel outil de validation peut être utilisé pour les deux premiers tests lorsque le fichier H.m se trouve dans le répertoire courant ?"
  - "Pourquoi l'outil de validation ne permet-il pas d'effectuer les tests suivants ?"
  - "Quelles ressources externes sont recommandées dans le texte et par quelle entreprise sont-elles fournies ?"
  - "Quelles sont les langues proposées par la plateforme d'auto-apprentissage MATLAB Academy ?"
  - "Quel type de documentation spécifique certaines universités mettent-elles à disposition pour l'apprentissage ?"
  - "Quelle université est donnée en exemple pour trouver des modèles de scripts MATLAB ?"
  - "Quelles sont les langues proposées par la plateforme d'auto-apprentissage MATLAB Academy ?"
  - "Quel type de documentation spécifique certaines universités mettent-elles à disposition pour l'apprentissage ?"
  - "Quelle université est donnée en exemple pour trouver des modèles de scripts MATLAB ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Il y a deux façons d'utiliser MATLAB sur nos grappes :

**1. Exécuter directement MATLAB**, mais vous devez avoir accès à une licence, soit :
* la licence fournie sur [Fir](fir.md), [Narval](../clusters/narval.md) ou [Trillium](../clusters/trillium.md) ou pour les étudiants, professeurs et chercheurs;
* une licence externe détenue par votre établissement, faculté, département ou laboratoire (voir la section *Utiliser une licence externe* ci-dessous).

**2. Compiler votre code MATLAB** avec le compilateur `mcc` et utiliser le fichier exécutable généré sur une de nos grappes. Vous pouvez utiliser cet exécutable sans tenir compte de la licence.

Vous trouverez ci-dessous les détails pour ces approches.

## Utiliser une licence externe
Nous sommes fournisseurs d'hébergement pour MATLAB. Dans ce contexte, MATLAB est installé sur nos grappes et vous pouvez avoir accès à une licence externe pour utiliser notre infrastructure; dans le cas de certains établissements, ceci s'effectue de façon automatique. Pour savoir si vous avez accès à une licence, faites le test suivant :

```bash
[name@cluster ~]$ module load matlab/2023b.2
[name@cluster ~]$ matlab -nojvm -nodisplay -batch license

987654
[name@cluster ~]$
```

Si tout est en ordre, un numéro de licence sera imprimé. Assurez-vous d'effectuer ce test sur chaque grappe avec laquelle vous voulez utiliser MATLAB puisque certaines licences ne sont pas disponibles partout.

Si vous obtenez le message *This version is newer than the version of the license.dat file and/or network license manager on the server machine*, essayez d'entrer une version moins récente de MATLAB dans la ligne `module load`.

Autrement, il se peut que votre établissement n'ait pas de licence, qu'il ne soit pas possible d'utiliser la licence de cette manière ou qu'aucune entente n'ait été conclue avec nous pour utiliser la licence. Pour savoir si vous pouvez utiliser une licence externe, contactez l'administrateur de la licence MATLAB de votre établissement ou votre gestionnaire de compte MATLAB.

Si vous pouvez utiliser une licence externe, certaines opérations de configuration sont requises. D'abord, vous devez créer un fichier semblable à

```bash hl_lines="1-3" title="matlab.lic"
# spécifications du serveur de licence
SERVER <ip address> ANY <port>
USE_SERVER
```

et placer ce fichier dans le répertoire `$HOME/.licenses/` où l'adresse IP et le numéro du port correspondent aux valeurs du serveur de licence de votre établissement. Notre équipe technique devra alors contacter le personnel technique qui gère votre licence pour que votre serveur puisse se connecter à nos nœuds de calcul. Pour organiser ceci, contactez le [soutien technique](../support/technical_support.md).

Consultez la documentation technique [http://www.mathworks.com/support](http://www.mathworks.com/support) et l'information sur le produit [http://www.mathworks.com](http://www.mathworks.com).

## Préparer votre répertoire `.matlab`
Puisque le répertoire `/home` de certains nœuds de calcul n'est accessible qu'en lecture, vous devez créer un lien symbolique `.matlab` pour que le profil et des données des tâches soient plutôt consignés dans `/scratch`.

```bash
[name@cluster ~]$ cd $HOME
[name@cluster ~]$ if [ -d ".matlab" ]; then
  mv .matlab scratch/
else
  mkdir -p scratch/.matlab
fi && ln -sn scratch/.matlab .matlab
```

## Boîtes à outils
Pour la liste des boîtes à outils disponibles avec la licence et la grappe sur laquelle vous travaillez, utilisez :

```bash
[name@cluster ~]$  module load matlab
[name@cluster ~]$  matlab -nojvm -batch "ver"
```

## Exécuter un programme séquentiel MATLAB

!!! important "Important"
    Pour tous les calculs d'envergure (durée de plus de cinq minutes ou mémoire d'un Go), la tâche doit être soumise à l'ordonnanceur comme démontré dans l'exemple suivant. Pour plus d'information, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

Voici un exemple de code :

```matlab hl_lines="1-2" title="cosplot.m"
function cosplot()
% exemple pour approximer un signal en dents de scie
% par une série de Fourier tronquée
nterms=5;
fourbypi=4.0/pi;
np=100;
y(1:np)=pi/2.0;
x(1:np)=linspace(-2.0*pi,2*pi,np);

for k=1:nterms
 twokm=2*k-1;
 y=y-fourbypi*cos(twokm*x)/twokm^2;
end

plot(x,y)
print -dpsc matlab_test_plot.ps
quit
end
```

Voici un script pour l'ordonnanceur Slurm qui exécute `cosplot.m` :

```bash hl_lines="2-9" title="matlab_slurm.sl"
#!/bin/bash -l
#SBATCH --job-name=matlab_test
#SBATCH --account=def-someprof # nom du compte utilisé pour soumettre des tâches
#SBATCH --time=0-03:00         # limite de temps (JJ-HH:MM)
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1      # à modifier si vous utilisez des commandes parallèles
#SBATCH --mem=4000             # mémoire requise par nœud (en mégaoctets par défaut)

# chargez le module pour la version voulue
module load matlab/2024b.1
matlab -singleCompThread -batch "cosplot"
```

Soumettez la tâche avec `sbatch`.

```bash
sbatch matlab_slurm.sl
```

Chaque fois que MATLAB est lancé, un fichier comme `java.log.12345` pourrait être créé. Pour économiser l'espace de stockage, ce fichier doit être supprimé une fois que MATLAB est fermé. La création de ce fichier peut cependant être évitée en utilisant l'option `-nojvm`, mais ceci pourrait interférer avec certaines fonctions de traçage.

Pour plus d'information sur les options en ligne de commande dont `-nodisplay`, `-nojvm`, `-singleCompThread`, `-batch` et autres, voir [MATLAB (Linux) le site de MathWorks](https://www.mathworks.com/help/matlab/ref/matlablinux.html).

## Exécuter en parallèle

MATLAB prend en charge [plusieurs modes d'exécution en parallèle](https://www.mathworks.com/help/parallel-computing/quick-start-parallel-computing-in-matlab.html). Pour la plupart d'entre vous, il suffira d'exécuter MATLAB dans un environnement parallèle `Threads` sur un nœud simple. Voici un exemple inspiré de [la documentation de MathWorks au sujet de `parfor`](https://www.mathworks.com/help/parallel-computing/parfor.html).

```matlab hl_lines="1-2" title="timeparfor.m"
function timeparfor()
   nthreads = str2num(getenv('SLURM_CPUS_PER_TASK'))
   parpool("Threads",nthreads)
   tic
   n = 200;
   A = 500;
   a = zeros(1,n);
   parfor i = 1:n
       a(i) = max(abs(eig(rand(A))));
   end
   toc
end
```

Sauvegardez le code ci-dessus dans un fichier nommé `timeparfor.m`. Créez ensuite le script suivant et soumettez-le avec `sbatch matlab_parallel.sh` pour exécuter la fonction en parallèle avec quatre cœurs.

```bash hl_lines="2-5" title="matlab_parallel.sh"
#!/bin/bash -l
#SBATCH --account=def-someprof
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=2000
module load matlab/2024b.1
matlab -nojvm -batch "timeparfor"
```

Vous pouvez expérimenter en donnant à `--cpus-per-task` des valeurs plus petites (par exemple 1, 2, 6, 8) pour voir l'effet sur la performance.

## Lancer en simultané plusieurs tâches parallèles
Si vous utilisez un environnement `Cluster` parallèle comme [ce qui est décrit ici](https://www.mathworks.com/help/parallel-computing/quick-start-parallel-computing-in-matlab.html#mw_d4204011-7467-47d9-b765-33dc8a8f83cd), le problème suivant pourrait survenir. Quand deux ou plusieurs tâches parallèles initialisent `parpool` au même moment, chacune des tâches essait de lire et écrire dans le même fichier `.dat` du répertoire `$HOME/.matlab/local_cluster_jobs/R*`. Ceci corrompt le profil parallèle local utilisé par les autres tâches. Si ceci se produit, supprimez le répertoire `local_cluster_jobs` quand aucune tâche n’est en cours d’exécution.

Pour éviter ce problème, nous recommandons que chaque tâche crée son propre profil parallèle dans un endroit unique en spécifiant la propriété de l'objet [`parallel.Cluster`](https://www.mathworks.com/help/parallel-computing/parallel.cluster.html), comme démontré ici.

```matlab hl_lines="1-2" title="parallel_main.m"
local_cluster = parcluster('local')
local_cluster.JobStorageLocation = getenv('SLURM_TMPDIR')
parpool(local_cluster);
```

Références :
* FAS Research Computing, [*MATLAB Parallel Computing Toolbox simultaneous job problem*](https://www.rc.fas.harvard.edu/resources/documentation/software/matlab-pct-simultaneous-job-problem/)
* MathWorks, [*Why am I unable to start a local MATLABPOOL from multiple MATLAB sessions that use a shared preference directory using Parallel Computing Toolbox 4.0 (R2008b)?*](https://www.mathworks.com/matlabcentral/answers/97141-why-am-i-unable-to-start-a-local-matlabpool-from-multiple-matlab-sessions-that-use-a-shared-preferen)

## Utiliser les bibliothèques Compiler et Runtime

!!! important "Important"
    Comme pour toutes les tâches aux exigences élevées, le code MCR doit toujours être inclus dans une tâche soumise à l'ordonnanceur; consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

Vous pouvez aussi compiler votre code avec MATLAB Compiler, un des modules dont nous sommes fournisseurs d'hébergement. Consultez la [documentation MATLAB Compiler](https://www.mathworks.com/help/compiler/index.html). Pour l'instant, mcc est disponible pour les versions 2014a, 2018a et suivantes.

Pour compiler l'exemple avec `cosplot.m` ci-dessus, vous utiliseriez la commande :

```bash hl_lines="1" title="[name@yourserver ~]$"
mcc -m -R -nodisplay cosplot.m
```

Ceci produit le binaire `cosplot` et le script enveloppant `run_cosplot.sh`. Pour exécuter le binaire sur nos serveurs, vous n'avez besoin que du binaire. Le script enveloppant ne fonctionnera pas tel quel sur nos serveurs puisque MATLAB s'attend à ce que certaines bibliothèques se trouvent à des endroits spécifiques. Utilisez plutôt le script enveloppant `run_mcr_binary.sh` qui définit les bons chemins.

[Chargez le module](../programming/utiliser_des_modules.md) MCR correspondant à la version de MATLAB que vous utilisez pour créer votre exécutable :

```bash
module load mcr/R2024b
```

Lancez la commande :

```bash
setrpaths.sh --path cosplot
```

ensuite, dans le script pour la tâche (**et non dans les nœuds de connexion**), utilisez le binaire comme suit :
`run_mcr_binary.sh cosplot`

La commande `setrpaths.sh` ne doit être exécutée qu'une seule fois pour chacun des binaires compilés; `run_mcr_binary.sh` vous demandera de l'exécuter si ce n'est pas fait.

## Utilisation de MATLAB Parallel Server
MATLAB Parallel Server n’est utile que si votre tâche MATLAB parallèle possède plus de processus (appelés *workers*) que les cœurs CPU disponibles sur un nœud de calcul unique. L’installation régulière de MATLAB décrite ci-dessus permet d’exécuter des tâches parallèles avec un nœud (jusqu’à 64 *workers* par tâche selon la grappe et le nœud); pour utiliser plus d’un nœud.

Cette solution permet habituellement de soumettre des tâches MATLAB parallèles à partir de l’interface MATLAB locale de votre ordinateur.

!!! warning "Avertissement"
    **Certaines améliorations à la sécurité des nos grappes ont été apportées en mai 2023 et, étant donné que MATLAB utilise un mode SSH qui n'est plus autorisé, il n'est plus possible de soumettre une tâche à partir d'un ordinateur local aussi longtemps que MATLAB n'utilisera pas une nouvelle méthode pour se connecter. Il n'y a présentement aucune solution.**

### Module d'extension pour Slurm

!!! warning "Avertissement"
    **La procédure suivante ne fonctionne pas en raison de l'extension Slurm qui n'est plus disponible et aussi du problème avec SSH qui est mentionné à la section précédente.** Toutefois, nous l'avons conservée pour lorsque la solution sera disponible.

1.  Installez MATLAB R2022a (ou une version plus récente), incluant le **Parallel Computing Toolbox**.
2.  De la [page MathWorks Slurm Plugin](https://www.mathworks.com/solutions/cluster-and-cloud-computing/slurm-plugin.html), téléchargez et exécutez le fichier `*.mlpkginstall` (bouton *Download* à la droite de la page, sous l'onglet *Overview*).
3.  Entrez vos identifiants MathWorks. Si la configuration ne démarre pas automatiquement, lancez dans MATLAB la commande :
    ```matlab
    parallel.cluster.generic.runProfileWizard()
    ```
4.  Entrez les renseignements suivants :
    *   Sélectionnez **Unix** (habituellement la seule option offerte)
    *   Shared location : **Non**
    *   Cluster host :
        *   Pour Narval : **narval.alliancecan.ca**
        *   Pour Rorqual : **rorqual.alliancecan.ca**
    *   Nom d'utilisateur (facultatif) : (entrez votre nom d’utilisateur; au besoin, le fichier d’identité peut être défini plus tard)
    *   Emplacement de stockage distant des tâches : **`/scratch`**
        *   Cochez *Utiliser des sous-dossiers uniques*.
    *   Nombre maximal de *workers* : **960**
    *   Dossier d'installation de MATLAB pour les *workers* : (les versions locale et distante doivent correspondre)
        *   Pour R2022a : **`/cvmfs/restricted.computecanada.ca/easybuild/software/2020/Core/matlab/2022a`**
    *   Type de licence : **Gestionnaire de licences réseau**
    *   Nom du profil : **narval** ou **rorqual**
5.  Cliquez sur *Créer* et *Terminer* pour compléter le profil.

### Modifier l'extension après son installation
Dans le terminal MATLAB, allez au répertoire `nonshared` en lançant la commande :

```matlab
cd(fullfile(matlabshared.supportpkg.getSupportPackageRoot, 'parallel', 'slurm', 'nonshared'))
```

1.  Ouvrez le fichier **independentSubmitFcn.m**; aux environs de la ligne 117, remplacez :
    ```matlab
    additionalSubmitArgs = sprintf('--ntasks=1 --cpus-per-task=%d', cluster.NumThreads);
    ```
    par :
    ```matlab
    additionalSubmitArgs = ccSBATCH().getSubmitArgs();
    ```
2.  Ouvrez le fichier **communicatingSubmitFcn.m**; aux environs de la ligne 126, remplacez :
    ```matlab
    additionalSubmitArgs = sprintf('--ntasks=%d --cpus-per-task=%d', environmentProperties.NumberOfTasks, cluster.NumThreads);
    ```
    par :
    ```matlab
    additionalSubmitArgs = ccSBATCH().getSubmitArgs();
    ```
3.  Ouvrez le fichier **communicatingJobWrapper.sh**; aux environs de la ligne 20 (après la déclaration du copyright), ajoutez la commande suivante et ajustez la version du module en fonction de la version de votre Matlab local :
    ```bash
    module load matlab/2022a
    ```

Redémarrez MATLAB et retournez à votre répertoire /home avec :
`cd(getenv('HOME'))` # ou sous Windows, `cd(getenv('HOMEPATH'))`

### Validation
**N'utilisez pas** l'outil de validation *Cluster Profile Manager*, mais exécutez l'exemple `TestParfor` avec un fichier de script `ccSBATCH.m` adéquatement configuré.
1.  Téléchargez et extrayez des exemples de code à partir de [https://github.com/ComputeCanada/matlab-parallel-server-samples](https://github.com/ComputeCanada/matlab-parallel-server-samples).
2.  Dans MATLAB, ouvrez le répertoire `TestParfor` que vous venez d'extraire.
3.  Suivez les directives données dans le fichier [https://github.com/ComputeCanada/matlab-parallel-server-samples/blob/master/README.md](https://github.com/ComputeCanada/matlab-parallel-server-samples/blob/master/README.md).

Note : Quand `ccSBATCH.m` se trouve dans votre répertoire courant, vous pouvez utiliser l’outil de validation *Cluster Profile Manager* pour les deux premiers tests car les autres ne sont pas encore pris en charge.

## Ressources externes

Voyez aussi les ressources offertes par MathWorks.
* Documentation : [https://www.mathworks.com/help/matlab/](https://www.mathworks.com/help/matlab/) (certaines pages sont en français)
* Auto-apprentissage : [https://matlabacademy.mathworks.com/](https://matlabacademy.mathworks.com/) (aussi en versions EN, JP, ES, KR, CN)

Certaines universités ont leur propre documentation, comme :
* pour des exemples de scripts : [https://rcs.ucalgary.ca/MATLAB](https://rcs.ucalgary.ca/MATLAB)