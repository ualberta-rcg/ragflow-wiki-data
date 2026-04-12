---
title: "Configuring Apache to use SSL"
slug: "configuring_apache_to_use_ssl"
lang: "base"

source_wiki_title: "Configuring Apache to use SSL"
source_hash: "f93c2e4292b4830b0fc3e4d4a341b82a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:31:31.458375+00:00"

tags:
  - cloud

keywords:
  - "Certbot"
  - "Apache"
  - "SSL certificate"
  - "default-ssl.conf"
  - "SSL configuration"
  - "Transport Layer Security"
  - "HTTPS redirect"
  - "Let's Encrypt"
  - "command questions"
  - "example responses"
  - "Common Name"
  - "server FQDN"
  - "Self-signed certificate"
  - "Organization Name"

questions:
  - "Why is it important to use SSL/TLS encryption for a web server, even when sensitive information is not being transmitted?"
  - "What are the main differences between a third-party signed certificate and a self-signed certificate, and in what scenarios should each be used?"
  - "What tools and network port configurations are necessary to automatically generate and configure a signed certificate using Let's Encrypt?"
  - "What should be entered for the \"Common Name\" when setting up the SSL certificate for a virtual machine?"
  - "How do you configure Apache's SSL configuration file to use the newly created certificate and private key?"
  - "What specific directives must be added to the Apache configuration files to tighten security and force all HTTP traffic to HTTPS?"
  - "What is the purpose of the command that prompts the user for this series of questions?"
  - "What are the specific example responses provided for the geographical fields like Country, State, and Locality?"
  - "What type of information should be entered into the \"Common Name\" field according to the text?"
  - "What should be entered for the \"Common Name\" when setting up the SSL certificate for a virtual machine?"
  - "How do you configure Apache's SSL configuration file to use the newly created certificate and private key?"
  - "What specific directives must be added to the Apache configuration files to tighten security and force all HTTP traffic to HTTPS?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Creating a web server on a cloud](creating-a-web-server-on-a-cloud.md)*

!!! note "Why Use SSL/TLS?"
    Transport Layer Security (TLS) and formerly Secure Sockets Layer (SSL) are both often referred to as SSL and allow encrypted communications over computer networks. It is important to use encryption when sending any sensitive information, such as passwords, over the internet. However, even if not sending sensitive information, encrypting the data sent from the web server to the client will prevent third parties from intercepting the data and modifying it before it continues on to the client. In almost all situations, it is a good idea to use SSL certificates to encrypt data transmitted to and from a web server over the internet.

There are two main types of certificates: a certificate signed by a third-party signing authority and a self-signed certificate.

!!! warning "Self-Signed Certificate Security"
    In most cases you will want a certificate signed by a third party since it is very easy to do using Let's Encrypt, as described below. However, there may be some cases, such as testing, where you may still want to create a self-signed certificate instead. With this method, data sent to and from your web server will be encrypted, however, there is no third party involved vouching for the validity of your web server. For this reason, visitors to your site will still get a warning about the security of your site. If you have a public-facing site, you probably do not want to use a self-signed certificate.

!!! tip "Check Your SSL Configuration"
    Once you have your certificate and the web server is configured, it is a good idea to check the security settings using ssllabs' [ssltest tool](https://www.ssllabs.com/ssltest/) which can suggest changes to your configuration to improve security.

## Signed certificate
Having a certificate signed by a [Certificate Authority](https://en.wikipedia.org/wiki/Certificate_authority) (CA) allows visitors to ensure they are accessing the right website, which avoids [man-in-the-middle-attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). Many CAs require a yearly fee, but one which does not is [Let's Encrypt](https://letsencrypt.org/) CA. Certbot is a tool that automatically creates or renews an SSL certificate signed by the Let's Encrypt CA and it automatically configures your web server to use the SSL certificate. The main [Certbot](https://certbot.eff.org/) page tells you everything you need to know to get started quickly. For additional details on Cerbot, see the [Certbot docs](https://certbot.eff.org/docs/).

!!! important "Certbot Port Requirement"
    Please note that if you are configuring Certbot via Apache, then you must open port 443 (TCP ingress) in order for Certbot to connect to the site. This is not mentioned in the Certbot documentation.

## Self-signed certificate
This section describes the procedure for creating a self-signed SSL certificate as opposed to one signed by a [CA](https://en.wikipedia.org/wiki/Certificate_authority), and for configuring Apache to use it to encrypt communications.

!!! warning "Self-Signed Certificates for Production"
    Self-signed certificates should not be used for production sites, though they may be useful for small locally used sites and for testing.

!!! note "Operating System Specifics"
    The following steps assume you are using the Ubuntu operating system. If using another Linux operating system, the steps will be similar, but the details will likely be different such as commands and locations and names of configuration files.

1.  **Activate the SSL module**
    Once Apache has been installed (see [Installing Apache](creating-a-web-server-on-a-cloud.md#install-apache2)), the SSL module must be enabled with
    ```bash
    sudo a2enmod ssl
    ```
    ```bash
    sudo service apache2 restart
    ```

2.  **Create a self-signed SSL certificate**
    ```bash
    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt
    ```
    If you are asked for a pass phrase, it likely means that you missed the `-nodes` option. Please reissue the command checking it carefully against the above. This command will ask you a series of questions. Below is a list of the questions with example responses.

    ```text
    Country Name (2 letter code) [AU]:CA
    State or Province Name (full name) [Some-State]:Nova Scotia
    Locality Name (eg, city) []:Halifax
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Alliance
    Organizational Unit Name (eg, section) []:ACENET
    Common Name (e.g. server FQDN or YOUR name) []:XXX-XXX-XXX-XXX.cloud.computecanada.ca
    Email Address []:<your email>
    ```

    !!! tip "Common Name for SSL Certificate"
        The most important question to answer is the "Common Name" question which should be the domain name of your server. In the case of a virtual machine on our clouds, it should look similar to the example response except that the string of Xs should be replaced with the floating IP associated with the virtual machine.

3.  **Set ownership and permissions**
    Set the correct ownership and permissions of the private key with
    ```bash
    sudo chown root:ssl-cert /etc/ssl/private/server.key
    ```
    ```bash
    sudo chmod 640 /etc/ssl/private/server.key
    ```

4.  **Configure Apache to use the certificate**
    Edit Apache's SSL configuration file with
    ```bash
    sudo vim /etc/apache2/sites-available/default-ssl.conf
    ```
    and change the lines
    ```apache
    SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
    SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
    ```
    to
    ```apache
    SSLCertificateFile      /etc/ssl/certs/server.crt
    SSLCertificateKeyFile /etc/ssl/private/server.key
    SSLCertificateChainFile /etc/ssl/certs/server.crt
    ```
    Assuming that the `default-ssl.conf` file is the SSL version of the non-encrypted `000-default.conf` file for the site, make sure both files have the same `DocumentRoot` variables.

5.  **Tighten security**
    Force all http traffic to https, require more modern versions of SSL, and use better cipher options first by editing the file with
    ```bash
    sudo vim /etc/apache2/sites-available/default-ssl.conf
    ```
    and adding the following at the bottom of the entry inside the `<VirtualHost>` tag, replacing XXX-XXX-XXX-XXX with your VM's public IP (note the '-' are needed in place of '.'):
    ```apache
    ServerName XXX-XXX-XXX-XXX.cloud.computecanada.ca
    SSLProtocol all -SSLv2 -SSLv3
    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5:!SEED:!IDEA:!RC4
    SSLHonorCipherOrder on
    ```
    Also, put a redirect directive on our virtual host by editing the default website configuration file with
    ```bash
    sudo vim /etc/apache2/sites-available/000-default.conf
    ```
    and adding the line
    ```apache
    Redirect permanent / https://XXX-XXX-XXX-XXX.cloud.computecanada.ca
    ```
    inside the `<VirtualHost>` tag.

6.  **Enable the SSL-enabled website**
    ```bash
    sudo a2ensite default-ssl.conf
    ```
    ```bash
    sudo service apache2 restart