---
title: "PennyLane"
slug: "pennylane"
lang: "base"

source_wiki_title: "PennyLane"
source_hash: "5325db467b52a40e6edff85e616ebdd3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:21:26.323185+00:00"

tags:
  []

keywords:
  - "PennyLane"
  - "apprentissage automatique"
  - "version désirée"
  - "calcul quantique différentiable"
  - "MonarQ"
  - "circuits quantiques"
  - "état de Bell"
  - "environnement virtuel"
  - "pip install"
  - "grappe"
  - "Python"
  - "circuit quantique"

questions:
  - "Qu'est-ce que la plateforme PennyLane et quel est son rôle dans le développement d'algorithmes quantiques hybrides ?"
  - "Quelles sont les principales fonctionnalités de PennyLane en matière d'intégration avec les bibliothèques d'apprentissage automatique et les différents matériels quantiques ?"
  - "Comment le plugiciel PennyLane-CalculQuebec permet-il d'exécuter des circuits quantiques sur l'ordinateur MonarQ ?"
  - "Comment configurer un environnement virtuel et installer les dépendances de PennyLane à l'aide d'un fichier de prérequis ?"
  - "Quelles sont les directives et commandes nécessaires dans un script SLURM pour exécuter un programme PennyLane sur une grappe de calcul ?"
  - "Quelles fonctions de la bibliothèque PennyLane sont utilisées dans l'exemple de code pour créer et simuler un circuit quantique générant un état de Bell ?"
  - "Quel est l'objectif principal de la création de cet environnement virtuel Python ?"
  - "Quelles sont les commandes spécifiques à exécuter pour initialiser l'environnement et installer le module ?"
  - "Que signifie la notation \"X.Y.Z\" mentionnée à la fin des instructions d'installation ?"
  - "Comment configurer un environnement virtuel et installer les dépendances de PennyLane à l'aide d'un fichier de prérequis ?"
  - "Quelles sont les directives et commandes nécessaires dans un script SLURM pour exécuter un programme PennyLane sur une grappe de calcul ?"
  - "Quelles fonctions de la bibliothèque PennyLane sont utilisées dans l'exemple de code pour créer et simuler un circuit quantique générant un état de Bell ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[PennyLane](https://pennylane.ai) is an open-source software platform for differentiable quantum computing, with [the first version published on GitHub](https://github.com/calculquebec/pennylane-snowflurry) in 2018. Developed in Toronto by Xanadu, PennyLane allows users to design quantum circuits and execute them on various simulators and quantum hardware. The platform is designed to facilitate the simulation, optimization, and learning of hybrid quantum algorithms that combine classical and quantum processing.

## Features
PennyLane offers several features to facilitate research and development in the field of differentiable quantum computing.

### Unified Quantum Interface
PennyLane provides a unified interface that allows users to design quantum circuits and execute them on different quantum simulators and hardware. The platform supports several popular quantum simulators, such as [Qiskit](qiskit.md), [CirQ](cirq.md), Strawberry Fields, and QuTip. PennyLane also supports several quantum hardware platforms, including quantum devices from Xanadu, IBM, Rigetti, and IonQ.

Calcul Québec has developed the [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) plugin, which uses the PennyLane interface to design and execute quantum circuits on [MonarQ](../../clusters/monarq.md).

### Integration with Machine Learning Libraries
PennyLane integrates seamlessly with popular machine learning libraries such as [TensorFlow](../tensorflow.md) and [PyTorch](../pytorch.md), allowing you to use machine learning tools to build hybrid quantum machine learning models and optimize quantum circuits.

### Quantum Circuit Optimization
By using differentiable optimization techniques and combining classical and quantum differentiation methods, PennyLane optimizes the parameters of quantum circuits to solve various problems.

### Visualization Tools
PennyLane provides visualization tools to facilitate understanding of how quantum circuits operate.

### Community and Development
PennyLane is an open-source project with an active community of developers and users. The project is constantly updated with new features and improvements, and everyone can contribute to the platform's development.

## Using PennyLane with MonarQ
[MonarQ](../../clusters/monarq.md) is designed to be programmed with [Snowflurry](snowflurry.md), a software library programmed in Julia and developed by Anyon Systems. However, thanks to the PennyLane-CalculQuebec plugin, PennyLane circuits can be created using Snowflurry in the backend. This allows circuits to be executed on [MonarQ](../../clusters/monarq.md) while benefiting from the features and development environment offered by PennyLane. See the [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) documentation for installation and usage guides.

A [quantum transpiler](quantum-transpiler.md) is also available from PennyLane to optimize its circuits for MonarQ.

## Creating the Virtual Environment
[Let's create a Python virtual environment](../python.md#creating-and-using-a-virtual-environment) to use PennyLane.
```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index pennylane==X.Y.Z
python -c "import pennylane"
```
where `X.Y.Z` is the desired version.

You can also write the last three commands above into a `pennylane-reqs.txt` file and call the file within a session with the commands:
```bash
module load python/3.11
pip install --no-index -r pennylane-reqs.txt
```

## Running PennyLane on a Cluster
```sh linenums="1" title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # Enter your account name
#SBATCH --time=00:15:00        # Modify as needed
#SBATCH --cpus-per-task=1      # Modify as needed
#SBATCH --mem-per-cpu=1G       # Modify as needed

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11

# Generate the virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install PennyLane and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/pennylane_requirements.txt

# Run your PennyLane program.
python pennylane_example.py
```
You can then submit your job to [the scheduler](../../running-jobs/running_jobs.md).

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
```
```
First Bell state :[0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

## References
* [PennyLane Official Website](https://pennylane.ai)
* [PennyLane Documentation on GitHub](https://github.com/PennyLaneAI/pennylane)
* [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry)