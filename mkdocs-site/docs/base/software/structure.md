---
title: "Structure"
slug: "structure"
lang: "base"

source_wiki_title: "Structure"
source_hash: "5f3e4324255e7ce3e7e8f29a8d9e40bd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:40:08.730791+00:00"

tags:
  - software

keywords:
  - "HPC clusters"
  - "SBATCH"
  - "STRUCTURE analysis"
  - "job submission"
  - "create_strauto_slurm_scripts.py"
  - "runstructure shell script"
  - "BMC Bioinformatics"
  - "Structure binary"
  - "Slurm"
  - "structure"
  - "Python script"
  - "structureHarvester"
  - "Structure software"
  - "template"
  - "bash script"
  - "StructureHarvester"
  - "SLURM job scripts"
  - "Slurm Workload manager"
  - "population structure"
  - "multilocus genotype data"
  - "job scripts"
  - "Structure"
  - "mainparams"
  - "SLURM"
  - "structureCommands"
  - "automation and parallelization"
  - "StrAuto"

questions:
  - "What is the primary purpose of the Structure software package and what types of genetic markers can it analyze?"
  - "Which specific configuration and data files are required by default when running Structure from the command line?"
  - "How can users achieve parallel execution for population structure inference since the Structure software does not natively support it?"
  - "What is the primary function of the StrAuto tool as described in the referenced 2017 publication?"
  - "Which two specific software tools are mentioned in the provided text fragment?"
  - "What types of online resources and documentation are cited for the StrAuto software?"
  - "Why is it recommended to submit long Structure runs as individual jobs to Slurm rather than grouping them together?"
  - "What specific scripts and software tools must be placed in the working directory to use the create_strauto_slurm_scripts.py script?"
  - "Which specific setting must be enabled in the input.py file before executing the StrAuto setup commands?"
  - "What is the primary purpose of the 'create_strauto_slurm_scripts.py' script?"
  - "What specific settings and parameters must be adjusted in the script and 'input.py' before execution?"
  - "What are the final commands used to submit the batch jobs and aggregate the results once they are completed?"
  - "What options are presented to the user before the system begins writing the output files?"
  - "Which specific parameter files are generated for the dataset named 'my_dataset'?"
  - "What is the purpose of executing the `create_strauto_slurm_scripts.py` command at the end of the process?"
  - "What is the primary purpose of this script regarding the generation of SLURM job scripts and directory structures?"
  - "Which specific input file is required for the script to execute successfully, and what happens if it is missing?"
  - "What are the functions of the `submit_strauto_jobs.sh` and `post_strauto.sh` helper scripts created at the end of the execution?"
  - "What is the primary purpose of the SLURM batch script defined in the `template` variable?"
  - "Which specific software module and version is being loaded for execution within the main job template?"
  - "What file management action does the `post_template` script perform?"
  - "What is the primary purpose of this script regarding the generation of SLURM job scripts and directory structures?"
  - "Which specific input file is required for the script to execute successfully, and what happens if it is missing?"
  - "What are the functions of the `submit_strauto_jobs.sh` and `post_strauto.sh` helper scripts created at the end of the execution?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

Structure[^homepage] is a free software package for using multilocus genotype data to investigate population structure. Its uses include inferring the presence of distinct populations, assigning individuals to populations, studying hybrid zones, identifying migrants and admixed individuals, and estimating population allele frequencies in situations where many individuals are migrants or admixed. It can be applied to most of the commonly-used genetic markers, including SNPs, microsatellites, RFLPs and AFLPs.
[^structure_2000]
[^structure_2009]

## Installed versions

At the time of writing, Structure v2.3.4 has been installed (module: `structure/2.3.4`).
Please look on page [Available software](../programming/available_software.md) for module `structure` for an up-to-date list of installed versions.

## Usage

When starting *structure* without any command-line options, it expects to find the following three files in the current working directory:
* `mainparams` - Example mainparams[^mainparams]
* `extraparams` - Example extraparams[^extraparams]
* and a data file. The name of the data file can either be set by the *INFILE* parameter in `mainparams` or supplied via the command line (-i).

Please refer to §7 "Running *structure* from the command line" in the Structure Documentation[^manual] for a complete description of the available parameters and file-formats. There are also several command-line options to supply alternative filenames or override options, e.g.: -m (mainparams), -e (extraparams), -i (input file), -o (output file).
See section §7.4 in the Structure Documentation[^manual].

Here is an example submission script:

```bash title="structure_job.sh"
#!/bin/bash
#SBATCH --time=0-0:30           # time limit (D-HH:MM)
module load structure
structure -i data_file1  -o results1
```

## Running Structure in parallel: StrAuto & StructureHarvester

The Structure software itself is not able to run in parallel; however, as population structure inference using the Evanno-method[^evanno_2005] involves multiple Structure runs, the tools StrAuto[^strauto_site][^strauto_doc][^strauto_2017] and StructureHarvester[^harvester_site][^harvester_2011] have been developed to automate the process of setting up such runs and aggregating their results, respectively.

### Practical considerations

There is an example for running StrAuto jobs on HPC clusters using the Slurm Workload manager outlined in chapter 8 of the StrAuto User Guide[^strauto_doc].
The example works best when the total number of Structure runs is a multiple of the number of requested tasks, as otherwise some of the allocated CPUs will sit idle while the last Structure runs are being executed. This may lead to a significant waste of computing resources.

Moreover, the requested maximum job time needs to be sufficiently large to accommodate multiple subsequent Structure runs.
While this can be a sensible choice for relatively short runs, jobs with long walltimes will typically have to wait longer until they are dispatched due to [job scheduling policies](../running-jobs/job_scheduling_policies.md#time-limits).
Therefore, in cases where an individual Structure run takes more than just a few hours to finish, we recommend submitting each Structure run as an individual job to Slurm.

### Running a set of longer Structure runs

The script `create_strauto_slurm_scripts.py` shown at the bottom of this section is designed to help you run Structure[^homepage] jobs on Compute Canada HPC clusters that use the Slurm Workload manager.
It requires Structure, StrAuto[^strauto_site], and StructureHarvester[^harvester_site].

Usage:

* Place the `create_strauto_slurm_scripts.py` script shown below into a directory along with:
    * `strauto_1.py` and `input.py` from StrAuto[^strauto_site].
    * `structureHarvester.py` and `harvesterCore.py` from StructureHarvester[^harvester_site].
    * The file with the Structure dataset, e.g., `my_dataset.str`.
* Make `create_strauto_slurm_scripts.py` executable with:
```bash
chmod u+x create_strauto_slurm_scripts.py
```
    * You should now have the following files:
```bash
ls -F
```
```text
create_strauto_slurm_scripts.py*  harvesterCore.py
input.py                          my_dataset.str
strauto_1.py*                     structureHarvester.py*
```
* Edit the settings in `input.py` as described in the StrAuto User Manual[^strauto_doc].
    * Make sure to set the option `parallel = True` (question 23).
* Adjust the parameters in this file (lines 65-70):
    * Set `max_jobtime` to a duration where you can be reasonably sure that no individual Structure run takes longer than this.
    * In cases where a user can submit under multiple Slurm-accounts, `slurm_account` can be used to specify under which account to submit.
    * To avoid overloading the Scheduler, the submission helper script delays each submission by a time defined by `submit_delay`.
* Run the following commands:

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
* Submit the jobs with:
```bash
bash submit_strauto_jobs.sh
```
```text
Submitted batch job 12345001
Submitted batch job 12345002
[...]
Submitted batch job 12345040
```
* After all jobs have completed, run `bash post_strauto.sh` to aggregate the results and run StructureHarvester.

#### The 'create_strauto_slurm_scripts.py' script

```python title="create_strauto_slurm_scripts.py"
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
max_jobtime = '1-0:00:0' # format: d-hh:mm:ss
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
                        MAXTIME=max_jobtime,
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

## References

[^homepage]: Structure Homepage: http://web.stanford.edu/group/pritchardlab/structure.html
[^structure_2000]: J.K. Pritchard, M. Stephens, and P. Donnelly. Inference of population structure using multilocus genotype data. Genetics, 155:945–959, 2000. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461096/
[^structure_2009]: M.J. Hubisz, D. Falush, M. Stephens, and J.K. Pritchard. Inferring weak population structure with the assistance of sample group information. Molecular Ecology Resources, 9(5):1322–1332, 2009. doi: https://doi.org/10.1111/j.1755-0998.2009.02591.x
[^mainparams]: Example [mainparams](http://web.stanford.edu/group/pritchardlab/software/mainparams) on the Structure Homepage
[^extraparams]: Example [extraparams](http://web.stanford.edu/group/pritchardlab/software/extraparams) on the Structure Homepage
[^manual]: Structure Documentation for version 2.3.4 [PDF](http://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v2.3.4/structure_doc.pdf)
[^evanno_2005]: G. Evanno, S. Regnaut, and J. Goudet. Detecting the number of clusters of individuals using the software structure: a simulation study. Molecular Ecology, 14:2611–2620, 2005. DOI: https://doi.org/10.1111/j.1365-294X.2005.02553.x
[^strauto_site]: StrAuto Homepage: https://vc.popgen.org/software/strauto/
[^strauto_doc]: StrAuto User Guide: https://vc.popgen.org/software/strauto/strauto_doc.pdf
[^strauto_2017]: Chhatre, VE & Emerson KJ. StrAuto: Automation and parallelization of STRUCTURE analysis. BMC Bioinformatics (2017) 18:192. doi: http://dx.doi.org/10.1186/s12859-017-1593-0
[^harvester_site]: StructureHarvester Homepage: http://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/ ; GitHub: https://github.com/dentearl/structureHarvester
[^harvester_2011]: Earl, Dent A. and vonHoldt, Bridgett M. STRUCTURE HARVESTER: a website and program for visualizing STRUCTURE output and implementing the Evanno method. Conservation Genetics Resources (2011) DOI: 10.1007/s12686-011-9548-7