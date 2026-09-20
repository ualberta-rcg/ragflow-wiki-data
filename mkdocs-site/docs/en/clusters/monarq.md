---
title: "MonarQ/en"
slug: "monarq"
lang: "en"

source_wiki_title: "MonarQ/en"
source_hash: "ef2a96b0a9452de96541222e7f9893c8"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:47:48.980170+00:00"

tags:
  []

keywords:
  - "sbatch"
  - "MonarQ"
  - "CalculQuebecClient"
  - "SSH"
  - "Snowflurry"
  - "Narval login node"
  - "qubits"
  - "quantum circuit"
  - "Python virtual environment"
  - "pennylane‑snowflurry plugin"
  - "PennyLane"
  - "calcul quantique"

questions:
  - "Comment peut‑on demander l’accès à MonarQ et quelles sont les conditions préalables requises ?"
  - "Quelles sont les spécifications techniques du processeur quantique MonarQ (nombre de qubits, fidélité des portes, temps de cohérence, profondeur maximale du circuit) ?"
  - "Quels logiciels et bibliothèques sont compatibles avec MonarQ et comment les utiliser sur le cluster Narval ?"
  - "How do you configure your MonarQ identifiers and create a PennyLane device for running a quantum circuit?"
  - "What are the steps to write and submit a Slurm job that executes a PennyLane circuit on MonarQ, and where is the result stored?"
  - "According to the documentation, what kinds of quantum computing applications is MonarQ particularly suited for?"
  - "How do users connect to the Narval cluster and what is the address of its login node?"
  - "What Python version and steps are required to create a virtual environment for using PennyLane on Narval?"
  - "Which PennyLane-related libraries are already installed on Narval, and how should they be imported?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "MonarQ Login Node"
    The MonarQ login node is: **https://monarq.calculquebec.ca**

!!! warning
    **MonarQ is currently undergoing maintenance and should be operational in February 2026. In the meantime, Calcul Québec can offer access to a similar but smaller machine, with 6 qubits.**

Its name is inspired by the monarch butterfly, a symbol of evolution and migration. The capital Q denotes the quantum nature of the computer and its origins in Quebec. Acquisition of MonarQ was made possible with the support of the [Ministère de l'Économie, de l'Innovation et de l'Énergie du Québec (MEIE)](https://www.economie.gouv.qc.ca/) and [Canada Economic Development (CED)](https://ced.canada.ca/en/ced-home/).

## Getting access to MonarQ

1.  To begin the process of getting access to MonarQ, [complete this form](https://forms.gle/zH1a3oB4SGvSjAwh7). It can only be completed by the principal investigator.
2.  You must have an [account with the Alliance](https://alliancecan.ca/en/services/advanced-research-computing/account-management/apply-account) in order to get access to MonarQ.
3.  Meet with our team to discuss the specifics of your project.
4.  Receive access to the MonarQ dashboard and generate your access token.
5.  To get started using MonarQ, see [Getting started](#getting-started) below.

Contact our quantum team at [quantum@calculquebec.ca](mailto:quantum@calculquebec.ca) if you have any questions or if you want to have a more general discussion before requesting access to MonarQ.

## Technical specifications

Like quantum processors available today, MonarQ operates in an environment where noise remains a significant factor. Performance metrics, updated at each calibration, are accessible via the Thunderhead portal which you will be able to use after being approved for access to MonarQ.

Among the metrics are:

*   24-qubit quantum processor
*   Single-qubit gate: 99.8% fidelity with gate duration of 15ns
*   Two-qubit gate: 95.6% fidelity with gate duration of 35ns
*   Coherence time: 4-10μs (depending on state)
*   Maximum circuit depth: approximately 350 for single-qubit gates and 115 for two-qubit gates

## Quantum computing software

There are several specialized software libraries for quantum computing and the development of quantum algorithms. These libraries allow you to build circuits that are executed on simulators that mimic the performance and results obtained on a quantum computer such as MonarQ. They can be used on all Alliance clusters.

*   [PennyLane](../software/quantum/pennylane.md), for Python commands
*   [Snowflurry](../software/quantum/snowflurry.md), for Julia commands
*   [Qiskit](../software/quantum/qiskit.md), for Python commands

The quantum logic gates of the MonarQ processor are called through a [Snowflurry](../software/quantum/snowflurry.md) software library written in [Julia](../software/julia.md). Although MonarQ is natively compatible with Snowflurry, there is a [PennyLane-Snowflurry](https://github.com/calculquebec/pennylane-snowflurry) plugin developed by Calcul Québec that allows you to execute circuits on MonarQ while benefiting from the features and development environment offered by [PennyLane](../software/quantum/pennylane.md).

## Getting started

!!! note "Prerequisites"
    Make sure you have access to MonarQ and that you have your login credentials (*username*, *API token*). If you have any questions, write to [quantique@calculquebec.ca](mailto:quantum@calculquebec.ca).

*   **Step 1: Connect to [Narval](narval.md)**
    *   MonarQ is only accessible from Narval, a Calcul Québec cluster. Narval is accessed from the login node `narval.alliancecan.ca`.
    *   For help connecting to Narval, see [SSH](../getting-started/ssh.md).

*   **Step 2: Create the environment**
    *   Create a Python virtual environment (3.11 or later) to use PennyLane and the [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin. These are already installed on Narval so that you will only have to import the software libraries you want.

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index --upgrade pennylane-calculquebec
python -c "import pennylane; import pennylane_calculquebec"
```

*   **Step 3: Configure your identifiers on MonarQ and define MonarQ as your device**
    *   Open a Python .py file and import the required dependencies (in the following example, PennyLane and MonarqClient).
    *   Create a client with your identifiers. Your token is available through the Thunderhead portal. The *host* is `https://monarq.calculquebec.ca`.
    *   Create a PennyLane device with your client. You can also enter the number of qubits (*wires*) and the number of shots.
    *   For more information, see [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

```python title="my_circuit.py"
import pennylane as qml
from pennylane_calculquebec.API.client import CalculQuebecClient

my_client = CalculQuebecClient(host="https://monarq.calculquebec.ca", user="your username", access_token="your access token", project_id="your project_id")

dev = qml.device("monarq.default", client = my_client, wires = 3)
```

*   **Step 4: Create your circuit**
    *   In the same Python file, you can now code your quantum circuit.

```python title="my_circuit.py"
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
    *   The [`sbatch`](https://slurm.schedmd.com/sbatch.html) command is used to submit a task.

```bash
$ sbatch simple_job.sh
Submitted batch job 123456
```
The Slurm script is similar to
```sh title="simple_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser # Your username
#SBATCH --cpus-per-task=1      # Modify if necessary
#SBATCH --mem-per-cpu=1G 	  # Modify if necessary
python my_circuit.py
```
*   The result is written to a file with a name starting with `slurm-`, followed by the task ID and the `.out` suffix, for example *slurm-123456.out*.
*   The file contains the result in dictionary `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
*   For more information on submitting tasks on Narval, see [Running jobs](../running-jobs/running_jobs.md).

## FAQ

*   [Frequently Asked Questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Other tools

*   [Quantum transpilation](../software/quantum/transpileur_quantique.md)

## Applications

MonarQ is suited for computations requiring small quantities of high-fidelity qubits, making it an ideal tool to develop and test quantum algorithms. Other possible applications include modelling small quantum systems; testing new methods and techniques for quantum programming and error correction; and more generally, fundamental research in quantum computing.

## Technical support

For questions about our quantum services, write to [quantum@calculquebec.ca](mailto:quantum@calculquebec.ca).
Sessions on quantum computing and programming with MonarQ are [listed here](https://www.eventbrite.com/o/calcul-quebec-8295332683).