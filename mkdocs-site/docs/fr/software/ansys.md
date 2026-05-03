---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "2822fe98fcaea9c651cc9a1848ae005d"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:34:39.411418+00:00"

tags:
  - software

keywords:
  - "module Ansys"
  - "interface graphique de Fluent"
  - "messages d'erreur"
  - "redémarrage"
  - "partitionnement du maillage"
  - "serveur CMC"
  - "bash script"
  - "simulation"
  - "temps d'exécution"
  - "Script Slurm"
  - "Remise en file d'attente"
  - "Redémarrage"
  - "script Slurm"
  - "ANSYS-FLUENT"
  - "fichier cas"
  - "vérification de licence"
  - "SLURM_SUBMIT_DIR"
  - "nombre de cœurs"
  - "SLURM"
  - "nombre total de pas"
  - "journal file"
  - "Fichiers de journalisation"
  - "paquet Ansys"
  - "Licence"
  - "Pas de temps"
  - "Compute nodes"
  - "Slurm batch script"
  - "grappe"
  - "coupe-feu"
  - "Fichier de journalisation"
  - ".cas.h5/.dat.h5"
  - "Niagara"
  - "SBATCH"
  - "Simulation"
  - "script bash"
  - "cellules par cœur"
  - "Serveur de licence"
  - "guide d'utilisation"
  - "fichier ansys.lic"
  - "fichier de cas"
  - "CC_CLUSTER"
  - "serveurs de licence locaux"
  - "solveur parallèle"
  - "module load ansys"
  - "établissement"
  - "serveur de licence"
  - "Ansys Fluent"
  - ".cas/.dat"
  - "Ansys"
  - "formats de fichiers"
  - "openmpi"
  - "ANSYS Fluent"
  - "trillium"
  - "plusieurs nœuds"
  - "Interface TUI"
  - "configuration requise"
  - "Tâches en lot"
  - "serveur de licence ANSYS"
  - "calcul parallèle"
  - "Journal file"
  - "gra-vdi"
  - "Narval"
  - "durée totale de la simulation"
  - "version Ansys"
  - "grappes"
  - "prêt à utiliser"
  - "SLURM_ARRAY_JOB_ID"
  - "fluent"
  - "Workbench"
  - "configuration"
  - "Service packs"
  - "intelmpi"
  - "Fluent"
  - "Script bash"
  - "Plusieurs nœuds"
  - "machinefile"
  - "redémarrages"
  - "Calcul Canada"
  - "fichier de licence"
  - "Slurm"
  - "Compatibilité des versions"
  - "scripts de soumission"
  - "nœuds de calcul"
  - "OpenMPI"
  - "ordonnanceur Slurm"
  - "serveur distant"

questions:
  - "Qu'est-ce que le logiciel Ansys et comment fonctionne le système de licence pour y accéder sur les grappes de calcul ?"
  - "Quelles sont les étapes pour configurer son propre fichier de licence Ansys dans son répertoire personnel ?"
  - "Quelles configurations réseau et de coupe-feu sont requises pour permettre l'utilisation d'un serveur de licence local ou institutionnel ?"
  - "Que doit-on configurer avant de pouvoir utiliser le serveur de licence de l'établissement ?"
  - "Quelles directives faut-il suivre si la configuration des coupe-feu est déjà effectuée ?"
  - "À quelle section doit-on se référer si la configuration requise n'a pas encore été réalisée ?"
  - "Quelles sont les trois informations de base nécessaires pour configurer le fichier `ansys.lic` lorsque le serveur est déjà prêt à être utilisé ?"
  - "Quelles exigences supplémentaires doivent être remplies si le serveur de licence Ansys n'a jamais été configuré pour les grappes distantes ?"
  - "Quelle est la procédure à suivre en ligne de commande pour vérifier que la licence Ansys est bien configurée et fonctionne correctement sur la grappe ?"
  - "Quelle commande est recommandée pour lancer Workbench afin d'utiliser un serveur distant ?"
  - "Quel fichier de licence spécifique est lu par le script enveloppant lors de son exécution ?"
  - "Comment l'option interactive simplifie-t-elle la configuration pour l'utilisation du serveur CMC ?"
  - "Quelles sont les recommandations et les limites de ressources (cœurs et mémoire) pour exécuter Mechanical et Fluent sur gra-vdi ?"
  - "Quelles commandes et actions faut-il exécuter pour résoudre un blocage de l'interface graphique d'Ansys ou de Workbench ?"
  - "Comment fonctionne la compatibilité entre les différentes versions d'Ansys et comment peut-on identifier la version utilisée pour créer un fichier cas Fluent ?"
  - "Pourquoi la version 2025R1.02 d'Ansys nécessite-t-elle une attention particulière concernant le serveur de licence par rapport aux versions 2024R2.04 ou antérieures ?"
  - "Comment le système de numérotation et de chargement des modules permet-il aux utilisateurs de gérer et de sélectionner des correctifs (service packs) spécifiques à partir de la version 2024 ?"
  - "Pourquoi les implémentations MPI incluses dans la suite Ansys nécessitent-elles des directives particulières pour soumettre des tâches en lot sur les grappes utilisant l'ordonnanceur Slurm ?"
  - "Quels sont les risques potentiels lors de l'ouverture d'une simulation créée avec une version antérieure du logiciel ?"
  - "Comment peut-on retrouver le numéro de la version Ansys Fluent utilisée pour créer un fichier cas si on l'a oublié ?"
  - "Quelle commande informatique spécifique est donnée en exemple pour extraire les informations de version à partir des fichiers \".cas\" ou \".cas.h5\" ?"
  - "Pourquoi faut-il utiliser des directives spécifiques à chaque paquet Ansys pour lancer une tâche parallèle ?"
  - "Que propose le document pour faciliter la soumission de ces tâches parallèles ?"
  - "Sur quelle grappe de calcul les scripts de soumission pourraient-ils nécessiter des ajustements particuliers ?"
  - "Quelles sont les étapes de préparation et de transfert des fichiers requises avant de lancer une simulation Ansys Fluent sur la grappe ?"
  - "Comment peut-on gérer automatiquement les erreurs liées au manque de licence lors de la soumission d'une tâche, et quels sont les risques associés à cette méthode ?"
  - "Quelles sont les recommandations concernant le choix des scripts Slurm (par nœud vs par cœur) et le partitionnement du maillage pour optimiser les performances de la simulation ?"
  - "Quelles sont les différences de directives Slurm entre une allocation de ressources par nœud et une allocation par cœur pour exécuter ANSYS Fluent ?"
  - "Comment les scripts gèrent-ils les spécificités des différentes grappes de calcul (comme Narval et Nibi) lors de la configuration de l'environnement MPI ?"
  - "Quels modules et paramètres de ligne de commande sont nécessaires pour lancer correctement la simulation Fluent selon ces scripts ?"
  - "Quelle est la méthode alternative mentionnée pour effectuer le partitionnement du maillage avant l'exécution sur la grappe ?"
  - "Quels sont les avantages de réaliser ce partitionnement manuellement dans l'interface graphique de Fluent ?"
  - "Quelles conditions numériques concernant les partitions et les cellules par cœur doivent être respectées pour obtenir une efficacité optimale ?"
  - "Comment le script adapte-t-il les paramètres de communication de Fluent (comme `-peth` ou `-pib`) en fonction du cluster identifié ?"
  - "Quelle est l'utilité du fichier `machinefile` généré dans le répertoire temporaire avec l'identifiant de la tâche Slurm (`$SLURM_JOB_ID`) ?"
  - "Quelles directives spécifiques doivent être incluses dans l'en-tête du script batch (comme le compte) pour soumettre une tâche sur plusieurs nœuds sur le cluster Narval ?"
  - "How do the Slurm resource allocation directives differ when configuring a job by node versus by core?"
  - "What specific environment modules and ANSYS versions are required to run the simulation on the Trillium cluster compared to Narval?"
  - "How are the `MYJOURNALFILE` and `MYVERSION` variables utilized in the execution command of the ANSYS Fluent scripts?"
  - "Quelles vérifications de répertoires et de fichiers de configuration le script effectue-t-il avant de lancer la tâche Fluent ?"
  - "Pour quels types de tâches Fluent l'utilisation des scripts de remise en file d'attente est-elle déconseillée et quelles en seraient les conséquences ?"
  - "Comment le paramètre de tableau (array) est-il utilisé dans le script Slurm pour gérer les multiples tentatives d'obtention de licence ?"
  - "What specific version of the ANSYS module is required to run successfully on the Trillium cluster?"
  - "How many CPUs per task are allocated in the SLURM batch script?"
  - "What are the acceptable values that can be specified for the solver version variable in the script?"
  - "What specific modules and environment variables are configured when the script detects it is running on the \"narval\" cluster?"
  - "Under what specific cluster and version conditions does the script set the Intel MPI bootstrap method to use SSH?"
  - "How does the script utilize Slurm environment variables to generate the machinefile and determine the number of cores for the ANSYS-FLUENT job?"
  - "Comment le script Slurm gère-t-il la remise en attente et la relance automatique des tâches Fluent en cas d'échec ?"
  - "Quelles modifications spécifiques doivent être apportées aux fichiers journaux pour configurer correctement le redémarrage d'une simulation à partir des données sauvegardées ?"
  - "Comment doit-on calculer le temps d'exécution et le nombre de pas de temps pour s'assurer que la simulation respecte la limite de temps imposée par les grappes de calcul ?"
  - "Pourquoi est-il recommandé de choisir la valeur 1 plutôt que 2 lorsqu'on part d'une solution précédente ?"
  - "Comment calcule-t-on la durée totale de la simulation et le nombre de fichiers de résultats générés si l'option 2 est sélectionnée ?"
  - "Comment doit-on déterminer la valeur du temps demandé pour s'assurer de respecter la fenêtre de temps de Slurm ?"
  - "Quel est l'objectif principal de ce script SLURM et quel logiciel de simulation vise-t-il ?"
  - "Comment le script gère-t-il le redémarrage automatique d'une simulation à l'aide des tableaux de tâches (job arrays) SLURM ?"
  - "De quelle manière le script adapte-t-il sa configuration MPI et ses paramètres d'exécution en fonction de la grappe de calcul utilisée (comme Narval ou Nibi) ?"
  - "Quel est l'objectif principal des commandes conditionnelles (if/else) présentes dans ce script bash ?"
  - "Comment le script interagit-il avec le gestionnaire de tâches Slurm lorsqu'une simulation se termine avec succès ?"
  - "Quelle configuration matérielle et quel mode d'exécution sont spécifiés par le nom de l'onglet et du fichier de script ?"
  - "Comment le script Slurm gère-t-il les redémarrages de la simulation à l'aide des tableaux de tâches (arrays) ?"
  - "Quel est le rôle principal des fichiers de journalisation dans l'interface TUI de Fluent selon le texte ?"
  - "Comment les formats de fichiers par défaut de Fluent évoluent-ils entre les versions antérieures à 2019R3 et celles à partir de 2020R1 ?"
  - "Où peut-on trouver des informations supplémentaires et la liste des commandes pour le logiciel Fluent ?"
  - "Quelle commande permet d'utiliser les formats de fichiers par défaut (.cas/.dat) pour les versions jusqu'à 2019R3 ?"
  - "Quels sont les formats de fichiers les plus efficaces introduits à partir de la version 2020R1 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Ansys](http://www.ansys.com/) est une suite logicielle pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

## Licence
La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas de licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez l'aspect légal de son utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence
Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire `/home`.
Pour indiquer votre propre serveur de licence, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient les deux lignes ci-dessous, où vous remplacez FLEXPORT, INTEPORT et LICSERVER par les valeurs de votre serveur.

```bash title="$HOME/.licenses/ansys.lic"
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@**LICSERVER**")
```

Les valeurs correspondant aux serveurs de licence CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un différent serveur, voir [Serveurs de licence locaux](#serveurs-de-licence-locaux) ci-dessous.

| Licence  | Grappe                                | LICSERVER                | FLEXPORT | INTEPORT | VENDPORT | NOTES                   |
| :------- | :------------------------------------ | :----------------------- | :------- | :------- | :------- | :---------------------- |
| CMC      | beluga                                | `10.20.73.21`            | `6624`   | `2325`   | s.o.     | aucune                  |
| CMC      | cedar                                 | `172.16.0.101`           | `6624`   | `2325`   | s.o.     | aucune                  |
| CMC      | graham                                | `10.25.1.56`             | `6624`   | `2325`   | s.o.     | nouvelle IP le 21 février 2025 |
| CMC      | narval                                | `10.100.64.10`           | `6624`   | `2325`   | s.o.     | aucune                  |
| SHARCNET | beluga/cedar/graham/gra-vdi/nibi/narval/rorqual | `license3.sharcnet.ca`   | `1055`   | `2325`   | s.o.     | aucune                  |
| SHARCNET | niagara                               | `localhost`              | `1055`   | `2325`   | `1793`   | aucune                  |

### Serveurs de licence locaux

Avant que le serveur de licence de votre établissement puisse être utilisé, les coupe-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans le paragraphe *Prêt à utiliser* ci-dessous. Autrement, référez-vous au paragraphe *Configuration requise* un peu plus bas.

#### Prêt à utiliser

Pour utiliser un serveur de licence Ansys déjà configuré pour être utilisé sur la grappe où vous allez soumettre des tâches, contactez votre administrateur de serveur de licences Ansys et obtenez les trois éléments d'information suivants :
1. le nom d'hôte complet (**LICSERVER**) du serveur
2. le port Flex (FLEXPORT) pour Ansys, habituellement 1055
3. le port d'interconnexion (INTEPORT), habituellement 2325
Une fois les trois éléments d'information collectés, configurez votre fichier `~/.licenses/ansys.lic` en entrant les valeurs de LICSERVER, FLEXPORT et INTEPORT dans le bloc de code pour `ansys.lic` ci-dessus.

#### Configuration requise

Si votre serveur de licence Ansys local n'a jamais été configuré pour être utilisé sur la ou les grappes où vous allez soumettre des tâches, en plus des 3 éléments ci-dessus, vous devrez **ÉGALEMENT** obtenir les éléments suivants auprès de l'administrateur :
4. le numéro de port statique du fournisseur (VENDPORT)
5. confirmation que `<servername>` se résoudra à la même adresse IP que LICSERVER sur nos grappes
où `<servername>` peut être trouvé dans la première ligne du fichier de licence avec le format *SERVER <servername> <host id> <lmgrd port>*. L'élément 5 est obligatoire sinon les extractions de licences Ansys ne fonctionneront sur aucune grappe distante. S'il s'avère que `<servername>` ne répond pas à cette exigence, demandez à votre administrateur de licence de remplacer `<servername>` par le même nom d'hôte complet que LICSERVER ou au moins par un nom d'hôte qui se résoudra à la même adresse IP que LICSERVER à distance.

## Vérifier la licence

Pour vérifier si `ansys.lic` est bien configuré et fonctionne correctement, copiez et collez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches. La seule différence est de spécifier YOURUSERID. Si le logiciel n’est pas à jour sur le serveur de licence distant, un problème peut survenir si la dernière version du module Ansys est chargée pour effectuer des tests. Pour que la licence fonctionne quand des tâches sont soumises, assurez-vous que la même version du module Ansys qui est chargé par votre script est utilisée dans les commandes ci-dessous.

```bash
cd /tmp
salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
module load StdEnv/2023; module load ansys/2023R2
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE 1> /dev/null && echo Success || echo Fail
```

```bash
cd /tmp
salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
module load StdEnv/2023; module load ansys/2025R2.04
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```
`Success` indique que les extractions de licence devraient fonctionner lors de la soumission de tâches à la file d'attente.
`Fail` indique un problème de configuration de licence et les tâches échoueront probablement.

!!! note "Remarque 1"
    Pour les modules Ansys installés localement, la commande `runwb2` de `SnEnv` utilise par défaut le serveur de licence SHARCNET, tel que défini dans le fichier du module Ansys que vous chargez. Pour utiliser un serveur distant, lancez plutôt Workbench avec `runwb2-gui`, car ce script enveloppant (*wrapper*) lira votre fichier `~/.licenses/ansys.lic` comme les modules disponibles sous `StdEnv/2023`. De plus, l'option interactive d'utilisation du serveur CMC (acheminé via le serveur SHARCNET CMC CadPASS) sera proposée, éliminant ainsi la nécessité de le configurer dans votre fichier ansys.lic.

!!! note "Remarque 2"
    Lorsque vous démarrez Fluent à partir de Workbench avec la version 2025R1, avant de cliquer sur le bouton *Start*, cliquez sur l'onglet *Environment* du panneau de lancement de *Fluent Launcher* et copiez/collez `HOOPS_PICTURE=opengl` dans le champ de saisie vide. Vous pouvez aussi définir `export HOOPS_PICTURE=opengl` dans votre environnement avant de démarrer Workbench. L'une ou l'autre de ces actions empêchera le message suivant, qui apparaîtrait dans les messages de démarrage de l'interface utilisateur : `Warning: Software rasterizer found, hardware acceleration will be disabled.`

!!! note "Remarque 3"
    Lorsque vous exécutez Mechanical dans Workbench sur gra-vdi, assurez-vous de cocher *Distributed* dans le panneau *Solver* du ruban supérieur et de spécifier une valeur maximale de **24 cœurs**. Lorsque vous exécutez Fluent sur gra-vdi, ne cochez pas *Distributed* et spécifiez une valeur maximale de **12 cœurs**. N'essayez pas d'utiliser plus de 128 Go de mémoire, sinon Ansys atteindra la limite et sera arrêté. Si vous avez besoin de plus de cœurs ou de mémoire, utilisez un nœud de calcul sur une grappe pour exécuter votre session graphique. Lorsque vous effectuez une ancienne tâche de prétraitement ou de post-traitement avec Ansys sur gra-vdi et que vous n'exécutez pas de calcul, utilisez uniquement **4 cœurs**, sinon les licences HPC seront extraites inutilement.

!!! note "Remarque 4"
    Dans de très rares cas, l'interface graphique de Workbench ou de certains programmes qu'il exécute se bloquent ou ne démarrent pas correctement, notamment si vnsviewer se déconnecte avant que Ansys soit fermé correctement. En général, si Ansys ne fonctionne pas correctement, ouvrez une nouvelle fenêtre de terminal sur gra-vdi et exécutez ```bash pkill -9 -e -u $USER -f "ansys|fluent|mwrpcss|mwfwrapper|ENGINE|mono" ``` pour arrêter complètement tous les processus Ansys. Si le problème persiste et que vous utilisiez l'interface graphique sur des nœuds de calcul avant de travailler sur gra-vdi, essayez d'exécuter `rm -rf .ansys`. Si le problème concerne /home, /project ou /scratch (la commande df bloque), il est fort probable qu'Ansys recommence à fonctionner normalement une fois le problème de stockage résolu.

## Compatibilité des versions

Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une moins récente version d'Ansys devraient pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec ansys/2022R2 devrait fonctionner avec ansys/2023R2, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
$ grep -ia fluent combustor.cas
(0 "fluent15.0.7 build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge

## Ansys Fluent
Voici la procédure habituelle pour utiliser Fluent avec les grappes de Calcul Canada :

## Nouveautés

Ansys publie régulièrement des *correctifs* pour regrouper plusieurs mises-à-jour apportant différents correctifs et améliorations à ses versions majeures. Des informations similaires pour les versions précédentes peuvent généralement être trouvées sur [le blog Ansys](https://www.ansys.com/blog), en utilisant la barre de recherche FILTERS. Par exemple, la recherche de `What’s New Fluent 2024 gpu` affichera le document [What’s New for Ansys Fluent in 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1) qui contient une multitude d'informations sur la prise en charge des GPU. Spécifier un numéro de version dans le champ de recherche [Press Release](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations sur les nouvelles versions. Le module `ansys/2025R1.02` pour la dernière version d'Ansys a été installé récemment; pour l'utiliser cependant, vous avez besoin d'un serveur de licence comme celui de CMC. La mise à jour du serveur de licence de SHARCNET est en cours et tant que ce travail ne sera pas terminé, seules les versions `ansys/2024R2.04` ou moins récentes seront prises en charge. Si un module pose problème ou pour demander l'installation d'une nouvelle version, écrivez au [soutien technique](../support/technical_support.md).

## Correctifs

À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *correctif* est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun *correctif* peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le *correctif* 3 peut être chargé avec `module load ansys/2024R1.03`. Si un *correctif* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *correctif* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *correctif* installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les *correctifs* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *correctif* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *correctif* rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque *correctif* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

## Soumettre des tâches en lot sur nos grappes
Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

### Ansys Fluent
La procédure suivante est habituellement utilisée pour exécuter Fluent sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *File > Export > Case…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `FFF-1.cas.gz`.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *File > Export > Data…* ou trouvez-le dans le même répertoire [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage) de la grappe (`FFF-1.dat.gz`).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers /project ou /scratch de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `FFF-1.*` ou renommez-les au téléversement.
5.  Créez un fichier de journalisation dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancez le solveur et enregistrez les résultats. Voyez les exemples ci-dessous et n'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour le script sous l'onglet *Plusieurs nœuds (par cœur + remise en attente)* plus loin. Cependant, ceci remet aussi en attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en attente est ou non due à un problème de licence. Si vous découvrez que la remise en attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `scancel jobid` et corrigez le problème.
7.  Lorsque la [tâche est terminée](../running-jobs/running_jobs.md), vous pouvez télécharger le fichier de données et le retourner dans Fluent avec *File > Import > Data…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale

La plupart des tâches Fluent devraient utiliser le script *par nœud* ci-dessous pour minimiser le temps d'attente et maximiser la performance en utilisant le moins de nœuds possible. Les tâches demandant beaucoup de cœurs CPU pourraient attendre moins longtemps dans la queue avec le script *par cœur*, mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent fournir une alternative plus robuste si Fluent plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts Intel standards avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de Fluent, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts Intel. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

=== "Plusieurs nœuds (par nœud)"

```bash title="script-flu-bynode-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
```

=== "Plusieurs nœuds (par cœur)"

```bash title="script-flu-bycore-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
#SBATCH --ntasks=16           # Specify total number of cores across all nodes
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
```

=== "Plusieurs nœuds (par nœud, Narval)"

```bash title="script-flu-bynode-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (1 or more)
#SBATCH --ntasks-per-node=64  # Specify number of cores per node (narval 64 or less)
#SBATCH --mem=0               # Do not change (allocate all memory per compute node)
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

export OPENMPI_ROOT=$EBROOTOPENMPI
slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
else
 export FI_PROVIDER=verbs
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
fi
```

=== "Plusieurs nœuds (par cœur, Narval)"

```bash title="script-flu-bycore-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify number of compute nodes (1 or more)
#SBATCH --ntasks=16           # Specify total number of cores across all nodes
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

export OPENMPI_ROOT=$EBROOTOPENMPI
slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
else
 export FI_PROVIDER=verbs
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
fi
```

=== "Plusieurs nœuds (par nœud, Trillium)"

```bash title="script-flu-bynode-intel-tri.sh"
#!/bin/bash

#SBATCH --account=def-group      # Specify account name
#SBATCH --time=00-03:00          # Specify time limit dd-hh:mm
#SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
#SBATCH --ntasks-per-node=16     # Specify number cores per node (max 192 on trillium)
##SBATCH --mem=0                 # Do not uncomment (be default trillium uses all memory per node)
#SBATCH --cpus-per-task=1        # Do not change (required parameter)

cd $SLURM_SUBMIT_DIR             # Submit from $SCRATCH/some/dir

module load StdEnv/2023          # Do not change
module load ansys/2025R2.04      # only 2025R2 or newer works on trillium

MYJOURNALFILE=sample.jou         # Specify your journal file name
MYVERSION=3d                     # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ ! -L "$HOME/.ansys" ]; then
  echo "ERROR: A link to a writable .ansys directory does not exist."
  echo 'Remove ~/.ansys if one exists and then run: ln -s $SCRATCH/.ansys ~/.ansys'
  echo "Then try submitting your job again. Aborting the current job now!"
elif [ ! -L "$HOME/.fluentconf" ]; then
  echo "ERROR: A link to a writable .fluentconf directory does not exist."
  echo 'Remove ~/.fluentconf if one exists and run: ln -s $SCRATCH/.fluentconf ~/.fluentconf'
  echo "Then try submitting your job again. Aborting the current job now!"
elif [ ! -L "$HOME/.flrecent" ]; then
  echo "ERROR: A link to a writable .flrecent file does not exist."
  echo 'Remove ~/.flrecent if one exists and then run: ln -s $SCRATCH/.flrecent ~/.flrecent'
  echo "Then try submitting your job again. Aborting the current job now!"
else
  mkdir -pv $SCRATCH/.ansys
  mkdir -pv $SCRATCH/.fluentconf
  touch $SCRATCH/.flrecent
  if [ "$SLURM_NNODES" == 1 ]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
  else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=$SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
  fi
fi
```

#### Remise en file d'attente pour obtenir la licence

Les scripts suivants ne doivent être utilisés qu'avec des tâches Fluent qui sont connues pour se terminer normalement sans générer d'erreurs en sortie, mais qui nécessitent généralement plusieurs tentatives de remise en file d'attente pour obtenir les licences. Ils ne sont pas recommandés pour les tâches Fluent qui peuvent 1) s'exécuter pendant une longue période avant de planter 2) s'exécuter jusqu'à la fin mais contenir des avertissements de journalisation; dans les deux cas, les simulations seront répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente spécifié par la valeur `array` soit atteint. Pour ces types de tâches, les scripts à usage général (ci-dessus) doivent être utilisés.

=== "Plusieurs nœuds (par nœud + remise en attente)"

```bash title="script-flu-bynode+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
if [ $? -eq 0 ]; then
    echo "Job completed successfully! Exiting now."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Resubmitting job now …"
    else
       echo "All job attempts failed exiting now."
    fi
fi
```

=== "Plusieurs nœuds (par cœur + remise en attente)"

```bash title="script-flu-bycore+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
#SBATCH --ntasks=16           # Specify total number of cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
if [ $? -eq 0 ]; then
    echo "Job completed successfully! Exiting now."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Resubmitting job now …"
    else
       echo "All job attempts failed exiting now."
    fi
fi
```

#### Redémarrage

Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de *sample.cas*, *sample.dat* et *sample.jou* doit être présent. Modifiez le fichier *sample.jou* pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier de journalisation avec ```bash cp sample.jou sample-restart.jou ``` et modifiez le fichier *sample-restart.jou* pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `;/solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez *sample-restart.jou* en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de *sample.jou* est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera 1\*Dt+2\*Nrestart\*Dt où Nrestart est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi 1+2\*Nrestart. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

=== "Plusieurs nœuds (par nœud + redémarrage)"

```bash title="script-flu-bynode+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=07-00:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of solution restarts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
MYJOUFILE=sample.jou                # Specify your journal filename
MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILE
  else
    fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILERES
  fi
else
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
   if [[ "${CC_CLUSTER}" == nibi ]]; then
     fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
   else
     fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
   fi
  else
   if [[ "${CC_CLUSTER}" == nibi ]]; then
     fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
   else
     fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
   fi
  fi
fi
if [ $? -eq 0 ]; then
    echo
    echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
    echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
    echo
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
      echo "Restarting job with the most recent output dat file …"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Job completed successfully! Exiting now."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation failed. Exiting …"
fi
```

=== "Plusieurs nœuds (par cœur + redémarrage)"

```bash title="script-flu-bycore+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
#SBATCH --ntasks=16           # Specify total number of cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of restart aka time steps (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
MYJOUFILE=sample.jou                # Specify your journal filename
MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
  #export I_MPI_HYDRA_BOOTSTRAP=ssh    # uncomment on beluga or cedar
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -I $MYJOUFILE
  else
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -I $MYJOUFILERES
  fi
else
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
  else
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
  fi
fi
if [ $? -eq 0 ]; then
    echo
    echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
    echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
    echo
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
      echo "Restarting job with the most recent output dat file"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Job completed successfully! Exiting now."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation failed. Exiting now."
fi
```

### Fichiers de journalisation

Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface TUI (*Text User Interface*) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le guide d'utilisation de Fluent pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `/file/cff-files yes`.

=== "Fichier de journalisation (stable, cas)"

```text title="sample1.jou"
; SAMPLE FLUENT JOURNAL FILE - STEADY SIMULATION
; ----------------------------------------------
; lines beginning with a semicolon are comments

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read input case and data files
/file/read-case-data FFF-in

; Run the solver for this many iterations
/solve/iterate 1000

; Overwrite output files by default
/file/confirm-overwrite n

; Write final output data file
/file/write-case-data FFF-out

; Write simulation report to file (optional)
/report/summary y "My_Simulation_Report.txt"

; Cleanly shutdown fluent
/exit
```

=== "Fichier de journalisation (stable, cas + données)"

```text title="sample2.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION STABLE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read input files
/file/read-case-data FFF-in

; Write a data file every 100 iterations
/file/auto-save/data-frequency 100

; Retain data files from 5 most recent iterations
/file/auto-save/retain-most-recent-files y

; Write data files to output sub-directory (appends iteration)
/file/auto-save/root-name output/FFF-out

; Run the solver for this many iterations
/solve/iterate 1000

; écrire le dernier fichier de cas et de données en sortie
/file/write-case-data FFF-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y "My_Simulation_Report.txt"

; fermez correctement Fluent
exit
```

=== "Fichier de journalisation (temporaire)"

```text title="sample3.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION TEMPORAIRE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read the input case file
/file/read-case FFF-transient-inp

; For continuation (restart) read in both case and data input files
;/file/read-case-data FFF-transient-inp

; Write a data (and maybe case) file every 100 time steps
/file/auto-save/data-frequency 100
/file/auto-save/case-frequency if-case-is-modified

; Retain only the most recent 5 data (and maybe case) files
/file/auto-save/retain-most-recent-files y

; Write to output sub-directory (appends flowtime and timestep)
/file/auto-save/root-name output/FFF-transient-out-%10.6f

; ##### Settings for Transient simulation :  #####

; Set the physical time step size
/solve/set/time-step 0.0001

; Set the number of iterations for which convergence monitors are reported
/solve/set/reporting-interval 1

; ##### Fin des paramètres #####

; initialiser avec la méthode hybride
/solve/initialize/hyb-initialization

; indiquer le nombre maximal d'itérations par pas et le nombre de pas
;/solve/set/max-iterations-per-time-step 75
;/solve/dual-time-iterate 1000 ,
/solve/dual-time-iterate 1000 75

; enregistrer les derniers fichiers en sortie pour les cas et les données
/file/write-case-data FFF-transient-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y Report_Transient_Simulation.txt

; Cleanly shutdown fluent
/exit
```

### Fonctions UDF

La première étape est de transférer vers la grappe votre UDF (*User-Defined Function*), soit le fichier source sampleudf.c et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui elle exécute Linux. L'UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *Interpreted UDFs* et *UDF Library Manager* ne sont pas configurées pour utiliser un UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interpreté

Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier sampleudf.c par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```bash
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilé

Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire libudf contenant la bibliothèque partagée `libudf.so` requise. Le répertoire libudf ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la libudf nouvellement créée vers n'importe quelle autre de nos grappes, à condition que votre compte charge la même version du module d'environnement StdEnv. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (load) libudf ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes libudf (compile et load) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de build de type « racetime » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent (exécutée sur n'importe quel nœud de calcul ou sur gra-vdi) peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *Compiled UDFs*, et cliquez sur *Build*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

```bash
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```
et/ou
```bash
define/user-defined/compiled-functions load libudf
```

#### Parallèle

Avant qu'une UDF puisse être utilisée avec une tâche parallèle Fluent (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque Fluent est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, Fluent fonctionnera lentement au mieux ou plantera immédiatement au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque Fluent est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans *Fluent Customization Manual, Part I: Chapter 7: Parallel Considerations* qui se trouve dans l'[Aide](#aide).

#### DPM
Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour *Discrete Phase Models*) comme décrit dans *2024R2 Fluent Users Guide, Part III: Solution Mode, Chapter 24: Modeling Discrete Phase, 24.2 Steps for Using the Discrete Phase Models,* et dans *2024R2 Fluent Customization Manual, Part I: Creating and Using User Defined Functions, Chapter 2: DEFINE Macros, 2.5 Discrete Phase Model (DPM) DEFINE Macros*. Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Point Properties* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physics--> Discrete Phase*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Create*. La boîte de dialogue *Set Injection Properties* contient le menu déroulant *Injection Type* avec les quatre premiers types disponibles (*single, group, surface, flat-fan-atomizer*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Point Properties* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Point Properties* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *File* dans le menu déroulant *Injection Type*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *File* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Set Injection Properties*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension .dpm) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Select File*, sélectionnez *All Files (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension .inj; cliquez sur le bouton OK. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Set Injection Properties* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Discrete Phase Model* et sélectionnez *Interaction with Continuous Phase* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple :
```bash
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```
où un format de fichier stable d'injection de base créé manuellement pourrait ressembler à :
```bash
$ cat zinjection01.inj
(z=4 12)
( x y z u v w diamètre t débit massique fréquence massique temps nom )
(( 2.90e-02 5.00e-03 0.0 -1,00e-03 0,0 0,0 1,00e-04 2,93e+02 1,00e-06 0,0 0,0 0,0 ) injection-0:1 )
```
notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans *2024R2 Fluent Customization Manual, Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format*.

## CFX

### Scripts pour l'ordonnanceur Slurm

Le résumé des options de ligne de commande peut être affiché avec `cfx5solve -help`. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, cfx5solve s'exécute en simple précision (*-single*). Pour exécuter cfx5solve en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, cfx5solve prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'Ansys CFX-Solver Manager pour plus de détails.

=== "Nœud simple"

```bash title="script-local.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify single compute node (do not change)
#SBATCH --ntasks-per-node=4   # Specify number cores (maximum: graham 44, cedar 32 or 48, beluga 40, narval 64)
#SBATCH --mem=16G             # Specify node memory (optionally set to 0 to allocate all node memory)
#SBATCH --cpus-per-task=1     # Do not change

#module load StdEnv/2020      # Uncomment to use (deprecated)
#module load 2021R2           # Specify 2021R2 only

module load StdEnv/2023
module load ansys/2023R2      # Or newer module versions

# append additional cfx5solve command line options as required
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
else
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
fi
```

=== "Plusieurs nœuds"

```bash title="script-cfx-multiple.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=2             # Specify multiple compute nodes (2 or more)
#SBATCH --ntasks-per-node=64  # Specify all cores per node (maximum: graham 44, 48, beluga 40, narval 64)
#SBATCH --mem=0               # Use all memory per compute node (do not change)
#SBATCH --cpus-per-task=1     # Do not change

#module load StdEnv/2020      # Uncomment to use (deprecated)
#module load 2021R2           # Specify 2021R2 only

module load StdEnv/2023
module load ansys/2023R2      # Specify 2022R2 or newer module versions

NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

# append additional cfx5solve command line options as required
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
else
  export I_MPI_HYDRA_BOOTSTRAP=ssh
  unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
fi
```

## Workbench

Initialisez le fichier de projet avant de le soumettre pour la première fois.
1. Connectez-vous à la grappe avec [TigerVNC](../interactive/vnc.md#nœuds-de-calcul).
2. Dans le même répertoire où se trouve le fichier de projet (YOURPROJECT.wbpj), [lancez Workbench](#workbench) avec la même version du module Ansys qui a servi à créer le projet.
3. Dans Workbench, ouvrez le projet avec *File -> Open*.
4. Dans la fenêtre principale, faites un clic droit sur *Setup* et sélectionnez *Clear All Generated Data*.
5. Dans la liste déroulante de la barre de menus du haut, cliquez sur *File -> Exit* pour sortir de Workbench.
6. Dans la fenêtre contextuelle Ansys Workbench qui affiche *The current project has been modified. Do you want to save it ?* cliquez sur le bouton *No*.
7. Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Puisqu'un nœud de calcul avec jusqu'à 96 cœurs, 768 Go de mémoire et 8 heures de temps d'exécution peut maintenant être réservé pour une session de bureau à la demande, envisagez d'exécuter vos simulations Workbench directement depuis l'interface graphique native de Workbench, ce qui peut être une option plus intuitive que de soumettre la tâche à la file d'attente avec un script Slurm.

### Scripts pour l'ordonnanceur Slurm

Pour soumettre un fichier de projet à la queue, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

=== "Nœud simple (StdEnv/2023)"

```bash title="script-wbpj-2023.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Time (DD-HH:MM)
#SBATCH --mem=16G                      # Total Memory (set to 0 for all node memory)
#SBATCH --ntasks=4                     # Number of cores
#SBATCH --nodes=1                      # Do not change (multi-node not supported)
##SBATCH --exclusive                   # Uncomment for scaling testing
##SBATCH --constraint=broadwell        # Applicable to graham or cedar

module load StdEnv/2023 ansys/2023R2   # OR newer Ansys module versions

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
else
  MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
fi

rm -fv *_files/.lock
MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"

export KMP_AFFINITY=disabled
export I_MPI_HYDRA_BOOTSTRAP=ssh

runwb2 -B -E "Update()" -F YOURPROJECT.wbpj
#runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
```

=== "Nœud simple (StdEnv/2020)"

```bash title="script-wbpj-2020.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Time (DD-HH:MM)
#SBATCH --mem=16G                      # Specify total memory
#SBATCH --ntasks=4                     # Specify number of cores
#SBATCH --nodes=1                      # Do not change (multi-node not supported)
##SBATCH --exclusive                   # Uncomment ONLY for scaling testing
##SBATCH --constraint=broadwell        # Uncomment to specify an available node type

module load StdEnv/2020 ansys/2021R2   # OR newer Ansys module versions

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
else
  MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
fi

rm -fv *_files/.lock
MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"

export KMP_AFFINITY=disabled
export I_MPI_HYDRA_BOOTSTRAP=ssh

runwb2 -B -E "Update()" -F YOURPROJECT.wbpj
#runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
```
Pour éviter d'écrire la solution quand une tâche en cours d'exécution se termine avec succès, changez `Save(Overwrite=True)` en `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera la détermination de l'efficacité de la simulation lorsque `#SBATCH --ntasks` est augmenté, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical

Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Tools -> Write Input Files* et en spécifiant `File name:` pour YOURAPDLFILE.inp et `Save as type:` pour les fichiers APDL en entrée (*.inp*). Les tâches APDL peuvent ensuite être soumises à la queue avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm

Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `##SBATCH` sont suivies d'un commentaire.

=== "Mémoire parallèle partagée (CPU)"

```bash title="script-smp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify your account
#SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
#SBATCH --mem=32G               # Specify memory for all cores
#SBATCH --nodes=1               # Do not change
#SBATCH --tasks=8               # Specify number of cores
#SBATCH --cpus-per-task=1       # Do not change

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
```

=== "Mémoire parallèle distribuée (CPU)"

```bash title="script-dmp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify your account
#SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
#SBATCH --mem-per-cpu=4G        # Specify memory per core
##SBATCH --nodes=2              # Specify number of nodes (optional)
#SBATCH --ntasks=8              # Specify number of cores
##SBATCH --ntasks-per-node=4    # Specify cores per node (optional)
#SBATCH --cpus-per-task=1       # Do not change

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
if [[ "$CC_CLUSTER" = cedar ]]; then
 ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
 export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
fi

if [[ "$CC_CLUSTER" = beluga  ]]; then
  export KMP_AFFINITY=none
  mapdl -dis -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
else
  mapdl -dis -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
fi
```

=== "Mémoire parallèle partagée (GPU)"

```bash title="script-smp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify your account
#SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
#SBATCH --mem=32G                # Specify memory for all cores
#SBATCH --ntasks=8               # Specify number of cores
#SBATCH --nodes=1                # Do not change
#SBATCH --cpus-per-task=1        # Do not change
#SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
##SBATCH --partition=debug       # Temporarily required on mini-graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

export ANSGPU_PRINTDEVICES=1
mapdl -smp -acc nvidia -na $SLURM_GPUS_ON_NODE -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID  -i YOURAPDLFILE.inp
```

=== "Mémoire parallèle distribuée (GPU)"

```bash title="script-dmp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify your account
#SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
#SBATCH --mem-per-cpu=4G         # Specify memory per core
#SBATCH --nodes=1                # Specify number of nodes
#SBATCH --ntasks-per-node=8      # Specify cores per node
#SBATCH --cpus-per-task=1        # Do not change
#SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
##SBATCH --partition=debug       # Temporarily required on mini-graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
if [[ "$CC_CLUSTER" = cedar ]]; then
 ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
 export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
fi

export ANSGPU_PRINTDEVICES=1
if [[ "$CC_CLUSTER" = beluga  ]]; then
  export KMP_AFFINITY=none
  mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
else
  mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
fi
```

Par défaut, Ansys alloue aux tâches APDL 1024 Mo de mémoire totale et 1024 Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande mapdl des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de scalabilité avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (SMP pour *Shared Memory Parallel*) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (DMP pour *Distributed Memory Parallel*) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```bash
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

En plus de pouvoir exécuter des simulations en mode graphique (comme indiqué dans la section *Mode graphique* ci-dessous), [Ansys Rocky](https://www.ansys.com/products/fluids/ansys-rocky) peut également exécuter des simulations en mode non graphique. Les deux modes prennent en charge l'exécution de Rocky avec des processeurs uniquement ou avec des processeurs et [des GPU](https://www.ansys.com/blog/mastering-multi-gpu-ansys-rocky-software-enhancing-its-performance). Dans la section ci-dessous, deux exemples de scripts sont fournis où chacun serait soumis à la file d'attente de Graham avec la commande habituelle `sbatch`. Au moment de la rédaction de cet article, aucun des deux scripts n'a été testé et des modifications seraient probablement nécessaires. Il est important de noter que ces scripts ne sont utilisables que sur Graham puisque le module Rocky qu'ils chargent tous les deux n'est (pour le moment) installé que sur Graham localement.

### Scripts pour l'ordonnanceur Slurm

Pour obtenir une liste complète des options de ligne de commande, exécutez `Rocky -h` sur la ligne de commande après avoir chargé un module Rocky (seul ansysrocky/2023R2 est présentement disponible sur Graham). En ce qui concerne l'utilisation de Rocky avec des GPU pour résoudre des problèmes couplés, le nombre de CPU que vous devez demander (sur le même nœud) doit être augmenté au maximum jusqu'à ce que la limite de scalabilité de l'application couplée soit atteinte. D'autre part, si Rocky est exécuté avec des GPU pour résoudre des problèmes découplés autonomes, seul un nombre minimal de CPU doit être demandé, ce qui permettra à Rocky de fonctionner de manière optimale; par exemple, seuls 2 ou éventuellement 3 CPU peuvent être nécessaires. Enfin, lorsque Rocky est exécuté avec 4 ou plus CPU, des licences *rocky_hpc* seront nécessaires, ce que fournit la licence SHARCNET.

=== "CPU seulement"

```bash title="script-rocky-cpu.sh"
#!/bin/bash

#SBATCH --account=account      # Specify your account (def or rrg)
#SBATCH --time=00-02:00        # Specify time (DD-HH:MM)
#SBATCH --mem=24G              # Specify total memory for cores
#SBATCH --cpus-per-task=6      # Specify number of cores to use
#SBATCH --nodes=1              # Request one node (do not change)

module load StdEnv/2023 ansys/2025R1       # or newer versions
export PATH=$EBROOTANSYS/v251/rocky:$PATH

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0
```

=== "GPU basé (redémarrage)"

```bash title="script-rocky-gpu.sh"
#!/bin/bash

#SBATCH --account=account      # Specify your account (def or reg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=24G              # Specify memory (set to 0 to use all node memory)
#SBATCH --cpus-per-task=6      # Specify cores (graham 32 or 44 to use all cores)
#SBATCH --gres=gpu:v100:2      # Specify gpu type : gpu quantity
#SBATCH --nodes=1              # Request one node (do not change)

module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04 # Example modules from other GPU script
# Or use similar modules as CPU based script if compatible:
# module load StdEnv/2023 ansys/2025R1
# export PATH=$EBROOTANSYS/v251/rocky:$PATH # Adjust version if needed

RESUME=0                                  # Specify 0 or 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Removes previous results
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
fi
```

=== "GPU basé (configuré)"

```bash title="script-rocky-gpu.sh0"
#!/bin/bash

#SBATCH --account=account      # Specify your account (def or reg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=24G              # Specify memory (set to 0 to use all node memory)
#SBATCH --cpus-per-task=6      # Specify cores (graham 32 or 44 to use all cores)
#SBATCH --gres=gpu:v100:2      # Specify gpu type : gpu quantity
#SBATCH --nodes=1              # Request one node (do not change)

# the rocky2023R2 module on graham was renamed to ansysrocky/2023R2   Apr24/2025
#module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2       # only avail on graham
module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04   # only avail on graham

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE
```

## Electronics

Les scripts Slurm pour utiliser Ansys EDT sont fournis sur une page wiki distincte [ici](ansysedt.md).

## Mode graphique

Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [Nibi](../clusters/nibi.md#accès-via-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
*   [Fir](fir.md) : `https://jupyterhub.fir.alliancecan.ca`
*   [Rorqual](../clusters/rorqual.md) : `https://jupyterhub.rorqual.alliancecan.ca`
*   [Narval](../clusters/narval.md) : `https://jupyterhub.narval.alliancecan.ca/`
*   [Trillium](https://ondemand.scinet.utoronto.ca) : `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources requises pour votre session de bureau interactive et cliquez sur Lancer ou Démarrer. Si des graphiques accélérés ou des calculs doivent être effectués au sein de votre session de bureau, assurez-vous de spécifier une ressource GPU. Une fois le bureau chargé, chargez un module Ansys. Si vous avez démarré un bureau propulsé par Jupyter Lab, cela peut être fait en cliquant sur le menu de gauche, ou si vous avez démarré un bureau OnDemand, tapez manuellement `module load ansys/version` sur la ligne de commande. Pour démarrer l'un des programmes Ansys courants tels que Fluent, CFX, Workbench et ainsi de suite, consultez la section suivante qui fournit des conseils pour la configuration des variables d'environnement et des arguments requis par les environnements graphiques basés sur VirtualGL ou Mesa, selon qu'un nœud avec une ressource GPU a été spécifié ou non.

### Fluent

Pour démarrer Ansys Fluent depuis la ligne de commande d'un bureau à la demande, ouvrez une fenêtre de terminal et exécutez les commandes :

```bash
module load StdEnv/2023 ansys/2025R1
fluent
```

Lorsque le panneau contextuel du lanceur Fluent apparaît, cliquez sur l'onglet Environnement et copiez/collez les paramètres de variables d'environnement suivants, selon que vous avez démarré votre session à la demande avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses (car ce sont des commentaires) et ne mettez pas "export" devant les noms de variables. Si la fenêtre de la console graphique devient corrompue au démarrage de l'interface graphique, redémarrez Fluent en définissant *HOOPS_PICTURE=null* pour désactiver la création du panneau graphique.

**Nœud de calcul (sans GPU demandé)**

*   `I_MPI_HYDRA_BOOTSTRAP=ssh` (requis sur Nibi)
*   `HOOPS_PICTURE=opengl2-mesa` (version 2025R1 ou plus récente)
*   `HOOPS_PICTURE=null` (version 2024R2 ou plus ancienne)
*   Cliquez sur le bouton `Start`

!!! note
    Lorsque vous exécutez Fluent sur la grappe Nibi, la variable d'environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être définie manuellement; sinon, Fluent plantera au démarrage des sessions de bureau de calcul OOD lorsque IntelMPI est utilisé. Des messages d'erreur tels que les suivants seront générés. Si cela se produit, quittez complètement Fluent, fermez proprement Workbench et recommencez.
    ```
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

### CFX

Au démarrage de CFX depuis un bureau à la demande, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal selon qu'un GPU a été demandé ou non au démarrage du bureau.

*   `module load StdEnv/2023 ansys/2025R1` (ou plus ancienne)
*   `cfx5 -graphics mesa` (sans GPU demandé)
*   `cfx5 -graphics ogl` (avec GPU demandé)

### Mapdl

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `mapdl -g`, ou via le démarreur,
*   `launcher` --> cliquer sur le bouton `RUN`

Les étapes suivantes pour démarrer l'interface graphique de Mechanical APDL depuis la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre bureau à la demande sur un nœd de calcul avec ou sans GPU.

### Workbench

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `xfwm4 --replace &` (nécessaire seulement si vous utilisez Ansys Mechanical)
*   `export QTWEBENGINE_DISABLE_SANDBOX=1` (nécessaire seulement si vous utilisez CFD-Post)
*   `runwb2`

Remarque : Quand vous exécutez en parallèle un programme d'analyse comme Mechanical ou Fluent sur un nœud simple, ne cochez pas la case *Distributed* et indiquez un nombre de cœurs égal à votre **session salloc, moins 1**. Les menus déroulants du Ansys Mechanical Workbench ne répondent pas correctement. Comme solution, lancez `xfwm4 --replace` sur la ligne de commande avant de démarrer Workbench. Pour avoir xfwm4 par défaut, modifiez `$HOME/.vnc/xstartup` et remplacez `mate-session` par `xfce4-session`.

Cette section montre comment démarrer Workbench (et éventuellement Fluent) sur un bureau à la demande ou un bureau Jupyter Lab.

### Problèmes avec SSH
Certains programmes d'interface graphique Ansys peuvent être exécutés à distance sur un nœud de calcul d'une de nos grappes par redirection X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que MobaXterm. La plupart d'entre vous trouveront les temps de réponse interactifs inacceptables pour les tâches de menu de base, sans parler de l'exécution de tâches plus complexes telles que celles nécessitant du rendu graphique. Les temps d'attente pour démarrer des programmes avec interface graphique peuvent également être très longs, dépendant de votre connexion Internet. Dans un test par exemple, il a fallu 40 minutes pour obtenir l'interface graphique avec SSH alors que vncviewer n'a pris que 34 secondes. Malgré la lenteur potentielle lors de la connexion via SSH pour exécuter des programmes avec interface graphique, cela peut toujours être intéressant si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou d'exécuter des calculs. Ces étapes de base sont un point de départ : 1) `ssh -Y username@graham.computecanada.ca`; 2) `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task =4 [--gpus-per-node=1] --account=def-mygroup`; 3) une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, chargez le module Ansys souhaité et essayez d'exécuter le programme.

#### Fluids
*   `module load CcEnv StdEnv/2023`
*   `module load ansys/2024R2.04` (ou versions moins récentes)
*   `unset SESSION_MANAGER`
*   `fluent | cfx5 | icemcfd`
*   La commande `unset SESSION_MANAGER` permet d'éviter le message d'erreur suivant au lancement de Fluent : `Qt: Session management error: None of the authentication protocols specified are supported`
*   Si le message suivant est affiché au lancement de icemcfd ... `Error segmentation violation - exiting after doing an emergency save` ... ne cliquez pas sur le bouton OK, autrement icemcfd va planter. Faites plutôt ce qui suit (une seule fois) :
*   sélectionnez *Settings Tab -> Display -> tick X11 -> Apply -> OK -> File -> Exit*
*   L'erreur ne devrait pas se produire quand vous démarrez de nouveau icemcfd.

#### Rocky
*   `module load clumod ansysrocky/2023R2 CcEnv StdEnv/2020 ansys/2023R2`
*   `module load clumod ansysrocky/2024R2.0 CcEnv StdEnv/2023 ansys/2024R2.04`
*   `module load CcEnv StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit `~/licenses/ansys.lic`
*   `Rocky-gui` Fournit par les modules ansysrocky locaux la sélection des serveurs CMC ou SHARCNET
*   `RockySolver` Exécute le solveur rocky à partir de la ligne de commande (l'ajout de -h pour *help* n'est pas testé)
*   `RockySchedular` Lance l'interface graphique pour soumettre et exécuter des tâches sur le nœud courant (non testé)
*   Rocky pour 2024R2 et moins récentes est disponible uniquement sur gra-vdi et les grappes Graham; l'installation sur toutes les grappes est prévue pour juin
*   Rocky pour 2025R1 et plus récentes est fourni sur toutes les grappes par le module Ansys (pas pris en charge par le serveur de licence SHARCNET)
*   Rocky ne peut utiliser que des CPU sur gra-vdi puisqu'il n'y a présentement qu'un seul GPU dédié aux graphiques
*   La licence SHARCNET inclut maintenant Rocky dont l'utilisation est sans frais pour la recherche
*   Voir la page [Rocky Innovation Space](https://innovationspace.ansys.com/ais-rocky/)
*   Pour des détails voir [Ansys Rocky 2024 R2 Release Highlights](https://innovationspace.ansys.com/knowledge/forums/topic/ansys-rocky-2024-r2-release-highlights/) et [Ansys Rocky 2025 R1 Release Highlights](https://innovationspace.ansys.com/knowledge/forums/topic/ansys-rocky-2025-r1-release-highlights/)

### Ansys EDT
*   Ouvrez une fenêtre de terminal et chargez le module avec
    *   `module load SnEnv ansysedt/2023R2`
    *   `module load SnEnv ansysedt/2021R2`
*   Dans le terminal, entrez `ansysedt` et attendez que l'interface s'affiche.
*   Ceci doit être fait une seule fois :
    *   sélectionnez *Tools -> Options -> HPC and Analysis Options -> Options*
    *   dans le menu déroulant, changez *HPC License* pour **Pool** (pour utiliser plus de 4 cœurs)
    *   cliquez sur *OK*
*   ---------- EXEMPLES ----------
*   Pour copier dans votre compte les exemples Antennas de 2023R2 :
    *   connectez-vous à une grappe (par exemple Graham)
    *   `module load ansysedt/2023R2`
    *   `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; cd ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf Antennas`
    *   `cp -a $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
*   Pour faire exécuter un exemple :
    *   ouvrez un fichier .aedt et cliquez sur *HFSS -> Validation Check*
    *   (si la validation produit une erreur, fermez et ouvrez de nouveau la simulation autant de fois que nécessaire)
    *   pour lancer la simulation, cliquez sur *Project -> Analyze All*
    *   pour quitter sans sauvegarder la solution, cliquez sur *File -> Close -> No*
*   si le programme plante et ne repart pas, essayez les commandes suivantes :
    *   `pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"`
    *   `rm -rf ~/.mw` (au lancement, ansysedt utilisera la configuration initiale)

### Ensight
*   `module load SnEnv`
*   `ansys/2024R2.04` (ou versions plus anciennes jusqu'à 2021R2)
*   `ensight`

### Mapdl
*   `module load CcEnv StdEnv/2023`
*   `ansys/2024R2.04` (ou versions plus anciennes)
*   `mapdl -g` (pour démarrer l'interface graphique directement), ou,
*   `unset SESSION_MANAGER; launcher -> click RUN button`

### Bureau JupyterLab
#### Rocky
*   `module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2`
*   `module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04`
*   `module load StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit le `~/licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules locaux ansysrocky permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de -h pour *help* n'est pas testé).
*   `RockySchedular`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions 2024R2 ou moins récentes ne fonctionnent que sur gra-vdi et Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions 2025R1 et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore pris en charge par le serveur de licence SHARCNET).
*   Le serveur de licence SHARCNET inclut Rocky; son utilisation est gratuite pour la recherche.
*   Rocky prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 CPU et 1 GPU pour un maximum de 8 heures, lancez
    ```bash
    salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount
    ```

**Nœud de calcul (sans GPU demandé)**

*   Cliquez pour charger ansys/2025R1 (ou une version plus récente) dans le menu latéral gauche du bureau.
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau Jupyter Lab.
    *   Si les graphiques de toute application (comme Fluent) démarrée dans Workbench apparaissent inutilisables en raison de graphiques corrompus, essayez d'effectuer les étapes suivantes. Elles créeront une icône de bureau `runwb2` personnalisée afin que Workbench puisse être démarré en mode Mesa. Si l'une des applications que vous démarrez dans Workbench est Fluent, alors lorsque le lanceur Fluent démarre, vous pouvez également essayer de définir la variable `HOOPS_PICTURE=opengl2-mesa` dans la fenêtre du lanceur Fluent.
*   Pour continuer, quittez Workbench, puis ouvrez une fenêtre de terminal. Copiez-collez la commande suivante dans le presse-papiers distant situé dans le coin supérieur droit de votre bureau Jupyter. Maintenant, les commandes peuvent être collées dans le terminal, c'est-à-dire :
*   `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop`
*   Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que nano en faisant ce qui suit :
*   `nano ~/Desktop/workbench-mesa.desktop`. Remplacez toutes les instances de `runwb2` par `runwb2 -oglmesa`, puis quittez l'éditeur en enregistrant les modifications. Maintenant, ACTUALISEZ le bureau Jupyter en appuyant sur la combinaison de touches *control-R*. La nouvelle icône devrait maintenant apparaître sur le bureau avec l'icône Workbench d'origine. Double-cliquez dessus pour démarrer Workbench.
*   La nouvelle icône persistera pour les sessions futures jusqu'à ce qu'elle soit supprimée manuellement avec la commande `rm -f ~/Desktop/workbench-mesa.desktop`.

**Nœud de calcul (avec GPU demandé)**

*   Cliquez pour charger ansys/2025R1 (ou une version plus récente) dans le menu latéral gauche du bureau
*   Cliquez sur l'icône Workbench (VNC) située dans la fenêtre centrale du bureau Jupyter Lab

#### Ensight
*   `module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6`
*   `export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib`
*   `ensight -X`

## Electronics

Des informations décrivant comment exécuter Ansys EDT en mode graphique peuvent être trouvées [ici](ansysedt.md).

## Particularités selon le site d'utilisation

### Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de ***recherche universitaire publiable***; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Multiphysics Campus Solution en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio).
Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par Ansys en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences anshpc de 1986 est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50% en CPU seront probablement signalées par le système et examinées par notre équipe technique.

```bash
unset SLURM_GTIDS
```

Depuis décembre 2022, chaque utilisateur peut exécuter 4 travaux en utilisant un total de 252 anshpc (plus 4 anshpc par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon ((252 + 4\*nombre de tâches) / nombre de tâches). MISE À JOUR : En octobre 2024, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

#### Fichier du serveur de licence

Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `ansys.lic` comme suit :
```bash title="~/.licenses/ansys.lic"
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
```

#### Licence

Pour connaître le nombre de licences utilisées qui sont associées à votre nom d'utilisateur et le nombre de licences utilisées par tous les utilisateurs, lancez

```bash
ssh graham.computecanada.ca
module load ansys
lmutil lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER"
```

```bash
#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-06:00       # Specify time limit dd-hh:mm
#SBATCH --ntasks=16           # Specify total number cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load ansys/2020R1

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

!!! note
    Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur gra-vdi), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `pkill -9 -e -u $USER -f "ansys"` pour libérer vos licences. Prenez note que gra-vdi possède deux nœuds (gra-vdi3 et gra-vdi4) qui vous sont assignés au hasard quand vous vous connectez avec tigervnc; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (gra-vdi3.sharcnet.ca ou grav-vdi4.sharcnet.ca) quand vous vous connectez.

## Additive Manufacturing

Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

### Activer Additive

Nous décrivons ici comment obtenir l'extension ACT d'Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple ANSYSMotion, désinstallez-les à partir de votre projet.

#### Télécharger l'extension
*   Téléchargez AdditiveWizard.wbex à partir de [https://catalog.ansys.com/](https://catalog.ansys.com/).
*   Téléversez AdditiveWizard.wbex sur la grappe où vous allez l'utiliser.

#### Lancer Workbench
*   Voir la section Workbench dans [Mode graphique](#mode-graphique).
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec File -> Open.

#### Ouvrir le gestionnaire d'extensions
*   Cliquez sur la page ACT Start pour faire afficher l'onglet de la page ACT Home.
*   Cliquez sur Manage Extensions pour ouvrir le gestionnaire d'extensions.

#### Installer l'extension
*   Cliquez sur la boîte avec le signe + sous la barre de recherche.
*   Sélectionnez et installez votre fichier AdditiveWizard.wbex.

#### Charger l'extension
*   Cliquez pour sélectionner la boîte AdditiveWizard, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Load extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

#### Supprimer l'extension
*   Cliquez pour désélectionner la boîte AdditiveWizard, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Do not load as default*, ce qui empêche le chargement de l'extension pour les futures sessions.

### Exécuter Additive

#### Gra-vdi

Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing sur gra-vdi en utilisant jusqu'à 16 cœurs comme suit :

*   Lancez Workbench sur gra-vdi comme décrit ci-dessus dans *Additive Manufacturing -> Activer Additive*.
*   Cliquez sur *File -> Open* et sélectionnez *test.wbpj* puis cliquez sur *Open*.
*   Cliquez sur *View -> Reset workspace* si votre écran est gris.
*   Lancez *Mechanical, Clear Generated Data*, sélectionnez *Distributed*, spécifiez *Cores*.
*   Cliquez sur *File -> Save Project -> Solve*.

Vérifiez l'utilisation :
*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

!!! note
    Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion gra-vdi ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur gra-vdi. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (Fluent, Workbench, etc.) n'est pas correctement terminée avant que vncviewer ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

#### Grappe

Préparation du projet

Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Additive Manufacturing -> Activer Additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour Workbench dans la section [Soumettre des tâches en lot sur nos grappes](#soumettre-des-tâches-en-lot-sur-nos-grappes) ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save (Overwrite=False)`; ou 2. enregistrez une copie du fichier YOURPROJECT.wbpj d'origine et du répertoire YOURPROJECT_files correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne FilePath.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

Utilisation des ressources

Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `srun`. Le script pour 8 cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

```text
[gra-login1:~] srun --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
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

Tests de scalabilité

Une fois la tâche complétée, son *temps réel d'exécution* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le *temps réel d'exécution* diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

## Aide

La documentation officielle complète pour les versions récentes Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles que Ansys 2023R[1|2] nécessite toutefois une [connexion](https://ansyshelp.ansys.com/). La documentation pour les développeurs se trouve dans le [Portail](https://developer.ansys.com) Ansys Developer. Les ressources d'apprentissage supplémentaires incluent les [vidéos](https://www.youtube.com/@AnsysHowTo/videos) Ansys HowTo, la [plateforme pour les éducateurs](https://innovationspace.ansys.com/educator-hub/) Ansys Educator et les [séries de webinaires](https://www.ansys.com/events/ansys-academic-webinar-series) Ansys Webinar.