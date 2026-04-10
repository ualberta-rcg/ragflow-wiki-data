---
title: "Ha fip"
slug: "ha_fip"
lang: "base"

source_wiki_title: "Ha fip"
source_hash: "65587f6f397d986ad3c2877f126c6c54"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:13:13.564975+00:00"

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

## Floating IP High Availability

A single VM hosting an application can fail and be offline, which also makes the application inaccessible.

To avoid such a scenario, it is possible to make the floating IP (FIP) highly available, which in turn can be used to make the application highly available too.

*   206.12.93.117 - Public IP the world is connecting to
*   192.168.27.251 - Internal Virtual IP, owned by the current active system
*   vrrp - Virtual Router Redundancy Protocol, determines the system's status

The two systems communicate via VRRP and determine their status. As long as the **MASTER** system responds, the other system will stay in **BACKUP** mode.

If the **MASTER** system stops responding, the system will change from **BACKUP** into **MASTER** and brings up the internal IP address 192.168.27.251, which it will not be reachable on.

The public IP 206.12.93.117 will always forward any traffic to the VIP. As long as there is a system reachable via the VIP, your application will be reachable.

---

### Active-Passive High-Availability

The scenario in this document describes an **active-passive** system, where one system owns the VIP and receives all the network traffic for that IP address, while the other simply stands by as a backup system if the current active one fails or becomes unreachable.

There are many ways to achieve this goal, and it depends on the desired outcome what needs to be done and configured.

The setup described below will only make sure that a system is reachable via IP. It will not take care of the availability of your application data, such as files, or its services, such as a running web server software.

This example setup will use:

1.  Two VMs hosting the application
2.  One VIP (shared IP) RFC1918 from within your project
3.  One HA Floating IP

Now it is time to build the two VMs and install the application on both systems. This example will only have Nginx running, displaying the default index page and showing that the application is reachable.

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

Once you have chosen an IP address you want to use that is not in the port list, go to **Compute --> Instances** and select the first VM which can later use this VIP.

Select the project's network in the **Interfaces** tab, then use the tab **Allowed Address Pair**.

Enter the VIP you have chosen earlier via the button **Add Allowed Address Pair**.

Repeat the exact same steps on the second server and confirm both have the IP address in the **Allowed Address Pair**.

### Configure Keepalived

Log in to your VM you want to configure as the active system and create the file **/etc/keepalived/keepalived.conf**.

```bash
root@web-srv-1:~# vi /etc/keepalived/keepalived.conf
```

```ini title="/etc/keepalived/keepalived.conf on the active system"
vrrp_instance VI_1 {
    state MASTER #<-- declare the system as the active system
    interface ens3 #<-- NIC of the internal network
    virtual_router_id 50
    priority 100 #<-- higher priority means leading node
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass EcbCp2b1 #<-- generate a new password
    }
    virtual_ipaddress {
      192.168.27.251
    }
    unicast_peer {
        192.168.27.127  #<-- internal IP of the standby system
    }
}
```

```ini title="/etc/keepalived/keepalived.conf on the passive system"
vrrp_instance VI_1 {
    state BACKUP #<-- declare the system as the standby
    interface ens3
    virtual_router_id 50
    priority 50 #<-- lower priority if there is a higher one on the network, the higher one takes precedence.
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass EcbCp2b1
    }
    virtual_ipaddress {
      192.168.27.251
    }
    unicast_peer {
        192.168.27.116  #<--- IP address of the active system
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

!!! note
    VRRP checks if the virtual IP (VIP) is up and reachable. Once it determines that a system has failed and the VIP is unreachable, the designated backup system will activate the VIP and make it available.

When we now start it on the standby node, we will see the same checks, but the VIP will stay on the active system.

---

```bash
root@web-srv-2:~# systemctl stop keepalived
root@web-srv-2:~# systemctl enable --now keepalived
Synchronizing state of keepalived.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable keepalived
root@web-srv-2:~# systemctl status keepalived
• keepalived.service - Keepalive Daemon (LVS and VRRP)
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

To test that the IP is taken over by the standby node, simply stop Keepalived and check that the IP is taken over, either via `ip a s dev ens3` or via the `systemctl status` command.

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

When you start Keepalived again on the first system, it will take over the VIP again. If that is not desired, set the priority to equal numbers.

```console
Jun 28 16:05:54 web-srv-2 systemd[1]: Started keepalived.service - Keepalive Daemon (LVS and VRRP).
Jun 28 16:05:54 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering BACKUP STATE (init)
Jun 28 16:15:04 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering MASTER STATE
Jun 28 16:22:31 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Master received advert from 192.168.27.116 with higher priority 100, ours 50
Jun 28 16:22:31 web-srv-2 Keepalived_vrrp[2238]: (VI_1) Entering BACKUP STATE
```

---

### Allocate HA Floating IP

To bind the floating IP to the VIP address, we need to allocate a port for it.

In **Network --> Networks --> your-projectname-network**, click on **Create Port** in the upper right corner and create the port with the VIP as a fixed address.

Now we are ready to allocate the FIP and associate it with the VIP.

Select the FIP in **Network --> Floating IPs**, click on **Associate** and select the VIP as the port to have the FIP associated with.

Click **Associate** and wait for the **Status** field to show up as **Active**.

Your application and systems are now reachable from any point in the world, assuming your **Security Groups** allow it. You can either shut down a system or simply stop Keepalived on a single system and verify the functionality.