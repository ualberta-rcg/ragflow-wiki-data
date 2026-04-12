---
title: "FTP server in the Cloud"
slug: "ftp_server_in_the_cloud"
lang: "base"

source_wiki_title: "FTP server in the Cloud"
source_hash: "ae910dabdcc9426abf7a911de3428e22"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:01:18.043151+00:00"

tags:
  - cloud

keywords:
  - "open ports"
  - "FTP"
  - "FTPS"
  - "security risks"
  - "SFTP"

questions:
  - "What are the recommended secure alternatives to FTP for anonymous read-only access and authenticated user access?"
  - "Why does the text strongly advise against using password logins for virtual machines, and what authentication method is suggested instead?"
  - "Which network ports must be opened to configure an FTP server, and how does this requirement impact the security of the virtual machine?"
  - "What are the recommended secure alternatives to FTP for anonymous read-only access and authenticated user access?"
  - "Why does the text strongly advise against using password logins for virtual machines, and what authentication method is suggested instead?"
  - "Which network ports must be opened to configure an FTP server, and how does this requirement impact the security of the virtual machine?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Cloud](cloud.md)*

## Better alternatives to FTP
If you have the freedom to choose an alternative to FTP, consider the following options:

*   If you are considering anonymous FTP...
    *   ...for read-only access: Use HTTP (see [Creating a web server on a cloud](creating_a_web_server_on_a_cloud.md)).
    *   ...for read/write access: The security risks of accepting anonymous incoming file transfers are very great. Please [contact us](../support/technical_support.md) and describe your use case so we can help you find a secure solution.
*   If you plan to authenticate FTP users (that is, require usernames and passwords)...
    *   ...a safer and easier alternative is [SFTP](../getting-started/globus.md).
    *   Another alternative is [FTPS](https://en.wikipedia.org/wiki/FTPS), which is an extension of FTP which uses [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) to encrypt data sent and received.
    When authenticating users via passwords, the transmitted data should be encrypted or else an eavesdropper could discover the password.

    !!! warning "Avoid password logins for VMs"
        We strongly recommend that you not allow password logins to your VM, as automated brute-force attempts to crack passwords can be expected on any machine connected to the internet. Instead, use ssh-key authentication (see [SSH Keys](../getting-started/ssh_keys.md)). [SFTP](../getting-started/globus.md) can be configured to use ssh-key authentication.

## Setting up FTP
If you do not have freedom to choose an alternative to FTP, see the guide which best matches your operating system:
*   [Ubuntu guide](https://help.ubuntu.com/lts/serverguide/ftp-server.html)
*   [CentOS 6 guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-vsftpd-on-centos-6--2)

The ports that FTP uses must be open on your VM; see [this page](managing_your_cloud_resources_with_openstack.md#security-groups) for information about opening ports. FTP uses port 21 to initiate file transfer requests, but the actual transfer can take place on a randomly chosen port above port 1025, though the details of this can vary depending in which mode FTP operates. For example, port 20 can also be involved. This means that to allow FTP access on your VM, you must open port 21, possibly port 20, and probably ports 1025 and above.

!!! warning "Security Risk: Open Ports"
    Every open port represents a security risk, which is why other protocols are preferred to FTP. See [this article](http://www.techrepublic.com/article/how-ftp-port-requests-challenge-firewall-security/5031026/) for more details on ports used by FTP.