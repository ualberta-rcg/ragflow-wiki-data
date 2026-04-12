---
title: "Using ipv6 in cloud"
slug: "using_ipv6_in_cloud"
lang: "base"

source_wiki_title: "Using ipv6 in cloud"
source_hash: "61c4adc4785c397e667841d3d45a327b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:24:08.640242+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "IPv6 enabled"
  - "Global Unicast Addresses"
  - "Network interface"
  - "Arbutus Cloud"
  - "IPv6"
  - "eth1"
  - "network-scripts"
  - "sysctl"
  - "configuration"
  - "kernel parameters"
  - "/etc/sysctl.conf"
  - "Red Hat"
  - "/dev/eth1"

questions:
  - "How are IPv6 Global Unicast Addresses (GUA) automatically configured and handled by default security group rules in the Arbutus cloud environment?"
  - "What are the steps to attach an IPv6 network interface to a VM, and what happens to the assigned GUA when the interface is detached compared to when the VM is restarted?"
  - "How can a user verify that IPv6 is enabled at the operating system level on a Linux virtual machine after attaching the new interface?"
  - "What initial system configurations must be applied to enable IPv6 on the eth1 interface?"
  - "Which parameters need to be added to the ifcfg-eth1 network script to ensure IPv6 initializes correctly?"
  - "What commands should be used to verify the IPv6 address configuration and test network connectivity?"
  - "What is the typical device name for a newly enabled IPv6 interface, and what is the easiest way to initialize it?"
  - "Which command is used to verify that IPv6 is enabled on the system, and what is the expected output?"
  - "In which configuration file should any necessary kernel parameter changes be saved?"
  - "What initial system configurations must be applied to enable IPv6 on the eth1 interface?"
  - "Which parameters need to be added to the ifcfg-eth1 network script to ensure IPv6 initializes correctly?"
  - "What commands should be used to verify the IPv6 address configuration and test network connectivity?"

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

Assign a new network interface to the VM, using IPv6 as network.

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

Log in to the dashboard and go to the *Instances* menu, click on *Attach Interface*, which will open a dialogue. Use IPv6-GUA (2607:f8f0:c11:7004::/64) from the network menu and click on *Attach*.

!!! note "IPv6 GUA Persistence"
    The shown IPv6 address is now available and can be used until the interface is detached. Every time the interface is detached, the GUA is released and put back into the pool and thus, can be used by anyone else. Rebuilding or restarting the VM however, will not release the GUA.

Access from any IPv6 GUA can be granted via *Security Groups* in OpenStack; the only difference is the CIDR which automatically detects the address type.

## Example of a Linux Configuration

The OpenStack network you configured above will appear in Linux as an additional eth-type interface. In most cases, `/dev/eth0` will be your existing interface. In most cases, your new IPv6 enabled interface will be `/dev/eth1`. The easiest way to pick up your new device is to reboot. But first, check to confirm that IPv6 is enabled with this command:

```bash
sudo sysctl -a | grep ipv6.*disable
```

The output should all end in zeros. IPv6 enabled is the default in all recent images. Any kernel parameters that need to be changed to zero should be added to `/etc/sysctl.conf`.

Also, add the following kernel parameters in `/etc/sysctl.conf`:

```text
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

*   From Red Hat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
*   From Red Hat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
*   From OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)