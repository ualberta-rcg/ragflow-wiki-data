---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "f027100479d213b7645a6c2e137d8152"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:15:19.070801+00:00"

tags:
  - software

keywords:
  - "Vérifier la licence"
  - "remise en file d'attente"
  - "Workbench"
  - "trillium"
  - "serveur de licence"
  - "lmutil lmstat"
  - "Plusieurs nœuds"
  - "compte utilisateur"
  - "CC_CLUSTER"
  - "compatibilité des versions"
  - "script Slurm"
  - "Narval"
  - "journal file"
  - "intelmpi"
  - "nombre de cœurs"
  - "solveur parallèle"
  - "fenêtre de temps de Slurm"
  - "fichiers de simulation"
  - "fichier de licence"
  - "scripts de soumission"
  - "SLURM"
  - "calcul parallèle"
  - "script"
  - "partitionnement du maillage"
  - "SBATCH"
  - "Formats de fichiers"
  - "Redémarrage"
  - ".cas/.dat"
  - "Nœuds de calcul"
  - "Configuration"
  - "SLURM_ARRAY_JOB_ID"
  - "Partitionnement du maillage"
  - "Fonctions UDF"
  - "licence CMC"
  - "temps d'exécution"
  - "Ansys Electronics Desktop"
  - "Fluent"
  - "redémarrage"
  - "bash script"
  - "MPI"
  - "cellules par cœur"
  - "soumettre des tâches en lot"
  - "Script Slurm"
  - "service packs"
  - "Calcul Canada"
  - "Bash script"
  - "formats de fichiers"
  - "Fichier de licence"
  - "fichier de journalisation"
  - "Fichiers de journalisation"
  - "Fichier de journalisation"
  - "guide d'utilisation"
  - "Fichier de cas et de données"
  - "salloc"
  - "simulation"
  - "ANSYSLMD_LICENSE_FILE"
  - "fluent"
  - "Ansys Fluent"
  - "ordonnanceur Slurm"
  - "UDF"
  - "ansys"
  - "suite Ansys"
  - ".cas.h5/.dat.h5"
  - "simulations Fluent"
  - "fichier de cas"
  - "Simulation"
  - "licence"
  - "Script bash"
  - "grappes"
  - "durée totale de la simulation"
  - "interface graphique de Fluent"
  - "Ordonnanceur Slurm"
  - "grappes de calcul"
  - "module load"
  - "messages d'erreur"
  - "commandes"
  - "ANSYS Fluent"
  - "Ansys Mechanical/Fluids"
  - "nombre de redémarrages"
  - "script bash"
  - "version antérieure"
  - "Compute nodes"
  - "Interface TUI"
  - "Serveur de licence local"
  - "Fichier de cas"
  - "Pas de temps"
  - "Ansys"
  - "openmpi"
  - "OpenMPI"

questions:
  - "Comment fonctionne le système de licence pour utiliser la suite logicielle Ansys sur les grappes de calcul ?"
  - "Quelles sont les étapes à suivre pour configurer son propre serveur de licence dans son répertoire personnel ?"
  - "Quelle démarche supplémentaire est obligatoire pour que la licence fonctionne si elle a été obtenue auprès de CMC ?"
  - "Que doit-on envoyer à l'adresse cmcsupport@cmc.ca pour que la licence puisse fonctionner ?"
  - "Où peut-on trouver l'information concernant le nombre de cœurs qu'il est possible d'utiliser avec une licence CMC ?"
  - "Quels sont les guides spécifiques mentionnés qu'il faut consulter pour accéder à la section \"Other Tricks and Tips\" ?"
  - "Quelles sont les trois informations de base à obtenir auprès de l'administrateur pour configurer un serveur de licence Ansys déjà prêt à l'emploi ?"
  - "Quelles exigences supplémentaires doivent être respectées si le serveur de licence local n'a jamais été configuré pour la grappe de calcul ?"
  - "Quelle est la procédure à suivre en ligne de commande pour vérifier que le fichier de licence est correctement configuré et fonctionnel ?"
  - "What parameters are used to allocate compute node resources with the salloc command?"
  - "Which software modules must be loaded into the environment before executing the Ansys commands?"
  - "How does the script verify that the Ansys license server is up and running?"
  - "Comment doit-on configurer le lancement d'Ansys Workbench pour utiliser un serveur de licence distant au lieu du serveur par défaut ?"
  - "Quelles sont les limites spécifiques de cœurs et de mémoire à respecter lors de l'utilisation de Mechanical et Fluent sur l'environnement gra-vdi ?"
  - "Quelles sont les commandes de dépannage à utiliser en cas de blocage d'Ansys et quelles sont les règles de compatibilité entre ses différentes versions ?"
  - "Est-il possible d'ouvrir une simulation Ansys avec une version antérieure à celle utilisée pour sa création ?"
  - "Quels problèmes peuvent survenir si l'on tente de lancer une simulation avec une ancienne version du logiciel ?"
  - "Comment peut-on identifier la version d'Ansys utilisée pour créer un fichier cas dans le cadre d'une simulation Fluent ?"
  - "Quelles sont les restrictions actuelles liées aux serveurs de licences pour l'utilisation des versions les plus récentes d'Ansys, comme la version 2025R1.02 ?"
  - "Comment fonctionne la nomenclature des modules Ansys à partir de 2024 pour identifier et charger des correctifs (service packs) spécifiques ?"
  - "Pourquoi l'exécution de tâches en lot avec Ansys nécessite-t-elle des directives particulières avec l'ordonnanceur Slurm ?"
  - "Quelles sont les étapes de préparation et d'exportation des fichiers requises sur un ordinateur local avant de lancer Ansys Fluent sur la grappe de calcul ?"
  - "Comment peut-on gérer automatiquement les erreurs de démarrage liées à un manque de licence et quels sont les risques associés à la remise en file d'attente ?"
  - "Pourquoi est-il recommandé d'utiliser un script d'ordonnancement Slurm « par nœud » plutôt que « par cœur » pour l'exécution des tâches ?"
  - "Pourquoi les applications de la suite Ansys ne peuvent-elles pas être utilisées directement avec l'ordonnanceur Slurm pour le calcul parallèle ?"
  - "Quelle méthode faut-il employer pour lancer une tâche parallèle avec les différents paquets Ansys ?"
  - "Sur quelle grappe de calcul spécifique les scripts de soumission fournis pourraient-ils nécessiter des ajustements ?"
  - "Quelle est la procédure alternative décrite pour effectuer le partitionnement du maillage et exécuter la tâche sur la grappe ?"
  - "Quel est l'avantage principal de réaliser le partitionnement manuellement dans l'interface graphique de Fluent ?"
  - "Quelles sont les conditions requises concernant le nombre de partitions et de cellules par cœur pour obtenir une efficacité optimale ?"
  - "Quelles sont les différences de configuration Slurm entre l'allocation des ressources par nœud et par cœur pour exécuter ANSYS Fluent ?"
  - "Comment le script gère-t-il les spécificités d'exécution MPI selon le cluster utilisé, comme Narval ou Nibi ?"
  - "Quels modules et variables d'environnement doivent être chargés et configurés avant de lancer le fichier journal Fluent ?"
  - "How do the Slurm `#SBATCH` directives differ when allocating resources by entire nodes versus by individual cores?"
  - "What specific ANSYS module versions are required to run jobs on the Trillium cluster compared to the Narval cluster?"
  - "How does the provided bash script alter the Fluent execution command depending on whether the job is allocated to a single node or multiple nodes?"
  - "Quelle est la différence entre les options de réseau `-peth` et `-pib` utilisées dans la commande Fluent selon l'environnement ?"
  - "Comment le script configure-t-il l'exécution d'ANSYS Fluent pour une utilisation sur plusieurs nœuds, notamment sur la grappe Narval ?"
  - "Quel est le rôle du fichier de machines (`machinefile`) et du fichier journal (`MYJOURNALFILE`) dans l'automatisation de cette tâche ?"
  - "What specific version of ANSYS is required to run successfully on the Trillium cluster according to the script?"
  - "What are the acceptable values that can be assigned to the MYVERSION variable?"
  - "How does this script handle ANSYS licensing compared to the default user license file?"
  - "Quels liens symboliques vers des répertoires ou fichiers inscriptibles doivent obligatoirement exister pour éviter l'annulation immédiate de la tâche ?"
  - "Dans quelles conditions spécifiques est-il recommandé d'utiliser les scripts de remise en file d'attente pour obtenir une licence Fluent ?"
  - "Quel est le risque d'utiliser la fonction de remise en file d'attente pour des simulations qui plantent après une longue période ou qui génèrent des avertissements ?"
  - "Comment le script Slurm gère-t-il la relance automatique ou l'annulation des tâches en fonction du succès ou de l'échec de la simulation ?"
  - "Quelles modifications spécifiques doivent être apportées aux fichiers journaux (sample.jou et sample-restart.jou) pour configurer correctement le redémarrage d'une tâche intensive ?"
  - "De quelle manière le nombre total de pas de temps et la durée globale de la simulation sont-ils calculés en fonction du nombre de redémarrages définis ?"
  - "What user-defined variables must be specified at the beginning of the script to configure the ANSYS job?"
  - "How does the script conditionally adjust the environment setup based on the specific cluster being used, such as \"narval\" or \"nibi\"?"
  - "Which specific Intel MPI modules and environment variables are loaded or modified when the script detects it is running on the \"narval\" cluster?"
  - "Pourquoi devrait-on choisir l'option 1 plutôt que l'option 2 pour le premier pas de sample.jou ?"
  - "Comment la durée totale de la simulation et le nombre de fichiers de résultats sont-ils calculés si l'option 2 est choisie ?"
  - "Comment doit-on déterminer la valeur du temps demandé pour la fenêtre d'exécution de Slurm ?"
  - "Quel est l'objectif principal de ce script SLURM et pour quel logiciel de simulation est-il conçu ?"
  - "Comment le script gère-t-il le processus de redémarrage automatique de la simulation à l'aide des tableaux de tâches (job arrays) SLURM ?"
  - "De quelle manière le script adapte-t-il sa configuration MPI et ses paramètres réseau en fonction de la grappe de calcul spécifique (comme Narval ou Nibi) utilisée ?"
  - "Quelles conditions déclenchent l'annulation de la tâche SLURM via la commande scancel dans ce script ?"
  - "Comment le script gère-t-il et signale-t-il l'échec d'une simulation ?"
  - "Quel est l'objectif principal du script bash présenté sous l'onglet \"Plusieurs nœuds (par cœur + redémarrage)\" ?"
  - "Comment le script Slurm gère-t-il les redémarrages successifs de la simulation à l'aide des tâches de tableau (array tasks) ?"
  - "Quel est le rôle principal des fichiers de journalisation (journal files) et quels paramètres permettent-ils de modifier dans ANSYS Fluent ?"
  - "Quelle est la différence de format de fichier de sauvegarde entre les versions de Fluent antérieures à 2019R3 et les versions à partir de 2020R1 ?"
  - "Où peut-on consulter la liste des commandes et obtenir plus d'informations sur l'utilisation de Fluent ?"
  - "Quelle commande permet d'utiliser les anciens formats de fichiers par défaut (.cas/.dat) pour les modules jusqu'à la version 2019R3 ?"
  - "Quels sont les formats de fichiers les plus efficaces introduits pour les versions à partir de 2020R1 ?"
  - "Quelles sont les commandes spécifiques utilisées dans les fichiers de journalisation pour configurer et sauvegarder une simulation temporaire par rapport à une simulation stable ?"
  - "Quelle précaution essentielle faut-il prendre lors du transfert d'un fichier UDF d'un environnement Windows vers la grappe Linux ?"
  - "Comment doit-on préparer le fichier de cas et le fichier de journalisation pour garantir que l'exécution de l'UDF soit entièrement contrôlée par les commandes lors de la soumission ?"
  - "À quel endroit précis du fichier de journalisation doit-on ajouter les nouvelles commandes par rapport à la lecture des fichiers de simulation cas et dat ?"
  - "Quelles vérifications préalables doivent être effectuées dans les boîtes de dialogue des UDF avant de télécharger le fichier de cas ?"
  - "Quel est l'objectif principal visé en s'assurant qu'aucun UDF n'est préconfiguré lors de la soumission des tâches ?"

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
La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas de licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez l'aspect légal de son utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](technical-support.md).

## Configurez votre propre fichier de licence
Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire personnel (`/home`).
Pour indiquer votre propre serveur de licence, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient la ligne ci-dessous, où vous remplacez `FLEXPORT@LICSERVER` par les valeurs de votre serveur.

```text title="ansys.lic"
setenv("ANSYSLMD_LICENSE_FILE", "FLEXPORT@LICSERVER")
```

Les valeurs correspondant aux serveurs de licence CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un différent serveur, voir [Serveurs de licence locaux](#serveurs-de-licence-locaux) ci-dessous.

| Licence | Grappe                    | LICSERVER              | FLEXPORT | INTEPORT | VENDPORT | NOTES                                |
| :------ | :------------------------ | :--------------------- | :------- | :------- | :------- | :----------------------------------- |
| CMC     | beluga                    | `10.20.73.21`          | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC     | cedar                     | `172.16.0.101`         | `6624`   | `2325`   | s.o.     | aucune                               |
| CMC     | graham                    | `10.25.1.56`           | `6624`   | `2325`   | s.o.     | nouvelle IP le 21 février 2025       |
| CMC     | narval                    | `10.100.64.10`         | `6624`   | `2325`   | s.o.     | aucune                               |
| SHARCNET| beluga/cedar/graham/gra-vdi/nibi/narval/rorqual | `license3.sharcnet.ca` | `1055`   | `2325`   | s.o.     | aucune                               |
| SHARCNET| niagara                   | `localhost`            | `1055`   | `2325`   | `1793`   | aucune                               |

Si vous avez obtenu une licence de CMC, vous devez faire parvenir le nom d'utilisateur associé à votre compte avec l'Alliance à cmcsupport@cmc.ca; autrement, la licence ne fonctionnera pas. Pour connaître le nombre de cœurs que vous pouvez utiliser avec une licence CMC, voyez les sections *Other Tricks and Tips* des [guides Ansys Electronics Desktop et Ansys Mechanical/Fluids](https://www.cmc.ca/?s=Other+Tricks+and+Tips&lang=en/).

### Serveurs de licence locaux
Avant que le serveur de licence de votre établissement puisse être utilisé, les coupe-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans le paragraphe *Prêt à utiliser* ci-dessous. Autrement, référez-vous au paragraphe *Configuration requise* un peu plus bas.

#### Prêt à utiliser
Pour utiliser un serveur de licence ANSYS déjà configuré pour être utilisé sur la grappe où vous allez soumettre des tâches, contactez votre administrateur de serveur de licences Ansys et obtenez les trois éléments d'information suivants :
1.  le nom d'hôte complet (`LICSERVER`) du serveur
2.  le port flex (`FLEXPORT`) pour Ansys, habituellement `1055`
3.  le port d'interconnexion (`INTEPORT`), habituellement `2325`
Une fois les trois éléments d'information collectés, configurez votre fichier `~/.licenses/ansys.lic` en entrant les valeurs de `LICSERVER`, `FLEXPORT` et `INTEPORT` dans le modèle *ansys.lic* ci-dessus.

#### Configuration requise
Si votre serveur de licence Ansys local n'a jamais été configuré pour être utilisé sur la ou les grappes où vous allez soumettre des tâches, en plus des 3 éléments ci-dessus, vous devrez ÉGALEMENT obtenir les éléments suivants auprès de l'administrateur :
4.  le numéro de port statique du fournisseur (`VENDPORT`)
5.  confirmation que `<nom_serveur>` se résoudra à la même adresse IP que `LICSERVER` sur nos grappes
où `<nom_serveur>` peut être trouvé dans la première ligne du fichier de licence avec le format *SERVER \<nom_serveur\> \<ID_hôte\> \<port_lmgrd\>*. L'élément 5 est obligatoire, sinon les extractions de licences Ansys ne fonctionneront sur aucune grappe distante. S'il s'avère que `<nom_serveur>` ne répond pas à cette exigence, demandez à votre administrateur de licence de remplacer `<nom_serveur>` par le même nom d'hôte complet que `LICSERVER` ou au moins par un nom d'hôte qui se résoudra à la même adresse IP que `LICSERVER` à distance.

## Vérifier la licence
Pour vérifier si `ansys.lic` est bien configuré et fonctionne correctement, copiez et collez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches. La seule différence est de spécifier `YOURUSERID`. Si le logiciel n’est pas à jour sur le serveur de licence distant, un problème peut survenir si la dernière version du module Ansys est chargée pour effectuer des tests. Pour que la licence fonctionne quand des tâches sont soumises, assurez-vous que la même version du module Ansys qui est chargé par votre script est utilisée dans les commandes ci-dessous.

```bash
gra-login:~ cd /tmp
gra-login:/tmp salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
compute-node/tmp module load StdEnv/2023; module load ansys/2023R2
compute-node:/tmp $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE 1> /dev/null || echo Fail
```

```bash
login-node:~ cd /tmp
login-node:/tmp salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
compute-node/tmp module load StdEnv/2023; module load ansys/2025R2.04
compute-node:/tmp $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```

La sortie `Success` indique que les licences devraient être extraites correctement lors de la soumission de tâches à la file d'attente.
La sortie `Fail` indique un problème avec la configuration de la licence et que les tâches échoueront probablement.

!!! note "Remarque 1"
    Pour les modules Ansys installés localement, la commande `runwb2` de `SnEnv` utilise par défaut le serveur de licence SHARCNET, tel que défini dans le fichier du module Ansys que vous chargez. Pour utiliser un serveur distant, lancez plutôt Workbench avec `runwb2-gui`, car ce script enveloppant (*wrapper*) lira votre fichier `~/.licenses/ansys.lic` comme les modules disponibles sous `StdEnv/2023`. De plus, l'option interactive d'utilisation du serveur CMC (acheminé via le serveur SHARCNET CMC CadPASS) sera proposée, éliminant ainsi la nécessité de le configurer dans votre fichier `ansys.lic`.

!!! note "Remarque 2"
    Lorsque vous démarrez Fluent à partir de Workbench avec la version 2025R1, avant de cliquer sur le bouton *Démarrer*, cliquez sur l'onglet *Environnement* du panneau de lancement de *Lanceur Fluent* et copiez/collez `HOOPS_PICTURE=opengl` dans le champ de saisie vide. Vous pouvez aussi définir `export HOOPS_PICTURE=opengl` dans votre environnement avant de démarrer Workbench. L'une ou l'autre de ces actions empêchera le message suivant, qui apparaîtrait dans les messages de démarrage de l'interface utilisateur : [Avertissement : un rastériseur logiciel a été détecté, l'accélération matérielle sera désactivée.]

!!! note "Remarque 3"
    Lorsque vous exécutez Mechanical dans Workbench sur `gra-vdi`, assurez-vous de cocher *Distribué* dans le panneau *Solveur* du ruban supérieur et de spécifier une valeur maximale de **24 cœurs**. Lorsque vous exécutez Fluent sur `gra-vdi`, ne cochez pas *Distribué* et spécifiez une valeur maximale de **12 cœurs**. N'essayez pas d'utiliser plus de 128Go de mémoire, sinon Ansys atteindra la limite et sera arrêté. Si vous avez besoin de plus de cœurs ou de mémoire, utilisez un nœud de calcul sur une grappe pour exécuter votre session graphique (comme décrit dans la section *Nœuds de calcul* ci-dessus). Lorsque vous effectuez une ancienne tâche de prétraitement ou de post-traitement avec Ansys sur `gra-vdi` et que vous n'exécutez pas de calcul, utilisez uniquement **4 cœurs**, sinon les licences HPC seront extraites inutilement.

!!! note "Remarque 4"
    Dans de très rares cas, l'interface graphique de Workbench ou de certains programmes qu'il exécute se bloquent ou ne démarrent pas correctement, notamment si `vnsviewer` se déconnecte avant que Ansys soit fermé correctement. En général, si Ansys ne fonctionne pas correctement, ouvrez une nouvelle fenêtre de terminal sur `gra-vdi` et exécutez `pkill -9 -e -u $USER -f "ansys|fluent|mwrpcss|mwfwrapper|ENGINE|mono"` pour arrêter complètement tous les processus Ansys. Si le problème persiste et que vous utilisiez l'interface graphique sur des nœuds de calcul avant de travailler sur `gra-vdi`, essayez d'exécuter `rm -rf .ansys`. Si le problème concerne `/home`, `/project` ou `/scratch` (la commande `df` bloque), il est fort probable qu'Ansys recommence à fonctionner normalement une fois le problème de stockage résolu.

```bash
compute-node:/tmp fluent -g 2d -n 2
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

## Compatibilité des versions
Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une moins récente version de Ansys devraient pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec `ansys/2022R2` devrait fonctionner avec `ansys/2023R2`, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
$ grep -ia fluent combustor.cas
   (0 "fluent15.0.7  build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
   ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge

## ANSYS Fluent
Voici la procédure habituelle pour utiliser Fluent avec les grappes de Calcul Canada :

## Nouveautés
Ansys publie régulièrement des *service packs* pour regrouper plusieurs mises à jour apportant différents correctifs et améliorations à ses versions majeures. Des informations similaires pour les versions précédentes peuvent généralement être trouvées sur [le blog Ansys](https://www.ansys.com/blog), en utilisant la barre de recherche FILTERS. Par exemple, la recherche de `What’s New Fluent 2024 gpu` affichera le document `[What’s New for Ansys Fluent in 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1)` qui contient une multitude d'informations sur la prise en charge des GPU. Spécifier un numéro de version dans le champ de recherche [Press Release](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations sur les nouvelles versions. Le module `ansys/2025R1.02` pour la dernière version de Ansys a été installé récemment; pour l'utiliser cependant, vous avez besoin d'un serveur de licence comme celui de CMC. La mise à jour du serveur de licence de SHARCNET est en cours et tant que ce travail ne sera pas terminé, seules les versions `ansys/2024R2.04` ou moins récentes seront prises en charge. Si un module pose problème ou pour demander l'installation d'une nouvelle version, écrivez au [soutien technique](technical-support.md).

## Correctifs
À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *service pack* est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun *service pack* peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le *service pack* 3 peut être chargé avec `module load ansys/2024R1.03`. Si un *service pack* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *service pack* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *service pack* installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les *service packs* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *service pack* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *service pack* rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque *service pack* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

## Soumettre des tâches en lot sur nos grappes
Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](running-jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

### Ansys Fluent
La procédure suivante est habituellement utilisée pour exécuter Fluent sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *Fichier > Exporter > Cas…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `FFF-1.cas.gz`.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *Fichier > Exporter > Données…* ou trouvez-le dans le même répertoire `/project` (`FFF-1.dat.gz`).
4.  [Transférez](transferring-data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](project-layout.md) ou [/scratch](storage-and-file-management.md#types-de-stockage) de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `FFF-1.*` ou renommez-les au téléversement.
5.  Créez un fichier de journalisation dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancez le solveur et enregistrez les résultats. Voyez les exemples ci-dessous et n'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour le script sous l'onglet *Plusieurs nœuds (par cœur + remise en attente)* plus loin. Cependant, ceci remet aussi en attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en attente est ou non due à un problème de licence. Si vous découvrez que la remise en attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `scancel jobid` et corrigez le problème.
7.  Lorsque la [tâche est terminée](running-jobs.md), vous pouvez télécharger le fichier de données et le retourner dans Fluent avec *Fichier > Importer > Données…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale
La plupart des tâches Fluent devraient utiliser le script *par nœud* ci-dessous pour minimiser le temps d'attente et maximiser la performance en utilisant le moins de nœuds possible. Les tâches demandant beaucoup de cœurs CPU pourraient attendre moins longtemps dans la queue avec le script *par cœur*, mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent fournir une alternative plus robuste si Fluent plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts standards Intel avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de Fluent, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts Intel. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

##### Plusieurs nœuds (par nœud)

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

##### Plusieurs nœuds (par cœur)

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

##### Plusieurs nœuds (par nœud, Narval)

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

##### Plusieurs nœuds (par cœur, Narval)

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

##### Plusieurs nœuds (par nœud, Trillium)

```bash title="script-flu-bynode-intel-tri.sh"
#!/bin/bash

#SBATCH --account=def-group      # Specify account name
#SBATCH --time=00-03:00          # Specify time limit dd-hh:mm
#SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
#SBATCH --ntasks-per-node=16     # Specify number cores per node (max 192 on trillium)
##SBATCH --mem=0                 # Do not uncomment (be default trillium uses all memory per node)
#SBATCH --cpus-per-task=1        # Do not change (required parameter)

module load StdEnv/2023          # Do not change
module load ansys/2025R2.04      # only 2025R2 or newer works on trillium

MYJOURNALFILE=sample.jou         # Specify your journal file name
MYVERSION=3d                     # Specify 2d, 2ddp, 3d or 3ddp

# These settings are used instead of your ~/.licenses/ansys.lic
LICSERVER=license1.computecanada.ca   # Specify license server hostname
FLEXPORT=1055                         # Specify server flex port
VENDPORT=1793                         # Specify server vendor port

# ------- do not change any lines below --------

ssh tri-gw -fNL $FLEXPORT:$LICSERVER:$FLEXPORT
ssh tri-gw -fNL $VENDPORT:$LICSERVER:$VENDPORT
export ANSYSLMD_LICENSE_FILE=$FLEXPORT@localhost
export ANSYSLI_SERVERS=$INTEPORT@localhost

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

##### Plusieurs nœuds (par nœud + remise en attente)

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

##### Plusieurs nœuds (par cœur + remise en attente)

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
Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de *sample.cas*, *sample.dat* et *sample.jou* doit être présent. Modifiez le fichier *sample.jou* pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier de journalisation avec `cp sample.jou sample-restart.jou` et modifiez le fichier *sample-restart.jou* pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `; /solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez *sample-restart.jou* en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de *sample.jou* est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt+2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1+2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

##### Plusieurs nœuds (par nœud + redémarrage)

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

##### Plusieurs nœuds (par cœur + redémarrage)

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
Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface utilisateur textuelle (`TUI`) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le guide d'utilisation de Fluent pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `/file/cff-files yes`.

##### Fichier de journalisation (stable, cas)

```text title="sample1.jou"
; FICHIER DE JOURNALISATION FLUENT EXEMPLE - SIMULATION STABLE
; ----------------------------------------------
; les lignes commençant par un point-virgule sont des commentaires

; Ne pas demander confirmation pour écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire les fichiers de cas et de données d'entrée
/file/read-case-data FFF-in

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; Ne pas demander confirmation pour écraser les fichiers de sortie par défaut
/file/confirm-overwrite n

; Écrire le fichier de données de sortie final
/file/write-case-data FFF-out

; Écrire un rapport de simulation dans un fichier (facultatif)
/report/summary y "My_Simulation_Report.txt"

; Arrêter Fluent proprement
/exit
```

##### Fichier de journalisation (stable, cas + données)

```text title="sample2.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION STABLE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Ne pas demander confirmation pour écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire les fichiers d'entrée
/file/read-case-data FFF-in

; Écrire un fichier de données toutes les 100 itérations
/file/auto-save/data-frequency 100

; Conserver les fichiers de données des 5 itérations les plus récentes
/file/auto-save/retain-most-recent-files y

; Écrire les fichiers de données dans le sous-répertoire de sortie (ajoute l'itération)
/file/auto-save/root-name output/FFF-out

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; écrire le dernier fichier de cas et de données en sortie
/file/write-case-data FFF-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y "My_Simulation_Report.txt"

; fermez correctement Fluent
exit
```

##### Fichier de journalisation (temporaire)

```text title="sample3.jou"
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION TEMPORAIRE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Ne pas demander confirmation pour écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire le fichier de cas d'entrée
/file/read-case FFF-transient-inp

; Pour la continuation (redémarrage) lire les deux fichiers de cas et de données d'entrée
;/file/read-case-data FFF-transient-inp

; Écrire un fichier de données (et peut-être de cas) toutes les 100 pas de temps
/file/auto-save/data-frequency 100
/file/auto-save/case-frequency if-case-is-modified

; Conserver uniquement les 5 fichiers de données (et peut-être de cas) les plus récents
/file/auto-save/retain-most-recent-files y

; Écrire dans le sous-répertoire de sortie (ajoute le temps d'écoulement et le pas de temps)
/file/auto-save/root-name output/FFF-transient-out-%10.6f

; ##### Paramètres pour la simulation transitoire : #####

; Définir la taille du pas de temps physique
/solve/set/time-step 0.0001

; Définir le nombre d'itérations pour lesquelles les moniteurs de convergence sont rapportés
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

; Arrêter Fluent proprement
/exit
```

### Fonctions UDF
La première étape est de transférer vers la grappe votre fonction définie par l'utilisateur (`UDF`), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui elle exécute Linux. L'UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *UDF interprétées* et *gestionnaire de bibliothèques UDF* ne sont pas configurées pour utiliser un UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interprétée
Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilée
Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `libudf.so` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quelle autre de nos grappes, à condition que votre compte charge la même version du module d'environnement `StdEnv`. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (`load`) `libudf` ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes `libudf` (`compile` et `load`) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de build de type « racetime » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent (exécutée sur n'importe quel nœud de calcul ou sur `gra-vdi`) peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *UDF compilées*, et cliquez sur *Compiler*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

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
Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (`DPM`) comme décrit dans *2024R2 Fluent Users Guide, Part III: Solution Mode, Chapter 24: Modeling Discrete Phase, 24.2 Steps for Using the Discrete Phase Models,* et dans *2024R2 Fluent Customization Manual, Part I: Creating and Using User Defined Functions, Chapter 2: DEFINE Macros, 2.5 Discrete Phase Model (DPM) DEFINE Macros*. Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Propriétés des points* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physique --> Phase discrète*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Créer*. La boîte de dialogue *Définir les propriétés d'injection* contient le menu déroulant *Type d'injection* avec les quatre premiers types disponibles (*simple, groupe, surface, atomiseur à jet plat*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Propriétés des points* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Propriétés des points* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *Fichier* dans le menu déroulant *Type d'injection*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *Fichier* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Définir les propriétés d'injection*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension `.dpm`) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Sélectionner le fichier*, sélectionnez *Tous les fichiers (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur le bouton *OK*. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Définir les propriétés d'injection* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Modèle de phase discrète* et sélectionnez *Interaction avec la phase continue* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple :
```
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```
où un format de fichier stable d'injection de base créé manuellement pourrait ressembler à :
```bash title="zinjection01.inj"
(z=4 12)
( x y z u v w diamètre t débit massique fréquence massique temps nom )
(( 2.90e-02 5.00e-03 0.0 -1,00e-03 0,0 0,0 1,00e-04 2,93e+02 1,00e-06 0,0 0,0 0,0 ) injection-0:1 )
```
notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans *2024R2 Fluent Customization Manual, Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format*.

## CFX

### Scripts pour l'ordonnanceur Slurm
Le résumé des options de ligne de commande peut être affiché avec `cfx5solve -help`. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, `cfx5solve` s'exécute en monoprécision (`-single`). Pour exécuter `cfx5solve` en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, `cfx5solve` prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'ANSYS CFX-Solver Manager pour plus de détails.

##### Nœud simple

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

##### Plusieurs nœuds

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
1.  Connectez-vous à la grappe avec [TigerVNC](vnc.md#noeuds-de-calcul).
2.  Dans le même répertoire où se trouve le fichier de projet (`YOURPROJECT.wbpj`), [lancez Workbench](ansys.md#workbench-3) avec la même version du module Ansys qui a servi à créer le projet.
3.  Dans Workbench, ouvrez le projet avec *Fichier -> Ouvrir*.
4.  Dans la fenêtre principale, faites un clic droit sur *Configuration* et sélectionnez *Effacer toutes les données générées*.
5.  Dans la liste déroulante de la barre de menus du haut, cliquez sur *Fichier -> Quitter* pour sortir de Workbench.
6.  Dans la fenêtre contextuelle Ansys Workbench qui affiche *Le projet actuel a été modifié. Voulez-vous le sauvegarder ?* cliquez sur le bouton *Non*.
7.  Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Puisqu'un nœud de calcul avec jusqu'à 96 cœurs, 768 Go de mémoire et 8 heures d'exécution peut maintenant être réservé pour une session de bureau à la demande, envisagez d'exécuter vos simulations Workbench directement depuis l'interface graphique native de Workbench lorsque cela est possible, comme une option plus intuitive par rapport à la soumission de la tâche à la file d'attente avec un script Slurm.

### Scripts pour l'ordonnanceur Slurm
Pour soumettre un fichier de projet à la queue, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

##### Single node (StdEnv/2023)

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

##### Single node (StdEnv/2020)

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

Pour éviter d'écrire la solution lorsqu'une tâche en cours d'exécution se termine avec succès, changez `Save(Overwrite=True)` à `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera la détermination de l'efficacité de la simulation lorsque `#SBATCH --ntasks` est augmenté, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical
Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Outils -> Écrire les fichiers d'entrée* et en spécifiant *Nom du fichier :* pour `YOURAPDLFILE.inp` et *Enregistrer sous le type :* pour les fichiers APDL en entrée (`*.inp`). Les tâches APDL peuvent ensuite être soumises à la queue avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm
Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `##SBATCH` sont suivies d'un commentaire.

##### Shared Memory Parallel (cpu)

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

##### Distributed Memory Parallel (cpu)

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

##### Shared Memory Parallel (gpu)

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

##### Mémoire parallèle distribuée (GPU)

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

Par défaut, Ansys alloue aux tâches APDL 1024 Mo de mémoire totale et 1024 Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande `mapdl` des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de mise à l'échelle avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (`SMP`) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (`DMP`) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```
gra-login2:~/testcase cat YOURAPDLFILE.inp | grep version
! ANSYS input file written by Workbench version 2019 R3
```

## Rocky
En plus de pouvoir exécuter des simulations en mode graphique (comme indiqué dans la section *Mode graphique* ci-dessous), [Ansys Rocky](https://www.ansys.com/products/fluids/ansys-rocky) peut également exécuter des simulations en mode non graphique. Les deux modes prennent en charge l'exécution de Rocky avec des processeurs uniquement ou avec des processeurs et des [GPU](https://www.ansys.com/blog/mastering-multi-gpu-ansys-rocky-software-enhancing-its-performance). Dans la section ci-dessous, deux exemples de scripts sont fournis où chacun serait soumis à la file d'attente de Graham avec la commande habituelle `sbatch`. Au moment de la rédaction de cet article, aucun des deux scripts n'a été testé et des modifications seraient probablement nécessaires. Il est important de noter que ces scripts ne sont utilisables que sur Graham puisque le module Rocky qu'ils chargent tous les deux n'est (pour le moment) installé que sur Graham localement.

### Scripts pour l'ordonnanceur Slurm
Pour obtenir une liste complète des options de ligne de commande, exécutez `Rocky -h` sur la ligne de commande après avoir chargé un module Rocky (seul `ansysrocky/2023R2` est présentement disponible sur Graham). En ce qui concerne l'utilisation de Rocky avec des GPU pour résoudre des problèmes couplés, le nombre de CPU que vous devez demander (sur le même nœud) doit être augmenté au maximum jusqu'à ce que la limite de scalabilité de l'application couplée soit atteinte. D'autre part, si Rocky est exécuté avec des GPU pour résoudre des problèmes découplés autonomes, seul un nombre minimal de CPU doit être demandé, ce qui permettra à Rocky de fonctionner de manière optimale; par exemple, seuls 2 ou éventuellement 3 CPU peuvent être nécessaires. Enfin, lorsque Rocky est exécuté avec 4 ou plus CPU, des licences `rocky_hpc` seront nécessaires, ce que fournit la licence SHARCNET.

##### CPU seulement

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

##### GPU based

```bash title="script-rocky-gpu.sh"
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
Les scripts Slurm pour utiliser AnsysEDT sont fournis dans une page wiki distincte [ici](https://docs.alliancecan.ca/wiki/AnsysEDT).

## Mode graphique
Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
*   [FIR](https://docs.alliancecan.ca/wiki/Fir): `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](https://docs.alliancecan.ca/wiki/Rorqual): `https://jupyterhub.rorqual.alliancecan.ca`
*   [NARVAL](https://jupyterhub.narval.alliancecan.ca/): `https://jupyterhub.narval.alliancecan.ca/`
*   [TRILLIUM](https://ondemand.scinet.utoronto.ca): `https://ondemand.scinet.utoronto.ca`

Soumettez votre demande de ressources et attendez. Si vous avez démarré une interface de lanceur Jupyter Lab, vous pouvez simplement charger un module logiciel Ansys à partir du menu de gauche, puis cliquer sur l'une des icônes Ansys pour démarrer CFX, Fluent, MAPDL ou Workbench. Autrement, si vous avez démarré un Bureau de calcul/de base à partir du système OnDemand de Nibi, vous devrez ouvrir une fenêtre de terminal, charger manuellement un module Ansys et ensuite taper le nom du programme pour le démarrer en ligne de commande. Pour ce dernier cas, si l'application nécessite des graphiques accélérés pour fonctionner correctement (par exemple pour que Fluent prenne en charge le rendu 3D), alors une ressource GPU complète (H100 ou T4 au moment de la rédaction de ce document) devrait être demandée. Puisque les différentes applications Ansys lancées en mode graphique se comportent différemment lorsque différentes versions de modules Ansys sont chargées, des recommandations pour ajouter des arguments de ligne de commande et exporter des variables d'environnement pour les environnements VirtualGL ou Mesa sont suggérées ci-dessous, selon qu'un GPU a été demandé ou non et qu'un bureau OnDemand ou Jupyter Lab est utilisé.

### Fluent
Pour démarrer Ansys Fluent depuis la ligne de commande d'un Bureau OnDemand, ouvrez une fenêtre de terminal et exécutez les commandes :

*   `module load StdEnv/2023 ansys/2025R1`
*   `fluent`

Lorsque le panneau de sélection contextuel du Lanceur Fluent apparaît, cliquez sur l'onglet Environnement et copiez/collez les paramètres de variable d'environnement suivants, selon que vous avez démarré votre session OnDemand avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses (ce sont des commentaires) et ne mettez pas `export` devant les noms de variables.

**Nœud de calcul (aucun GPU demandé)**

*   `I_MPI_HYDRA_BOOTSTRAP=ssh` (requis sur nibi)
*   `HOOPS_PICTURE=opengl2-mesa` (version 2025R1 ou plus récente)
*   `HOOPS_PICTURE=null` (version 2024R2 ou plus ancienne)
*   Cliquez sur le bouton *Démarrer*

Si `I_MPI_HYDRA_BOOTSTRAP=ssh` n'est pas configuré correctement sur Nibi lorsque Fluent est démarré depuis des sessions de bureau de calcul OnDemand et qu'`intelmpi` est utilisé, Fluent plantera au démarrage en produisant la sortie d'erreur suivante. Si cela se produit, quittez complètement Fluent, arrêtez Workbench et recommencez.
```
[mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for event error
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```

### CFX
Lors du démarrage de CFX depuis un Bureau OnDemand, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal, selon qu'un GPU a été demandé ou non au démarrage du Bureau.

*   `module load StdEnv/2023 ansys/2025R1` (ou plus ancien)
*   `cfx5 -graphics mesa` (aucun GPU demandé)
*   `cfx5 -graphics ogl` (avec GPU demandé)

### Mapdl
Les étapes suivantes pour démarrer l'interface graphique de Mechanical APDL depuis la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre Bureau OnDemand sur un nœud de calcul avec ou sans GPU.

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `mapdl -g`, ou,
*   `launcher` puis cliquer sur le bouton *RUN*

### Workbench
*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `xfwm4 --replace &` (nécessaire seulement si vous utilisez Ansys Mechanical)
*   `export QTWEBENGINE_DISABLE_SANDBOX=1` (nécessaire seulement si vous utilisez CFD-Post)
*   `runwb2`
*   Remarque : Quand vous exécutez en parallèle un programme d'analyse comme Mechanical ou Fluent sur un nœud simple, ne cochez pas la case *Distribué* et indiquez un nombre de cœurs égal à votre **session salloc, moins 1**. Les menus déroulants du Ansys Mechanical Workbench ne répondent pas correctement. Comme solution, lancez `xfwm4 --replace` sur la ligne de commande avant de démarrer Workbench. Pour avoir xfwm4 par défaut, modifiez `~/.vnc/xstartup` et remplacez `mate-session` par `xfce4-session`.

Cette section montre comment démarrer Workbench (et éventuellement Fluent) sur un Bureau OnDemand ou un Bureau Jupyter Lab.

### Jupyter Lab Desktop

#### Rocky
*   `module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2`
*   `module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04`
*   `module load StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit le `~/licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules locaux `ansysrocky` permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de `-h` pour *help* n'est pas testé).
*   `RockySchedular`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions 2024R2 ou moins récentes ne fonctionnent que sur `gra-vdi` et les grappes Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions 2025R1 et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore pris en charge par le serveur de licence SHARCNET).
*   Le serveur de licence SHARCNET inclut Rocky; son utilisation est gratuite pour la recherche.
*   Rocky prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 CPU et 1 GPU pour un maximum de 8 heures, lancez :
    `salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount`

#### Nœud de calcul (aucun GPU demandé)
*   Cliquez pour charger `ansys/2025R1` (ou version plus récente) dans le menu de gauche du Bureau.
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau Jupyter Lab.
*   Étant donné que l'icône par défaut est configurée pour un nœud GPU, nous devons la personnaliser afin que Workbench puisse être redémarré en mode Mesa. Pour continuer, quittez le bureau Workbench, ouvrez une fenêtre de terminal et exécutez les commandes suivantes sur la ligne de commande :
    `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop`
*   Éditez ensuite `workbench-mesa.desktop` et changez `runwb2` en `runwb2 -oglmesa`.
*   Enregistrez le fichier, puis cliquez sur votre icône nouvellement personnalisée pour démarrer Workbench.
*   Notez que l'icône Workbench que vous avez créée persistera pour les sessions futures jusqu'à ce qu'elle soit supprimée manuellement avec : `rm -f ~/Desktop/workbench-mesa.desktop`

#### Nœud de calcul (avec GPU demandé)
*   Cliquez pour charger `ansys/2025R1` (ou version plus récente) dans le menu de gauche du Bureau.
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau Jupyter Lab.

## Problèmes avec SSH
Certains programmes d'interface graphique ANSYS peuvent être exécutés à distance sur un nœud de calcul d'une de nos grappes par redirection X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que MobaXterm. La plupart d'entre vous trouverez les temps de réponse interactifs inacceptables pour les tâches de menu de base, sans parler de l'exécution de tâches plus complexes telles que celles nécessitant du rendu graphique. Les temps d'attente pour démarrer des programmes avec interface graphique peuvent également être très longs, dépendant de votre connexion Internet. Dans un test par exemple, il a fallu 40 minutes pour obtenir l'interface graphique avec SSH alors que `vncviewer` n'a pris que 34 secondes. Malgré la lenteur potentielle lors de la connexion via SSH pour exécuter des programmes avec interface graphique, cela peut toujours être intéressant si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou d'exécuter des calculs. Ces étapes de base sont un point de départ : 1) `ssh -Y username@graham.computecanada.ca`; 2) `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task =4 [--gpus-per-node=1] --account=def-mygroup`; 3) une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, chargez le module Ansys souhaité et essayez d'exécuter le programme.

### Fluids
*   `module load CcEnv StdEnv/2023`
*   `module load ansys/2024R2.04` (ou versions moins récentes)
*   `unset SESSION_MANAGER`
*   `fluent | cfx5 | icemcfd`
*   La commande `unset SESSION_MANAGER` permet d'éviter le message d'erreur suivant au lancement de Fluent :
    *Qt: Erreur de gestion de session : Aucun des protocoles d'authentification spécifiés n'est pris en charge*
*   Si le message suivant est affiché au lancement de icemcfd ...
    *Erreur de violation de segment - sortie après une sauvegarde d'urgence*
    ... ne cliquez pas sur le bouton *OK*, autrement icemcfd va planter. Faites plutôt ce qui suit (une seule fois) :
    sélectionnez *Onglet Paramètres -> Affichage -> cocher X11 -> Appliquer -> OK -> Fichier -> Quitter*
    L'erreur ne devrait pas se produire quand vous démarrez de nouveau icemcfd.

### Rocky
*   `module load clumod ansysrocky/2023R2 CcEnv StdEnv/2020 ansys/2023R2`, ou
*   `module load clumod ansysrocky/2024R2.0 CcEnv StdEnv/2023 ansys/2024R2.04`, ou
*   `module load CcEnv StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit `~/licenses/ansys.lic`
*   `Rocky-gui` Fournit par les modules `ansysrocky` locaux la sélection des serveurs CMC ou SHARCNET
*   `RockySolver` Exécute le solveur rocky à partir de la ligne de commande (l'ajout de `-h` pour *help* n'est pas testé)
*   `RockySchedular` Lance l'interface graphique pour soumettre et exécuter des tâches sur le nœud courant (non testé)
*   Rocky pour 2024R2 et moins récentes est disponible uniquement sur `gra-vdi` et les grappes Graham; l'installation sur toutes les grappes est prévue pour juin
*   Rocky pour 2025R1 et plus récentes est fourni sur toutes les grappes par le module Ansys (pas pris en charge par le serveur de licence SHARCNET)
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
    *   sélectionnez *Outils -> Options -> Options HPC et d'analyse -> Options*
    *   dans le menu déroulant, changez *Licence HPC* pour **Pool** (pour utiliser plus de 4 cœurs)
    *   cliquez sur *OK*
*   ---------- EXEMPLES ----------
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
*   `unset SESSION_MANAGER; launcher -> click RUN button`

Si `I_MPI_HYDRA_BOOTSTRAP=ssh` n'est pas configuré correctement sur Nibi lorsque Fluent est démarré depuis des sessions de bureau de calcul OnDemand et qu'`intelmpi` est utilisé, Fluent plantera au démarrage en produisant la sortie d'erreur suivante. Si cela se produit, quittez complètement Fluent, arrêtez Workbench, puis recommencez.
```
[mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for event error
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```

## Particularités selon le site d'utilisation

### Licence SHARCNET
La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de *recherche universitaire publiable*; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Multiphysics Campus Solution en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio).
Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par ANSYS en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences `anshpc` de 1986 est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50% en CPU seront probablement signalées par le système et examinées par notre équipe technique.

Depuis décembre 2022, chaque utilisateur peut exécuter 4 travaux en utilisant un total de 252 `anshpc` (plus 4 `anshpc` par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon `((252 + 4 * nombre de tâches) / nombre de tâches)`. MISE À JOUR : En octobre 2024, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

Vous pouvez aussi acheter votre propre licence Ansys auprès de [CMC](https://www.cmc.ca/subscriptions/) et utiliser leurs serveurs de licences distants. Ceci présente plusieurs avantages :
*   un serveur de licences institutionnel local n'est pas nécessaire,
*   une licence physique n'a pas besoin d'être obtenue à chaque renouvellement,
*   la licence peut être utilisée [presque n'importe où](https://www.cmc.ca/ansys-campus-solutions-cmc-00200-04847/), y compris à la maison, dans des établissements ou dans toutes les grappes de l'Alliance,
*   les directives de téléchargement et d'installation pour la version Windows d'Ansys sont fournies afin de permettre l'exécution de `spaceclaim` sur votre propre ordinateur (ceci n'est pas possible sur nos systèmes qui sont basés sur Linux).
Il existe cependant une limitation potentiellement sérieuse à prendre en compte : selon [Ansys Quick Start Guides](https://www.cmc.ca/qsg-ansys-cadpass-r20/), il pourrait y avoir une limite de 64 cœurs par utilisateur.

#### Fichier du serveur de licence
Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `ansys.lic` comme suit :
```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
```

#### Licence
Pour connaître le nombre de licences utilisées qui sont associées à votre nom d'utilisateur et le nombre de licences utilisées par tous les utilisateurs, lancez :

```bash
ssh graham.computecanada.ca
module load ansys
lmutil lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER"
```

Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur `gra-vdi`), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `pkill -9 -e -u $USER -f "ansys"` pour libérer vos licences. Prenez note que `gra-vdi` possède deux nœuds (`gra-vdi3` et `gra-vdi4`) qui vous sont assignés au hasard quand vous vous connectez avec `tigervnc`; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (`gra-vdi3.sharcnet.ca` ou `grav-vdi4.sharcnet.ca`) quand vous vous connectez.

## Additive Manufacturing
Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

### Activer Additive
Nous décrivons ici comment obtenir l'extension ACT de Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple ANSYSMotion, désinstallez-les à partir de votre projet.

#### Télécharger l'extension
*   téléchargez `AdditiveWizard.wbex` à partir de `https://catalog.ansys.com/`
*   téléversez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser

#### Lancer Workbench
*   Voir la section Workbench dans [Mode graphique](#workbench) plus haut.
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec *Fichier -> Ouvrir*.

#### Ouvrir le gestionnaire d'extensions
*   Cliquez sur la page ACT Start pour faire afficher l'onglet de la page ACT Home.
*   Cliquez sur Manage Extensions pour ouvrir le gestionnaire d'extensions.

#### Installer l'extension
*   Cliquez sur la boîte avec le signe `+` sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

#### Charger l'extension
*   Cliquez pour sélectionner la boîte `AdditiveWizard`, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte `AdditiveWizard` et sélectionnez *Load extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

#### Supprimer l'extension
*   Cliquez pour désélectionner la boîte `AdditiveWizard`, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte `AdditiveWizard` et sélectionnez *Do not load as default*, ce qui empêche le chargement de l'extension pour les futures sessions.

### Exécuter Additive

#### Gra-vdi
Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing sur `gra-vdi` en utilisant jusqu'à 16 cœurs comme suit :

*   Lancez Workbench sur `gra-vdi` comme décrit ci-dessus dans *Additive Manufacturing -> Activer Additive*.
*   Cliquez sur *Fichier -> Ouvrir* et sélectionnez `test.wbpj` puis cliquez sur *Ouvrir*.
*   Cliquez sur *Vue -> Réinitialiser l'espace de travail* si votre écran est gris.
*   Lancez *Mechanical, Effacer les données générées*, sélectionnez *Distribué*, spécifiez *Cœurs*.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

Vérifiez l'utilisation :
*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion `gra-vdi` ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur `gra-vdi`. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (Fluent, Workbench, etc.) n'est pas correctement terminée avant que `vncviewer` ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

#### Grappe
Préparation du projet

Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Additive Manufacturing -> Activer Additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour Workbench dans la section *Soumettre des tâches en lot sur nos grappes* ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)`; ou 2. enregistrez une copie du fichier `YOURPROJECT.wbpj` d'origine et du répertoire `YOURPROJECT_files` correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne `FilePath`.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

Utilisation des ressources

Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `srun`. Le script pour 8 cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

```
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

Une fois la tâche complétée, son *Job Wall-clock time* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le *Wall-clock time* diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

## Aide
La documentation officielle complète pour les versions récentes Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles qu'Ansys 2023R[1|2] nécessite cependant une [connexion](https://ansyshelp.ansys.com/login). La documentation des développeurs peut être trouvée sur le [Portail des développeurs Ansys](https://developer.ansys.com). Les ressources d'apprentissage supplémentaires incluent les [vidéos Ansys HowTo](https://www.youtube.com/@AnsysHowTo/videos), le [Hub des éducateurs Ansys](https://innovationspace.ansys.com/educator-hub/) et la [série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

```bash
#module load ansys/2021R1
module load ansys/2021R2