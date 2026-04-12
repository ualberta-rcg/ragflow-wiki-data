---
title: "Creating a web server on a cloud/en"
slug: "creating_a_web_server_on_a_cloud"
lang: "en"

source_wiki_title: "Creating a web server on a cloud/en"
source_hash: "d941930d8fab70c07416ce1eae3bbf59"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:36:11.539592+00:00"

tags:
  - cloud

keywords:
  - "libapache2-mod-bw"
  - "Apache bandwidth module"
  - "VirtualHost"
  - "Limiting bandwidth"
  - "sudo service apache2 restart"
  - "bandwidth limit"
  - "Web server configuration"
  - "Security considerations"
  - "Apache web server"
  - "configuration"
  - "Virtual machine"
  - "Apache2"
  - "public_html"
  - "Ubuntu Linux"

questions:
  - "What are the primary security measures and encryption practices recommended when exposing a cloud-based virtual machine to the public?"
  - "What are the necessary steps and commands to install, configure, and test an Apache web server on an Ubuntu Linux virtual machine?"
  - "How can a user change the Apache web server's default root directory to their home directory to simplify website file management?"
  - "How do you install and enable the bandwidth limiting module in Apache?"
  - "What specific configuration directives are used to limit the total client bandwidth to 100Mbps?"
  - "Where exactly should the bandwidth configuration directives be placed within the Apache site configuration files?"
  - "How can you verify that the changes made to the index.html file without using sudo have been successfully applied?"
  - "Why might a web server administrator need to limit the overall bandwidth usage of their Apache server?"
  - "What specific module is recommended to help control and limit the bandwidth resources used by an Apache web server?"
  - "How do you install and enable the bandwidth limiting module in Apache?"
  - "What specific configuration directives are used to limit the total client bandwidth to 100Mbps?"
  - "Where exactly should the bandwidth configuration directives be placed within the Apache site configuration files?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

This page describes the simplest case of creating a web server on our clouds using Ubuntu Linux and the Apache web server.

## Security considerations
Any time you make a computer accessible to the public, security must be considered. *Accessible to the public* could mean allowing SSH connections, displaying HTML via HTTP, or using third-party software to provide a service (e.g., WordPress). Services such as SSH or HTTP are provided by programs called [daemons](https://en.wikipedia.org/wiki/Daemon_(computing)), which stay running all the time on the computer and respond to outside requests on specific [ports](https://en.wikipedia.org/wiki/Port_(computer_networking)). With [OpenStack](managing-your-cloud-resources-with-openstack.md), you can manage and restrict access to these ports, including granting access only to a specific [IP address](https://en.wikipedia.org/wiki/IP_address) or to ranges of IP addresses; see [Security groups](managing-your-cloud-resources-with-openstack.md#security-groups). Restricting access to your VM will improve its security. However, restricting access does not necessarily remove all security vulnerabilities. If we do not use some sort of encryption when sending data (e.g., passwords), an eavesdropper can read that information. [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) is the common way to encrypt this data, and any website which uses logins (e.g., WordPress, MediaWiki) should use it; see [Configuring Apache to use SSL](configuring-apache-to-use-ssl.md). It is also possible that data transmitted from your web server to a client could be modified on the way by a third party if you are not encrypting it. While this might not directly cause issues for your web server, it can for your clients. In most cases, it is recommended to use encryption on your web server.

!!! warning
    You are responsible for the security of your virtual machines and should take this seriously.

## Installing Apache

1.  Create a persistent virtual machine (see [Booting from a volume](working-with-volumes.md#booting-from-a-volume)) running Ubuntu Linux by following the [Cloud Quick Start](cloud-quick-start.md) instructions.
2.  Open port 80 to allow HTTP requests into your VM by following [these instructions](cloud-quick-start.md#connecting-to-your-vm-with-ssh) but selecting HTTP from the drop-down box instead of SSH.
3.  While logged into your VM:
    1.  Update your `apt-get` repositories with the command
        ```bash
        sudo apt-get update
        ```
    2.  Upgrade Ubuntu to the latest version with the command
        ```bash
        sudo apt-get upgrade
        ```
        !!! tip
            Upgrading to the latest version of Ubuntu ensures your VM has the latest security patches.
    3.  Install the Apache web server with the command
        ```bash
        sudo apt-get install apache2
        ```
4.  Go to the newly created temporary Apache web page by entering the floating IP address of your VM into your browser's address bar. This is the same IP address you use to connect to your VM with SSH. You should see something similar to the Apache2 test page.
5.  Start modifying the content of the files in `/var/www/html` to create your website, specifically the `index.html` file, which is the entry point for your newly created website.

### Change the web server's root directory
It is often much easier to manage a website if the files are owned by the user who is connecting to the VM. In the case of the Ubuntu image we're using in this example, this is user `ubuntu`. Follow these steps to direct Apache to serve files from `/home/ubuntu/public_html`, for example, instead of from `/var/www/html`.

1.  Use the command
    ```bash
    sudo vim /etc/apache2/apache2.conf
    ```
    (or some other editor) to change the line `<Directory /var/www/>` to `<Directory /home/ubuntu/public_html>`.
2.  Use the command
    ```bash
    sudo vim /etc/apache2/sites-available/000-default.conf
    ```
    to edit the line `DocumentRoot /var/www/html` to become `DocumentRoot /home/ubuntu/public_html`.
3.  Create the directory in the Ubuntu user's home directory with
    ```bash
    mkdir public_html
    ```
4.  Copy the default page into the directory with
    ```bash
    cp /var/www/html/index.html /home/ubuntu/public_html
    ```
5.  Then restart the Apache server for these changes to take effect with
    ```bash
    sudo service apache2 restart
    ```
You should now be able to edit the file `/home/ubuntu/public_html/index.html` without using `sudo`. Any changes you make should be visible if you refresh the page you loaded into your browser in the previous section.

## Limiting bandwidth
If your web server is in high demand, it is possible that it may use considerable bandwidth resources. A good way to limit overall bandwidth usage of your Apache web server is to use the [Apache bandwidth module](https://github.com/IvnSoft/mod_bw).

### Installing
```bash
sudo apt install libapache2-mod-bw
```
```bash
sudo a2enmod bw
```

### Configuring
An example configuration to limit total bandwidth from all clients to 100Mbps is

```apacheconf
BandWidthModule On
ForceBandWidthModule On

#Exceptions to bandwidth of 100Mbps should go here above limit
#below in order to override it

#limit all connections to 100Mbps
#100Mbps *1/8(B/b)*1e6=12,500,000 bytes/s
BandWidth all 12500000
```
This should be placed between the `<VirtualHost></VirtualHost>` tags for your site. The default Apache site configuration is in the file `/etc/apache2/sites-enabled/000-default.conf`.

## Where to go from here
*   [Configuring Apache to use SSL](configuring-apache-to-use-ssl.md)
*   [Apache2 documentation](http://httpd.apache.org/docs/2.0/)
*   [w3schools HTML tutorial](http://www.w3schools.com/html/)