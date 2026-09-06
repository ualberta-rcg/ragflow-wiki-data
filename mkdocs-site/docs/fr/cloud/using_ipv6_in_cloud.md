---
title: "Using ipv6 in cloud/fr"
slug: "using_ipv6_in_cloud"
lang: "fr"

source_wiki_title: "Using ipv6 in cloud/fr"
source_hash: "4546e679d85fc3b8b80f8765ef1418d8"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T03:01:44.495084+00:00"

tags:
  - cloud

keywords:
  - "IPv6‑GUA"
  - "Configuration Script"
  - "sysctl.conf"
  - "Attacher l'interface"
  - "Debian instance"
  - "ssh_authorized_keys"
  - "IPv6-GUA"
  - "SLAAC"
  - "initial user account creation"
  - "SSH key pair installation failure"
  - "Permission Denied error"
  - "Groupes de sécurité"
  - "OpenStack CLI"
  - "eth1"
  - "IPv6"

questions:
  - "Comment les adresses IPv6 (LLA et GUA) sont‑elles configurées et quelles sont les règles de sécurité par défaut dans l’environnement Arbutus ?"
  - "Quelles sont les étapes, en ligne de commande et via le tableau de bord, pour attacher une interface réseau IPv6‑GUA à une instance OpenStack ?"
  - "Quel problème apparaît lors du lancement d’une instance Debian avec le réseau IPv6‑GUA et comment le contourner pour pouvoir se connecter en SSH ?"
  - "Quel script doit‑on ajouter dans le « Customization Script » et quelles valeurs doivent être remplacées par le nom d’utilisateur et la clé publique ?"
  - "Comment vérifier que l’IPv6 est activée sur le système et quelles modifications faut‑il apporter à /etc/sysctl.conf et aux fichiers de configuration réseau pour activer l’interface eth1 ?"
  - "Quelles commandes permettent de confirmer que l’interface eth1 est correctement configurée et que l’IPv6 fonctionne après les redémarrages ?"
  - "What issue arises with the SSH key pair when a Debian instance is launched using an IPv6‑GUA network?"
  - "What error message do researchers receive when they attempt to SSH into the affected instance?"
  - "What steps are recommended as a workaround to gain access to the instance during its configuration?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## IPv6 avec Arbutus

Les adresses LLA (Link-Local) et GUA (Global Unicast Addresses) sont généralement disponibles dans l'environnement infonuagique d'Arbutus. Les adresses GUA peuvent être configurées via une interface distincte, qui à son tour ne s'occupe que du trafic IPv6.
Les adresses sont configurées par SLAAC (Stateless Address Auto Configuration), qui configure automatiquement l'IP sur l'interface de l'instance. Par défaut, les règles des groupes de sécurité permettent le trafic sortant de l'instance via le GUA d'IPv6, mais rien en provenance de l'extérieur de l'instance ne sera permis tant que des règles spécifiques n'auront pas été définies. Ce comportement est identique à celui d'IPv4.

### Exemple de configuration avec l'interface de ligne de commande (CLI) OpenStack

Obtenez l'ID de l'instance pour attacher l'interface réseau.

```bash
openstack server list
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                      | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
```

Assignez une nouvelle interface réseau à l'instance avec IPv6 comme réseau.

```bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34  IPv6-GUA
```

Vérifiez l'état de l'assignation.

```bash
openstack server list
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                                                                       | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
```

### Exemple de configuration via l'interface web

Connectez-vous au tableau de bord. Dans le menu *Instances*, cliquez sur *Attacher l'interface* pour afficher la boîte de dialogue.
Dans le champ *Réseau*, sélectionnez *IPv6-GUA (2607:f8f0:c11:7004::/64)* et cliquez sur *Attacher l'interface*.

L'adresse IPv6 restera disponible jusqu'à ce qu'elle soit détachée. Chaque fois que l'interface est détachée, l'adresse GUA est libérée et elle retourne dans le bassin; elle peut ainsi être utilisée par les autres. Toutefois, le fait de reconstruire ou de redémarrer l'instance ne libère pas l'adresse GUA.

L'accès à partir d'une adresse GUA peut être autorisé par la fonction *Groupes de sécurité* d'OpenStack, à l'exception du CIDR qui détecte automatiquement le type d'une adresse.

### Exemple d'une instance Debian

Lorsque les chercheurs lancent une instance avec le système d'exploitation Debian et le réseau IPv6 (c'est-à-dire IPv6-GUA), la paire de clés SSH sélectionnée ne s'installera pas correctement. Par conséquent, les chercheurs ne pourront pas se connecter à l'instance via SSH et recevront un message d'erreur « Permission refusée ». Pour contourner ce problème, lorsqu'un chercheur lance une nouvelle instance, il peut créer un compte utilisateur initial en suivant les étapes ci-dessous :

1.  Accédez à l'étape « Configuration ».
2.  Ajoutez le script suivant au « Script de personnalisation ». Remplacez `[nom d'utilisateur]` par le nom d'utilisateur préféré du chercheur et `[clé publique]` par sa clé publique.
3.  Sélectionnez « Lecteur de configuration ».

```yaml
users:
  - name: [nom d'utilisateur]
    gecos: [nom d'utilisateur]
    groups: sudo
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
    lock_passwd: true
    ssh_authorized_keys:
      - [clé publique]

ssh_pwauth: false
```

## Exemple de configuration Linux

Le réseau OpenStack que vous avez configuré ci-dessus apparaîtra sous Linux comme une interface de type eth. Dans la plupart des cas, votre interface actuelle sera `/dev/eth0` et votre nouvelle interface IPv6 activée sera `/dev/eth1`. Le moyen le plus facile de détecter votre nouveau périphérique est de redémarrer l'ordinateur. Mais auparavant, vérifiez que IPv6 est activée avec la commande :

```bash
sudo sysctl -a | grep ipv6.*disable
```

Les résultats devraient tous se terminer par zéro. L'IPv6 est activée par défaut pour toutes les images récentes. Les paramètres qui devraient être modifiés à zéro devraient être ajoutés à `/etc/sysctl.conf`.

Ajoutez aussi les paramètres de noyau suivants dans `/etc/sysctl.conf`.

```ini
net.ipv6.conf.eth1.forwarding=0
net.ipv6.conf.eth1.accept_ra=1
```

Redémarrez votre système et confirmez que IPv6 est activé et que `/dev/eth1` existe.

Ajoutez les configurations suivantes à `/etc/sysconfig/network-scripts/ifcfg-eth1` :

```ini
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
```

Redémarrez votre système à nouveau; l'interface `/dev/eth1` devrait être configurée et prête à être utilisée.

Vous pouvez maintenant confirmer la configuration IPv6 avec la commande :

```bash
ip -6 address
```

Confirmez que IPv6 fonctionne avec la commande :

```bash
ping6 -c 1 www.google.com
```

Votre système est maintenant configuré pour utiliser IPv6.

## Plus d'informations

*   [Ce qu'il faut savoir sur IPv6 (RedHat)](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
*   [Configuration d'une adresse IPv6 dans Red Hat Enterprise Linux 7 et 8 (RedHat)](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
*   [IPv6 (OpenStack)](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)