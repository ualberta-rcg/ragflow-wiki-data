---
title: "VM recovery via cloud console/fr"
tags:
  - cloud

keywords:
  []
---

S'il est impossible d'accéder à l'instance via SSH ou via un utilisateur local, vous pouvez démarrer le système d'exploitation en mode utilisateur unique ou encore lancer un noyau de récupération, ce qui vous donnera un accès privilégié à l'image du système d'exploitation. La seule condition est que le gestionnaire de démarrage soit accessible et modifiable.

## Sous Debian10 

Comme on peut s'y attendre de la part de CentOS, la procédure de récupération n'est pas facile; la fonctionnalité est la même, ou du moins similaire. Pour la plupart des images, le compte racine est verrouillé et donc le démarrage en mode utilisateur unique ne nous aidera pas. Toutefois, quand un système Linux démarre, peu importe le gabarit, le noyau abandonne le contrôle dans l'espace utilisateur à toute chose reliée à l'espace utilisateur, par exemple l'exécution des démons, etc.  Ceci se fait aussitôt que le matériel est initialisé, puis le noyau exécute un binaire de l'espace d'un seul utilisateur nommé le processus `init` qui a toujours PID1; dans les plus récentes distributions, il s'agit de `systemd`, `systemV` ou `upstart`. Nous pouvons modifier ceci avec le gestionnaire de démarrage, pour dire au noyau d'exécuter plutôt un interpréteur (<i>shell</i>), monter manuellement le système de fichiers image et effectuer les opérations de récupération. L'image debian10 vient aussi avec GRUB2, mais avec un menu sensiblement différent; par contre, les clés et combinaisons de clés restent les mêmes. Démarrez ou redémarrez le système jusqu'à ce que le menu GRUB soit affiché puis entrez `e` (pour <i>edit</i>). Supprimez les consoles à transmission série et ajoutez `init=/bin/bash` pour que le noyau reconnaisse le nouveau processus `init`.

Modifiez la ligne suivant `linux` comme suit&nbsp;:

`linux  /boot/vmlinuz-4.19.0-6-cloud-amd64 root=UUID=d187d85e-8a80-4664-8b5a-dce4d7ceca9e ro  biosdevname=0 net.ifnames=0 console=tty0 init=/bin/bash`

Ceci démarre le noyau, initialise `initrd` et exécute `/bin/bash` comme processus `init`. Nous sommes maintenant en mémoire et le système de fichiers est monté en lecture seule (r/o) puisque le processus `init` est censé prendre en charge le système de fichiers racine; le noyau doit simplement savoir où le trouver avant d'abandonner le contrôle. Pour que la récupération soit utile, les prochaines étapes sont de remonter le système de fichiers initrd en lecture-écriture, monter le disque image du système d'exploitation, entrer avec chroot, définir un mot de passe pour la racine et redémarrer l'instance. Il est alors possible de se connecter avec les privilèges racine. Prenez note que bash n'a pas de `reboot` ni de mécanisme de contrôle de l'alimentation; nous devons donc tout démonter proprement et arrêter l'instance.

Dans notre initrd, remontez le système de fichiers en lecture-écriture (r/w).

`mount -o remount,rw /`

Montez /dev/vda1 (la première partition primaire) sur /mnt.

`mount /dev/vda1 /mnt`

Le système de fichiers de l'image de la racine est maintenant monté en lecture-écriture sur `/mnt`. Pour pouvoir y utiliser des outils via chroot, nous devons montrer  `/dev` pour avoir un accès tty, puis `/proc` et `/sys` pour ensuite pouvoir avoir accès au réseau.

`mount -o bind /proc /mnt/proc` `mount -o bind /sys /mnt/sys` `mount -o bind /dev /mnt/dev`

Entrez dans `/mnt` avec chroot, ce qui produira une erreur ioctl pour le groupe de processus du terminal; ne tenez pas compte de cette erreur. Nous pouvons maintenant utiliser `passwd` pour redéfinir le mot de passe de la racine, puis quitter chroot avec `Ctrl+D`, démonter les points de montage montés précédemment et redémarrer le système avec le bouton `Ctrl+Alt+Del` de la page de la console OpenStack. Vous pouvez aussi simplement arrêter et lancer l'instance puisque tous les systèmes de fichiers physiques sont déjà démontés, qu'ils sont déjà synchronisés et que toutes les mémoires tampons ont été vidées sur le disque virtuel; nous opérons directement dans la mémoire, ce qui est en soi volatil.

Une fois que l'instance est lancée, vous pouvez vous y connecter avec le mot de passe que vous avez sélectionné, ensuite supprimer de nouveau le mot de passe ou désactiver les connexions directes en mode racine via SSH.

## Sous CentOS7 

Ouvrez la console via Horizon et redémarrez l'instance avec le bouton `CtrlAltDel` dans le coin supérieur de droite (à moins que vous deviez récupérer d'une situation de panique persistante due au noyau). Le gestionnaire de démarrage sera affiché, ce qui est habituel pour les images infonuagiques GRUB ou GRUB2. Les autres fonctionneraient aussi, mais avec une séquence différente de clés pour avoir accès aux paramètres <i>append</i> pour le noyau. Quand le menu GRUB est affiché, appuyez sur la touche `e` du clavier pour entrer en mode d'édition et vous verrez quelque chose comme ceci&nbsp;:

<pre>        insmod xfs
        set root='hd0,msdos1'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint='hd0,msdos1'  3ef2b806-efd7-4eef-aaa2-2584909365ff
        else
          search --no-floppy --fs-uuid --set=root 3ef2b806-efd7-4eef-aaa2-2584909365ff
        fi
        linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro console=tty0 console=ttyS0,115200n8 crashkernel=auto console=ttyS0,115200 LANG=en_US.UTF-8
        initrd16 /boot/initramfs-3.10.0-1127.19.1.el7.x86_64.img
</pre>
Naviguez ensuite à la ligne qui commence par `linux16` où tous les paramètres de la console doivent être supprimés. Puisque qemu utilise la console à transmission série (ttySX), il faudrait se rendre directement sur le nœud de calcul pour l'attacher à un  terminal. Le plus simple est de laisser `console=tty0` sur place.
Si nous voulons que le système de fichiers soit monté en lecture-écriture, il faudrait remplacer le paramètre `ro` par `rw`, mais ceci peut attendre; il est préférable d'être en lecture seule parce que les estampilles temporelles resteront intactes au cas où il faudrait retracer un problème. Le paramètre Centos `rd.break` permet d'interrompre le processus de démarrage à ses débuts. La ligne `linux16` ressemblerait à ceci (l'ordre des paramètres est sans importance)&nbsp;:

`linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro rd.break console=tty0 crashkernel=auto LANG=en_US.UTF-8`

Pour démarrer le noyau avec les modifications, appuyez sur `Crtl+x`. Sous `/sysroot`, vous trouverez le système de fichiers en lecture seule monté avec l'image et vous pouvez y entrer avec chroot ou encore le modifier directement. Pour le rendre en lecture-écriture,  vous devez le remonter avec `mount -o remount,rw /sysroot`.

## Sous CentOS8 

Les étapes sont semblables à la procédure avec CentOS7. L'option `console` doit initialiser un tty plutôt qu'une console à transmission série et `rd.break` lancera l'environnement de récupération,

par exemple `root=UUID=c7b1ead0-f176-4f23-b9c7-299eb4a06cef ro console=tty no_timer_check net.ifnames=0 crashkernel=auto`