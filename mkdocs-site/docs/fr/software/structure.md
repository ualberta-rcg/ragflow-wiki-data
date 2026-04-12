---
title: "Structure/fr"
slug: "structure"
lang: "fr"

source_wiki_title: "Structure/fr"
source_hash: "bcf081ecfd78a71beb1e6fe4d57cb8b1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:41:38.600038+00:00"

tags:
  - software

keywords:
  - "Automatisation"
  - "exécution parallèle"
  - "SBATCH"
  - "create_strauto_slurm_scripts.py"
  - "runstructure shell script"
  - "job submissions"
  - "BMC Bioinformatics"
  - "Structure binary"
  - "Slurm"
  - "Python script"
  - "structureHarvester"
  - "Analyse STRUCTURE"
  - "Ordonnanceur Slurm"
  - "génétique des populations"
  - "StructureHarvester"
  - "bash script template"
  - "données de génotypage"
  - "postprocessing script"
  - "structure command"
  - "Python"
  - "SLURM job scripts"
  - "marqueurs génétiques"
  - "job scripts"
  - "Exécution de processus"
  - "Structure"
  - "logiciel structure"
  - "mainparams"
  - "SLURM"
  - "extraparams"
  - "structureCommands"
  - "StrAuto"

questions:
  - "À quoi sert le logiciel ''structure'' et quels types de marqueurs génétiques peut-il analyser ?"
  - "Quels sont les fichiers requis par défaut pour exécuter ''structure'' en ligne de commande ?"
  - "Quels outils supplémentaires permettent de pallier l'absence d'exécution parallèle native dans ''structure'' ?"
  - "Quelle est la fonction principale du programme StrAuto décrit dans l'article de BMC Bioinformatics de 2017 ?"
  - "Sur quelles plateformes en ligne le logiciel StructureHarvester est-il hébergé et accessible ?"
  - "Quel type d'analyse spécifique ces deux outils informatiques cherchent-ils à faciliter ou à automatiser ?"
  - "Quelles sont les limites d'optimisation des ressources et de temps d'exécution lors de l'utilisation de StrAuto avec l'ordonnanceur Slurm ?"
  - "Quels sont les outils et les fichiers spécifiques requis dans le répertoire pour utiliser le script d'exécution de processus de longue durée ?"
  - "Quelles sont les étapes de configuration du fichier input.py et les commandes à exécuter pour préparer et lancer l'analyse ?"
  - "Quelles sont les commandes à exécuter pour soumettre les tâches SLURM et agréger les résultats une fois celles-ci terminées ?"
  - "Quels paramètres spécifiques l'utilisateur doit-il ajuster dans le script `create_strauto_slurm_scripts.py` avant de l'utiliser ?"
  - "Quels fichiers provenant de StrAuto et StructureHarvester doivent être placés dans le répertoire de travail selon les instructions du script ?"
  - "What is the primary purpose of the `create_strauto_slurm_scripts.py` script as demonstrated in the text?"
  - "Which specific configuration and execution files are generated for \"my_dataset\" after the user accepts the prompt?"
  - "What external binary dependency does the script check for before creating the final shell script?"
  - "What is the primary purpose of this Python script in relation to the SLURM workload manager and the `structure` program?"
  - "How does the script process the `structureCommands` input file to determine the necessary job names, datasets, and K-values?"
  - "What specific tasks are executed by the generated `post_strauto.sh` post-processing script once the main structure runs have finished?"
  - "What is the purpose of the `job_prefix` variable in the script configuration?"
  - "Why does the script include a strict warning instructing the user not to make any changes below a specific line?"
  - "What specific SLURM directives and software modules are defined within the bash script template?"
  - "What is the primary purpose of this Python script in relation to the SLURM workload manager and the `structure` program?"
  - "How does the script process the `structureCommands` input file to determine the necessary job names, datasets, and K-values?"
  - "What specific tasks are executed by the generated `post_strauto.sh` post-processing script once the main structure runs have finished?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

*structure*[^1] est un logiciel gratuit qui utilise les données de génotypage de locus multiples dans la recherche en structure génétique des populations. Il est employé pour inférer la présence de populations distinctes, assigner des individus à des populations, étudier les zones hybrides, identifier les individus migrants et estimer la fréquence des allèles dans les populations avec individus migrants. *structure* peut être utilisé avec la plupart des marqueurs génétiques couramment utilisés, incluant les SNP, RFLP, AFLP et les microsatellites[^2][^3].

## Versions installées

Consultez la liste des [logiciels disponibles](../programming/available_software.md) pour connaître la version à jour du module *structure* (par exemple, `structure/2.3.4` en date de janvier 2019).

## Utilisation

Au démarrage en ligne de commande sans options, *structure* s’attend à trouver les trois fichiers suivants dans le répertoire courant :
*   `mainparams` (exemples[^4]),
*   `extraparams` (exemples[^5]),
*   fichier de données; le fichier peut être identifié par le paramètre INFILE de `mainparams` ou en ligne de commande avec `-i`.

Pour la description des paramètres et des formats de fichiers, consultez la documentation[^6] au chapitre 7, *Running structure from the command line*. La section 7.4 décrit plusieurs options pour modifier les paramètres.

Voici un exemple d’un script de soumission :

::: structure_job.sh
```bash
#!/bin/bash
#SBATCH --time=0-0:30           # time limit (D-HH:MM)
module load structure
structure -i data_file1  -o results1
```

## Exécution parallèle : StrAuto et StructureHarvester

*structure* n’est pas conçu pour travailler en parallèle; cependant, pour travailler avec la méthode Evanno[^7], les outils StrAuto[^8][^9][^10] et StructureHarvester[^11][^12] sont utilisés pour automatiser la préparation de processus multiples et l’agrégation des résultats.

### Considérations pratiques

Le chapitre 8 du manuel de l’utilisateur pour StrAuto[^9] montre un exemple de tâches exécutées sur des grappes de CHP avec l’ordonnanceur Slurm. Cet exemple fonctionne mieux lorsque le nombre total de processus est un multiple du nombre de cœurs demandés. Si ce n’est pas le cas, certains des CPU qui ont été alloués ne seront pas utilisés pendant que les derniers processus *structure* sont exécutés, ce qui n’est pas une utilisation maximale des ressources de calcul.

De plus, le temps d’exécution demandé doit être suffisant pour tenir compte des multiples processus *structure* qui vont suivre. Ceci est un choix raisonnable dans le cas de processus qui exigent un temps d’exécution relativement court, mais les tâches plus longues resteront plus longtemps en attente en raison de la [politique d'ordonnancement](../running-jobs/job_scheduling_policies.md#durée-maximale).

### Exécution de processus de longue durée

Le script `create_strauto_slurm_scripts.py` au bas de cette section est conçu pour vous aider à exécuter des tâches Structure[^1] ordonnancées par Slurm sur les grappes de Calcul Canada. Les outils requis sont Structure, StrAuto[^8] et StructureHarvester[^11].

Utilisation :

*   Placez le script `create_strauto_slurm_scripts.py` dans un répertoire avec
    *   `strauto_1.py` et `input.py` de StrAuto[^8] ;
    *   `structureHarvester.py` et `harvesterCore.py` de StructureHarvester[^11] ;
    *   le fichier de données, par exemple `my_dataset.str`.
*   Rendez `create_strauto_slurm_scripts.py` exécutable avec
    ```bash
    chmod u+x create_strauto_slurm_scripts.py
    ```
    *   Vous devriez maintenant avoir les fichiers suivants :
        ```bash
        ls -F
        ```
        ```text
        create_strauto_slurm_scripts.py*  harvesterCore.py
        input.py                          my_dataset.str
        strauto_1.py*                     structureHarvester.py*
        ```
*   Modifiez les paramètres de `input.py` tel que décrit dans le manuel StrAuto[^9].
    *   Assurez-vous de configurer l'option `parallel = True` (question 23).
*   Ajustez les paramètres (lignes 65-70) :
    *   Définissez une valeur appropriée pour `max_jobtime`, soit une durée minimale pour l’exécution d’un processus *structure* unique.
    *   Utilisez `slurm_account` pour indiquer dans quel compte Slurm soumettre la tâche.
    *   Définissez une valeur appropriée pour `submit_delay` afin d’éviter de surcharger l’ordonnanceur.
*   Exécutez les commandes suivantes :
    ```bash
    module load python/2.7
    ```
    ```bash
    ./strauto_1.py
    ```
    ```text
    input.py found. Proceeding!
    ----------------------------------------------------------------------
      Finished entering data for 'my_dataset'.  Verify your information.
    ----------------------------------------------------------------------
                  Maximum number of assumed populations :   4
                               Number of burnin :   1000
                            Number of MCMC reps :   1000
                                Name of dataset :   my_dataset
    [...]
                 Run Structure Harvester automatically? :   True
    ----------------------------------------------------------------------
                      (a)ccept to start writing output files.
                         (q)uit if you find errors above.
                Then correct the input file and rerun this script
    >> a
    Preparing to write...
    Now writing 'mainparams' file for my_dataset!
    Now writing 'extraparams' with default values for my_dataset!
    -------------------------------
    Checking for Structure binary
    -----------------------------------------
    Now writing 'runstructure' shell script
    ```
    ```bash
    ./create_strauto_slurm_scripts.py
    ```
    ```text
    Creating SLURM job scripts...
    created 40 job scripts.

    Creating directories...done!

    Creating submission helper script...
    created helper script: "submit_strauto_jobs.sh"

    Creating postprocessing script...
    created post-script: "post_strauto.sh"
    ```

*   Soumettez les tâches avec
    ```bash
    bash submit_strauto_jobs.sh
    ```
    ```text
    Submitted batch job 12345001
    Submitted batch job 12345002
    [...]
    Submitted batch job 12345040
    ```
*   Lorsque toutes les tâches sont terminées, lancez `bash post_strauto.sh` pour effectuer l’agrégation des résultats et exécuter StructureHarvester.

#### Script create_strauto_slurm_scripts.py

::: create_strauto_slurm_scripts.py
```python
#!/usr/bin/env python
'''
create_strauto_slurm_scripts.py
===============================

This script is designed to be a supplement to running Structure[1] jobs on
Compute Canada HPC clusters that are using the Slurm Workload manager.
It is meant to be used with Structure, StrAuto[2] and StructureHarvester[3].

Usage:
******

* Place this script 'create_strauto_slurm_scripts.py' into a directory along with
    * 'strauto_1.py' and 'input.py' from StrAuto[2].
    * 'structureHarvester.py' and 'harvesterCore.py' from StructureHarvester[3]
    * The file with the Structure dataset e.g. 'sim.str'.
* Edit the settings in 'input.py' as described in the StrAuto User Manual.
    * Make sure to set the option 'parallel = True' (question 23).
* Adjust the parameters in this file (ca. lines 65-70):
    * Set 'max_jobtime' to a duration where you can be reasonably sure that no
      individual Structure run takes longer than this.
    * In cases where a user can submit under multiple Slurm-accounts
      'slurm_account' can be used to specify under which account to submit.
    * To avoid overloading the Scheduler, the submission helper script delays
      each submission by a time defined by 'submit_delay'.
* Run the following commands:
    * ./strauto_1.py
    * ./create_strauto_slurm_scripts.py
* Submit the jobs with:
    * ./submit_strauto_jobs.sh
* After all jobs have completed, run './post_strauto.sh' to aggregate the
  results and run StructureHarvester.

[1] Structure: http://web.stanford.edu/group/pritchardlab/structure.html
[2] StrAuto:   http://www.crypticlineage.net/pages/software.html
[3] Harvester: http://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/
               https://github.com/dentearl/structureHarvester

LICENSE:
========
This program is licensed under the conditions of the "MIT License".

Copyright 2017-2020 Oliver Stueker <ostueker(a)ace-net.ca>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
'''
from __future__ import print_function
import re, os, sys
##############################################################################
### Please adjust the following parameters:
##############################################################################
max_job_time = '1-0:00:0' # format: d-hh:mm:ss
slurm_account = None     # e.g.: slurm_account='def-somegroup'
submit_delay = '0.5s'    # pause this long between job submissions
job_prefix = None        # (optional) e.g.: job_prefix='strauto'

##############################################################################
### Don't make any changes below this line:
##############################################################################
template = '''#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --time={MAXTIME:}              # d-hh:mm:ss
#SBATCH --job-name={JOBNAME:}
#SBATCH --chdir={DIRECTORY:}
#SBATCH --output=%x_%j_slurm.out
{SLURM_ACCT:}
module load structure/2.3.4

{STRUCTURE_COMMAND}
'''

post_template = '''#!/bin/bash
mv {KLIST:} results_f/
mkdir harvester_input
cp results_f/k*/*_f harvester_input
echo "The structure runs have finished."

# Run structureHarvester.py
./structureHarvester.py --dir harvester_input --out harvester --evanno --clumpp
echo 'structureHarvester run has finished.'

# Clean up Harvester input files.
zip {DATASET:}_Harvester_Upload.zip harvester_input/*
mv {DATASET:}_Harvester_Upload.zip harvester/
rm -rf harvester_input
'''

if __name__ == '__main__':
    if not os.path.exists('structureCommands'):
        print('ERROR: File "structureCommands" does not exist!')
        print('You need to run "./strauto_1.py" before running "{}".'
              .format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    # initialize some variables
    scripts_dir = 'slurm_scripts'
    job_directory = os.getcwd()
    if slurm_account:
        slurm_account = '#SBATCH --account='+slurm_account
    else:
        slurm_account = ''
    re_jobname = re.compile(r'-o (k\d+)/((.+)_\1_run\d+) ')
    job_scripts = []
    klist = set()

    with open('structureCommands', 'r') as structureCommands:
        print("Creating SLURM job scripts...")
        for line in structureCommands:
            match = re_jobname.search(line)
            if match:
                kn = match.group(1)
                jobname = match.group(2)
                dataset = match.group(3)

                klist.add(kn)
                if job_prefix:
                    jobname = '_'.join([job_prefix, jobname])

                line = line.replace('./structure', 'structure')

                job_script_content = template.format(
                        SLURM_ACCT=slurm_account,
                        MAXTIME=max_job_time,
                        JOBNAME=jobname,
                        DIRECTORY=job_directory,
                        STRUCTURE_COMMAND=line,
                    )

                if not ( os.path.exists(scripts_dir) and
                         os.path.isdir(scripts_dir) ):
                    os.mkdir(scripts_dir)

                job_script_name = os.path.join( scripts_dir,
                                    'slurm_job_{:}.sh'.format(jobname))
                with open(job_script_name, 'w') as slurm_script:
                    slurm_script.write(job_script_content)
                job_scripts.append(job_script_name)
        print("created {:} job scripts.\n".format(len(job_scripts)))

    print("Creating directories...", end='')
    directories = ['results_f', 'log', 'harvester']
    for kn in sorted(klist):
        directories.append(kn)
        directories.append(os.path.join('log', kn))
    print('done!', end='\n\n')

    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)

    print('Creating submission helper script...')
    helper_script_name='submit_strauto_jobs.sh'
    with open(helper_script_name, 'w') as helper_script:
        helper_script.write('#!/bin/bash\n')
        for job_script in job_scripts:
            helper_script.write('sleep 0.5s ; sbatch {:}\n'.format(job_script))
    print('created helper script: "{:}"\n'.format(helper_script_name))

    print('Creating postprocessing script...')
    post_script_name='post_strauto.sh'
    with open(post_script_name, 'w') as pst_script:
        pst_script.write(post_template.format(KLIST=' '.join(sorted(klist)),
                                              DATASET=dataset))
    print('created post-script: "{:}"\n'.format(post_script_name))
```

## Références

[^1]: Site web : [http://web.stanford.edu/group/pritchardlab/structure.html](http://web.stanford.edu/group/pritchardlab/structure.html)
[^2]: J.K. Pritchard, M. Stephens, and P. Donnelly. Inference of population structure using multilocus genotype data. Genetics, 155:945–959, 2000. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461096/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461096/)
[^3]: M.J. Hubisz, D. Falush, M. Stephens, and J.K. Pritchard. Inferring weak population structure with the assistance of sample group information. Molecular Ecology Resources, 9(5):1322–1332, 2009. doi: [https://doi.org/10.1111/j.1755-0998.2009.02591.x](https://doi.org/10.1111/j.1755-0998.2009.02591.x)
[^4]: [mainparams](http://web.stanford.edu/group/pritchardlab/software/mainparams)
[^5]: [extraparams](http://web.stanford.edu/group/pritchardlab/software/extraparams)
[^6]: Version 2.3.4 [(PDF)](http://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v2.3.4/structure_doc.pdf)
[^7]: G. Evanno, S. Regnaut, and J. Goudet. Detecting the number of clusters of individuals using the software structure: a simulation study. Molecular Ecology, 14:2611–2620, 2005. DOI: [https://doi.org/10.1111/j.1365-294X.2005.02553.x](https://doi.org/10.1111/j.1365-294X.2005.02553.x)
[^8]: Site web StrAuto : [https://vc.popgen.org/software/strauto/](https://vc.popgen.org/software/strauto/)
[^9]: Guide de l'utilisateur StrAuto : [https://vc.popgen.org/software/strauto/strauto_doc.pdf](https://vc.popgen.org/software/strauto/strauto_doc.pdf)
[^10]: Chhatre, VE & Emerson KJ. StrAuto: Automation and parallelization of STRUCTURE analysis. BMC Bioinformatics (2017) 18:192. doi: [http://dx.doi.org/10.1186/s12859-017-1593-0](http://dx.doi.org/10.1186/s12859-017-1593-0)
[^11]: Site web StructureHarvester : [http://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/](http://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/) ; GitHub: [https://github.com/dentearl/structureHarvester](https://github.com/dentearl/structureHarvester)
[^12]: Earl, Dent A. and vonHoldt, Bridgett M. STRUCTURE HARVESTER: a website and program for visualizing STRUCTURE output and implementing the Evanno method. Conservation Genetics Resources (2011) DOI: [10.1007/s12686-011-9548-7](https://doi.org/10.1007/s12686-011-9548-7)