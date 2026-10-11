---
title: "Using ipv6 in cloud/fr"
slug: "using_ipv6_in_cloud"
lang: "fr"

source_wiki_title: "Using ipv6 in cloud/fr"
source_hash: "d2a834bc9ba8bbbd319e61d6fc5f6da9"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:41:11.754269+00:00"

tags:
  - cloud

keywords:
  - "Lancer une instance"
  - "Debian ou Ubuntu 26.04"
  - "clé SSH non installée"
  - "IPv6 activée"
  - "Permission Denied"
  - "script de personnalisation"
  - "Arbutus"
  - "ping6"
  - "réseau IPv6 (IPv6‑GUA)"
  - "net.ipv6.conf.eth1"
  - "MTU 1452"
  - "SLAAC"
  - "IPv6"
  - "compte utilisateur initial"
  - "GUA (Global Unicast Addresses)"

questions:
  - "Quels paramètres MTU sont recommandés pendant la migration du nuage Arbutus pour IPv6, et quelle action doit‑être effectuée une fois la migration terminée ?"
  - "Comment attacher une interface réseau IPv6‑GUA à une instance à l’aide de la CLI OpenStack et vérifier que l’adresse a bien été assignée ?"
  - "Quel problème de configuration des clés SSH survient lors du lancement d’une instance Debian ou Ubuntu 26.04 avec IPv6‑GUA, et quelle solution de contournement est proposée ?"
  - "Quels sont les étapes pour créer une machine virtuelle et ajouter le script de personnalisation avec votre nom d'utilisateur et votre clé publique ?"
  - "Comment activer et configurer l'interface IPv6 (eth1) sous Linux après le déploiement de la VM OpenStack ?"
  - "Quelles commandes permettent de vérifier que l'IPv6 est correctement activée et fonctionnelle sur la machine virtuelle ?"
  - "Comment l'interface utilisateur détecte‑t‑elle automatiquement le type d’une adresse dans ce contexte ?"
  - "Pourquoi la paire de clés SSH ne s’installe‑t‑elle pas correctement sur une instance Debian ou Ubuntu 26.04 avec IPv6‑GUA, entraînant l’erreur « Permission Denied » ?"
  - "Quelle est la procédure recommandée pour créer un compte utilisateur initial afin de contourner ce problème de connexion SSH ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## IPv6 avec Arbutus

!!! warning "Attention"
    Des problèmes de connexion ont été rapportés dans la migration entre les deux versions du nuage Arbutus. Un MTU de 1452 aux extrémités de chaque interface réseau IPv6 peut être la solution. Une fois la migration terminée, revenez à la valeur par défaut du MTU.

Les adresses LLA (Link-Local) et GUA (Global Unicast Addresses) sont généralement disponibles dans l'environnement infonuagique d'Arbutus.

Les adresses GUA peuvent être configurées via une interface distincte, qui à son tour ne s'occupe que du trafic IPv6.
Les adresses sont configurées par SLAAC (Stateless Address Auto Configuration), qui configure automatiquement l'IP sur l'interface de l'instance. Par défaut, les règles des groupes de sécurité permettent le trafic sortant de l'instance via le GUA de IPv6, mais rien en provenance de l'extérieur de l'instance ne sera permis jusqu'à ce que des règles spécifiques soient définies. Ceci est le même comportement qu'avec IPv4.

## Exemple d'une configuration avec la CLI OpenStack

Obtenez l'ID de l'instance pour attacher l'interface réseau.

```bash
openstack server list
```

```
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                      | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
```

Assignez une nouvelle interface réseau à l'instance avec IPv6 comme réseau.

```bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34 IPv6-GUA
```

Vérifiez l'état de l'assignation.

```bash
openstack server list
```

```
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                                                                       | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
```

## Exemple d'une configuration via l'interface Web

Connectez-vous au tableau de bord. Dans le menu **Instances**, cliquez sur **Attacher l'interface** pour faire afficher la boîte de dialogue.
Dans le champ **Réseau**, sélectionnez **IPv6-GUA (2607:f8f0:c11:7004::/64)** et cliquez sur **Attacher l'interface**.

L'adresse IPv6 restera disponible jusqu'à ce qu'elle soit détachée. Chaque fois que l'interface est détachée, l'adresse GUA est libérée et elle retourne dans le **pool**; elle peut ainsi être utilisée par les autres. Toutefois, le fait de reconstruire ou de redémarrer l'instance ne libère pas l'adresse GUA.

L'accès à partir d'une adresse GUA peut être autorisé par la fonction **Groupes de sécurité** d'OpenStack, à l'exception de CIDR qui détecte automatiquement le type d'une adresse.

## Exemple avec une instance Debian ou Ubuntu 26.04

Avec le système d'exploitation Debian ou Ubuntu 26.04 et le réseau IPv6 (IPv6-GUA), la paire de clés SSH sélectionnée ne s'installe pas correctement quand une instance est lancée. Par conséquent, la connexion à l'instance via SSH ne se fait pas et le message d'erreur **Permission Denied** survient. Pour contourner ce problème au lancement d'une nouvelle instance, vous pouvez créer un compte utilisateur initial comme suit :
1.  Pour créer une machine virtuelle, sélectionnez **Calcul -> Instances** dans le menu de gauche, puis cliquez sur le bouton **Lancer une instance**.
2.  Référez-vous au [guide de démarrage](cloud_quick_start.md) pour faire afficher le formulaire de définition de votre machine virtuelle.
3.  Dans le menu de gauche, sélectionnez **Configuration**.
4.  Ajoutez le script suivant au script de personnalisation en remplaçant `[username]` par votre nom d'utilisateur et `[public key]` par votre clé publique.
    ```yaml
    users:
      - name: [username]
        gecos: [username]
        groups: sudo
        sudo: ALL=(ALL) NOPASSWD:ALL
        shell: /bin/bash
        lock_passwd: true
        ssh_authorized_keys:
          - [public key]

    ssh_pwauth: false
    ```
5.  Sélectionnez **Disque de configuration**.

## Exemple d'une configuration Linux

Le réseau OpenStack que vous avez configuré ci-dessus apparaîtra sous Linux comme une interface de type eth. Dans la plupart des cas, votre interface courante sera `/dev/eth0` et votre nouvelle interface IPv6 activée sera `/dev/eth1`. Le moyen le plus facile d'attraper votre nouveau périphérique est de redémarrer l'ordinateur. Mais auparavant, vérifiez que IPv6 est activée avec la commande `sudo sysctl -a | grep ipv6.*disable`.
Les résultats devraient tous se terminer par des zéros. L'IPv6 activée est l'interface par défaut pour toutes les images récentes. Les paramètres qui doivent être changés pour des zéros devraient être ajoutés à `/etc/sysctl.conf`.

Ajoutez aussi les paramètres du noyau suivants dans `/etc/sysctl.conf`.
```ini
net.ipv6.conf.eth1.forwarding=0
net.ipv6.conf.eth1.accept_ra=1
```

Redémarrez votre système et confirmez que IPv6 est activé et que `/dev/eth1` existe.

Ajoutez à `/etc/sysconfig/network-scripts/ifcfg-eth1` les configurations suivantes :
```ini
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
```

Redémarrez votre système à nouveau; l'interface `/dev/eth1` devrait être configurée et prête à être utilisée.

Vous pouvez maintenant confirmer la configuration IPv6 avec la commande
```bash
ip -6 address
```

Confirmez que IPv6 fonctionne avec la commande
```bash
ping6 -c 1 www.google.com
```

Votre système est maintenant configuré pour utiliser IPv6.

## Plus d'information

*   de Red Hat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
*   de Red Hat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
*   d'OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)