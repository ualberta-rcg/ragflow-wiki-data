---
title: "Qiskit/fr"
slug: "qiskit"
lang: "fr"

source_wiki_title: "Qiskit/fr"
source_hash: "9ec466c100c6048f10971cf490981512"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:42:02.373142+00:00"

tags:
  []

keywords:
  - "backend MonarQ"
  - "Qiskit"
  - "programmation quantique"
  - "MonarQ"
  - "identifiants"
  - "portail Thunderhead"
  - "environnement virtuel"
  - "Circuit quantique"
  - "qiskit-calculquebec"
  - "grappe"
  - "Calcul Québec"
  - "Transpilation"

questions:
  - "Qu'est-ce que la bibliothèque Qiskit et quelles sont ses principales fonctionnalités ?"
  - "Quelles sont les étapes nécessaires pour installer Qiskit dans un environnement virtuel et soumettre une tâche sur une grappe de calcul ?"
  - "Comment doit-on configurer Qiskit pour l'utiliser directement avec l'infrastructure quantique MonarQ de Calcul Québec ?"
  - "Comment configure-t-on le client et le backend pour se connecter à l'ordinateur quantique MonarQ avec Qiskit ?"
  - "Pourquoi l'étape de transpilation est-elle indispensable avant d'exécuter le circuit quantique sur le backend ?"
  - "Quelles sont les limites et recommandations spécifiées pour l'exécution du circuit, notamment concernant le nombre de tirs (shots) et l'outil d'échantillonnage ?"
  - "Quelle est la particularité de l'installation du paquet qiskit-calculquebec concernant Qiskit ?"
  - "Où l'utilisateur peut-il récupérer son jeton pour configurer ses identifiants ?"
  - "Quelle est l'adresse exacte de l'hôte (host) requise pour l'initialisation du backend MonarQ ?"
  - "Comment configure-t-on le client et le backend pour se connecter à l'ordinateur quantique MonarQ avec Qiskit ?"
  - "Pourquoi l'étape de transpilation est-elle indispensable avant d'exécuter le circuit quantique sur le backend ?"
  - "Quelles sont les limites et recommandations spécifiées pour l'exécution du circuit, notamment concernant le nombre de tirs (shots) et l'outil d'échantillonnage ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Qiskit](https://docs.quantum.ibm.com/) est une bibliothèque de programmation quantique à code source ouvert développée en Python par IBM. Comme [PennyLane](pennylane.md) et [Snowflurry](snowflurry.md), elle permet de construire, simuler et exécuter des circuits quantiques.

## Installation
1. Chargez les dépendances de Qiskit.
```bash
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2
```

2. Créez et activez un [environnement virtuel Python](../python.md#creer-et-utiliser-un-environnement-virtuel).
```bash
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
```

3. Installez une version spécifique de Qiskit.
```bash
pip install --no-index --upgrade pip
pip install --no-index qiskit==X.Y.Z qiskit_aer==X.Y.Z
```
où `X.Y.Z` représente le numéro de la version, par exemple `1.4.0`. Pour installer la plus récente version disponible sur nos grappes, n'indiquez pas de version. Ici, nous n'avons importé que `qiskit` et `qiskit_aer`. Vous pouvez ajouter d'autres logiciels Qiskit en fonction de vos besoins en suivant la structure `qiskit_package==X.Y.Z` où `qiskit_package` représente le logiciel voulu, par exemple `qiskit-finance`. Les *wheels* présentement disponibles sont listés sur la page [Wheels Python](../../programming/available_python_wheels.md).

4. Validez l’installation de Qiskit.
```bash
python -c 'import qiskit'
```

5. Gelez l'environnement et les dépendances.
```bash
pip freeze --local > ~/qiskit_requirements.txt
```

## Exécuter Qiskit sur une grappe
```bash title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser #indiquez le nom de votre compte
#SBATCH --time=00:15:00        #modifiez s'il y a lieu
#SBATCH --cpus-per-task=1      #modifiez s'il y a lieu
#SBATCH --mem-per-cpu=1G       #modifiez s'il y a lieu

# Chargez les dépendances des modules.
module load StdEnv/2023 gcc python/3.11 symengine/0.11.2

# Générez l'environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez Qiskit et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/qiskit_requirements.txt

# Modifiez le programme Qiskit.
python qiskit_example.py
```
Vous pouvez ensuite [soumettre votre tâche à l'ordonnanceur](../../running-jobs/running_jobs.md).

## Utiliser Qiskit avec MonarQ

Il est possible d’utiliser directement [MonarQ](../../clusters/monarq.md) avec Qiskit via le plugiciel qiskit-calculquebec. Ce plugiciel permet de développer et d'exécuter des circuits Qiskit sur l’infrastructure de Calcul Québec.

### Installation des dépendances

*   Étape 1 : Installer les dépendances
```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index qiskit-calculquebec
pip install --no-index qiskit-ibm-runtime
python -c "import qiskit; import qiskit_calculquebec"
```

!!! note
    **qiskit-calculquebec** installe automatiquement Qiskit.

### Initialisation du backend MonarQ

*   Étape 2 : Configurer vos identifiants et le backend
    *   Créez un client avec vos identifiants. Votre jeton est disponible via le portail Thunderhead.
    *   Le *host* est **https://monarq.calculquebec.ca**.
    *   Initialisez ensuite le backend MonarQ.

```python title="qiskit_example.py"
import qiskit
from qiskit import QuantumCircuit
from qiskit_calculquebec.API.client import CalculQuebecClient
from qiskit_calculquebec.backends import MonarQBackend

# Identifiants
user = "username"
access_token = "token"
host = "https://monarq.calculquebec.ca"
project_id = "project_id"

# Création du client et du backend
my_client = CalculQuebecClient(host, user, access_token, project_id=project_id)
backend = MonarQBackend("monarq", my_client)

# Circuit simple
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
```

### Exécution du circuit

*   Étape 3 : Transpiler et exécuter le circuit

```python title="qiskit_example.py"
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Transpilation adaptée au backend
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
transpiled_qc = pm.run(qc)

# Exécution
sampler = Sampler(mode=backend)
job = sampler.run([transpiled_qc], shots=1000)

result = job.result()
print(result[0].data.meas.get_counts())
```

### Notes

*   La transpilation est nécessaire pour adapter le circuit à la connectivité et aux portes natives de MonarQ.
*   Le nombre de *shots* peut être ajusté selon les besoins (maximum : 1024).
*   L’utilisation de **SamplerV2** est recommandée pour l’exécution de circuits avec mesures.