---
title: "Configuring WSL as a ControlMaster relay server/fr"
slug: "configuring_wsl_as_a_controlmaster_relay_server"
lang: "fr"

source_wiki_title: "Configuring WSL as a ControlMaster relay server/fr"
source_hash: "ed4269d341f77537e85c51c03e0a03ac"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:48:15.828191+00:00"

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

!!! attention "Important"
Cette page est une ébauche; nous travaillons à sa version finale.

Si vous avez des suggestions, écrivez au [soutien technique](technical-support.md).

Cette procédure permet d'utiliser ControlMaster de WSL pour vous connecter aux grappes avec plusieurs applications Windows natives pour une certaine durée, sans avoir à vous authentifier pour chaque session.

## Installer Linux sur Windows avec WSL
Voir [Travailler avec Windows Subsystem for Linux (WSL)](windows-subsystem-for-linux-wsl.md)

Dans les fichiers de configuration :
*   la distribution est Ubuntu
*   le nom de l'hôte pour l'instance WSL est *ubuntu*; */etc/hostname* contient *ubuntu* et */etc/hosts* contient *127.0.0.1 localhost ubuntu*
*   le nom du système Windows est *smart* et la connexion est faite par l'utilisateur nommé *jaime*
*   le nom de l'utilisateur pour la machine virtuelle Ubuntu est aussi *jaime*
*   le nom de l'utilisateur pour l'Alliance est *pinto* et nous voulons nous connecter à Cedar

## Installer d'autres logiciels
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y
```
Vous pouvez vous connecter à Ubuntu à partir de Windows avec `ssh localhost`.

## La configuration ressemble à
```text
[ssh client] ----> [ssh relay server] ----> [ssh target server]
your Windows     modified authorized_keys     using cedar for
  machine          in your Ubuntu VM           this exercise
 smart        ubuntu                 Cedar
```

## Se connecter à la machine virtuelle Ubuntu et créer le répertoire *custom_ssh*
```bash
jaime@ubuntu:~$ cat custom_ssh/sshd_config
Port 2222
HostKey /home/jaime/custom_ssh/ssh_host_ed25519_key
HostKey /home/jaime/custom_ssh/ssh_host_rsa_key
AuthorizedKeysFile /home/jaime/custom_ssh/authorized_keys
ChallengeResponseAuthentication no
UsePAM no
Subsystem sftp /usr/lib/openssh/sftp-server
PidFile /home/jaime/custom_ssh/sshd.pid
```
Pour copier les clés *ssh_host* de */etc/ssh*, utilisez
```bash
sudo cp /etc/ssh/ssh_host_ed25519_key /home/jaime/custom_ssh/
```

## Modifier *.ssh/config* sur Ubuntu
```bash
jaime@ubuntu:~$ cat ~/.ssh/config
Host cedar
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 10m
    HostName cedar.alliancecan.ca
    User pinto
```

## Modifier les clés autorisées
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```
Utilisez la clé publique SSH que vous avez téléchargée dans CCDB.

## Démarrer le serveur sshd sur Ubuntu
```bash
jaime@ubuntu:~/custom_ssh$ /usr/sbin/sshd -f ${HOME}/custom_ssh/sshd_config
```
Assurez-vous que le serveur est démarré avec votre profil et non avec le profil racine (*root*). Vous devrez démarrer le serveur sshd à chaque fois que vous redémarrez votre ordinateur ou que WSL est fermé ou redémarré.

## Modifier *.ssh/config* sur *smart* avec `RemoteCommand`
```bash
jaime@smart ~/.ssh cat config
Host ubuntu
        Hostname localhost
        RemoteCommand ssh cedar
```

## Se connecter à Cedar
```bash
jaime@smart ~
$ ssh -t ubuntu -p 2222
Enter passphrase for key '/home/jaime/.ssh/id_ed25519':
Last login: Fri Mar 22 10:50:12 2024 from 99.239.174.157
================================================================================
Welcome to Cedar! / Bienvenue sur Cedar!
...
...
...
[pinto@cedar1 ~]$
```

## Autre option de configuration
Vous pouvez aussi personnaliser les clés autorisées pour Ubuntu et le fichier *~/.ssh/config* de Windows pour que certaines applications graphiques fonctionnent sans avoir à indiquer `RemoteCommand` (par exemple, WinSCP). Dans ce cas, `RemoteCommand` est indiqué pour la clé publique.
```bash
jaime@ubuntu:~/custom_ssh$ cat /home/jaime/custom_ssh/authorized_keys
command="ssh cedar" ssh-ed25519 AAAZDINzaC1lZDI1NTE5AAC1lZDIvqzlffkzcjRAaMQoTBrPe5FxlSAjRAaMQyVzN+A+
```
```bash
jaime@smart ~/.ssh cat config
Host ubuntu
        Hostname localhost
        #RemoteCommand ssh cedar
```
Par la suite, vous pouvez encore utiliser `ssh ubuntu -p 2222` à partir d'un interpréteur (*shell*) Windows.

## Configuration avec MobaXterm