---
title: "AnsysEDT/fr"
slug: "ansysedt"
lang: "fr"

source_wiki_title: "AnsysEDT/fr"
source_hash: "2649370c55f68780dd3b1afd02349c3d"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:40:28.836489+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

[AnsysEDT](https://www.ansys.com/products/electronics) regroupe des solutions de simulation électromagnétique telles qu'Ansys HFSS, Ansys Maxwell, Ansys Q3D Extractor, Ansys SIwave et Ansys Icepak, utilisant des flux de travail de CAO électriques (ECAD) et mécaniques (MCAD). AnsysEDT s'intègre également à l'ensemble de la gamme Ansys de solveurs thermiques, fluides et mécaniques, permettant une analyse multiphysique complète.

## Licence

AnsysEDT est hébergé sur nos grappes, mais nous n'avons pas de licence qui permette un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des serveurs de licences qui peuvent être utilisés selon l'aspect légal de leur utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Quand tout sera en place, vous pourrez charger le module ansysEDT qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

### Configurer votre propre fichier de licence

Pour indiquer votre licence ansysedt, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient deux lignes. Pour les détails, voir [Configurez votre propre fichier de licence](ansys.md#configurez-votre-propre-fichier-de-licence).

## Soumettre des tâches par lots

Ansys EDT peut être exécuté de manière interactive en mode *batch* (sans interface graphique) en démarrant d'abord une session salloc avec les options `salloc --time=3:00:00 --tasks=8 --mem=16G --account=def- compte`; copiez-collez ensuite la commande `ansysedt` complète donnée à la dernière ligne de *script-local-cmd.sh* en vous assurant de spécifier manuellement `$YOUR_AEDT_FILE`.

### Scripts pour l'ordonnanceur Slurm

Les tâches peuvent être soumises à la file d'attente d'une grappe avec la commande `sbatch script-name.sh` en utilisant l'un des scripts Slurm pour nœud simple ci-dessous.

!!! note "À noter"
    Veuillez noter que ces scripts sont génériques et doivent probablement être modifiés selon la grappe utilisée. Avant de les utiliser, spécifiez le temps de simulation, la mémoire, le nombre de cœurs et remplacez `YOUR_AEDT_FILE` par le nom de votre fichier d'entrée.

Une liste complète des options de ligne de commande peut être obtenue en démarrant AnsysEDT [en mode graphique](ansys.md#mode-graphique) avec les commandes `ansysedt -help` ou `ansysedt -Batchoptionhelp` pour obtenir des fenêtres graphiques contextuelles déroulantes.

=== "Nœud simple (ligne de commande)"

    ```bash title="script-local-cmd.sh"
    #!/bin/bash

    #SBATCH --account=account      # Specify your account (def or rrg)
    #SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=16G              # Specify memory (set to 0 to use all compute node memory)
    #SBATCH --ntasks=8             # Specify number of cores to be used on a single node
    #SBATCH --nodes=1              # Request one node (Do Not Change)

    module load StdEnv/2023
    #module load ansysedt/2023R2
    module load ansysedt/2024R2.1

    # Uncomment next line to run a test example:
    #cp -f $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
    cp -f $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

    # Specify input file such as:
    YOUR_AEDT_FILE="TransientGeoRadar.aedt"

    # Remove previous output:
    rm -rf $YOUR_AEDT_FILE.* ${YOUR_AEDT_FILE}results

    # ---- do not change anything below this line ---- #

    echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
    echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
    echo -e "SLURM_TMPDIR= $SLURM_TMPDIR on $SLURMD_NODENAME\n"

    export KMP_AFFINITY=disabled
    ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:$SLURM_NTASKS \
    -batchoptions "TempDirectory=$SLURM_TMPDIR HPCLicenseType=pool HFSS/EnableGPU=0" -batchsolve "$YOUR_AEDT_FILE"
    ```

=== "Nœud simple (options)"

    ```bash title="script-local-opt.sh"
    #!/bin/bash

    #SBATCH --account=account      # Specify your account (def or rrg)
    #SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
    #SBATCH --mem=16G              # Specify memory (set to 0 to allocate all compute node memory)
    #SBATCH --ntasks=8             # Specify number of cores to be used on a single node
    #SBATCH --nodes=1              # Request one node (Do Not Change)

    module load StdEnv/2023
    #module load ansysedt/2023R2
    module load ansysedt/2024R2.1

    # Uncomment next line to run a test example:
    #cp -f $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
    cp -f $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

    # Specify input filename such as:
    YOUR_AEDT_FILE="TransientGeoRadar.aedt"

    # Remove previous output:
    rm -rf $YOUR_AEDT_FILE.* ${YOUR_AEDT_FILE}results

    # Specify options filename:
    OPTIONS_TXT="Options.txt"

    # Write sample options file
    rm -f $OPTIONS_TXT
    cat > $OPTIONS_TXT <<EOF
    \$begin 'Config'
    'TempDirectory'='$SLURM_TMPDIR'
    'HPCLicenseType'='pool'
    'HFSS/EnableGPU'=0
    \$end 'Config'
    EOF

    # ---- do not change anything below this line ---- #

    echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
    echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
    echo -e "SLURM_TMPDIR= $SLURM_TMPDIR on $SLURMD_NODENAME\n"

    export KMP_AFFINITY=disabled

    ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:$SLURM_NTASKS \
    -batchoptions $OPTIONS_TXT -batchsolve "$YOUR_AEDT_FILE"
    ```

## Mode graphique

Pour travailler en mode graphique, utilisez un système [Open OnDemand (OOD)](../clusters/nibi.md#accès-via-open-ondemand-ood) ou JupyterLab et démarrez un bureau à distance comme suit :

### OnDemand

1.  Connectez-vous à un système OnDemand avec une des adresses suivantes :
    *   [NIBI](../clusters/nibi.md#accès-via-open-ondemand-ood)
    *   `https://ondemand.sharcnet.ca`
    *   FIR, `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL, `https://portail.narval.calculquebec.ca/`
    *   RORQUAL, `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM, `https://ondemand.scinet.utoronto.ca`
2.  Sur le bureau, ouvrez une nouvelle fenêtre de terminal et exécutez :
    *   `module load StdEnv/2023` (par défaut)
    *   `module load ansysedt/2024R2.1` **OU** `ansysedt/2023R2`
    *   Dans le terminal, entrez `ansysedt` et attendez que l'interface graphique soit affichée.
3.  Vérifiez les configurations suivantes :
    *   Effectuez ce qui suit une fois seulement :
        *   Cliquez sur *Outils* -> *Options* -> *Options HPC et d'analyse* -> *Modifier*.
        *   Quand le panneau *Configurations d'analyse* s'affiche, supprimez la coche pour *Utiliser les paramètres automatiques*.
        *   Vérifiez que la configuration sous l'onglet *Machine* correspond aux ressources demandées, par exemple :
            *   `Tâches 1 | Cœurs 4 | Cœurs_alloués | GPU 0 | RAM 90 | Activé`.
        *   Cliquez sur *OK* pour sauvegarder les modifications et fermer le panneau *Configurations d'analyse*.
        *   Cliquez sur *OK* pour fermer le panneau *Options HPC et d'analyse*.
4.  Pour obtenir les exemples 2024R2.1 Antennas, copiez son répertoire dans votre compte comme suit :
    *   `module load ansysedt/2024R2.1`
    *   `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf ~/Ansoft/$EBVERSIONANSYSEDT/Antennas`
    *   `cp -a $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
5.  Exécutez l'exemple :
    *   Ouvrez un des fichiers `.aedt` et cliquez sur *HFSS* -> *Vérification de la validation*.
    *   Cliquez sur *Simulation* -> *Configuration* -> *Avancé* -> *Options de maillage/solution* -> *Utiliser les valeurs par défaut*.
    *   Lancez la simulation en cliquant sur *Simulation* -> *Analyser tout*.
    *   Pour fermer sans sauvegarder la solution, cliquez sur *Fichier* -> *Fermer* -> *Non*.
6.  Si ansysedt plante et ne peut être redémarré, essayez d'exécuter les commandes suivantes :
    *   `pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"`
    *   `rm -rf ~/.mw` (ansysedt exécutera à nouveau la première configuration au démarrage).

## Particularités selon le site

### Licence SHARCNET

Les conditions d'utilisation de la licence ANSYS de SHARCNET (qui inclut AnsysEDT) se trouvent sur la [page wiki pour Ansys](ansys.md), ainsi que les autres informations; elles ne sont pas répétées ici.

#### Fichier de licence

La licence Ansys de SHARCNET peut être utilisée sans frais avec les modules AnsysEDT pour les travaux de recherche sur nos grappes. Pour ce faire, configurez votre fichier `ansys.lic` comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")