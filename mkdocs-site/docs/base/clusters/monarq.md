---
title: "MonarQ"
slug: "monarq"
lang: "base"

source_wiki_title: "MonarQ"
source_hash: "c9f71b39a8a3a6a6028b705c0f3aea5d"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:47:23.687483+00:00"

tags:
  []

keywords:
  - "Narval"
  - "account=def-someuser"
  - "ordinateur quantique supraconducteur à 24 qubits"
  - "résultat du circuit"
  - "#SBATCH"
  - "environnement de développement PennyLane"
  - "plugiciel PennyLane-CalculQuébec"
  - "sbatch"
  - "dictionnaire"
  - "environnement virtuel Python"
  - "qubits de haute fidélité"
  - "bibliothèques Snowflurry et PennyLane"
  - "PennyLane-CalculQuébec"
  - "circuits quantiques"
  - "Snowflurry"
  - "portail Thunderhead pour métriques"
  - "support technique"
  - "time=00:15:00"
  - "slurm-<ID>.out"
  - "MonarQ"
  - "8 % et durée 32 ns"
  - "cpus-per-task=1"
  - "fidélité de porte 99"

questions:
  - "Quelles sont les principales spécifications techniques de l’ordinateur quantique MonarQ (nombre de qubits, fidélité des portes, temps de cohérence, profondeur maximale des circuits) ?"
  - "Quelles sont les étapes et les conditions requises pour obtenir un accès à MonarQ, depuis la soumission du formulaire jusqu’à la réception du jeton d’accès ?"
  - "Quelles bibliothèques logicielles sont prises en charge par MonarQ et comment peuvent‑elles être utilisées pour développer et exécuter des circuits quantiques sur cette plateforme ?"
  - "Quels sont les prérequis nécessaires pour commencer à utiliser MonarQ ?"
  - "Comment configure‑t‑on les identifiants et le dispositif (device) PennyLane afin d’exécuter un circuit sur MonarQ ?"
  - "Quelle est la procédure pour soumettre et lancer un circuit quantique sur MonarQ à l’aide du planificateur Slurm ?"
  - "Quelle est la relation entre MonarQ et Snowflurry mentionnée dans le texte ?"
  - "Quel rôle joue le plugiciel développé par Calcul Québec pour l’utilisation de MonarQ avec PennyLane ?"
  - "En quel langage le code du projet MonarQ est‑il écrit, selon le texte ?"
  - "Quels paramètres SLURM sont spécifiés dans le script `simple_job.sh` et quelle est leur fonction ?"
  - "Comment le script lance‑t‑il le programme Python `my_circuit.py` ?"
  - "De quelle manière le fichier de sortie SLURM est‑il nommé et que contient‑il généralement ?"
  - "Que représente le dictionnaire {'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504} affiché dans le fichier ?"
  - "Comment soumettre une tâche sur le supercalculateur Narval en utilisant MonarQ ?"
  - "Quelles sont les principales applications et les types de calculs pour lesquels MonarQ est recommandé ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "Connection Node"
    Connection node: `https://manager.anyonlabs.com`

MonarQ is a 24-qubit superconducting quantum computer developed in Montréal by [Anyon Systems](https://anyonsys.com/) and located at the [École de technologie supérieure](http://www.etsmtl.ca/). For more information on MonarQ's specifications and performance, see the [Technical Specifications](#technical-specifications) section below.

The name MonarQ is inspired by the shape of the qubit circuit on the quantum processor, which resembles a monarch butterfly, a symbol of evolution and migration. The capital 'Q' highlights the quantum nature of the computer and its Québec origin. MonarQ's acquisition was made possible through the support of the [Ministère de l'Économie, de l'Innovation et de l'Énergie du Québec (MEIE)](https://www.economie.gouv.qc.ca/) and [Canada Economic Development (DEC)](https://dec.canada.ca/).

## Accessing MonarQ

1.  To begin the process of accessing MonarQ, [complete this form](https://forms.gle/zH1a3oB4SGvSjAwh7). It must be completed by the principal investigator.
2.  You must [have an Alliance account](https://alliancecan.ca/en/services/advanced-research-computing/research-portal/account-management/apply-for-an-account) to access MonarQ.
3.  Meet with our team to discuss the specifics of your project, access, and billing details.
4.  Receive access to the MonarQ dashboard and generate your access token.
5.  To get started, see the [Getting Started with MonarQ](#getting-started-with-monarq) section below.

Contact our quantum team at [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca) if you have any questions or would like a more general discussion before requesting access.

## Technical Specifications

Like quantum processors available today, MonarQ operates in an environment where noise remains a significant factor. Performance metrics, updated with each calibration, are accessible via the Thunderhead portal. Access to this portal requires MonarQ access approval.

Among other things, the following metrics are available:

*   24-qubit quantum processor
*   Single-qubit gate fidelity of 99.8% and duration of 32 ns
*   Two-qubit gate fidelity of 96% and duration of 90 ns
*   Coherence time of 4-10 μs (depending on the state)
*   Maximum circuit depth of approximately 350 for single-qubit gates and 115 for two-qubit gates

## Quantum Computing Software

Several specialized software libraries exist for quantum computing and developing quantum algorithms. These libraries allow for building circuits that are executed on simulators, imitating the performance and results obtained on a quantum computer like MonarQ. They can be used on all Alliance clusters.

*   [PennyLane](../software/quantum/pennylane.md), a Python command library
*   [Snowflurry](../software/quantum/snowflurry.md), a Julia command library
*   [Qiskit](../software/quantum/qiskit.md), a Python command library

MonarQ's quantum logic gates are called through the [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) software library, written in [Julia](https://julialang.org/). Although MonarQ is natively compatible with Snowflurry, a [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin, developed by Calcul Québec, allows for executing circuits on MonarQ while benefiting from the functionalities and development environment offered by [PennyLane](../software/quantum/pennylane.md).

## Getting Started with MonarQ
**Prerequisites**: Ensure you have MonarQ access and your login credentials (*username*, *API token*). For any questions, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).

*   **Step 1: Connect to [Narval](narval.md)**
    *   MonarQ is accessible from Narval, a Calcul Québec cluster. Access to Narval is via the login node **narval.alliancecan.ca**.
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
    *   Open a Python .py file and import the necessary dependencies, namely PennyLane and CalculQuebecClient, as shown in the example below.
    *   Create a client with your credentials. Your token is available from the Thunderhead portal. The *host* is `https://manager.anyonlabs.com`
    *   Create a PennyLane *device* with your client. You can also specify the number of qubits (*wires*) to use and the number of samples (*shots*).
    *   For help, consult [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

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
    *   The `sbatch` command is used to submit a job [sbatch](https://slurm.schedmd.com/sbatch.html).

    ```bash
    $ sbatch simple_job.sh
    Submitted batch job 123456
    ```

    With a Slurm script resembling this:

    ```sh title="simple_job.sh"
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --account=def-someuser # Your username
    #SBATCH --cpus-per-task=1      # Modify if necessary
    #SBATCH --mem-per-cpu=1G 	  # Modify if necessary
    python my_circuit.py 
    ```
    *   The circuit's output is written to a file whose name starts with `slurm-`, followed by the job ID and the `.out` suffix, for example, *slurm-123456.out*.
    *   This file contains the circuit's output in a dictionary: `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
    *   For more information on how to submit jobs on Narval, see [Running Jobs](../running-jobs/running_jobs.md).

## Frequently Asked Questions

*   [Frequently Asked Questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Other Tools

*   [Quantum Transpiler](../software/quantum/transpileur_quantique.md)

## Applications

MonarQ is suitable for calculations requiring small numbers of high-fidelity qubits, making it an ideal tool for developing and testing quantum algorithms. Other possible applications include modelling small quantum systems; testing new quantum programming methods and error correction techniques; and, more generally, fundamental research in quantum computing.

## Technical Support

If you have questions about our quantum services, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).
Sessions on quantum computing and programming with MonarQ are [listed here](https://www.eventbrite.com/o/calcul-quebec-8295332683).