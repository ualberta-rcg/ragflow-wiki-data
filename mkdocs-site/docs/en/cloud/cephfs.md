---
title: "CephFS/en"
slug: "cephfs"
lang: "en"

source_wiki_title: "CephFS/en"
source_hash: "037ad1071d1298f1fd9551bc0b95d355"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:12:48.655719+00:00"

tags:
  - cloud

keywords:
  - "repository"
  - "user space"
  - "booted from volume"
  - "namespace option"
  - "Access rule"
  - "CephFS client"
  - "VM configuration"
  - "lsb_release"
  - "Virtual Machine"
  - "prune-dtn1"
  - "OpenStack"
  - "fstab"
  - "ceph-fuse"
  - "ha4-15gb"
  - "device path"
  - "nofail option"
  - "CephFS service"
  - "Red Hat family"
  - "ceph.keyring"
  - "Ceph"
  - "ceph.conf"
  - "CephFS"
  - "apt-add-repository"
  - "mount options"
  - "Share configuration"
  - "OpenStack cluster"
  - "ACTIVE"
  - "distro codename"
  - "ceph client"
  - "test_network"
  - "mount"
  - "Debian family"

questions:
  - "What information must be provided when requesting a CephFS quota from the cloud support team?"
  - "What are the steps and required parameters to create a new CephFS share and its corresponding access rule in the OpenStack interface?"
  - "How does the process of attaching the CephFS network to a virtual machine differ between the Arbutus and SD4H/Juno environments?"
  - "What is the name and current operational status of the instance?"
  - "What are the specific IP addresses and network assigned to this server?"
  - "How is the instance booted, and what hardware flavor does it use?"
  - "How can you attach the CephFS network to a specific Virtual Machine using OpenStack CLI commands?"
  - "What repository configurations and packages are required to install the CephFS client on Red Hat family distributions like Enterprise Linux 9?"
  - "How do you add the correct Ceph repository for Debian family distributions using the distribution's codename?"
  - "What packages must be installed to set up the CephFS client and its dependencies?"
  - "Where can a user find the monitor information, client name, and access key required to configure the ceph.conf and ceph.keyring files?"
  - "How do you permanently mount the CephFS device using the /etc/fstab file, and what specific syntax or options are required?"
  - "How can a user find their Linux distribution's codename according to the text?"
  - "What bash command is provided to add the Ceph 'debian-tentacle' repository?"
  - "How should a user revert the repository addition if the initial command produces an error?"
  - "What are the specific command-line differences when mounting CephFS directly on Arbutus compared to SD4H/Juno?"
  - "What steps and configuration changes are required to mount CephFS in user space using ceph-fuse?"
  - "How can granular access control be implemented for a shared filesystem, and what are the network limitations for accessing this service?"
  - "Why is there a non-standard colon before the device path in the configuration?"
  - "What is the required mount option for SD4H/Juno systems, and what are the other options used for?"
  - "How does the nofail option protect the system's boot process if the CephFS service is unreachable?"
  - "What are the specific command-line differences when mounting CephFS directly on Arbutus compared to SD4H/Juno?"
  - "What steps and configuration changes are required to mount CephFS in user space using ceph-fuse?"
  - "How can granular access control be implemented for a shared filesystem, and what are the network limitations for accessing this service?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

CephFS provides a common filesystem that can be shared amongst multiple OpenStack VM hosts. Access to the service is granted via requests to [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).

This is a fairly technical procedure that assumes basic Linux skills for creating/editing files, setting permissions, and creating mount points. For assistance in setting up this service, write to [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).

## Procedure

## Request access to shares

If you do not already have a quota for the service, you will need to request this through [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca). In your request please provide the following:
* OpenStack project name
* amount of quota required (in GB)
* number of shares required

## OpenStack configuration: Create a CephFS share

**Create the share:**
In *Project* --> *Share* --> *Shares*, click on *+Create Share*.
*Share Name* = enter a name that identifies your project (e.g. *project-name-shareName*)
*Share Protocol* = CephFS
*Size* = size you need for this share
*Share Type* = cephfs (or cephfs-ec42 on SD4H/Juno)
*Availability Zone* = nova
Do not check *Make visible for all* (or *Make visible to users from all projects* on SD4H/Juno), otherwise the share will be accessible by all users in all projects.
Click on the *Create* button.

**Create an access rule to generate an access key:**
In *Project* --> *Share* --> *Shares* --> *Actions* column, select *Manage Rules* from the drop-down menu.
Click on the *+Add Rule* button (right of the page).
*Access Type* = cephx
*Access Level* = select *read-write* or *read-only* (you can create multiple rules for either access level if required)
*Access To* = select a key name that describes the key. This name is important because it will be used in the CephFS client configuration on the VM; on this page, we use *MyCephFS-RW*.

**Note the share details which you will need later:**
In *Project* --> *Share* --> *Shares*, click on the name of the share.
In the *Share Overview*, note the three elements circled in red in the image above: *Path*, which will be used in the mount command on the VM; the *Access to*, which will be the client name; and the *Access Key* that will let the VM's client connect.

## Attach the CephFS network to your VM

### On Arbutus

On `Arbutus`, the CephFS network is already exposed to your VM; there is nothing to do here, **[go to the VM configuration section](#vm-configuration-install-and-configure-cephfs-client)**.

### On SD4H/Juno

On `SD4H/Juno`, you need to explicitly attach the CephFS network to the VM.

**With the Web GUI:**
For each VM you need to attach, select *Instance* --> *Action* --> *Attach interface*, select the CephFS-Network, leave the *Fixed IP Address* box empty.

**With the [OpenStack client](openstack-command-line-clients.md):**
List the servers and select the ID of the server you need to attach to the CephFS.

```bash
$ openstack server list
+--------------------------------------+--------------+--------+-------------------------------------------+--------------------------+----------+
| ID                                   | Name         | Status | Networks                                  | Image                    | Flavor   |
+--------------------------------------+--------------+--------+-------------------------------------------+--------------------------+----------+
| 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 | prune-dtn1   | ACTIVE | test_network=172.16.1.86, 198.168.189.3   | N/A (booted from volume) | ha4-15gb |
| 0c6df8ea-9d6a-43a9-8f8b-85eb64ca882b | prune-mgmt1  | ACTIVE | test_network=172.16.1.64                  | N/A (booted from volume) | ha4-15gb |
| 2b7ebdfa-ee58-4919-bd12-647a382ec9f6 | prune-login1 | ACTIVE | test_network=172.16.1.111, 198.168.189.82 | N/A (booted from volume) | ha4-15gb |
+--------------------------------------+--------------+--------+----------------------------------------------+--------------------------+----------+
```

Select the ID of the VM you want to attach; we will pick the first one here and run:

```bash
$ openstack server add network 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 CephFS-Network
$ openstack server list
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| ID                                   | Name         | Status | Networks                                                            | Image                    | Flavor   |
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 | prune-dtn1   | ACTIVE | CephFS-Network=10.65.20.71; test_network=172.16.1.86, 198.168.189.3 | N/A (booted from volume) | ha4-15gb |
| 0c6df8ea-9d6a-43a9-8f8b-85eb64ca882b | prune-mgmt1  | ACTIVE | test_network=172.16.1.64                                            | N/A (booted from volume) | ha4-15gb |
| 2b7ebdfa-ee58-4919-bd12-647a382ec9f6 | prune-login1 | ACTIVE | test_network=172.16.1.111, 198.168.189.82                           | N/A (booted from volume) | ha4-15gb |
+--------------------------------------+--------------+--------+------------------------------------------------------------------------+--------------------------+----------+
```

We can see that the CephFS network is attached to the first VM.

## VM configuration: Install and configure CephFS client

### Required packages for the Red Hat family (RHEL, CentOS, Fedora, Rocky, Alma)

Check the available releases at [https://download.ceph.com/](https://download.ceph.com/) and look for recent `rpm-*` directories.
As of April 2026, `tentacle` is the latest stable release.
The compatible distributions (distros) are listed at [https://download.ceph.com/rpm-tentacle/](https://download.ceph.com/rpm-tentacle/).
Here we show configuration examples for `Enterprise Linux 9`.

**Install relevant repositories for access to Ceph client packages:**

```ini title="/etc/yum.repos.d/ceph.repo"
[Ceph]
name=Ceph packages for $basearch
baseurl=http://download.ceph.com/rpm-tentacle/el9/$basearch
enabled=1
gpgcheck=1
type=rpm-md
gpgkey=https://download.ceph.com/keys/release.asc

[Ceph-noarch]
name=Ceph noarch packages
baseurl=http://download.ceph.com/rpm-tentacle/el9/noarch
enabled=1
gpgcheck=1
type=rpm-md
gpgkey=https://download.ceph.com/keys/release.asc

[ceph-source]
name=Ceph source packages
baseurl=http://download.ceph.com/rpm-tentacle/el9/SRPMS
enabled=1
gpgcheck=1
type=rpm-md
gpgkey=https://download.ceph.com/keys/release.asc
```

The EPEL repo also needs to be in place:
```bash
sudo dnf install epel-release
```

You can now install the Ceph lib, CephFS client, and other dependencies:
```bash
sudo dnf install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

### Required packages for the Debian family (Debian, Ubuntu, Mint, etc.)

You can get the repository once you have figured out your distro `{codename}` with `lsb_release -sc`:
```bash
sudo apt-add-repository 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```
If the previous command gave an error, revert it with the following command and go to the next step:
```bash
sudo add-apt-repository -r 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```

You can now install the Ceph lib, CephFS client, and other dependencies:
```bash
sudo apt-get install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

### Configure Ceph client

Once the client is installed, you can create a `ceph.conf` file.
Note the different `mon host` for the different cloud.

=== "Arbutus"

    ```ini title="/etc/ceph/ceph.conf"
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = [v2:134.87.15.61:3300/0,v1:134.87.15.61:6789/0] [v2:134.87.15.62:3300/0,v1:134.87.15.62:6789/0] [v2:134.87.15.63:3300/0,v1:134.87.15.63:6789/0]
    [client]
    quota = true
    ```

=== "SD4H/Juno"

    ```ini title="/etc/ceph/ceph.conf"
    [global]
    admin socket = /var/run/ceph/$cluster-$name-$pid.asok
    client reconnect stale = true
    debug client = 0/2
    fuse big writes = true
    mon host = 10.65.0.10:6789,10.65.0.12:6789,10.65.0.11:6789
    [client]
    quota = true
    ```

You can find the monitor information in the share details *Path* field that will be used to mount the volume. If the value of the web page is different than what is seen here, it means that the wiki page is out of date.

You also need to put your client name and secret in the `ceph.keyring` file:

```ini title="/etc/ceph/ceph.keyring"
[client.MyCephFS-RW]
    key = <Access Key>
```

Again, the access key and client name (here MyCephFS-RW) are found under the access rules on your project web page.
Look for *Project* --> *Share* --> *Shares*, then click on the name of the share.

**Retrieve the connection information from the share page for your connection:**
* Open up the share details by clicking on the name of the share in the *Shares* page.
* Copy the portion of the *Path* of the share that starts with `:` which we will use to mount the filesystem (for example `:/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c`, is used here).

**Mount the filesystem:**
* Create a mount point directory somewhere in your host (`/cephfs`, is used here):
    ```bash
    mkdir /cephfs
    ```
* You can use the Ceph driver to permanently mount your CephFS device by adding the following in the VM fstab:

=== "Arbutus"

    ```text title="/etc/fstab"
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,nofail 0  2
    ```

=== "SD4H/Juno"

    ```text title="/etc/fstab"
    :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw,nofail 0  2
    ```

!!! note
    Notice the non-standard `:` before the device path. It is not a typo!
    The mount options are different on different systems.
    The namespace option is required for SD4H/Juno, while other options are performance tweaks. The `nofail` option ensures that the system will boot even in the unlikely case that the CephFS service is down or unreachable.

You can also do the mount directly from the command line:

=== "Arbutus"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW
    ```

=== "SD4H/Juno"

    ```bash
    sudo mount -t ceph :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ -o name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw
    ```

CephFS can also be mounted directly in user space via `ceph-fuse`.

Install the `ceph-fuse` lib:
```bash
sudo dnf install ceph-fuse
```
Let the FUSE mount be accessible in user space by uncommenting `user_allow_other` in the `fuse.conf` file:

```text title="/etc/fuse.conf"
# mount_max = 1000
user_allow_other
```

You can now mount CephFS in a user’s home:
```bash
mkdir ~/my_cephfs
ceph-fuse my_cephfs/ --id=MyCephFS-RW --conf=~/ceph.conf --keyring=~/ceph.keyring   --client-mountpoint=/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c
```
Note that the client name is here the `--id`. The `ceph.conf` and `ceph.keyring` content are exactly the same as for the Ceph kernel mount.

## Notes

A particular share can have more than one user key provisioned for it. This allows more granular access to the filesystem, for example, if you needed some hosts to only access the filesystem in a read-only capacity. If you have multiple keys for a share, you can add the extra keys to your host and modify the above mounting procedure. This service is not available to hosts outside of the OpenStack cluster.