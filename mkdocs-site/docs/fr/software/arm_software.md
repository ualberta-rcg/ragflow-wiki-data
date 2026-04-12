---
title: "ARM software/fr"
slug: "arm_software"
lang: "fr"

source_wiki_title: "ARM software/fr"
source_hash: "de6bc7717ff429c0b1804700a4652a01"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:26:17.201032+00:00"

tags:
  - software

keywords:
  - "ddt-gpu"
  - "Linaro DDT"
  - "débogage"
  - "permissions"
  - "module CUDA"
  - "problème de latence"
  - "profileur MAP"
  - "DDT"
  - "CUDA"
  - "pilote CUDA"
  - "code parallèle"
  - "ddt"
  - "openmpi"
  - "X11"
  - "VNC"

questions:
  - "Quelles sont les principales fonctionnalités de Linaro DDT et quels langages ou types d'applications permet-il de déboguer ?"
  - "Comment doit-on procéder pour allouer des ressources, lancer une session interactive sur CPU et contourner le problème d'affichage des files de messages avec OpenMPI ?"
  - "Quelles sont les étapes spécifiques et les modules nécessaires pour configurer et lancer le débogage d'un code CUDA sur un GPU ?"
  - "Comment peut-on résoudre le problème de latence de l'interface DDT causé par la redirection X-11 ?"
  - "Quelle est la procédure pour lancer manuellement une tâche DDT lorsque la session VNC se trouve sur un nœud de connexion ou un nœud VDI ?"
  - "Comment doit-on modifier les permissions de son répertoire personnel pour corriger les problèmes connus liés à X11 ?"
  - "Quels modules doivent être chargés avant de pouvoir utiliser l'outil DDT ?"
  - "Quelle commande permet de lancer DDT sur un chemin de code spécifique ?"
  - "Comment résoudre les problèmes liés à une incompatibilité entre le pilote CUDA et la version de la boîte d'outils lors de l'utilisation de DDT ?"
  - "Comment peut-on résoudre le problème de latence de l'interface DDT causé par la redirection X-11 ?"
  - "Quelle est la procédure pour lancer manuellement une tâche DDT lorsque la session VNC se trouve sur un nœud de connexion ou un nœud VDI ?"
  - "Comment doit-on modifier les permissions de son répertoire personnel pour corriger les problèmes connus liés à X11 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

[Linaro DDT](https://www.linaroforge.com/linaro-ddt) (auparavant *ARM DDT*) est un outil commercial puissant pour le débogage de code parallèle. Doté d'une interface utilisateur graphique, il sert au débogage en C, C++ et Fortran des applications en série, MPI, multifils, CUDA ou toute combinaison de ces types. Linaro offre également le profileur [MAP](https://www.linaroforge.com/linaro-map) pour le code parallèle.

Les modules suivants sont disponibles sur Nibi et Trillium (quand le module StdEnv est chargé) :
*   ddt-cpu pour déboguer et profiler le code sur le CPU;
*   ddt-gpu pour déboguer le code sur les GPU ou sur CPU/GPU.

Puisqu'il s'agit d'une application avec une interface graphique, connectez-vous avec `ssh -Y` et utilisez un [client SSH](../getting-started/ssh.md) comme [MobaXTerm](../getting-started/connecting_with_mobaxterm.md) (sous Windows) ou [XQuartz](https://www.xquartz.org/) (sous Mac) pour assurer la redirection X11.

On utilise généralement DDT et MAP de façon interactive via l'interface utilisateur avec la commande `salloc`. Le profileur MAP peut aussi être utilisé de façon non interactive en soumettant des tâches à l'ordonnanceur avec la commande `sbatch`.

Avec la licence actuelle, DDT/MAP peuvent utiliser concurremment jusqu'à 64 CPU pour tous les utilisateurs, alors que DDT-GPU ne peut utiliser que 8 GPU.

## Utilisation

### Avec le CPU seulement (aucun GPU)

1.  Allouez le ou les nœuds sur lesquels vous voulez déboguer ou profiler; ceci ouvre une session de l'interpréteur (*shell*) sur les nœuds en question.
    ```bash
    salloc --x11 --time=0-1:00 --mem-per-cpu=4G --ntasks=4
    ```

2.  Chargez le module approprié, par exemple :
    ```bash
    module load ddt-cpu
    ```

3.  Lancez la commande ddt ou map.
    ```bash
    ddt chemin/vers/le/code
    map chemin/vers/le/code
    ```

!!! note
    Avant de cliquer sur « Run », assurez-vous que l'implémentation MPI est l'OpenMPI par défaut dans la fenêtre de DDT/MAP. Si ce n'est pas le cas, cliquez sur le bouton « Modifier » (près de « Implémentation ») et sélectionnez l'option correcte dans le menu déroulant. Spécifiez aussi le nombre de cœurs de CPU dans cette fenêtre.

4.  Quittez l'interpréteur pour terminer l'allocation.

!!! warning "Important"
    Les versions courantes de DDT et OpenMPI ont un problème de compatibilité qui empêche DDT d'afficher les files de messages (menu déroulant « Outils »). Pour contourner ce problème, lancez la commande :

    ```bash
    export OMPI_MCA_pml=ob1
    ```

    Comme ceci peut ralentir le code MPI, n'utilisez cette commande qu'en débogage.

### Avec CUDA

1.  Allouez le ou les nœuds sur lesquels vous voulez déboguer ou profiler avec `salloc`; ceci ouvre une session de l'interpréteur (*shell*) sur les nœuds en question.
    ```bash
    salloc --x11 --time=0-1:00 --mem-per-cpu=4G --ntasks=1 --gres=gpu:1
    ```

2.  Chargez le module approprié, par exemple :
    ```bash
    module load ddt-gpu
    ```

!!! tip
    Il est possible qu'on vous demande de charger d'abord une version antérieure d'OpenMPI. Dans ce cas, chargez de nouveau le module OpenMPI en utilisant la commande proposée, puis chargez de nouveau le module ddt-gpu.
    ```bash
    module load openmpi/2.0.2
    module load ddt-gpu
    ```

3.  Assurez-vous qu'un module CUDA est chargé.
    ```bash
    module load cuda
    ```

4.  Lancez la commande ddt.
    ```bash
    ddt chemin/vers/le/code
    ```

    Si DDT crée des difficultés en raison d'une incompatibilité entre le pilote CUDA et la version de la boîte d'outils, exécutez la commande suivante et lancez DDT de nouveau (utiliser la même version que dans la commande).
    ```bash
    export ALLINEA_FORCE_CUDA_VERSION=10.1
    ```

5.  Quittez l'interpréteur pour terminer l'allocation.

### Problème de latence

!!! tip
    Les directives ci-dessus utilisent la redirection X-11 qui s'avère très sensible au problème de latence des paquets. Si vous n'êtes pas sur le même campus que le supercalculateur, l'interface de DDT sera probablement lente et occasionnera de la frustration. Pour remédier à ce problème, utilisez DDT sous VNC.

Pour ce faire, [préparez une session VNC](../interactive/vnc.md). Si votre session VNC se trouve sur le nœud de calcul, vous pouvez démarrer votre programme ddt directement, comme décrit ci-dessus. Si votre session VNC se trouve sur le nœud de connexion ou si vous utilisez le nœud VDI de Graham, vous devez lancer la tâche à partir de l'écran de démarrage de DDT comme suit :

*   sélectionnez l'option « Lancer le *backend* vous-même manuellement » pour le lancement de la tâche;
*   entrez les renseignements de votre tâche et cliquez sur le bouton « Écouter »;
*   cliquez sur le bouton « Aide » à droite de « En attente du démarrage de la tâche... ».

Ceci vous donnera la commande à utiliser pour lancer votre tâche. Allouez une tâche sur le supercalculateur et démarrez votre programme tel qu'indiqué. Dans l'exemple suivant, `$USER` est votre nom d'utilisateur et `$PROGRAM` est la commande pour démarrer votre programme.

```bash
[nom@grappe-connexion:~]$ salloc ...
[nom@nœud-grappe:~]$ /cvmfs/restricted.computecanada.ca/easybuild/software/2020/Core/allinea/20.2/bin/forge-client --ddtsessionfile /home/$USER/.allinea/session/gra-vdi3-1 $PROGRAM ...
```

## Problèmes connus

!!! warning
    Si vous avez des problèmes avec X11, modifiez les permissions de votre répertoire `/home` pour que l'accès soit possible uniquement par vous.

D'abord, vérifiez (et notez au besoin) les permissions courantes avec :
```bash
ls -ld /home/$USER
```
Le résultat devrait commencer par :
```
drwx------
```
Si certains tirets sont remplacés par des lettres, votre groupe et les autres utilisateurs ont des permissions de lecture, écriture (peu probable) ou exécution pour votre répertoire.

La commande suivante supprimera les permissions de lecture et exécution pour le groupe et les autres utilisateurs.
```bash
chmod go-rx /home/$USER
```
Quand vous aurez terminé avec DDT, vous pourrez, au choix, revenir aux permissions antérieures (en supposant que vous les avez notées). Pour plus d'information, consultez [Partage de données](../storage-and-data/sharing_data.md).

## Pour plus d'information

*   ["Debugging your code with DDT"](https://youtu.be/Q8HwLg22BpY) (vidéo d'une durée de 55 minutes)
*   *Parallel debugging with DDT* (court tutoriel)