---
title: "Security corrections for virtual machines"
slug: "security_corrections_for_virtual_machines"
lang: "base"

source_wiki_title: "Security corrections for virtual machines"
source_hash: "9846ca6b29303ef64128e731ae010597"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:15:37.659226+00:00"

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

If you are responsible for one or more virtual machines running in our cloud services, you may occasionally receive communications from our security team containing a list of security issues which have been detected on your VMs.
Here are suggested solutions to some issues which are commonly identified.

## HTTP TRACE / TRACK Methods Allowed

You can disable this in Apache by doing the following:
1. Add the line `TraceEnable off` to a configuration file such as `/etc/httpd/conf.d/custom.conf`.
2. Restart the `httpd` service.

## SSL Certificate Expiry, SSL Certificate Cannot Be Trusted, SSL Self-Signed Certificate, HSTS Missing From HTTPS Server

If you manage your own domain name for your VM, these error messages may be caused by Apache's default configuration, which serves a self-signed certificate that is installed when you install Apache. A simple solution is to tell Apache to not reply to requests other than your configured virtual hosts. This is done by removing the entire section for the default configuration, such as
```apache
<VirtualHost _default_:443>
...
</VirtualHost>
```
from your `/etc/httpd/conf.d/ssl.conf` file and then restarting the `httpd` service.