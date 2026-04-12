---
title: "CirQ"
slug: "cirq"
lang: "base"

source_wiki_title: "CirQ"
source_hash: "93cdfe514843f8774c0c095bb53b0ad4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:15:45.661928+00:00"

tags:
  []

keywords:
  - "états de Bell"
  - "simulations"
  - "CirQ"
  - "Cirq"
  - "porte CNOT"
  - "état de Bell"
  - "porte de Hadamard"
  - "informatique quantique"
  - "Python"
  - "intrication"
  - "diagramme"
  - "circuit quantique"

questions:
  - "Qu'est-ce que la bibliothèque CirQ et quelles sont ses principales fonctionnalités en informatique quantique ?"
  - "Quelles sont les étapes requises pour installer CirQ et soumettre une tâche d'exécution sur une grappe de calcul ?"
  - "Comment le code fourni utilise-t-il les portes quantiques dans CirQ pour construire et simuler un état de Bell ?"
  - "Quelles bibliothèques Python sont utilisées pour simuler et tracer les résultats du circuit quantique ?"
  - "Combien de répétitions sont effectuées lors de la simulation du circuit selon le code fourni ?"
  - "Quel état quantique spécifique est représenté par le diagramme généré à l'issue des simulations ?"
  - "Quels sont les rôles respectifs de la porte de Hadamard et de la porte CNOT dans la création de l'état de Bell ?"
  - "De quels états quantiques l'état de Bell final est-il une superposition égale ?"
  - "Comment le simulateur CirQ représente-t-il l'état |11⟩ dans ses résultats et pour quelle raison ?"
  - "Quelles bibliothèques Python sont utilisées pour simuler et tracer les résultats du circuit quantique ?"
  - "Combien de répétitions sont effectuées lors de la simulation du circuit selon le code fourni ?"
  - "Quel état quantique spécifique est représenté par le diagramme généré à l'issue des simulations ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CirQ](https://quantumai.google/cirq) is an open-source quantum computing library developed in [Python](python.md) by Google, which allows building, optimizing, simulating, and executing quantum circuits. More specifically, CirQ allows simulating circuits on specific qubit configurations, which can optimize a circuit for a certain qubit architecture. Information on the library's features is available in the [documentation](https://quantumai.google/cirq) and on CirQ's [GitHub](https://github.com/quantumlib/Cirq). Like [Snowflurry](snowflurry.md), CirQ can be used to execute quantum circuits on the [MonarQ](monarq.md) quantum computer.

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
::: sh title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # specify your account name
#SBATCH --time=00:15:00        # modify if needed
#SBATCH --cpus-per-task=1      # modify if needed
#SBATCH --mem-per-cpu=1G       # modify if needed

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11

# Generate the virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install CirQ and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/cirq-1.4.1-reqs.txt

# Modify the CirQ program.
python cirq_example.py
```

You can then [submit your job to the scheduler](running-jobs.md).

## Example Usage: Bell States
Bell states are the simplest states that allow explaining both superposition and entanglement on qubits.
The [CirQ](https://github.com/quantumlib/Cirq) library allows building a Bell state as follows:
```python
import cirq
from cirq.contrib.svg import SVGCircuit
from cirq import H, CNOT

qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(H.on(qubits[0]), CNOT.on(qubits[0], qubits[1]))
circuit.append(cirq.measure(qubits, key='m'))
SVGCircuit(circuit)
```
This code constructs and displays a circuit that prepares a Bell state. The H gate (Hadamard gate) creates an equal superposition of |0⟩ and |1⟩ on the first qubit, while the CNOT gate (controlled-X gate) creates entanglement between the two qubits. This Bell state is thus an equal superposition of the |00⟩ and |11⟩ states. Simulating this circuit using CirQ allows visualizing the results. In this diagram, the integer 3 represents the |11⟩ state, since 3 is written as 11 in binary.
```python
import matplotlib.pyplot as plt
s = cirq.Simulator().run(circuit, repetitions=1000)
counts = s.histogram(key='m')
cirq.plot_state_histogram(counts, plt.subplot())