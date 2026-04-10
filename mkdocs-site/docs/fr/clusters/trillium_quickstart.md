---
title: "Trillium Quickstart/fr"
slug: "trillium_quickstart"
lang: "fr"

source_wiki_title: "Trillium Quickstart/fr"
source_hash: "abaaa9b7b0e149971df5dd3e9be0d579"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:09:36.191214+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Aperçu

La grappe Trillium est conçue pour prendre en charge des tâches massivement parallèles. Construite par Lenovo Canada, elle est hébergée par SciNet à l'Université de Toronto. Ses trois composantes principales sont :

1.  Sous-grappe de CPU
    *   235 008 cœurs dans 1 224 nœuds de calcul CPU
    *   Chaque nœud de calcul CPU a 192 cœurs provenant de deux processeurs AMD EPYC 9655 de 96 cœurs chacun (Zen 5, ou Turin) cadencés à 2,6GHz (fréquence de base).
    *   Chaque nœud de calcul CPU a 755GiB / 810GB de mémoire disponible.
    *   Les nœuds ont une connexion InfiniBand NDR non bloquante (1:1) à 400Gb/s.
    *   Cette sous-grappe est conçue pour les tâches massivement parallèles.

2.  Sous-grappe de GPU
    *   252 GPU fournis par 63 nœuds de calcul GPU.
    *   Chaque nœud de calcul GPU est équipé de 4 GPU NVIDIA H100 (SXM) avec 80GB de VRAM dédiée.
    *   Chaque nœud de calcul GPU a 96 cœurs provenant d'un processeur AMD EPYC 9654 à 96 cœurs (Zen 4, ou Genoa) cadencé à 2,4GHz (fréquence de base).
    *   Les nœuds ont une connexion InfiniBand NDR non bloquante (1:1) de 800Gb/s, soit 200Gb/s par GPU.
    *   Dispose d'un nœud de connexion dédié (trig-login01) avec 4 GPU NVIDIA H100 (SXM).
    *   Cette sous-grappe est optimisée pour l'IA, l'apprentissage machine et les charges de travail scientifiques accélérées.

3.  Système de stockage
    *   Stockage NVMe VAST unifié de 29PB pour toutes les charges de travail
    *   Utilise uniquement de la mémoire flash pour des performances constantes
    *   Accessible en tant que système de fichiers parallèle partagé standard

## Avant de commencer

Vous devez posséder un compte [CCDB](https://ccdb.alliancecan.ca) actif auprès de l'Alliance de recherche numérique du Canada. Vous pourrez ensuite demander l'accès à Trillium en sélectionnant ''Ressources-->Accès aux systèmes-->onglet HPC''. Cliquez sur ''Trillium'' et sur ''Je demande l'accès''. Il faut environ une heure pour que votre compte soit créé et que vous puissiez utiliser Trillium.

Prenez bien connaissance de la présente page. La page [Foire aux questions](frequently-asked-questions.md) est aussi une ressource utile. Si vous avez besoin d'aide ou si vous avez des questions, n'hésitez pas à nous écrire à [trillium@tech.alliancecan.ca](mailto:trillium@tech.alliancecan.ca).

## Se connecter

Il y a deux moyens de se connecter à Trillium :

*   Via un navigateur avec Open OnDemand. Cette méthode est recommandée si vous ne connaissez pas bien Linux ou la ligne de commande. Voir [Trillium : Guide de démarrage Open OnDemand](trillium-open-ondemand-quickstart.md).
*   Via un terminal avec ssh, comme décrit ci-dessous.

Comme pour tous les systèmes de SciNet et de l'Alliance, l'accès s'effectue via [SSH](ssh.md). De plus, pour Trillium en particulier, l'authentification est uniquement autorisée via des clés SSH téléversées dans [CCDB](https://ccdb.alliancecan.ca). Pour savoir comment générer votre paire de clés SSH, téléverser et utiliser vos clés SSH, voir [Clés SSH](ssh-keys.md).

Trillium utilise Rocky Linux 9.6, un système d'exploitation de type Linux. Vous devez connaître l'interpréteur Linux pour travailler sur Trillium. Si ce n'est pas le cas, nous vous conseillons de lire [Introduction à Linux](linux-introduction.md), de vous inscrire à une [formation sur l'interpréteur Linux](https://explora.alliancecan.ca/events?include_expired=true&keywords=Shell) ou de suivre un [tutoriel de formation autonome](self-paced-courses.md).

Vous pouvez utiliser [SSH](ssh.md) en ouvrant une fenêtre de terminal (par exemple, en vous [connectant avec PuTTY](connecting-with-putty.md) sous Windows, ou avec [MobaXTerm](connecting-with-mobaxterm.md)), puis en vous connectant via SSH aux nœuds de connexion Trillium avec vos identifiants CCDB.

*   Pour vous connecter à l'un des nœuds de connexion de la sous-grappe de CPU, utilisez la commande
    ```bash
    $ ssh -i /PATH/TO/SSH_PRIVATE_KEY MYALLIANCEUSERNAME@trillium.scinet.utoronto.ca
    ```

*   Pour vous connecter à l'un des nœuds de connexion de la sous-grappe de GPU, utilisez la commande
    ```bash
    $ ssh -i /PATH/TO/SSH_PRIVATE_KEY MYALLIANCEUSERNAME@trillium-gpu.scinet.utoronto.ca
    ```

où `/PATH/TO/SSH_PRIVATE_KEY` est le chemin de votre clé SSH privée et `MYALLIANCEUSERNAME` est votre nom d'utilisateur CCDB.

!!! info "Remarques"

*   À votre première connexion, assurez-vous que vous êtes bien sur Trillium en vérifiant si [l'empreinte de la clé hôte du nœud de connexion](ssh-security-improvements.md#trillium) correspond.
*   Les nœuds de connexion de Trillium vous permettent de développer, de modifier, de compiler, de préparer et de soumettre des tâches.
*   Les nœuds de connexion CPU et GPU ne font pas partie des nœuds de calcul, mais ils ont la même architecture, le même système d'exploitation et la même pile logicielle que les nœuds de calcul CPU et GPU.
*   Vous pouvez vous connecter via SSH d'un nœud de connexion à un autre en utilisant leurs noms d'hôte internes `tri-login01, ..., tri-login06` et `trig-login01` (ce dernier étant le nœud de connexion GPU).
*   L'option `-Y` active la redirection X11, ce qui permet aux programmes graphiques sur Trillium d'ouvrir des fenêtres sur votre ordinateur local.
*   Pour exécuter des tâches sur les nœuds de calcul, vous devez soumettre une tâche en lot.

!!! warning "Sur les nœuds de connexion, vous ne pouvez pas"

*   exécuter des tâches à forte consommation de mémoire;
*   exécuter des entraînements parallèles ou des processus hautement multifils;
*   exécuter des calculs de longue durée (ne dépassez pas quelques minutes);
*   exécuter des tâches intensives, comme des opérations avec plusieurs I/O ou des simulations.

Si vous ne parvenez pas à vous connecter,

*   vérifiez d'abord [l'état du système](https://status.alliancecan.ca),
*   assurez-vous que votre compte [CCDB](https://ccdb.alliancecan.ca) est actif,
*   assurez-vous que votre clé publique a été téléversée (au format openssh) dans CCDB
*   vérifiez que vous avez demandé l'accès sur la page [Accès aux systèmes](https://ccdb.alliancecan.ca/me/access_systems).

## Stockage

Trillium dispose d'un système de stockage unifié de haute performance basé sur la plateforme VAST, avec les répertoires suivants :

*   `/home` – pour les configurations et fichiers personnels
*   `/scratch` – espace de stockage personnel temporaire haute vitesse pour les données des tâches
*   `/project` – espace partagé pour les projets d'équipe et la collaboration

Pour plus de commodité, l'emplacement du niveau supérieur de vos répertoires /home et /scratch est disponible dans les variables d'environnement `$HOME` et `$SCRATCH`, tandis que la variable `$PROJECT` pointe vers votre répertoire dans /project.

Dans le cas où vous participez à plusieurs projets, `$PROJECT` pointe vers votre dernier projet dans l'ordre alphabétique (souvent celui associé à une allocation). Vous trouverez cependant tous les répertoires de niveau supérieur des projets auxquels vous avez accès dans `$HOME/links/projects`, à côté d'un lien `$HOME/links/scratch` pointant vers `$SCRATCH`. Si vous ne voyez pas le répertoire `$HOME/links` dans votre compte, vous pouvez le créer avec la commande
```bash
$ trisetup
```
Le contenu de `$HOME/links/projects` sera automatiquement mis à jour lorsque vous quitterez ou joindrez des projets.

Sur [HPSS](using-nearline-storage.md) (le système /nearline qui sera attaché à Trillium), une variable d'environnement appelée `$ARCHIVE` pointera vers l'emplacement de votre répertoire de niveau supérieur, le cas échéant.

Le tableau ci-dessous indique l'espace disponible et les politiques pour chaque emplacement.

| emplacement | quota                                                               | délai d'expiration | sauvegarde   | sur les nœuds de connexion | sur les nœuds de calcul |
| :---------- | :------------------------------------------------------------------ | :----------------- | :----------- | :----------------------- | :-------------------- |
| $HOME       | 100GB par utilisateur                                               | aucun              | oui          | oui                      | lecture seule         |
| $SCRATCH    | 25TB par utilisateur<sup>*</sup>                                    | à déterminer<sup>*</sup> | non          | oui                      | oui                   |
| $PROJECT    | déterminé par l'allocation via le concours<br>1 To pour groupe par défaut<sup>(2)</sup> | aucun              | oui          | oui                      | lecture seule         |
| $ARCHIVE    | déterminé par l'allocation via le concours<sup>(2)</sup>            | aucun              | double copie | non                      | non                   |

<sup>(1)</sup>Les politiques pour SCRATCH ne sont pas définitives.
<sup>(2)</sup>Le concours pour l'allocation de ressources ne permet pas d'augmenter les quotas pour project ($PROJECT) et nearline ($ARCHIVE) sur Trillium.

## Logiciels

Trillium utilise des [modules d'environnement](utiliser-des-modules.md) pour gérer les compilateurs, les bibliothèques et autres progiciels. Les modules modifient dynamiquement votre environnement (par exemple, `PATH`, `LD_LIBRARY_PATH`) afin que vous puissiez accéder sans problème à différentes versions des logiciels.

Commandes fréquemment utilisées :

*   `module load <module-name>`, charge la version par défaut d'un paquet logiciel
*   `module load <nom-module>/<version-module>`, charge une version spécifique
*   `module purge`, retire tous les modules actuellement chargés
*   `module avail`, liste les modules disponibles pouvant être chargés
*   `module list`, affiche les modules actuellement chargés
*   `module spider` ou `module spider <nom-module>`, recherche des modules et leurs versions

Abréviations utiles :

*   `ml`, équivaut à `module list`
*   `ml <module-name>`, équivaut à `module load <module-name>`

Au moment où vous vous connectez, seuls les modules `CCconfig`, `gentoo/2023` et `mii` sont chargés, offrant les fonctionnalités de base du système d'exploitation. Pour obtenir un ensemble standard de compilateurs et de bibliothèques, comme sur nos autres grappes de calcul, chargez `StdEnv/2023`.

## Conseils pour le chargement de logiciels

Une bonne gestion de votre environnement logiciel est essentielle pour éviter les conflits et garantir la reproductibilité. Voici quelques bonnes pratiques :

*   Évitez de charger des modules dans votre fichier `.bashrc`, car cela peut entraîner des comportements inattendus, notamment dans les environnements non interactifs comme les tâches en lot ou les interpréteurs distants.

*   Chargez plutôt les modules manuellement, à partir d'un script distinct ou à l'aide de collections de modules. Cette approche offre un meilleur contrôle et contribue à préserver la propreté des environnements.

*   Chargez les modules requis dans votre script de tâche, ce qui garantit que votre tâche s'exécute dans l'environnement logiciel attendu, quels que soient les paramètres de votre interpréteur interactif.

*   Soyez explicite quant aux versions des modules. Des noms courts comme `gcc` chargeront le module par défaut (par exemple `gcc/12.3`) qui pourrait éventuellement changer. Spécifiez les versions complètes (par exemple `gcc/13.3`) pour une reproductibilité à long terme.

*   Résolvez les dépendances avec `module spider`. Certains modules dépendent d'autres modules. Utilisez `module spider <module-name>` pour savoir lesquels sont requis et comment les charger dans le bon ordre. Pour en savoir plus, voir [Sous-commande spider](utiliser-des-modules.md#sous-commande-spider).

## Applications commerciales

Certains aspects sont à considérer si vous voulez utiliser des logiciels commerciaux sur Trillium.

*   Vous pouvez utiliser des logiciels commerciaux sur Trillium si vous possédez une licence valide. Si le logiciel nécessite un serveur de licences, vous pouvez vous y connecter en toute sécurité via [un tunnel SSH](ssh-tunnelling.md).

*   Nous ne fournissons pas de licence spécifique à chaque utilisateur. En raison du nombre et de la diversité de nos utilisateurs, nous ne pouvons pas offrir des licences pour des paquets individuels ou spécialisés.

*   Certains outils du commerce très utiles sont disponibles, tels que des compilateurs (Intel), bibliothèques mathématiques (MKL) et débogueurs (DDT).

*   Nous pouvons vous aider. Si vous possédez une licence valide et avez besoin d'aide pour installer un logiciel, n'hésitez pas à nous contacter.

## Tests et débogage

Avant de soumettre votre tâche, il est important de tester votre code pour vous assurer de son exactitude et des ressources nécessaires.

*   **Les tests légers** peuvent être exécutés directement sur les nœuds de connexion. En règle générale, ils doivent :
    *   s'exécuter en quelques minutes
    *   utiliser au plus 1 à 2GB de mémoire
    *   utiliser entre 1 et 4 CPU
    *   utiliser au plus 1 GPU

*   Vous pouvez également exécuter le débogueur parallèle [ARM DDT](arm-software.md) sur les nœuds de connexion après l'avoir chargé avec `module load ddt-cpu` ou `module load ddt-gpu`.

*   Pour les tests dépassant les limites du nœud de connexion ou nécessitant des ressources dédiées, demandez une tâche de débogage interactive à l'aide de la commande `debugjob` sur un nœud de connexion.
    ```bash
    $ debugjob
    ```
    Exécutée depuis un nœud de connexion CPU, cette commande vous permet d'utiliser un interpréteur interactif dans une session de calcul CPU pendant une heure. La commande `debugjob` exécutée depuis un nœud de connexion GPU ouvre une session interactive avec un GPU sur un nœud de calcul GPU (partagé) pendant deux heures. Le tableau suivant montre quelques variantes de cette commande permettant de demander davantage de ressources pour une session interactive. Notez que plus vous demandez de ressources, plus le temps d'exécution alloué est court, ce qui permet de garantir que la session interactive démarre presque toujours immédiatement.

| Commande                               | Sous-grappe | Nombre de cœurs | Nombre de cœurs CPU | Nombre de GPU | Mémoire  | Temps d'exécution maximum |
| :------------------------------------- | :---------- | :-------------- | :------------------ | :------------ | :------- | :------------------------ |
| debugjob                               | CPU         | 1               | 192                 | 0             | 755GiB   | 60 minutes                |
| debugjob 2                             | CPU         | 2               | 384                 | 0             | 2x755GiB | 30 minutes                |
| debugjob<br>debugjob -g 1              | GPU         | 1/4             | 24                  | 1             | 188GiB   | 120 minutes               |
| debugjob 1<br>debugjob -g 4            | GPU         | 1               | 96                  | 4             | 755GiB   | 30 minutes                |
| debugjob 2<br>debugjob -g 8            | GPU         | 2               | 192                 | 8             | 2x755GiB | 15 minutes                |

L'environnement de l'interpréteur pour une tâche de débogage est similaire à celui que vous obtenez lorsque vous venez de vous connecter : seuls les modules standards sont chargés, aucun accès Internet, aucun accès en écriture aux systèmes de fichiers /home et /projet, et aucune soumission de tâche. Sachez que si vous souhaitez que la session hérite des modules chargés avant d'exécuter la commande de débogage, vous pouvez ajouter `--export=ALL` comme première option à debugjob.

*   Si votre tâche de test nécessite plus de temps que ce qui est autorisé par debugjob, vous pouvez demander une session interactive depuis la file d'attente standard avec `salloc`. Pour les tâches de test CPU, la commande serait
    ```bash
    $ salloc --export=NONE --nodes=N --time=M:00:00 [--ngpus-per-node=G] [--x11]
    ```
    où
    *   `N` est le nombre de nœuds
    *   `M` est le nombre d'heures d'exécution de la tâche
    *   `G` est le nombre de GPU par nœud (le cas échéant)
    *   `--x11` est requis uniquement pour les applications graphiques (par exemple [ARM DDT](arm-software.md)).

!!! info "Remarque"

Les tâches soumises avec `salloc` peuvent prendre plus de temps à démarrer qu'avec debugjob et sont comptabilisées dans votre allocation.

## Soumettez des tâches à l'ordonnanceur

Une fois que votre code ou votre flux de travail est compilé et testé sur les nœuds de connexion de Trillium et que son bon fonctionnement est confirmé, vous pouvez soumettre des tâches sur la grappe. Ces tâches s'exécuteront sur les nœuds de calcul de Trillium et leur exécution sera gérée par l'ordonnanceur.

Trillium utilise SLURM comme ordonnanceur de tâches. Pour plus d'information sur l'interaction avec l'ordonnanceur, voyez [la page Slurm](running-jobs.md).

Pour soumettre une tâche, utilisez la commande `sbatch` sur un nœud de connexion.
```bash
$ sbatch jobscript.sh
```
Les tâches avec CPU doivent être soumises depuis les nœuds de connexion CPU, tandis que les tâches avec GPU doivent être soumises depuis le nœud de connexion GPU. Dans les deux cas, la commande est identique, mais les options du script sont différentes (voir ci-dessous).

La commande `sbatch` place votre tâche dans la file d'attente. Le script doit contenir des lignes commençant par `#SBATCH` spécifiant les ressources nécessaires (les options les plus courantes sont présentées ci-dessous). L'ordonnanceur exécutera ce script sur les nœuds de calcul lorsque votre tâche aura passé au début de la file d'attente et que les ressources seront disponibles.

La priorité d'une tâche dans la file d'attente dépend des ressources demandées, du temps déjà passé dans la file d'attente, de l'utilisation récente, ainsi que du compte SLURM avec lequel la tâche a été soumise. Les comptes SLURM correspondent aux [RAP (Resource Allocation Project)](frequently-asked-questions-about-the-ccdb.md#rap-resource-allocation-project) :
*   Chaque chercheuse principale ou chercheur principal dispose d'au moins un RAP, le RAP par défaut du service d'accès rapide. Les membres parrainés ont accès au compte SLURM correspondant dont le nom commence par `def-`.
*   Une chercheuse principale ou un chercheur principal disposant d'une allocation via concours dispose d'un RAP supplémentaire, auquel des utilisateurs peuvent être ajoutés. Le nom des comptes SLURM correspondants commence généralement par `rrg-` ou `rpp-`. Notez que les RAC sont liés à un système; par exemple, un RAC pour Nibi ne peut pas être utilisé sur Trillium.

## Restrictions particulières à Trillium

Trillium étant conçue pour les tâches massivement parallèles, elle présente certaines différences par rapport aux grappes à usage général ([Fir](fir.md), [Nibi](nibi.md), [Narval](narval.md), [Rorqual](rorqual.md)), que nous allons maintenant aborder.

### Les données de sortie doivent être écrites dans /scratch

`/scratch` est un système de fichiers parallèle rapide que vous devriez utiliser pour écrire les données pendant l'exécution des tâches. Ceci est nécessaire parce que /home et /project sont en lecture seulement sur les nœuds de calcul.

En plus de vous assurer que votre application écrit dans le répertoire /scratch, vous devez généralement soumettre vos tâches depuis votre répertoire `$SCRATCH` (et non $HOME ou $PROJECT). L'emplacement par défaut des fichiers de sortie de l'ordonnanceur se trouve dans le répertoire à partir duquel vous soumettez vos tâches. Par conséquent, si ce répertoire n'est pas dans /scratch, les fichiers de sortie ne seront pas écrits.

### Compte par défaut pour l'ordonnanceur

Les tâches s'exécuteront avec l'allocation attribuée à votre groupe ou, à défaut, avec une allocation du service d'accès rapide. Vous pouvez contrôler ceci explicitement en spécifiant le compte avec l'option `--account=ACCOUNT_NAME` dans votre script de tâche ou votre commande de soumission. Si vous disposez de plusieurs allocations, il est fortement recommandé de spécifier le nom du compte.

### Tâche soumise par une autre tâche

Les tâches ne peuvent pas être soumises depuis les nœuds de calcul (ni depuis les nœuds de copie). Ceci évite de générer accidentellement de nombreuses tâches et de surcharger l'ordonnanceur et le processus de sauvegarde.

### Ordonnancement pour nœud entier ou GPU entier

Il n'est pas possible de demander un nombre particulier de cœurs sur Trillium. Sur la sous-grappe de CPU, toutes les tâches doivent utiliser des nœuds entiers. Ceci signifie que la taille minimale d'une tâche CPU est de 192 cœurs, que vous devez utiliser efficacement. Si vous exécutez des tâches séquentielles ou à faible nombre de cœurs, vous devez tout de même utiliser les 192 cœurs du nœud en regroupant plusieurs tâches indépendantes dans un seul script. Pour des exemples, consultez [GNU Parallel](gnu-parallel.md) et [cette section de la page META-Farm (fonctions avancées)](meta-farm-advanced-features-and-troubleshooting.md#mode-whole-node).

Si votre tâche sous-utilise les cœurs, notre équipe peut vous aider à optimiser votre flux de travail, ou vous pouvez [nous contacter](mailto:trillium@tech.alliancecan.ca) pour obtenir de l'aide.

Sur la sous-grappe de GPU, chaque nœud contient 4 GPU. L'ordonnanceur vous permet de demander soit un nombre entier de nœuds, soit un seul GPU. Ce dernier équivaut à un quart de nœud, avec 24 cœurs et environ 188 GiB de RAM. Il est important d'utiliser le GPU efficacement. Trillium ne prend pas en charge MIG comme sur les autres grappes (MIG permet de planifier une fraction de GPU), mais vous pouvez utiliser [HyperQ / MPS](hyper-q-mps.md) dans vos tâches.

### Quantité de mémoire allouée

N'indiquez pas la quantité de mémoire requise. Les tâches CPU reçoivent toujours `N × 768GB` de RAM, où `N` est le nombre de nœuds et 768GB est la quantité de mémoire pour chaque nœud. Les tâches sur un nœud GPU entier obtiennent la même quantité de mémoire alors que celles sur un GPU unique obtiennent 1/4 de la mémoire, soit 188GiB.

## Options fréquemment utilisées dans les scripts de tâches

Les options suivantes sont fréquemment utilisées :

| option                  | short option | résultat                                                      | remarques                                                              |
| :---------------------- | :----------- | :------------------------------------------------------------ | :--------------------------------------------------------------------- |
| `--nodes`               | `-N`         | nombre de nœuds                                               | il est recommandé de toujours inclure cette option                     |
| `--ntasks-per-node`     |              | nombre de tâches à lancer par srun/mpirun, par nœud           | préférez cette option à `--ntasks`                                     |
| `--ntasks`              | `-n`         | nombre de tâches à lancer par srun/mpirun                     |                                                                        |
| `--cpus-per-task`       | `-c`         | nombre de cœurs par tâche                                     | habituellement pour les fils (OpenMP)                                  |
| `--time`                | `-t`         | durée de la tâche                                             |                                                                        |
| `--job-name`            | `-J`         | nom de la tâche                                               |                                                                        |
| `--output`              | `-o`         | fichier de sortie                                             | peut être répété (par exemple avec %j pour l'identifiant de la tâche) |
| `--mail-type`           |              | quand envoyer un courriel (par exemple BEGIN, END, FAIL, ALL) |                                                                        |
| `--gpus-per-node`       |              | nombre de GPU à utiliser sur chaque nœud                      | les valeurs pour la sous-grappe de GPU sont 1 et 4                     |
| `--partition`           | `-p`         | partition à laquelle soumettre la tâche                       | (voir les partitions disponibles ci-dessous)                           |
| `--account`             | `-A`         | compte slurm à utiliser                                       | dans plusieurs cas, ceci est automatique sur Trillium                  |
| `--mem`                 |              | quantité de mémoire                                           | ne s'applique pas (vous obtenez toute la mémoire)                      |

Ces options doivent être dans des lignes de commentaire distinctes en haut du script de tâche (mais après `#!/bin/bash`), préfixées par `#SBATCH`. Elles peuvent également être utilisées comme options de ligne de commande pour salloc. Vous trouverez ci-dessous quelques exemples de scripts de tâches.

Pour plus d'information, voyez [Exécuter des tâches](running-jobs.md) et [la documentation sur SLURM](https://slurm.schedmd.com/sbatch.html).

## Soumettre des tâches sur la sous-grappe de CPU

### Partitions et limites

La taille et la durée de vos tâches, leur nombre d'exécutions et leur nombre de mises en file d'attente sont limités. L'appartenance ou non d'un utilisateur à un groupe disposant d'une allocation via concours (pour un groupe de recherche ou pour une plateforme ou un portail) est importante. La partition d'exécution de la tâche est également importante. Dans le langage de l'ordonnanceur Slurm, le terme ''partition'' est utilisé pour décrire les cas d'utilisation. Vous spécifiez la partition avec le paramètre `-p` de `sbatch` ou `salloc`, mais si vous n'en spécifiez pas, votre tâche s'exécutera dans la partition `compute`, ce qui est le cas le plus courant.

| Utilisation       | Partition | Limite pour les tâches en cours | Limite pour les tâches soumises et en cours | Plus petite taille des tâches | Plus grande taille des tâches                                                                                     | Plus court temps d'exécution | Plus long temps d'exécution |
| :---------------- | :-------- | :---------------------------- | :------------------------------------------ | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- | :--------------------------- | :-------------------------- |
| tâches de calcul  | compute   | 150                           | 500                                         | 1 nœud (192 cœurs)            | par défaut, 10 nœuds (1920 cœurs) <br> avec une allocation, 128 nœuds (24576 cœurs)<sup>\*</sup>                 | 15 minutes                   | 24 heures                   |
| tests ou débogage | debug     | 1                             | 1                                           | 1 nœud (192 cœurs)            | 2 nœuds (384 cœurs)                                                                                               | s.o.                         | 1 heure                     |

<sup>\*</sup> Maximum recommandé; si vous avez des tâches plus exigeantes, contactez-nous.

Même si vous respectez ces limites, vos tâches devront passer par la file d'attente. Le temps d'attente dépend de nombreux facteurs, tels que la taille de l'allocation pour votre groupe, la quantité de ressources utilisées récemment, le nombre de nœuds et le temps d’exécution demandés, ainsi que le nombre total de tâches en attente.

### Exemple d'une tâche MPI

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192
#SBATCH --time=01:00:00
#SBATCH --job-name=mpi_job
#SBATCH --output=mpi_output_%j.txt
#SBATCH --mail-type=FAIL

cd $SLURM_SUBMIT_DIR

module load StdEnv/2023
module load gcc/12.3
module load openmpi/4.1.5

source /scinet/vast/etc/vastpreload-openmpi.bash # important if doing MPI-IO

mpirun ./mpi_example
```

Depuis un nœud de connexion, à partir de votre répertoire `$SCRATCH`, soumettez ce script avec la commande
```bash
$ sbatch mpi_job.sh
```

*   La première ligne indique qu'il s'agit d'un script bash.
*   Les lignes commençant par `#SBATCH` sont dirigées vers l'ordonnanceur.
*   `sbatch` lit ces lignes comme étant une requête de tâche qu'elle nomme `mpi_job`.
*   Ici, l'ordonnanceur recherche deux nœuds pour exécuter chacun 192 tâches pendant une heure.
*   Une fois ces nœuds alloués, Slurm exécute le script qui effectue les opérations suivantes :
    *   accéder au répertoire de soumission,
    *   charger les modules,
    *   précharger une bibliothèque optimisant MPI-IO pour le système de fichiers VAST; si vous utilisez IntelMPI au lieu d'OpenMPI, utilisez plutôt `source /scinet/vast/etc/vastpreload-intelmpi.bash`.
    !!! info ""
        **Pour que le préchargement de la bibliothèque VAST fonctionne, il faut utiliser `mpirun` plutôt que `srun`**;
    *   exécuter l'application `mpi_example` (l'ordonnanceur indiquera à `mpirun` ou `srun` le nombre de processus à exécuter).

### Exemple d'une tâche OpenMP

```bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=192
#SBATCH --time=01:00:00
#SBATCH --job-name=openmp_job
#SBATCH --output=openmp_output_%j.txt
#SBATCH --mail-type=FAIL

cd $SLURM_SUBMIT_DIR

module load StdEnv/2023
module load gcc/12.3

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

./openmp_example
# or "srun ./openmp_example"
```

À partir de votre répertoire `$SCRATCH`, soumettez ce script depuis un nœud de connexion CPU avec la commande
```bash
$ sbatch openmp_job.sh
```

*   La première ligne indique qu'il s'agit d'un script bash.
*   Les lignes commençant par `#SBATCH` sont des directives pour l'ordonnanceur.
*   `sbatch` lit ces lignes comme étant une requête de tâche qu'elle nomme `openmp_job`.
*   Ici, l'ordonnanceur recherche un nœud avec 192 CPU pour exécuter une tâche pendant une heure.
*   Une fois le nœud alloué, Slurm exécute le script qui effectue les opérations suivantes :
    *   changer le répertoire de soumission,
    *   charger les modules,
    *   configurer `OMP_NUM_THREADS` pour le nombre de CPU demandés,
    *   exécuter l'application `openmp_example`.

### Exemple d'une tâche hybride MPI/OpenMP

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00
#SBATCH --job-name=hybrid_job
#SBATCH --output=hybrid_output_%j.txt
#SBATCH --mail-type=FAIL

cd $SLURM_SUBMIT_DIR

module load StdEnv/2023
module load gcc/12.3
module load openmpi/4.1.5

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=true

export CORES_PER_L3CACHE=8
export RANKS_PER_L3CACHE=$(( $CORES_PER_L3CACHE / $OMP_NUM_THREADS ))  # this works up to 8 threads

source /scinet/vast/etc/vastpreload-openmpi.bash # important if doing MPI-IO

mpirun --bind-to core --map-by ppr:$RANKS_PER_L3CACHE:l3cache:pe=$OMP_NUM_THREADS ./hybrid_example
```

Depuis un nœud de connexion À partir de votre répertoire `$SCRATCH`, soumettez ce script avec la commande
```bash
$ sbatch hybrid_job.sh
```

*   La première ligne indique qu'il s'agit d'un script bash.
*   Les lignes commençant par `#SBATCH` sont des directives pour l'ordonnanceur.
*   `sbatch` lit ces lignes comme étant une requête de tâche qu'elle nomme `hybrid_job`.
*   Ici, l'ordonnanceur recherche deux nœuds pour exécuter chacun 48 tâches avec chacune 4 fils pendant une heure.
*   Une fois les nœuds alloués, Slurm exécute le script qui effectue les opérations suivantes :
    *   changer le répertoire de soumission,
    *   charger les modules,
    *   précharger une bibliothèque optimisant MPI-IO pour le système de fichiers VAST; si vous utilisez IntelMPI au lieu d'OpenMPI, utilisez plutôt `source /scinet/vast/etc/vastpreload-intelmpi.bash`.
    !!! info ""
        **Pour que le préchargement de la bibliothèque VAST fonctionne, il faut utiliser `mpirun` plutôt que `srun`**;
    *   exécuter l'application `hybrid_example`; même si l'ordonnanceur indique à `mpirun` combien de processus il faut exécuter, il faut quand même distribuer également les processus et les fils sur l'ensemble des cœurs, ce qui est fait par l’option --map-by. Si vous utilisez plus de 8 fils par processus (tâche ou rang MPI) mais au plus 24, changez ''l3cache'' pour ''numa''. Si vous utilisez plus de 24 fils par processus, changez pour ''socket''.

## Soumettre des tâches sur la sous-grappe de GPU

### Partitions et limites

Tout comme pour la sous-grappe de CPU, la taille et la durée des tâches, le nombre de tâches exécutables et le nombre de tâches mises en file d'attente sont limités, ainsi que l'appartenance ou non d'un utilisateur à un groupe disposant d'une allocation via concours. La sous-grappe de GPU comporte plus de partitions que la sous-grappe de CPU pour pouvoir prendre en charge la planification par GPU plutôt que par nœud (chaque nœud dispose de 4 GPU).

Sur Trillium, vous ne pouvez demander qu'un seul GPU ou un multiple de quatre GPU. Vous ne pouvez pas demander `--gpus-per-node=2` ou `3`, ni utiliser la technologie MIG de NVIDIA pour allouer une fraction d'un GPU. Dans une tâche, vous pouvez utiliser MPS (Multi-Process Service) de NVIDIA pour partager un GPU entre les processus exécutés dans la tâche.

*   Pour une tâche avec un seul GPU, utilisez `--gpus-per-node=1`.
*   Pour une tâche avec un nœud GPU entier, utilisez `--gpus-per-node=4`.

| Utilisation    | Partition | Limite pour les tâches en cours | Limite pour les soumises et les tâches en cours | Plus petite taille des tâches | Plus grande taille des tâches                                                                                     | Plus court temps d'exécution | Plus long temps d'exécution              |
| :------------- | :-------- | :---------------------------- | :---------------------------------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- | :--------------------------- | :--------------------------------------- |
| calcul avec GPU | calcul    | 150                           | 500                                             | 1/4 nœud (24 cœurs / 1GPU)    | par défaut, 5 nœuds (480 cœurs /20 GPU) <br> avec une allocation: 25 nœuds (2400 cœurs /100 GPU)                 | 15 minutes                   | 24 heures                                |
| test avec GPU  | débogage  | 1                             | 1                                               | 1/4 nœud (24 cœurs / 1 GPU)   | 2 nœuds (192 cœurs / 8 GPU)                                                                                       | s.o.                         | 2 heures (1 GPU) - 30 minutes (8 GPU)    |

Même si vous respectez ces limites, vos tâches devront passer par la file d'attente. Le temps d'attente dépend de nombreux facteurs, tels que la taille de ressources pour votre groupe, la quantité de l'allocation utilisée récemment, le nombre de nœuds et le temps d'exécution demandés, ainsi que le nombre total des tâches en attente.

### Exemple d'une tâche avec un seul GPU

```bash
#!/bin/bash
#SBATCH --job-name=single_gpu_job         # Job name
#SBATCH --output=single_gpu_job_%j.out    # Output file (%j = job ID)
#SBATCH --nodes=1                         # Request 1 node
#SBATCH --gpus-per-node=1                 # Request 1 GPU
#SBATCH --time=00:30:00                   # Max runtime (30 minutes)

# Load modules
module load StdEnv/2023
module load cuda/12.6
module load python/3.11.5

# Activate Python environment (if applicable)
source ~/myenv/bin/activate

# Check GPU allocation
srun nvidia-smi

# Run your workload
srun python my_script.py
```

### Exemple : Tâche avec un nœud entier (4 GPU)

```bash
#!/bin/bash
#SBATCH --job-name=whole_node_gpu_job
#SBATCH --output=whole_node_gpu_job_%j.out
#SBATCH --nodes=1
#SBATCH --gpus-per-node=4
#SBATCH --time=02:00:00

module load StdEnv/2023
module load cuda/12.6
module load python/3.11.5

# Activate Python environment (if applicable)
source ~/myenv/bin/activate

srun python my_distributed_script.py
```

### Exemple d'une tâche avec plusieurs nœuds GPU

```bash
#!/bin/bash
#SBATCH --job-name=multi_node_gpu_job
#SBATCH --output=multi_node_gpu_job_%j.out
#SBATCH --nodes=2                        # Request 2 full nodes
#SBATCH --gpus-per-node=4                # 4 GPUs per node (full node)
#SBATCH --time=04:00:00

module load StdEnv/2023
module load cuda/12.6
module load openmpi/4.1.5

# Check all GPUs allocated
srun nvidia-smi

# Activate Python environment (if applicable)
source ~/myenv/bin/activate

# Example: run a distributed training job with 8 GPUs (2 nodes × 4 GPUs)
srun python train_distributed.py
```

### Meilleures pratiques pour les tâches avec GPU

*   N'utilisez pas `--mem`; la mémoire est fixe par GPU (192GB) ou par nœud (768GB).
*   Indiquez toujours le nombre de nœuds et `--gpus-per-node=4` pour les tâches sur un nœud entier ou sur plusieurs nœuds.
*   Chargez uniquement les modules nécessaires ([voir Utiliser des modules](utiliser-des-modules.md)).
*   Pour une meilleure reproductibilité, soyez explicite quant aux versions des logiciels (par exemple, `cuda/12.6` plutôt que simplement `cuda`).
*   Testez sur un seul GPU avant de passer à plusieurs GPU ou nœuds.
*   Surveillez l'utilisation avec `nvidia-smi` pour vous assurer que les GPU sont pleinement utilisés.

## Suivi

### Suivi de la file

Une fois votre tâche soumise à la file d'attente, vous pouvez surveiller son état et ses performances à l'aide des commandes SLURM suivantes :

*   `squeue` montre toutes les tâches dans la file; pour voir uniquement vos propres tâches, utilisez `squeue -u $USER`.
*   `squeue -j JOBID` montre l'état courant d'une tâche en particulier; pour les détails sur une tâche, incluant les nœuds alloués, les ressources et les indicateurs pour la tâche, utilisez `scontrol show job JOBID`.
*   `squeue --start -j JOBID` donne une estimation du moment où une tâche en attente devrait démarrer. Notez que cette estimation est souvent inexacte et peut varier en fonction de la charge du système et des priorités.
*   `scancel JOBID` annule une tâche déjà soumise
*   `jobperf JOBID` produit un instantané en temps réel de l'utilisation du CPU et de la mémoire pendant que la tâche est exécutée.
*   `sacct` affiche des informations sur vos tâches passées, notamment l'heure de début, l'heure d'exécution, l'utilisation du nœud et l'état de sortie.

Pour plus d'information sur le suivi des tâches, voir [la page sur Slurm](running-jobs.md).

### Suivi des tâches en cours et des tâches passées

Une fois que votre tâche est terminée, elle est retirée de la file; ainsi les commandes relatives à la file (par exemple `squeue` et `sacct`) ne trouveront plus la tâche.

Vos tâches passées et leur utilisation des ressources peuvent être consultées via le portail [my.SciNet](https://my.scinet.utoronto.ca). Ce portail enregistre des informations sur toutes les tâches, y compris les données de performance collectées toutes les deux minutes pendant leur exécution.

## Commandes fréquemment utilisées

| Commande                 | Description                                                  |
| :----------------------- | :----------------------------------------------------------- |
| `sbatch <script>`        | soumet un script pour une tâche en lot                       |
| `squeue [-u $USER]`      | montre les tâches dans la file (toutes les tâches ou uniquement les vôtres) |
| `scancel <JOBID>`        | annule une tâche                                             |
| `sacct`                  | montre les données de *comptabilité* des tâches récemment exécutées |
| `module load <module>`   | charge un module logiciel                                    |
| `module list`            | liste les modules chargés                                    |
| `module avail`           | liste les modules disponibles                                |
| `module spider <module>` | recherche les modules et leurs dépendances                   |
| `debugjob [N]`           | demande une courte tâche de débogage (sur N nombre de nœuds) |
| `diskusage_report`       | vérifie les quotas de stockage                               |
| `jobperf <JOBID>`        | fait le suivi d'un CPU et de la mémoire utilisée pour une tâche en cours |
| `nvidia-smi`             | vérifie l'état d'un GPU (sur un nœud GPU)                    |