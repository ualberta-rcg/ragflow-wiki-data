---
title: "VM recovery via cloud console/fr"
slug: "vm_recovery_via_cloud_console"
lang: "fr"

source_wiki_title: "VM recovery via cloud console/fr"
source_hash: "83302d240b0f578d18d60f6bc6450e98"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:35:21.608643+00:00"

tags:
  - cloud

keywords:
  - "environnement de récupération"
  - "accès au réseau"
  - "rd.break"
  - "chroot"
  - "démarrer le noyau"
  - "lecture-écriture"
  - "récupération"
  - "CentOS7"
  - "accès tty"
  - "GRUB"
  - "CentOS8"
  - "mot de passe racine"
  - "mode utilisateur unique"
  - "CentOS 7"
  - "console"
  - "gestionnaire de démarrage"
  - "système de fichiers"
  - "mount"
  - "/sysroot"
  - "processus init"

questions:
  - "Quelle est la condition préalable indispensable pour pouvoir démarrer l'instance en mode de récupération ?"
  - "Quelle modification doit-on apporter à la ligne du noyau dans GRUB pour forcer l'exécution d'un interpréteur de commandes au démarrage ?"
  - "Quelles commandes de montage doivent être exécutées dans l'interpréteur pour préparer le système de fichiers avant d'utiliser chroot ?"
  - "Quelles sont les étapes à suivre dans l'environnement chroot pour redéfinir le mot de passe racine et redémarrer correctement l'instance ?"
  - "Comment modifier les paramètres de la ligne de commande du noyau dans le menu GRUB sous CentOS 7 pour interrompre le processus de démarrage ?"
  - "Pourquoi est-il conseillé de garder le système de fichiers en lecture seule initialement, et quelle commande permet de le remonter en lecture-écriture sous `/sysroot` ?"
  - "Pourquoi est-il nécessaire de monter les répertoires `/dev`, `/proc` et `/sys` avant d'utiliser des outils via chroot ?"
  - "Quels répertoires spécifiques permettent d'obtenir respectivement un accès tty et un accès au réseau dans le nouvel environnement ?"
  - "Quelle commande et quelle option sont utilisées pour lier les répertoires du système hôte vers le point de montage `/mnt` ?"
  - "Quelle combinaison de touches permet de démarrer le noyau avec les modifications apportées ?"
  - "Où se trouve le système de fichiers monté en lecture seule et comment peut-on y accéder ?"
  - "Quelle commande doit-on exécuter pour remonter le système de fichiers en mode lecture-écriture ?"
  - "Comment la procédure sous CentOS 8 se compare-t-elle à celle de CentOS 7 ?"
  - "Quelle modification doit être apportée à l'option console par rapport à une console à transmission série ?"
  - "Quelle option permet de lancer l'environnement de récupération du système ?"
  - "Comment la procédure sous CentOS 8 se compare-t-elle à celle de CentOS 7 ?"
  - "Quelle modification doit être apportée à l'option console par rapport à une console à transmission série ?"
  - "Quelle option permet de lancer l'environnement de récupération du système ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Si vous ne pouvez pas accéder à l'instance via SSH ou via un utilisateur local, vous avez l'option de démarrer le système d'exploitation en mode utilisateur unique ou de lancer un noyau de récupération. Ces méthodes vous accorderont un accès privilégié à l'image du système d'exploitation. La seule condition préalable est que le gestionnaire de démarrage soit accessible et puisse être modifié.

## Sous Debian10

Comme on peut s'y attendre de la part de CentOS, la procédure de récupération n'est pas facile; la fonctionnalité est la même, ou du moins similaire. Pour la plupart des images, le compte racine est verrouillé et donc le démarrage en mode utilisateur unique ne nous aidera pas. Toutefois, quand un système Linux démarre, peu importe le gabarit, le noyau abandonne le contrôle dans l'espace utilisateur à toute chose reliée à l'espace utilisateur, par exemple l'exécution des démons, etc. Ceci se fait aussitôt que le matériel est initialisé, puis le noyau exécute un binaire de l'espace d'un seul utilisateur nommé le processus `init` qui a toujours PID1; dans les plus récentes distributions, il s'agit de `systemd`, `systemV` ou `upstart`. Nous pouvons modifier ceci avec le gestionnaire de démarrage, pour dire au noyau d'exécuter plutôt un interpréteur de commandes (*shell*), monter manuellement le système de fichiers image et effectuer les opérations de récupération. L'image Debian10 vient aussi avec GRUB2, mais avec un menu sensiblement différent; par contre, les clés et combinaisons de clés restent les mêmes. Démarrez ou redémarrez le système jusqu'à ce que le menu GRUB soit affiché puis entrez `e` (pour modifier). Supprimez les consoles à transmission série et ajoutez `init=/bin/bash` pour que le noyau reconnaisse le nouveau processus `init`.

Modifiez la ligne suivant `linux` comme suit :

```bash
linux /boot/vmlinuz-4.19.0-6-cloud-amd64 root=UUID=d187d85e-8a80-4664-8b5a-dce4d7ceca9e ro biosdevname=0 net.ifnames=0 console=tty0 init=/bin/bash
```

Ceci démarre le noyau, initialise `initrd` et exécute `/bin/bash` comme processus `init`. Nous sommes maintenant en mémoire et le système de fichiers est monté en lecture seule (r/o) puisque le processus `init` est censé prendre en charge le système de fichiers racine; le noyau doit simplement savoir où le trouver avant d'abandonner le contrôle. Pour que la récupération soit utile, les prochaines étapes sont de remonter le système de fichiers initrd en lecture-écriture, monter le disque image du système d'exploitation, entrer avec chroot, définir un mot de passe pour la racine et redémarrer l'instance. Il est alors possible de se connecter avec les privilèges racine.

!!! note "À prendre en note"
    Bash ne dispose pas d'une commande `reboot` ni d'un mécanisme de contrôle de l'alimentation. Nous devons donc tout démonter proprement et arrêter l'instance.

Dans notre initrd, remontez le système de fichiers en lecture-écriture (r/w).

```bash
mount -o remount,rw /
```

Montez /dev/vda1 (la première partition primaire) sur /mnt.

```bash
mount /dev/vda1 /mnt
```

Le système de fichiers de l'image de la racine est maintenant monté en lecture-écriture sur `/mnt`. Pour pouvoir y utiliser des outils via chroot, nous devons monter `/dev` pour avoir un accès TTY, puis `/proc` et `/sys` pour ensuite pouvoir avoir accès au réseau.

```bash
mount -o bind /proc /mnt/proc
```

```bash
mount -o bind /sys /mnt/sys
```

```bash
mount -o bind /dev /mnt/dev
```

Entrez dans `/mnt` avec chroot.

!!! tip "Note sur l'erreur chroot"
    Lorsque vous entrez dans `/mnt` avec chroot, une erreur ioctl pour le groupe de processus du terminal pourrait survenir. Ignorez cette erreur.

Nous pouvons maintenant utiliser `passwd` pour redéfinir le mot de passe de la racine, puis quitter chroot avec `Ctrl+D`, démonter les points de montage montés précédemment et redémarrer le système avec le bouton `Ctrl+Alt+Del` de la page de la console OpenStack. Vous pouvez aussi simplement arrêter et lancer l'instance puisque tous les systèmes de fichiers physiques sont déjà démontés, qu'ils sont déjà synchronisés et que toutes les mémoires tampons ont été vidées sur le disque virtuel; nous opérons directement dans la mémoire, ce qui est en soi volatil.

Une fois que l'instance est démarrée, vous pouvez vous y connecter avec le mot de passe que vous avez choisi. Par la suite, vous pourrez supprimer le mot de passe à nouveau ou désactiver les connexions directes en mode racine via SSH.

## Sous CentOS7

Ouvrez la console via Horizon et redémarrez l'instance avec le bouton `Ctrl+Alt+Del` dans le coin supérieur droit (à moins que vous ne deviez récupérer d'une situation de panique persistante due au noyau). Le gestionnaire de démarrage s'affichera, ce qui est habituel pour les images infonuagiques GRUB ou GRUB2. D'autres gestionnaires fonctionneraient également, mais avec une séquence de touches différente pour accéder aux paramètres d'ajout (*append*) pour le noyau. Lorsque le menu GRUB est affiché, appuyez sur la touche `e` du clavier pour entrer en mode d'édition et vous verrez quelque chose comme ceci :

```
        insmod xfs
        set root='hd0,msdos1'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint='hd0,msdos1'  3ef2b806-efd7-4eef-aaa2-2584909365ff
        else
          search --no-floppy --fs-uuid --set=root 3ef2b806-efd7-4eef-aaa2-2584909365ff
        fi
        linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro console=tty0 console=ttyS0,115200n8 crashkernel=auto console=ttyS0,115200 LANG=en_US.UTF-8
        initrd16 /boot/initramfs-3.10.0-1127.19.1.el7.x86_64.img
```

Naviguez ensuite à la ligne qui commence par `linux16` où tous les paramètres de la console doivent être supprimés. Étant donné que qemu utilise la console à transmission série (ttySX), il faudrait se rendre directement sur le nœud de calcul pour l'attacher à un terminal. Le plus simple est de laisser `console=tty0` en place. Si nous voulons que le système de fichiers soit monté en lecture-écriture, il faudrait remplacer le paramètre `ro` par `rw`, mais cela peut attendre; il est préférable de rester en lecture seule, car les horodatages resteront intacts au cas où il faudrait retracer un problème. Le paramètre CentOS `rd.break` permet d'interrompre le processus de démarrage à ses débuts. La ligne `linux16` ressemblerait à ceci (l'ordre des paramètres est sans importance) :

```bash
linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro rd.break console=tty0 crashkernel=auto LANG=en_US.UTF-8
```

Pour démarrer le noyau avec les modifications, appuyez sur `Ctrl+x`. Sous `/sysroot`, vous trouverez le système de fichiers monté en lecture seule avec l'image. Vous pouvez y entrer avec chroot ou le modifier directement. Pour le rendre en lecture-écriture, vous devez le remonter avec `mount -o remount,rw /sysroot`.

## Sous CentOS8

Les étapes sont similaires à la procédure avec CentOS7. L'option `console` doit initialiser un TTY plutôt qu'une console à transmission série et `rd.break` lancera l'environnement de récupération, par exemple :

```bash
root=UUID=c7b1ead0-f176-4f23-b9c7-299eb4a06cef ro console=tty no_timer_check net.ifnames=0 crashkernel=auto