---
title: "CephFS"
slug: "cephfs"
lang: "base"

source_wiki_title: "CephFS"
source_hash: "8eb322361c955cee995542b5c42c9e07"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:11:50.328153+00:00"

tags:
  - cloud

keywords:
  - "server id"
  - "cephfs client"
  - "ceph driver"
  - "Access rule"
  - "mount"
  - "CephFS client"
  - "VM configuration"
  - "bash"
  - "openstack server list"
  - "/etc/fstab"
  - "Virtual Machine"
  - "OpenStack"
  - "fstab"
  - "source packages"
  - "ceph-fuse"
  - "host directory"
  - "ceph client"
  - "epel-release"
  - "CephFS-Network"
  - "Red Hat family"
  - "ceph.keyring"
  - "mount filesystem"
  - "Ceph"
  - "ceph.conf"
  - "CephFS"
  - "OpenStack cluster"
  - "servers"
  - "Share creation"
  - "rpm-tentacle"

questions:
  - "How do you request an initial quota and access to the CephFS service?"
  - "What are the steps and required parameters to create a new CephFS share and generate an access key in the OpenStack Horizon GUI?"
  - "How does the process of attaching the CephFS network to a virtual machine differ between the Arbutus and SD4H/Juno clusters?"
  - "What is the primary purpose of listing the servers as described in the text?"
  - "Which specific bash command is executed to retrieve the list of servers?"
  - "What are the column headers displayed in the output table of the server list?"
  - "What OpenStack command is used to attach the CephFS network to a specific virtual machine?"
  - "How do you configure the YUM repository file to access the latest stable Ceph client packages for Enterprise Linux 9?"
  - "What prerequisite repository needs to be installed on the system before installing the CephFS client and its dependencies?"
  - "How do you install the necessary Ceph client packages and dependencies on a Debian-based distribution?"
  - "What information must be included in the ceph.conf and ceph.keyring files to properly configure and authenticate the Ceph client?"
  - "What are the steps to permanently mount the CephFS filesystem on the host machine using the /etc/fstab file?"
  - "What are the specific base URLs and GPG keys used to configure the Ceph noarch and source package repositories?"
  - "What command must be executed to install the required EPEL repository before proceeding with the Ceph installation?"
  - "Which Ceph components and dependencies become available for installation once the repositories are properly set up?"
  - "What is the significance of the non-standard colon and the `nofail` option when configuring the CephFS mount in the system?"
  - "What are the necessary steps and configurations required to mount CephFS directly in user space using `ceph-fuse`?"
  - "How can multiple user keys be utilized to provide granular access control, such as read-only permissions, for a specific share?"
  - "What command is used to create the mount point directory on the host?"
  - "How can you permanently mount a CephFS device to a virtual machine?"
  - "What specific configuration details must be added to the /etc/fstab file?"
  - "What is the significance of the non-standard colon and the `nofail` option when configuring the CephFS mount in the system?"
  - "What are the necessary steps and configurations required to mount CephFS directly in user space using `ceph-fuse`?"
  - "How can multiple user keys be utilized to provide granular access control, such as read-only permissions, for a specific share?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

CephFS provides a common filesystem that can be shared amongst multiple OpenStack VM hosts. Access to the service is granted via requests to [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).

!!! note
    This is a fairly technical procedure that assumes basic Linux skills for creating/editing files, setting permissions, and creating mount points. For assistance in setting up this service, write to [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca).

## Procedure

### Request access to shares

If you do not already have a quota for the service, you will need to request this through [cloud@tech.alliancecan.ca](mailto:cloud@tech.alliancecan.ca). In your request, please provide the following:
*   OpenStack project name
*   amount of quota required (in GB)
*   number of shares required

### OpenStack configuration: Create a CephFS share

**Create the share.**

*   In *Project --> Share --> Shares*, click on *+Create Share*.
*   **Share Name** = enter a name that identifies your project (e.g., *project-name-shareName*)
*   **Share Protocol** = CephFS
*   **Size** = size you need for this share
*   **Share Type** = cephfs (or cephfs-ec42 on SD4H/Juno)
*   **Availability Zone** = nova
*   Do not check *Make visible for all* (or *Make visible to users from all projects* on SD4H/Juno), otherwise the share will be accessible by all users in all projects.
*   Click on the *Create* button.

**Create an access rule to generate an access key.**

*   In *Project --> Share --> Shares --> Actions* column, select *Manage Rules* from the drop-down menu.
*   Click on the *+Add Rule* button (right of the page).
*   **Access Type** = cephx
*   **Access Level** = select *read-write* or *read-only* (you can create multiple rules for either access level if required)
*   **Access To** = select a key name that describes the key. This name is important because it will be used in the CephFS client configuration on the VM; on this page, we use *MyCephFS-RW*.

**Note the share details which you will need later.**

*   In *Project --> Share --> Shares*, click on the name of the share.
*   In the *Share Overview*, note the three elements circled in red in the image above: *Path*, which will be used in the mount command on the VM; the *Access to*, which will be the client name; and the *Access Key* that will let the VM's client connect.

### Attach the CephFS network to your VM

#### On Arbutus

On `Arbutus`, the CephFS network is already exposed to your VM; there is nothing to do here, **[go to the VM configuration section](#vm-configuration-install-and-configure-cephfs-client)**.

#### On SD4H/Juno

On `SD4H/Juno`, you need to explicitly attach the CephFS network to the VM.

**With the Web GUI**

For each VM you need to attach, select *Instance --> Action --> Attach interface*, select the CephFS-Network, and leave the *Fixed IP Address* box empty.

**With the [OpenStack client](openstack-command-line-clients.md)**

List the servers and select the ID of the server you need to attach to the CephFS.

```bash
$ openstack  server list
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
$ openstack  server add network 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 CephFS-Network
$ openstack  server list
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| ID                                   | Name         | Status | Networks                                                            | Image                    | Flavor   |
+--------------------------------------+--------------+--------+---------------------------------------------------------------------+--------------------------+----------+
| 1b2a3c21-c1b4-42b8-9016-d96fc8406e04 | prune-dtn1   | ACTIVE | CephFS-Network=10.65.20.71; test_network=172.16.1.86, 198.168.189.3 | N/A (booted from volume) | ha4-15gb |
| 0c6df8ea-9d6a-43a9-8f8b-85eb64ca882b | prune-mgmt1  | ACTIVE | test_network=172.16.1.64                                            | N/A (booted from volume) | ha4-15gb |
| 2b7ebdfa-ee58-4919-bd12-647a382ec9f6 | prune-login1 | ACTIVE | test_network=172.16.1.111, 198.168.189.82                           | N/A (booted from volume) | ha4-15gb |
+--------------------------------------+--------------+--------+------------------------------------------------------------------------+--------------------------+----------+
```

We can see that the CephFS network is attached to the first VM.

### VM configuration: install and configure CephFS client

#### Required packages for the Red Hat family (RHEL, CentOS, Fedora, Rocky, Alma)

Check the available releases at [https://download.ceph.com/](https://download.ceph.com/) and look for recent `rpm-*` directories. As of April 2026, `tentacle` is the latest stable release. The compatible distributions (distros) are listed at [https://download.ceph.com/rpm-tentacle/](https://download.ceph.com/rpm-tentacle/). Here we show configuration examples for `Enterprise Linux 9`.

**Install relevant repositories for access to Ceph client packages:**

=== "/etc/yum.repos.d/ceph.repo"

    ```ini
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

The epel repo also needs to be in place:

```bash
sudo dnf install epel-release
```

You can now install the ceph lib, cephfs client, and other dependencies:

```bash
sudo dnf install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

#### Required packages for the Debian family (Debian, Ubuntu, Mint, etc.)

You can get the repository once you have figured out your distro `{codename}` with `lsb_release -sc`:

```bash
sudo apt-add-repository 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```

If the previous command gave an error, revert it with the following command and go to the next step:

```bash
sudo add-apt-repository -r 'deb https://download.ceph.com/debian-tentacle/ {codename} main'
```

You can now install the ceph lib, cephfs client, and other dependencies:

```bash
sudo apt-get install -y libcephfs2 python3-cephfs ceph-common python3-ceph-argparse
```

#### Configure Ceph client

Once the client is installed, you can create a `ceph.conf` file. Note the different `mon host` for the different cloud.

=== "Arbutus"

    === "/etc/ceph/ceph.conf"

        ```ini
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

    === "/etc/ceph/ceph.conf"

        ```ini
        [global]
        admin socket = /var/run/ceph/$cluster-$name-$pid.asok
        client reconnect stale = true
        debug client = 0/2
        fuse big writes = true
        mon host = 10.65.0.10:6789,10.65.0.12:6789,10.65.0.11:6789
        [client]
        quota = true
        ```

You can find the monitor information in the share details *Path* field that will be used to mount the volume. If the value on the web page is different than what is seen here, it means that the wiki page is out of date.

You also need to put your client name and secret in the `ceph.keyring` file:

=== "/etc/ceph/ceph.keyring"

    ```ini
    [client.MyCephFS-RW]
        key = <Access Key>
    ```

Again, the access key and client name (here MyCephFS-RW) are found under the access rules on your project web page. Look for *Project --> Share --> Shares*, then click on the name of the share.

**Retrieve the connection information from the share page for your connection:**

*   Open up the share details by clicking on the name of the share in the *Shares* page.
*   Copy the portion of the *Path* of the share that starts with `:` which we will use to mount the filesystem (for example `:/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c`, is used here).

**Mount the filesystem**

*   Create a mount point directory somewhere in your host (`/cephfs`, is used here):

```bash
mkdir /cephfs
```

*   You can use the Ceph driver to permanently mount your CephFS device by adding the following in the VM fstab:

=== "Arbutus"

    === "/etc/fstab"

        ```text
        :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,nofail 0  2
        ```

=== "SD4H/Juno"

    === "/etc/fstab"

        ```text
        :/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c /cephfs/ ceph name=MyCephFS-RW,mds_namespace=cephfs_4_2,x-systemd.device-timeout=30,x-systemd.mount-timeout=30,noatime,_netdev,rw,nofail 0  2
        ```

**Notice** the non-standard `:` before the device path. It is not a typo! The mount options are different on different systems. The namespace option is required for SD4H/Juno, while other options are performance tweaks. The `nofail` option ensures that the system will boot even in the unlikely case that the CephFS service is down or unreachable.

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

Let the fuse mount be accessible in userspace by uncommenting `user_allow_other` in the `fuse.conf` file.

=== "/etc/fuse.conf"

    ```text
    # mount_max = 1000
    user_allow_other
    ```

You can now mount CephFS in a user’s home:

```bash
mkdir ~/my_cephfs
ceph-fuse my_cephfs/ --id=MyCephFS-RW --conf=~/ceph.conf --keyring=~/ceph.keyring   --client-mountpoint=/volumes/_nogroup/f6cb8f06-f0a4-4b88-b261-f8bd6b03582c
```

Note that the client name is here the `--id`. The `ceph.conf` and `ceph.keyring` content are exactly the same as for the ceph kernel mount.

## Notes

A particular share can have more than one user key provisioned for it. This allows more granular access to the filesystem, for example, if you needed some hosts to only access the filesystem in a read-only capacity. If you have multiple keys for a share, you can add the extra keys to your host and modify the above mounting procedure. This service is not available to hosts outside of the OpenStack cluster.