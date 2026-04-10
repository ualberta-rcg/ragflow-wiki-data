---
title: "Classiq"
slug: "classiq"
lang: "base"

source_wiki_title: "Classiq"
source_hash: "e70f0d93f679e43e75cb902b526124b1"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:26:23.345940+00:00"

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

[Classiq](https://www.classiq.io/) is quantum computing software that lets you design, optimize, and execute quantum programs and is free to use for academic researchers (sign up on [classiq.io](https://www.classiq.io/) with an institutional email).

The software can be used via their online platform, [platform.classiq.io](https://platform.classiq.io/). Execution of quantum programs designed and optimized with Classiq can be run on multiple provider backends. Classiq also provides a [Python SDK](https://docs.classiq.io/latest/sdk-reference/) that can be used on other platforms.

!!! note
    While Classiq is largely hardware independent for execution, synthesizing (compiling) quantum programs with Classiq requires use of the Classiq platform via their API and requires authentication. Therefore, even if using local execution, synthesis can only be done on compute nodes with internet access. As such, [Fir](fir.md) and [Nibi](nibi.md) are suitable choices for using Classiq.

## Installation

Installation on Alliance clusters is straightforward. Classiq will work with all versions of Python >= 3.11:

```bash
module load python/3.11 scipy-stack/2025a
virtualenv --no-download ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index classiq
```

## Authentication on Alliance Clusters

Before using the Python SDK with Classiq, you will need to authenticate with Classiq on one of the login nodes. This requires first signing up for an account with Classiq at [platform.classiq.io](https://platform.classiq.io/#sign-up). In order to obtain the free academic use license, please sign up using your institutional email.

1.  Sign up for an account with Classiq at [platform.classiq.io](https://platform.classiq.io/#sign-up)

2.  Proceed with installation of the [Python SDK](https://docs.classiq.io/latest/sdk-reference/) using the instructions above.

3.  Activate the virtual environment in which you installed Classiq and start a Python terminal.

    ```bash
    (ENV) [user@server ~]$ python
    ```
    ```python
    Python 3.11.5 (main, Sep 19 2023, 16:07:22) [GCC 12.3.1 20230526] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

4.  Import the `authenticate` module and run the authentication, this will open a browser window, press "q" and confirm with "Y" to exit the browser:

    ```python
    >>> from classiq import authenticate
    >>> authenticate()
    ```

5.  After quitting the browser, you will see a message, giving a URL to the authentication website. You can copy and paste this website into a browser on your own computer and sign into Classiq to verify:

    ```python
    >>> authenticate()
    If a browser doesn't automatically open, please visit this URL from any trusted device to authenticate: <URL>
    Your user code: <XXXX-XXXX>
    ```

6.  Verify the user code given on the Classiq website matches that shown in the terminal on the cluster and proceed with authentication.