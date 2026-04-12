---
title: "SSH tunnelling"
slug: "ssh_tunnelling"
lang: "base"

source_wiki_title: "SSH tunnelling"
source_hash: "74e1a074d31357fc3de9e280ecc2b1e3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:19:18.015586+00:00"

tags:
  []

keywords:
  - "SSH tunnelling"
  - "sshuttle"
  - "port forwarding"
  - "SSH tunnel"
  - "database server"
  - "PostgreSQL"
  - "port number"
  - "environment variable"
  - "license server"
  - "localhost"
  - "MySQL"
  - "SSH connection"
  - "gateway server"
  - "compute node"
  - "Fir"
  - "job script"
  - "Jupyter Notebook"

questions:
  - "What is SSH tunnelling and why is it necessary for compute nodes on certain clusters?"
  - "What are the primary use cases that require setting up an SSH tunnel in this environment?"
  - "How do you configure a batch job script to forward a port and connect a compute node to an external license server?"
  - "What is the primary purpose of using SSH tunneling to connect to a compute node on a cluster?"
  - "Which specific tool is recommended for creating an SSH tunnel on Linux or MacOS X systems, and what command is used to initiate it?"
  - "How can a Windows user utilize MobaXTerm to set up local port forwarding to access an application running on a remote compute node?"
  - "How does the method for informing software to use a specific port on localhost vary?"
  - "What is a common way to set the license server port in a job script according to the text?"
  - "What specific action does the example job script perform regarding the license server?"
  - "How can a user access a Jupyter notebook using the provided localhost URL and token?"
  - "Which database servers can be accessed from a desktop by creating an SSH tunnel to the Fir cluster?"
  - "What is the specific SSH command syntax used to establish a connection to the PostgreSQL server on Fir?"
  - "How do you establish an SSH tunnel to connect a local port to the remote PostgreSQL or MySQL database servers?"
  - "What is the maximum allowed value for the local port number chosen for the SSH connection?"
  - "Where is the required MySQL password stored, and what determines how long the database connection remains open?"
  - "How do you establish an SSH tunnel to connect a local port to the remote PostgreSQL or MySQL database servers?"
  - "What is the maximum allowed value for the local port number chosen for the SSH connection?"
  - "Where is the required MySQL password stored, and what determines how long the database connection remains open?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [SSH](ssh.md)*

## What is SSH tunnelling?

SSH tunnelling is a method to use a gateway computer to connect two computers that cannot connect directly.

In the context of the Alliance, SSH tunnelling is necessary in certain cases, because compute nodes on some clusters do not have direct access to the Internet, nor can the compute nodes be contacted directly from the Internet.

The following use cases require SSH tunnels:

*   Running commercial software on a compute node that needs to contact a license server over the Internet;
*   Running [visualization software](../software/visualization.md) on a compute node that needs to be contacted by client software on a user's local computer;
*   Connecting to a database hosted on a cluster from somewhere other than that cluster's head node, e.g., your desktop.

In the first case, the license server is outside of the compute cluster and is rarely under a user's control, whereas in the other cases, the server is on the compute node but the challenge is to connect to it from the outside. We will therefore consider these two situations below.

!!! note
    While not strictly required to use SSH tunnelling, you may wish to be familiar with [SSH key pairs](ssh_keys.md).

## Contacting a license server from a compute node

!!! tip "What's a port?"
    A port is a number used to distinguish streams of communication from one another. You can think of it as loosely analogous to a radio frequency or a channel. Many port numbers are reserved, by rule or by convention, for certain types of traffic. See [List of TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) for more.

Certain commercially licensed programs must connect to a license server machine somewhere on the Internet via a predetermined port. If the compute node where the program is running has no access to the Internet, then a *gateway server* which does have access must be used to forward communications on that port, from the compute node to the license server. To enable this, one must set up an *SSH tunnel*. Such an arrangement is also called *port forwarding*.

In most cases, creating an SSH tunnel in a batch job requires only two or three commands in your job script. You will need the following information:

*   The IP address or the name of the license server (here LICSERVER).
*   The port number of the license service (here LICPORT).

You should obtain this information from whoever maintains the license server. That server also must allow connections from the login nodes; for Trillium, the outgoing IP address will be 142.150.188.58.

With this information, one can now set up the SSH tunnel. For nibi, an alternative solution is to request a firewall exception for the license server LICSERVER and its specific port LICPORT. The gateway server (GATEWAY) on Trillium is tri-gw while on nibi you would pick one of the login nodes (l1, l2, ... l5). You also need to choose which port number (COMPUTEPORT) to use on the compute node. The SSH command to issue in the job script is then:

```bash
ssh GATEWAY -L COMPUTEPORT:LICSERVER:LICPORT -N -f
```

In this command, the string following the `-L` parameter specifies the port forwarding information:
*   `-N` tells SSH not to open a shell on the GATEWAY,
*   `-f` and `-N` tell SSH not to open a shell and to run in the background, allowing the job script to continue on past this SSH command.

A further command to add to the job script should tell the software that the license server is on port COMPUTEPORT on the server *localhost*. The term *localhost* is the standard name by which a computer refers to itself. It is to be taken literally and should not be replaced with your computer's name. Exactly how to inform your software to use this port on *localhost* will depend on the specific application and the type of license server, but often it is simply a matter of setting an environment variable in the job script like

```bash
export MLM_LICENSE_FILE=COMPUTEPORT@localhost
```

### Example job script

The following job script sets up an SSH tunnel to contact licenseserver.institution.ca at port 9999.

```bash
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks 192
#SBATCH --time 3:00:00

REMOTEHOST=licenseserver.institution.ca
REMOTEPORT=9999
LOCALHOST=localhost
for ((i=0; i<10; ++i)); do
  LOCALPORT=$(shuf -i 1024-65535 -n 1)
  ssh tri-gw -L $LOCALPORT:$REMOTEHOST:$REMOTEPORT -N -f && break
done || { echo "Giving up forwarding license port after $i attempts..."; exit 1; }
export MLM_LICENSE_FILE=$LOCALPORT@$LOCALHOST

module load thesoftware/2.0
mpirun thesoftware .....
```

## Connecting to a program running on a compute node

SSH tunnelling can also be used in our context to allow a user's computer to connect to a compute node on a cluster through an encrypted tunnel that is routed via the login node of this cluster. This technique allows graphical output of applications like a [Jupyter Notebook](../software/jupyter.md) or [visualization software](../software/visualization.md) to be displayed transparently on the user's local workstation even while they are running on a cluster's compute node. When connecting to a database server where the connection is only possible through the head node, SSH tunnelling can be used to bind an external port to the database server.

There is Network Address Translation (NAT) on both Nibi and Fir allowing users to access the Internet from the compute nodes.

### From Linux or MacOS X

On a Linux or MacOS X system, we recommend using the [sshuttle](https://sshuttle.readthedocs.io) Python package.

On your computer, open a new terminal window and run the following `sshuttle` command to create the tunnel.

```bash
sshuttle --dns -Nr userid@machine_name
```

Then, copy and paste the application's URL into your browser. If your application is a [Jupyter notebook](../software/jupyter.md), for example, you are given a URL with a token:
```text
 http://fc3281.int.fir.alliancecan.ca:8888/?token=7ed7059fad64446f837567e32af8d20efa72e72476eb72ca
```

### From Windows

An SSH tunnel can be created from Windows using [MobaXTerm](connecting_with_mobaxterm.md) as follows.

Open two sessions in MobaXTerm.

*   Session 1 should be a connection to a cluster. Start your job there following the instructions for your application, such as [Jupyter Notebook](../software/jupyter.md). You should be given a URL that includes a host name and a port, such as `fc3281.int.fir.alliancecan.ca:8888` for example.

*   Session 2 should be a local terminal in which we will set up the SSH tunnel. Run the following command, replacing this example host name with the one from the URL you received in Session 1.

```bash
ssh -L 8888:fc3281.int.fir.alliancecan.ca:8888 someuser@fir.alliancecan.ca
```

This command forwards connections to **local port** 8888 to port 8888 on fc3281.int.fir.alliancecan.ca, the **remote port**. The local port number, the first one, does not *need* to match the remote port number, the second one, but it is conventional and reduces confusion.

Modify the URL you were given in Session 1 by replacing the host name with `localhost`. Again using an example from [Jupyter Notebook](../software/jupyter.md), this would be the URL to paste into a browser:
```text
 http://localhost:8888/?token=7ed7059fad64446f837567e32af8d20efa72e72476eb72ca
```

### Example for connecting to a database server on Fir from your desktop

An SSH tunnel can be created from your desktop to database servers PostgreSQL or MySQL using the following commands respectively:

```bash
ssh -L PORT:cedar-pgsql-vm.int.cedar.computecanada.ca:5432 someuser@fir.alliancecan.ca
ssh -L PORT:cedar-mysql-vm.int.cedar.computecanada.ca:3306 someuser@fir.alliancecan.ca
```

These commands connect port number PORT on your local host to PostgreSQL or MySQL database servers respectively. The port number you choose (PORT) should not be bigger than 32768 (2^15). In this example, *someuser* is your account username. The difference between this connection and an ordinary SSH connection is that you can now use another terminal to connect to the database server directly from your desktop. On your desktop, run one of these commands for PostgreSQL or MySQL as appropriate:

```bash
psql -h 127.0.0.1 -p PORT -U <your username> -d <your database>
mysql -h 127.0.0.1 -P PORT -u <your username> --protocol=TCP -p
```

MySQL requires a password; it is stored in your *.my.cnf* located in your home directory on Fir. The database connection will remain open as long as the SSH connection remains open.