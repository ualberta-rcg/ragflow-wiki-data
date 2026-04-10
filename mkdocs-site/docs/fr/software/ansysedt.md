---
title: "AnsysEDT/fr"
tags:
  - software

keywords:
  []
---

[AnsysEDT](https://www.ansys.com/products/electronics) regroupe des solutions de simulation électromagnétique telles qu'Ansys HFSS, Ansys Maxwell, Ansys Q3D Extractor, Ansys SIwave et Ansys Icepak, utilisant des flux de travail de CAO électriques (ECAD) et mécaniques (MCAD). AnsysEDT s'intègre également à l'ensemble de la gamme Ansys de solveurs thermiques, fluides et mécaniques, permettant une analyse multiphysique complète.

<span id="Licensing"></span>
= Licence=

AnsysEDT est hébergé sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des serveurs de licences qui peuvent être utilisés dépendant de l'aspect légal de leur utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence.  Quand tout sera en place, vous pourrez charger le module ansysEDT qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](technical-support-fr.md).

## Configurer votre propre fichier de licence 
 Pour indiquer votre licence ansysedt, créez un fichier nommé `$HOME/.licenses/ansys.lic` qui contient deux lignes. Pour les détails, voir [Configurez votre propre fichier de licence](ansys-fr#configurez_votre_propre_fichier_de_licence.md).

<span id="Cluster_batch_job_submission"></span>
= Soumettre des tâches en lots =

Ansys EDT peut être exécuté de manière interactive en mode <i>batch</i> (sans interface graphique) en démarrant d'abord une session salloc avec les options `salloc --time=3:00:00 --tasks=8 --mem=16G --account=def- compte`; copiez-collez ensuite la commande `ansysedt` complète donnée à la dernière ligne de <i>script-local-cmd.sh</i> en vous assurant de spécifier manuellement $YOUR_AEDT_FILE.

<span id="Slurm_scripts"></span>
### Scripts pour l'ordonnanceur Slurm 

<div class="mw-translate-fuzzy">
Les tâches peuvent être soumises à la file d'attente d'une grappe avec la commande `sbatch script-name.sh` en utilisant l'un des scripts Slurm pour nœud simple ci-dessous. En date de janvier 2023, ces scripts n'ont été testés que sur Graham et pourraient donc être mis à jour à l'avenir si nécessaire pour fonctionner avec d'autres grappes. Avant de les utiliser, spécifiez le temps de simulation, la mémoire, le nombre de cœurs et remplacez YOUR_AEDT_FILE par le nom de votre fichier d'entrée. Une liste complète des options de ligne de commande peut être obtenue en démarrant AnsysEDT [en mode graphique](ansys-fr#mode_graphique.md) avec les commandes `ansysedt -help` ou `ansysedt -Batchoptionhelp` pour obtenir des fenêtres graphiques contextuelles déroulantes.
</div>  

<tabs>
<tab name="Nœud simple (ligne de commande)">
{{File
|name=script-local-cmd.sh
|lang="bash"
|contents=
#!/bin/bash

<div class="mw-translate-fuzzy">
#SBATCH --account=account      # Specify your account (def or rrg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=16G              # Specify memory (set to 0 to use all compute node memory)
#SBATCH --ntasks=8             # Specify cores (beluga 40, cedar 32 or 48, graham 32 or 44, narval 64)
#SBATCH --nodes=1              # Request one node (Do Not Change)
</div>

<div class="mw-translate-fuzzy">
module load StdEnv/2023
module load ansysedt/2023R2    # ou plus récente
</div>

<div class="mw-translate-fuzzy">
# Uncomment next line to run a test example:
cp -f $EBROOTANSYSEDT/AnsysEM21.2/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
</div>

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
}}
</tab>
<tab name="Nœud simple (options)">
{{File
|name=script-local-opt.sh
|lang="bash"
|contents=
#!/bin/bash

<div class="mw-translate-fuzzy">
#SBATCH --account=account      # Specify your account (def or rrg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=16G              # Specify memory (set to 0 to allocate all compute node memory)
#SBATCH --ntasks=8             # Specify cores (beluga 40, cedar 32 or 48, graham 32 or 44, narval 64)
#SBATCH --nodes=1              # Request one node (Do Not Change)
</div>

<div class="mw-translate-fuzzy">
module load StdEnv/2023
module load ansysedt/2023R2    # ou plus récente
</div>

<div class="mw-translate-fuzzy">
# Uncomment next line to run a test example:
cp -f $EBROOTANSYSEDT/AnsysEM21.2/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
</div>

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
}}
</tab>
</tabs>

<span id="Graphical_use"></span>
= Mode graphique =

<div class="mw-translate-fuzzy">
Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.
</div>

<span id="OnDemand"></span>
<div class="mw-translate-fuzzy">
## Nœuds VDI 
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
1. Connect to an OnDemand system using one of the following URLs in your laptop browser :

 [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
 FIR: `https://jupyterhub.fir.alliancecan.ca`
 NARVAL: ` https://portail.narval.calculquebec.ca/`
 RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
 TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2. Open a new terminal window in your desktop and run:
::: `module load StdEnv/2023`  (default)
::: `module load ansysedt/2024R2.1` **OR** `ansysedt/2023R2`
::: Type `ansysedt` in the terminal and wait for the gui to start
3. Verify the following settings 
::: The following only needs to be done once:
:::: click `Tools -> Options -> HPC and Analysis Options -> Edit`
:::: When the Analysis Configuration panel appears untic `Use Automatic Settings`
:::: Ensure the settings in the `Machine` tab correspond requested desktop resources such as:
:::: ` | Tasks 1 | Cores 4 | Allocated_Cores | GPUs 0 | RAM 90 | tic Enabled |`
:::: Click the OK button to save any changes and close the `Analysis Configuration` panel
:::: Click the OK button close the `HPC and Analysis` Options panel
4.  To retrieve the 2024R2.1 Antennas examples, copy its directory under your account as follows:
:::: `module load ansysedt/2024R2.1`
:::: `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf ~/Ansoft/$EBVERSIONANSYSEDT/Antennas`
:::: `cp -a $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
5. Now to run the example:
:::: Open one of the Antennas examples .aedt files then click `HFSS -> Validation Check`
:::: Click simulation -> setup -> advanced -> Mesh/Solution options -> Use Defaults
:::: Start simulation running by clicking `Simulation -> Analyze All`
:::: To quit without saving the converged solution click `File -> Close -> No `
6. If ansysedt crashes and won't restart try running the following commands:
:::: `pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"`
:::: `rm -rf ~/.mw` (ansysedt will re-run first-time configuration on startup)
</div>

<span id="Site-Specific"></span>
= Particularités selon le site =

<span id="SHARCNET_license"></span>
## Licence SHARCNET 

Les conditions d'utilisation de la licence ANSYS de SHARCNET (qui inclut AnsysEDT) se trouvent sur la [page wiki pour Ansys](ansys-fr.md), ainsi que les autres informations; elles ne sont pas répétées ici. 

<span id="License_file"></span>
#### Fichier de licence 

La licence Ansys de SHARCNET peut être utilisée sans frais avec les modules AnsysEDT pour les traaux de recherche sur nos grappes. Pour ce faire, configurez votre fichier `ansys.lic` comme suit&nbsp;:
<source lang="bash">
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
</source>