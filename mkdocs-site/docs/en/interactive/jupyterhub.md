---
title: "JupyterHub/en"
slug: "jupyterhub"
lang: "en"

source_wiki_title: "JupyterHub/en"
source_hash: "cedf5631d6d32455a8f1849d052ea1f6"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:38:16.931771+00:00"

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

*JupyterHub is the best way to serve Jupyter Notebook for multiple users. It can be used in a class of students, a corporate data science group or scientific research group.*

JupyterHub provides a preconfigured version of JupyterLab and/or Jupyter Notebook; for more configuration options, please check the [Jupyter](jupyter.md) page.

!!! warning "Running notebooks"
    Jupyter Lab and notebooks are meant for **short** interactive tasks such as testing, debugging or quickly visualize data (few minutes). Running longer analysis must be done in a [non-interactive job (sbatch)](running_jobs.md#use-sbatch-to-submit-jobs).
    See also [how to run notebooks as python scripts below](#running-notebooks-as-python-scripts).

## Alliance initiatives

Some regional initiatives offer access to computing resources through JupyterHub.

### JupyterHub on clusters

On the following clusters[<sup>‡</sup>](#clusters_note), use your Alliance username and password to connect to JupyterHub:

| JupyterHub | Comments |
| :--------- | :------- |
| **[Fir](https://jupyterhub.fir.alliancecan.ca/)** | Provides access to JupyterLab servers spawned through jobs on the [Fir](fir.md) cluster. |
| **[Narval](https://jupyterhub.narval.alliancecan.ca/)** | Provides access to JupyterLab servers spawned through jobs on the [Narval](narval.md) cluster. |
| **[Rorqual](https://jupyterhub.rorqual.alliancecan.ca/)** | Provides access to JupyterLab servers spawned through jobs on the [Rorqual](rorqual.md) cluster. |

Some clusters provide access to JupyterLab through Open OnDemand. See [JupyterLab](jupyterlab.md) for more information.

<sup id="clusters_note">‡</sup> **Note that the compute nodes running the Jupyter kernels do not have internet access**. This means that you can only transfer files from/to your own computer; you cannot download code or data from the internet (e.g. cannot do "git clone", cannot do "pip install" if the wheel is absent from our [wheelhouse](available_python_wheels.md)). You may also have problems if your code performs downloads or uploads (e.g. in machine learning where downloading data from the code is often done).

### JupyterHub for universities and schools

* The [Pacific Institute for the Mathematical Sciences](https://www.pims.math.ca) in collaboration with the Alliance and [Cybera](http://www.cybera.ca) offer cloud-based hubs to universities and schools. Each institution can have its own hub where users authenticate with their credentials from that institution. The hubs are hosted on Alliance [clouds](cloud.md) and are essentially for training purposes. Institutions interested in obtaining their own hub can visit [Syzygy](http://syzygy.ca).

## Server options

Once logged in, depending on the configuration of JupyterHub, the user's web browser is redirected to either
**a)** a previously launched Jupyter server,
**b)** a new Jupyter server with default options, or
**c)** a form that allows a user to set different options for their Jupyter server before pressing the *Start* button.
In all cases, it is equivalent to accessing requested resources via an [interactive job](running_jobs.md#interactive-jobs) on the corresponding cluster.

**Important:** On each cluster, only one interactive job at a time gets a priority increase in order to start in a few seconds or minutes. That includes `salloc`, `srun` and JupyterHub jobs. If you already have another interactive job running on the cluster hosting JupyterHub, your new Jupyter session may never start before the time limit of 5 minutes.

### Compute resources

For example, *Server Options* available on [Béluga's JupyterHub](https://jupyterhub.beluga.computecanada.ca/) are:
* *Account* to be used: any `def-*`, `rrg-*`, `rpp-*` or `ctb-*` account a user has access to
* *Time (hours)* required for the session
* *Number of (CPU) cores* that will be reserved on a single node
* *Memory (MB)* limit for the entire session
* (Optional) *GPU configuration*: at least one GPU
* *[User interface](#user-interface)* (see below)

### User interface

While JupyterHub allows each user to use one Jupyter server at a time on each hub, there can be multiple options under *User interface*:
* **[JupyterLab](jupyterlab.md)** (modern interface): This is the most recommended Jupyter user interface for interactive prototyping and data visualization.
* Jupyter Notebook (classic interface): Even though it offers many functionalities, the community is moving towards [JupyterLab](#jupyterlab), which is a better platform that offers many more features.
* Terminal (for a single terminal only): It gives access to a terminal connected to a remote account, which is comparable to connecting to a server through an SSH connection.

!!! note
    JupyterHub could also have been configured to force a specific user interface. This is usually done for special events.

## JupyterLab

The JupyterLab interface is now described in our [JupyterLab](jupyterlab.md) page.

## Troubleshooting

### "Spawn failed: Timeout"

Most JupyterHub errors are caused by the underlying job scheduler which is either unresponsive or not able to find appropriate resources for your session. For example:

* When starting a new session, JupyterHub automatically submits on your behalf a new [interactive job](running_jobs.md#interactive-jobs) to the cluster. If the job does not start within five minutes, a "Timeout" error message is raised and the session is cancelled.
    * Just like any interactive job on any cluster, a longer requested time can cause a longer wait time in the queue. Requesting a GPU or too many CPU cores can also cause a longer wait time. Make sure to request only the resources you need for your session.
    * If you already have another interactive job on the same cluster, your Jupyter session will be waiting along with other regular batch jobs in the queue. If possible, stop or cancel any other interactive job before using JupyterHub.
    * There may be just no resource available at the moment. Check the [status page](https://status.alliancecan.ca/) for any issue and try again later.

### "Authentication error: Error 403"

Your account or your access to the cluster is currently inactive:
1. Make sure your account is active, that is [**it has been renewed**](https://alliancecan.ca/en/services/advanced-research-computing/account-management/account-renewals)
2. Make sure your [**access to a cluster**](https://ccdb.alliancecan.ca/me/access_services) is enabled

### Startup hangs

If JupyterHub posts the message "Your server is starting up. You will be redirected automatically when it's ready for you" and stays there indefinitely:
* Check for the problems described above under "Spawn failed: Timeout".
* If none of those seem to apply, log on to the cluster with an ordinary SSH client (since JH doesn't work).
* Use `sq` to identify the Slurm job corresponding to your JupyterHub session.
* Cancel the Slurm job with `scancel`.
* Delete hidden Jupyter files with
    ```bash
    cd ~
    rm -r .local/share/jupyter
    rm -r .jupyter
    ```
* Try again. (Jupyter will recreate the hidden files.)

## References
* [JupyterHub documentation](http://jupyterhub.readthedocs.io/en/latest/index.html)