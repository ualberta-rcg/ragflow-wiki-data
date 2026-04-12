---
title: "Securing your account/en"
slug: "securing_your_account"
lang: "en"

source_wiki_title: "Securing your account/en"
source_hash: "0bdbbe6a30639f93d47c4febd3b2731e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:24:22.645932+00:00"

tags:
  []

keywords:
  - "Multifactor authentication"
  - "Authentication"
  - "Passwords"
  - "SSH keys"
  - "Security best practices"

questions:
  - "What are the recommended best practices for securely managing passwords and SSH keys when authenticating to the cluster?"
  - "How does multifactor authentication (MFA) function to provide an additional layer of security beyond standard login credentials?"
  - "What general security measures should users implement on their local computers and remote systems to prevent unauthorized access and safely share data?"
  - "What are the recommended best practices for securely managing passwords and SSH keys when authenticating to the cluster?"
  - "How does multifactor authentication (MFA) function to provide an additional layer of security beyond standard login credentials?"
  - "What general security measures should users implement on their local computers and remote systems to prevent unauthorized access and safely share data?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Authentication
There are two primary authentication mechanisms that are used to connect to a cluster: passwords and SSH keys. Below are some best practices for both methods.

## Password best practices
* Users are strongly encouraged to use unique passwords, and to never reuse them.
* Passwords are sensitive confidential information and users must never share or disclose them by any means. Users should also refrain from disclosing tips that could help identify their passwords.
* Users are encouraged to never write down a password. In the situation where a user needs to write or store their password on a given media, it is acceptable to do so given that the appropriate security measures to prevent unauthorized access are in place (encryption, strong password protection, etc.). A user should never store or write a password to facilitate access or transfer between information systems.
* Users are encouraged to not use the "remember your password" feature of browser or operating systems.

### Resetting your password
If you think that your password may have been compromised, you can reset it through [this page](https://ccdb.computecanada.ca/security/change_password).

## SSH keys best practices
SSH keys can be a good way to authenticate to your account without typing your password every time. However, to be secure, it is **imperative that SSH keys use a strong passphrase** that is treated like a password.

!!! warning "SSH Private Key Security"
    Treat the private key as a security token, even when encrypted with a passphrase. Avoid putting a private key on any shared machine. Placing an unencrypted private key on the clusters is a huge security hole.

For technical details on implementing SSH keys for your account, please see [this page](ssh-keys.md).

## Multifactor authentication
Multifactor authentication (MFA) allows you to protect your account with more than a password or an SSH key. Once your account is configured to use MFA, you will need to enter your username and password or SSH key as usual, and then perform a second action (the second factor) to access most of our services.

!!! tip "Activate Multifactor Authentication (MFA)"
    It is highly recommended to activate MFA on your account. Please see the [Multifactor authentication](multifactor-authentication.md) page for more details.

# General best practices

## Sharing data
When sharing data among collaborators, it may seem convenient to change filesystem permissions to allow everyone to read or write some files. This can compromise your account if not done properly. Please see our [Sharing data](sharing-data.md) page.

## For the system you log in from
Security issues often start on the outside, by a third party getting access to a user's password or (passwordless) SSH key. To help prevent this, please:
* Log in from trusted computers only;
* On Windows computers, make sure to regularly run a virus scanner and malware scanner;
* Regardless of what Operating System you have, keep up to date with security updates for all software;
* Do not leave your computer or laptop unattended.
* On clients that use OpenSSH (Linux, Mac and as an option under Windows), you can configure SSH behaviour using `~/.ssh/config`. In particular, you can define system and even username-specific behaviour, such as selecting specific keys to use, or automatically selecting advanced features such as X/port forwarding, and even ProxyJump.

## For the system you log in to
One important advantage of using SSH keys is that the remote system only needs your public key. This value is not sensitive, so there is no risk of it being disclosed. If someone gets your public key, all they can do is give you additional access.

!!! warning "Private Keys on Remote Systems"
    Avoid placing any private keys on remote machines, even encrypted ones. An unencrypted key is equivalent to a password, and may be stolen or exposed inadvertently. An encrypted key is, by itself, not sensitive - except if you ever use it on that machine (at which point you are effectively trusting the machine.)

* If you use ssh-agent, avoid forwarding it to remote machines which you do not trust.