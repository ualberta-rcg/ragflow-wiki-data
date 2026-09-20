---
title: "MonarQ/en-ca"
slug: "monarq_en-ca"
lang: "base"

source_wiki_title: "MonarQ/en-ca"
source_hash: "0817695a92a401ca28b51591869368e6"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:48:24.048359+00:00"

tags:
  []

keywords:
  - "Narval"
  - "soumission de tâches"
  - "CalculQuebecClient"
  - "portail Thunderhead"
  - "circuit quantique"
  - "PennyLane"
  - "environnement de développement PennyLane"
  - "plugiciel PennyLane-CalculQuébec"
  - "sbatch"
  - "fichier slurm‑*.out"
  - "fidélité de 99"
  - "8 %"
  - "FAQ (foire aux questions)"
  - "Slurm"
  - "ordinateur quantique à 24 qubits"
  - "Snowflurry"
  - "simple_job.sh"
  - "Julia"
  - "MonarQ"
  - "circuit"
  - "ordonnanceur"

questions:
  - "Quels sont les principaux paramètres techniques de MonarQ, tels que le nombre de qubits, la fidélité des portes, le temps de cohérence et la profondeur maximale des circuits ?"
  - "Quelles sont les étapes à suivre, ainsi que les prérequis (compte Alliance, formulaire, rencontre avec l’équipe), pour obtenir un accès au tableau de bord MonarQ et générer un jeton d’accès ?"
  - "Quelles bibliothèques logicielles (PennyLane, Snowflurry, Qiskit) et quels plugiciels permettent d’exécuter des circuits quantiques sur MonarQ, et comment les intégrer via Snowflurry ou le plug‑in PennyLane‑CalculQuébec ?"
  - "Quels sont les prérequis nécessaires avant de commencer à utiliser MonarQ ?"
  - "Comment configure‑t‑on les identifiants et le device PennyLane pour exécuter un circuit sur MonarQ ?"
  - "Quelle est la procédure pour soumettre et exécuter un circuit quantique sur MonarQ à l’aide de Slurm ?"
  - "Quel est le rôle de Snowflurry et dans quel langage de programmation est‑il implémenté ?"
  - "Comment MonarQ assure‑t‑il la compatibilité native avec Snowflurry ?"
  - "En quoi le plugiciel développé par Calcul Québec améliore‑t‑il l’utilisation de MonarQ avec l’environnement PennyLane ?"
  - "Quelle est la fonction de la commande `sbatch` dans le cadre de l’exécution du circuit ?"
  - "Comment doit être rédigé le script `simple_job.sh` pour être soumis correctement avec `sbatch` ?"
  - "Que représente le message « Submitted batch job 123456 » affiché après l’exécution de la commande `sbatch` ?"
  - "Comment soumettre un script Python sur le cluster Narval avec SLURM et quelles sont les options à modifier selon les besoins ?"
  - "Où se trouve le fichier de sortie du circuit quantique et comment lire le dictionnaire de résultats qu’il contient ?"
  - "Quelles sont les principales applications de MonarQ et comment contacter le support technique en cas de besoin ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Connection Node: https://manager.anyonlabs.com |
| :--------------------------------------------- |

MonarQ is a 24-qubit superconducting quantum computer developed in Montreal by [Anyon Systems](https://anyonsys.com/) and located at the [École de technologie supérieure](http://www.etsmtl.ca/). For more information on MonarQ's specifications and performance, see [Technical Specifications](#technical-specifications) below.

## Accessing MonarQ

1.  To begin the process of accessing MonarQ, [fill out this form](https://forms.gle/zH1a3oB4SGvSjAwh7). It must be completed by the principal investigator.
2.  You must [have an Alliance account](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/gestion-de-compte/demander-un-compte) to access MonarQ.
3.  Meet with our team to discuss your project's specific needs, access, and billing details.
4.  Receive access to the MonarQ dashboard and generate your access token.
5.  To get started, see [Getting Started with MonarQ](#getting-started-with-monarq) below.

Contact our quantum team at [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca) if you have any questions or would like a more general discussion before requesting access.

## Technical Specifications

Like other quantum processors available today, MonarQ operates in an environment where noise remains a significant factor. Performance metrics, updated with each calibration, are accessible via the Thunderhead portal. Access to this portal requires MonarQ access approval.

Among other things, the following metrics are available:

*   24-qubit quantum processor
*   One-qubit gate with 99.8% fidelity and 32ns duration
*   Two-qubit gate with 96% fidelity and 90ns duration
*   Coherence time of 4-10μs (depending on the state)
*   Maximum circuit depth of approximately 350 for one-qubit gates and 115 for two-qubit gates

## Quantum Computing Software

Several specialized software libraries exist for quantum computing and developing quantum algorithms. These libraries allow you to build circuits that are executed on simulators which mimic the performance and results obtained on a quantum computer such as MonarQ. They can be used on all Alliance clusters.

*   [PennyLane](../software/quantum/pennylane.md), Python command library
*   [Snowflurry](../software/quantum/snowflurry.md), Julia command library
*   [Qiskit](../software/quantum/qiskit.md), Python command library

MonarQ's quantum logic gates are called via the [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) software library, written in [Julia](https://julialang.org/). Although MonarQ is natively compatible with Snowflurry, there is a [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin developed by Calcul Québec that allows circuits to be executed on MonarQ while leveraging the features and development environment offered by [PennyLane](https://docs.alliancecan.ca/wiki/PennyLane).

## Getting Started with MonarQ

!!! note "Prerequisites"
    Ensure you have access to MonarQ and your login credentials (*username*, *API token*). For any questions, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).

*   **Step 1: Connect to [Narval](narval.md)**
    *   MonarQ is accessible from Narval, a Calcul Québec cluster. Access to Narval is via the connection node `narval.alliancecan.ca`.
    *   For help connecting to Narval, consult the [SSH](../getting-started/ssh.md) page.

*   **Step 2: Create the environment**
    *   Create a Python virtual environment (3.11 or later) to use PennyLane and the [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin. These are already installed on Narval, and you will only need to import the software libraries you wish to use.

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index --upgrade pennylane-calculquebec
python -c "import pennylane; import pennylane_calculquebec"
```

*   **Step 3: Configure your MonarQ credentials and define MonarQ as the *device***
    *   Open a Python `.py` file and import the necessary dependencies, namely PennyLane and `CalculQuebecClient` as shown in the example below.
    *   Create a client with your credentials. Your token is available from the Thunderhead portal. The *host* is `https://manager.anyonlabs.com`.
    *   Create a PennyLane *device* with your client. You can also specify the number of qubits (*wires*) to use and the number of samples (*shots*).
    *   For help, consult [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

```python
# my_circuit.py
import pennylane as qml
from pennylane_calculquebec.API.client import CalculQuebecClient

my_client = CalculQuebecClient(host="https://monarq.calculquebec.ca", user="your username", access_token="your access token", project_id="your project_id")

dev = qml.device("monarq.default", client = my_client, wires = 3)
```

*   **Step 4: Create your circuit**
    *   In the same Python file, you can now code your quantum circuit.

```python
# my_circuit.py
@qml.set_shots(1000)
@qml.qnode(dev)

def bell_circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])

    return qml.counts()

result = bell_circuit()
print(result)
```

*   **Step 5: Execute your circuit from the scheduler**
    *   The `sbatch` command is used to submit a task [sbatch](https://slurm.schedmd.com/sbatch.html).

```bash
$ sbatch simple_job.sh
Submitted batch job 123456
```

    *   With a Slurm script similar to this:

```sh
# simple_job.sh
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser # Your username
#SBATCH --cpus-per-task=1      # Modify if applicable
#SBATCH --mem-per-cpu=1G 	  # Modify if applicable
python my_circuit.py
```

    *   The circuit's output is written to a file named `slurm-` followed by the job ID and the `.out` suffix, for example, *slurm-123456.out*.
    *   In this file, you will find the circuit's result in a dictionary `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
    *   For more information on how to submit jobs on Narval, see [Running jobs](../running-jobs/running_jobs.md).

## Common Questions

*   [Frequently Asked Questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Other Tools

*   [Quantum Transpiler](../software/quantum/transpileur_quantique.md)

## Applications

MonarQ is suited for computations requiring small numbers of high-fidelity qubits, making it an ideal tool for the development and testing of quantum algorithms. Other possible applications include modelling small quantum systems; testing new quantum programming and error correction methods and techniques; and more generally, fundamental research in quantum computing.

## Technical Support

If you have questions about our quantum services, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).
Sessions on quantum computing and programming with MonarQ are [listed here](https://www.eventbrite.com/o/calcul-quebec-8295332683).