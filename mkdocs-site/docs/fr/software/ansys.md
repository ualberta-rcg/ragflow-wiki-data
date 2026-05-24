---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "476f308fc0bdf1f339e47a6d29c80bc4"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:39:24.237027+00:00"

tags:
  - software

keywords:
  - "openmpi"
  - "grappes"
  - "Remise en file d'attente"
  - "Licence"
  - "script Slurm"
  - "serveurs de licence locaux"
  - "trillium"
  - "Fichiers de journalisation"
  - "guide d'utilisation"
  - "SBATCH"
  - "service packs"
  - "runwb2-gui"
  - "fichier cas"
  - "scripts de soumission"
  - "Workbench"
  - "cellules par cœur"
  - "SLURM"
  - ".cas/.dat"
  - "simulation intensive"
  - "ansys"
  - "fichier de cas"
  - "soumission de tâches"
  - "Slurm"
  - "Ansys"
  - "messages d'erreur"
  - "serveur distant"
  - "gra-vdi"
  - "Compute nodes"
  - "Interface TUI"
  - "Prêt à utiliser"
  - "journal file"
  - "partitionnement du maillage"
  - ".cas.h5/.dat.h5"
  - "CC_CLUSTER"
  - "OpenMPI"
  - "nœuds de calcul"
  - "configuration requise"
  - "redémarrages"
  - "formats de fichiers"
  - "fichier de données"
  - "Paramètres de simulation"
  - "Fluent"
  - "bash script"
  - "modules Ansys"
  - "conception 3D et simulation"
  - "fichier de journalisation"
  - "calcul parallèle"
  - "ANSYS-FLUENT"
  - "version Ansys"
  - "serveur CMC"
  - "fichier de licence"
  - "simulations Fluent"
  - "nombre de cœurs"
  - "interface graphique de Fluent"
  - "nombre de pas"
  - "compatibilité des versions"
  - "établissement"
  - "vérifier la licence"
  - "module Ansys"
  - "Intel MPI"
  - "grep"
  - "Slurm batch script"
  - "simulation"
  - "Script bash"
  - "solveur parallèle"
  - "coupe-feu"
  - "fichier ansys.lic"
  - "grappe"
  - "Redémarrage"
  - "paquet Ansys"
  - "machinefile"
  - "ordonnanceur Slurm"
  - "configuration"
  - "fluent"
  - "redémarrage"
  - "Plusieurs nœuds"
  - "serveur de licence"
  - "Job submission"
  - "ANSYS Fluent"
  - "Ansys Fluent"
  - "script Bash"
  - "temps d'exécution"
  - "serveur de licence ANSYS"
  - "grappes de calcul"

questions:
  - "Qu'est-ce que la suite logicielle Ansys et quelles applications spécifiques inclut-elle ?"
  - "Comment fonctionne la politique d'accès et de gestion des licences Ansys sur les grappes de calcul ?"
  - "Quelles sont les étapes techniques pour configurer son propre fichier de licence ou utiliser un serveur de licence local ?"
  - "Quelle étape préalable concernant les coupe-feu est nécessaire avant d'utiliser le serveur de licence local ?"
  - "Quelles directives faut-il suivre si la configuration des coupe-feu est déjà terminée ?"
  - "À quel paragraphe doit-on se référer si la configuration des coupe-feu reste à faire ?"
  - "Quelles sont les trois informations de base nécessaires pour configurer un serveur de licence ANSYS déjà prêt à être utilisé ?"
  - "Quelles données et vérifications supplémentaires sont requises si le serveur de licence n'a jamais été configuré pour la grappe cible ?"
  - "Comment peut-on tester et vérifier que le fichier de licence ansys.lic fonctionne correctement avant de soumettre des tâches ?"
  - "Quelle commande est recommandée pour lancer Workbench lors de l'utilisation d'un serveur distant ?"
  - "Quel fichier spécifique le script enveloppant `runwb2-gui` lit-il pour gérer les licences ?"
  - "Quel est l'avantage principal de l'option interactive du serveur CMC concernant la configuration des licences ?"
  - "Comment doit-on configurer l'environnement au démarrage de Fluent 2025R1 dans Workbench pour éviter l'avertissement lié à l'accélération matérielle ?"
  - "Quelles sont les limites de cœurs et de mémoire à respecter lors de l'utilisation de Mechanical et Fluent sur gra-vdi afin d'éviter l'arrêt du programme ou le gaspillage de licences ?"
  - "Quelles sont les étapes de dépannage en cas de blocage de l'interface graphique d'Ansys et comment fonctionne la compatibilité des fichiers entre les différentes versions du logiciel ?"
  - "Quelles sont les restrictions actuelles liées aux serveurs de licence pour l'utilisation des versions les plus récentes d'Ansys, telles que la 2025R1.02 ?"
  - "Comment fonctionne la nomenclature des modules Ansys à partir de 2024 pour identifier et charger des correctifs (service packs) spécifiques ?"
  - "Pourquoi faut-il utiliser des directives particulières pour soumettre des tâches parallèles avec Ansys sur les grappes gérées par l'ordonnanceur Slurm ?"
  - "Quels sont les risques encourus lors de l'utilisation d'une version antérieure du logiciel pour exécuter une simulation ?"
  - "Comment peut-on identifier la version d'Ansys utilisée pour créer un fichier cas Fluent si on l'a oubliée ?"
  - "Quelles commandes spécifiques permettent d'extraire les informations de version à partir des fichiers de simulation ?"
  - "Pourquoi faut-il utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle ?"
  - "Quelle solution est proposée dans le texte pour soumettre des tâches parallèles sur les différentes grappes ?"
  - "Quelle est l'exception mentionnée concernant l'utilisation de ces scripts de soumission sur la grappe Niagara ?"
  - "Quelles sont les étapes préalables requises pour préparer, exporter et transférer les fichiers d'une tâche Ansys Fluent vers la grappe de calcul ?"
  - "Comment peut-on automatiser la remise en file d'attente en cas de manque de licence, et quelles précautions faut-il prendre pour éviter de gaspiller du temps de calcul ?"
  - "Quelles sont les différences de performance et de stabilité entre l'utilisation de scripts Slurm \"par nœud\" et \"par cœur\", notamment en ce qui concerne le partitionnement du maillage ?"
  - "Quelles sont les différences de configuration Slurm entre l'allocation des ressources par nœud et l'allocation par cœur pour exécuter ANSYS Fluent ?"
  - "Comment les scripts gèrent-ils les spécificités des différentes grappes de calcul (comme Narval et Nibi) lors de l'initialisation de l'environnement MPI ?"
  - "Quels sont les paramètres et variables requis par la commande `fluent` pour lancer correctement une simulation en mode batch selon ces scripts ?"
  - "Quelle est la procédure alternative proposée pour partitionner le maillage et exécuter la tâche sur la grappe ?"
  - "Quel est l'avantage principal d'effectuer le partitionnement manuellement dans l'interface graphique de Fluent ?"
  - "Quelles sont les règles à respecter concernant le nombre de partitions et de cellules par cœur pour obtenir une efficacité optimale ?"
  - "Comment le script détermine-t-il s'il doit utiliser l'interface réseau Ethernet (-peth) ou InfiniBand (-pib) pour lancer Fluent ?"
  - "Quel est le rôle du fichier machinefile généré à partir de l'identifiant de tâche Slurm ($SLURM_JOB_ID) lors de l'exécution sur plusieurs nœuds ?"
  - "Quelles sont les directives de base nécessaires dans l'en-tête du script SBATCH pour soumettre correctement cette tâche sur la grappe Narval ?"
  - "How do the Slurm resource allocation directives differ when submitting an ANSYS Fluent job by node versus by core?"
  - "What specific version of ANSYS Fluent is required to successfully run jobs on the Trillium cluster?"
  - "How do the provided bash scripts configure the MPI execution environment differently for single-node versus multi-node jobs?"
  - "Quelles sont les vérifications de liens symboliques effectuées par le script au démarrage et que se passe-t-il s'ils sont manquants ?"
  - "Dans quels cas spécifiques est-il déconseillé d'utiliser les scripts de remise en file d'attente pour obtenir une licence ?"
  - "Comment la commande d'exécution d'ANSYS Fluent diffère-t-elle selon que la tâche utilise un seul nœud ou plusieurs nœuds ?"
  - "Which specific version of ANSYS is required to run successfully on the Trillium cluster according to the script?"
  - "What SLURM parameter is explicitly marked as required and should not be changed in this job submission script?"
  - "What are the acceptable values that can be assigned to the MYVERSION variable for specifying the solver type?"
  - "What specific environment variables and modules are loaded or modified when the script detects it is running on the \"narval\" cluster?"
  - "Under what conditions does the script configure the Intel MPI Hydra bootstrap method to use SSH?"
  - "How does the script generate the machine file required for running ANSYS-FLUENT within the Slurm job allocation?"
  - "Comment le script Slurm gère-t-il les échecs d'exécution liés aux problèmes de licence ou de simulation ?"
  - "Quelles modifications spécifiques doivent être apportées aux fichiers journaux pour permettre le redémarrage automatique d'une tâche intensive ?"
  - "De quelle manière la durée totale de la simulation et le nombre de fichiers de résultats sont-ils calculés en fonction des redémarrages ?"
  - "Pourquoi est-il recommandé de choisir l'option 1 plutôt que la 2 lors d'une reprise à partir d'une solution précédente ?"
  - "Comment calcule-t-on la durée totale de la simulation et le nombre de fichiers de résultats générés si l'option 2 est choisie ?"
  - "Quelle contrainte doit être prise en compte lors de la définition du temps d'exécution demandé dans le script Slurm ?"
  - "Quel est l'objectif principal de ce script SLURM et quel logiciel de simulation permet-il d'exécuter ?"
  - "Comment le script gère-t-il le redémarrage automatique des simulations à l'aide des tâches en tableau (arrays) et des fichiers de sauvegarde ?"
  - "De quelle manière le script adapte-t-il les paramètres d'exécution MPI en fonction de la grappe de calcul utilisée (comme Narval ou Nibi) et du nombre de nœuds ?"
  - "Quel est l'objectif principal du script \"script-flu-bycore+restart.sh\" pour la configuration à plusieurs nœuds ?"
  - "Comment le script gère-t-il la réussite d'une tâche et l'annulation des autres tâches de la grappe Slurm ?"
  - "Quelles commandes sont utilisées pour extraire le dernier fichier de données et vérifier les fichiers de sortie ?"
  - "Comment le script SLURM fourni gère-t-il le redémarrage automatique d'une simulation à l'aide des tableaux de tâches (job arrays) ?"
  - "Quel est le rôle principal des fichiers de journalisation (fichiers journal) dans ANSYS Fluent selon les explications du texte ?"
  - "Quelle est la différence de format de fichier par défaut entre les versions de Fluent antérieures à 2019R3 et les versions à partir de 2020R1 ?"
  - "Quel document doit-on consulter pour obtenir plus d'informations et connaître la liste des commandes de Fluent ?"
  - "Quelle commande permet de configurer l'utilisation des formats de fichiers classiques (.cas/.dat) par défaut pour les versions jusqu'à 2019R3 ?"
  - "Quels sont les formats de fichiers les plus efficaces introduits pour les versions à partir de 2020R1 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

La suite [Ansys](http://www.ansys.com/) est un ensemble de logiciels pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

# Licence

La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas de licence qui permette un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez la légalité de leur utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence

Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire `~`.
Pour indiquer votre propre serveur de licence, créez un fichier nommé `~/.licenses/ansys.lic` qui contient la ligne ci-dessous, où vous remplacez `FLEXPORT` et `LICSERVER` par les valeurs de votre serveur.

```bash title="FILE: ansys.lic"
setenv("ANSYSLMD_LICENSE_FILE", "FLEXPORT@LICSERVER")
```

Les valeurs correspondant aux serveurs de licence CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un serveur différent, voir [Serveurs de licence locaux](#serveurs-de-licence-locaux) ci-dessous.

| Licence   | Grappe                     | LICSERVER              | FLEXPORT | INTEPORT | VENDPORT | NOTES                                |
| :-------- | :------------------------- | :--------------------- | :------- | :------- | :------- | :----------------------------------- |
| CMC       | beluga                     | `10.20.73.21`          | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC       | cedar                      | `172.16.0.101`         | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC       | graham                     | `10.25.1.56`           | `6624`   | `2325`   | s.o.     | nouvelle IP le 21 février 2025       |
| CMC       | narval                     | `10.100.64.10`         | `6624`   | `2325`   | s.o.     | aucune                               |
| SHARCNET  | beluga/cedar/graham/gra-vdi/nibi/narval/rorqual | `license3.sharcnet.ca` | `1055`   | `2325`   | n/a      | None                                 |
| SHARCNET  | niagara                    | `localhost`            | `1055`   | `2325`   | `1793`   | aucune                               |

### Serveurs de licence locaux

Avant que le serveur de licence de votre établissement puisse être utilisé, les coupe-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans le paragraphe *Prêt à utiliser* ci-dessous. Autrement, référez-vous au paragraphe *Configuration requise* un peu plus bas.

#### Prêt à utiliser

Pour utiliser un serveur de licence ANSYS déjà configuré pour être utilisé sur la grappe où vous allez soumettre des tâches, contactez votre administrateur de serveur de licences Ansys et obtenez les trois éléments d'information suivants :
1.  le nom d'hôte complet (`LICSERVER`) du serveur
2.  le port flex (`FLEXPORT`) pour Ansys, habituellement 1055
3.  le port d'interconnexion (`INTEPORT`), habituellement 2325
Une fois les trois éléments d'information collectés, configurez votre fichier `~/.licenses/ansys.lic` en entrant les valeurs de `LICSERVER`, `FLEXPORT` et `INTEPORT` dans le modèle `FILE: ansys.lic` ci-dessus.

#### Configuration requise

Si votre serveur de licence Ansys local n'a jamais été configuré pour être utilisé sur la ou les grappes où vous allez soumettre des tâches, en plus des 3 éléments ci-dessus, vous devrez ÉGALEMENT obtenir les éléments suivants auprès de l'administrateur :
4.  le numéro de port statique du fournisseur (`VENDPORT`)
5.  confirmation que `servername` se résoudra à la même adresse IP que `LICSERVER` sur nos grappes
où `servername` peut être trouvé dans la première ligne du fichier de licence avec le format `SERVER <servername> <host id> <lmgrd port>`. L'élément 5 est obligatoire, sinon les extractions de licences Ansys ne fonctionneront sur aucune grappe distante. S'il s'avère que `servername` ne répond pas à cette exigence, demandez à votre administrateur de licence de remplacer `servername` par le même nom d'hôte complet que `LICSERVER` ou au moins par un nom d'hôte qui se résoudra à la même adresse IP que `LICSERVER` à distance.

## Vérifier la licence

Pour vérifier si `ansys.lic` est bien configuré et fonctionne correctement, copiez et collez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches. La seule différence est de spécifier `YOURUSERID`. Si le logiciel n’est pas à jour sur le serveur de licence distant, un problème peut survenir si la dernière version du module Ansys est chargée pour effectuer des tests. Pour que la licence fonctionne quand des tâches sont soumises, assurez-vous que la même version du module Ansys qui est chargé par votre script est utilisée dans les commandes ci-dessous.

```bash
[gra-login:~] cd /tmp
[gra-login:~] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[gra-login:~] module load StdEnv/2023; module load ansys/2023R2
[gra-login:~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE 1> /dev/null && echo Success || echo Fail
```

```bash
[login-node:~] cd /tmp
[login-node:/tmp] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[compute-node/tmp] module load StdEnv/2023; module load ansys/2025R2.04
[compute-node:/tmp] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```

Le résultat **Success** indique que les extractions de licences devraient fonctionner lorsque les tâches sont soumises à la file d'attente.
Le résultat **Fail** indique un problème quelque part dans la configuration des licences et les tâches échoueront probablement.

!!! note "Remarque 1"
    Pour les modules Ansys installés localement, la commande `runwb2` de `SnEnv` utilise par défaut le serveur de licence SHARCNET, tel que défini dans le fichier du module Ansys que vous chargez. Pour utiliser un serveur distant, lancez plutôt Workbench avec `runwb2-gui`, car ce script enveloppant (*wrapper*) lira votre fichier `~/.licenses/ansys.lic` comme les modules disponibles sous `StdEnv/2023`. De plus, l'option interactive d'utilisation du serveur CMC (acheminé via le serveur SHARCNET CMC CadPASS) sera proposée, éliminant ainsi la nécessité de le configurer dans votre fichier ansys.lic.

!!! note "Remarque 2"
    Lorsque vous démarrez Fluent à partir de Workbench avec la version 2025R1, avant de cliquer sur le bouton *Start*, cliquez sur l'onglet *Environment* du panneau de lancement de *Fluent Launcher* et copiez/collez `HOOPS_PICTURE=opengl` dans le champ de saisie vide. Vous pouvez aussi définir `export HOOPS_PICTURE=opengl` dans votre environnement avant de démarrer Workbench. L'une ou l'autre de ces actions empêchera le message suivant, qui apparaîtrait dans les messages de démarrage de l'interface utilisateur : `[Warning: Software rasterizer found, hardware acceleration will be disabled.]`

!!! note "Remarque 3"
    Lorsque vous exécutez Mechanical dans Workbench sur `gra-vdi`, assurez-vous de cocher *Distributed* dans le panneau *Solver* du ruban supérieur et de spécifier une valeur maximale de **24 cœurs**. Lorsque vous exécutez Fluent sur `gra-vdi`, ne cochez pas *Distributed* et spécifiez une valeur maximale de **12 cœurs**. N'essayez pas d'utiliser plus de 128Go de mémoire, sinon Ansys atteindra la limite et sera arrêté. Si vous avez besoin de plus de cœurs ou de mémoire, utilisez un nœud de calcul sur une grappe pour exécuter votre session graphique (comme décrit dans la section *Nœuds de calcul* ci-dessus). Lorsque vous effectuez une ancienne tâche de prétraitement ou de post-traitement avec Ansys sur `gra-vdi` et que vous n'exécutez pas de calcul, utilisez uniquement **4 cœurs**, sinon les licences HPC seront extraites inutilement.

!!! note "Remarque 4"
    Dans de très rares cas, l'interface graphique de Workbench ou de certains programmes qu'il exécute se bloquent ou ne démarrent pas correctement, notamment si vnsviewer se déconnecte avant que Ansys soit fermé correctement. En général, si Ansys ne fonctionne pas correctement, ouvrez une nouvelle fenêtre de terminal sur `gra-vdi` et exécutez `pkill -9 -e -u $USER -f "ansys|fluent|mwrpcss|mwfwrapper|ENGINE|mono"` pour arrêter complètement tous les processus Ansys. Si le problème persiste et que vous utilisiez l'interface graphique sur des nœuds de calcul avant de travailler sur `gra-vdi`, essayez d'exécuter `rm -rf .ansys`. Si le problème concerne `/home`, `/project` ou `/scratch` (la commande df bloque), il est fort probable qu'Ansys recommence à fonctionner normalement une fois le problème de stockage résolu.

```bash
[compute-node:/tmp] fluent -g 2d -n 2
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

# Compatibilité des versions

Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une version moins récente de Ansys devraient pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec `ansys/2022R2` devrait fonctionner avec `ansys/2023R2`, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
$ grep -ia fluent combustor.cas
   (0 "fluent15.0.7  build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
   ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge

## Ansys Fluent

Voici la procédure habituelle pour utiliser Fluent avec les grappes de Calcul Canada :

## Nouveautés

Ansys publie régulièrement des *service packs* pour regrouper plusieurs mises à jour apportant différents correctifs et améliorations à ses versions majeures. Des informations similaires pour les versions précédentes peuvent généralement être trouvées sur [le blog Ansys](https://www.ansys.com/blog), en utilisant la barre de recherche FILTERS. Par exemple, la recherche de `What’s New Fluent 2024 gpu` affichera le document [What’s New for Ansys Fluent in 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1) qui contient une multitude d'informations sur la prise en charge des GPU. Spécifier un numéro de version dans le champ de recherche [Press Release](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations sur les nouvelles versions. Le module `ansys/2025R1.02` pour la dernière version de Ansys a été installé récemment; pour l'utiliser cependant, vous avez besoin d'un serveur de licence comme celui de CMC. La mise à jour du serveur de licence de SHARCNET est en cours et tant que ce travail ne sera pas terminé, seules les versions `ansys/2024R2.04` ou moins récentes seront prises en charge. Si un module pose problème ou pour demander l'installation d'une nouvelle version, écrivez au [soutien technique](../support/technical_support.md).

## Correctifs

À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *service pack* est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun *service pack* peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le *service pack* 3 peut être chargé avec `module load ansys/2024R1.03`. Si un *service pack* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *service pack* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *service pack* installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les *service packs* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *service pack* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *service pack* rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque *service pack* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

# Soumettre des tâches en lot sur nos grappes

Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

## Ansys Fluent

La procédure suivante est habituellement utilisée pour exécuter Fluent sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *File > Export > Case…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `FFF-1.cas.gz`.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *File > Export > Data…* ou trouvez-le dans le même répertoire `/project` (`FFF-1.dat.gz`).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage) de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `FFF-1.*` ou renommez-les au téléversement.
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

#SBATCH --account=def-group   # Indiquez le nom du compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Indiquez le nombre de nœuds de calcul (Narval : 1 nœud max)
#SBATCH --ntasks-per-node=32  # Indiquez le nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Indiquez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne pas modifier

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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

#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval : 1 nœud max)
#SBATCH --ntasks=16           # Indiquez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Indiquez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne pas modifier

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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

#SBATCH --account=def-group   # Indiquez le nom du compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Indiquez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=64  # Indiquez le nombre de cœurs par nœud (Narval : 64 ou moins)
#SBATCH --mem=0               # Ne pas modifier (allouer toute la mémoire par nœud de calcul)
#SBATCH --cpus-per-task=1     # Ne pas modifier

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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

#SBATCH --account=def-group   # Indiquez le nom du compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks=16           # Indiquez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Indiquez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne pas modifier

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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

#SBATCH --account=def-group      # Indiquez le nom du compte
#SBATCH --time=00-03:00          # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1                # Indiquez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=16     # Indiquez le nombre de cœurs par nœud (max 192 sur Trillium)
##SBATCH --mem=0                 # Ne pas décommenter (par défaut Trillium utilise toute la mémoire par nœud)
#SBATCH --cpus-per-task=1        # Ne pas modifier (paramètre requis)

cd $SLURM_SUBMIT_DIR             # Soumettez depuis $SCRATCH/some/dir

module load StdEnv/2023          # Ne pas modifier
module load ansys/2025R2.04      # seule la version 2025R2 ou plus récente fonctionne sur Trillium

MYJOURNALFILE=sample.jou         # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                     # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ ! -L "$HOME/.ansys" ]; then
  echo "ERROR: Un lien vers un répertoire .ansys inscriptible n'existe pas."
  echo 'Supprimez ~/.ansys s’il existe, puis exécutez : ln -s $SCRATCH/.ansys ~/.ansys'
  echo "Ensuite, essayez de soumettre à nouveau votre tâche. Annulation de la tâche actuelle!"
elif [ ! -L "$HOME/.fluentconf" ]; then
  echo "ERROR: Un lien vers un répertoire .fluentconf inscriptible n'existe pas."
  echo 'Supprimez ~/.fluentconf s’il existe et exécutez : ln -s $SCRATCH/.fluentconf ~/.fluentconf'
  echo "Ensuite, essayez de soumettre à nouveau votre tâche. Annulation de la tâche actuelle!"
elif [ ! -L "$HOME/.flrecent" ]; then
  echo "ERROR: Un lien vers un fichier .flrecent inscriptible n'existe pas."
  echo 'Supprimez ~/.flrecent s’il existe, puis exécutez : ln -s $SCRATCH/.flrecent ~/.flrecent'
  echo "Ensuite, essayez de soumettre à nouveau votre tâche. Annulation de la tâche actuelle!"
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

:tabs:

#### Remise en file d'attente pour obtenir la licence

Les scripts suivants ne doivent être utilisés qu'avec des tâches Fluent qui sont connues pour se terminer normalement sans générer d'erreurs en sortie, mais qui nécessitent généralement plusieurs tentatives de remise en file d'attente pour obtenir les licences. Ils ne sont pas recommandés pour les tâches Fluent qui peuvent 1) s'exécuter pendant une longue période avant de planter 2) s'exécuter jusqu'à la fin mais contenir des avertissements de journalisation; dans les deux cas, les simulations seront répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente spécifié par la valeur `array` soit atteint. Pour ces types de tâches, les scripts à usage général (ci-dessus) doivent être utilisés.

=== "Plusieurs nœuds (par nœud + remise en attente)"

```bash title="script-flu-bynode+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Indiquez le nombre de nœuds de calcul (Narval : 1 nœud max)
#SBATCH --ntasks-per-node=32  # Indiquez le nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Indiquez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne pas modifier
#SBATCH --array=1-5%1         # Indiquez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est montré)

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # Indiquez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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
    echo "Tâche terminée avec succès! Sortie maintenant."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT a échoué en raison d'un problème de licence ou de simulation!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Soumission de la tâche à nouveau..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie maintenant."
    fi
fi
```

=== "Plusieurs nœuds (par cœur + remise en attente)"

```bash title="script-flu-bycore+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval : 1 nœud max)
#SBATCH --ntasks=16           # Indiquez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Indiquez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne pas modifier
#SBATCH --array=1-5%1         # Indiquez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est montré)

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # Indiquez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Indiquez le nom de votre fichier de journalisation
MYVERSION=3d                  # Indiquez 2d, 2ddp, 3d ou 3ddp

# ------- ne pas modifier les lignes ci-dessous --------

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
    echo "Tâche terminée avec succès! Sortie maintenant."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT a échoué en raison d'un problème de licence ou de simulation!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Soumission de la tâche à nouveau..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie maintenant."
    fi
fi
```

:tabs:

#### Redémarrage

Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de `sample.cas`, `sample.dat` et `sample.jou` doit être présent. Modifiez le fichier `sample.jou` pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier de journalisation avec `cp sample.jou sample-restart.jou` et modifiez le fichier `sample-restart.jou` pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `; /solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez `sample-restart.jou` en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de `sample.jou` est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt+2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1+2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

=== "Plusieurs nœuds (par nœud + redémarrage)"

```bash title="script-flu-bynode+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=07-00:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Indiquez le nombre de nœuds de calcul (Narval : 1 nœud max)
#SBATCH --ntasks-per-node=32  # Indiquez le nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Indiquez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne pas modifier
#SBATCH --array=1-5%1         # Indiquez le nombre de redémarrages de solution (2 ou plus, 5 est montré)

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # Indiquez la version (ou plus récente)

MYVERSION=3d                        # Indiquez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Indiquez le nom de votre fichier de journalisation
MYJOUFILERES=sample-restart.jou     # Indiquez le nom du fichier de journalisation de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Indiquez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Indiquez le nom du fichier dat de redémarrage

# ------- ne pas modifier les lignes ci-dessous --------

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
      echo "Redémarrage de la tâche avec le fichier de données de sortie le plus récent..."
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Tâche terminée avec succès! Sortie maintenant."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie..."
fi
```

=== "Plusieurs nœuds (par cœur + redémarrage)"

```bash title="script-flu-bycore+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval : 1 nœud max)
#SBATCH --ntasks=16           # Indiquez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Indiquez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne pas modifier
#SBATCH --array=1-5%1         # Indiquez le nombre de redémarrages (alias pas de temps) (2 ou plus, 5 est montré)

module load StdEnv/2023       # Ne pas modifier
module load ansys/2023R2      # Indiquez la version (ou plus récente)

MYVERSION=3d                        # Indiquez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Indiquez le nom de votre fichier de journalisation
MYJOUFILERES=sample-restart.jou     # Indiquez le nom du fichier de journalisation de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Indiquez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Indiquez le nom du fichier dat de redémarrage

# ------- ne pas modifier les lignes ci-dessous --------

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
  #export I_MPI_HYDRA_BOOTSTRAP=ssh    # décommentez sur beluga ou cedar
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -I $MYFILEJOU
  else
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -I $MYFILEJOURES
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
      echo "Redémarrage de la tâche avec le fichier de données de sortie le plus récent"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Tâche terminée avec succès! Sortie maintenant."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie maintenant."
fi
```

:tabs:

### Fichiers de journalisation

Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface TUI (*Text User Interface*) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le guide d'utilisation de Fluent pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `/file/cff-files yes`.

=== "Fichier de journalisation (stable, cas)"

```text title="sample1.jou"
; FICHIER DE JOURNALISATION FLUENT EXEMPLAIRE - SIMULATION STABLE
; ----------------------------------------------
; les lignes commençant par un point-virgule sont des commentaires

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Lire/écrire préférentiellement les fichiers au format hérité
/file/cff-files no

; Lire les fichiers d'entrée de cas et de données
/file/read-case-data FFF-in

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; Écraser les fichiers de sortie par défaut
/file/confirm-overwrite n

; Écrire le fichier de données de sortie final
/file/write-case-data FFF-out

; Écrire le rapport de simulation dans un fichier (facultatif)
/report/summary y "My_Simulation_Report.txt"

; Fermer Fluent correctement
/exit
```

=== "Fichier de journalisation (stable, cas + données)"

```text title="sample2.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION STABLE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Lire/écrire préférentiellement les fichiers au format hérité
/file/cff-files no

; Lire les fichiers d'entrée
/file/read-case-data FFF-in

; Écrire un fichier de données toutes les 100 itérations
/file/auto-save/data-frequency 100

; Conserver les fichiers de données des 5 dernières itérations
/file/auto-save/retain-most-recent-files y

; Écrire les fichiers de données dans le sous-répertoire de sortie (ajoute l'itération)
/file/auto-save/root-name output/FFF-out

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; écrire le dernier fichier de cas et de données en sortie
/file/write-case-data FFF-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y "My_Simulation_Report.txt"

; fermer correctement Fluent
exit
```

=== "Fichier de journalisation (temporaire)"

```text title="sample3.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION TEMPORAIRE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Lire/écrire préférentiellement les fichiers au format hérité
/file/cff-files no

; Lire le fichier de cas d'entrée
/file/read-case FFF-transient-inp

; Pour la poursuite (redémarrage), lisez les deux fichiers d'entrée de cas et de données
;/file/read-case-data FFF-transient-inp

; Écrire un fichier de données (et peut-être de cas) toutes les 100 pas de temps
/file/auto-save/data-frequency 100
/file/auto-save/case-frequency if-case-is-modified

; Conserver uniquement les 5 fichiers de données (et peut-être de cas) les plus récents
/file/auto-save/retain-most-recent-files y

; Écrire dans le sous-répertoire de sortie (ajoute le temps d'écoulement et le pas de temps)
/file/auto-save/root-name output/FFF-transient-out-%10.6f

; ##### Paramètres pour la simulation transitoire :  #####

; Définir la taille du pas de temps physique
/solve/set/time-step 0.0001

; Définir le nombre d'itérations pour lesquelles les moniteurs de convergence sont rapportés
/solve/set/reporting-interval 1

; ##### Fin des paramètres #####

; initialiser avec la méthode hybride
/solve/initialize/hyb-initialization

; indiquer le nombre maximal d'itérations par pas de temps et le nombre de pas de temps
;/solve/set/max-iterations-per-time-step 75
;/solve/dual-time-iterate 1000 ,
/solve/dual-time-iterate 1000 75

; enregistrer les derniers fichiers en sortie pour les cas et les données
/file/write-case-data FFF-transient-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y Report_Transient_Simulation.txt

; Fermer Fluent correctement
/exit
```

:tabs:

### Fonctions UDF

La première étape est de transférer vers la grappe votre UDF (*User-Defined Function*), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui elle exécute Linux. L'UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *Interpreted UDFs* et *UDF Library Manager* ne sont pas configurées pour utiliser un UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interprétée

Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilée

Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `libudf.so` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quelle autre de nos grappes, à condition que votre compte charge la même version du module d'environnement `StdEnv`. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (`load`) `libudf` ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes `libudf` (`compile` et `load`) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de *build* de type « *racetime* » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent (exécutée sur n'importe quel nœud de calcul ou sur `gra-vdi`) peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *Compiled UDFs*, et cliquez sur *Build*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

```
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

et/ou

```
define/user-defined/compiled-functions load libudf
```

#### Parallèle

Avant qu'une UDF puisse être utilisée avec une tâche parallèle Fluent (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque Fluent est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, Fluent fonctionnera lentement au mieux ou plantera immédiatement au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque Fluent est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans *Fluent Customization Manual, Part I: Chapter 7: Parallel Considerations* qui se trouve dans la [Documentation en ligne](#aide).

#### DPM

Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour *Discrete Phase Models*) comme décrit dans *2024R2 Fluent Users Guide, Part III: Solution Mode, Chapter 24: Modeling Discrete Phase, 24.2 Steps for Using the Discrete Phase Models,* et dans *2024R2 Fluent Customization Manual, Part I: Creating and Using User Defined Functions, Chapter 2: DEFINE Macros, 2.5 Discrete Phase Model (DPM) DEFINE Macros*. Avant qu'une UDF basée sur DPM puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Point Properties* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physics--> Discrete Phase*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Create*. La boîte de dialogue *Set Injection Properties* contient le menu déroulant *Injection Type* avec les quatre premiers types disponibles (*single, group, surface, flat-fan-atomizer*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Point Properties* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Point Properties* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *File* dans le menu déroulant *Injection Type*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *File* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Set Injection Properties*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension .dpm) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Select File*, sélectionnez *All Files (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur le bouton OK. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Set Injection Properties* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Discrete Phase Model* et sélectionnez *Interaction with Continuous Phase* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple :

```
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

Le résumé des options de ligne de commande peut être affiché avec **cfx5solve -help**. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, `cfx5solve` s'exécute en simple précision (*-single*). Pour exécuter `cfx5solve` en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, `cfx5solve` prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'ANSYS CFX-Solver Manager pour plus de détails.

=== "Nœud simple"

```bash title="script-local.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le nom du compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Indiquez un seul nœud de calcul (ne pas modifier)
#SBATCH --ntasks-per-node=4   # Indiquez le nombre de cœurs (maximum : Graham 44, Cedar 32 ou 48, Béluga 40, Narval 64)
#SBATCH --mem=16G             # Indiquez la mémoire du nœud (facultativement, définissez à 0 pour allouer toute la mémoire du nœud)
#SBATCH --cpus-per-task=1     # Ne pas modifier

#module load StdEnv/2020      # Décommentez pour utiliser (déprécié)
#module load 2021R2           # Spécifier 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Ou versions de module plus récentes

# ajoutez des options supplémentaires à la ligne de commande cfx5solve si nécessaire
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
else
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
fi
```

=== "Plusieurs nœuds"

```bash title="script-cfx-multiple.sh"
#!/bin/bash

#SBATCH --account=def-group   # Indiquez le nom du compte
#SBATCH --time=00-03:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --nodes=2             # Indiquez plusieurs nœuds de calcul (2 ou plus)
#SBATCH --ntasks-per-node=64  # Indiquez tous les cœurs par nœud (maximum : Graham 44, 48, Béluga 40, Narval 64)
#SBATCH --mem=0               # Utilisez toute la mémoire par nœud de calcul (ne pas modifier)
#SBATCH --cpus-per-task=1     # Ne pas modifier

#module load StdEnv/2020      # Décommentez pour utiliser (déprécié)
#module load 2021R2           # Spécifier 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Indiquez les versions de module 2022R2 ou plus récentes

NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

# ajoutez des options supplémentaires à la ligne de commande cfx5solve si nécessaire
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
else
  export I_MPI_HYDRA_BOOTSTRAP=ssh
  unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
fi
```

:tabs:

## Workbench

Initialisez le fichier de projet avant de le soumettre pour la première fois.

1.  Connectez-vous à la grappe avec [TigerVNC](../interactive/vnc.md).
2.  Dans le même répertoire où se trouve le fichier de projet (`YOURPROJECT.wbpj`), [lancez Workbench](#workbench-graphique) avec la même version du module Ansys qui a servi à créer le projet.
3.  Dans Workbench, ouvrez le projet avec *File -> Open*.
4.  Dans la fenêtre principale, faites un clic droit sur *Setup* et sélectionnez *Clear All Generated Data*.
5.  Dans la liste déroulante de la barre de menus du haut, cliquez sur *File -> Exit* pour sortir de Workbench.
6.  Dans la fenêtre contextuelle Ansys Workbench qui affiche *The current project has been modified. Do you want to save it ?* cliquez sur le bouton *No*.
7.  Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Puisqu'un nœud de calcul avec jusqu'à 96 cœurs, 768 Go de mémoire et 8 heures de temps d'exécution peut maintenant être réservé pour une session de bureau à la demande, envisagez d'exécuter vos simulations Workbench directement depuis l'interface graphique native de Workbench lorsque cela est possible, comme une option plus intuitive par rapport à la soumission de la tâche à la file d'attente avec un script Slurm.

### Scripts pour l'ordonnanceur Slurm

Pour soumettre un fichier de projet à la queue, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

=== "Nœud simple (StdEnv/2023)"

```bash title="script-wbpj-2023.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Temps (JJ-HH:MM)
#SBATCH --mem=16G                      # Mémoire totale (définir à 0 pour toute la mémoire du nœud)
#SBATCH --ntasks=4                     # Nombre de cœurs
#SBATCH --nodes=1                      # Ne pas modifier (multinœud non pris en charge)
##SBATCH --exclusive                   # Décommentez pour les tests de mise à l'échelle
##SBATCH --constraint=broadwell        # Applicable à Graham ou Cedar

module load StdEnv/2023 ansys/2023R2   # OU versions de module Ansys plus récentes

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Définir à 0 pour SMP (mémoire partagée parallèle)
else
  MEMPAR=1                             # Définir à 1 pour DMP (mémoire distribuée parallèle)
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
#SBATCH --time=00-03:00                # Temps (JJ-HH:MM)
#SBATCH --mem=16G                      # Indiquez la mémoire totale
#SBATCH --ntasks=4                     # Indiquez le nombre de cœurs
#SBATCH --nodes=1                      # Ne pas modifier (multinœud non pris en charge)
##SBATCH --exclusive                   # Décommentez UNIQUEMENT pour les tests de mise à l'échelle
##SBATCH --constraint=broadwell        # Décommentez pour spécifier un type de nœud disponible

module load StdEnv/2020 ansys/2021R2   # OU versions de module Ansys plus récentes

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Définir à 0 pour SMP (mémoire partagée parallèle)
else
  MEMPAR=1                             # Définir à 1 pour DMP (mémoire distribuée parallèle)
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

:tabs:

Pour éviter d'écrire la solution lorsqu'une tâche en cours d'exécution se termine avec succès, remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera la détermination de la performance de la simulation lorsque `#SBATCH --ntasks` est augmenté, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical

Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Tools -> Write Input Files* et en spécifiant *File name:* pour `YOURAPDLFILE.inp` et *Save as type:* pour les fichiers APDL en entrée (*.inp*). Les tâches APDL peuvent ensuite être soumises à la queue avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm

Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `##SBATCH` sont suivies d'un commentaire.

=== "Mémoire partagée parallèle (CPU)"

```bash title="script-smp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Indiquez votre compte
#SBATCH --time=00-03:00         # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem=32G               # Indiquez la mémoire pour tous les cœurs
#SBATCH --nodes=1               # Ne pas modifier
#SBATCH --tasks=8               # Indiquez le nombre de cœurs
#SBATCH --cpus-per-task=1       # Ne pas modifier

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
```

=== "Mémoire distribuée parallèle (CPU)"

```bash title="script-dmp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Indiquez votre compte
#SBATCH --time=00-03:00         # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G        # Indiquez la mémoire par cœur
##SBATCH --nodes=2              # Indiquez le nombre de nœuds (facultatif)
#SBATCH --ntasks=8              # Indiquez le nombre de cœurs
##SBATCH --ntasks-per-node=4    # Indiquez les cœurs par nœud (facultatif)
#SBATCH --cpus-per-task=1       # Ne pas modifier

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

=== "Mémoire partagée parallèle (GPU)"

```bash title="script-smp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Indiquez votre compte
#SBATCH --time=00-03:00          # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem=32G                # Indiquez la mémoire pour tous les cœurs
#SBATCH --ntasks=8               # Indiquez le nombre de cœurs
#SBATCH --nodes=1                # Ne pas modifier
#SBATCH --cpus-per-task=1        # Ne pas modifier
#SBATCH --gpus-per-node=1        # Indiquez [type_gpu:]quantité
##SBATCH --gpus-per-node=h100:1  # Temporairement requis sur mini-Graham
##SBATCH --partition=debug       # Temporairement requis sur mini-Graham

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
#SBATCH --account=def-account    # Indiquez votre compte
#SBATCH --time=00-03:00          # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G         # Indiquez la mémoire par cœur
#SBATCH --nodes=1                # Indiquez le nombre de nœuds
#SBATCH --ntasks-per-node=8      # Indiquez les cœurs par nœud
#SBATCH --cpus-per-task=1        # Ne pas modifier
#SBATCH --gpus-per-node=1        # Indiquez [type_gpu:]quantité
##SBATCH --gpus-per-node=h100:1  # Temporairement requis sur mini-Graham
##SBATCH --partition=debug       # Temporairement requis sur mini-Graham

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

:tabs:

Par défaut, Ansys alloue aux tâches APDL 1024Mo de mémoire totale et 1024Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande `mapdl` des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de mise à l'échelle avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (*SMP pour Shared Memory Parallel*) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (*DMP pour Distributed Memory Parallel*) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```bash
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
 ! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

Cette section fournit des exemples de scripts Slurm pour résoudre des simulations Rocky autonomes non couplées dans une file d'attente de grappe. Les deux scripts sont configurés avec `RESUME=0` afin que les simulations soient résolues depuis le début par défaut. Pour redémarrer une simulation partiellement complétée, définissez `RESUME=1` et soumettez le script à nouveau à la file d'attente. Pour obtenir une liste complète des options de ligne de commande, exécutez `Rocky -h` sur la ligne de commande après avoir chargé le module Ansys. Puisqu'un fichier de verrouillage est généré chaque fois qu'une simulation est lancée, une seule tâche doit être soumise à la fois à partir du même répertoire. En ce qui concerne le script à utiliser, bien que toutes les simulations doivent être testées indépendamment, pour un cas de test de base, le script basé uniquement sur le GPU s'est avéré surpasser le script basé uniquement sur le CPU d'un facteur de 3,5x. Des augmentations supplémentaires des ressources au-delà de 6 CPU (pour le script CPU seul) ou 2 CPU + 1 GPU (1/7 d'un GPU H100 pour le script basé sur le GPU) n'ont pas fourni d'accélération supplémentaire lors des tests de mise à l'échelle pour aucun des scripts. Compte tenu de ces résultats, il semble probable que le script basé sur le GPU fournira des temps de solution significativement plus rapides que l'utilisation seule des CPU pour d'autres simulations Rocky autonomes. Comme indiqué sur chaque page wiki de la grappe ou résumé sur [https://docs.alliancecan.ca/wiki/Allocations_and_compute_scheduling#Ratios_in_bundles](https://docs.alliancecan.ca/wiki/Allocations_and_compute_scheduling#Ratios_in_bundles), toutes les grappes sauf Narval disposent de GPU H100. Par conséquent, lors de l'utilisation du script GPU sur Narval, l'option `--gpus` de Slurm doit être modifiée pour demander un GPU A100. Notez qu'à ce jour, seul Rocky avec les modules `ansys/2025R2|2.04` a été testé, mais pas encore les modules `ansys/2025R1|1.02`.

### Scripts pour l'ordonnanceur Slurm

=== "CPU seulement"

```bash title="script-rocky-cpu.sh"
#!/bin/bash

#SBATCH --account=account      # Indiquez votre compte (déf ou rrg)
#SBATCH --time=00-02:00        # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem=24G              # Indiquez la mémoire totale pour les cœurs
#SBATCH --cpus-per-task=6      # Indiquez le nombre de cœurs à utiliser
#SBATCH --nodes=1              # Demandez un nœud (ne pas modifier)

module load StdEnv/2023 ansys/2025R1       # ou versions plus récentes
export PATH=$EBROOTANSYS/v251/rocky:$PATH

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0
```

=== "Basé sur GPU (générique)"

```bash title="script-rocky-gpu.sh"
#!/bin/bash

RESUME=0                                  # Indiquez 0 ou 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Supprime les résultats précédents
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
fi
```

=== "Basé sur GPU (spécifique)"

```bash title="script-rocky-gpu.sh"
#!/bin/bash

#SBATCH --account=account      # Indiquez votre compte (déf ou rrg)
#SBATCH --time=00-01:00        # Indiquez la durée (JJ-HH:MM)
#SBATCH --mem=24G              # Indiquez la mémoire (définissez à 0 pour utiliser toute la mémoire du nœud)
#SBATCH --cpus-per-task=6      # Indiquez les cœurs (Graham 32 ou 44 pour utiliser tous les cœurs)
#SBATCH --gres=gpu:v100:2      # Indiquez le type de GPU : quantité de GPU
#SBATCH --nodes=1              # Demandez un nœud (ne pas modifier)

# le module rocky2023R2 sur Graham a été renommé en ansysrocky/2023R2 le 24 avril 2025
#module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2       # disponible uniquement sur Graham
module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04   # disponible uniquement sur Graham

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE
```

:tabs:

```bash
RESUME=0                                  # Indiquez 0 ou 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Supprime les résultats précédents
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
fi
```

## Electronics

Des scripts Slurm pour utiliser AnsysEDT sont fournis sur une page wiki distincte [ici](ansysedt.md).

# Mode graphique

Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
*   [FIR](https://docs.alliancecan.ca/wiki/Fir): `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](https://docs.alliancecan.ca/wiki/Rorqual): `https://jupyterhub.rorqual.alliancecan.ca`
*   [NARVAL](https://jupyterhub.narval.alliancecan.ca/): `https://jupyterhub.narval.alliancecan.ca/`
*   [TRILLIUM](https://docs.scinet.utoronto.ca/index.php/Open_OnDemand_Quickstart): `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources requises pour votre session de bureau interactive et cliquez sur *Lancer* ou *Démarrer*. Si des graphiques accélérés ou des calculs seront effectués depuis votre session de bureau, assurez-vous de spécifier une ressource GPU. Une fois le bureau chargé, chargez un module Ansys. Si vous avez démarré un bureau propulsé par Jupyter Lab, cela peut être fait en cliquant sur le menu de gauche, ou si vous avez démarré un bureau OnDemand, tapez manuellement `module load ansys/version` sur la ligne de commande. Pour démarrer l'un des programmes Ansys courants tels que fluent, cfx, workbench, etc., consultez la section suivante qui fournit des conseils pour définir les variables d'environnement et les arguments requis par les environnements graphiques basés sur VirtualGL ou Mesa, selon qu'une ressource GPU a été spécifiée ou non.

### Fluent

Pour démarrer Ansys Fluent depuis la ligne de commande d'un bureau On Demand, ouvrez une fenêtre de terminal et exécutez les commandes :

```bash
module load StdEnv/2023 ansys/2025R1
```

```bash
fluent
```

Lorsque le panneau de sélection contextuel *Fluent Launcher* apparaît, cliquez sur l'onglet *Environment* et copiez/collez les paramètres de variables d'environnement suivants, selon que vous avez démarré votre session On Demand avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses (car ce sont des commentaires) et ne mettez pas `export` devant les noms de variables. Si la fenêtre de la console graphique est corrompue au démarrage de l'interface graphique, redémarrez Fluent en définissant `HOOPS_PICTURE=null` pour désactiver la création du panneau graphique.

**Nœud de calcul (aucun GPU demandé)**

*   `I_MPI_HYDRA_BOOTSTRAP=ssh` (requis sur Nibi)
*   `HOOPS_PICTURE=opengl2-mesa` (version 2025R1 ou plus récente)
*   `HOOPS_PICTURE=null` (version 2024R2 ou plus ancienne)

*   Cliquez sur le bouton *Start*

```bash
slurm_hl2hl.py --format ANSYS-FLUENT > machinefile
NCORES=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

fluent 3d -t $NCORES -cnf=machinefile -mpi=intel -affinity=0 -g -i sample.jou
```

NOTE : Lors de l'exécution de Fluent sur la grappe Nibi, la variable d'environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être définie manuellement; sinon, Fluent se bloquera au démarrage des sessions de bureau de calcul OOD lorsque Intel MPI est utilisé. Des messages d'erreur tels que les suivants seront générés. Si cela se produit, quittez complètement Fluent, fermez correctement Workbench et recommencez.

```
[mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```

### CFX

Lors du démarrage de CFX à partir d'un bureau On Demand, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal, selon qu'un GPU a été demandé lors du démarrage du bureau.

*   `module load StdEnv/2023 ansys/2025R1` (ou plus ancienne)
*   `cfx5 -graphics mesa` (aucun GPU demandé)
*   `cfx5 -graphics ogl` (avec GPU demandé)

### Mapdl

```bash
module load StdEnv/2023 ansys/2022R2
```

ou versions plus récentes.

```bash
mapdl -g
```

ou via le lanceur, `launcher` puis cliquer sur le bouton `RUN`.

Les étapes suivantes pour démarrer l'interface graphique Mechanical APDL à partir de la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre bureau On Demand sur un nœud de calcul avec ou sans GPU.

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `mapdl -g`, ou,
*   `launcher` puis cliquez sur le bouton `RUN`.

### Workbench

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `xfwm4 --replace &` (nécessaire seulement si vous utilisez Ansys Mechanical)
*   `export QTWEBENGINE_DISABLE_SANDBOX=1` (nécessaire seulement si vous utilisez CFD-Post)
*   `runwb2`
*   Remarque : Quand vous exécutez en parallèle un programme d'analyse comme Mechanical ou Fluent sur un nœud simple, ne cochez pas la case *Distributed* et indiquez un nombre de cœurs égal à votre **session salloc, moins 1**. Les menus déroulants du Ansys Mechanical Workbench ne répondent pas correctement. Comme solution, lancez `xfwm4 --replace` sur la ligne de commande avant de démarrer Workbench. Pour avoir `xfwm4` par défaut, modifiez `~/.vnc/xstartup` et remplacez `mate-session` par `xfce4-session`.

Cette section montre comment démarrer Workbench (et éventuellement Fluent) sur un bureau On Demand ou un bureau Jupyter Lab.

## Problèmes avec SSH

Certains programmes d'interface graphique ANSYS peuvent être exécutés à distance sur un nœud de calcul d'une de nos grappes par redirection X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge, car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que MobaXterm. La plupart d'entre vous trouveront les temps de réponse interactifs inacceptables pour les tâches de menu de base, sans parler de l'exécution de tâches plus complexes telles que celles nécessitant du rendu graphique. Les temps d'attente pour démarrer des programmes avec interface graphique peuvent également être très longs, dépendant de votre connexion Internet. Dans un test par exemple, il a fallu 40 minutes pour obtenir l'interface graphique avec SSH alors que `vncviewer` n'a pris que 34 secondes. Malgré la lenteur potentielle lors de la connexion via SSH pour exécuter des programmes avec interface graphique, cela peut toujours être intéressant si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou d'exécuter des calculs. Ces étapes de base sont un point de départ :

1.  `ssh -Y username@graham.computecanada.ca`
2.  `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task =4 [--gpus-per-node=1] --account=def-mygroup`
3.  une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, chargez le module Ansys souhaité et essayez d'exécuter le programme.

### Fluids

*   `module load CcEnv StdEnv/2023`
*   `module load ansys/2024R2.04` (ou versions moins récentes)
*   `unset SESSION_MANAGER`
*   `fluent | cfx5 | icemcfd`
    *   La commande `unset SESSION_MANAGER` permet d'éviter le message d'erreur suivant au lancement de Fluent.
    *   `[Qt: Session management error: None of the authentication protocols specified are supported]`
    *   Si le message suivant est affiché au lancement de `icemcfd`...
    *   `[Error segmentation violation - exiting after doing an emergency save]`
    *   ... ne cliquez pas sur le bouton OK, autrement `icemcfd` va planter. Faites plutôt ce qui suit (une seule fois) :
    *   sélectionnez *onglet Paramètres -> Affichage -> cochez X11 -> Appliquer -> OK -> Fichier -> Quitter*
    *   L'erreur ne devrait pas se produire quand vous démarrez de nouveau `icemcfd`.

### Workbench

### Rocky

*   `module load clumod ansysrocky/2023R2 CcEnv StdEnv/2020 ansys/2023R2`, ou
*   `module load clumod ansysrocky/2024R2.0 CcEnv StdEnv/2023 ansys/2024R2.04`, ou
*   `module load CcEnv StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit `~/.licenses/ansys.lic`
*   `Rocky-gui` Fournit par les modules ansysrocky locaux la sélection des serveurs CMC ou SHARCNET
*   `RockySolver` Exécute le solveur rocky à partir de la ligne de commande (l'ajout de `-h` pour *help* n'est pas testé)
*   `RockySchedular` Lance l'interface graphique pour soumettre et exécuter des tâches sur le nœud courant (non testé)
*   Rocky pour 2024R2 et moins récentes est disponible uniquement sur `gra-vdi` et Graham clusters; l'installation sur toutes les grappes est prévue pour juin
*   Rocky pour 2025R1 et plus récentes est fourni sur toutes les grappes par le module ansys (pas pris en charge par le serveur de licence SHARCNET)
*   Rocky ne peut utiliser que des CPU sur `gra-vdi` puisqu'il n'y a présentement qu'un seul GPU dédié aux graphiques
*   La licence SHARCNET inclut maintenant Rocky dont l'utilisation est sans frais pour la recherche
*   Voir la page [Rocky Innovation Space](https://innovationspace.ansys.com/ais-rocky/)
*   Pour des détails voir [Ansys Rocky 2024 R2 Release Highlights](https://innovationspace.ansys.com/knowledge/forums/topic/ansys-rocky-2024-r2-release-highlights/) et [Ansys Rocky 2025 R1 Release Highlights](https://innovationspace.ansys.com/knowledge/forums/topic/ansys-rocky-2025-r1-release-highlights/)

### Ansys EDT

*   Ouvrez une fenêtre de terminal et chargez le module avec
    *   `module load SnEnv ansysedt/2023R2`, ou
    *   `module load SnEnv ansysedt/2021R2`
*   Dans le terminal, entrez `ansysedt` et attendez que l'interface s'affiche.
*   Ceci doit être fait une seule fois :
    *   sélectionnez *Outils -> Options -> HPC et options d'analyse -> Options*
    *   dans le menu déroulant, changez *Licence HPC* pour **Pool** (pour utiliser plus de 4 cœurs)
    *   cliquez sur *OK*
*   ----------   EXEMPLES  ----------
*   Pour copier dans votre compte les exemples Antennas de 2023R2 :
    *   connectez-vous à une grappe (par exemple Graham)
    *   `module load ansysedt/2023R2`
    *   `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; cd ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf Antennas`
    *   `cp -a $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
*   Pour faire exécuter un exemple :
    *   ouvrez un fichier `.aedt` et cliquez sur *HFSS -> Vérification de la validation*
    *   (si la validation produit une erreur, fermez et ouvrez de nouveau la simulation autant de fois que nécessaire)
    *   pour lancer la simulation, cliquez sur *Projet -> Analyser tout*
    *   pour quitter sans sauvegarder la solution, cliquez sur *Fichier -> Fermer -> Non*
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
*   `unset SESSION_MANAGER; launcher` puis cliquer sur le bouton `RUN`.

Si `I_MPI_HYDRA_BOOTSTRAP=ssh` n'est pas correctement défini sur Nibi lorsque Fluent est démarré à partir des sessions de bureau de calcul OOD et que Intel MPI est utilisé, Fluent se bloquera au démarrage et produira le message d'erreur suivant. Si cela se produit, quittez complètement Fluent, fermez Workbench, puis recommencez.

```
[mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```

### Rocky

*   `module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2`
*   `module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04`
*   `module load StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit le `~/.licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules locaux `ansysrocky` permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de `-h` pour *help* n'est pas testé).
*   `RockySchedular`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions 2024R2 ou moins récentes ne fonctionnent que sur `gra-vdi` et Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions 2025R1 et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore pris en charge par le serveur de licence SHARCNET).
*   Le serveur de licence SHARCNET inclut Rocky; son utilisation est gratuite pour la recherche.
*   Rocky prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 CPU et 1 GPU pour un maximum de 8 heures, lancez
    `salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount`

**Nœud de calcul (aucun GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu de gauche du bureau.
*   Cliquez sur l'icône *Workbench (VNC)* située dans la fenêtre centrale du bureau Jupyter Lab.
    *   Si les graphiques de toute application (telle que Fluent) démarrée dans Workbench
    *   apparaissent inutilisables en raison de graphiques corrompus, essayez d'effectuer les
    *   étapes suivantes. Elles créeront une icône de bureau `runwb2` personnalisée afin
    *   que Workbench puisse être démarré en mode Mesa. Si l'une des applications que vous
    *   démarrerez dans Workbench est Fluent, alors lorsque le lanceur Fluent démarre, vous
    *   pouvez également essayer de définir la variable `HOOPS_PICTURE=opengl2-mesa` dans la fenêtre du lanceur Fluent.
*   Pour continuer, quittez Workbench, puis ouvrez une fenêtre de terminal. Copiez-collez la commande suivante
*   dans le presse-papiers distant situé dans le coin supérieur droit de votre bureau Jupyter.
*   Maintenant, les commandes peuvent être collées dans le terminal, par exemple :
*   `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop`
*   Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que `nano` en faisant ce qui suit :
*   `nano ~/Desktop/workbench-mesa.desktop`. Modifiez toutes les instances de `runwb2`
*   par `runwb2 -oglmesa` puis quittez l'éditeur en enregistrant les modifications. Maintenant, ACTUALISEZ
*   le bureau Jupyter en appuyant sur la combinaison de touches *Control-R*. La nouvelle icône devrait maintenant
*   apparaître sur le bureau avec l'icône originale de Workbench. Double-cliquez dessus pour démarrer Workbench.
*   La nouvelle icône persistera pour les sessions futures jusqu'à ce qu'elle soit supprimée manuellement avec la commande
*   `rm -f ~/Desktop/workbench-mesa.desktop`.

**Nœud de calcul (avec GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu de gauche du bureau.
*   Cliquez sur l'icône *Workbench (VNC)* située dans la fenêtre centrale du bureau Jupyter Lab.

### Ensight

*   `module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6`
*   `export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib`
*   `ensight -X`

### Electronics

Des informations décrivant comment exécuter AnsysEDT en mode graphique peuvent être trouvées [ici](ansysedt.md).

# Particularités selon le site d'utilisation

## Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de ***recherche universitaire publiable***; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Multiphysics Campus Solution en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio).
Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par ANSYS en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences `anshpc` de 1986 est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50% en CPU seront probablement signalées par le système et examinées par notre équipe technique.

```bash
unset SLURM_GTIDS
```

Depuis décembre 2022, chaque utilisateur peut exécuter 4 travaux en utilisant un total de 252 `anshpc` (plus 4 `anshpc` par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon (`(252 + 4 * nombre de tâches) / nombre de tâches`). **MISE À JOUR :** En octobre 2024, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

#### Fichier du serveur de licence

Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `ansys.lic` comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
```

#### Interroger les licences

Pour connaître le nombre de licences utilisées qui sont associées à votre nom d'utilisateur et le nombre de licences utilisées par tous les utilisateurs, lancez

```bash
ssh graham.computecanada.ca
module load ansys
lmutil lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER"
```

```bash
#SBATCH --account=def-group   # Indiquez le compte
#SBATCH --time=00-06:00       # Indiquez la limite de temps jj-hh:mm
#SBATCH --ntasks=16           # Indiquez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Indiquez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne pas modifier

module load ansys/2020R1
```

```
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

Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur `gra-vdi`), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `pkill -9 -e -u $USER -f "ansys"` pour libérer vos licences. Prenez note que `gra-vdi` possède deux nœuds (`gra-vdi3` et `gra-vdi4`) qui vous sont assignés au hasard quand vous vous connectez avec `tigervnc`; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (`gra-vdi3.sharcnet.ca` ou `gra-vdi4.sharcnet.ca`) quand vous vous connectez.

# Fabrication additive

Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

## Activer la fabrication additive

Nous décrivons ici comment obtenir l'extension ACT de Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple ANSYSMotion, désinstallez-les à partir de votre projet.

### Télécharger l'extension

*   téléchargez `AdditiveWizard.wbex` à partir de <https://catalog.ansys.com/>
*   téléversez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser

### Lancer Workbench

*   Voir la section Workbench dans [Mode graphique plus haut](#workbench-graphique).
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec *File -> Open*.

### Ouvrir le gestionnaire d'extensions

*   Cliquez sur la page *Démarrage ACT* pour faire afficher l'onglet de la page *Accueil ACT*.
*   Cliquez sur *Gérer les extensions* pour ouvrir le gestionnaire d'extensions.

### Installer l'extension

*   Cliquez sur la boîte avec le signe + sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

### Charger l'extension

*   Cliquez pour sélectionner la boîte AdditiveWizard, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Charger l'extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

### Supprimer l'extension

*   Cliquez pour désélectionner la boîte AdditiveWizard, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Ne pas charger par défaut*, ce qui empêche le chargement de l'extension pour les futures sessions.

## Exécuter la fabrication additive

### Gra-vdi

Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing sur `gra-vdi` en utilisant jusqu'à 16 cœurs comme suit :

*   Lancez Workbench sur `gra-vdi` comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*.
*   Cliquez sur *Fichier -> Ouvrir* et sélectionnez `test.wbpj` puis cliquez sur *Ouvrir*.
*   Cliquez sur *Affichage -> Réinitialiser l'espace de travail* si votre écran est gris.
*   Lancez *Mechanical, Effacer les données générées*, sélectionnez *Distribué*, spécifiez *Cœurs*.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

Vérifiez l'utilisation :

*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion `gra-vdi` ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur `gra-vdi`. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (Fluent, Workbench, etc.) n'est pas correctement terminée avant que `vncviewer` ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

### Grappe

Préparation du projet

Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour Workbench dans la section *Soumettre des tâches en lot sur nos grappes* ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)`; ou 2. enregistrez une copie du fichier `YOURPROJECT.wbpj` d'origine et du répertoire `YOURPROJECT_files` correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne FilePath.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

Utilisation des ressources

Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `srun`. Le script pour 8 cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

```bash
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

Une fois la tâche complétée, son *temps d'exécution réel (Wall-clock time)* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le *Wall-clock time* diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

# Aide

La documentation officielle complète pour les versions récentes Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles que Ansys 2023R[1|2] nécessite [une connexion](https://ansyshelp.ansys.com/). La documentation pour les développeurs peut être trouvée sur le [portail](https://developer.ansys.com) Ansys Developer. Des ressources d'apprentissage supplémentaires incluent les [vidéos](https://www.youtube.com/@AnsysHowTo/videos) Ansys HowTo, le [centre pour éducateurs](https://innovationspace.ansys.com/educator-hub/) Ansys Educator et les [séries de webinaires](https://www.ansys.com/events/ansys-academic-webinar-series) Ansys Webinar.

```bash
#module load ansys/2021R1
module load ansys/2021R2