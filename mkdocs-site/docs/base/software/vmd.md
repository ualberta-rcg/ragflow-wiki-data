---
title: "VMD"
slug: "vmd"
lang: "base"

source_wiki_title: "VMD"
source_hash: "4946e266d9bf9f6b396e45240bef8ca8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:32:42.491802+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "biomolecular systems"
  - "molecular visualization"
  - "VMD"
  - "installation"
  - "plugins"

questions:
  - "What is VMD and what is the recommended method to connect to a cluster to run its pre-installed version?"
  - "What are the step-by-step instructions for manually installing VMD version 1.9.4 Alpha in a user's local directory?"
  - "How can a user install additional VMD plugins, such as CaFE, and configure the system to recognize them?"
  - "What is VMD and what is the recommended method to connect to a cluster to run its pre-installed version?"
  - "What are the step-by-step instructions for manually installing VMD version 1.9.4 Alpha in a user's local directory?"
  - "How can a user install additional VMD plugins, such as CaFE, and configure the system to recognize them?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

"VMD is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting."
The VMD web site is [here](https://www.ks.uiuc.edu/Research/vmd/).

## Using a pre-installed version

Connect to a cluster using [VNC](../interactive/vnc.md), `ssh -X`, or `ssh -Y`, in order to enable graphics.

!!! tip
    We recommend using VNC for best performance.

To run the default version of VMD, currently `1.9.4a57`, do:

```bash
module load vmd
vmd
```

This should open VMD graphical windows.

See [Using modules](using-modules.md) for more on the `module` command, including how to find and use other pre-installed versions.

## Installing version 1.9.4 Alpha

1.  Download the 1.9.4 LATEST ALPHA tar file from [http://www.ks.uiuc.edu/](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD), selecting the LINUX_64 version. Free registration is required.

2.  Copy the file to the home directory of the cluster you wish to use.

3.  Unpack the file:

```bash
tar xvf vmd-1.9.4*.opengl.tar.gz
```

4.  Enter the newly-created directory:

```bash
cd vmd-1.9.4*
```

5.  Create two new directories to receive the program files:

```bash
mkdir ~/vmd_install
mkdir ~/vmd_library
```

5.  Edit the `configure` file to read as follows, replacing each instance of `your_user_name` with your actual user name:

```text title="configure"
# Directory where VMD startup script is installed, should be in users' paths.
$install_bin_dir="/home/your_user_name/vmd_install";

# Directory where VMD files and executables are installed
$install_library_dir="/home/your_user_name/vmd_library";
```

6.  Run `configure` and `make`:

```bash
./configure
cd src
make install
```

7.  Add the resulting executable to your path:

```bash
export PATH=~/vmd_install:$PATH
```

8.  Use `setrpaths.sh` to modify the VMD executables so they use libraries from CVMFS:

```bash
cd ~/vmd_library/
setrpaths.sh --path .
```

!!! note
    If you are using a Mac and getting a blank window, try running this:

    ```bash
    defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
    ```

## Installing plugins

VMD has many plugins available. You can install them in your own space.
The example that follows illustrates how to install the [CaFE plugin](https://github.com/HuiLiuCode/CaFE_Plugin),
from detailed instructions which can be found [here](https://github.com/HuiLiuCode/CaFE_Plugin/blob/master/doc/manual.pdf):

```bash
wget https://github.com/HuiLiuCode/CaFE_Plugin/archive/refs/heads/master.zip
unzip master.zip
cd CaFE_Plugin-master
mv src cafe1.0
mv cafe1.0 ~
cd
```

Edit the `.vmdrc` file with your favourite editor (`nano, vim, emacs` etc.) and add this line:

```tcl
set auto_path [linsert $auto_path 0 {~/cafe1.0}]
```

After this, load the `vmd` module and any other modules which are required, such as `namd` and the CaFE plugin should be available.

## Links

*   WestGrid webinars (in English)
    *   [Molecular visualization with VMD](https://www.youtube.com/watch?v=_skmrS6X4Ys)
    *   [Advanced VMD: Trajectories, movies, scripting](https://www.youtube.com/watch?v=Jce5JN2fLuo)