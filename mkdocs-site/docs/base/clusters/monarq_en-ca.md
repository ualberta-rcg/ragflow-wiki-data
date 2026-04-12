---
title: "MonarQ/en-ca"
slug: "monarq_en-ca"
lang: "base"

source_wiki_title: "MonarQ/en-ca"
source_hash: "aeb0bb0aa150443c2cfc2b10420e487c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:28:36.731412+00:00"

tags:
  []

keywords:
  - "algorithmes quantiques"
  - "calcul quantique"
  - "qml.device"
  - "MonarQ"
  - "Circuit quantique"
  - "Anyon Systèmes"
  - "simulateurs"
  - "monarq"
  - "Snowflurry"
  - "informatique quantique"
  - "Calcul Québec"
  - "ordinateur quantique"
  - "circuit quantique"
  - "qubits"
  - "CalculQuebecClient"
  - "bibliothèques"
  - "fichier Python"
  - "ordonnanceur Slurm"
  - "PennyLane"

questions:
  - "Qu'est-ce que l'ordinateur quantique MonarQ et quand sera-t-il de nouveau opérationnel ?"
  - "Quelles sont les étapes à suivre pour obtenir un accès à MonarQ ?"
  - "Quelles sont les principales spécifications techniques et les performances du processeur quantique MonarQ ?"
  - "Quelles bibliothèques logicielles permettent d'interagir avec le processeur quantique MonarQ et comment sont-elles intégrées ?"
  - "Quels sont les prérequis et l'infrastructure réseau (comme la grappe Narval) nécessaires pour se connecter à MonarQ ?"
  - "Comment configurer son environnement Python et ses identifiants pour définir MonarQ comme périphérique d'exécution d'un circuit quantique ?"
  - "À quoi servent les bibliothèques mentionnées dans le domaine du calcul quantique ?"
  - "Quel est le rôle des simulateurs par rapport aux ordinateurs quantiques tels que MonarQ ?"
  - "Sur quelle infrastructure informatique est-il possible d'utiliser ces outils de développement quantique ?"
  - "Quelles informations sont requises pour initialiser la connexion avec le `CalculQuebecClient` ?"
  - "Comment le dispositif quantique est-il configuré à l'aide de la bibliothèque PennyLane (`qml.device`) ?"
  - "Quelle action l'utilisateur doit-il accomplir à l'étape 4 dans son fichier Python ?"
  - "Comment soumettre et exécuter un circuit quantique à l'aide de l'ordonnanceur Slurm ?"
  - "Où et sous quel format les résultats de l'exécution du circuit sont-ils enregistrés ?"
  - "Quelles sont les principales applications et les cas d'usage idéaux pour le système quantique MonarQ ?"
  - "Comment soumettre et exécuter un circuit quantique à l'aide de l'ordonnanceur Slurm ?"
  - "Où et sous quel format les résultats de l'exécution du circuit sont-ils enregistrés ?"
  - "Quelles sont les principales applications et les cas d'usage idéaux pour le système quantique MonarQ ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "MonarQ Status Update"

    MonarQ is currently undergoing maintenance and is expected to be operational in February 2026. In the meantime, Calcul Québec can offer access to a similar but smaller machine with 6 qubits.

    **Connection Node**: `https://monarq.calculquebec.ca`

MonarQ is a 24-qubit superconducting quantum computer developed in Montreal by [Anyon Systèmes](https://anyonsys.com/) and located at the [École de technologie supérieure](http://www.etsmtl.ca/). For more information on MonarQ's specifications and performance, see [Technical Specifications](#technical-specifications) below.

## Accessing MonarQ

1.  To begin the MonarQ access process, [fill out this form](https://forms.gle/zH1a3oB4SGvSjAwh7). It must be completed by the principal investigator.
2.  You must [have an Alliance account](https://alliancecan.ca/en/services/advanced-research-computing/research-portal/account-management/request-account) to access MonarQ.
3.  Meet with our team to discuss your project's specific needs, access, and billing details.
4.  Receive access to the MonarQ dashboard and generate your access token.
5.  To get started, see [Getting Started with MonarQ](#getting-started-with-monarq) below.

Contact our quantum team at [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca) if you have any questions or would like a more general discussion before requesting access.

## Technical Specifications

Similar to other quantum processors available today, MonarQ operates in an environment where noise remains a significant factor. Performance metrics, updated with each calibration, are accessible via the Thunderhead portal. Access to this portal requires approved MonarQ access.

Among others, the following metrics are available:

*   24-qubit quantum processor
*   Single-qubit gate with 99.8% fidelity and 32ns duration
*   Two-qubit gate with 96% fidelity and 90ns duration
*   Coherence time of 4-10μs (depending on state)
*   Maximum circuit depth of approximately 350 for single-qubit gates and 115 for two-qubit gates

## Quantum Computing Software

Several specialized software libraries exist for quantum computing and developing quantum algorithms. These libraries allow for the construction of circuits that are executed on simulators imitating the performance and results obtained on a quantum computer like MonarQ. They can be used on all Alliance clusters.

*   [PennyLane](../software/quantum/pennylane.md), Python command library
*   [Snowflurry](../software/quantum/snowflurry.md), Julia command library
*   [Qiskit](../software/quantum/qiskit.md), Python command library

MonarQ's quantum logic gates are called through the [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) software library, written in [Julia](https://julialang.org/). Although MonarQ is natively compatible with Snowflurry, a [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin developed by Calcul Québec allows for executing circuits on MonarQ while benefiting from the features and development environment offered by [PennyLane](../software/quantum/pennylane.md).

## Getting Started with MonarQ

**Prerequisites**: Ensure you have MonarQ access and your login credentials (*username*, *API token*). For any questions, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).

*   **Step 1: Connect to [Narval](narval.md)**
    *   MonarQ is only accessible from Narval, a Calcul Québec cluster. Access to Narval is via the connection node `narval.alliancecan.ca`.
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

*   **Step 3: Configure your MonarQ credentials and define MonarQ as a *device***
    *   Open a Python `.py` file and import the necessary dependencies, PennyLane and CalculQuebecClient, as shown in the example below.
    *   Create a client with your credentials. Your token is available from the Thunderhead portal. The *host* is `https://monarq.calculquebec.ca`.
    *   Create a PennyLane *device* with your client. You can also specify the number of qubits (*wires*) to use and the number of samples (*shots*).
    *   For help, consult [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

```python linenums="1" title="my_circuit.py"
import pennylane as qml
from pennylane_calculquebec.API.client import CalculQuebecClient

my_client = CalculQuebecClient(host="https://monarq.calculquebec.ca", user="your username", access_token="your access token", project_id="your project_id")

dev = qml.device("monarq.default", client = my_client, wires = 3)
```

*   **Step 4: Create your circuit**
    *   In the same Python file, you can now code your quantum circuit.

```python linenums="1" title="my_circuit.py"
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
    *   The `sbatch` command is used to submit an [`sbatch`](https://slurm.schedmd.com/sbatch.html) job.

```bash
$ sbatch simple_job.sh
Submitted batch job 123456
```

    With a Slurm script resembling this:

```sh linenums="1" title="simple_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --account=def-someuser # Your username
#SBATCH --cpus-per-task=1      # Modify if applicable
#SBATCH --mem-per-cpu=1G 	  # Modify if applicable
python my_circuit.py
```

*   The circuit's result is written to a file whose name starts with `slurm-`, followed by the job ID and the `.out` suffix, for example, *slurm-123456.out*.
*   In this file, you will find the result of our circuit in a dictionary `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
*   For more information on how to submit jobs on Narval, see [Running Jobs](../running-jobs/running_jobs.md).

## Common Questions

*   [Frequently Asked Questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Other Tools

*   [Quantum Transpiler](quantum-transpiler.md)

## Applications

MonarQ is suitable for computations requiring small numbers of high-fidelity qubits, making it an ideal tool for the development and testing of quantum algorithms. Other possible applications include modeling small quantum systems; testing new quantum programming methods, error correction techniques; and more generally, fundamental research in quantum computing.

## Technical Support

If you have questions about our quantum services, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).
Sessions on quantum computing and programming with MonarQ are [listed here](https://www.eventbrite.com/o/calcul-quebec-8295332683).