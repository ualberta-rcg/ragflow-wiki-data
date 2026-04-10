---
title: "PennyLane"
slug: "pennylane"
lang: "base"

source_wiki_title: "PennyLane"
source_hash: "5325db467b52a40e6edff85e616ebdd3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:53:21.591949+00:00"

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

[PennyLane](https://pennylane.ai/) is an open-source software platform for differentiable quantum computing, with [its first version published on GitHub](https://github.com/calculquebec/pennylane-snowflurry) in 2018. Developed in Toronto by Xanadu, PennyLane allows for designing quantum circuits and executing them on various quantum simulators and hardware. The platform is designed to facilitate the simulation, optimization, and learning of hybrid quantum algorithms that combine classical and quantum processing.

## Features
PennyLane offers several features to facilitate research and development in the field of differentiable quantum computing.

### Unified Quantum Interface
PennyLane provides a unified interface that allows for designing quantum circuits and executing them on different simulators and quantum hardware. The platform supports several popular quantum simulators, such as [Qiskit](qiskit.md), [CirQ](cirq.md), Strawberry Fields, and QuTip. PennyLane also supports several quantum hardware, including devices from Xanadu, IBM, Rigetti, and IonQ.

Calcul Québec developed the [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) plugin, which uses the PennyLane interface to design and execute quantum circuits on [MonarQ](monarq.md).

### Integration with Machine Learning Libraries
PennyLane integrates seamlessly with popular machine learning libraries such as [TensorFlow](tensorflow.md) and [PyTorch](pytorch.md), and allows you to use machine learning tools to build hybrid quantum machine learning models and optimize quantum circuits.

### Quantum Circuit Optimization
By using differentiable optimization techniques and combining classical and quantum differentiation methods, PennyLane optimizes the parameters of quantum circuits to solve various problems.

### Visualization Tools
PennyLane provides visualization tools to facilitate understanding how quantum circuits operate.

### Community and Development
PennyLane is an open-source project with an active community of developers and users. The project is constantly updated with new features and improvements, and everyone can contribute to the platform's development.

## Using PennyLane with MonarQ
[MonarQ](monarq.md) is designed to be programmed with [Snowflurry](snowflurry.md), a software library programmed in Julia and developed by Anyon Systems. However, thanks to the PennyLane-CalculQuebec plugin, PennyLane circuits can be created using Snowflurry in the background. This allows for executing circuits on [MonarQ](monarq.md) while benefiting from the features and development environment offered by PennyLane. See the [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) documentation for installation and usage guides.

A [quantum transpiler](transpileur-quantique.md) is also available from PennyLane to optimize circuits for [MonarQ](monarq.md).

## Creating the Virtual Environment
Let's [create a Python virtual environment](python.md#creating-and-using-a-virtual-environment) to use PennyLane.
```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index pennylane==X.Y.Z
python -c "import pennylane"
```
where `X.Y.Z` is the desired version.

You can also save the last three commands above into a `pennylane-reqs.txt` file and call the file within a session with the commands:
```bash
module load python/3.11
pip install --no-index -r pennylane-reqs.txt
```

## Running PennyLane on a Cluster
```sh linenums="1"
#!/bin/bash
#SBATCH --account=def-someuser # Enter your account name
#SBATCH --time=00:15:00        # Modify if necessary
#SBATCH --cpus-per-task=1      # Modify if necessary
#SBATCH --mem-per-cpu=1G       # Modify if necessary

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11 

# Generate the virtual environment in $SLURM_TMPDIR.                                                                                                        
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Install PennyLane and its dependencies.                                                                                                                                                                                                                                                                                    
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/pennylane_requirements.txt

# Modify your PennyLane program.                                                                                                                                                                       
python pennylane_example.py
```
You can then submit your job to [the scheduler](running-jobs.md).

## Usage Example: Bell States
Let's start by creating the virtual environment, as described above.

Next, we will generate the first Bell state using PennyLane.
```python
import pennylane as qml

# Define the quantum circuit to generate the first Bell state
def bell_circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

# Define the quantum circuit simulator
dev = qml.device('default.qubit', wires=2)

# Define the quantum circuit as a QNode function
@qml.qnode(dev)
def generate_bell_state():
    bell_circuit()
    return qml.state()

# Generate and display the first Bell state
bell_state_0 = generate_bell_state()
print("First Bell state :", bell_state_0)
# Expected output:
# First Bell state : [0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

## References
*   [Official PennyLane Website](https://pennylane.ai)
*   [PennyLane Documentation on GitHub](https://github.com/PennyLaneAI/pennylane)
*   [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry)