---
title: "Qiskit"
slug: "qiskit"
lang: "base"

source_wiki_title: "Qiskit"
source_hash: "ba7dcfe42bd7fed1f5809f66ba98b5df"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:51:42.813152+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

[Qiskit](https://docs.quantum.ibm.com/) is an open-source quantum programming library developed in Python by IBM. Like [PennyLane](pennylane.md) and [Snowflurry](snowflurry.md), it allows you to build, simulate, and execute quantum circuits.

## Installation
1. Load Qiskit's dependencies.
    ```bash
    module load StdEnv/2023 gcc python/3.11 symengine/0.11.2
    ```

2. Create and activate a [Python virtual environment](../python.md).
    ```bash
    virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
    ```

3. Install a specific version of Qiskit.
    ```bash
    # (ENV) [name@server ~]
    pip install --no-index --upgrade pip
    pip install --no-index qiskit==X.Y.Z qiskit_aer==X.Y.Z
    ```
    where `X.Y.Z` represents the version number, for example `1.4.0`. To install the latest version available on our clusters, do not specify a version. Here, we have only imported `qiskit` and `qiskit_aer`. You can add other Qiskit software depending on your needs by following the `qiskit_package==X.Y.Z` structure, where `qiskit_package` represents the desired software, for example `qiskit-finance`. The wheels currently available are listed on the [Python Wheels](../../programming/available_python_wheels.md) page.

4. Validate the Qiskit installation.
    ```bash
    # (ENV) [name@server ~]
    python -c 'import qiskit'
    ```

5. Freeze the environment and dependencies.
    ```bash
    # (ENV) [name@server ~]
    pip freeze --local > ~/qiskit_requirements.txt
    ```

## Run Qiskit on a Cluster
```sh title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # specify your account name
#SBATCH --time=00:15:00        # modify if necessary
#SBATCH --cpus-per-task=1      # modify if necessary
#SBATCH --mem-per-cpu=1G       # modify if necessary

# Load module dependencies.
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2 

# Generate the virtual environment in $SLURM_TMPDIR.                                                                                                         
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Install Qiskit and its dependencies.                                                                                                                                                                                                                                                                                    
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/qiskit_requirements.txt

# Modify the Qiskit program.                                                                                                                                                                       
python qiskit_example.py
```
You can then [submit your job to the scheduler](../../running-jobs/running_jobs.md).

## Use Qiskit with MonarQ
It is possible to use [MonarQ](../../clusters/monarq.md) directly with Qiskit via the `qiskit-calculquebec` plugin. This plugin allows you to develop and execute Qiskit circuits on Calcul Québec's infrastructure.

### Install Dependencies
* Step 1: Install dependencies
    ```bash
    module load python/3.11
    virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
    pip install --no-index --upgrade pip
    pip install --no-index qiskit-calculquebec
    pip install --no-index qiskit-ibm-runtime
    python -c "import qiskit; import qiskit_calculquebec"
    ```

* Note: **qiskit-calculquebec** automatically installs Qiskit.

### Initialize MonarQ Backend and Execute Circuit
* Step 2: Configure your credentials and the backend
    * Create a client with your credentials. Your token is available via the Thunderhead portal.
    * The *host* is `https://monarq.calculquebec.ca`.
    * Then, initialize the MonarQ backend.

* Step 3: Transpile and execute the circuit

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

# Client and backend creation
my_client = CalculQuebecClient(host, user, access_token, project_id=project_id)
backend = MonarQBackend("monarq", my_client)

# Simple circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Backend-adapted transpilation
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
transpiled_qc = pm.run(qc)

# Execution
sampler = Sampler(mode=backend)
job = sampler.run([transpiled_qc], shots=1000)

result = job.result()
print(result[0].data.meas.get_counts())
```

### Notes
* Transpilation is necessary to adapt the circuit to MonarQ's connectivity and native gates.
* The number of *shots* can be adjusted as needed (maximum: 1024).
* The use of **SamplerV2** is recommended for executing circuits with measurements.