---
title: "Using ipv6 in cloud/en"
slug: "using_ipv6_in_cloud"
lang: "en"

source_wiki_title: "Using ipv6 in cloud/en"
source_hash: "e354088fe4dec89951d2af1a3665212c"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:31:29.522858+00:00"

tags:
  - cloud

keywords:
  - "OpenStack server add network"
  - "IPv6 configuration"
  - "shell: /bin/bash"
  - "sysctl.conf"
  - "Security Groups"
  - "ping6"
  - "net.ipv6.conf.eth1"
  - "OpenStack network"
  - "IPv6 GUA"
  - "ssh_authorized_keys"
  - "IPv6 enabled interface"
  - "lock_passwd"
  - "ifcfg-eth1"
  - "Stateless Address Auto Configuration (SLAAC)"
  - "Debian instance SSH key issue"

questions:
  - "How can a user attach an IPv6‑GUA network interface to a VM using the OpenStack CLI in Arbutus Cloud?"
  - "What steps are required to enable SSH access to a Debian instance with an IPv6‑GUA network when the default key pair installation fails?"
  - "How do security group rules control inbound and outbound IPv6 traffic for VMs in the Arbutus Cloud environment?"
  - "Which kernel parameters should be set to zero in /etc/sysctl.conf to ensure IPv6 is enabled?"
  - "What specific settings must be added to /etc/sysconfig/network-scripts/ifcfg-eth1 to activate IPv6 on the eth1 interface?"
  - "Which commands can you use to confirm that IPv6 is configured correctly and operational after rebooting?"
  - "What does the `lock_passwd: true` setting do in the provided cloud‑init configuration, and why might `ssh_pwauth` be set to false?"
  - "How does the screenshot labeled “Allow icmp from any IPv6 GUA” relate to the network security policy for IPv6 traffic?"
  - "According to the example, which steps should be taken to verify that the newly added IPv6‑enabled interface (typically `/dev/eth1`) is correctly recognized after configuring OpenStack networking?"

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
GUA can be set up via a separate interface, which in turn also handles only the IPv6 traffic.
Addresses are being set up using *Stateless Address Auto Configuration* (SLAAC), which automatically sets up the IP on the VM interface. By default, the security group rules will allow all outbound traffic from the VM via the IPv6 GUA, but no traffic that originates from outside the VM will be allowed until specific security group rules have been defined. This is the same behaviour as IPv4.

### Example of an OpenStack CLI Configuration

Get the ID of the VM to attach the network interface.

```bash
openstack server list
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                      | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+-----------------------------------------------+----------------------------------+----------+
```

Assign a new network interface to the VM, using IPv6 as the network.

```bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34  IPv6-GUA
```

Check the status of the assignment.

```bash
openstack server list
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| ID                                   | Name            | Status  | Networks                                                                                       | Image                            | Flavor   |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
| 74be352d-19ca-46cc-9661-7088d2652e34 | test            | ACTIVE  | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |
+--------------------------------------+-----------------+---------+------------------------------------------------------------------------------------------------+----------------------------------+----------+
```

### Example of a Web Interface Configuration
Log in to the dashboard and go to the *Instances* menu, click on *Attach Interface*, which will open a dialogue.
Use IPv6-GUA (2607:f8f0:c11:7004::/64) from the network menu and click on *Attach*.

The IPv6 address for the attached interface is now available and can be used until the interface is detached. Every time the interface is detached, the GUA is released and put back into the pool and thus, can be used by anyone else. Rebuilding or restarting the VM, however, will not release the GUA.

Access from any IPv6 GUA can be granted via *Security Groups* in OpenStack; the only difference is the CIDR which automatically detects the address type.

### Example of a Debian Instance

!!! warning "Debian Instance SSH Key Issue"
    When researchers launch an instance with the Debian operating system with the IPv6 network (i.e., IPv6-GUA), the selected SSH key pair will not install successfully. As a result, users cannot SSH into the instance and will receive a "Permission Denied" error message. To work around this problem, when launching a new instance, create an initial user account by completing the following steps:

1.  Go to the "Configuration" step.
2.  Add the following script to the "Customization Script". Replace `[username]` with your preferred username and `[public key]` with your public key.
3.  Select "Configuration Drive".

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

## Example of a Linux Configuration

The OpenStack network you configured above will appear in Linux as an additional eth-type interface. In most cases, `/dev/eth0` will be your existing interface. In most cases, your new IPv6 enabled interface will be `/dev/eth1`. The easiest way to pick up your new device is to reboot. But first, check to confirm that IPv6 is enabled with this command:

```bash
sudo sysctl -a | grep ipv6.*disable
```

The output should all end in zeros. IPv6 enabled is the default in all recent images. Any kernel parameters that need to be changed to zero should be added to `/etc/sysctl.conf`.

Also, add the following kernel parameters in `/etc/sysctl.conf`:

```sysctl
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
*   From RedHat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
*   From RedHat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
*   From OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)