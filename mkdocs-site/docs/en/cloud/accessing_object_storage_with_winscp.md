---
title: "Accessing object storage with WinSCP/en"
tags:
  - cloud

keywords:
  - Amazon S3
  - Access Control Lists
  - WinSCP
  - Arbutus object storage
  - Configuration
---

This page contains instructions on how to set up and access [Arbutus object storage](arbutus-object-storage.md) with WinSCP, one of the [object storage clients](arbutus_object_storage_clients.md) available for this storage type.

## Installing WinSCP 
WinSCP can be installed from https://winscp.net/.

## Configuring WinSCP 
Under "New Session", make the following configurations:
<ul>
<li>File protocol: Amazon S3</li>
<li>Host name: object-arbutus.alliancecan.ca</li>
<li>Port number: 443</li>
<li>Access key ID: 20_DIGIT_ACCESS_KEY</li>
</ul>
and "Save" these settings as shown below

[600px|thumb|center|WinSCP configuration screen](file:winscp-configuration.png.md)

Next, click on the "Edit" button and then click on "Advanced..." and navigate to "Environment" to "S3" to "Protocol options" to "URL style:" which <b>must</b> changed from "Virtual Host" to "Path" as shown below:

[600px|thumb|center|WinSCP Path Configuration](file:winscp-path-configuration.png.md)

This "Path" setting is important, otherwise WinSCP will not work and you will see hostname resolution errors, like this:
[400px|thumb|center|WinSCP resolve error](file:winscp-resolve-error.png.md)

## Using WinSCP 
Click on the "Login" button and use the WinSCP GUI to create buckets and to transfer files:

[800px|thumb|center|WinSCP file transfer screen](file:winscp-transfers.png.md)

## Access Control Lists (ACLs) and Policies 
Right-clicking on a file will allow you to set a file's ACL, like this:
[400px|thumb|center|WinSCP ACL screen](file:winscp-acl.png.md)