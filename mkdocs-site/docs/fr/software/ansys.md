---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "0c250b6843f99dfbf7896bbf89199136"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:18:55.394291+00:00"

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

!!! attention "Note du traducteur de juillet 2026 : Cette page est présentement en cours de révision."

[Ansys](http://www.ansys.com/) est une suite logicielle pour la simulation d'ingénierie et la conception 3D. Elle comprend des progiciels tels que [Ansys Fluent](https://www.ansys.com/products/fluids/ansys-fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

# Licences

L'Alliance est un fournisseur d'hébergement pour Ansys. Cela signifie que nous avons le logiciel installé sur nos grappes, mais nous ne fournissons pas de licence générique accessible à tout le monde. Cependant, de nombreuses institutions, facultés et départements possèdent déjà des licences qui peuvent être utilisées sur nos grappes. Une fois les aspects juridiques concernant les licences réglés, il restera des aspects techniques. Le serveur de licences de votre côté devra être accessible par nos nœuds de calcul. Cela nécessitera que notre équipe technique prenne contact avec les personnes techniques qui gèrent votre logiciel de licence. Dans certains cas, cela a déjà été fait. Vous devriez alors pouvoir charger le module Ansys, et il devrait trouver sa licence automatiquement. Si ce n'est pas le cas, veuillez contacter notre [soutien technique](../support/technical_support.md) pour prendre les dispositions nécessaires.

## Configurer votre fichier de licence

Notre module Ansys est conçu pour chercher les informations de licence à quelques endroits. L'un de ces endroits est votre répertoire `/home`. Vous pouvez spécifier votre serveur de licences en créant un fichier nommé `$HOME/.licenses/ansys.lic`, comme illustré ci-dessous. Personnalisez le fichier en remplaçant FLEXPORT et LICSERVER par les valeurs appropriées pour votre serveur.

```bash
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@**LICSERVER**")
```

Le tableau suivant fournit les valeurs établies pour le serveur de licences SHARCNET.

| Licence | Système/Grappe                 | LICSERVER                  | FLEXPORT | REMARQUES               |
| :------ | :----------------------------- | :------------------------- | :------- | :---------------------- |
| SHARCNET | Nibi/Fir/Narval/Rorqual/Trillium | `license1.computecanada.ca` | `1055`   | actuellement opérationnel |

### Serveurs de licences locaux

Avant qu'un serveur de licences Ansys institutionnel local puisse être utilisé sur nos grappes, des changements au pare-feu devront être effectués du côté du serveur et du côté de la grappe. Pour de nombreux serveurs Ansys, ce travail a déjà été fait et ils peuvent être utilisés en suivant les étapes de la section [Prêt à l'emploi](#prêt-à-lemploi) ci-dessous. Pour les serveurs Ansys qui n'ont jamais été utilisés sur nos grappes, une étape supplémentaire doit être effectuée, comme indiqué dans la section [Configuration requise](#configuration-requise) ci-dessous.

#### Prêt à l'emploi

Pour utiliser un serveur de licences Ansys institutionnel local avec une grappe de l'Alliance dont les connexions réseau/pare-feu ont déjà été configurées, contactez votre administrateur de serveur Ansys et obtenez les informations suivantes pour le serveur de licences :
1.  Le numéro de port flexible Ansys (FLEXPORT), communément 1055.
2.  Le nom d'hôte entièrement qualifié (LICSERVER).
Maintenant, configurez votre fichier `~/.licenses/ansys.lic` en y insérant ces valeurs, et c'est tout.

#### Configuration requise

Pour utiliser un serveur de licences Ansys local avec une grappe de l'Alliance dont les connexions réseau/pare-feu n'ont jamais été configurées auparavant, vous devrez également obtenir de votre administrateur de serveur Ansys :
3.  Le numéro de port vendeur Ansys (VENDPORT) configuré statiquement.
Envoyez les éléments 1 à 3 par courriel au [soutien technique](../support/technical_support.md) et mentionnez sur quelle grappe de l'Alliance vous souhaitez exécuter des tâches Ansys. Un administrateur système de l'Alliance ouvrira alors le pare-feu sortant de la grappe (si nécessaire) afin que les requêtes d'extraction de licences puissent atteindre votre serveur de licences depuis les nœuds de calcul de la grappe. Une plage d'adresses IP (appelées nœuds NAT de la grappe) vous sera ensuite renvoyée. Donnez ces adresses IP à votre administrateur réseau local et demandez que les ports FLEXPORT et VENDPORT du pare-feu du serveur local soient ouverts pour permettre les connexions depuis toutes ces adresses. Demandez également à l'administrateur de vérifier que la ligne contenant `SERVER <servername> <host id> <lmgrd port>`, trouvée en haut du fichier de licence Ansys, contient soit LICSERVER, soit IP_ADDRESS pour la valeur `<servername>`, car celle-ci doit être résoluble depuis la grappe distante.

## Vérifier une licence

Pour vérifier si votre fichier `ansys.lic` est configuré et fonctionne correctement avec votre serveur de licences, exécutez la séquence de commandes suivante sur la grappe où vous soumettrez vos tâches.

```bash
[login-node:~] cd /tmp
[login-node:/tmp] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[compute-node/tmp] module load StdEnv/2023; module load ansys/2025R2.04
[compute-node:/tmp] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Succès || echo Échec
```
La sortie `Succès` indique que les extractions de licences devraient fonctionner lorsque les tâches sont soumises à la file d'attente.
La sortie `Échec` indique un problème avec la configuration des licences, et les tâches échoueront probablement.

S'il y a un problème d'extraction de licence du serveur Ansys, le message suivant apparaîtra dans les fichiers de sortie Slurm lorsque les tâches Fluent sont démarrées par des scripts Slurm dans la file d'attente *OU* lorsque Fluent est démarré de manière interactive, simplement en procédant comme suit :

```bash
[compute-node:/tmp] fluent -g 2d -n 2
 Connected License Server List:	<Shared_Web_License_Server>
 Appuyez sur Entrée pour quitter.
```

# Compatibilité des versions

Les simulations Ansys sont généralement compatibles vers l'avant, mais **PAS** compatibles vers l'arrière. Cela signifie que l'on peut s'attendre à ce que les simulations créées avec une version plus ancienne d'Ansys se chargent et s'exécutent sans problème avec toute version plus récente. Par exemple, une simulation créée et enregistrée avec `ansys/2022R2` devrait se charger et s'exécuter sans problème avec `ansys/2023R2`, mais **PAS** l'inverse. Bien qu'il soit possible de lancer une simulation avec une version plus ancienne, des messages d'erreur aléatoires ou des plantages surviendront probablement. Concernant les simulations Fluent, si vous ne vous souvenez plus de la version d'Ansys utilisée pour créer votre fichier de cas, essayez de le `grep`per comme suit pour trouver des indices :

```bash
$ grep -ia fluent combustor.cas
   (0 "fluent15.0.7  build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
   ANSYS_FLUENT 24.1 Build 1018
```

## Prise en charge des plateformes

Ansys fournit des [informations détaillées sur la prise en charge des plateformes](https://www.ansys.com/it-solutions/platform-support/previous-releases) décrivant la compatibilité logicielle/matérielle pour les versions actuelles et précédentes. Ceci est d'un intérêt particulier car cela indique quels progiciels sont pris en charge sous Windows, mais pas sous Linux, et donc pas sur les grappes de l'Alliance (par exemple, SpaceClaim).

## Nouveautés

L'information sur la dernière version d'Ansys peut être trouvée [ici](https://www.ansys.com/products/release-highlights) (Ansys 2026 R1, en date de mai 2026). Les publications concernant les versions précédentes peuvent être trouvées sur le [blogue Ansys](https://www.ansys.com/blog) en faisant défiler jusqu'à la barre de recherche FILTRES. Saisir par exemple *What’s New Fluent 2024 GPU* devrait faire apparaître un document contenant les dernières informations sur le support GPU pour cette version. La barre de recherche [Communiqués de presse](https://www.ansys.com/news-center/press-releases) est aussi un bon moyen de trouver des informations spécifiques à une version.

## Lots de services

À partir d'Ansys 2024, un module Ansys distinct apparaîtra sur les grappes avec une décimale et deux chiffres suivant le numéro de version chaque fois qu'un lot de services est installé sur la version initiale. Par exemple, la version initiale 2024 sans lot de services appliqué peut être chargée avec `module load ansys/2024R1`, tandis qu'un module avec le lot de services 3 appliqué sera chargé avec `module load ansys/2024R1.03`. Si un lot de services est déjà disponible au moment où une nouvelle version doit être installée, seul un module pour ce numéro de lot de services sera très probablement installé, à moins qu'une demande d'installation de la version initiale ne soit également reçue.

La plupart des utilisateurs voudront probablement charger la dernière version du module, munie du dernier lot de services installé, ce qui peut être fait avec `module load ansys`. Bien qu'il ne soit pas prévu que les lots de services aient un impact sur les résultats numériques, les changements qu'ils apportent sont étendus et donc, si des calculs ont déjà été effectués avec la version initiale ou un lot de services antérieur, certains groupes pourraient préférer continuer à l'utiliser. Avoir des modules distincts pour chaque lot de services rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que chaque lot de services apporte peut être trouvée en cherchant *Service Pack Details* dans ce [lien](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf). Les futures versions seront vraisemblablement recherchables de manière similaire en modifiant manuellement le numéro de version.

# Soumission de tâches par lots sur la grappe

Soumission de tâches par lots sur la grappe avec Ansys

# Utilisation graphique

[Utilisation graphique d'Ansys](../general/graphical_use_of_ansys.md)

# Utilisation spécifique au site

## Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour une utilisation académique par **tout** chercheur de l'Alliance sur **tout** système de l'Alliance. Le logiciel installé n'a aucune limite de solveur ou de géométrie. La licence SHARCNET peut être utilisée pour la ***Recherche Académique Publiable***, mais pas à des fins privées/commerciales, car cela est strictement interdit par les termes de la licence. La licence Ansys de SHARCNET est basée sur la solution Multiphysics Campus et comprend des produits tels que : HF, EM, Electronics HPC, Mechanical, CFD, ROCKY et LS-DYNA comme décrit [ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Le logiciel Lumerical est inclus dans les versions récentes des modules Ansys, mais il N'EST PAS couvert par la licence SHARCNET. Le logiciel SpaceClaim n'est pas installé avec les modules Ansys car il n'existe pas de version Linux ; il est cependant techniquement couvert par la licence SHARCNET.

!!! tip "Tests de mise à l'échelle"
    Des tests de mise à l'échelle devraient être effectués avant de lancer des tâches longues afin de déterminer la taille optimale et évolutive de la tâche, de sorte que les licences et le matériel limités soient utilisés aussi efficacement que possible, et que les temps d'exécution totaux et de démarrage des tâches soient minimisés. Les tâches parallèles qui n'atteignent pas au moins 50 % d'utilisation du CPU seront probablement signalées par le système, ce qui entraînera un suivi par un membre de l'équipe de l'Alliance.

#### Limites de licence

La licence Ansys de SHARCNET est disponible selon le principe du premier arrivé, premier servi. Elle permet actuellement à chaque chercheur d'exécuter un maximum de 16 tâches simultanées utilisant un total de 512 cœurs HPC sur toutes les grappes. Par conséquent, l'une des combinaisons de taille de tâche maximale suivantes peut être exécutée simultanément : 1x512, 2x256, 4x128, 8x64, 16x32 ou, plus communément, l'une de ces combinaisons de nœuds complets : 1x384, 2x192 ou 1x192 cœurs. Notez cependant que la licence SHARCNET est sur-souscrite, il est donc possible que les tâches échouent au démarrage si toutes (ou presque toutes) les 1986 licences `anshpc` du pool de licences SHARCNET sont utilisées. Si cela se produit, vous devrez soumettre à nouveau manuellement votre tâche à la file d'attente. Comme il y a eu un nombre croissant d'instances de pénurie de licences (REFUSÉ) où les tâches échouent au démarrage, la limite totale de cœurs `anshpc` par chercheur sera réduite de 512 à 384 le 1er avril 2026. Si vous avez besoin d'utiliser plus de 384 cœurs HPC pour votre recherche, utilisez le serveur de licences Ansys local de votre institution s'il en existe un, OU ouvrez un billet pour demander l'achat de licences supplémentaires pour la licence SHARCNET, celles-ci étant alors réservées à votre usage exclusif ou à celui de votre groupe.

#### Fichier de licence

En date de février 2026, le serveur de licences `license3.sharcnet.ca` a été définitivement fermé. Pour utiliser la licence Ansys de SHARCNET sur n'importe quelle grappe de l'Alliance, configurez simplement votre fichier `ansys.lic` comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license1.computecanada.ca")
```

#### Requête de licence

Pour afficher le nombre de licences Ansys utilisées par votre nom d'utilisateur et le total utilisé par tous les utilisateurs, exécutez la commande :

```bash
ssh nibi.alliancecan.ca
module load ansys
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil \
lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
```

#### Exemple

Considérons le cas où un utilisateur soumet une tâche Fluent de 8 cœurs et une tâche Fluent de 32 cœurs. Une fois les deux tâches en cours d'exécution, l'utilisateur exécute la commande de requête `lmutil` et la sortie ci-dessous est générée. Ici, nous voyons qu'un total de (8-4) + (32-4) = 32 licences `anshpc` sont utilisées par les deux tâches. En conséquence, le nombre total de licences passe de 1568 à 1600, de sorte que seulement (1986-1600) = 386 d'entre elles restent disponibles pour des tâches supplémentaires soumises par tous les utilisateurs. Par conséquent, si une tâche parallèle de 400 cœurs tente de démarrer à ce moment-là, elle échouera car (400-4) = 396 licences `anshpc` seraient nécessaires. L'utilisateur a deux options : soit attendre qu'un nombre suffisant de licences devienne disponible, SOIT réduire la taille de la tâche à 390 cœurs ou moins et la soumettre à nouveau immédiatement. Cet exemple se concentre sur la fonctionnalité `anshpc` car elle est la plus généreusement sur-souscrite pour permettre à tout utilisateur de soumettre la plus grande tâche possible, mais il montre également que le nombre réel de licences disponibles par utilisateur peut parfois être bien inférieur à ce que la limite de 512 par utilisateur suggérerait.

```bash
 [l2(nibi):~] sq
            JOBID     USER        ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS MIN_MEM NODELIST (REASON) 
         10161023  roberpj   cc-debug_cpu script-flu-int   R    2:57:19     4    8     N/A      4G c[630-633] (None) 
         10161033  roberpj   cc-debug_cpu script-flu-int   R    2:58:25    16   32     N/A      4G c[627-628,630-633,637,642,645,655,657,662,665,667,669,682] (None) 
 [l2(nibi):~]
 [l2(nibi):~] module load ansys
 [l2(nibi):~]
 [l2(nibi):~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil  \
              lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
 Users of anshpc:  (Total of 1986 licenses issued;  Total of 1600 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 2579), start Wed 3/11 16:46, 4 licenses, PID: 1239140 
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 5716), start Wed 3/11 16:48, 28 licenses, PID: 510058 
 Users of cfd_base:  (Total of 275 licenses issued;  Total of 19 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10327), start Wed 3/11 16:46, PID: 1239140 
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 7171), start Wed 3/11 16:47, PID: 510058 
 Users of cfd_preppost:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of cfd_preppost_pro:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of cfd_solve_level1:  (Total of 275 licenses issued;  Total of 18 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 7994), start Wed 3/11 16:46, PID: 1239140 
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 6200), start Wed 3/11 16:47, PID: 510058 
 Users of cfd_solve_level2:  (Total of 275 licenses issued;  Total of 18 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10520), start Wed 3/11 16:46, PID: 1239140 
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 375), start Wed 3/11 16:47, PID: 510058 
 Users of elec_solve_hfss:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of elec_solve_level1:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of elec_solve_level2:  (Total of 275 licenses issued;  Total of 1 license in use)
```

!!! attention "Processus Ansys fantômes"
    Une situation rare peut se produire où la sortie de la commande de requête de licence révèle que des licences Ansys sont toujours utilisées inopinément par votre nom d'utilisateur sur un nœud de bureau ou de calcul. Cela se produirait si, par exemple, un programme Ansys GUI exécuté sur un nœud de bureau distant n'a pas été fermé proprement, laissant des processus Ansys toujours en cours d'exécution, ou si un programme Ansys plante sur un nœud de calcul de grappe à l'intérieur d'une session `salloc` exécutée de manière interactive depuis la ligne de commande, laissant encore une fois des processus Ansys « voyous » en cours d'exécution. Pour tuer tous les processus Ansys « voyous » potentiellement responsables, fermez le bureau, `scancel` la session `salloc`, ou ouvrez simplement une fenêtre de terminal sur le nœud affecté et émettez la commande `pkill -9 -e -u $USER -f "ansys"`. Toutes les licences Ansys qui étaient maintenues ouvertes devraient être immédiatement retournées au serveur de licences SHARCNET et redevenir disponibles pour votre usage ou celui d'autres chercheurs.

# Fabrication additive

Pour commencer, configurez votre fichier `~/.licenses/ansys.lic` pour qu'il pointe vers un serveur de licences possédant une licence Ansys Mechanical valide. Ceci doit être fait sur tous les systèmes où vous comptez exécuter le logiciel.

## Activer la fabrication additive

Cette section décrit comment rendre l'extension ACT de fabrication additive d'Ansys disponible pour utilisation dans votre projet. Les étapes doivent être effectuées sur chaque grappe pour chaque version du module Ansys où l'extension sera utilisée. Toutes les extensions nécessaires à votre projet devront également être installées sur la grappe comme décrit ci-dessous. Si vous recevez des avertissements concernant des extensions manquantes non nécessaires (comme ANSYSMotion), désinstallez-les de votre projet.

### Télécharger les extensions

*   Téléchargez `AdditiveWizard.wbex` depuis [https://catalog.ansys.com/](https://catalog.ansys.com/).
*   Téléchargez (ou transférez) `AdditiveWizard.wbex` sur la grappe où il sera utilisé.

### Démarrer Workbench

*   Suivez la section [Utilisation graphique](../general/graphical_use_of_ansys.md) ci-dessus pour Workbench.
*   Cliquez sur *Fichier -> Ouvrir* votre fichier de projet (se terminant par `.wbpj`) dans l'interface graphique de Workbench.

### Ouvrir le gestionnaire d'extensions

*   Cliquez sur la page de démarrage d'ACT et l'onglet de la page d'accueil d'ACT s'ouvrira.
*   Cliquez sur *Gérer les extensions* et le gestionnaire d'extensions s'ouvrira.

### Installer les extensions

*   Cliquez sur la boîte avec le grand signe `+` sous la barre de recherche.
*   Naviguez pour sélectionner et installer votre fichier `AdditiveWizard.wbex`.

### Charger les extensions

*   Cliquez pour sélectionner la boîte *AdditiveWizard* (charge l'extension AdditiveWizard pour la session actuelle seulement).
*   Cliquez sur la flèche du coin inférieur droit de la boîte *AdditiveWizard* et sélectionnez *Charger l'extension* (charge l'extension pour les sessions actuelle ET futures).

### Décharger les extensions

*   Cliquez pour désélectionner la boîte *AdditiveWizard* (décharge l'extension pour la session actuelle seulement).
*   Cliquez sur la flèche du coin inférieur droit de la boîte *AdditiveWizard* et sélectionnez *Ne pas charger par défaut* (l'extension ne se chargera pas pour les sessions futures).

## Exécuter Additive

### Sur demande (OnDemand)

Vous pouvez exécuter une seule tâche de fabrication additive Ansys dans une session graphique Sur demande (OnDemand) en suivant ces étapes :

*   Démarrez Workbench comme décrit ci-dessus dans [Activer la fabrication additive](#activer-la-fabrication-additive).
*   Cliquez sur *Fichier -> Ouvrir*, sélectionnez *test.wbpj* et cliquez sur *Ouvrir*.
*   Cliquez sur *Affichage -> réinitialiser l'espace de travail* si vous obtenez un écran gris.
*   Démarrez Mechanical, effacez les données générées, cochez *Distribué*, spécifiez les cœurs.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

**Vérifier l'utilisation**
*   Ouvrez un autre terminal et exécutez `top -u $USER` **OU** `ps u -u $USER | grep ansys`.
*   Tuez les processus « voyous » des exécutions précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que les processus « voyous » liés à Ansys peuvent bloquer de manière persistante de précieuses licences à l'intérieur d'une session de nœud de connexion OnDemand en cours d'exécution si une session GUI Ansys (Fluent, Workbench, Mechanical, etc.) n'est pas proprement terminée ou est terminée de manière inattendue par une panne réseau ou un système de fichiers bloqué. Si ce dernier est en cause, les processus pourraient ne pas être tuables tant que l'accès normal au disque n'est pas restauré.

### Grappe

**Préparation du projet**

Avant de soumettre un projet Additive nouvellement téléchargé à une file d'attente de grappe (avec `sbatch scriptname`), certaines préparations doivent être effectuées. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (tel que décrit dans la section [Activer la fabrication additive](#activer-la-fabrication-additive) ci-dessus) dans le même répertoire à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisée pour la tâche. Ensuite, créez un script Slurm (tel qu'expliqué dans la section Soumission de tâches par lots sur la grappe - WORKBENCH ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** à recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1) remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)`, soit 2) enregistrez une copie du fichier `YOURPROJECT.wbpj` original et du répertoire `YOURPROJECT_files` correspondant. Optionnellement, créez puis exécutez manuellement un fichier de relecture sur la grappe dans le répertoire du cas de test respectif entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne `FilePath`.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

**Utilisation des ressources**

Une fois que votre tâche Additive a été exécutée pendant quelques minutes, un instantané de son utilisation des ressources sur le(s) nœud(s) de calcul peut être obtenu avec la commande `srun`. Un exemple de sortie correspondant à un script de soumission de huit cœurs est présenté ci-après. Nous voyons que deux nœuds ont été sélectionnés par l'ordonnanceur :

```bash
[gra-login1:~] srun --overlap --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
 22843 demo   20   0 2272124 256048  72796 R  88.0  0.2  1:06.24  ansys.e
 22849 demo   20   0 2272118 256024  72822 R  99.0  0.2  1:06.37  ansys.e
 22838 demo   20   0 2272362 255086  76644 R  96.0  0.2  1:06.37  ansys.e
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
  4310 demo   20   0 2740212 271096 101892 R 101.0  0.2  1:06.26  ansys.e
  4311 demo   20   0 2740416 284552  98084 R  98.0  0.2  1:06.55  ansys.e
  4304 demo   20   0 2729516 268824 100388 R 100.0  0.2  1:06.12  ansys.e
  4305 demo   20   0 2729436 263204 100932 R 100.0  0.2  1:06.88  ansys.e
  4306 demo   20   0 2734720 431532  95180 R 100.0  0.3  1:06.57  ansys.e
```

*Tests de mise à l'échelle*

Une fois la tâche terminée, son temps d'horloge (wall-clock time) peut être obtenu avec `seff myjobid`. En utilisant cette valeur, des tests de mise à l'échelle peuvent être effectués en soumettant de courtes tâches de test avec un nombre croissant de cœurs. Si le temps d'horloge diminue d'environ 50 % lorsque le nombre de cœurs est doublé, des cœurs supplémentaires peuvent être envisagés.

# Ressources d'aide

La documentation officielle complète pour les versions récentes d'Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles qu'Ansys 2023R[1|2] nécessite cependant une [connexion](https://ansyshelp.ansys.com/login). La documentation pour développeurs se trouve sur le [portail des développeurs Ansys](https://developer.ansys.com). Des ressources d'apprentissage supplémentaires incluent les [vidéos Ansys HowTo](https://www.youtube.com/@AnsysHowTo/videos), le [hub des éducateurs Ansys](https://innovationspace.ansys.com/educator-hub/) et la [série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

!!! attention "Note héritée X sur SSH"
    Certains programmes peuvent être exécutés à distance sur un nœud de calcul de grappe en redirigeant X via SSH vers votre bureau local. Contrairement à VNC, cette approche n'est pas testée et n'est pas prise en charge car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que MobaXterm. La plupart des utilisateurs trouveront les temps de réponse interactifs inacceptablement lents pour les tâches de menu de base, sans parler des tâches plus complexes comme celles impliquant le rendu graphique. Les temps de démarrage pour les programmes GUI peuvent également être très lents selon votre connexion Internet. Par exemple, lors d'un test, il a fallu 40 minutes pour démarrer complètement l'interface graphique via SSH, alors que le démarrage avec vncviewer n'a pris que 34 secondes. Malgré la lenteur potentielle, l'utilisation de cette méthode de connexion peut toujours être intéressante si votre seul objectif est d'ouvrir une simulation et d'effectuer quelques opérations de menu de base ou d'exécuter quelques calculs, et que les délais de réponse peuvent être tolérés. Les étapes de base sont données ici comme point de départ :
    1.  `ssh -Y username@alliancecan.ca`
    2.  `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task=4 [--gpus-per-node=1] --account=def-mygroup;`
    3.  Une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, procédez au chargement du module Ansys souhaité et essayez d'exécuter le programme.