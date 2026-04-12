---
title: "VM recovery via cloud console"
slug: "vm_recovery_via_cloud_console"
lang: "base"

source_wiki_title: "VM recovery via cloud console"
source_hash: "d7bc644735e19a807fa6b15eebb528fe"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:34:31.684031+00:00"

tags:
  - cloud

keywords:
  - "SSH"
  - "reset root password"
  - "console=tty0"
  - "Debian 10 recovery"
  - "virtual disk"
  - "VM"
  - "init process"
  - "kernel parameters"
  - "OpenStack console"
  - "single user mode"
  - "CentOS recovery"
  - "rd.break"
  - "chroot"
  - "root login"
  - "GRUB menu"

questions:
  - "How do you modify the GRUB boot manager to boot the kernel directly into a bash shell instead of the default init process?"
  - "What steps are necessary to remount the filesystem read/write and mount the required directories before using chroot?"
  - "How is the root password reset within the chroot environment, and what is the safe procedure to restart the VM afterward?"
  - "How do you access and enter edit mode in the GRUB boot manager via the Horizon console?"
  - "What specific parameters must be added or removed from the kernel boot line to interrupt the boot process and launch the recovery environment?"
  - "After successfully interrupting the boot process, how do you remount the root filesystem to make it read-write for modifications?"
  - "Why is it considered safe to stop and start the VM directly from the OpenStack console in this specific context?"
  - "How should a user log into the VM after it has successfully started?"
  - "What security actions must be performed on the root account after the necessary tasks are completed?"
  - "How do you access and enter edit mode in the GRUB boot manager via the Horizon console?"
  - "What specific parameters must be added or removed from the kernel boot line to interrupt the boot process and launch the recovery environment?"
  - "After successfully interrupting the boot process, how do you remount the root filesystem to make it read-write for modifications?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

If the VM can't be accessed anymore via SSH or via a local user, the OS can be booted into single user mode or a recovery kernel can be launched, which provides privileged access to the OS image. The only requirement is that the boot manager is accessible and can be modified.

## Debian 10 Recovery

!!! note
    Most cloud images have the root account locked, so just booting single user won't help us.

The recovery procedure is not that easy and convenient, as you would expect from CentOS; the functionality is the same or at least similar. However, when a Linux-based system boots, regardless what flavour it is, the kernel gives up the control into userspace for all things related to userspace, like running daemons, etc. That is done as soon as all the hardware is initialized, then the kernel runs a single userspace binary, called the `init` process which always has PID1; in most recent distributions it is either `systemd`, `systemV` or `upstart`. Via the boot manager, we are able to modify that and tell the kernel to execute a shell instead and manually mount the image filesystem and do our recovery operations. The Debian 10 image comes with GRUB2 as well, but the menu looks a little different; however, the keys and key combinations we need to use are all the same. Boot or reboot the system until you see the GRUB menu, then hit `e` for *edit*. Remove the serial consoles and add `init=/bin/bash` to let the kernel know the new `init` process.

Modify the line after `linux` like below:

```bash
linux /boot/vmlinuz-4.19.0-6-cloud-amd64 root=UUID=d187d85e-8a80-4664-8b5a-dce4d7ceca9e ro biosdevname=0 net.ifnames=0 console=tty0 init=/bin/bash
```

That will boot the kernel, initialize `initrd` and execute `/bin/bash` as the `init` process. Now, we basically landed in memory and are mounted r/o, since the userspace `init` process is supposed to take care of the root filesystem; the kernel just needs to know where to find it before it hands over the control. To do a useful recovery, the next steps will be to remount the initrd filesystem r/w, mount the OS image disk, `chroot` into it, set a root password and restart the VM. After a successful restart, we can log in as root.

!!! note
    Bash has no `reboot` or any power control mechanism, so we have to unmount everything cleanly and stop the VM.

Within our `initrd` remount the file system r/w:

```bash
mount -o remount,rw /
```

Mount `/dev/vda1` (the first primary partition) to `/mnt`:

```bash
mount /dev/vda1 /mnt
```

We now have the image root filesystem r/w mounted at `/mnt`, to use tools like `passwd` via `chroot` in there, we need to mount `/dev` to gain tty access and `/proc` and `/sys`, since we can then also access the network.

```bash
mount -o bind /proc /mnt/proc
mount -o bind /sys /mnt/sys
mount -o bind /dev /mnt/dev
```

Then `chroot` into `/mnt`, which will show an ioctl error for the terminal process group; we can ignore that. Now we can just use `passwd` to reset the root password. Once done, we leave the `chroot` via `Ctrl+D`, unmount our previously mounted mount points, and restart the system by using the `Ctrl+Alt+Del` submit button on the OpenStack console page. You can also just stop and start the VM since we unmounted all real filesystems, they are already synced and all buffers flushed to the virtual disk. So we are strictly operating in memory, which is volatile anyway.

!!! warning "Security Notice"
    After the VM has started, you can now log in as user root with the password you have chosen. Once completed, remove the root password again, or disable direct root logins via SSH.

## CentOS 7 Recovery

Open the console via Horizon and reboot the VM; the `Ctrl+Alt+Del` button in the upper right corner can be used for that, unless you need to recover from a persistent kernel panic. At one point the boot manager shows up, which is currently for all cloud images GRUB or GRUB2. Others would work as well; they will only have a different key sequence to gain access to the append parameters for the kernel. Once the GRUB menu is visible, hit `e` on your keyboard to get into edit mode, you will see something like this:

```text
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

Now, navigate to the line which starts with `linux16`. Here, all console parameters need to be removed. Since qemu uses the serial console (`ttySX`), we would have to go onto the compute node directly and attach it there to a terminal. The easier option is just to leave `console=tty0` in there. If we want to have the filesystem from the image mounted r/w, we would have to change the parameter `ro` to `rw`, but that can be done later as well; if something needs to be investigated, r/o is a very good option to leave timestamps intact on files. CentOS has a parameter to interrupt the boot process in an early stage, which is `rd.break`. The `linux16` line should then look like this (the order of the parameters does not matter):

```bash
linux16 /boot/vmlinuz-3.10.0-1127.19.1.el7.x86_64 root=UUID=3ef2b806-efd7-4eef-aaa2-2584909365ff ro rd.break console=tty0 crashkernel=auto LANG=en_US.UTF-8
```

To boot the kernel with the changes, hit `Ctrl+x`. Under `/sysroot`, you will find the ro mounted filesystem from the image; you can `chroot` into it or modify it directly. To make it rw, it needs to be remounted:

```bash
mount -o remount,rw /sysroot
```

## CentOS 8 Recovery

The steps are very similar compared to the CentOS 7 recovery procedure: the option `console` needs to initialize a tty instead of a serial console and `rd.break` will launch the recovery environment.

e.g:

```bash
root=UUID=c7b1ead0-f176-4f23-b9c7-299eb4a06cef ro console=tty no_timer_check net.ifnames=0 crashkernel=auto