---
title: "Using ipv6 in cloud/en"
slug: "using_ipv6_in_cloud"
lang: "en"

source_wiki_title: "Using ipv6 in cloud/en"
source_hash: "ff3afdb814fba370e547acf95cf2bc6e"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:55:50.420626+00:00"

tags:
  - cloud

keywords:
  - "IPv6"
  - "Launch Instance"
  - "SSH key permission denied"
  - "IPv6 GUA"
  - "SLAAC"
  - "OpenStack security groups"
  - "sudo NOPASSWD"
  - "ifcfg-eth1"
  - "Customization Script"
  - "attach network interface"
  - "sysctl.conf"
  - "Cloud Quick Start Guide"
  - "Configuration Drive"
  - "/dev/eth1"
  - "ping6"

questions:
  - "How can a VM be assigned an IPv6 Global Unicast Address (GUA) using the OpenStack CLI in Arbutus Cloud?"
  - "What occurs to an IPv6 GUA when its interface is detached, and how does this differ from rebuilding or restarting the VM?"
  - "Why do Debian or Ubuntu 26.04 instances launched with the IPv6‑GUA network fail to install the SSH key pair, and what workaround is recommended?"
  - "How can you verify that IPv6 is enabled on the Linux system before configuring the new interface?"
  - "Which kernel parameters must be added to /etc/sysctl.conf for the new eth1 interface, and what values should they have?"
  - "What are the required changes to /etc/sysconfig/network-scripts/ifcfg-eth1 to enable and activate IPv6 on eth1?"
  - "What are the steps to launch a new virtual machine instance according to the guide?"
  - "How should the customization script be written, and which placeholders need to be replaced with the researcher’s information?"
  - "Why is it necessary to select “Configuration Drive” when configuring the instance?"

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
```

| ID                                   | Name | Status | Networks                                      | Image                            | Flavor   |
| :----------------------------------- | :--- | :----- | :-------------------------------------------- | :------------------------------- | :------- |
| 74be352d-19ca-46cc-9661-7088d2652e34 | test | ACTIVE | def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |

Assign a new network interface to the VM, using IPv6 as the network.

```bash
openstack server add network 74be352d-19ca-46cc-9661-7088d2652e34 IPv6-GUA
```

Check the status of the assignment.

```bash
openstack server list
```

| ID                                   | Name | Status | Networks                                                                                       | Image                            | Flavor   |
| :----------------------------------- | :--- | :----- | :--------------------------------------------------------------------------------------------- | :------------------------------- | :------- |
| 74be352d-19ca-46cc-9661-7088d2652e34 | test | ACTIVE | IPv6-GUA=2607:f8f0:c11:7004:f816:3eff:fef1:8cee; def-bott-network=192.168.27.140, 206.12.93.29 | Debian-10.9.2-Buster-x64-2021-05 | p1-1.5gb |

### Example of a Web Interface Configuration

Log into the dashboard and go to the *Instances* menu. Click on *Attach Interface*, which will open a dialogue. Use `IPv6-GUA` (2607:f8f0:c11:7004::/64) from the network menu and click on *Attach*. This process will add the IPv6 interface.

The assigned IPv6 address is now available and can be used until the interface is detached. Every time the interface is detached, the GUA is released and returned to the pool, and thus, can be used by anyone else. Rebuilding or restarting the VM, however, will not release the GUA.

Access from any IPv6 GUA can be granted via *Security Groups* in OpenStack; the only difference is the CIDR, which automatically detects the address type. For example, to allow ICMP from any IPv6 GUA, a security group rule would be configured accordingly.

### Example of a Debian or Ubuntu 26.04 Instance

!!! warning "SSH Key Installation Issue with Debian or Ubuntu 26.04"
    When researchers launch an instance with the Debian or Ubuntu 26.04 operating system with the IPv6 network (i.e., IPv6-GUA), the selected SSH key pair will not install successfully. As a result, researchers cannot SSH into the instance and will receive a **Permission Denied** error message instead.

    To work around this problem, when launching a new instance, create an initial user account by completing the following steps:

1.  To create a virtual machine, select *Compute* -> *Instances* on the left menu, then click on the *Launch Instance* button.
2.  Follow the [Cloud Quick Start Guide](cloud_quick_start.md) to complete the displayed form where you define your virtual machine.
3.  Select *Configuration* in the left menu.
4.  Add the following script to the *Customization Script*. Replace `[username]` with the researcher's preferred username and `[public key]` with the user's public key.
5.  Select *Configuration Drive*.

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

The OpenStack network you configured above will appear in Linux as an additional `eth`-type interface. In most cases, `/dev/eth0` will be your existing interface. In most cases, your new IPv6-enabled interface will be `/dev/eth1`. The easiest way to pick up your new device is to reboot. But first, check to confirm that IPv6 is enabled with this command:

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
* From RedHat, [What you need to know about IPv6](https://www.redhat.com/sysadmin/what-you-need-know-about-ipv6)
* From RedHat, [Configuring an IPv6 address in Red Hat Enterprise Linux 7 and 8](https://www.redhat.com/sysadmin/configuring-ipv6-rhel-7-8)
* From OpenStack, [IPv6](https://docs.openstack.org/neutron/pike/admin/config-ipv6.html)