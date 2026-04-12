---
title: "OpenStack dashboard GUI"
slug: "openstack_dashboard_gui"
lang: "base"

source_wiki_title: "OpenStack dashboard GUI"
source_hash: "7ecbd198511f503ba7a3419d07db01ce"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:06:14.878486+00:00"

tags:
  - cloud

keywords:
  - "cloud project"
  - "OpenStack command line clients"
  - "OpenStack dashboard GUI"
  - "virtual machines"
  - "Horizon"

questions:
  - "What functionalities does the OpenStack dashboard GUI provide for managing a cloud project?"
  - "What prerequisite must be met before a user can sign in to the dashboard GUI for a specific cloud site?"
  - "What alternative tool can be used to perform actions that are not supported by the dashboard GUI?"
  - "What functionalities does the OpenStack dashboard GUI provide for managing a cloud project?"
  - "What prerequisite must be met before a user can sign in to the dashboard GUI for a specific cloud site?"
  - "What alternative tool can be used to perform actions that are not supported by the dashboard GUI?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## OpenStack dashboard GUI
The OpenStack dashboard GUI allows you to manage various aspects of your OpenStack cloud project. This includes creating and managing virtual machines (VMs) and networks. The GUI is based on software from the OpenStack project called Horizon. The GUI can be used from any machine, virtual or otherwise, and only requires an internet connection and a web browser. For example, the dashboard shows a project's used resources and available quota.

The [OpenStack command line clients](openstack_command_line_clients.md) allow you to perform functionality that the dashboard does not.

## Dashboard GUI
The URL to access the dashboard GUI varies by site:
*   [Arbutus](https://arbutus.cloud.computecanada.ca)
*   [Béluga cloud](https://beluga.cloud.computecanada.ca)
*   [Cedar](http://cedar.cloud.computecanada.ca)
*   [Graham](https://graham.cloud.computecanada.ca)

!!! note
    You must have a project on the cloud site in order to sign in to the respective URL(s). For questions about obtaining a project, please read [this page](https://docs.alliancecan.ca/wiki/Cloud#Getting_a_Cloud_project).

## Dashboard GUI documentation
See [The OpenStack End User documentation](https://docs.openstack.org/horizon/latest/user) for more details on how to use the dashboard GUI.