---
title: "CirQ"
slug: "cirq"
lang: "base"

source_wiki_title: "CirQ"
source_hash: "93cdfe514843f8774c0c095bb53b0ad4"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:25:28.140405+00:00"

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

[CirQ](https://quantumai.google/cirq) is an open-source quantum computing library developed in [Python](python.md) by Google, which allows for building, optimizing, simulating, and executing quantum circuits. More specifically, CirQ allows simulating circuits on specific qubit configurations, which can optimize a circuit for a certain qubit architecture. Information on the library's features is available in the [documentation](https://quantumai.google/cirq) and on CirQ's [GitHub](https://github.com/quantumlib/Cirq). Just like [Snowflurry](snowflurry.md), CirQ can be used to execute quantum circuits on the [MonarQ](monarq.md) quantum computer.

## Installation
The CirQ quantum computer simulator is available on all our clusters. The [Python](python.md) programming language must be loaded before accessing it. It is preferable to work in a [Python virtual environment](python.md#create-and-use-a-virtual-environment).

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index cirq==1.4.1
python -c "import cirq"
pip freeze > cirq-1.4.1-reqs.txt
```
The last command creates a file named `cirq-1.4.1-reqs.txt`, which you can reuse in a job script, as described below.

## Running on a Cluster
```sh linenums="1" hl_lines="1-5 8-9 12-13 16"
#!/bin/bash
#SBATCH --account=def-someuser # specify your account name
#SBATCH --time=00:15:00        # modify if necessary
#SBATCH --cpus-per-task=1      # modify if necessary
#SBATCH --mem-per-cpu=1G       # modify if necessary

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11

# Generate the virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install CirQ and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/cirq-1.4.1-reqs.txt

# Execute the CirQ program.
python cirq_example.py
```

You can then [submit your job to the scheduler](running-jobs.md).

## Usage Example: Bell States
Bell states are the simplest states that allow explaining both superposition and entanglement on qubits.
The [CirQ](https://github.com/quantumlib/Cirq) library allows building a Bell state like this:

```python
import cirq
from cirq.contrib.svg import SVGCircuit
from cirq import H, CNOT

qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(H.on(qubits[0]),CNOT.on(qubits[0],qubits[1]))
circuit.append(cirq.measure(qubits, key='m'))
SVGCircuit(circuit)
```

This code constructs and displays a circuit that prepares a Bell state. The H gate (Hadamard gate) creates an equal superposition of |0⟩ and |1⟩ on the first qubit, while the CNOT gate (controlled X gate) creates entanglement between the two qubits. This Bell state is thus an equal superposition of the |00⟩ and |11⟩ states. Simulating this circuit using CirQ allows visualizing the results. In this diagram, the integer 3 represents the |11⟩ state, since 3 is written as 11 in binary.

```python
import matplotlib.pyplot as plt
s = cirq.Simulator().run(circuit, repetitions=1000)
counts = s.histogram(key='m')
cirq.plot_state_histogram(counts, plt.subplot())