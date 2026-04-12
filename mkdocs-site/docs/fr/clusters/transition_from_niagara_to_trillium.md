---
title: "Transition from Niagara to Trillium/fr"
slug: "transition_from_niagara_to_trillium"
lang: "fr"

source_wiki_title: "Transition from Niagara to Trillium/fr"
source_hash: "2bd827ae7b203c592fcc43c6fce3f1d6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:04:15.599541+00:00"

tags:
  []

keywords:
  - "environnements virtuels Python"
  - "cœurs"
  - "pile logicielle"
  - "AMD Zen 5"
  - "CPU et GPU"
  - "répertoire /home"
  - "grappe"
  - "groupe propriétaire"
  - "connexion SSH"
  - "nœuds de calcul"
  - "GPU"
  - "partager des fichiers"
  - "Trillium"
  - "systèmes de fichiers"
  - "sous-grappe de CPU"
  - "Niagara"
  - "Migration des données"
  - "recompilation"
  - "Répertoires"
  - "listes de contrôle d'accès (ACL)"

questions:
  - "Comment les utilisateurs peuvent-ils obtenir l'accès à la grappe Trillium et à son système de stockage HPSS ?"
  - "Quelles sont les procédures et commandes requises pour se connecter aux sous-grappes CPU et GPU et configurer son environnement lors de la première connexion ?"
  - "Quelles sont les nouvelles caractéristiques matérielles des nœuds de calcul CPU de Trillium comparativement à l'ancien système Niagara ?"
  - "Quelles sont les caractéristiques techniques des nœuds de calcul GPU sur la grappe Trillium et quelles bibliothèques mathématiques sont désormais recommandées ?"
  - "Comment s'effectue la migration des données depuis Niagara vers Trillium et quelle est la procédure pour copier manuellement les fichiers récents ?"
  - "Quelles sont les différences de structure et de permissions pour les répertoires personnels et de projet sur Trillium par rapport à Niagara ?"
  - "Quelles sont les deux sous-grappes principales qui composent le système Trillium ?"
  - "Comment les caractéristiques techniques (cœurs et mémoire) d'un nœud de calcul de Trillium se comparent-elles à celles du système Niagara ?"
  - "Quel modèle de processeur équipe la sous-grappe CPU et quelle est sa capacité totale en termes de nœuds et de cœurs ?"
  - "Quelle était la configuration des droits de propriété du répertoire /home sur le système agara ?"
  - "À quel groupe appartiennent par défaut les fichiers et répertoires du dossier /home sur Trillium ?"
  - "Quelles sont les méthodes requises sur Trillium pour partager des fichiers de son répertoire /home avec d'autres membres ?"
  - "Quelles sont les différences de permissions et d'accès en lecture/écriture entre les répertoires /scratch, /project et /home sur les nœuds de calcul de Trillium ?"
  - "Quels changements ont été apportés à la pile logicielle sur Trillium et comment les utilisateurs doivent-ils procéder pour charger les modules nécessaires à leurs travaux ?"
  - "Pourquoi les utilisateurs doivent-ils obligatoirement recompiler leurs codes et recréer leurs environnements virtuels Python sur le nouveau système ?"
  - "Quelles sont les différences de permissions et d'accès en lecture/écriture entre les répertoires /scratch, /project et /home sur les nœuds de calcul de Trillium ?"
  - "Quels changements ont été apportés à la pile logicielle sur Trillium et comment les utilisateurs doivent-ils procéder pour charger les modules nécessaires à leurs travaux ?"
  - "Pourquoi les utilisateurs doivent-ils obligatoirement recompiler leurs codes et recréer leurs environnements virtuels Python sur le nouveau système ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Accès à la grappe

### Permission d'accès

Pour utiliser Niagara et Mist, vous deviez faire une demande d'accès sur CCDB. Vous devez aussi faire une demande pour Trillium. La procédure se fait sur la nouvelle page [https://ccdb.alliancecan.ca/me/access_systems](https://ccdb.alliancecan.ca/me/access_systems) où vous pouvez aussi sélectionner des services nationaux.

Si vous avez obtenu l'accès à Niagara/Mist avant le 5 août 2025, vous avez automatiquement accès à Trillium.

Sur Trillium, vous avez accès aux sous-grappes de CPU et de GPU.

Pour avoir accès à HPSS (le système `/nearline` sur Trillium) vous devez en faire la demande sur [https://ccdb.alliancecan.ca/me/access_systems](https://ccdb.alliancecan.ca/me/access_systems). Par contre, si vous aviez accès à Niagara avant le 5 août, vous avez automatiquement accès.
HPSS n'est pas encore intégré à Trillium. Une fois intégrés, les fichiers sur HPSS resteront inchangés, puisque c'est le même système de stockage.

### Se connecter

#### Accès par un terminal
Pour vous connecter à la sous-grappe de CPU via SSH, utilisez :

```bash
$ ssh USERNAME@trillium.alliancecan.ca
```
À votre première connexion, assurez-vous que vous êtes bien sur Trillium en vérifiant si [l'empreinte de la clé hôte du nœud de connexion](ssh-security-improvements/fr.md#trillium) correspond. Comme c'était le cas avec Niagara et Mist, vous devez avoir activé l'authentification multifacteur et utiliser une [clé SSH](ssh-keys/fr.md) enregistrée pour votre compte. Vous aurez ainsi accès à l'un des six nœuds de connexion CPU nommés tri-login01-6. Ces nœuds n'ont pas de GPU **et peuvent traiter uniquement des tâches sur des nœuds de CPU**.

Pour vous connecter à la sous-grappe de GPU `trillium-gpu.alliancecan.ca`, utilisez la commande ci-dessous. L'authentification multifacteur et une clé SSH enregistrée sont aussi requises.

```bash
$ ssh USERNAME@trillium-gpu.alliancecan.ca
```
Ceci établit la connexion au nœud GPU trig-login01 qui offre 4 GPU NVIDIA H100. De là, vous pouvez **uniquement soumettre des tâches aux nœuds de calcul de la sous-grappe GPU.**

#### Première connexion

À votre première connexion à Trillium, vous verrez vos fichiers qui se trouvaient sur Niagara.

!!! tip "Initialisation de l'environnement"
    Vos fichiers d'initialisation ne fonctionneront probablement pas comme ils le devraient, alors **nous vous recommandons fortement** de lancer :
    ```bash
    $ trisetup
    ```
    Cette commande placera dans votre répertoire `/home` les fichiers `.bashrc`, `.bash_profile`, `.chsrc`, et `.Xauthority`. La commande créera les répertoires `.licenses`, `.local`, `.ssh`, et `links`. Ce dernier répertoire contient des liens symboliques vers vos répertoires `/home` et `/project`. Les versions originales de ces fichiers seront sauvegardées sous un nouveau nom avec un horodatage.

Vous pouvez maintenant recompiler votre code, réinstaller des environnements virtuels, etc.

#### Accès par le web

Pour le moment, le [site web SciNet OnDemand](https://ondemand.scinet.utoronto.ca) reste connecté à Niagara. Il est prévu que le site offre un moyen de se connecter à Trillium pour utiliser des applications web comme Jupyper, avec accès au système de fichiers Trillium.

## Nouvelle configuration matérielle

Trillium offre deux sous-grappes homogènes, soit la sous-grappe de CPU et la sous-grappe de GPU.

### CPU
Chacun des nœuds de calcul possède 192 cœurs (contrairement aux 40 de Niagara) et 755 Go de mémoire (188 Go sur Niagara). Les CPU sont des AMD Zen 5, aussi connus sous le nom de Turin (CPU Intel Skylake et Cascaselake sur Niagara). La sous-grappe possède 1224 nœuds de calcul et un total de 235 008 cœurs.

Si vous compiliez du code avec Intel MKL pour les routines mathématiques et d'algèbre linéaire, nous vous suggérons de passer à [Flexiblas](blas-and-lapack/fr.md) ou d'utiliser directement les bibliothèques AOCL de AMD; celles-ci sont disponibles dans les modules `aocl-blas` et `aocl-lapack`.

### GPU
Chaque nœud de calcul de la sous-grappe de GPU dispose de 4 GPU, 96 cœurs et de 755 Go de mémoire disponible. Les processeurs sont des AMD Zen 4 (aussi appelés Genoa), tandis que les GPU sont des NVIDIA H100 (les GPU de Mist étaient des V100). Il y a 61 nœuds de calcul GPU et un total de 244 GPU.

!!! note
    Il est important de vous assurer que vos tâches ne gaspillent pas de ressources. Elles doivent soit utiliser tous les cœurs, soit utiliser la majeure partie de la mémoire, soit exploiter efficacement les GPU.

## Stockage

### Migration automatique des données

Toutes les données présentes dans vos répertoires `/home`, `/scratch` et `/project` sur Niagara au 31 juillet 2025 et qui n'ont pas été modifiés par la suite ont été copiées dans le répertoire correspondant sur Trillium. Il est possible que vous deviez copier les données ajoutées ou modifiées ultérieurement sur Niagara. Par exemple pour vous connecter via SSH au nœud de copie `nia-datamover1`.

```bash
$ ssh USERNAME@nia-datamover1.scinet.utoronto.ca
```

Profitez du fait que les systèmes de fichiers de Niagara et Trillium sont montés ici pour faire des copies localement, d'une grappe à l'autre.

```bash
USERNAME@nia-dm1:~$ cp /home/G/GROUP/USERNAME/file.txt /trillium_home/USERNAME/file.txt
```

En date du 4 novembre, les quotas pour `/home` et `/scratch` restent les mêmes valeurs par défaut que celles de Niagara, soit 100 Go et 25 To, respectivement.

### Emplacement des répertoires

Les structures de `/home`, `/scratch` et `/project` sont différentes de celles sur Niagara. Les répertoires `/home` et `/scratch` ne sont pas imbriqués dans un groupe, mais se trouvent dans **`/home/USERNAME`** et **`/scratch/USERNAME`**.

Le quota sur `/scratch` et la configuration des purges seront mis à jour dans les prochains mois.

Si votre groupe avait un répertoire `/project` sur Niagara, vous le trouverez dans **`/project/RRG-NAME`**, où RRG-NAME est le nom de votre allocation de projet de recherche. De plus, chaque groupe aura un répertoire `/project` **`/project/def-PINAME`** où PINAME est le nom de la chercheuse ou du chercheur principal, avec un quota de 1 To.

Comme sur Niagara, `/home` et `/project` seront sauvegardés, mais `/scratch` ne le sera pas.

Pour trouver plus facilement ces emplacements, vous pouvez créer un répertoire appelé `liens` dans votre répertoire `/home` pour y conserver des liens vers vos répertoires `/scratch` et `/project`. Pour créer ces liens, exécutez la commande :

```bash
$ trisetup
```
Cela mettra également à jour votre fichier `.bashrc` et les autres fichiers de démarrage; la commande affichera exactement ce qu'elle a fait et où elle a enregistré les versions antérieures.

Une fois configurés, les liens dans `` `$HOME/links/project` `` seront automatiquement modifiés si vous vous joignez à un groupe ou vous en quittez un.

### Permissions pour les fichiers et répertoires

Sur Niagara, vous étiez propriétaire de votre répertoire `/home`, mais le groupe propriétaire était celui de votre chercheur ou chercheuse principale. Sur Trillium, vos fichiers et répertoires dans `/home` appartiennent à votre propre groupe privé. Par conséquent, pour partager des fichiers dans `/home` avec d'autres membres d’un groupe, vous devrez définir les autorisations à l'aide des listes de contrôle d'accès (ACL) ou changer le groupe propriétaire des fichiers.

De même pour `/scratch`, les nouveaux utilisateurs verront leur répertoire `/scratch` comme étant privé, c'est-à-dire que son groupe propriétaire est leur groupe privé. Pour partager des fichiers avec quelqu'un d'autre, vous devrez utiliser les listes de contrôle d'accès (ACL) ou modifier la propriété des groupes. Il est toutefois à noter que les utilisateurs dont les fichiers ont été transférés de Niagara verront ceux dont le groupe de propriété est celui du groupe de recherche sous lequel leur répertoire `/scratch` était initialement imbriqué.

Le répertoire `/project` est configuré pour être partagé et les membres du groupe correspondent à ceux définis dans l'allocation par défaut ou l'allocation pour un projet du groupe de recherche.

!!! note
    Les systèmes de fichiers `/home` et `/project` sont en lecture seule sur les nœuds de calcul de Trillium. Vos tâches doivent donc écrire dans le répertoire `/scratch`. La copie de données de `/scratch` vers `/project` ou `/home` doit être limitée aux données qui doivent absolument être conservées et sauvegardées. Pour cela, vous pouvez utiliser les commandes `scp` ou `rsync` à la fin de votre tâche pour copier les fichiers vers le nœud de copie ou un nœud de connexion, ou vous connecter au nœud de copie pour y effectuer le transfert.

## Logiciels

### Pile logicielle
La pile logicielle NiaEnv sur Niagara sera éliminée et ne sera pas disponible sur Trillium. La pile logicielle MistEnv sur Mist ne sera pas disponible sur Trillium-gpu. La pile CVMFS sera disponible sur Trillium comme sur toutes les autres grappes nationales. Cependant, ce sont uniquement les modules `gentoo/2023` et `CCconfig` qui seront chargés par défaut; vous devrez charger explicitement tous les autres modules (compilateurs, bibliothèques, Python, etc.).

Pour charger par défaut les mêmes modules que sur les autres grappes nationales, chargez le module `StdEnv/2023`.
```bash
$ module load StdEnv/2023
```
Ceci charge le compilateur `gcc` par défaut, ainsi que plusieurs autres modules.

Pour compiler du code GPU avec CUDA, vous devez aussi charger le module CUDA.
```bash
trig-login01$ module load StdEnv/2023 cuda/12.6
```
Le module CUDA n'est pas disponible sur les nœuds CPU de Trillium; il fonctionne uniquement sur le nœud de connexion GPU et les nœuds de calcul GPU.

### Recompilation

Même si tous vos fichiers, binaires compris, ont été copiés, les codes n'utilisant pas la pile logicielle CVMFS ou utilisant des chemins absolus devront être recompilés. Il est d'ailleurs recommandé de recompiler tout votre code, même s'il utilisait la pile CVMFS sur Niagara.

### Environnements virtuels Python

Même si tous vos fichiers ont été copiés, vos environnements virtuels ne fonctionneront pas. Vous devrez les recréer en raison du changement de l’emplacement des répertoires des utilisateurs.

Comme il n'y a plus de module `anaconda`, vous devrez utiliser plutôt un environnement virtuel.

## Formation, documentation et soutien
*   Information sur comment démarrer : [Trillium : Guide de démarrage](trillium-quickstart/fr.md)
*   Soutien technique : [trillium@tech.alliancecan.ca](mailto:trillium@tech.alliancecan.ca)
*   Autoformation : [Intro to SciNet and Trillium](https://education.scinet.utoronto.ca/course/view.php?id=1389) (en anglais)