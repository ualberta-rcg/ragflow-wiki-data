---
title: "Qiskit/en"
slug: "qiskit"
lang: "en"

source_wiki_title: "Qiskit/en"
source_hash: "11f3de977c1fb0e5d893fd6850b7ab13"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:41:40.397947+00:00"

tags:
  []

keywords:
  - "CalculQuebecClient"
  - "quantum computing"
  - "QuantumCircuit"
  - "SamplerV2"
  - "Python virtual environment"
  - "Qiskit"
  - "MonarQ backend"
  - "qiskit-calculquebec"
  - "Quantum circuit"
  - "Transpilation"
  - "Python"

questions:
  - "What is Qiskit and what are its primary functions in quantum computing?"
  - "What are the required steps to install Qiskit and submit a job using it on a cluster via Slurm?"
  - "How do you configure and initialize the MonarQ backend to run Qiskit circuits on the Calcul Québec infrastructure?"
  - "What are the necessary steps to transpile and execute a quantum circuit on the MonarQ backend?"
  - "Why is transpilation specifically required when using the MonarQ backend?"
  - "Which Qiskit execution class is recommended for running circuits with measurements, and what is the maximum number of shots allowed?"
  - "How do you initialize the MonarQ backend using the `qiskit_calculquebec` library?"
  - "What specific credentials and parameters are required to successfully create the `CalculQuebecClient`?"
  - "Which Python modules and classes must be imported to execute this quantum computing setup?"
  - "What are the necessary steps to transpile and execute a quantum circuit on the MonarQ backend?"
  - "Why is transpilation specifically required when using the MonarQ backend?"
  - "Which Qiskit execution class is recommended for running circuits with measurements, and what is the maximum number of shots allowed?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Developed in Python by IBM, [Qiskit](https://docs.quantum.ibm.com/) is an open-source quantum computing library. Like [PennyLane](pennylane.md) and [Snowflurry](snowflurry.md), it allows you to build, simulate, and run quantum circuits.

## Installation
1. Load the Qiskit dependencies.
```bash
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2
```

2. Create and activate a [Python virtual environment](../python.md#creating-and-using-a-virtual-environment).
```bash
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
```

3. Install a version of Qiskit.
```bash
pip install --no-index --upgrade pip
pip install --no-index qiskit==X.Y.Z qiskit_aer==X.Y.Z
```
where `X.Y.Z` is the version number, for example `1.4.0`. To install the most recent version available on our clusters, do not specify a number. Here, we only imported `qiskit` and `qiskit_aer`. You can add other Qiskit software with the syntax `qiskit_package==X.Y.Z` where `qiskit_package` is the software name, for example `qiskit-finance`. To see the wheels that are currently available, see [Available Python wheels](../../programming/available_python_wheels.md).

4. Validate the installation.
```bash
python -c 'import qiskit'
```

5. Freeze the environment and its dependencies.
```bash
pip freeze --local > ~/qiskit_requirements.txt
```

## Running Qiskit on a cluster

```sh title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser #Modify with your account name
#SBATCH --time=00:15:00        #Modify as needed
#SBATCH --cpus-per-task=1      #Modify as needed
#SBATCH --mem-per-cpu=1G       #Modify as needed

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2 

# Generate your virtual environment in $SLURM_TMPDIR.                                                                                                         
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Install Qiskit and its dependencies.                                                                                                                                                                                                                                                                                    
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/qiskit_requirements.txt

# Modify your Qiskit program.                                                                                                                                                                       
python qiskit_example.py
```
You can then [submit your job to the scheduler](../../running-jobs/running_jobs.md).

## Using Qiskit with MonarQ

You can use [MonarQ](../../clusters/monarq.md) directly with Qiskit via the qiskit-calculquebec plugin. This plugin allows you to develop and run Qiskit circuits on the Calcul Québec infrastructure.

### Install the dependencies

* Step 1: Install the dependencies
```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index qiskit-calculquebec
pip install --no-index qiskit-ibm-runtime
python -c "import qiskit; import qiskit_calculquebec"
```

!!! note
    **qiskit-calculquebec** installs Qiskit automatically.

### MonarQ backend initialisation

* Step 2: Set up your credentials and the backend
    * Create a client using your credentials. Your token is available via the Thunderhead portal.
    * The *host* is `https://monarq.calculquebec.ca`.
    * Then initialize the MonarQ backend.

```python title="qiskit_example.py"
import qiskit
from qiskit import QuantumCircuit
from qiskit_calculquebec.API.client import CalculQuebecClient
from qiskit_calculquebec.backends import MonarQBackend

# Credentials
user = "username"
access_token = "token"
host = "https://monarq.calculquebec.ca"
project_id = "project_id"

# Creating the client and the backend
my_client = CalculQuebecClient(host, user, access_token, project_id=project_id)
backend = MonarQBackend("monarq", my_client)

# Simple circuit example
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
```

### Running the circuit

* Step 3: Transpile and run the circuit

```python title="qiskit_example.py"
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Transpilation tailored to the backend
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
transpiled_qc = pm.run(qc)

# Execution
sampler = Sampler(mode=backend)
job = sampler.run([transpiled_qc], shots=1000)

result = job.result()
print(result[0].data.meas.get_counts())
```

### Notes

* Transpilation is required to adapt the circuit to MonarQ's native connectivity and ports.
* The number of *shots* can be adjusted as needed (maximum: 1024).
* The use of `SamplerV2` is recommended for running circuits with measures.