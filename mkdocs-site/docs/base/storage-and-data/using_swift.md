---
title: "Using swift"
tags:
  []

keywords:
  []
---

## Object Storage in Arbutus cloud 

The OpenStack Object Store project, known as Swift, offers cloud storage software so that you can store and retrieve lots of data with a simple API.

If you require s3 access to it, please contact our [Technical support](technical-support.md).

## Using the Object Storage via Browser 

Swift can be accessed via the openstack cli and/or via the [Cloud webinterface](https://arbutus.cloud.computecanada.ca).

{| 
|+ 
|-
| [thumb|center|Dashboard Menu](file:objectstoragemenu.png.md)  || The object storage can be accessed via the menu on the left side.
|-
| [thumb|center| Publicly accessible container](file:2.png.md)  || To store data a storage container needs to be created, which can hold the data. Multiple containers can be created if required, by clicking on **Public Access**,
the container becomes public and will be accessible by anyone. If the container has no public access, it can only be used within the projects VMs.
|-
| [thumb|center| File upload via browser](file:3.png.md) || To upload files via browser into the container, click on the upload button.
|}

## Using the Object Storage via OSA cli