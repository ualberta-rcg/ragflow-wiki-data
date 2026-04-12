---
title: "Ha fip"
slug: "ha_fip"
lang: "base"

source_wiki_title: "Ha fip"
source_hash: "65587f6f397d986ad3c2877f126c6c54"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:54:14.968603+00:00"

tags:
  []

keywords:
  - "standby node"
  - "keepalived.conf"
  - "Floating IP High Availability"
  - "virtual IP"
  - "failover"
  - "systemctl"
  - "vrrp_instance"
  - "leading node"
  - "ens3"
  - "High Availability"
  - "Virtual IP"
  - "keepalived"
  - "standby system"
  - "virtual_ipaddress"
  - "Floating IP"
  - "VIP"
  - "Active-Passive"
  - "VRRP"
  - "active/standby system"
  - "IP takeover"

questions:
  - "How does the active-passive high availability setup utilize VRRP and a Virtual IP to ensure an application remains accessible if the primary virtual machine fails?"
  - "What are the limitations of this specific high availability configuration regarding application data synchronization and service-level monitoring?"
  - "What are the key differences in the keepalived configuration files between the active (MASTER) and passive (BACKUP) systems?"
  - "What network security configuration must be verified to allow proper VRRP communication between the systems?"
  - "How can an administrator verify that the virtual IP address has been successfully assigned to the active node's network interface?"
  - "What is the process for testing the failover functionality to ensure the standby node takes over the virtual IP?"
  - "How does the configuration determine which node acts as the leading system versus the standby system?"
  - "What is the purpose of the virtual_ipaddress and unicast_peer directives in this setup?"
  - "How is the communication between the active and passive systems secured according to the configuration?"
  - "How can you test if an IP address has been successfully taken over by a standby node?"
  - "What specific command is used to stop the keepalived service and trigger the failover process?"
  - "Which commands are recommended to verify the network interface status and confirm the IP takeover?"
  - "How does the keepalived service manage Virtual IP (VIP) failover between systems, and how can priority settings be adjusted to prevent automatic fallback?"
  - "What are the specific steps required to create a port for the VIP and associate a High Availability Floating IP (FIP) with it?"
  - "How can an administrator test the high availability setup to ensure the application remains reachable after configuring the Floating IP?"
  - "How does the keepalived service manage Virtual IP (VIP) failover between systems, and how can priority settings be adjusted to prevent automatic fallback?"
  - "What are the specific steps required to create a port for the VIP and associate a High Availability Floating IP (FIP) with it?"
  - "How can an administrator test the high availability setup to ensure the application remains reachable after configuring the Floating IP?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Floating IP High Availability

A single VM hosting an application can fail and be offline, which also makes the application inaccessible.

To avoid such a scenario, it is possible to make the floating IP (FIP) high-available, which in turn can be used to make the application highly available too.

*   206.12.93.117 - Public IP the world is connecting to
*   192.168.27.251 - Internal Virtual IP, owned by the current active system
*   vrrp - Virtual Router Redundancy Protocol, determines the systems' status

The two systems communicate via VRRP and determine their status. As long as the **MASTER** system responds, the other system will stay in **BACKUP** mode.

If the **MASTER** system stops responding, the system will change from **BACKUP** into **MASTER** and bring up the internal IP address 192.168.27.251, which it will then be reachable on.

The public IP 206.12.93.117 will always forward any traffic to the VIP. As long as there is a system reachable via the VIP, your application will be reachable.

---

### Active-Passive High-Availability

The scenario in this document describes an *active-passive* system, where one system owns the VIP and receives all the network traffic for that IP address, while the other one simply stands by as a backup system if the current active one fails or becomes unreachable.

There are many ways to achieve this goal, and it depends on the desired outcome what needs to be done and configured.

!!! warning
    The setup described below will only make sure that a system is reachable via IP. It will not take care of the availability of your application data, such as files, or its services, such as a running web server software.

This example setup will use:

1.  Two VMs hosting the application
2.  One VIP (shared IP) RFC1918 from within your project
3.  One HA Floating IP

Now it is time to build the two VMs and install the application on both systems. This example here will only have Nginx running, displaying the default index page and showing that the application is reachable.

---

### Step 1: Installing Nginx and Keepalived

After successfully building the two VMs, which will share the internal VIP, install Nginx and Keepalived.

```bash
root@web-srv-1:~# apt-get update && apt-get -y dist-upgrade && apt-get install -y nginx keepalived
[...]
root@web-srv-2:~# apt-get update && apt-get -y dist-upgrade && apt-get install -y nginx keepalived
[...]
```

---

### Step 2: Allocating an Internal VIP

IP addresses are unique identifiers, which is true within an internal, private network too. Therefore, we have to make sure to select a VIP which is not already used.

In the left menu, go to **Network --> Networks --> your-projectname-network**.

Select **Ports** in the upper tab.

The network range in the example is from 192.168.27.1-254; all currently allocated addresses are listed in this port list.

Once you have chosen an IP address you want to use and which is not in the port list, go to **Compute --> Instances** and select the first VM which can later use this VIP.

Select the project's network in the **Interfaces** tab, then use the tab **Allowed Address Pair**.

Enter the VIP you chose earlier via the button **Add Allowed Address Pair**.

Repeat the exact same steps on the second server and confirm both have the IP address in the **Allowed Address Pair**.

### Configure Keepalived

Log in to your VM you want to configure as the active system and create the file `/etc/keepalived/keepalived.conf`.

```bash
root@web-srv-1:~# vi /etc/keepalived/keepalived.conf
```

*/etc/keepalived/keepalived.conf* on the active system:

```ini
vrrp_instance VI_1 {
    state MASTER # declare the system as the active system
    interface ens3 # NIC of the internal network
    virtual_router_id 50
    priority 100 # higher priority means leading node
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass EcbCp2b1 # generate a new password
    }
    virtual_ipaddress {
      192.168.27.251
    }
    unicast_peer {
        192.168.27.127  # internal IP of the standby system
    }
}
```

*/etc/keepalived/keepalived.conf* on the passive system:

```ini
vrrp_instance VI_1 {
    state BACKUP # declare the system as the standby
    interface ens3
    virtual_router_id 50
    priority 50 # lower priority if there is a higher one on the network, the higher one takes precedence.
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass EcbCp2b1
    }
    virtual_ipaddress {
      192.168.27.251
    }
    unicast_peer {
        192.168.27.116  # IP address of the active system
    }
}
```

Make sure you allow the VRRP traffic between the systems in your **Security Groups** and ensure it is attached to your systems.

Now it is time to start Keepalived and check its functionality.

```bash
root@web-srv-1:~# systemctl enable --now keepalived
Synchronizing state of keepalived.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable keepalived

root@web-srv-1:~# ip a s dev ens3
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:3e:23:46 brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 192.168.27.116/24 metric 100 brd 192.168.27.255 scope global dynamic ens3
       valid_lft 82678sec preferred_lft 82678sec
    inet 192.168.27.251/32 scope global ens3 <------
       valid_lft forever preferred_lft forever
    inet6 fe80::f816:3eff:fe3e:2346/64 scope link
       valid_lft forever preferred_lft forever
```

VRRP checks if the IP is up and reachable. Once it finds out that the standby system does not respond and the IP is unreachable, it starts it and makes it available.

When we now start it on the standby node, we will see the same checks, but the VIP will stay on the active system.

---

```bash
root@web-srv-2:~# systemctl stop keepalived
root@web-srv-2:~# systemctl enable --now keepalived
Synchronizing state of keepalived.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable keepalived
root@web-srv-2:~# systemctl status keepalived
● keepalived.service - Keepalive Daemon (LVS and VRRP)
     Loaded: loaded (/lib/systemd/system/keepalived.service; enabled; preset: enabled)
    [....]

Jun 28 16:05:54 web-srv-2 Keepalived[2237]: Startup complete
Jun 28 16:05:54 web-srv-2 systemd[1]: Started keepalived.service - Keepalive Daemon (LVS and VRRP).
Jun 28 16:05:54 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering BACKUP STATE (init)

root@web-srv-2:~# ip a s dev ens3
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:8f:c6:ed brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 192.168.27.127/24 metric 100 brd 192.168.27.255 scope global dynamic ens3
       valid_lft 80957sec preferred_lft 80957sec
    inet6 fe80::f816:3eff:fe8f:c6ed/64 scope link
       valid_lft forever preferred_lft forever
```

To test that the IP is taken over by the standby node, simply stop Keepalived and check that the IP is taken over, either via **ip a s dev ens3** or via the `systemctl status` command.

Active system:
```bash
root@web-srv-1:~# systemctl stop keepalived
root@web-srv-1:~# ip a s dev ens3
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:3e:23:46 brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 192.168.27.116/24 metric 100 brd 192.168.27.255 scope global dynamic ens3
       valid_lft 82242sec preferred_lft 82242sec
    inet6 fe80::f816:3eff:fe3e:2346/64 scope link
       valid_lft forever preferred_lft forever
```

Passive system (now owns the VIP):
```bash
root@web-srv-2:~# ip a s dev ens3
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:8f:c6:ed brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 192.168.27.127/24 metric 100 brd 192.168.27.255 scope global dynamic ens3
       valid_lft 80346sec preferred_lft 80346sec
    inet 192.168.27.251/32 scope global ens3
       valid_lft forever preferred_lft forever
    inet6 fe80::f816:3eff:fe8f:c6ed/64 scope link
       valid_lft forever preferred_lft forever
```

When you start Keepalived again on the first system, it will take the VIP over again. If that is not desired, set the priority to equal numbers.

```bash
Jun 28 16:05:54 web-srv-2 systemd[1]: Started keepalived.service - Keepalive Daemon (LVS and VRRP).
Jun 28 16:05:54 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering BACKUP STATE (init)
Jun 28 16:15:04 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering MASTER STATE
Jun 28 16:22:31 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Master received advert from 192.168.27.116 with higher priority 100, ours 50
Jun 28 16:22:31 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering BACKUP STATE
```

---

### Allocate HA Floating IP

To bind the floating IP to the VIP address, we need to allocate a port for it.

In **Network --> Networks --> your-projectname-network**, click on **Create Port** in the upper right corner and create the port with the VIP as the fixed address.

Now we are ready to allocate the FIP and associate it with the VIP.

Select the FIP in **Network --> Floating IPs**, click on **Associate** and select the VIP as the port to have the FIP associated with.

Click associate and wait for the **Status** field to show up as **Active**.

Your application and systems are now reachable from any point in the world, assuming your **Security Groups** allow it. You can either shut down a system or simply stop Keepalived on a single system and verify the functionality.