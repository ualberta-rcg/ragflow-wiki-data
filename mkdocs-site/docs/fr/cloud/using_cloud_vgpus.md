---
title: "Using cloud vGPUs/fr"
slug: "using_cloud_vgpus"
lang: "fr"

source_wiki_title: "Using cloud vGPUs/fr"
source_hash: "81c104819ca306add9ec45720370b515"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:23:42.212998+00:00"

tags:
  - cloud

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Cette page décrit comment :

*   allouer des ressources de GPU virtuel (vGPU) à une machine virtuelle (VM);
*   installer les pilotes nécessaires;
*   vérifier si le vGPU peut être utilisé.

L'accès aux dépôts de données ainsi qu'aux vGPU n'est actuellement disponible que sur [le nuage Arbutus](arbutus.md). Veuillez noter que la documentation ci-dessous ne couvre que l'installation du pilote vGPU. La [boîte à outils CUDA](https://developer.nvidia.com/cuda-toolkit-archive) n'est pas préinstallée, mais vous pouvez l'installer directement à partir de NVIDIA ou la charger de [la pile logicielle dans CVMFS](accessing-cvmfs.md).

!!! warning "Attention"
    Si vous optez pour une installation directe de la boîte à outils CUDA depuis NVIDIA, soyez vigilant afin que le pilote vGPU ne soit pas écrasé par le pilote CUDA inclus.

## Gabarits pris en charge

Pour utiliser un vGPU dans une machine virtuelle, l'instance doit être déployée sur l'un des gabarits mentionnés ci-dessous. Le vGPU sera disponible pour le système d'exploitation via le bus PCI.

*   g1-12gb-c3-35gb-125
*   g1-24gb-c6-70gb-250

## Préparer une machine virtuelle

Une fois que la machine virtuelle est disponible, assurez-vous de mettre à jour le système d'exploitation avec la dernière version disponible, y compris le noyau (*kernel*).

!!! important "Redémarrage requis"
    Redémarrez la machine virtuelle pour vous assurer que le dernier noyau est utilisé.

Nous recommandons l'installation de [DKMS](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support), qui est disponible par défaut dans toutes les distributions notables. Si DKMS n'installe pas automatiquement le paquet `kernel-header`, il faudra l'installer manuellement avec le gestionnaire de paquets de votre distribution.

Téléchargez sur votre ordinateur les deux fichiers suivants :

1.  **NVIDIA-Linux-x86_64-580.105.08-grid.run**
2.  **kalpa-prod.tok**

```bash
wget https://object-arbutus.alliancecan.ca/swift/v1/6c87c15eb7d2468daf3d2bd0c58bbfce/vgpu/NVIDIA-Linux-x86_64-580.105.08-grid.run
wget https://object-arbutus.alliancecan.ca/swift/v1/6c87c15eb7d2468daf3d2bd0c58bbfce/vgpu/kalpa-prod.tok
```

Installez le pilote pour vGPU de Nvidia avec la commande suivante :

```bash
chmod 755 NVIDIA-Linux-x86_64-580.105.08-grid.run && ./NVIDIA-Linux-x86_64-580.105.08-grid.run
```

Les options **NVIDIA Proprietary** et **DKMS** sont recommandées.

Quand votre installation est réussie, redémarrez l'ordinateur et utilisez `nvidia-smi` pour vérifier si le système d'exploitation a bien accès au vGPU.

```text
root@vgpudoc:/home/debian# nvidia-smi 
Thu Apr  2 19:06:00 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100L-1-12C             On  |   00000000:00:06.0 Off |                   On |
| N/A   N/A    P0            N/A  /  N/A  |       1MiB /  12288MiB |     N/A      Default |
|                                         |                        |              Enabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| MIG devices:                                                                            |
+------------------+----------------------------------+-----------+-----------------------+
| GPU  GI  CI  MIG |              Shared Memory-Usage |        Vol|        Shared         |
|      ID  ID  Dev |                Shared BAR1-Usage | SM     Unc| CE ENC  DEC  OFA  JPG |
|                  |                                  |        ECC|                       |
|==================+==================================+===========+=======================|
|  0    0   0   0  |               1MiB / 10565MiB    | 16      0 |  1   0    1    0    1 |
|                  |               0MiB /  4096MiB    |           |                       |
+------------------+----------------------------------+-----------+-----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

Le vGPU est maintenant accessible et doit être licencié. Copiez le jeton *kalpa-prod.tok* vers `/etc/nvidia/ClientConfigToken/`.

Configurez `nvidia-gridd` via la commande ci-dessous :

```bash
echo "FeatureType=4" >/etc/nvidia/gridd.conf
```

Activez `nvidia-gridd` et vérifiez son état :

```bash
systemctl enable --now nvidia-gridd
```

```text
nvidia-gridd.service - NVIDIA Grid Daemon
     Loaded: loaded (/usr/lib/systemd/system/nvidia-gridd.service; enabled; preset: enabled)
     Active: active (running) since Thu 2026-04-02 19:11:13 UTC; 19s ago
 Invocation: 11dbb0370aee4ceeb1603481991037ec
    Process: 836 ExecStart=/usr/bin/nvidia-gridd (code=exited, status=0/SUCCESS)
   Main PID: 837 (nvidia-gridd)
      Tasks: 4 (limit: 42042)
     Memory: 2M (peak: 2.7M)
        CPU: 307ms
     CGroup: /system.slice/nvidia-gridd.service
             ââ837 /usr/bin/nvidia-gridd

Apr 02 19:11:13 vgpudoc systemd[1]: Starting nvidia-gridd.service - NVIDIA Grid Daemon...
Apr 02 19:11:13 vgpudoc nvidia-gridd[837]: Started (837)
Apr 02 19:11:13 vgpudoc systemd[1]: Started nvidia-gridd.service - NVIDIA Grid Daemon.
Apr 02 19:11:13 vgpudoc nvidia-gridd[837]: vGPU Software package (0)
Apr 02 19:11:13 vgpudoc nvidia-gridd[837]: Ignore service provider and node-locked licensing
Apr 02 19:11:13 vgpudoc nvidia-gridd[837]: NLS initialized
Apr 02 19:11:14 vgpudoc nvidia-gridd[837]: Acquiring license. (Info: api.cls.licensing.nvidia.com; NVIDIA Virtual Compute Server)
Apr 02 19:11:16 vgpudoc nvidia-gridd[837]: License acquired successfully. (Info: api.cls.licensing.nvidia.com, NVIDIA Virtual Compute Server; Expiry: 2026-4-3 19:11:16 GMT)
```

Une fois que `gridd` a reçu une licence valide, toutes les fonctionnalités du vGPU peuvent être utilisées. Le renouvellement des licences est géré automatiquement par `nvidia-gridd`.