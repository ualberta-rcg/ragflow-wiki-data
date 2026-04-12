---
title: "OpenStack command line clients/en"
slug: "openstack_command_line_clients"
lang: "en"

source_wiki_title: "OpenStack command line clients/en"
source_hash: "29166a2a11d49dd1846a7a97c79b8025"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:05:37.796998+00:00"

tags:
  - cloud

keywords:
  - "command-line interfaces"
  - "command group"
  - "command line tool"
  - "glance"
  - "individual commands"
  - "server command group"
  - "installation"
  - "OpenStack RC file"
  - "extra functionality"
  - "separate components"
  - "heat"
  - "average user"
  - "components"
  - "OpenStack"
  - "server commands"
  - "nova"
  - "cinder"
  - "openstack command"
  - "Python"
  - "available commands"
  - "command groups"

questions:
  - "How do you install the OpenStack command line tools on different Linux distributions or without administrative privileges?"
  - "What is the process for connecting and authenticating the command line client to an OpenStack project using an RC file?"
  - "How can users execute commands and access the built-in help features within the OpenStack CLI?"
  - "What are the primary command groups and their associated subcommands available within the unified OpenStack command-line interface?"
  - "What is the purpose of having separate command-line interfaces in addition to the unified openstack command?"
  - "Are any additional installation steps required to use the separate component-specific commands after installing the main openstack command?"
  - "Why are the available commands grouped by command groups in this document?"
  - "What is the name of the specific command group detailed in the provided text?"
  - "What are some examples of the specific commands that can be executed within the server command group?"
  - "What is the primary advantage of using the individual OpenStack component commands instead of the unified command?"
  - "How are the separate component commands installed in relation to the main openstack command?"
  - "What specific information is expected to be listed immediately following this text passage?"
  - "What are the specific functions of the nova, glance, cinder, and heat commands within the OpenStack environment?"
  - "Where can users find the official documentation and manuals for these OpenStack command-line tools?"
  - "What overarching technology category do these specific command-line tools belong to?"
  - "What are the specific functions of the nova, glance, cinder, and heat commands within the OpenStack environment?"
  - "Where can users find the official documentation and manuals for these OpenStack command-line tools?"
  - "What overarching technology category do these specific command-line tools belong to?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Managing your cloud resources with OpenStack](managing-your-cloud-resources-with-openstack.md)*

The [OpenStack command line tool](http://docs.openstack.org/developer/python-openstackclient/) allows you to perform many of the actions provided by the OpenStack dashboard GUI, as well as providing some functionality which the dashboard does not. The command line client can be used from any machine, virtual or otherwise, and only requires having an internet connection and the client installed. The discussion below assumes that it is being used on a Linux machine.

## Installation
The OpenStack command line tools are Python-based. You can install and run them on your personal computer or on a cloud VM. Different Linux distributions may have pre-built packages for the client, see the OpenStack [installation documentation](https://docs.openstack.org/user-guide/common/cli-install-openstack-command-line-clients.html) for more details. You can quickly install both Python and the OpenStack command line tools if you have administrative privileges on your machine.

**Ubuntu**
```bash
sudo apt-get install python python-dev python-pip
sudo pip install python-openstackclient
```
**CentOS 7**
Run as root
```bash
yum install epel-release
yum install gcc python python-dev python2-pip
pip install python-openstackclient
```
**Fedora**
```bash
sudo dnf install python-openstackclient
```
**Note:** If you do not have administrative privileges and cannot use the OS package manager, then you will need to install Python and [pip](https://pip.pypa.io/en/latest/installing/) by other means. Once installed, you can get the command line tools installed into your home space like so:
```bash
pip install --user python-openstackclient
```
The install location is probably already included in your `$PATH`, but you can double check whether `~/.bashrc` or `~/.bash_profile` contains the following line `PATH=$PATH:$HOME/.local/bin:$HOME/bin`

**SDK**
If you wish to explore the [OpenStack API for Python](http://docs.openstack.org/user-guide/sdk.html), add `export PYTHONPATH=${HOME}/.local/lib/python2.7/site-packages/:${PYTHONPATH}` to your `.bashrc` file. Adjust the `python2.7` phrase to match the Python version you have installed.

## Connecting CLI to OpenStack
Your command line client must now be told how to find your OpenStack project on our clouds.
The most convenient way to do this is to download an OpenStack environment setup file. On the OpenStack dashboard go to Project-> API Access-> Download OpenStack RC File.

Then source the file with something like
```bash
source <project name>-openrc.sh
```
It will ask you for your OpenStack password, which is simply your CCDB password. Test your setup by typing
```bash
openstack image list
```

!!! warning
    If you switch between different RC files you should be careful of environment variables which may still be set from the previous RC file; these may cause your OpenStack client commands to fail. Either ensure that all environment variables set in the RC file are unset with `unset <variable-name>`, or start a fresh new session without any of the RC environment variables set.

## Executing commands
The CLI tool can be used interactively by typing
```bash
openstack
```
and then issuing commands at the prompt. Alternatively, the commands can be issued as one-offs by preceding the command with `openstack`, for example
```bash
openstack server list
```
When running in interactive mode a list of available commands can be seen by typing `help` at the OpenStack prompt. The available commands are categorized by groups; many of the most commonly used groups are listed below. A list of commands belonging to a command group can be obtained by typing `help <command group>`. To get help on a particular command (e.g. options and arguments of the command) one can type `help <command group> <command>`. Note that many commands are available only to OpenStack administrators and will return an error message if a non-administrator tries using it. For this reason a list of available commands grouped by command groups is provided below to allow one to easily identify commands available to the average user.

## Command groups
### `server` command group

| `add security group` | `migrate`             | `resume`                | `unlock`           |
|----------------------|-----------------------|-------------------------|--------------------|
| `add volume`         | `pause`               | `set`                   | `unpause`          |
| `create`             | `reboot`              | `shelve`                | `unrescue`         |
| `delete`             | `rebuild`             | `show`                  | `unset`            |
| `dump create`        | `remove security group` | `ssh`                   | `unshelve`         |
| `image create`       | `remove volume`       | `start`                 |                    |
| `list`               | `rescue`              | `stop`                  |                    |
| `lock`               | `resize`              | `suspend`               |                    |

### `volume` command group

| `create` | `set`   |
|----------|---------|
| `delete` | `show`  |
| `list`   | `unset` |

### `console` command group

| `log show` | `url show` |
|------------|------------|

### `flavor` command group

| `list` | `show` |
|--------|--------|

### `image` command group

| `create` | `save` |
|----------|--------|
| `delete` | `set`  |
| `list`   | `show` |

### `ip` command group

| `fixed add`       | `floating list`      |
|-------------------|----------------------|
| `fixed remove`    | `floating pool list` |
| `floating add`    | `floating remove`    |
| `floating create` | `floating show`      |
| `floating delete` |                      |

### `keypair` command group

| `create` | `list` |
|----------|--------|
| `delete` | `show` |

### `network` command group

| `create` | `set`  |
|----------|--------|
| `delete` | `show` |
| `list`   |        |

### `snapshot` command group

| `create` | `set`   |
|----------|---------|
| `delete` | `show`  |
| `list`   | `unset` |

### `security group` command group

| `create`    | `rule list` |
|-------------|-------------|
| `delete`    | `rule show` |
| `list`      | `set`       |
| `rule create` | `show`      |
| `rule delete` |             |

### `limits` command group

| `show` | |
|--------|---|

## Separate Command-line interfaces
In addition to the `openstack` command described above which incorporates much of the total functionality available into one command there are also individual commands to work with the separate components of OpenStack which often have extra functionality. These separate commands are installed at the same time as the `openstack` command, as described above, so no further installation is required to use them. A list of the commands for working with common components of OpenStack are:
*   `nova`: for working with servers, see [OpenStack docs for nova command](https://docs.openstack.org/python-novaclient/latest/cli/nova.html).
*   `glance`: for working with images, see [OpenStack docs for glance command](https://docs.openstack.org/python-glanceclient/latest/cli/glance.html).
*   `cinder`: for working with volumes, see [OpenStack docs for cinder command](https://docs.openstack.org/python-cinderclient/latest/user/shell.html).
*   `heat`: for working with orchestration, see [OpenStack docs for heat command](https://docs.openstack.org/python-heatclient/latest/man/heat.html).