---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "e6a7f83bab85bd4eab1806d10dacd689"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:13:35.447091+00:00"

tags:
  - software

keywords:
  - "Configuration"
  - "Serveur de licence"
  - "redémarrages"
  - "compte utilisateur"
  - "Partitionnement du maillage"
  - "interface TUI"
  - "interface graphique de Fluent"
  - "simulations Fluent"
  - "Script bash"
  - "fluent"
  - "ansys"
  - "batch script"
  - "ordonnanceur Slurm"
  - "narval"
  - "Compatibilité des versions"
  - "licence"
  - "nœuds"
  - "Nœuds de calcul"
  - "OpenMPI"
  - "durée totale de la simulation"
  - "pas de temps"
  - "Ordonnanceur Slurm"
  - "Slurm"
  - "SBATCH"
  - "Ansys Electronics Desktop"
  - "remise en file d'attente"
  - "redémarrage"
  - "grappes"
  - "Script Bash"
  - "trillium"
  - "Ansys Mechanical/Fluids"
  - "bash"
  - "cellules par cœur"
  - "salloc"
  - "ANSYS Fluent"
  - "module load"
  - "configuration"
  - "script Slurm"
  - "Ansys Fluent"
  - "Workbench"
  - "nombre de cœurs"
  - ".cas.h5/.dat.h5"
  - "Fluent"
  - "solveur parallèle"
  - "Grappe de calcul"
  - "ansys/2025R2.04"
  - "calcul parallèle"
  - "service packs"
  - "SLURM"
  - "Simulation"
  - "Ansys"
  - "journal file"
  - "serveur de licence"
  - "guide d'utilisation"
  - "version antérieure"
  - "suite Ansys"
  - "ANSYS"
  - "openmpi"
  - "Plusieurs nœuds"
  - "compute nodes"
  - "Grappe"
  - "Redémarrage"
  - "fichiers de journalisation"
  - "grappes de calcul"
  - "Fichier de cas"
  - "Intel MPI"
  - ".cas/.dat"
  - "temps d'exécution"
  - "simulation"
  - "scripts de soumission"
  - "messages d'erreur"
  - "tâches en lot"
  - "licence CMC"
  - "Fichier de licence"
  - "formats de fichiers"
  - "nombre total de pas"
  - "lmutil lmstat"
  - "SLURM_SUBMIT_DIR"
  - "fichier de journalisation"
  - "ANSYSLMD_LICENSE_FILE"
  - "intelmpi"
  - "partitionnement du maillage"

questions:
  - "Qu'est-ce que la suite logicielle Ansys et quelles applications principales comprend-elle ?"
  - "Comment fonctionne la politique d'accès et de gestion des licences pour utiliser Ansys sur les grappes de calcul ?"
  - "Quelles sont les étapes techniques pour configurer son propre fichier de licence et se connecter à un serveur spécifique (comme CMC ou SHARCNET) ?"
  - "À quelle adresse courriel doit-on envoyer le nom d'utilisateur de l'Alliance pour que la licence fonctionne ?"
  - "Quelle est la conséquence si l'on ne communique pas les informations de son compte au support ?"
  - "Dans quelle section des guides Ansys peut-on vérifier le nombre de cœurs autorisés par la licence CMC ?"
  - "Quelles sont les trois informations à obtenir auprès de l'administrateur pour utiliser un serveur de licence Ansys déjà configuré ?"
  - "Quelles exigences supplémentaires doivent être respectées si le serveur de licence local n'a jamais été configuré pour les grappes ?"
  - "Quelle est la procédure de commandes à exécuter pour vérifier que le fichier de licence est correctement configuré et fonctionnel ?"
  - "How are compute resources allocated for the job using the Slurm workload manager?"
  - "Which specific software modules and versions must be loaded into the environment?"
  - "What command sequence is used to verify the operational status of the Ansys license server?"
  - "Comment doit-on lancer Ansys Workbench pour utiliser un serveur de licence distant au lieu du serveur par défaut ?"
  - "Quelles sont les limites de ressources (cœurs et mémoire) à respecter lors de l'exécution de Mechanical ou Fluent sur gra-vdi ?"
  - "Quelle est la règle de compatibilité concernant l'ouverture de fichiers de simulation entre différentes versions d'Ansys ?"
  - "Quelles sont les restrictions actuelles concernant l'utilisation de la version la plus récente d'Ansys (2025R1.02) par rapport aux serveurs de licence ?"
  - "Comment fonctionne la nomenclature des modules pour charger une version spécifique d'Ansys incluant un correctif (service pack) particulier ?"
  - "Pourquoi est-il nécessaire d'utiliser des directives spécifiques pour soumettre des tâches parallèles Ansys sur les grappes utilisant l'ordonnanceur Slurm ?"
  - "Est-il possible d'ouvrir une simulation Ansys avec une version antérieure à celle utilisée pour sa création ?"
  - "Quels sont les risques potentiels lors du lancement d'une simulation créée avec une version précédente du logiciel ?"
  - "Comment peut-on retrouver la version d'Ansys utilisée pour créer un fichier cas de simulation Fluent si on l'a oubliée ?"
  - "Pourquoi faut-il utiliser des directives particulières pour lancer une tâche parallèle avec les paquets Ansys ?"
  - "Quelle solution est proposée pour soumettre des tâches parallèles malgré l'incompatibilité avec l'ordonnanceur Slurm ?"
  - "Sur quelle grappe de calcul spécifique les scripts de soumission pourraient-ils nécessiter des ajustements ?"
  - "Quelles sont les étapes requises pour préparer, exporter et transférer les fichiers d'une simulation Ansys Fluent vers la grappe de calcul ?"
  - "Comment peut-on configurer un script pour gérer les problèmes de licences manquantes, et quels sont les risques associés à la remise en file d'attente automatique ?"
  - "Quelles sont les recommandations concernant le choix des scripts Slurm (par nœud ou par cœur) et l'optimisation du partitionnement du maillage pour maximiser les performances ?"
  - "Quelles sont les différences de configuration SLURM entre l'allocation des ressources par nœud et par cœur pour les tâches Ansys Fluent ?"
  - "Comment les scripts gèrent-ils les spécificités des différentes grappes de calcul (comme Narval et Nibi) lors de l'exécution ?"
  - "Quels modules et paramètres MPI doivent être chargés et configurés pour exécuter correctement le fichier journal Fluent ?"
  - "Quelle est la procédure alternative mentionnée pour partitionner le maillage et exécuter la tâche sur la grappe ?"
  - "Quel est l'avantage principal de réaliser le partitionnement manuellement dans l'interface graphique de Fluent ?"
  - "Quelles sont les recommandations numériques concernant le nombre de partitions et de cellules par cœur pour assurer une efficacité optimale ?"
  - "Comment le script ajuste-t-il les paramètres d'interconnexion MPI de Fluent selon que l'exécution se fait sur la grappe Nibi ou sur une autre ?"
  - "Quelles sont les directives SLURM nécessaires pour configurer l'allocation de ressources sur plusieurs nœuds pour la grappe Narval ?"
  - "Quels arguments spécifiques sont passés à la commande Fluent pour définir la version, le nombre de cœurs et le fichier journal à utiliser ?"
  - "How do the Slurm resource allocation directives differ when submitting an ANSYS Fluent job by whole nodes versus by individual cores?"
  - "What specific module versions are required to run ANSYS Fluent on the Trillium cluster compared to the Narval cluster?"
  - "How does the script alter the ANSYS Fluent execution command and MPI settings depending on whether the job is running on a single node or multiple nodes?"
  - "Comment le script configure-t-il la connexion au serveur de licences ANSYS ?"
  - "Pourquoi le script exige-t-il la création de liens symboliques pour les répertoires tels que `.ansys` et `.fluentconf` avant l'exécution ?"
  - "Dans quels cas spécifiques est-il déconseillé d'utiliser le script de remise en file d'attente pour obtenir une licence ?"
  - "What specific version of the ANSYS module is required to run successfully on the Trillium system?"
  - "How many CPUs per task are strictly allocated in this SLURM job configuration?"
  - "What are the acceptable values that can be assigned to the MYVERSION variable for the simulation?"
  - "What are the key user-configurable variables and module versions that need to be specified before running the script?"
  - "Which specific lines or sections of the script are strictly prohibited from being modified by the user?"
  - "How does the script conditionally handle the environment setup when running on the \"narval\" cluster?"
  - "Comment les scripts fournis automatisent-ils la gestion des échecs et le redémarrage des simulations ANSYS Fluent sur la grappe de calcul ?"
  - "Quelles modifications spécifiques doivent être apportées aux fichiers journaux (comme sample.jou et sample-restart.jou) pour configurer correctement le redémarrage d'une simulation ?"
  - "Comment doit-on ajuster le nombre d'itérations par redémarrage et le temps alloué dans Slurm pour s'assurer que les calculs respectent la limite maximale d'exécution ?"
  - "Comment doit-on choisir la valeur du premier pas dans le fichier sample.jou lorsqu'on part d'une solution précédente ?"
  - "Comment calcule-t-on la durée totale de la simulation et le nombre de fichiers de résultats si la valeur 2 est sélectionnée ?"
  - "Quels critères faut-il prendre en compte pour définir le temps d'exécution demandé dans le script Slurm ?"
  - "Quel est l'objectif principal de ce script SLURM et quel logiciel de simulation permet-il d'exécuter ?"
  - "Comment le script gère-t-il le redémarrage automatique de la simulation à l'aide des tableaux de tâches (job arrays) ?"
  - "De quelle manière le script adapte-t-il ses configurations MPI et réseau en fonction de la grappe de calcul (comme Narval ou Nibi) utilisée ?"
  - "Comment le script gère-t-il la vérification de la réussite ou de l'échec de la simulation ?"
  - "Quel est le rôle spécifique de la commande `scancel $SLURM_ARRAY_JOB_ID` dans ce flux de travail ?"
  - "Quelles sont les caractéristiques de la configuration définie sous l'onglet \"Plusieurs nœuds (par cœur + redémarrage)\" ?"
  - "Comment le script Slurm fourni gère-t-il les redémarrages automatiques de la simulation à l'aide des tableaux de tâches (array jobs) ?"
  - "Quel est le rôle principal des fichiers de journalisation dans ANSYS Fluent et comment permettent-ils d'automatiser les simulations ?"
  - "Quelle est la différence de format de fichier par défaut entre les versions de Fluent antérieures à 2019R3 et celles à partir de 2020R1 ?"
  - "Où peut-on consulter la liste des commandes et obtenir plus d'informations sur l'utilisation de Fluent ?"
  - "Quelle configuration permet d'utiliser les formats de fichiers par défaut .cas et .dat pour les modules jusqu'à la version 2019R3 ?"
  - "Quels sont les formats de fichiers les plus efficaces qui ont été introduits à partir de la version 2020R1 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Ansys est une suite logicielle pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

## Licence

La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez l'aspect légal de son utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence

Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire `/home`.
Pour indiquer votre propre serveur de licence, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient les deux lignes ci-dessous, où vous remplacez FLEXPORT, INTEPORT et LICSERVER par les valeurs de votre serveur.

```bash
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@LICSERVER")
```

Les valeurs correspondant aux serveurs de licence CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un différent serveur, voir [Serveurs de licence locaux](#serveurs-de-licence-locaux) ci-dessous.

| Licence   | Grappe                              | LICSERVER              | FLEXPORT | INTEPORT | VENDPORT | NOTES                                |
| :-------- | :---------------------------------- | :--------------------- | :------- | :------- | :------- | :----------------------------------- |
| CMC       | beluga                              | `10.20.73.21`          | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC       | cedar                               | `172.16.0.101`         | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC       | graham                              | `10.25.1.56`           | `6624`   | `2325`   | s.o.     | nouvelle IP le 21 février 2025       |
| CMC       | narval                              | `10.100.64.10`         | `6624`   | `2325`   | s.o.     | aucune                               |
| SHARCNET  | beluga/cedar/graham/gra-vdi/nibi/narval/rorqual | `license3.sharcnet.ca` | `1055`   | `2325`   | n/a      | aucune                               |
| SHARCNET  | niagara                             | `localhost`            | `1055`   | `2325`   | `1793`   | aucune                               |

Si vous avez obtenu une licence de CMC, vous devez faire parvenir le nom d'utilisateur associé à votre compte avec l'Alliance à <cmcsupport@cmc.ca>, autrement la licence ne fonctionnera pas. Pour connaître le nombre de cœurs que vous pouvez utiliser avec une licence CMC, voyez les sections *Other Tricks and Tips* des [guides Ansys Electronics Desktop et Ansys Mechanical/Fluids](https://www.cmc.ca/?s=Other+Tricks+and+Tips&lang=en/).

### Serveurs de licence locaux

Avant que le serveur de licence de votre établissement puisse être utilisé, les coupe-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans la section *Prêt à utiliser* ci-dessous. Autrement, référez-vous à la section *Configuration requise* un peu plus bas.

#### Prêt à utiliser

Pour utiliser un serveur de licence ANSYS déjà configuré pour être utilisé sur la grappe où vous allez soumettre des tâches, contactez votre administrateur de serveur de licences Ansys et obtenez les trois éléments d'information suivants :
1.  le nom d'hôte complet (LICSERVER) du serveur
2.  le port flex (FLEXPORT) pour Ansys, habituellement `1055`
3.  le port d'interconnexion (INTEPORT), habituellement `2325`
Une fois les trois éléments d'information collectés, configurez votre fichier `~/.licenses/ansys.lic` en entrant les valeurs de LICSERVER, FLEXPORT et INTEPORT dans le modèle du bloc de code `ansys.lic` ci-dessus.

#### Configuration requise

Si votre serveur de licence Ansys local n'a jamais été configuré pour être utilisé sur la ou les grappes où vous allez soumettre des tâches, en plus des 3 éléments ci-dessus, vous devrez ÉGALEMENT obtenir les éléments suivants auprès de l'administrateur :
4.  le numéro de port statique du fournisseur (VENDPORT)
5.  confirmation que `<servername>` se résoudra à la même adresse IP que LICSERVER sur nos grappes
où `<servername>` peut être trouvé dans la première ligne du fichier de licence avec le format *SERVER <servername> <host id> <lmgrd port>*. L'élément 5 est obligatoire sinon les extractions de licences Ansys ne fonctionneront sur aucune grappe distante. S'il s'avère que `<servername>` ne répond pas à cette exigence, demandez à votre administrateur de licence de remplacer `<servername>` par le même nom d'hôte complet que LICSERVER ou au moins par un nom d'hôte qui se résoudra à la même adresse IP que LICSERVER à distance.

## Vérifier la licence

Pour vérifier si `ansys.lic` est bien configuré et fonctionne correctement, copiez et collez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches. La seule différence est de spécifier YOURUSERID. Si le logiciel n’est pas à jour sur le serveur de licence distant, un problème peut survenir si la dernière version du module Ansys est chargée pour effectuer des tests. Pour que la licence fonctionne quand des tâches sont soumises, assurez-vous que la même version du module Ansys qui est chargé par votre script est utilisée dans les commandes ci-dessous.

```bash
cd /tmp
salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
module load StdEnv/2023; module load ansys/2025R2.04
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```

`Success` indique que les extractions de licence devraient fonctionner lorsque les tâches sont soumises à la file d'attente.
`Fail` indique un problème avec la configuration de la licence et les tâches échoueront probablement.

!!! note "Remarque 1"
    Pour les modules Ansys installés localement, la commande `runwb2` de `SnEnv` utilise par défaut le serveur de licence SHARCNET, tel que défini dans le fichier du module Ansys que vous chargez. Pour utiliser un serveur distant, lancez plutôt Workbench avec `runwb2-gui`, car ce script enveloppant (*wrapper*) lira votre fichier `~/.licenses/ansys.lic` comme les modules disponibles sous `StdEnv/2023`. De plus, l'option interactive d'utilisation du serveur CMC (acheminé via le serveur SHARCNET CMC CadPASS) sera proposée, éliminant ainsi la nécessité de le configurer dans votre fichier ansys.lic.

!!! note "Remarque 2"
    Lorsque vous démarrez Fluent à partir de Workbench avec la version 2025R1, avant de cliquer sur le bouton *Démarrer*, cliquez sur l'onglet *Environnement* du panneau de lancement du *Lanceur Fluent* et copiez/collez `HOOPS_PICTURE=opengl` dans le champ de saisie vide. Vous pouvez aussi définir `export HOOPS_PICTURE=opengl` dans votre environnement avant de démarrer Workbench. L'une ou l'autre de ces actions empêchera le message suivant, qui apparaîtrait dans les messages de démarrage de l'interface utilisateur : **[Avertissement : Le rastériseur logiciel a été détecté, l'accélération matérielle sera désactivée.]**

!!! note "Remarque 3"
    Lorsque vous exécutez Mechanical dans Workbench sur gra-vdi, assurez-vous de cocher *Distribué* dans le panneau *Solveur* du ruban supérieur et de spécifier une valeur maximale de **24 cœurs**. Lorsque vous exécutez Fluent sur gra-vdi, ne cochez pas *Distribué* et spécifiez une valeur maximale de **12 cœurs**. N'essayez pas d'utiliser plus de 128 Go de mémoire, sinon Ansys atteindra la limite et sera arrêté. Si vous avez besoin de plus de cœurs ou de mémoire, utilisez un nœud de calcul sur une grappe pour exécuter votre session graphique (comme décrit dans la section *Nœuds de calcul*). Lorsque vous effectuez une ancienne tâche de prétraitement ou de post-traitement avec Ansys sur gra-vdi et que vous n'exécutez pas de calcul, utilisez uniquement **4 cœurs**, sinon les licences HPC seront extraites inutilement.

!!! note "Remarque 4"
    Dans de très rares cas, l'interface graphique de Workbench ou de certains programmes qu'il exécute se bloquent ou ne démarrent pas correctement, notamment si vnsviewer se déconnecte avant que Ansys soit fermé correctement. En général, si Ansys ne fonctionne pas correctement, ouvrez une nouvelle fenêtre de terminal sur gra-vdi et exécutez `pkill -9 -e -u $USER -f "ansys|fluent|mwrpcss|mwfwrapper|ENGINE|mono"` pour arrêter complètement tous les processus Ansys. Si le problème persiste et que vous utilisiez l'interface graphique sur des nœuds de calcul avant de travailler sur gra-vdi, essayez d'exécuter `rm -rf .ansys`. Si le problème concerne /home, /project ou /scratch (la commande df bloque), il est fort probable qu'Ansys recommence à fonctionner normalement une fois le problème de stockage résolu.

```bash
fluent -g 2d -n 2
```
```text
Liste des serveurs de licence connectés :	<Shared_Web_License_Server>
Appuyez sur Entrée pour quitter.
```

## Compatibilité des versions

Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une moins récente version de Ansys devrait pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec ansys/2022R2 devrait fonctionner avec ansys/2023R2, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
grep -ia fluent combustor.cas
```
```text
(0 "fluent15.0.7  build-id: 596")
```

```bash
grep -ia fluent cavity.cas.h5
```
```text
ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge

## ANSYS Fluent

Voici la procédure habituelle pour utiliser Fluent avec les grappes de Calcul Canada :

## Nouveautés

Ansys publie régulièrement des *service packs* pour regrouper plusieurs mises-à-jour apportant différents correctifs et améliorations à ses versions majeures. Des informations similaires pour les versions précédentes peuvent généralement être trouvées sur [le blog Ansys](https://www.ansys.com/blog), en utilisant la barre de recherche FILTRES. Par exemple, la recherche de `What’s New Fluent 2024 gpu` affichera le document `[Quoi de neuf pour Ansys Fluent en 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1)` qui contient une multitude d'informations sur la prise en charge des GPU. Spécifier un numéro de version dans le champ de recherche [Communiqués de presse](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations sur les nouvelles versions. Le module `ansys/2025R1.02` pour la dernière version de Ansys a été installé récemment; pour l'utiliser cependant, vous avez besoin d'un serveur de licence comme celui de CMC. La mise à jour du serveur de licence de SHARCNET est en cours et tant que ce travail ne sera pas terminé, seules les versions `ansys/2024R2.04` ou moins récentes seront prises en charge. Si un module pose problème ou pour demander l'installation d'une nouvelle version, écrivez au [soutien technique](../support/technical_support.md).

## Correctifs

À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *service pack* est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun *service pack* peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le *service pack* 3 peut être chargé avec `module load ansys/2024R1.03`. Si un *service pack* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *service pack* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *service pack* installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les *service packs* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *service pack* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *service pack* rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque *service pack* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

## Soumettre des tâches en lot sur nos grappes

Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

## Ansys Fluent

La procédure suivante est habituellement utilisée pour exécuter Fluent sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *Fichier > Exporter > Cas…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `FFF-1.cas.gz`.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *Fichier > Exporter > Données…* ou trouvez-le dans le même répertoire `/project` (`FFF-1.dat.gz`).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage) de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `FFF-1.*` ou renommez-les au téléversement.
5.  Créez un fichier de journalisation dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancez le solveur et enregistrez les résultats. Voyez les exemples ci-dessous et n'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour le script sous l'onglet *Plusieurs nœuds (par cœur + remise en attente)* plus loin. Cependant, ceci remet aussi en attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en attente est ou non due à un problème de licence. Si vous découvrez que la remise en attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `scancel jobid` et corrigez le problème.
7.  Lorsque la [tâche est terminée](../running-jobs/running_jobs.md), vous pouvez télécharger le fichier de données et le retourner dans Fluent avec *Fichier > Importer > Données…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale

La plupart des tâches Fluent devraient utiliser le script *par nœud* ci-dessous pour minimiser le temps d'attente et maximiser la performance en utilisant le moins de nœuds possible. Les tâches demandant beaucoup de cœurs CPU pourraient attendre moins longtemps dans la queue avec le script *par cœur*, mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent fournir une alternative plus robuste si Fluent plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts Intel standards avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de Fluent, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts Intel. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

=== "Plusieurs nœuds (par nœud)"

```bash linenums="1" title="script-flu-bynode-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (narval 1 nœud max)
#SBATCH --ntasks-per-node=32  # Spécifiez jusqu'au nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne modifiez pas

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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

```bash linenums="1" title="script-flu-bycore-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (narval 1 nœud max)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne modifiez pas

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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

```bash linenums="1" title="script-flu-bynode-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=64  # Spécifiez le nombre de cœurs par nœud (narval 64 ou moins)
#SBATCH --mem=0               # Ne modifiez pas (alloue toute la mémoire par nœud de calcul)
#SBATCH --cpus-per-task=1     # Ne modifiez pas

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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

```bash linenums="1" title="script-flu-bycore-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne modifiez pas

module load StdEnv/2023       # Ne modifiez pas     
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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

```bash linenums="1" title="script-flu-bynode-intel-tri.sh"
#!/bin/bash

#SBATCH --account=def-group      # Spécifiez le nom du compte
#SBATCH --time=00-03:00          # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=16     # Spécifiez le nombre de cœurs par nœud (max 192 sur trillium)
##SBATCH --mem=0                 # Ne décommentez pas (par défaut, trillium utilise toute la mémoire par nœud)
#SBATCH --cpus-per-task=1        # Ne modifiez pas (paramètre obligatoire)

cd $SLURM_SUBMIT_DIR             # Soumettez depuis $SCRATCH/some/dir

module load StdEnv/2023          # Ne modifiez pas
module load ansys/2025R2.04      # seulement 2025R2 ou plus récent fonctionne sur trillium

MYJOURNALFILE=sample.jou         # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                     # Spécifiez 2d, 2ddp, 3d ou 3ddp

# Ces paramètres sont utilisés à la place de votre ~/.licenses/ansys.lic
LICSERVER=license1.computecanada.ca   # Spécifiez le nom d'hôte du serveur de licence
FLEXPORT=1055                         # Spécifiez le port flex du serveur
VENDPORT=1793                         # Spécifiez le port du fournisseur du serveur

# ------- ne modifiez aucune ligne ci-dessous --------

ssh tri-gw -fNL $FLEXPORT:$LICSERVER:$FLEXPORT
ssh tri-gw -fNL $VENDPORT:$LICSERVER:$VENDPORT
export ANSYSLMD_LICENSE_FILE=$FLEXPORT@localhost
export ANSYSLI_SERVERS=$INTEPORT@localhost

slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ ! -L "$HOME/.ansys" ]; then
  echo "ERREUR : Un lien vers un répertoire .ansys inscriptible n'existe pas."
  echo 'Supprimez ~/.ansys si l\'un existe, puis exécutez : ln -s $SCRATCH/.ansys ~/.ansys'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
elif [ ! -L "$HOME/.fluentconf" ]; then
  echo "ERREUR : Un lien vers un répertoire .fluentconf inscriptible n'existe pas."
  echo 'Supprimez ~/.fluentconf si l\'un existe et exécutez : ln -s $SCRATCH/.fluentconf ~/.fluentconf'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
elif [ ! -L "$HOME/.flrecent" ]; then
  echo "ERREUR : Un lien vers un fichier .flrecent inscriptible n'existe pas."
  echo 'Supprimez ~/.flrecent si l\'un existe, puis exécutez : ln -s $SCRATCH/.flrecent ~/.flrecent'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
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

:fontawesome-solid-angle-right:{.right}

#### Remise en file d'attente pour obtenir la licence

Les scripts suivants ne doivent être utilisés qu'avec des tâches Fluent qui sont connues pour se terminer normalement sans générer d'erreurs en sortie, mais qui nécessitent généralement plusieurs tentatives de remise en file d'attente pour obtenir les licences. Ils ne sont pas recommandés pour les tâches Fluent qui peuvent 1) s'exécuter pendant une longue période avant de planter 2) s'exécuter jusqu'à la fin mais contenir des avertissements de journalisation; dans les deux cas, les simulations seront répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente spécifié par la valeur `array` soit atteint. Pour ces types de tâches, les scripts à usage général (ci-dessus) doivent être utilisés.

=== "Plusieurs nœuds (par nœud + remise en attente)"

```bash linenums="1" title="script-flu-bynode+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (narval 1 nœud max)
#SBATCH --ntasks-per-node=32  # Spécifiez jusqu'au nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne modifiez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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
    echo "Tâche terminée avec succès ! Sortie immédiate."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT échouée en raison d'un problème de licence ou de simulation !"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Nouvelle soumission de la tâche en cours..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie immédiate."
    fi
fi
```

=== "Plusieurs nœuds (par cœur + remise en attente)"

```bash linenums="1" title="script-flu-bycore+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (narval 1 nœud max) 
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne modifiez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne modifiez pas     
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier de journalisation
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- ne modifiez aucune ligne ci-dessous --------

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
    echo "Tâche terminée avec succès ! Sortie immédiate."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT échouée en raison d'un problème de licence ou de simulation !"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Nouvelle soumission de la tâche en cours..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie immédiate."
    fi
fi
```

:fontawesome-solid-angle-right:{.right}

#### Redémarrage

Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de *sample.cas*, *sample.dat* et *sample.jou* doit être présent. Modifiez le fichier *sample.jou* pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier de journalisation avec `cp sample.jou sample-restart.jou` et modifiez le fichier *sample-restart.jou* pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `;/solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez *sample-restart.jou* en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de *sample.jou* est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt+2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1+2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

=== "Plusieurs nœuds (par nœud + redémarrage)"

```bash linenums="1" title="script-flu-bynode+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=07-00:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (narval 1 nœud max)
#SBATCH --ntasks-per-node=32  # Spécifiez jusqu'au nombre maximal de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne modifiez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de redémarrages de solution (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYVERSION=3d                        # Spécifiez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Spécifiez le nom de votre fichier de journalisation
MYJOUFILERES=sample-restart.jou     # Spécifiez le nom du fichier de journalisation de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Spécifiez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Spécifiez le nom du fichier dat de redémarrage

# ------- ne modifiez aucune ligne ci-dessous --------

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
      echo "Tâche terminée avec succès ! Sortie immédiate."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie immédiate..."
fi
```

=== "Plusieurs nœuds (par cœur + redémarrage)"

```bash linenums="1" title="script-flu-bycore+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
##SBATCH --nodes=1            # Décommentez pour spécifier (narval 1 nœud max)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne modifiez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de redémarrages (pas de temps) (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne modifiez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYVERSION=3d                        # Spécifiez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Spécifiez le nom de votre fichier de journalisation
MYJOUFILERES=sample-restart.jou     # Spécifiez le nom du fichier de journalisation de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Spécifiez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Spécifiez le nom du fichier dat de redémarrage

# ------- ne modifiez aucune ligne ci-dessous --------

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
      echo "Tâche terminée avec succès ! Sortie immédiate."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie immédiate."
fi
```

:fontawesome-solid-angle-right:{.right}

### Fichiers de journalisation

Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface utilisateur textuelle (TUI) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le guide d'utilisation de Fluent pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `/file/cff-files yes`.

=== "Fichier de journalisation (stable, cas)"

```text linenums="1" title="sample1.jou"
; FICHIER DE JOURNALISATION FLUENT EXEMPLE - SIMULATION STABLE
; ----------------------------------------------
; les lignes commençant par un point-virgule sont des commentaires

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Lire/écrire les fichiers de préférence au format hérité
/file/cff-files no

; Lire les fichiers de cas et de données d'entrée
/file/read-case-data FFF-in

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; Écraser les fichiers de sortie par défaut
/file/confirm-overwrite n

; Écrire le fichier de données de sortie final
/file/write-case-data FFF-out

; Écrire le rapport de simulation dans un fichier (optionnel)
/report/summary y "My_Simulation_Report.txt"

; Arrêter Fluent proprement
/exit
```

=== "Fichier de journalisation (stable, cas + données)"

```text linenums="1" title="sample2.jou"
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

```text linenums="1" title="sample3.jou"
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

:fontawesome-solid-angle-right:{.right}

### Fonctions UDF

La première étape est de transférer vers la grappe votre fonction UDF (*User-Defined Function*), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui elle exécute Linux. La fonction UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *Fonctions UDF interprétées* et *Gestionnaire de bibliothèques UDF* ne sont pas configurées pour utiliser une UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interprété

Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```text
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilé

Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `libudf.so` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quel autre de nos grappes, à condition que votre compte charge la même version du module d'environnement StdEnv. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (load) `libudf` ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes `libudf` (compile et load) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de build de type « racetime » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent (exécutée sur n'importe quel nœud de calcul ou sur gra-vdi) peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *Fonctions UDF compilées*, et cliquez sur *Compiler*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

```text
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

et/ou

```text
define/user-defined/compiled-functions load libudf
```

#### Parallèle

Avant qu'une UDF puisse être utilisée avec une tâche parallèle Fluent (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque Fluent est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, Fluent fonctionnera lentement au mieux ou plantera immédiatement au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque Fluent est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans *Manuel de personnalisation de Fluent, Partie I : Chapitre 7 : Considérations parallèles* qui se trouve dans la [Documentation en ligne](#aide).

#### DPM

Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour *Discrete Phase Models*) comme décrit dans *Guide de l'utilisateur Fluent 2024R2, Partie III : Mode solution, Chapitre 24 : Modélisation de la phase discrète, 24.2 Étapes pour l'utilisation des modèles de phase discrète,* et dans *Manuel de personnalisation de Fluent 2024R2, Partie I : Création et utilisation de fonctions définies par l'utilisateur, Chapitre 2 : Macros DEFINE, 2.5 Macros DEFINE du modèle de phase discrète (DPM)*. Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Propriétés des points* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physique--> Phase discrète*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Créer*. La boîte de dialogue *Définir les propriétés d'injection* contient le menu déroulant *Type d'injection* avec les quatre premiers types disponibles (*simple, groupe, surface, atomiseur à jet plat*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Propriétés des points* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Propriétés des points* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *Fichier* dans le menu déroulant *Type d'injection*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *Fichier* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Définir les propriétés d'injection*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension `.dpm`) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Sélectionner un fichier*, sélectionnez *Tous les fichiers (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur le bouton *OK*. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Définir les propriétés d'injection* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Modèle de phase discrète* et sélectionnez *Interaction avec la phase continue* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple :

```text
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```

où un format de fichier stable d'injection de base créé manuellement pourrait ressembler à :

```text
$ cat zinjection01.inj
(z=4 12)
( x y z u v w diamètre t débit massique fréquence massique temps nom )
(( 2.90e-02 5.00e-03 0.0 -1,00e-03 0,0 0,0 1,00e-04 2,93e+02 1,00e-06 0,0 0,0 0,0 ) injection-0:1 )
```

notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans *Manuel de personnalisation de Fluent 2024R2, Partie III : Mode solution | Chapitre 24 : Modélisation de la phase discrète | 24.3. Définition des conditions initiales pour la phase discrète | 24.3.13 Propriétés des points pour les injections de fichiers | 24.3.13.1 Format de fichier stable*.

## CFX

### Scripts pour l'ordonnanceur Slurm

Le résumé des options de ligne de commande peut être affiché avec **cfx5solve -help**. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, cfx5solve s'exécute en simple précision (*-single*). Pour exécuter cfx5solve en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, cfx5solve prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être uitilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'ANSYS CFX-Solver Manager pour plus de détails.

=== "Nœud simple"

```bash linenums="1" title="script-local.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=1             # Spécifiez un nœud de calcul unique (ne modifiez pas)
#SBATCH --ntasks-per-node=4   # Spécifiez le nombre de cœurs (maximum : graham 44, cedar 32 ou 48, beluga 40, narval 64)
#SBATCH --mem=16G             # Spécifiez la mémoire du nœud (facultativement, définissez à 0 pour allouer toute la mémoire du nœud)
#SBATCH --cpus-per-task=1     # Ne modifiez pas

#module load StdEnv/2020      # Décommentez pour utiliser (déprécié)     
#module load 2021R2           # Spécifiez 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Ou versions de modules plus récentes

# ajoutez les options de ligne de commande cfx5solve supplémentaires au besoin
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
else
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
fi
```

=== "Plusieurs nœuds"

```bash linenums="1" title="script-cfx-multiple.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --nodes=2             # Spécifiez plusieurs nœuds de calcul (2 ou plus)
#SBATCH --ntasks-per-node=64  # Spécifiez tous les cœurs par nœud (maximum : graham 44, 48, beluga 40, narval 64)
#SBATCH --mem=0               # Utilisez toute la mémoire par nœud de calcul (ne modifiez pas)
#SBATCH --cpus-per-task=1     # Ne modifiez pas

#module load StdEnv/2020      # Décommentez pour utiliser (déprécié)     
#module load 2021R2           # Spécifiez 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Spécifiez 2022R2 ou versions de modules plus récentes

NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

# ajoutez les options de ligne de commande cfx5solve supplémentaires au besoin
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
else
  export I_MPI_HYDRA_BOOTSTRAP=ssh
  unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
fi
```

:fontawesome-solid-angle-right:{.right}

## Workbench

Initialisez le fichier de projet avant de le soumettre pour la première fois.
1.  Connectez-vous à la grappe avec [TigerVNC](../interactive/vnc.md#nœuds-de-calcul).
2.  Dans le même répertoire où se trouve le fichier de projet (`YOURPROJECT.wbpj`), [lancez Workbench](ansys.md) avec la même version du module Ansys qui a servi à créer le projet.
3.  Dans Workbench, ouvrez le projet avec *Fichier -> Ouvrir*.
4.  Dans la fenêtre principale, faites un clic droit sur *Configuration* et sélectionnez *Effacer toutes les données générées*.
5.  Dans la liste déroulante de la barre de menus du haut, cliquez sur *Fichier -> Quitter* pour sortir de Workbench.
6.  Dans la fenêtre contextuelle Ansys Workbench qui affiche *Le projet actuel a été modifié. Voulez-vous le sauvegarder ?* cliquez sur le bouton *Non*.
7.  Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Considérez exécuter vos simulations Workbench directement à partir de l'interface graphique native de Workbench lorsque c'est possible, car c'est une option plus intuitive que de soumettre la tâche à la file d'attente avec un script Slurm.

### Scripts pour l'ordonnanceur Slurm

Pour soumettre un fichier de projet à la queue, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

=== "Nœud unique (StdEnv/2023)"

```bash linenums="1" title="script-wbpj-2023.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Temps (JJ-HH:MM)
#SBATCH --mem=16G                      # Mémoire totale (définir à 0 pour toute la mémoire du nœud)
#SBATCH --ntasks=4                     # Nombre de cœurs
#SBATCH --nodes=1                      # Ne modifiez pas (multi-nœud non pris en charge)
##SBATCH --exclusive                   # Décommentez pour les tests de mise à l'échelle
##SBATCH --constraint=broadwell        # Applicable à graham ou cedar

module load StdEnv/2023 ansys/2023R2   # OU versions de modules Ansys plus récentes

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

=== "Nœud unique (StdEnv/2020)"

```bash linenums="1" title="script-wbpj-2020.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Temps (JJ-HH:MM)
#SBATCH --mem=16G                      # Spécifiez la mémoire totale
#SBATCH --ntasks=4                     # Spécifiez le nombre de cœurs
#SBATCH --nodes=1                      # Ne modifiez pas (multi-nœud non pris en charge)
##SBATCH --exclusive                   # Décommentez UNIQUEMENT pour les tests de mise à l'échelle
##SBATCH --constraint=broadwell        # Décommentez pour spécifier un type de nœud disponible

module load StdEnv/2020 ansys/2021R2   # OU versions de modules Ansys plus récentes

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

:fontawesome-solid-angle-right:{.right}

Pour éviter d'écrire la solution lorsqu'une tâche en cours d'exécution se termine avec succès, changez `Save(Overwrite=True)` en `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera la détermination de la performance de la simulation lorsque `#SBATCH --ntasks` est augmenté, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical

Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Outils -> Écrire les fichiers d'entrée* et en spécifiant `Nom du fichier :` pour `YOURAPDLFILE.inp` et `Enregistrer sous le type :` pour les fichiers APDL en entrée (*.inp*). Les tâches APDL peuvent ensuite être soumises à la file d'attente avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm

Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `##SBATCH` sont suivies d'un commentaire.

=== "Mémoire partagée parallèle (CPU)"

```bash linenums="1" title="script-smp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez votre compte
#SBATCH --time=00-03:00         # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem=32G               # Spécifiez la mémoire pour tous les cœurs
#SBATCH --nodes=1               # Ne modifiez pas
#SBATCH --tasks=8               # Spécifiez le nombre de cœurs
#SBATCH --cpus-per-task=1       # Ne modifiez pas

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
```

=== "Mémoire distribuée parallèle (CPU)"

```bash linenums="1" title="script-dmp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez votre compte
#SBATCH --time=00-03:00         # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G        # Spécifiez la mémoire par cœur
##SBATCH --nodes=2              # Spécifiez le nombre de nœuds (optionnel)
#SBATCH --ntasks=8              # Spécifiez le nombre de cœurs
##SBATCH --ntasks-per-node=4    # Spécifiez les cœurs par nœud (optionnel)
#SBATCH --cpus-per-task=1       # Ne modifiez pas

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

```bash linenums="1" title="script-smp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez votre compte
#SBATCH --time=00-03:00          # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem=32G                # Spécifiez la mémoire pour tous les cœurs
#SBATCH --ntasks=8               # Spécifiez le nombre de cœurs
#SBATCH --nodes=1                # Ne modifiez pas
#SBATCH --cpus-per-task=1        # Ne modifiez pas
#SBATCH --gpus-per-node=1        # Spécifiez [type_gpu:]quantité
##SBATCH --gpus-per-node=h100:1  # Temporairement requis sur mini-graham
##SBATCH --partition=debug       # Temporairement requis sur mini-graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

export ANSGPU_PRINTDEVICES=1
mapdl -smp -acc nvidia -na $SLURM_GPUS_ON_NODE -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID  -i YOURAPDLFILE.inp
```

=== "Mémoire parallèle distribuée (GPU)"

```bash linenums="1" title="script-dmp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez votre compte
#SBATCH --time=00-03:00          # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G         # Spécifiez la mémoire par cœur
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds
#SBATCH --ntasks-per-node=8      # Spécifiez les cœurs par nœud
#SBATCH --cpus-per-task=1        # Ne modifiez pas
#SBATCH --gpus-per-node=1        # Spécifiez [type_gpu:]quantité
##SBATCH --gpus-per-node=h100:1  # Temporairement requis sur mini-graham
##SBATCH --partition=debug       # Temporairement requis sur mini-graham

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

:fontawesome-solid-angle-right:{.right}

Par défaut, Ansys alloue aux tâches APDL 1024 Mo de mémoire totale et 1024 Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande `mapdl` des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de mise à l'échelle avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (SMP pour *Shared Memory Parallel*) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (DMP pour *Distributed Memory Parallel*) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```bash
cat YOURAPDLFILE.inp | grep version
```
```text
! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

En plus de pouvoir exécuter des simulations en mode graphique (comme indiqué dans la section [Mode graphique](#mode-graphique) ci-dessous), [Ansys Rocky](https://www.ansys.com/products/fluids/ansys-rocky) peut également exécuter des simulations en mode non graphique. Les deux modes prennent en charge l'exécution de Rocky avec des processeurs uniquement ou avec des processeurs et [des GPU](https://www.ansys.com/blog/mastering-multi-gpu-ansys-rocky-software-enhancing-its-performance). Dans la section ci-dessous, deux exemples de scripts sont fournis où chacun serait soumis à la file d'attente de Graham avec la commande habituelle `sbatch`. Au moment de la rédaction de cet article, aucun des deux scripts n'a été testé et des modifications seraient probablement nécessaires. Il est important de noter que ces scripts ne sont utilisables que sur Graham puisque le module Rocky qu'ils chargent tous les deux n'est (pour le moment) installé que sur Graham localement.

### Scripts pour l'ordonnanceur Slurm

Pour obtenir une liste complète des options de ligne de commande, exécutez `Rocky -h` sur la ligne de commande après avoir chargé un module Rocky (seul `ansysrocky/2023R2` est présentement disponible sur Graham). En ce qui concerne l'utilisation de Rocky avec des GPU pour résoudre des problèmes couplés, le nombre de CPU que vous devez demander (sur le même nœud) doit être augmenté au maximum jusqu'à ce que la limite de scalabilité de l'application couplée soit atteinte. D'autre part, si Rocky est exécuté avec des GPU pour résoudre des problèmes découplés autonomes, seul un nombre minimal de CPU doit être demandé, ce qui permettra à Rocky de fonctionner de manière optimale; par exemple, seuls 2 ou éventuellement 3 CPU peuvent être nécessaires. Enfin, lorsque Rocky est exécuté avec 4 ou plus CPU, des licences *rocky_hpc* seront nécessaires, ce que fournit la licence SHARCNET.

=== "CPU seulement"

```bash linenums="1" title="script-rocky-cpu.sh"
#!/bin/bash

#SBATCH --account=account      # Spécifiez votre compte (def ou rrg)
#SBATCH --time=00-02:00        # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem=24G              # Spécifiez la mémoire totale pour les cœurs
#SBATCH --cpus-per-task=6      # Spécifiez le nombre de cœurs à utiliser
#SBATCH --nodes=1              # Demandez un nœud (ne modifiez pas)

module load StdEnv/2023 ansys/2025R1       # ou versions plus récentes
export PATH=$EBROOTANSYS/v251/rocky:$PATH

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0
```

=== "Basé sur GPU"

```bash linenums="1" title="script-rocky-gpu.sh"
#!/bin/bash

#SBATCH --account=account      # Spécifiez votre compte (def ou reg)
#SBATCH --time=00-01:00        # Spécifiez le temps (JJ-HH:MM)
#SBATCH --mem=24G              # Spécifiez la mémoire (définir à 0 pour utiliser toute la mémoire du nœud)
#SBATCH --cpus-per-task=6      # Spécifiez les cœurs (graham 32 ou 44 pour utiliser tous les cœurs)
#SBATCH --gres=gpu:v100:2      # Spécifiez le type de GPU : quantité de GPU
#SBATCH --nodes=1              # Demandez un nœud (ne modifiez pas)

# le module rocky2023R2 sur graham a été renommé ansysrocky/2023R2   24 avril 2025
#module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2       # disponible uniquement sur graham
module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04   # disponible uniquement sur graham

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE
```

:fontawesome-solid-angle-right:{.right}

## Electronics

Des scripts Slurm pour utiliser AnsysEDT sont fournis sur une page wiki distincte [ici](ansysedt.md).

## Mode graphique

Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
*   [FIR](https://docs.alliancecan.ca/wiki/Fir): `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](https://docs.alliancecan.ca/wiki/Rorqual): `https://jupyterhub.rorqual.alliancecan.ca`
*   [NARVAL](https://docs.alliancecan.ca/wiki/Narval): `https://jupyterhub.narval.alliancecan.ca/`
*   [TRILLIUM](https://docs.scinet.utoronto.ca/index.php/Open_OnDemand_Quickstart): `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources requises pour votre session de bureau interactive et cliquez sur Lancer ou Démarrer. Si des graphiques accélérés ou des calculs doivent être effectués à partir de votre session de bureau, assurez-vous de spécifier une ressource GPU. Une fois le bureau chargé, chargez un module Ansys. Si vous avez démarré un bureau propulsé par Jupyter Lab, cela peut être fait en cliquant sur le menu de gauche, ou si vous avez démarré un bureau OnDemand, tapez manuellement `module load ansys/version` sur la ligne de commande. Pour démarrer l'un des programmes Ansys courants tels que fluent, cfx, workbench, etc., référez-vous à la section suivante qui fournit des conseils pour la configuration des variables d'environnement et des arguments requis par les environnements graphiques basés sur VirtualGL ou Mesa, selon qu'un nœud avec une ressource GPU a été spécifié ou non.

### Fluent

Pour démarrer Ansys Fluent depuis la ligne de commande d'un bureau On Demand, ouvrez une fenêtre de terminal et exécutez les commandes :

```bash
module load StdEnv/2023 ansys/2025R1
```
```bash
fluent
```

Lorsque le panneau de sélection contextuel du Lanceur Fluent apparaît, cliquez sur l'onglet Environnement et copiez/collez les paramètres de variable d'environnement suivants, selon que vous avez démarré votre session On Demand avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses (car ce sont des commentaires) et ne mettez pas `export` devant les noms de variables. Le paramètre *null* signifie qu'un onglet de fenêtre de console graphique ne sera pas créé au démarrage de l'interface graphique, car les graphiques interactifs ne sont plus pris en charge pour la version, mais il devrait toujours être possible d'effectuer des opérations de menu normales et d'exécuter des tâches de manière interactive.

**Nœud de calcul (aucun GPU demandé)**

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh            (requis sur nibi)
HOOPS_PICTURE=opengl2-mesa           (version 2025R1 ou plus récente)
HOOPS_PICTURE=null                   (version 2024R2 ou plus ancienne)
```
Cliquez sur le bouton `Démarrer`.

```bash
slurm_hl2hl.py --format ANSYS-FLUENT > machinefile
NCORES=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))
fluent 3d -t $NCORES -cnf=machinefile -mpi=intel -affinity=0 -g -i sample.jou
```

Si `I_MPI_HYDRA_BOOTSTRAP=ssh` n'est pas correctement défini sur nibi lorsque Fluent est démarré à partir des sessions de bureau On Demand et qu'intelmpi est utilisé, Fluent plantera au démarrage en produisant le message d'erreur suivant. Si cela se produit, quittez Fluent complètement, fermez Workbench et recommencez.

```text
[mpiexec@g4.nibi.sharcnet] Error: Impossible d'exécuter bstrap_proxy sur g4.nibi.sharcnet (pid 2251587, code de sortie 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): erreur de vérification des codes de sortie
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): erreur de sondage pour l'événement
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): erreur d'attente d'événement
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```

### CFX

Lors du démarrage de CFX à partir d'un bureau On Demand, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal selon qu'un GPU a été demandé ou non lors du démarrage du bureau.

```bash
module load StdEnv/2023 ansys/2025R1   # (ou versions plus anciennes)
```
```bash
cfx5 -graphics mesa                   # (aucun GPU demandé)
```
```bash
cfx5 -graphics ogl                    # (avec GPU demandé)
```

### Mapdl

Les étapes suivantes pour démarrer l'interface graphique de Mechanical APDL à partir de la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre bureau On Demand sur un nœud de calcul avec ou sans GPU.

```bash
module load StdEnv/2023 ansys/2022R2   # (ou versions plus récentes)
```
```bash
mapdl -g                               # ou,
```
```bash
launcher                               # puis cliquez sur le bouton EXÉCUTER
```

### Workbench

```bash
module load StdEnv/2023 ansys/2022R2   # (ou versions plus récentes)
```
```bash
xfwm4 --replace &                      # (nécessaire seulement si vous utilisez Ansys Mechanical)
```
```bash
export QTWEBENGINE_DISABLE_SANDBOX=1   # (nécessaire seulement si vous utilisez CFD-Post)
```
```bash
runwb2
```
Remarque : Quand vous exécutez en parallèle un programme d'analyse comme Mechanical ou Fluent sur un nœud simple, ne cochez pas la case *Distribué* et indiquez un nombre de cœurs égal à votre **session salloc, moins 1**. Les menus déroulants du Ansys Mechanical Workbench ne répondent pas correctement. Comme solution, lancez `xfwm4 --replace` sur la ligne de commande avant de démarrer Workbench. Pour avoir xfwm4 par défaut, modifiez `$HOME/.vnc/xstartup` et remplacez `mate-session` par `xfce4-session`.

Cette section montre comment démarrer Workbench (et éventuellement Fluent) sur un bureau On Demand ou Jupyter Lab.

## Problèmes avec SSH

Certains programmes d'interface graphique ANSYS peuvent être exécutés à distance sur un nœud de calcul d'une de nos grappes par redirection X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que MobaXterm. La plupart d'entre vous trouverez les temps de réponse interactifs inacceptables pour les tâches de menu de base, sans parler de l'exécution de tâches plus complexes telles que celles nécessitant du rendu graphique. Les temps d'attente pour démarrer des programmes avec interface graphique peuvent également être très longs, dépendant de votre connexion Internet. Dans un test par exemple, il a fallu 40 minutes pour obtenir l'interface graphique avec SSH alors que vncviewer n'a pris que 34 secondes. Malgré la lenteur potentielle lors de la connexion via SSH pour exécuter des programmes avec interface graphique, cela peut toujours être intéressant si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou d'exécuter des calculs. Ces étapes de base sont un point de départ :

1.  ```bash
    ssh -Y username@graham.computecanada.ca
    ```
2.  ```bash
    salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task =4 [--gpus-per-node=1] --account=def-mygroup
    ```
3.  une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, chargez le module Ansys souhaité et essayez d'exécuter le programme.

### Fluids

```bash
module load CcEnv StdEnv/2023
```
```bash
module load ansys/2024R2.04   # (ou versions moins récentes)
```
```bash
unset SESSION_MANAGER
```
```bash
fluent | cfx5 | icemcfd
```

*   La commande `unset SESSION_MANAGER` permet d'éviter le message d'erreur suivant au lancement de Fluent.
    **[Erreur de gestion de session Qt : Aucun des protocoles d'authentification spécifiés n'est pris en charge]**
*   Si le message suivant est affiché au lancement de icemcfd ...
    **[Erreur de violation de segmentation - sortie après une sauvegarde d'urgence]**
    ... ne cliquez pas sur le bouton *OK*, autrement icemcfd va planter. Faites plutôt ce qui suit (une seule fois) :
    sélectionnez *Onglet Paramètres -> Affichage -> cocher X11 -> Appliquer -> OK -> Fichier -> Quitter*
    L'erreur ne devrait pas se produire quand vous démarrez de nouveau icemcfd.

### Workbench

### Rocky

```bash
module load clumod ansysrocky/2023R2 CcEnv StdEnv/2020 ansys/2023R2   # ou
```
```bash
module load clumod ansysrocky/2024R2.0 CcEnv StdEnv/2023 ansys/2024R2.04   # ou
```
```bash
module load CcEnv StdEnv/2023 ansys/2025R1
```

*   `Rocky` Le module Ansys lit le `~/licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules `ansysrocky` locaux permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de `-h` pour *aide* n'est pas testé).
*   `RockySchedular`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions 2024R2 ou moins récentes ne fonctionnent que sur gra-vdi et Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions 2025R1 et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore pris en charge par le serveur de licence SHARCNET).
*   Le serveur de licence SHARCNET inclut Rocky; son utilisation est gratuite pour la recherche.
*   Rocky prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 CPU et 1 GPU pour un maximum de 8 heures, lancez

```bash
salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount
```

### Ansys EDT

*   Ouvrez une fenêtre de terminal et chargez le module avec
    ```bash
    module load SnEnv ansysedt/2023R2   # ou
    ```
    ```bash
    module load SnEnv ansysedt/2021R2
    ```
*   Dans le terminal, entrez `ansysedt` et attendez que l'interface s'affiche.
*   Ceci doit être fait une seule fois :
    *   sélectionnez *Outils -> Options -> Options HPC et analyse -> Options*
    *   dans le menu déroulant, changez *Licence HPC* pour **Pool** (pour utiliser plus de 4 cœurs)
    *   cliquez sur *OK*
*   ---------- EXEMPLES ----------
*   Pour copier dans votre compte les exemples Antennas de 2023R2 :
    *   connectez-vous à une grappe (par exemple Graham)
    *   ```bash
        module load ansysedt/2023R2
        ```
    *   ```bash
        mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; cd ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf Antennas
        ```
    *   ```bash
        cp -a $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT
        ```
*   Pour faire exécuter un exemple :
    *   ouvrez un fichier `.aedt` et cliquez sur *HFSS -> Vérification de validation*
    *   (si la validation produit une erreur, fermez et ouvrez de nouveau la simulation autant de fois que nécessaire)
    *   pour lancer la simulation, cliquez sur *Projet -> Analyser tout*
    *   pour quitter sans sauvegarder la solution, cliquez sur *Fichier -> Fermer -> Non*
*   si le programme plante et ne repart pas, essayez les commandes suivantes :
    *   ```bash
        pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"
        ```
    *   ```bash
        rm -rf ~/.mw   # (au lancement, ansysedt utilisera la configuration initiale)
        ```

### Ensight

```bash
module load SnEnv
```
```bash
ansys/2024R2.04   # (ou versions plus anciennes jusqu'à 2021R2)
```
```bash
ensight
```

### Mapdl

```bash
module load CcEnv StdEnv/2023
```
```bash
ansys/2024R2.04   # (ou versions plus anciennes)
```
```bash
mapdl -g          # (pour démarrer l'interface graphique directement), ou,
```
```bash
unset SESSION_MANAGER; launcher -> click RUN button
```

### Bureau Jupyter Lab

#### Rocky

```bash
module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2
```
```bash
module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04
```
```bash
module load StdEnv/2023 ansys/2025R1
```

*   `Rocky` Le module Ansys lit le `~/licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules `ansysrocky` locaux permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de `-h` pour *aide* n'est pas testé).
*   `RockySchedular`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions 2024R2 ou moins récentes ne fonctionnent que sur gra-vdi et Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions 2025R1 et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore pris en charge par le serveur de licence SHARCNET).
*   Le serveur de licence SHARCNET inclut Rocky; son utilisation est gratuite pour la recherche.
*   Rocky prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 CPU et 1 GPU pour un maximum de 8 heures, lancez

```bash
salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount
```

**Nœud de calcul (aucun GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu de gauche du bureau
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau Jupyter Lab
*   Puisque l'icône par défaut est configurée pour un nœud GPU, nous devons la personnaliser pour que Workbench puisse être redémarré en mode Mesa. Pour continuer, quittez le bureau Workbench, ouvrez une fenêtre de terminal et exécutez les commandes suivantes sur la ligne de commande :
    ```bash
    cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop
    ```
    puis modifiez `workbench-mesa.desktop` et changez `runwb2` en `runwb2 -oglmesa`
    Enregistrez le fichier puis cliquez sur votre nouvelle icône personnalisée pour démarrer Workbench.
    Notez que l'icône Workbench que vous avez créée persistera pour les sessions futures jusqu'à ce qu'elle soit supprimée manuellement avec : `rm -f ~/Desktop/workbench-mesa.desktop`

**Nœud de calcul (GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu de gauche du bureau
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau Jupyter Lab

#### Ensight

```bash
module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6
```
```bash
export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib
```
```bash
ensight -X
```

## Particularités selon le site d'utilisation

### Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de *recherche universitaire publiable*; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Multiphysics Campus Solution en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par ANSYS en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences `anshpc` de 1986 est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50% en CPU seront probablement signalées par le système et examinées par notre équipe technique.

unset SLURM_GTIDS

**MISE À JOUR :** Depuis décembre 2022, chaque utilisateur peut exécuter 4 travaux en utilisant un total de 252 `anshpc` (plus 4 `anshpc` par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon ((252 + 4 * nombre de tâches) / nombre de tâches). En octobre 2024, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

#### Fichier du serveur de licence

Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `ansys.lic` comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
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
#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-06:00       # Spécifiez la limite de temps jj-hh:mm
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne modifiez pas

module load ansys/2020R1  
```
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

Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur gra-vdi), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `pkill -9 -e -u $USER -f "ansys"` pour libérer vos licences. Prenez note que gra-vdi possède deux nœuds (gra-vdi3 et gra-vdi4) qui vous sont assignés au hasard quand vous vous connectez avec TigerVNC; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (`gra-vdi3.sharcnet.ca` ou `grav-vdi4.sharcnet.ca`) quand vous vous connectez.

## Fabrication additive

Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

### Activer la fabrication additive

Nous décrivons ici comment obtenir l'extension ACT de Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple ANSYSMotion, désinstallez-les à partir de votre projet.

#### Télécharger l'extension

*   téléchargez `AdditiveWizard.wbex` à partir de [https://catalog.ansys.com/](https://catalog.ansys.com/)
*   téléversez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser

#### Lancer Workbench

*   Voir la section Workbench dans [Mode graphique](#mode-graphique) plus haut.
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec *Fichier -> Ouvrir*.

#### Ouvrir le gestionnaire d'extensions

*   Cliquez sur la page *ACT Démarrage* pour faire afficher l'onglet de la page *ACT Accueil*.
*   Cliquez sur *Gérer les extensions* pour ouvrir le gestionnaire d'extensions.

#### Installer l'extension

*   Cliquez sur la boîte avec le signe + sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

#### Charger l'extension

*   Cliquez pour sélectionner la boîte AdditiveWizard, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Charger l'extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

#### Supprimer l'extension

*   Cliquez pour désélectionner la boîte AdditiveWizard, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Ne pas charger par défaut*, ce qui empêche le chargement de l'extension pour les futures sessions.

### Exécuter la fabrication additive

#### Gra-vdi

Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing sur gra-vdi en utilisant jusqu'à 16 cœurs comme suit :

*   Lancez Workbench sur gra-vdi comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*.
*   Cliquez sur *Fichier -> Ouvrir* et sélectionnez `test.wbpj` puis cliquez sur *Ouvrir*.
*   Cliquez sur *Affichage -> Réinitialiser l'espace de travail* si votre écran est gris.
*   Lancez *Mécanique, Effacer les données générées*, sélectionnez *Distribué*, spécifiez *Cœurs*.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

Vérifiez l'utilisation :
*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion gra-vdi ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur gra-vdi. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (Fluent, Workbench, etc.) n'est pas correctement terminée avant que vncviewer ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

#### Grappe

Préparation du projet

Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans la section Workbench de la section *Soumettre des tâches en lot sur nos grappes* ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)`; ou 2. enregistrez une copie du fichier `YOURPROJECT.wbpj` d'origine et du répertoire `YOURPROJECT_files` correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne FilePath.

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

Une fois la tâche complétée, son *temps d'exécution réel de la tâche* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le temps d'exécution réel diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

## Aide

La documentation officielle complète pour les versions récentes d'Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes, telles qu'Ansys 2023R[1|2], nécessite toutefois [une connexion](https://ansyshelp.ansys.com/). La documentation pour les développeurs se trouve dans le [Portail des développeurs Ansys](https://developer.ansys.com). Les ressources d'apprentissage supplémentaires comprennent les [vidéos Ansys HowTo](https://www.youtube.com/@AnsysHowTo/videos), le [Pôle éducatif Ansys](https://innovationspace.ansys.com/educator-hub/) et la [série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

```bash
#module load ansys/2021R1
module load ansys/2021R2