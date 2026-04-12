---
title: "CirQ/en"
slug: "cirq"
lang: "en"

source_wiki_title: "CirQ/en"
source_hash: "1682feceb368b9ce09cc869473586964"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:16:05.378956+00:00"

tags:
  []

keywords:
  - "quantum computing"
  - "CirQ"
  - "quantum circuits"
  - "Python"
  - "Bell states"

questions:
  - "What is the CirQ library and what are its main capabilities in quantum computing?"
  - "What are the necessary steps to install and execute a CirQ job using a Python virtual environment on a computing cluster?"
  - "How does the provided use case utilize CirQ's Hadamard and CNOT gates to construct and simulate a Bell state?"
  - "What is the CirQ library and what are its main capabilities in quantum computing?"
  - "What are the necessary steps to install and execute a CirQ job using a Python virtual environment on a computing cluster?"
  - "How does the provided use case utilize CirQ's Hadamard and CNOT gates to construct and simulate a Bell state?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Developed by Google, [CirQ](https://quantumai.google/cirq) is an open-source quantum computing library to build, optimize, simulate, and run quantum circuits. More specifically, CirQ allows for the simulation of circuits on particular qubit configurations, which can optimize a circuit for a certain qubit architecture. Information on the features can be found in the CirQ [documentation](https://quantumai.google/cirq) and [GitHub](https://github.com/quantumlib/Cirq). Like [Snowflurry](snowflurry.md), CirQ can be used to run quantum circuits on the [MonarQ](monarq.md) quantum computer.

## Installation
The CirQ simulator is available on all of our clusters. To have access, you must load the [Python](python.md) language.

!!! note
    It is preferable to work in a [Python virtual environment](python.md).

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index cirq==1.4.1
python -c "import cirq"
pip freeze > cirq-1.4.1-reqs.txt
```
The last command creates the `cirq-1.4.1-reqs.txt` file, which you can also use in a job script, such as in the example below.

## Running on a Cluster
```sh title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # Modify with your account name
#SBATCH --time=00:15:00        # Modify as needed
#SBATCH --cpus-per-task=1      # Modify as needed
#SBATCH --mem-per-cpu=1G       # Modify as needed

# Load modules dependencies.
module load StdEnv/2023 gcc python/3.11 

# Generate your virtual environment in $SLURM_TMPDIR.                                                                                           
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Install CirQ and its dependencies.                                                                                                                                                                                                                                                                                  
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/cirq-1.4.1-reqs.txt

# Edit with your CirQ program.                                                                                                                                                             
python cirq_example.py
```

You can then [submit your job to the scheduler](running-jobs.md).

## Use case: Bell states
Bell states are the simplest states that allow for the explanation of both superposition and entanglement on qubits.
The [CirQ](https://github.com/quantumlib/Cirq) library allows for the construction of a Bell state as follows:

```python
python> import cirq
python> from cirq.contrib.svg import SVGCircuit
python> from cirq import H, CNOT

python> qubits = cirq.LineQubit.range(2)
python> circuit = cirq.Circuit(H.on(qubits[0]),CNOT.on(qubits[0],qubits[1]))
python> circuit.append(cirq.measure(qubits, key='m'))
python> SVGCircuit(circuit)
```

This code builds and displays a circuit that prepares a Bell state. The H gate (Hadamard gate) creates an equal superposition of |0⟩ and |1⟩ on the first qubit, while the CNOT gate (controlled X gate) creates an entanglement between the two qubits. This Bell state is therefore an equal superposition of the states |00⟩ and |11⟩. Simulating this circuit using CirQ allows you to visualize the results. In this diagram, the integer 3 represents the state |11⟩ since 3 is written 11 in binary.

```python
python> import matplotlib.pyplot as plt
python> s = cirq.Simulator().run(circuit, repetitions=1000)
python> counts = s.histogram(key='m')
python> cirq.plot_state_histogram(counts, plt.subplot())