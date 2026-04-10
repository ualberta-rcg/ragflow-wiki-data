---
title: "Qiskit/en"
tags:
  []

keywords:
  []
---

Developed in Python by IBM, [Qiskit](https://docs.quantum.ibm.com/) is an open-source quantum computing library. Like [PennyLane](pennylane-en.md) and [Snowflurry](snowflurry-en.md), it allows you to build, simulate and run quantum circuits.

## Installation 
1. Load the Qiskit dependencies.

```bash
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2
```

2. Create and activate a [Python virtual environment](python#creating_and_using_a_virtual_environment.md).

```bash
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
```

3. Install a version of Qiskit.

```bash

```
X.Y.Z  qiskit_aerX.Y.Z}}
where `X.Y.Z` is the version number, for  example `1.4.0`. To install the most recent version available on our clusters, do not specify a number. Here, we only imported `qiskit` and `qiskit_aer`. You can add other Qiskit software with the syntax `qiskit_package==X.Y.Z` where `qiskit_package` is the softare name, for example `qiskit-finance`. To see the wheels that are currently available, see [Available Python wheels](available-python-wheels.md). 

4. Validate the installation.

```bash
python -c 'import qiskit'
```

5. Freeze the environment and its dependencies.

```bash
pip freeze --local > ~/qiskit_requirements.txt
```

## Running Qiskit on a cluster
{{File
  |name=script.sh
  |lang="sh"
  |contents=
#!/bin/bash
#SBATCH --account=def-someuser #Modify with your account name
#SBATCH --time=00:15:00        #Modify as needed
#SBATCH --cpus-per-task=1      #Modify as needed
#SBATCH --mem-per-cpu=1G       #Modify as needed

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2 

# Generate your virtual environment in $SLURM_TMPDIR.                                                                                                         
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Install Qiskit and its dependencies.                                                                                                                                                                                                                                                                                    
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/qiskit_requirements.txt

# Modify your Qiskit program.                                                                                                                                                                       
python qiskit_example.py
}}
You can then [submit your job to the scheduler](running-jobs.md). 
## Using Qiskit with MonarQ 

You can use [MonarQ](monarq.md) directly with Qiskit via the qiskit-calculquebec plugin. This plugin allows you to develop and run Qiskit circuits on the Calcul Québec infrastructure.

<span id="Installation_des_dépendances"></span>
### Install the dependencies 

* Step 1: Install the dependencies

```bash
python -c "import qiskit; import qiskit_calculquebec"
```

* Note: **qiskit-calculquebec** installs Qiskit automatically.

<span id="Initialisation_du_backend_MonarQ"></span>
### MonarQ backend initialisation 

* Step 2: Set up your credentials and the backend
** Create a client using your credentials. Your token is available via the Thunderhead portal.
** The <i>host</i> is ‘’'<nowiki>https://monarq.calculquebec.ca</nowiki>.‘’'
** Then initialize the MonarQ backend.

<span id="Exécution_du_circuit"></span>
### Running the circuit 

* Step 3: Transpile and run the circuit

### Notes 

* Transpilation is required to adapt the circuit to MonarQ's native connectivity and ports.
* The number of <i>shots</i> can be adjusted as needed (maximum: 1024).
* The use of ‘’'SamplerV2'‘’ is recommended for running circuits with measures.

<!--
## Use case: Bell states 
Before you create a simulation of the first Bell state on [Narval](narval-en.md), the required modules need to be loaded. 
    from qiskit_aer import AerSimulator
    from qiskit import QuantumCircuit, transpile
    from qiskit.visualization import plot_histogram

Define the circuit. Apply an Hadamard gate to create a superposition state on the first qubit and a CNOT gate to intricate the first and second qubits.
    circuit = QuantumCircuit(2,2)
    circuit.h(0)
    circuit.cx(0,1)
    circuit.measure_all()

We will use the default simulator `AerSimulator`. This provides the final number of qubits after having made 1000 measurements.
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1000).result()
    counts = result.get_counts()
    print(counts)
    {'00': 489, '11': 535}
The results are displayed.
    plot_histogram(counts)

[thumb|Results of 1000 measurements on the first Bell 
 state](file:qiskit-counts.png.md)

-->