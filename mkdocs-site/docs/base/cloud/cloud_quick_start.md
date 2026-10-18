---
title: "Cloud Quick Start"
slug: "cloud_quick_start"
lang: "base"

source_wiki_title: "Cloud Quick Start"
source_hash: "f84aedd776cd99db7a57c0e3de341fbe"
last_synced: "2026-10-18T00:43:06.821597+00:00"
last_processed: "2026-10-18T01:24:42.839900+00:00"

tags:
  - cloud

keywords:
  - "Network"
  - "Using SSH keys in Linux"
  - "ssh -i"
  - "recommended not to delete the volume"
  - "IP address column"
  - "SSH key pair"
  - "Remmina client"
  - "backing up your VM"
  - "Create New Volume"
  - "private key"
  - "public IP"
  - "Administrator password"
  - "Allocated list"
  - "MobaXterm"
  - "Windows VM"
  - "boot the VM"
  - "default user name"
  - "automating VM creation"
  - "SSH Keys"
  - "Floating IPs"
  - "CIDR rule"
  - "Importing an existing key pair"
  - "Cloud Technical Glossary"
  - "security rule"
  - "Generating SSH keys in Windows"
  - "cloud project"
  - "certificate warning"
  - "Delete Volume on Instance Delete"
  - "Volume Size"
  - "Key Pair"
  - "Associate button"
  - "SSH key pairs"
  - "SSH"
  - "Add Rule"
  - "RDP"
  - "0.0.0.0/0"
  - "floating IP"
  - "Floating IP"
  - "alert icon"
  - "SSH connection"
  - "public IP address"
  - "Creating a Linux VM"
  - "Flavor"
  - "Debian"
  - "OpenStack"
  - "get a license"
  - "apply license"
  - "brute force attacks"
  - "private key (.pem)"
  - "RDP rule"
  - "flavor"
  - "CIDR"
  - "cloud VM"
  - "OpenStack dashboard"
  - "Windows image access"
  - "compatible browser"
  - "Import Public Key"
  - "virtual machine"
  - "security considerations"
  - "Remote Desktop Connection"
  - "license information"
  - "resource allocation"
  - "Virtual machine flavors"
  - "Security Groups"
  - "Private IP address"
  - "Launch Instance"

questions:
  - "What steps must you complete before you can access a cloud project?"
  - "Which web browsers are recommended for accessing the cloud interface, and what error might appear with unsupported browsers?"
  - "How does OpenStack handle authentication for newly created virtual machines, and what should you do if you don’t have an SSH key pair?"
  - "What steps should be followed to import an existing SSH key pair?"
  - "Where can users find instructions for generating SSH keys on Windows versus Linux/Mac?"
  - "Where can additional information about creating and managing SSH key pairs be found?"
  - "What are the steps and requirements for importing an existing RSA public key pair into OpenStack, and why is creating key pairs directly in OpenStack discouraged?"
  - "When launching a new virtual machine, which options must be configured under the Details, Source, and Flavor tabs, and how should appropriate values be chosen?"
  - "How do the volume settings (creating a new volume, specifying its size, and the “Delete Volume on Instance Delete” option) impact data persistence for the instance?"
  - "What steps must be taken to ensure the default security group is correctly allocated before launching a VM?"
  - "How do you associate a floating (public) IP address with a newly created instance in OpenStack?"
  - "Which options are recommended to remain unchanged during the initial VM creation process, and why?"
  - "What does an alert icon next to a specification indicate when choosing a virtual machine flavor?"
  - "How do you allocate a flavor that your project can support without triggering an alert?"
  - "Where can you find more detailed information about virtual machine flavors?"
  - "How can you assign a public IP address to a VM using the IP Address field?"
  - "What are the two IP addresses shown for the VM after association, and how are they formatted?"
  - "Where can you view a list of all your public (floating) IP addresses and their associated projects?"
  - "How do you add an SSH rule to the default security group in OpenStack and restrict it to a specific IP address?"
  - "What steps should you take if your IP address changes or you need to allow a range of IPs for SSH access?"
  - "How can you connect to your OpenStack VM via SSH from a Linux or macOS machine, and what information do you need beforehand?"
  - "What is the exact SSH command syntax to connect to your VM using a private key?<br>How should the placeholders `<user name>` and `<public IP of your server>` be replaced when executing the command?<br>What default usernames correspond to the Debian, Ubuntu, and CentOS images listed in the table?"
  - "How can you set up an SSH session in MobaXterm to connect to your VM using a private .key file?"
  - "What volume configuration options are recommended when launching a Windows VM (size, delete‑on‑instance‑delete, etc.)?"
  - "Why is direct SSH access to the root account disabled, and which default user is granted full sudo privileges?"
  - "What steps are required in the OpenStack dashboard to launch a Windows VM, including selecting the image name, flavor, security groups, and network?"
  - "How do you change the Administrator password on the newly created Windows VM using the console, and what actions should you take if the console screen is blank or in screensaver mode?"
  - "How can you assign a public (floating) IP to the VM and configure the security group’s RDP rule to allow remote desktop access while restricting it to your own IP address?"
  - "What source should be selected to boot the VM?"
  - "What minimum size is recommended for the root drive volume?"
  - "Why is it generally advised not to enable “Delete Volume on Instance Delete” when creating a new volume?"
  - "Why does leaving the RDP CIDR set to 0.0.0.0/0 expose your VM to security risks and possible revocation of access?"
  - "How can you limit RDP access to a single IP address or a specific range of IP addresses using CIDR notation?"
  - "What steps should you take if you need to allow RDP connections from additional IPs beyond the initially configured one?"
  - "What information (floating IP, username, password) must be provided to connect to a Windows VM via Remote Desktop?"
  - "How do the connection steps vary when using the Remote Desktop client on Windows, the Remmina client on Linux, and the Windows App client on macOS?"
  - "What should users do about the certificate warning (“The certificate is not from a trusted certifying authority”) that appears when connecting to the Windows VM?"
  - "What steps are required to create a Linux virtual machine?"
  - "Where can I find guidance on managing cloud resources using OpenStack?"
  - "How can I automate the creation and backup of my virtual machines?"
  - "Where can users obtain the appropriate license for running cloud VMs?"
  - "Which types of licenses are required or compatible for cloud VM usage, and what are the differences between them?"
  - "How do you apply a license to an existing cloud VM compared to applying it to a newly created VM?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

## Before you start

1.  **Have a cloud project**

    **You cannot access a cloud without first having a cloud project.** If you don't already have a [cloud project](managing_your_cloud_resources_with_openstack.md#projects), see [Getting a cloud project](cloud.md#getting-a-cloud-project). Once a cloud project is associated with your account, you will receive a confirmation email which will have important details you will need to access your project and get started with the cloud. Make sure you have this confirmation email ready.

2.  **Have a compatible browser**

    The web interface for accessing your cloud project works well with both the [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Chrome](https://www.google.com/chrome/) web browsers. Other browsers may also work; however, some have shown the error message `Danger: There was an error submitting the form. Please try again.` which suggests that your browser is not supported by our system. This error message was noticed with certain versions of the Safari web browser on Macs; upgrading Safari may help, but we recommend that you use [Firefox](https://www.mozilla.org/en-US/firefox/new/) or [Chrome](https://www.google.com/chrome/). If you are still having issues, email [technical support](../support/technical_support.md).

## Creating your first virtual machine

Your project will allow you to create virtual machines (also referred to as *instances* or *VMs*) stored on the cloud, which you can access from your personal computer using our web interface.

1.  **Log in to the cloud interface to access your project**

    The confirmation email you received includes a link to the cloud interface your project is associated with. Click on this link to open your project in your default web browser. If your default web browser is not compatible, open a compatible web browser and copy and paste the link address into the browser. If you know the name of your associated cloud, but don't have the login URL, see [using the cloud](cloud.md#cloud-systems) for the list of cloud interface URLs at which you can log in. Use your username (not your email address) and password to log in.

2.  **Check your OpenStack dashboard**

    After logging on to the cloud interface (the platform is called *OpenStack*), you will see a dashboard that shows an overview of all the resources available in your project. If you want to know more about navigating and understanding your OpenStack dashboard, read the official [OpenStack documentation](https://docs.openstack.org/horizon/latest/user/index.html).

Below there are instructions on starting a Windows VM or a Linux VM, depending on which tab you select. **Remember this is the operating system for the virtual machine or *instance* you are creating, not the operating system of the physical computer you are using to connect**. It should be clear from your project pre-planning whether you will be using Linux or Windows for your VM operating system, but if you are unsure, please email [technical support](../support/technical_support.md).

=== "Linux"

### SSH key pair

When you create a virtual machine, password authentication is disabled for security reasons.

Instead, OpenStack creates your VM with one SSH (Secure Shell) public key installed, and you can only log in using this SSH key pair. If you have used SSH keys before, the SSH public key can come from a key pair which you have already created on some other machine. In this case, follow the instructions below for **Importing an existing key pair**. If you have not used SSH key pairs before or don't currently have a pair you want to use, you will need to create a key pair. If you are using a Windows machine, see the [Generating SSH keys in Windows](../getting-started/generating_ssh_keys_in_windows.md) page; otherwise, follow the [Linux/Mac instructions](../getting-started/using_ssh_keys_in_linux.md). For more information on creating and managing your key pairs, see the [SSH Keys](../getting-started/ssh_keys.md) page in our documentation.

#### Importing an existing key pair

1.  On the OpenStack left menu, select *Compute->Key Pairs*.
2.  Click on the *Import Public Key* button; the *Import Public Key* window is displayed.
3.  Name your key pair.
4.  Paste your public key (only RSA type SSH keys are currently supported).
    Ensure your pasted public key contains no newline or space characters.
5.  Click on the *Import Public Key* button.

**It is not advised to create key pairs in OpenStack because they are not created with a passphrase, which creates security issues.**

### Launching a VM

To create a virtual machine, select *Compute->Instances* on the left menu, then click on the *Launch Instance* button.

A form is displayed where you define your virtual machine. If you have a plan for the exact specifications your VM needs through your pre-planning, feel free to use those specifications. Otherwise, you can follow along with this example for a fairly generic, easy-to-use Linux VM.
The *Launch Instance* window has the following options:

1.  *Details*
    *   *Instance Name:* Enter a name for your virtual machine. Do not include spaces or special characters in your instance name. For more details on naming rules, see [restrictions on valid host names](https://en.wikipedia.org/wiki/Hostname).
    *   *Description:* This field is optional.
    *   *Availability Zone:* The default is *Any Availability Zone*; do not change this.
    *   *Count:* This indicates the number of virtual machines to create. Unless you have specifically planned for multiple machines, leave this set at 1.

2.  *Source*
    *   *Select Boot Source:* Because it's your first VM, select *Image* as the boot source. For information about other options, see [Booting from a volume](working_with_volumes.md#booting-from-a-volume).
    *   *Create New Volume:* Click *Yes*; your VM's data will be stored in the cloud volume (or persistent storage). For more information on volume usage and management, see [Working with volumes](working_with_volumes.md).
    *   *Volume Size (GB):* If you have a pre-planned volume size, use that; otherwise, 30 GB is reasonable for the operating system and some modest data needs. For more information on volume usage and management, see [Working with volumes](working_with_volumes.md).
    *   *Delete Volume on Instance Delete:* Click on *No* to help prevent your volume from being deleted accidentally; however, if you are confident you always want your volume deleted when your instance is deleted, click on *Yes*.
    *   *Allocated* and *Available* lists: The list at the bottom of the window shows the available images your VM can boot. For a beginner on Linux, we recommend the most recent **Ubuntu** image, but if you prefer, you can choose any one of the other Linux operating systems. To select an image, click on the upwards pointing arrow on the far right of the row containing your desired image. That row should now show up in the *Allocated* list above. **It is important for later to remember which image you chose** (e.g., Ubuntu, Fedora, etc.).

3.  *Flavour*
    *   *Allocated* and *Available* lists: The flavour determines what type of hardware is used for your VM, which determines how much memory and processing capabilities it has. The *Available* list shows all the flavours available for your chosen boot image. Click on the > icon at the far left of a row to see how that particular flavour matches up with what you have been allocated for your project. If there is an alert icon on one of the specifications, that means that your project doesn't have enough of that resource to support that flavour. Choose a flavour that your project can support (i.e., doesn't issue an alert) and click on the upwards arrow on the far right of that row. That flavour should now show up in the *Allocated* list. For more details, see [Virtual machine flavours](virtual_machine_flavors.md).

4.  *Networks:* Do not change this unless required. On Arbutus, select your project network by default (usually starting with *def-project-name*).

5.  *Network Ports:* Do not change this now.

6.  *Security Groups:* The default security group should be in the *Allocated* list. If it is not, move it from *Available* to *Allocated* using the upwards arrow located on the far right of the group's row. For more information, see [Security Groups](managing_your_cloud_resources_with_openstack.md#security-groups).

7.  *Key Pair:* From the *Available* list, select the SSH key pair you created earlier by clicking the upwards arrow on the far right of its row. If you do not have a key pair, you can create or import one from this window using the buttons at the top of the window (please [see above](#ssh-key-pair)). For more detailed information on managing and using key pairs, see [SSH Keys](../getting-started/ssh_keys.md).

8.  *Configuration:* Do not change this now. For more information on customization scripts, see [Using CloudInit](automating_vm_creation.md).
9.  *Server Groups:* Do not change this now.
10. *Scheduler Hints:* Do not change this now.
11. *Metadata:* Do not change this now.

Once you have reviewed all the options and defined your virtual machine, click on the *Launch Instance* button and your virtual machine will be created. The list of instances will be displayed and the *Task* field will show the current task for the VM; it will likely be *Spawning* initially. Once the VM has spawned, it will have the power state of *Running*; this may take a few minutes.

### Network settings

On the *Instances* page is a list of VMs with their IP address(es) displayed in the *IP Address* column. Each VM will have at least one private IP address, but some may also have a second public IP assigned to it. When your OpenStack project is created, a local network is also created for you. This local network is used to connect VMs to each other and to an internet gateway within that project, allowing them to communicate with each other and the outside world. The private IP address provides inter-VM networking but does not allow for connection to the outside world. Any VM created in your project will have a private IP address assigned to it from this network of the form `192.168.X.Y`. Public IPs allow outside services and tools to initiate contact with your VM, such as allowing you to connect to your VM via your personal computer to perform administrative tasks or serve up web content. Public IPs can also be pointed to by domain names.

1.  Assign a public IP address
    *   Ensure you are still viewing the instances list where you were redirected as your VM launched. If you need to use the navigation panel, select options *Compute->Instances* on the OpenStack menu.
    *   Click on the drop-down arrow menu (indicated by &#x25BC;) on the far right of the row for your VM and select *Associate Floating IP*, then in the *Allocate Floating IP* window, click on the *Allocate IP* button. If this is your first time associating a floating IP, you need to click on the “+” sign in the *Manage Floating IP Associations* dialog box. If you need to allocate a public IP address for this VM again in the future, you can select one from the list by clicking the &#x25BC; in the *IP Address* field.
    *   Click on the *Associate* button.
    *   You should now have two IP addresses in your IP address column. One will be of the form `192.168.X.Y`, the other is your public IP. You can also find a list of your public IP addresses and their associated projects by going to *Network->Floating IPs*. You will need your public IP when you are trying to connect to your VM.
2.  Configure the firewall
    *   On the OpenStack left menu, select *Network->Security Groups*.
    *   On the group row named *default*, click on the *Manage Rules* button on the far right.
    *   On the next screen, click on the *+Add Rule* button near the top right corner.
    *   In the *Rule* drop-down menu, select *SSH*.
    *   The *Remote* text box should automatically have *CIDR* in it; do not change this.
    *   In the *CIDR* text box, replace `0.0.0.0/0` with `your-ip/32`. Note that this is the IP address of the physical computer you are wanting to use to connect to your VM. If you don't know your current IP address, you can see it by going to [ipv4.icanhazip.com](http://ipv4.icanhazip.com) in your browser. If you want to access your VM from other IPs, you can add more rules with different IP addresses. If you want to specify a range of IP addresses, use [this tool](https://www.ipaddressguide.com/cidr) to calculate your CIDR rule for a range of IP addresses.
    *   Finally, click on the *Add* button. Now the rule you just created should show up on the list in security groups.
3.  Important notes
    *   **Do not remove the default security rules** as this will affect the ability of your VM to function properly (see [Security Groups](managing_your_cloud_resources_with_openstack.md#security-groups)).
    *   **Security rules cannot be edited**; they can only be deleted and re-added. If you make a mistake when creating a security group rule, you need to delete it using the *Delete Rule* button on the far left of the row for that rule in the security groups screen, and then re-add it correctly from scratch using the *+Add Rule* button.
    *   If you change your network location (and therefore your IP address), then you need to add the security rule described in this section for that new IP address. Remember that when you change your physical location (e.g., working on campus versus working from home), you are changing your network location.
    *   If you do not have a static IP address for the network you are using, remember that it can sometimes change, so if you can no longer connect to your VM after a period of time, sometimes it's worth checking to see if your IP address has changed. You can do this by putting [ipv4.icanhazip.com](http://ipv4.icanhazip.com) in your browser and seeing if it matches what you have in your security rule. If your IP address changes frequently, but the leftmost numbers always stay the same, it could make more sense to add a range of IP addresses rather than frequently modifying your security rules. Use [this tool](https://www.ipaddressguide.com/cidr) for determining a CIDR IP range from an IP range, or learn more about CIDR notation [here](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
    *   It can be helpful to add a description about what a security rule is for (e.g., home or office). That way, you will know which rule is no longer needed if you want to add a new rule while connecting, for example, from home.

### Connecting to your VM with SSH

In the first step of this quick guide, you saved a private key to your computer. Make sure you remember where you saved it because you will need it to connect to your VM. You will also need to remember which type of image you used (Ubuntu, Fedora, etc.) and which public IP address is associated with your VM.

#### Connecting from a Linux or Mac machine

If the computer you are using to connect to your VM has a Linux or Mac operating system, use the following instructions to connect to your VM. Otherwise, skip down to the next section to connect with a Windows computer.

Open a terminal and input the following command:

```bash
ssh -i /path/where/your/private/key/is/my_key.key <user name>@<public IP of your server>
```

where `<user name>` is the name of the user connecting and `<public IP of your VM>` is the public IP you associated with your VM in the previous step. The default user name depends on the image.

| Image distribution name | `<user name>` |
| :---------------------- | :------------ |
| Debian                  | debian        |
| Ubuntu                  | ubuntu        |
| CentOS                  | centos        |
| Fedora                  | fedora        |
| AlmaLinux               | almalinux     |
| Rocky                   | rocky         |

These default users have full sudo privileges. Connecting directly to the root account via SSH is disabled.

#### Connecting from a Windows machine

If you want to use a Windows computer to connect to your VM, you will need to have an interface application to handle the SSH connection. We recommend **MobaXTerm**, and will show the instructions for connecting with MobaXTerm below. If you want to connect using PuTTY instead, see [Connecting with PuTTY](../getting-started/connecting_with_putty.md).

To download MobaXterm, [click here](http://mobaxterm.mobatek.net/).
To connect to your VM using MobaXterm, follow these instructions:

1.  Open the MobaXterm application.
2.  Click on *Sessions*, then press *New session*.
3.  Select an SSH session.
4.  Enter the public IP address for your VM in the *Remote host* address field.
5.  Ensure that the *Specify username* checkbox is checked, then enter the image type for your VM (Ubuntu, for example) into the username field, all lowercase.
6.  Click on the *Advanced SSH settings* tab, and check the *Use private key* checkbox.
7.  Click on the page icon in the far right of the *Use private key* field. In the pop-up dialogue box, select the key pair (.pem file) that you saved to your computer at the beginning of this quick guide.
8.  Then click on OK. MobaXterm will then save that session information you just entered for future connections, and also open an SSH connection to your VM. It also opens an SFTP connection, which allows you to transfer files to and from your VM using drag-and-drop via the left-hand panel.

### Where to go from here

*   Learn about using the [Linux command line](../getting-started/linux_introduction.md) in your VM
*   Learn about [security considerations when running a VM](security_considerations_when_running_a_vm.md)
*   See [configuring a data or web server](configuring_a_data_or_web_server.md)
*   Learn more about working with [OpenStack](managing_your_cloud_resources_with_openstack.md)
*   [Cloud Technical Glossary](cloud_technical_glossary.md)
*   [Automating VM creation](automating_vm_creation.md)
*   [Backing up your VM](backing_up_your_vm.md)
*   For questions about our cloud service, email [technical support](../support/technical_support.md).

=== "Windows"

### Request access to a Windows image

To create a Windows VM on one of our clouds, you must first request access to a Windows image by emailing [technical support](../support/technical_support.md).

You will be provided access to a Windows Server 2025 Datacenter image and a Windows-specific flavour.

### Launching a VM

To create a virtual machine, click on the *Instances* menu item on the left, then click on the Launch Instance button.

A form is displayed where you define your virtual machine.

*   *Details* tab
    *   *Availability Zone*: Keep the default option, Any Availability Zone
    *   *Instance Name*: Enter a name for your virtual machine. For details on naming rules, see [restrictions on valid host names](https://en.wikipedia.org/wiki/Hostname).
    *   *Instance Count*: Number of virtual machines to create.
*   *Source* tab
    *   *Select Boot Source*: What source should be used to boot the VM; choose *Image*.
    *   *Create New Volume*: Keep the default option, Yes.
    *   *Volume Size*: The size of the root drive; enter 50 GB or more.
    *   *Delete Volume on Instance Delete*: If Yes is selected, the volume that is created with the VM will be deleted when the VM is terminated.

    !!! note "Recommendation for Volume Deletion"
        It is generally recommended not to delete the volume on instance delete. The volume can be deleted manually if desired and allows the VM to be terminated without deleting the volume.

    *   *Image Name*: Select the Windows image name you were provided (e.g., Windows-2025-Datacenter).
*   *Flavour* tab
    *   *Flavour*: The flavour defines virtual machine hardware specifications; choose the 'p4-15gb-windows' flavour.
*   *Access & Security* tab
    *   *Security Groups*: Ensure the *default* security group is checked.
*   *Networking* tab: Select the IPv4 network (e.g., <project name>-network).

Once you have reviewed all the tabs and defined your virtual machine, click on the Launch Instance button and your virtual machine will be created. The Instances list will be displayed and the Task field will show the current task for the VM; it will likely be "Block Device Mapping" initially. Once the VM has spawned and begins to boot, it will have the Power State of "Running". It will likely take 10+ minutes to finish creating the volume and copying the image to it before beginning to boot.

### Change the Administrator Password

When the VM first boots it will not finish booting until you change the Administrator password using the console built into the OpenStack dashboard.

To get to the console:

1.  Go to *Instances* on the left-hand menu.
2.  Click on the *Instance Name* of your Windows VM.
3.  Click on the *Console* tab to display the *Instance Console* and wait until you see the appropriate screen. If you waited a significant amount of time, the console screen may have gone into a screensaver mode (blank/black screen). If this is the case, click on the blank/black screen so that it gains focus and if necessary, press a key on your keyboard to wake it up.

At this point, your VM will continue booting. Once it finishes, the Console will display a Server Manager.

### Network

On the *Instances* page is a list VMs with their IP address(es) displayed in the *IP Address* column. Each VM will have at least one private IP address, but some may also have a second public IP assigned to it.

#### Private IP

When your OpenStack project is created, a local network is also created for you. This local network is used to connect VMs within that project, allowing them to communicate with each other and the outside world. Their private IP address does not allow the outside world to reference that VM. Any VM created in your project will have a private IP address assigned to it from this network of the form `192.168.X.Y`.

#### Public IP

Public IPs allow outside services and tools to initiate contact with your VM, such as allowing you to connect to it to perform administrative tasks or serve up web content. Public IPs can also be pointed to by domain names.

To assign a public IP to a VM, you need to select *Associate Floating IP* from the drop-down menu button (indicated by &#x25BC;) of the *Actions* column in the *Instances* list. If this is your first time associating a floating IP, your project hasn't been assigned an external IP address yet. You need to click on the “+” sign to bring up the *Allocate Floating IP* dialog box. There is only one pool of public addresses, so the correct pool will already be selected; click on the *Allocate IP* button. The *Manage Floating IP Associations* screen is displayed again, indicating the IP address and the port (or VM) to which it will be associated (or more specifically [NATted](https://en.wikipedia.org/wiki/Network_address_translation)); click on the *Associate* button.

#### Firewall, add rules to allow RDP

To connect to your virtual machine using a remote desktop connection client, you will need to allow access for remote desktop protocol (RDP) to your VM.

1.  On the *Security Groups* tab, select *Access & Security* (under Network); on the default row, click the *Manage Rules* button.
2.  On the next screen, click the *Add Rule* button.
3.  RDP has a predefined rule. Select it in the *Rules* drop-down menu and leave *CIDR* under *Remote*.
4.  Replace the `0.0.0.0/0` in the CIDR text box with `<your-ip>/32`. If you don't know your current IP address, you can see it by going to [ipv4.icanhazip.com](http://ipv4.icanhazip.com) in your browser. Leaving `0.0.0.0/0` will allow anyone to attempt a connection with your VM. You should never allow completely open access with RDP as your VM will be susceptible to [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack). This replacement will restrict RDP access to your VM only from this IP. If you want to allow access from other IPs, you can add additional RDP rules with different IP addresses or you can specify a range of IP addresses by using [this tool](https://www.ipaddressguide.com/cidr) to calculate your CIDR rule from a range of IP addresses.

    !!! warning "Security Alert: Do Not Leave RDP Open to the World"
        **If you leave RDP open to the world by leaving the `0.0.0.0/0` in the CIDR text box, a cloud administrator may revoke access to your VM until the security rule is fixed.**

5.  Finally, click the *Add* button.

### Remote desktop connection

To connect to a Windows VM, we will use a Remote Desktop Connection client. To connect to your Windows VM, you need to supply a floating IP, user name, and password.

#### From a Windows client

Many Windows systems come with the remote desktop connection tool pre-installed. Try searching for "remote desktop connection" in your Windows system search. If you cannot find it, you can go to [the Microsoft store](https://www.microsoft.com/en-ca/store/p/microsoft-remote-desktop/9wzdncrfj3ps) and install it. It should be a free installation.

Once you have run the remote desktop connection tool, you should see a window similar to the expected interface. To connect to your Windows VM:

1.  Enter the public IP address next to *Computer*.
2.  Add *Administrator* in the *User name* text box.
3.  Click the *Connect* button at the bottom.
4.  Enter the password when prompted.
5.  Click the *OK* button.

If you are using the Windows App tool, you should see a window similar to the expected interface. To connect to your Windows VM:

1.  Select *Add* from the menu on the left.
2.  Enter the public IP address next to *PC Name*.
3.  Click the *Add & Connect* button at the bottom.
4.  Enter the password when prompted.
5.  Click the *OK* button.

You will likely be presented with an alert "The identity of the remote computer cannot be verified. Do you want to connect anyway?". This is normal; click *Yes* to continue. Once you connect, you should see the desktop of your Windows VM displayed within the RDC window.

!!! question "TODO: Certificate Error"
    The specific certificate error is "The certificate is not from a trusted certifying authority". Is seeing this alert really normal? Do we want to register the Windows image certificate with a signing authority? Could we use Let's Encrypt or should we just ignore this issue?

#### From a Linux client

To connect via RDP from Linux, you will need a remote desktop client. There are a number of different clients out there, but the [Remmina client](https://github.com/FreeRDP/Remmina/wiki) appears to work well when tested with Ubuntu. The previous link provides instructions for installing it in Ubuntu, Debian, Fedora, and a few other Linux operating systems.

Once you have installed and launched Remmina to connect to your Windows VM:

1.  Click on *Create a new remote desktop file* (file with a green '+' sign). You should see a window similar to the expected interface.
2.  Enter the public IP of your Windows VM next to *Server*.
3.  Enter the user name you were provided next to *User name*.
4.  Enter the password next to *Password*.
5.  Click *Connect*.

#### From a Mac client

To connect via RDP from macOS, you will need a remote desktop client. There are a number of different clients, but the Windows App appears to work well. To install the client, go to the App Store and search for *Windows App*.

When you have installed and launched Windows App, to connect to your Windows VM:

1.  Select *Devices* from the menu on the left.
2.  Select + in the top right corner, and select *Add PC*.
3.  Enter the public IP address next to *PC Name*.
4.  Click the *Add* button at the bottom.
5.  Double-click the newly created tile.
6.  Enter the username *Administrator* and the password when prompted.
7.  Click the *Continue* button.

### Licence information

!!! question "TODO: Licence Information"
    More information is needed here to help users understand what path to take to get a licence. This should cover:
    *   Where to go to get a licence.
    *   What kind of licence is needed/what licences will work on the cloud.
    *   How to apply a licence to an existing cloud VM.
    *   How to apply it to a new VM (if that is different than the above bullet item).

### Where to go from here

*   Learn about [security considerations when running a VM](security_considerations_when_running_a_vm.md)
*   Learn about [creating a Linux VM](cloud_quick_start.md)
*   Learn more about working with [OpenStack](managing_your_cloud_resources_with_openstack.md)
*   [Cloud Technical Glossary](cloud_technical_glossary.md)
*   [Automating VM creation](automating_vm_creation.md)
*   [Backing up your VM](backing_up_your_vm.md)
*   For questions about our cloud service, email [technical support](../support/technical_support.md).