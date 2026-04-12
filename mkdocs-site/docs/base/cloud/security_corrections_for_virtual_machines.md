---
title: "Security corrections for virtual machines"
slug: "security_corrections_for_virtual_machines"
lang: "base"

source_wiki_title: "Security corrections for virtual machines"
source_hash: "9846ca6b29303ef64128e731ae010597"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:26:09.339752+00:00"

tags:
  []

keywords:
  - "SSL Certificate"
  - "HTTP TRACE / TRACK"
  - "security issues"
  - "virtual machines"
  - "Apache configuration"

questions:
  - "Why might a virtual machine owner receive communications from the cloud services security team?"
  - "How can an administrator disable HTTP TRACE and TRACK methods in an Apache server configuration?"
  - "What steps should be taken to resolve default SSL certificate errors such as self-signed or untrusted certificates in Apache?"
  - "Why might a virtual machine owner receive communications from the cloud services security team?"
  - "How can an administrator disable HTTP TRACE and TRACK methods in an Apache server configuration?"
  - "What steps should be taken to resolve default SSL certificate errors such as self-signed or untrusted certificates in Apache?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note
    If you are responsible for one or more virtual machines running in our cloud services, you may occasionally receive communications from our security team containing a list of security issues which have been detected on your VMs. Here are suggested solutions to some issues which are commonly identified.

## HTTP TRACE / TRACK Methods Allowed

You can disable this in Apache by doing the following:

1.  Add the line `TraceEnable off` to a configuration file such as `/etc/httpd/conf.d/custom.conf`.
2.  Restart the `httpd` service.

## SSL Certificate Expiry, SSL Certificate Cannot Be Trusted, SSL Self-Signed Certificate, HSTS Missing From HTTPS Server

If you manage your own domain name for your VM, these error messages may be caused by Apache's default configuration, which serves a self-signed certificate that is installed when you install Apache. A simple solution is to tell Apache to not reply to requests other than your configured virtual hosts. This is done by removing the entire section for the default configuration, such as

```apache
<VirtualHost _default_:443>
...
</VirtualHost>
```

from your `/etc/httpd/conf.d/ssl.conf` file and then restarting the `httpd` service.