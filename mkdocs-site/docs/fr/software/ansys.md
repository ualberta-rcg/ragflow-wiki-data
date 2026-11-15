---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "c9dd33da7dce8deef598290f511d3c77"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:22:36.980733+00:00"

tags:
  - software

keywords:
  - "c630"
  - "support technique"
  - "lmutil lmstat"
  - "YOURPROJECT_files"
  - "licences Ansys"
  - "Total of 1986 licenses issued"
  - "ports VENDPORT"
  - "pkill -9 -e -u $USER -f \"ansys\""
  - "utilisation des ressources"
  - "ansys.lic"
  - "extensions nécessaires"
  - "XoverSSH"
  - "installation"
  - "Gestionnaire d'extensions"
  - "suite logicielle Ansys"
  - "avertissements"
  - "plateformes prises en charge"
  - "limite totale de cœurs Ansys"
  - "utilisation des licences"
  - "lmutil"
  - "module load ansys/2024R1"
  - "384 cœurs"
  - "version initiale"
  - "documentation Ansys"
  - "grappes"
  - "module load ansys"
  - "ports FLEXPORT"
  - "port FLEXPORT"
  - "Total of 1600 licenses in use"
  - "service pack"
  - "Chargement de l'extension"
  - "Save (Overwrite=False)"
  - "licences anshpc"
  - "roberpj"
  - "tests de scalabilité"
  - "licence ansys"
  - "serveur de licence local"
  - "adresses IP"
  - "limite de 512 cœurs"
  - "license SHARCNET"
  - "Exécution OnDemand"
  - "Script Slurm"
  - "versions de module Ansys"
  - "fichier de relecture"
  - "compatibilité des versions"
  - "license1.computecanada.ca"
  - "paramètre interne FilePath"
  - "administrateur réseau"
  - "extension Additive Manufacturing"
  - "fichier de licence ansys.lic"
  - "demande"
  - "serveur de licences Ansys local"
  - "nombre de licences"
  - "cfd_base"
  - "AdditiveWizard.wbex"
  - "désinstaller les extensions inutiles"
  - "YOURPROJECT.wbpj"
  - "refus de licences (DENIED)"
  - "licences SHARCNET supplémentaires"
  - "fichier de licence Ansys"
  - "srun"
  - "licence SHARCNET"

questions:
  - "Quels sont les prérequis techniques pour que les nœuds de calcul puissent communiquer avec le serveur de licence Ansys ?"
  - "Comment doit‑on configurer le fichier « $HOME/.licenses/ansys.lic » pour utiliser un serveur de licence local ?"
  - "Quelles démarches supplémentaires sont nécessaires si le pare‑feu n’est pas encore configuré entre la grappe et le serveur de licence ?"
  - "Quels ports du pare‑feu du serveur local devez‑vous demander à votre administrateur d’ouvrir pour les adresses IP fournies ?"
  - "Quelle information doit contenir la ligne « SERVER <servername> <host id> <lmgrd port> » du fichier de licence Ansys pour être reconnue par la grappe distante ?"
  - "Pourquoi est‑il nécessaire de transmettre les adresses IP à l’administrateur réseau et de vérifier la configuration du serveur dans le fichier de licence ?"
  - "Comment vérifier que le fichier ansys.lic est correctement configuré et fonctionnel sur le nœud de calcul ?"
  - "Quelle est la règle de compatibilité entre les versions antérieures et ultérieures d’Ansys/Fluent pour charger et exécuter des simulations ?"
  - "Comment charger un module Ansys avec un service pack spécifique (par ex. 2024R1.03) et où trouver les informations sur les plateformes supportées et les nouveautés de chaque version ?"
  - "Comment charger une version spécifique d’Ansys avec un service pack particulier au lieu de la version la plus récente ?"
  - "Quelles sont les restrictions d’utilisation de la licence SHARCNET Ansys concernant les activités académiques et commerciales ?"
  - "Quels sont les plafonds actuels de cœurs et de tâches pour la licence SHARCNET, et quelles démarches suivre en cas de refus de licence ou de besoin de plus de cœurs ?"
  - "Comment charger la version initiale d’Ansys 2024 sans aucun service pack ?"
  - "Quelle commande utilise‑t‑on pour charger un module Ansys avec un service pack précis, comme le service pack 3 ?"
  - "Que se passe‑t‑il lorsqu’un service pack est déjà disponible au moment de l’installation d’une nouvelle version d’Ansys ?"
  - "Quelle sera la nouvelle limite maximale de cœurs Ansys par chercheur à partir du 1er avril 2026 ?"
  - "Quelle est la cause invoquée pour la réduction du nombre de cœurs autorisés ?"
  - "Quelles options sont proposées aux chercheurs qui ont besoin de plus de 384 cœurs ?"
  - "Quel fichier de licence doit‑être configuré et quelle variable d’environnement doit‑elle contenir pour utiliser la licence SHARCNET depuis février 2026 ?"
  - "Quelle commande permet d’afficher le nombre de licences Ansys utilisées par votre nom d’utilisateur ainsi que le total des licences en cours d’utilisation ?"
  - "Dans l’exemple fourni, comment le nombre de licences nécessaires est‑il calculé pour les deux tâches Fluent de 8 cœurs et 32 cœurs, et quelles options l’utilisateur a‑t‑il lorsque la tâche parallèle de 400 cœurs échoue ?"
  - "How many total licenses have been issued and how many are currently in use according to the report?"
  - "Which user and host combination is listed with the highest number of licenses allocated, and how many licenses does it have?"
  - "What is the purpose of the `grep -v \" Total of 0 licenses in use\"` command at the beginning of the output?"
  - "What does the license usage report reveal about the total number of licenses issued versus those currently in use for each Ansys module listed (e.g., cfd_base, cfd_solve_level1, elec_solve_hfss)?"
  - "According to the French instructions, what commands or actions should a user take to terminate lingering Ansys processes that are unintentionally holding licenses?"
  - "What configuration steps are necessary to set up the Ansys Additive Manufacturing ACT extension on the clusters, including any required license file adjustments and module installations?"
  - "Quelles sont les étapes à suivre pour chaque version du module Ansys sur chaque grappe où l'extension sera utilisée ?"
  - "Comment installer les extensions requises pour le projet sur les grappes, conformément aux instructions décrites ?"
  - "Que doit‑on faire lorsqu’on reçoit des avertissements indiquant l'absence d'extensions inutiles, comme ANSYSMotion ?"
  - "Quelles sont les étapes à suivre pour télécharger, installer et charger l’extension AdditiveWizard.wbex dans l’interface Workbench ?"
  - "Comment lancer et surveiller l’exécution d’une tâche Additive Manufacturing en mode OnDemand, notamment la gestion des processus et des licences ?"
  - "Quels sont les préparatifs requis et les réglages à appliquer dans le script Slurm pour soumettre correctement un projet Additive sur une grappe ?"
  - "Quelle modification faut‑il apporter à l’appel <code>Save</code> pour empêcher l’écrasement du fichier ?"
  - "Comment sauvegarder une copie du fichier <code>YOURPROJECT.wbpj</code> ainsi que du répertoire <code>YOURPROJECT_files</code> associé ?"
  - "Comment réutiliser un même fichier de relecture dans différents répertoires de cas de test en modifiant le paramètre <code>FilePath</code> ?"
  - "Comment obtenir et interpréter un instantané de l’utilisation des ressources d’une tâche Ansys avec la commande srun ?"
  - "Quelle méthode suivre pour réaliser des tests de scalabilité d’un job Ansys et quels critères de réduction du temps d’exécution doivent être observés ?"
  - "Quels sont les avantages et les limites de l’utilisation de XoverSSH pour lancer des applications graphiques Ansys sur un nœud de calcul, et quelles sont les étapes de base pour le configurer ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ansys est une suite logicielle pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](https://www.ansys.com/products/fluids/ansys-fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

Voir aussi :
*   Ansys en mode graphique
*   Ansys : Soumettre des tâches en lots

# Licence

La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez l'aspect légal de son utilisation. Pour ce qui est de l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence

Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire `/home`. Pour indiquer votre propre serveur de licence, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient les deux lignes ci-dessous, où vous remplacez FLEXPORT et LICSERVER par les valeurs réelles de votre serveur.

!!! info "Fichier : ansys.lic"
    ```bash
    setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT@LICSERVER**")
    ```

Les valeurs correspondant au serveur de licence SHARCNET se trouvent dans le tableau ci-dessous.

| Licence   | Système/Grappe            | LICSERVER                 | FLEXPORT | REMARQUES |
| :-------- | :------------------------ | :------------------------ | :------- | :-------- |
| SHARCNET  | Nibi/Fir/Narval/Rorqual/Trillium | `license1.computecanada.ca` | `1055`   | en fonction |

### Serveurs de licence locaux

Avant que le serveur de licence de votre établissement puisse être utilisé avec nos grappes, les pare-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans *Prêt à utiliser* ci-dessous. Autrement, référez-vous à *Étapes additionnelles*.

#### Prêt à utiliser

Pour utiliser un serveur de licences Ansys local de votre établissement dont les connexions réseau/pare-feu sont déjà configurées pour nos grappes, contactez votre administrateur de serveur de licence Ansys et obtenez les deux renseignements suivants :
1.  le numéro de port flexible Ansys configuré (FLEXPORT), généralement 1055,
2.  le nom d'hôte complet (LICSERVER) du serveur de licence.

Configurez ensuite votre fichier `~/.licenses/ansys.lic` en y insérant les valeurs de FLEXPORT et LICSERVER dans le modèle *Fichier : ansys.lic* ci-dessus.

#### Étapes additionnelles

Pour utiliser un serveur de licence Ansys local avec une de nos grappes dont la connexion réseau/pare-feu n'a jamais été configurée, vous devrez également obtenir les informations suivantes auprès de votre administrateur de serveur Ansys :
3.  le numéro de port fournisseur Ansys (VENDPORT) configuré statiquement.

Envoyez les éléments 1 à 3 par courriel au [soutien technique](../support/technical_support.md) en précisant la grappe sur laquelle vous souhaitez exécuter des tâches Ansys. Un administrateur système de l'Alliance ouvrira alors le pare-feu sortant de la grappe (au besoin) afin que les demandes d'obtention de licences puissent atteindre votre serveur depuis les nœuds de calcul de la grappe. Une plage d'adresses IP (appelées nœuds NAT) vous sera ensuite communiquée. Transmettez ces adresses IP à votre administrateur réseau local et demandez-lui d'ouvrir les ports FLEXPORT et VENDPORT du pare-feu du serveur local pour autoriser les connexions pour toutes ces adresses. Demandez également à l'administrateur de vérifier que la ligne contenant `SERVER <servername> <host id> <lmgrd port>` qui se trouve en haut du fichier de licence Ansys contient soit LICSERVER, soit IP_ADDRESS pour la valeur `<servername>`, car celle-ci doit être lisible par la grappe distante.

## Obtenir une licence

Pour vérifier si ansys.lic est bien configuré et fonctionne correctement avec votre serveur de licence, exécutez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches.

```bash
[login-node:~] cd /tmp
[login-node:/tmp] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[compute-node/tmp] module load StdEnv/2023; module load ansys/2025R2.04
[compute-node:/tmp] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```

`Success` indique que la licence devrait pouvoir soumettre des tâches à la file.
`Fail` indique un problème dans la configuration et les tâches vont probablement échouer.

En cas de problème d'obtention de licence auprès du serveur Ansys, le message suivant apparaîtra dans les fichiers de sortie Slurm lorsque des tâches Fluent sont lancées par des scripts Slurm en file d'attente *OU* lorsque Fluent est lancé de manière interactive, en procédant comme suit :

```bash
[compute-node:/tmp] fluent -g 2d -n 2
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

# Compatibilité des versions

Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une moins récente version de Ansys devrait pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec ansys/2022R2 devrait fonctionner avec ansys/2023R2, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
$ grep -ia fluent combustor.cas
   (0 "fluent15.0.7  build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
   ANSYS_FLUENT 24.1 Build 1018
```

# Plateformes prises en charge

Ansys fournit des informations détaillées sur [la compatibilité des plateformes](https://www.ansys.com/it-solutions/platform-support/previous-releases), notamment la compatibilité logicielle et matérielle, pour la version actuelle et les versions précédentes. Ceci est particulièrement utile car on y trouve les logiciels compatibles sous Windows mais pas sous Linux, et donc pas sur l'Alliance (par exemple Spaceclaim).

# Nouveautés

Vous trouverez des informations sur [la dernière version d'Ansys](https://www.ansys.com/products/release-highlights), `Ansys 2026 R1` en date de mai 2026. Les articles relatifs aux versions précédentes sont accessibles sur [la page Ansys](https://www.ansys.com/blog) en faisant défiler la page jusqu'à la barre de recherche FILTRES. Saisir par exemple *What’s New Fluent 2024 gpu* devrait afficher un document contenant les dernières informations sur la prise en charge des GPU par cette version.

# Correctifs

À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un service pack est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun service pack peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le service pack 3 peut être chargé avec `module load ansys/2024R1.03`. Si un service pack est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de service pack sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier service pack installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les service packs aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un service pack antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque service pack rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque service pack se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf); les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien.

# Particularités selon le site d'utilisation

## Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut uniquement être utilisée à des fins de **recherche universitaire publiable**; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Multiphysics Campus Solution en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par Ansys en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET.

!!! tip "Scalabilité des tâches"
    ⚔️ Il est recommandé d'effectuer des tests de scalabilité avant de lancer des longues tâches afin de déterminer la taille optimale de ces tâches. Ceci permettra d'utiliser au mieux les licences et le matériel limités, et de minimiser la durée totale d'exécution et de démarrage. Les tâches parallèles n'atteignant pas au moins 50% d'utilisation de CPU seront probablement signalées par le système, ce qui entraînera une intervention d'un membre de notre équipe.

### Limites

La licence SHARCNET Ansys est attribuée selon le principe du premier arrivé, premier servi. Elle permet d'exécuter simultanément un maximum de 16 tâches, utilisant jusqu'à 512 cœurs répartis sur l'ensemble des grappes. Ainsi, les combinaisons de tailles de tâches suivantes peuvent être exécutées simultanément : 1x512, 2x256, 4x128, 8x64, 16x32, ou plus fréquemment, l'une de ces combinaisons de nœuds complets : 1x384, 2x192 ou 1x192 cœurs. Notez cependant que la licence SHARCNET est surutilisée; il est donc possible que des tâches échouent au démarrage si la totalité (ou la quasi-totalité) des 1 986 licences `anshpc` du pool de licences SHARCNET sont utilisées. Dans ce cas, vous devrez soumettre manuellement votre tâche à nouveau à la file d'attente. En raison de l'augmentation des cas de refus de licences (DENIED) entraînant l'échec des tâches au démarrage, la limite totale de cœurs Ansys par chercheur sera réduite de 512 à 384 le 1er avril 2026. Si vous avez besoin de plus de 384 cœurs pour vos travaux, vous pouvez soit utiliser le serveur de licences Ansys local de votre établissement s'il en dispose, soit ouvrir un billet d'assistance pour demander l'achat de licences SHARCNET supplémentaires. Ces licences seront alors réservées à votre usage personnel ou à celui de votre groupe.

### Fichier de licence

Depuis février 2026, le serveur license3.sharcnet.ca n'est plus en fonction. Pour utiliser la licence de SHARCNET sur une de nos grappes, configurez votre fichier *ansys.lic* comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license1.computecanada.ca")
```

### Licences utilisées

Pour afficher le nombre de licences Ansys utilisées par votre nom d'utilisateur et le nombre total de licences utilisées par tous les utilisateurs, exécutez :

```bash
ssh nibi.alliancecan.ca
module load ansys
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil \
lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
```

### Exemple

Prenons l'exemple d'un utilisateur qui soumet une tâche Fluent de 8 cœurs et une autre de 32 cœurs. Une fois les deux tâches lancées, l'utilisateur exécute la commande `lmutil` et le résultat ci-dessous est généré. On constate que les deux tâches utilisent un total de (8-4)+(32-4)=32 licences `anshpc`. Par conséquent, le nombre total de licences passe de 1568 à 1600, ne laissant disponibles que (1986-1600)=386 licences pour les tâches supplémentaires soumises par d'autres. Ainsi, si une tâche parallèle à 400 cœurs tente de démarrer à ce moment-là, elle échouera, car (400-4)=396 licences `anshpc` seraient nécessaires. L'utilisateur a deux options : soit attendre qu'un nombre suffisant de licences se libère, soit réduire la taille de la tâche à 390 cœurs ou moins et la soumettre à nouveau immédiatement. Cet exemple porte sur la fonctionnalité `anshpc` car elle est surchargée pour permettre à tout utilisateur de soumettre le plus gros travail possible, mais il montre également que le nombre réel de licences disponibles par utilisateur peut parfois être bien inférieur à la limite suggérée de 512 par utilisateur.

```text
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

!!! warning "Licences bloquées"
    🕵️ Il peut arriver, quoique rarement, que la commande de requête de licence révèle que certaines licences Ansys sont encore utilisées de manière inattendue par votre nom d'utilisateur sur un poste de travail ou un nœud de calcul. Cela se produit par exemple si un programme Ansys exécuté sur un poste de travail distant n'a pas été arrêté correctement, laissant ainsi des processus actifs, ou si un programme Ansys plante sur un nœud de calcul d'une grappe dans une session `salloc` exécutée de manière interactive en ligne de commande, laissant là encore des processus Ansys actifs. Pour mettre fin à tous les processus Ansys potentiellement responsables, fermez le bureau, annulez la session (`salloc`), ou ouvrez simplement une fenêtre de terminal sur le nœud concerné et exécutez la commande `pkill -9 -e -u $USER -f "ansys"`. Toutes les licences Ansys qui étaient ouvertes devraient être immédiatement restituées au serveur de licences SHARCNET et redevenir disponibles pour vous ou d'autres utilisateurs.

# Fabrication additive

Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

## Activer la fabrication additive

Nous décrivons ici comment obtenir l'extension ACT de Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple ANSYSMotion, désinstallez-les à partir de votre projet.

### Télécharger l'extension

*   Téléchargez `AdditiveWizard.wbex` à partir de [https://catalog.ansys.com/](https://catalog.ansys.com/).
*   Téléversez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser.

### Lancer Workbench

*   Voir la section Workbench dans Ansys en mode graphique.
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec *Fichier -> Ouvrir*.

### Ouvrir le gestionnaire d'extensions

*   Cliquez sur la page ACT pour faire afficher l'onglet de la page ACT.
*   Cliquez sur *Gérer les extensions* pour ouvrir le gestionnaire d'extensions.

### Installer l'extension

*   Cliquez sur la boîte avec le signe + sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

### Charger l'extension

*   Cliquez pour sélectionner la boîte *AdditiveWizard*, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte *AdditiveWizard* et sélectionnez *Charger l'extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

### Supprimer l'extension

*   Cliquez pour désélectionner la boîte *AdditiveWizard*, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte *AdditiveWizard* et sélectionnez *Ne pas charger par défaut*, ce qui empêche le chargement de l'extension pour les futures sessions.

## Exécuter la fabrication additive

### OnDemand

Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing dans une session graphique OnDemand comme suit :

*   Lancez Workbench comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*.
*   Cliquez sur *Fichier -> Ouvrir* et sélectionnez *test.wbpj* puis cliquez sur *Ouvrir*.
*   Cliquez sur *Vue -> Réinitialiser l'espace de travail* si votre écran est gris.
*   Lancez *Mécanique, Effacer les données générées*, sélectionnez *Distribué*, spécifiez *Cœurs*.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

**Vérifiez l'utilisation**
*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que des processus Ansys persistants peuvent monopoliser des licences précieuses au sein d'une session de nœud de connexion OnDemand active si une session d'interface graphique Ansys (Fluent, Workbench, Mechanical, etc.) n'est pas fermée correctement ou est interrompue de manière inattendue par une panne réseau ou un blocage du système de fichiers. Dans ce dernier cas, il sera peut-être impossible d'arrêter les processus tant que l'accès normal au disque n'est pas rétabli.

### Grappe

**Préparation du projet**

Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour Workbench dans la section Soumettre des tâches en lot sur nos grappes ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution et recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)`; ou 2. enregistrez une copie du fichier `YOURPROJECT.wbpj` d'origine et du répertoire `YOURPROJECT_files` correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne `FilePath`.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

**Utilisation des ressources**

Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `srun`. Le script pour huit cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

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

**Tests de scalabilité**

Une fois la tâche complétée, son *temps d'exécution effectif* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le temps d'exécution effectif diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

# Aide

La documentation complète et officielle des versions récentes d'Ansys 202[4|5]R[1|2] est disponible sur [ansyshelp.ansys.com](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation des versions plus anciennes, telles qu'Ansys 2023R[1|2], nécessite [de se connecter](https://ansyshelp.ansys.com/connection). La documentation de développement est disponible sur [Ansys Developer Portal](https://developer.ansys.com). D'autres ressources pédagogiques sont également disponibles, notamment les [tutoriels vidéo Ansys](https://www.youtube.com/@AnsysHowTo/videos), la [plateforme Ansys Educator Hub](https://innovationspace.ansys.com/educator-hub/) et la [série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

### XoverSSH

Certains programmes peuvent être exécutés à distance sur un nœud de calcul d'une grappe en redirigeant X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge, car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation OU sur la sélection, l'installation et la configuration d'un émulateur client X approprié tel que MobaXterm. Les temps de réponse interactifs sont inacceptablement longs pour les tâches de menu de base, et a fortiori pour les tâches plus complexes impliquant le rendu graphique. Le temps de démarrage des programmes avec interface graphique peut également être très long en fonction de votre connexion Internet. Par exemple, lors d'un test, le démarrage complet de l'interface graphique via SSH a pris 40 minutes, contre seulement 34 secondes avec vncviewer. Malgré cette lenteur potentielle, cette méthode de connexion peut s'avérer intéressante si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou des calculs, et si les délais de réponse sont acceptables. Voici les étapes de base pour commencer :

1.  `ssh -Y username@alliancecan.ca`
2.  `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task=4 [--gpus-per-node=1] --account=def-mygroup`
3.  Une fois connecté à un nœud de calcul, exécutez la commande `xclock`. Si l'horloge apparaît sur votre bureau, chargez ensuite le logiciel Ansys souhaité.