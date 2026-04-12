---
title: "VM recovery via cloud console/en"
slug: "vm_recovery_via_cloud_console"
lang: "en"

source_wiki_title: "VM recovery via cloud console/en"
source_hash: "233f5d494fe429089f3e29b78e47e165"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:34:52.432990+00:00"

tags:
  - cloud

keywords:
  - "append parameters"
  - "sysroot"
  - "GRUB"
  - "VM recovery"
  - "Debian 10"
  - "linux16"
  - "rd.break"
  - "edit mode"
  - "console parameters"
  - "boot manager"
  - "kernel panic"
  - "single user mode"
  - "CentOS recovery"
  - "root password"
  - "GRUB boot manager"

questions:
  - "What is the fundamental requirement and underlying process for regaining access to a Linux VM when standard SSH or local logins fail?"
  - "What specific modifications need to be made to the GRUB boot parameters to launch a recovery shell in Debian 10?"
  - "After accessing the recovery shell, what sequence of commands is required to mount the file systems, reset the root password, and safely reboot the virtual machine?"
  - "What specific parameters must be added or removed from the `linux16` line to interrupt the boot process and enter the recovery environment?"
  - "Why does the guide recommend leaving `console=tty0` and removing other serial console parameters during this procedure?"
  - "How do you remount the image's filesystem with read and write permissions once you have accessed the recovery environment under `/sysroot`?"
  - "What is the purpose of the CtrlAltDel button in the upper right corner, and in what situation might it not be sufficient?"
  - "Which boot managers are currently utilized for all cloud images mentioned in the text?"
  - "What keyboard action is required to enter edit mode and access the kernel's append parameters once the GRUB menu appears?"
  - "What specific parameters must be added or removed from the `linux16` line to interrupt the boot process and enter the recovery environment?"
  - "Why does the guide recommend leaving `console=tty0` and removing other serial console parameters during this procedure?"
  - "How do you remount the image's filesystem with read and write permissions once you have accessed the recovery environment under `/sysroot`?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

If the VM can't be accessed anymore via SSH or via a local user, the OS can be booted into single user mode or a recovery kernel can be launched, which provides privileged access to the OS image. The only requirement is that the boot manager is accessible and can be modified.

## Debian10 recovery

The recovery procedure is not that easy and convenient, as you would expect from CentOS; the functionality is the same or at least similar. Most cloud images have the root account locked, so just booting single user won't help us. However, when a Linux-based system boots, regardless what flavour it is, the kernel gives up the control into userspace for all things related to userspace, like running daemons, etc. That is done as soon as all the hardware is initialized, then the kernel runs a single userspace binary, called the `init` process which always has PID1; in most recent distributions it is either `systemd`, `systemV` or `upstart`. Via the boot manager, we are able to modify that and tell the kernel to execute a shell instead and manually mount the image filesystem and do our recovery operations. The debian10 image comes with GRUB2 as well, but the menu looks a little different; however, the keys and key combinations we need to use are all the same. Boot or reboot the system until you see the GRUB menu, then hit `e` for *edit*. Remove the serial consoles and add `init=/bin/bash` to let the kernel know the new `init` process.

Modify the line after `linux` like below:

```bash
linux  /boot/vmlinuz-4.19.0-6-cloud-amd64 root=UUID=d187d85e-8a80-4664-8b5a-dce4d7ceca9e ro  biosdevname=0 net.ifnames=0 console=tty0 init=/bin/bash
```

That will boot the kernel, initialize `initrd` and execute `/bin/bash` as the `init` process. Now, we basically landed in memory and are mounted r/o, since the userspace `init` process is supposed to take care of the root filesystem; the kernel just needs to know where to find it before it hands over the control. To do a useful recovery, the next steps will be to remount the initrd filesystem r/w, mount the OS image disk, chroot into it, set a root password and restart the VM. After a successful restart, we can log in as root.

!!! note "Important Reboot Information"
    Bash has no `reboot` or any power control mechanism, so we have to unmount everything cleanly and stop the VM.

Within our initrd remount the file system r/w:

```bash
mount -o remount,rw /
```

Mount /dev/vda1 (the first primary partition) to /mnt:

```bash
mount /dev/vda1 /mnt
```

We now have the image root filesystem r/w mounted at `/mnt`. To use tools like `passwd` via chroot in there, we need to mount `/dev` to gain tty access and `/proc` and `/sys`, since we can then also access the network.

```bash
mount -o bind /proc /mnt/proc
mount -o bind /sys /mnt/sys
mount -o bind /dev /mnt/dev
```

Then chroot into `/mnt`.

!!! note "Ignoring ioctl Error"
    This will show an ioctl error for the terminal process group; you can ignore that.

Now we can just use `passwd` to reset the root password. Once done we leave the chroot via `Ctrl+D`, unmount our previously mounted mount points and restart the system by using the `Ctrl+Alt+Del` submit button on the OpenStack console page. You can also just stop and start the VM since we unmounted all real filesystems; they are already synced and all buffers flushed to the virtual disk. So we are strictly operating in memory, which is volatile anyway.

!!! warning "Post-Recovery Security"
    After the VM has started, you can now log in as user root with the password you have chosen. Once completed, remove the root password again, or disable direct root logins via SSH.

## CentOS7 recovery

Open the console via Horizon and reboot the VM; the `CtrlAltDel` button in the upper right corner can be used for that, unless you need to recover from a persistent kernel panic. At one point the boot manager shows up, which is currently for all cloud images GRUB or GRUB2. Others would work as well; they will only have a different key sequence to gain access to the append parameters for the kernel. Once the GRUB menu is visible, hit `e` on your keyboard to get into *edit* mode. You will see something like this:

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
Now, navigate to the line which starts with `linux16`. Here, all console parameters need to be removed. Since qemu uses the serial console (ttySX), we would have to go onto the compute node directly and attach it there to a terminal. The easier option is just to leave `console=tty0` in there. If we want to have the filesystem from the image mounted r/w, we would have to change the parameter `ro` to `rw`, but that can be done later as well; if something needs to be investigated, r/o is a very good option to leave timestamps intact on files. Centos has a parameter to interrupt the boot process in an early stage, which is `rd.break`. The `linux16` line should then look like this (the order of the parameters do not matter):

```bash
linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro rd.break console=tty0 crashkernel=auto LANG=en_US.UTF-8
```

To boot the kernel with the changes, hit `Ctrl+x`. Under `/sysroot`, you will find the r/o mounted filesystem from the image. You can chroot into it or modify it directly. To make it r/w, it needs to be remounted:

```bash
mount -o remount,rw /sysroot
```

## CentOS8 recovery

The steps are very similar compared to the CentOS7 recovery procedure: the option `console` needs to initialize a tty instead of a serial console and `rd.break` will launch the recovery environment.

e.g:
```bash
root=UUID=c7b1ead0-f176-4f23-b9c7-299eb4a06cef ro console=tty no_timer_check net.ifnames=0 crashkernel=auto