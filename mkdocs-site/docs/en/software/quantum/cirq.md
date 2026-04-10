---
title: "CirQ/en"
slug: "cirq"
lang: "en"

source_wiki_title: "CirQ/en"
source_hash: "1682feceb368b9ce09cc869473586964"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:25:50.835412+00:00"

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

Google-developed, [CirQ](https://quantumai.google/cirq) is an open-source quantum computing library to build, optimize, simulate, and run quantum circuits. More specifically, CirQ allows simulating circuits on particular qubit configurations, which can optimize a circuit for a certain qubit architecture. Information on the features can be found in the CirQ [documentation](https://quantumai.google/cirq) and [GitHub](https://github.com/quantumlib/Cirq). Like [Snowflurry](snowflurry.md), CirQ can be used to run quantum circuits on the [MonarQ](monarq.md) quantum computer.

## Installation
The CirQ simulator is available on all of our clusters. To have access, you must load the [Python](python/fr.md) language. It is preferable to work in a [Python virtual environment](python/fr.md#créer-et-utiliser-un-environnement-virtuel).

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index cirq==1.4.1
python -c "import cirq"
pip freeze > cirq-1.4.1-reqs.txt
```

The last command creates the `cirq-1.4.1-reqs.txt` file, which you can also use in a job script such as in the example below.

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
Bell states are the simplest states that allow explaining both superposition and entanglement on qubits.
The [CirQ library](https://github.com/quantumlib/Cirq) allows building a Bell state as follows:

```python
python> import cirq
python> from cirq.contrib.svg import SVGCircuit
python> from cirq import H, CNOT

python> qubits = cirq.LineQubit.range(2)
python> circuit = cirq.Circuit(H.on(qubits[0]),CNOT.on(qubits[0],qubits[1]))
python> circuit.append(cirq.measure(qubits, key='m'))
python> SVGCircuit(circuit)
```

This code builds and displays a circuit that prepares a Bell state. The H gate (Hadamard gate) creates an equal superposition of |0⟩ and |1⟩ on the first qubit while the CNOT gate (controlled X gate) creates an entanglement between the two qubits. This Bell state is therefore an equal superposition of the states |00⟩ and |11⟩. Simulating this circuit using CirQ allows you to visualize the results. In this diagram, the integer 3 represents the state |11⟩ since 3 is written 11 in binary.

```python
python> import matplotlib.pyplot as plt
python> s = cirq.Simulator().run(circuit, repetitions=1000)
python> counts = s.histogram(key='m')
python> cirq.plot_state_histogram(counts, plt.subplot())