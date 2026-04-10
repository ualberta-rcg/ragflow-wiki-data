---
title: "MonarQ/en-ca"
slug: "monarq_en-ca"
lang: "base"

source_wiki_title: "MonarQ/en-ca"
source_hash: "aeb0bb0aa150443c2cfc2b10420e487c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:55:51.340571+00:00"

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

**Connection node:** https://monarq.calculquebec.ca

!!! warning
    MonarQ is currently undergoing maintenance and is expected to be operational in February 2026. In the meantime, Calcul Québec can offer access to a similar but smaller machine with 6 qubits.

MonarQ is a 24-qubit superconducting quantum computer developed in Montreal by [Anyon Systems](https://anyonsys.com/) and located at the [École de technologie supérieure](http://www.etsmtl.ca/). For more information on MonarQ's specifications and performance, see [Technical Specifications](#technical-specifications) below.

## Accessing MonarQ

1.  To begin the MonarQ access process, [fill out this form](https://forms.gle/zH1a3oB4SGvSjAwh7). It must be completed by the principal investigator.
2.  You must [have an Alliance account](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/gestion-de-compte/demander-un-compte) to access MonarQ.
3.  Meet our team to discuss your project specifics, access, and billing details.
4.  Receive access to the MonarQ dashboard and generate your access token.
5.  To get started, see [Getting Started on MonarQ](#getting-started-on-monarq) below.

Contact our quantum team at [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca) if you have any questions or would like a more general discussion before requesting access.

## Technical Specifications

Similar to quantum processors available today, MonarQ operates in an environment where noise remains a significant factor. Performance metrics, updated with each calibration, are accessible via the Thunderhead portal. Access to this portal requires MonarQ access approval.

Among others, the following metrics are available:

*   24-qubit quantum processor
*   One-qubit gate with 99.8% fidelity and 32ns duration
*   Two-qubit gate with 96% fidelity and 90ns duration
*   Coherence time of 4-10μs (state-dependent)
*   Maximum circuit depth of approximately 350 for one-qubit gates and 115 for two-qubit gates

## Quantum Computing Software

Several specialized software libraries exist for quantum computing and for developing quantum algorithms. These libraries allow for building circuits that are executed on simulators which mimic the performance and results obtained on a quantum computer like MonarQ. They can be used on all Alliance clusters.

*   [PennyLane](pennylane.md), Python command library
*   [Snowflurry](snowflurry.md), Julia command library
*   [Qiskit](qiskit.md), Python command library

MonarQ's quantum logic gates are called via a software library, [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl), written in [Julia](https://julialang.org/). Although MonarQ is natively compatible with Snowflurry, there is a [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) plugin developed by Calcul Québec that allows circuits to be executed on MonarQ while benefiting from the features and development environment offered by [PennyLane](https://docs.alliancecan.ca/wiki/PennyLane).

## Getting Started on MonarQ

!!! tip "Prerequisites"
    Ensure you have MonarQ access and your login credentials (*username*, *API token*). For any questions, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).

*   **Step 1: Connect to [Narval](narval.md)**
    *   MonarQ is only accessible from Narval, a Calcul Québec cluster. Access to Narval is via the login node **narval.alliancecan.ca**.
    *   For help connecting to Narval, consult the [SSH](ssh.md) page.

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
    *   Open a Python `.py` file and import the necessary dependencies, namely PennyLane and CalculQuebecClient, as shown in the example below.
    *   Create a client with your credentials. Your token is available from the Thunderhead portal. The *host* is **https://monarq.calculquebec.ca**.
    *   Create a PennyLane *device* with your client. You can also specify the number of qubits (*wires*) to use and the number of samples (*shots*).
    *   For assistance, consult [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

    ::: python {data-title="my_circuit.py"}
    import pennylane as qml
    from pennylane_calculquebec.API.client import CalculQuebecClient

    my_client = CalculQuebecClient(host="https://monarq.calculquebec.ca", user="your username", access_token="your access token", project_id="your project_id")

    dev = qml.device("monarq.default", client = my_client, wires = 3)
    :::

*   **Step 4: Create your circuit**
    *   In the same Python file, you can now code your quantum circuit.

    ::: python {data-title="my_circuit.py"}
    @qml.set_shots(1000)
    @qml.qnode(dev)

    def bell_circuit():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])

        return qml.counts()

    result = bell_circuit()
    print(result)
    :::

*   **Step 5: Execute your circuit from the scheduler**
    *   The `sbatch` command is used to submit a job ([`sbatch`](https://slurm.schedmd.com/sbatch.html)).

    ```bash
    $ sbatch simple_job.sh
    Submitted batch job 123456
    ```

    With a Slurm script resembling this:

    ::: sh {data-title="simple_job.sh"}
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --account=def-someuser # Your username
    #SBATCH --cpus-per-task=1      # Modify if applicable
    #SBATCH --mem-per-cpu=1G       # Modify if applicable
    python my_circuit.py
    :::

    *   The circuit's result is written to a file whose name begins with `slurm-`, followed by the job ID and the `.out` suffix, for example *slurm-123456.out*.
    *   In this file, you will find the result of our circuit in a dictionary `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
    *   For more information on how to submit jobs on Narval, see [Run jobs](running_jobs.md).

## Common Questions

*   [Frequently Asked Questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Other Tools

*   [Quantum Transpiler](quantum_transpiler.md)

## Applications

MonarQ is suited for calculations requiring small numbers of high-fidelity qubits, making it an ideal tool for the development and testing of quantum algorithms. Other possible applications include the modeling of small quantum systems; testing new quantum programming methods and techniques, and error correction; and more generally, fundamental research in quantum computing.

## Technical Support

If you have questions about our quantum services, write to [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).
Sessions on quantum computing and programming with MonarQ are [listed here](https://www.eventbrite.com/o/calcul-quebec-8295332683).