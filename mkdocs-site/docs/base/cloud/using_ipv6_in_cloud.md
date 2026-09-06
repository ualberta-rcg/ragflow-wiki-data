---
title: "Using ipv6 in cloud"
slug: "using_ipv6_in_cloud"
lang: "base"

source_wiki_title: "Using ipv6 in cloud"
source_hash: "c67d1ebb2f1c6ff08a7f2fd928451b8a"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T03:00:49.314255+00:00"

tags:
  - cloud

keywords:
  - "IPv6‑GUA"
  - "attach network interface"
  - "ping6 test"
  - "/dev/eth1 interface"
  - "initial user account"
  - "IPv6 configuration"
  - "Customization Script"
  - "/etc/sysctl.conf"
  - "Configuration Drive"
  - "public key"
  - "Debian instance SSH key problem"
  - "OpenStack security groups"
  - "OpenStack network"
  - "sudo NOPASSWD"
  - "Stateless Address Auto Configuration (SLAAC)"

questions:
  - "How can a user attach an IPv6‑GUA network interface to a VM in Arbutus Cloud using the OpenStack CLI?"
  - "What happens to an IPv6 GUA address when the associated interface is detached, and how does this differ from rebuilding or restarting the VM?"
  - "What steps are required to enable SSH access to a Debian instance launched with an IPv6‑GUA network when the default key‑pair installation fails?"
  - "How can you verify that IPv6 is enabled on the system before configuring the new interface?"
  - "Which kernel parameters and configuration files must be edited to set up the new eth1 interface for IPv6?"
  - "What commands should you run after reboot to confirm that the IPv6 interface is correctly configured and functional?"
  - "What steps must researchers follow in the “Configuration” stage to create an initial user account for a new instance?"
  - "How should the placeholders [username] and [public key] be replaced in the customization script?"
  - "What sudo privileges are granted to the newly created user according to the provided script?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## IPv6 in Arbutus Cloud
IPv6 Link-Local (LLA) and Global Unicast Addresses (GUA) are generally available within the Arbutus cloud environment.
GUA can be set up via a separate interface, which in turn also handles only the IPv6 traffic. Addresses are being set up using *Stateless Address Auto Configuration* (SLAAC), which automatically sets up the IP on the VM interface. By default, the security group rules will allow all outbound traffic from the VM via the IPv6 GUA, but no traffic that originates from outside the VM will be allowed until specific security group rules have been defined. This is the same behaviour as IPv4.

### Example of an OpenStack CLI configuration

Get the ID of the VM to attach the network interface.

```console
openstack server list
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                      | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
```

Assign a new network interface to the VM, using IPv6 as network.

```bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34  IPv6-GUA
```

Check the status of the assignment.

```console
openstack server list
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                                                                       | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
```

### Example of a Web Interface configuration
Log in to the dashboard and go to the *Instances* menu, click on *Attach Interface*, which will open a dialogue. Use IPv6-GUA (2607:f8f0:c11:7004::/64) from the network menu and click on *Attach*.

The IPv6 address is now available and can be used until the interface is detached. Every time the interface is detached, the GUA is released and returned to the pool, where it can be used by anyone else. Rebuilding or restarting the VM, however, will not release the GUA.

Access from any IPv6 GUA can be granted via *Security Groups* in OpenStack; the only difference is the CIDR, which automatically detects the address type.

### Example of a Debian Instance
When researchers launch an instance with the Debian operating system with the IPv6 network (i.e., IPv6-GUA), the selected SSH key pair will not install successfully. As a result, the researchers cannot ssh into the instance and will receive a “Permission Denied” error message instead. To work around the problem, when researchers are launching a new instance, they can create an initial user account by completing the following steps:

1. Go to the "Configuration" step.
2. Add the following script to the "Customization Script". Replace `[username]` with the researcher's preferred username and `[public key]` with the user's public key.
3. Select "Configuration Drive".

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

## Example of a Linux configuration

The OpenStack network you configured above will appear in Linux as an additional eth-type interface. In most cases, `/dev/eth0` will be your existing interface. In most cases, your new IPv6 enabled interface will be `/dev/eth1`. The easiest way to pick up your new device is to reboot. But first, check to confirm that IPv6 is enabled with this command:

```bash
sudo sysctl -a | grep ipv6.*disable
```
The output should all end in zeros. IPv6 enabled is the default in all recent images. Any kernel parameters that need to be changed to zero should be added to `/etc/sysctl.conf`.

Also, add the following kernel parameters in `/etc/sysctl.conf`:

```ini
net.ipv6.conf.eth1.forwarding=0
net.ipv6.conf.eth1.accept_ra=1
```

Reboot your system and confirm IPv6 is enabled and that `/dev/eth1` exists.

Next, add the following configurations to `/etc/sysconfig/network-scripts/ifcfg-eth1`:

```ini
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
```

Reboot your system again. The `/dev/eth1` interface should be configured and ready to be used.

You may then confirm the IPv6 configuration with:

```bash
ip -6 address
```

Finally, confirm that IPv6 is working with:

```bash
ping6 -c 1 www.google.com
```

That's all. Congratulations. Your system is now configured to use IPv6.

## Further Reading
* From Red Hat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
* From Red Hat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
* From OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)