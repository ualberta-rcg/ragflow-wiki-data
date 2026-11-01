---
title: "Using cloud vGPUs/fr"
slug: "using_cloud_vgpus"
lang: "fr"

source_wiki_title: "Using cloud vGPUs/fr"
source_hash: "f4bdb7b6046ff36b87ea5f9a02e70bf3"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:34:47.327178+00:00"

tags:
  - cloud

keywords:
  - "GPU"
  - "pilote NVIDIA"
  - "nvidia-gridd"
  - "ClientConfigToken"
  - "systemctl enable"
  - "vGPU"
  - "Shared Memory-Usage"
  - "CI"
  - "machine virtuelle"
  - "nvidia-smi"
  - "vGPU licensing"
  - "license acquisition"
  - "MIG devices"
  - "Vol"
  - "DKMS"

questions:
  - "Quels gabarits d'instance sont compatibles avec l'utilisation d'un vGPU sur le nuage Arbutus ?"
  - "Quelles sont les étapes de préparation d’une machine virtuelle avant d’installer le pilote vGPU (mise à jour du système, installation de DKMS, etc.) ?"
  - "Comment vérifier que le pilote vGPU est correctement installé et que le vGPU est accessible depuis le système d’exploitation ?"
  - "What steps must be taken to copy the token, configure `nvidia-gridd`, and enable the service to license the newly accessible vGPU?"
  - "How can you confirm that the `nvidia-gridd` daemon is active and has successfully acquired a valid license?"
  - "What does the displayed GPU usage table reveal about current memory allocation and running processes on the system?"
  - "What information does the “Shared Memory‑Usage” column provide for each MIG device?"
  - "How are the GPU, GI, CI, and MIG identifiers organized and related in the table?"
  - "What do the “Vol” and “Shared” columns represent, and how should they be interpreted when analyzing MIG device performance?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Utilisation des vGPU dans le nuage

Cette page décrit comment :

*   allouer des ressources de GPU virtuel (vGPU) à une machine virtuelle (VM);
*   installer les pilotes nécessaires;
*   et vérifier si le vGPU peut être utilisé.

L'accès aux dépôts de données ainsi qu'aux vGPU n'est actuellement disponible que sur [le nuage Arbutus](../clusters/arbutus.md). Veuillez noter que la documentation ci-dessous ne couvre que l'installation du pilote vGPU. La [boîte à outils CUDA](https://developer.nvidia.com/cuda-toolkit-archive) n'est pas préinstallée, mais vous pouvez l'installer directement à partir de NVIDIA ou la charger de [la pile logicielle dans CVMFS](../software/cvmfs/accessing_cvmfs.md).
Si vous choisissez d'installer la boîte à outils directement de NVIDIA, assurez-vous que le pilote vGPU n'est pas écrasé par celui de CUDA.

## Gabarits pris en charge

Pour utiliser un vGPU dans une machine virtuelle, l'instance doit être déployée sur l'un des gabarits mentionnés ci-dessous. Le vGPU sera disponible pour le système d'exploitation via le bus PCI.

*   `g1-12gb-c3-35gb-125`
*   `g1-24gb-c6-70gb-250`

## Préparer une machine virtuelle

Une fois que la machine virtuelle est disponible, assurez-vous de mettre à jour le système d'exploitation avec la dernière version disponible, y compris le noyau (*kernel*).

!!! note
    **Redémarrez ensuite la machine virtuelle pour avoir le dernier noyau.**

Nous recommandons l'installation de [DKMS](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support), qui est disponible par défaut dans toutes les distributions notables.
Si DKMS n'installe pas automatiquement le paquet ``kernel-header``, il faudra l'installer manuellement avec le gestionnaire de paquets de votre distribution.

Téléchargez sur votre ordinateur les deux fichiers suivants :

1.  **NVIDIA-Linux-x86_64-580.105.08-grid.run** ou **NVIDIA-Linux-x86_64-580.178.04-grid.run**
2.  **kalpa-prod.tok**

```bash
wget https://object-arbutus.alliancecan.ca/swift/v1/6c87c15eb7d2468daf3d2bd0c58bbfce/vgpu/NVIDIA-Linux-x86_64-580.105.08-grid.run
wget https://object-arbutus.alliancecan.ca/swift/v1/6c87c15eb7d2468daf3d2bd0c58bbfce/vgpu/kalpa-prod.tok
```

Installez le pilote pour vGPU de Nvidia avec :

```bash
chmod 755 NVIDIA-Linux-x86_64-580.105.08-grid.run && ./NVIDIA-Linux-x86_64-580.105.08-grid.run
```

Les options *NVIDIA Proprietary* et *DKMS* sont recommandées.

Lorsque l'installation est réussie, redémarrez l'ordinateur et utilisez ``nvidia-smi`` pour vérifier si le système d'exploitation a bien accès au vGPU.

```console
root@vgpudoc:/home/debian# nvidia-smi 
Jeu 02 avr 19:06:00 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Version du pilote: 580.105.08     Version CUDA: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Nom                 Persistance-M | Bus-Id          Disp.A | ECC volatile non corrigé |
| Ventilateur  Temp   Perf          Pwr:Usage/Cap |           Utilisation-mémoire | Util. GPU  Mode Calcul. |
|                                         |                        |               Mode MIG. |
|=========================================+========================+======================|
|   0  NVIDIA H100L-1-12C             On  |   00000000:00:06.0 Off |                   On |
| N/A   N/A    P0            N/A  /  N/A  |       1MiB /  12288MiB |     N/A      Défaut |
|                                         |                        |              Activé |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Périphériques MIG:                                                                            |
+------------------+----------------------------------+-----------+-----------------------+
| GPU  GI  CI  MIG |              Utilisation de la mémoire partagée |        Vol|        Partagé         |
|      ID  ID  Dev |                Utilisation du BAR1 partagé | SM     Unc| CE ENC  DEC  OFA  JPG |
|                  |                                  |        ECC|                       |
|==================+==================================+===========+=======================|
|  0    0   0   0  |               1MiB / 10565MiB    | 16      0 |  1   0    1    0    1 |
|                  |               0MiB /  4096MiB    |           |                       |
+------------------+----------------------------------+-----------+-----------------------+

+-----------------------------------------------------------------------------------------+
| Processus:                                                                              |
|  GPU   GI   CI              PID   Type   Nom du processus                        Mémoire GPU |
|        ID   ID                                                               Utilisation      |
|=========================================================================================|
| Aucun processus en cours d'exécution trouvé                                                             |
+-----------------------------------------------------------------------------------------+
```

Le vGPU est maintenant accessible et doit être sous licence. Copiez le jeton ``kalpa-prod.tok`` dans le répertoire ``/etc/nvidia/ClientConfigToken/``.

Configurez ``nvidia-gridd`` avec la commande ci-dessous :

```bash
echo "FeatureType=4" >/etc/nvidia/gridd.conf
```

Activez ``nvidia-gridd`` et vérifiez son état.

```bash
systemctl enable --now nvidia-gridd
```

```console
nvidia-gridd.service - Démon NVIDIA Grid
     Chargé: loaded (/usr/lib/systemd/system/nvidia-gridd.service; activé; préréglé: activé)
     Actif: active (running) depuis Jeu 2026-04-02 19:11:13 UTC; il y a 19s
 Invocation: 11dbb0370aee4ceeb1603481991037ec
    Processus: 836 ExecStart=/usr/bin/nvidia-gridd (code=exited, status=0/SUCCESS)
   PID principal: 837 (nvidia-gridd)
      Tâches: 4 (limite: 42042)
     Mémoire: 2M (pic: 2.7M)
        CPU: 307ms
     CGroup: /system.slice/nvidia-gridd.service
             ââ837 /usr/bin/nvidia-gridd

Avr 02 19:11:13 vgpudoc systemd[1]: Démarrage de nvidia-gridd.service - Démon NVIDIA Grid...
Avr 02 19:11:13 vgpudoc nvidia-gridd[837]: Démarré (837)
Avr 02 19:11:13 vgpudoc systemd[1]: nvidia-gridd.service - Démon NVIDIA Grid démarré.
Avr 02 19:11:13 vgpudoc nvidia-gridd[837]: vGPU Software package (0)
Avr 02 19:11:13 vgpudoc nvidia-gridd[837]: Ignorer le fournisseur de services et la licence liée au nœud
Avr 02 19:11:13 vgpudoc nvidia-gridd[837]: NLS initialisé
Avr 02 19:11:14 vgpudoc nvidia-gridd[837]: Acquisition de la licence. (Info: api.cls.licensing.nvidia.com; NVIDIA Virtual Compute Server)
Avr 02 19:11:16 vgpudoc nvidia-gridd[837]: Licence acquise avec succès. (Info: api.cls.licensing.nvidia.com, NVIDIA Virtual Compute Server; Expiration: 2026-4-3 19:11:16 GMT)
```

Une fois que `gridd` a obtenu une licence valide, toutes les fonctionnalités du vGPU peuvent être utilisées. Le renouvellement des licences est géré automatiquement par `nvidia-gridd`.