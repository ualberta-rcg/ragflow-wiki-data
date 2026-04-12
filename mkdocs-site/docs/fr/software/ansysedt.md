---
title: "AnsysEDT/fr"
slug: "ansysedt"
lang: "fr"

source_wiki_title: "AnsysEDT/fr"
source_hash: "26e0703aa41d894d7d9dd51d06bfb437"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:16:48.678743+00:00"

tags:
  - software

keywords:
  - "AnsysEDT"
  - "ansysedt"
  - "SBATCH"
  - "scripts Slurm"
  - "HFSS"
  - "TransientGeoRadar.aedt"
  - "licence"
  - "Open OnDemand"
  - "Mode graphique"
  - "TRILLIUM"
  - "narval"
  - "module load"
  - "simulation électromagnétique"
  - "Antennas examples"
  - "Analysis Configuration"
  - "Licence SHARCNET"
  - "tâches en lots"
  - "RORQUAL"
  - "SLURM"
  - "terminal window"

questions:
  - "Qu'est-ce qu'AnsysEDT et quels types de simulations et d'analyses multiphysiques permet-il de réaliser ?"
  - "Comment fonctionne le système de licence pour AnsysEDT sur les grappes de calcul et comment les utilisateurs doivent-ils le configurer ?"
  - "Quelle est la procédure pour soumettre et exécuter des tâches en lots (batch) avec AnsysEDT via l'ordonnanceur Slurm ?"
  - "Comment configurer un script Slurm pour exécuter Ansys Electronics Desktop en mode batch avec un fichier d'options ?"
  - "Quelles sont les étapes pour accéder à l'interface graphique d'Ansys via le système Open OnDemand ?"
  - "Quels modules spécifiques doivent être chargés dans le terminal avant de pouvoir lancer le logiciel ?"
  - "Why is the number of requested nodes strictly set to one in the Slurm configuration?"
  - "Which specific software modules and versions need to be loaded to prepare the environment?"
  - "How can a user access and run the provided HFSS test example for a transient geo-radar antenna?"
  - "What are the web addresses provided for accessing the RORQUAL and TRILLIUM platforms?"
  - "Which environment and software modules must be loaded in the terminal prior to starting the application?"
  - "What specific command needs to be typed in the terminal to launch the graphical user interface?"
  - "How do you configure the HPC and Analysis options to allocate the correct desktop resources for a simulation in AnsysEDT?"
  - "What specific commands should be executed to troubleshoot and reset the software if AnsysEDT crashes and fails to restart?"
  - "How must the user configure the `ansys.lic` file to properly access and use the SHARCNET Ansys license on the clusters?"
  - "How do you configure the HPC and Analysis options to allocate the correct desktop resources for a simulation in AnsysEDT?"
  - "What specific commands should be executed to troubleshoot and reset the software if AnsysEDT crashes and fails to restart?"
  - "How must the user configure the `ansys.lic` file to properly access and use the SHARCNET Ansys license on the clusters?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[AnsysEDT](https://www.ansys.com/products/electronics) regroupe des solutions de simulation électromagnétique telles qu'Ansys HFSS, Ansys Maxwell, Ansys Q3D Extractor, Ansys SIwave et Ansys Icepak, utilisant des flux de travail de CAO électriques (ECAD) et mécaniques (MCAD). AnsysEDT s'intègre également à l'ensemble de la gamme Ansys de solveurs thermiques, fluides et mécaniques, permettant une analyse multiphysique complète.

# Licence

AnsysEDT est hébergé sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des serveurs de licences qui peuvent être utilisés dépendant de l'aspect légal de leur utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Quand tout sera en place, vous pourrez charger le module ansysEDT qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurer votre propre fichier de licence
Pour indiquer votre licence ansysedt, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient deux lignes. Pour les détails, voir [Configurez votre propre fichier de licence](ansys.md#configurez-votre-propre-fichier-de-licence).

# Soumettre des tâches en lots

Ansys EDT peut être exécuté de manière interactive en mode *batch* (sans interface graphique) en démarrant d'abord une session salloc avec les options `salloc --time=3:00:00 --tasks=8 --mem=16G --account=def- compte`; copiez-collez ensuite la commande `ansysedt` complète donnée à la dernière ligne de *script-local-cmd.sh* en vous assurant de spécifier manuellement $YOUR_AEDT_FILE.

## Scripts pour l'ordonnanceur Slurm

Les tâches peuvent être soumises à la file d'attente d'une grappe avec la commande `sbatch script-name.sh` en utilisant l'un des scripts Slurm pour nœud simple ci-dessous. En date de janvier 2023, ces scripts n'ont été testés que sur Graham et pourraient donc être mis à jour à l'avenir si nécessaire pour fonctionner avec d'autres grappes. Avant de les utiliser, spécifiez le temps de simulation, la mémoire, le nombre de cœurs et remplacez YOUR_AEDT_FILE par le nom de votre fichier d'entrée. Une liste complète des options de ligne de commande peut être obtenue en démarrant AnsysEDT [en mode graphique](ansys.md#mode-graphique) avec les commandes `ansysedt -help` ou `ansysedt -Batchoptionhelp` pour obtenir des fenêtres graphiques contextuelles déroulantes.

=== "Nœud simple (ligne de commande)"
    ```bash title="script-local-cmd.sh"
    #!/bin/bash

    #SBATCH --account=account      # Spécifiez votre compte (def ou rrg)
    #SBATCH --time=00-01:00        # Spécifiez le temps (JJ-HH:MM)
    #SBATCH --mem=16G              # Spécifiez la mémoire (mettez 0 pour utiliser toute la mémoire du nœud de calcul)
    #SBATCH --ntasks=8             # Spécifiez les cœurs (beluga 40, cedar 32 ou 48, graham 32 ou 44, narval 64)
    #SBATCH --nodes=1              # Demandez un nœud (Ne pas modifier)

    module load StdEnv/2023
    module load ansysedt/2023R2    # ou plus récente

    # Décommentez la ligne suivante pour exécuter un exemple de test :
    cp -f $EBROOTANSYSEDT/AnsysEM21.2/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

    # Spécifiez le fichier d'entrée comme :
    YOUR_AEDT_FILE="TransientGeoRadar.aedt"

    # Supprimez la sortie précédente :
    rm -rf $YOUR_AEDT_FILE.* ${YOUR_AEDT_FILE}results

    # ---- Ne rien modifier sous cette ligne ---- #

    echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
    echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
    echo -e "SLURM_TMPDIR= $SLURM_TMPDIR sur $SLURMD_NODENAME\n"

    export KMP_AFFINITY=disabled
    ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:$SLURM_NTASKS \
    -batchoptions "TempDirectory=$SLURM_TMPDIR HPCLicenseType=pool HFSS/EnableGPU=0" -batchsolve "$YOUR_AEDT_FILE"
    ```
=== "Nœud simple (options)"
    ```bash title="script-local-opt.sh"
    #!/bin/bash

    #SBATCH --account=account      # Spécifiez votre compte (def ou rrg)
    #SBATCH --time=00-01:00        # Spécifiez le temps (JJ-HH:MM)
    #SBATCH --mem=16G              # Spécifiez la mémoire (mettez 0 pour allouer toute la mémoire du nœud de calcul)
    #SBATCH --ntasks=8             # Spécifiez les cœurs (beluga 40, cedar 32 ou 48, graham 32 ou 44, narval 64)
    #SBATCH --nodes=1              # Demandez un nœud (Ne pas modifier)

    module load StdEnv/2023
    module load ansysedt/2023R2    # ou plus récente

    # Décommentez la ligne suivante pour exécuter un exemple de test :
    cp -f $EBROOTANSYSEDT/AnsysEM21.2/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

    # Spécifiez le nom du fichier d'entrée comme :
    YOUR_AEDT_FILE="TransientGeoRadar.aedt"

    # Supprimez la sortie précédente :
    rm -rf $YOUR_AEDT_FILE.* ${YOUR_AEDT_FILE}results

    # Spécifiez le nom du fichier d'options :
    OPTIONS_TXT="Options.txt"

    # Écrivez un fichier d'options d'exemple
    rm -f $OPTIONS_TXT
    cat > $OPTIONS_TXT <<EOF
    $begin 'Config'
    'TempDirectory'='$SLURM_TMPDIR'
    'HPCLicenseType'='pool'
    'HFSS/EnableGPU'=0
    $end 'Config'
    EOF

    # ---- Ne rien modifier sous cette ligne ---- #

    echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
    echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
    echo -e "SLURM_TMPDIR= $SLURM_TMPDIR sur $SLURMD_NODENAME\n"

    export KMP_AFFINITY=disabled

    ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:$SLURM_NTASKS \
    -batchoptions $OPTIONS_TXT -batchsolve "$YOUR_AEDT_FILE"
    ```

# Mode graphique

Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

## Nœuds VDI

1.  Connectez-vous à un système OnDemand en utilisant l'une des URLs suivantes dans le navigateur de votre portable :
    [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    FIR: `https://jupyterhub.fir.alliancecan.ca`
    NARVAL: ` https://portail.narval.calculquebec.ca/`
    RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
    TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Ouvrez une nouvelle fenêtre de terminal sur votre bureau et exécutez :
    - `module load StdEnv/2023` (par défaut)
    - `module load ansysedt/2024R2.1` **OU** `ansysedt/2023R2`
    - Tapez `ansysedt` dans le terminal et attendez que l'interface graphique démarre.
3.  Vérifiez les paramètres suivants :
    - Ce qui suit ne doit être fait qu'une seule fois :
      - Cliquez sur `Outils -> Options -> Options HPC et d'analyse -> Modifier`
      - Lorsque le panneau « Configuration de l'analyse » apparaît, décochez « Utiliser les paramètres automatiques »
      - Assurez-vous que les paramètres dans l'onglet « Machine » correspondent aux ressources de bureau demandées, tels que :
      - ` | Tâches 1 | Cœurs 4 | Cœurs alloués | GPU 0 | RAM 90 | coche Activé |`
      - Cliquez sur le bouton « OK » pour enregistrer les modifications et fermer le panneau « Configuration de l'analyse ».
      - Cliquez sur le bouton « OK » pour fermer le panneau « Options HPC et d'analyse ».
4.  Pour récupérer les exemples d'antennes 2024R2.1, copiez son répertoire sous votre compte comme suit :
    - `module load ansysedt/2024R2.1`
    - `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf ~/Ansoft/$EBVERSIONANSYSEDT/Antennas`
    - `cp -a $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
5.  Maintenant, pour exécuter l'exemple :
    - Ouvrez l'un des fichiers .aedt des exemples d'antennes, puis cliquez sur `HFSS -> Vérification de la validation`.
    - Cliquez sur `Simulation -> Configuration -> Avancé -> Options Maillage/Solution -> Utiliser les valeurs par défaut`.
    - Démarrez la simulation en cliquant sur `Simulation -> Analyser tout`.
    - Pour quitter sans sauvegarder la solution convergée, cliquez sur `Fichier -> Fermer -> Non`.
6.  Si ansysedt plante et ne redémarre pas, essayez d'exécuter les commandes suivantes :
    - `pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"`
    - `rm -rf ~/.mw` (ansysedt réexécutera la configuration initiale au démarrage)

# Particularités selon le site

## Licence SHARCNET

Les conditions d'utilisation de la licence ANSYS de SHARCNET (qui inclut AnsysEDT) se trouvent sur la [page wiki pour Ansys](ansys.md), ainsi que les autres informations; elles ne sont pas répétées ici.

### Fichier de licence

La licence Ansys de SHARCNET peut être utilisée sans frais avec les modules AnsysEDT pour les travaux de recherche sur nos grappes. Pour ce faire, configurez votre fichier `ansys.lic` comme suit :
```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")