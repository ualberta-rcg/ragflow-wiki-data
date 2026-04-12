---
title: "CirQ/fr"
slug: "cirq"
lang: "fr"

source_wiki_title: "CirQ/fr"
source_hash: "1deb60a5762056fdec89483da0eba46b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:16:27.945778+00:00"

tags:
  []

keywords:
  - "états de Bell"
  - "simulations"
  - "CirQ"
  - "porte CNOT"
  - "état de Bell"
  - "porte de Hadamard"
  - "informatique quantique"
  - "matplotlib"
  - "Python"
  - "intrication"
  - "cirq"
  - "diagramme"
  - "circuit quantique"

questions:
  - "Qu'est-ce que la bibliothèque CirQ et quelles sont ses principales fonctionnalités dans le domaine de l'informatique quantique ?"
  - "Quelles sont les étapes requises pour installer et exécuter CirQ sur une grappe de calcul à l'aide d'un environnement virtuel et d'un script de tâche ?"
  - "Comment le code d'exemple utilise-t-il les portes quantiques dans CirQ pour construire et simuler un état de Bell ?"
  - "Quelle bibliothèque Python est utilisée pour simuler le circuit quantique et générer l'histogramme ?"
  - "Combien de répétitions sont exécutées lors de cette simulation ?"
  - "Quel état quantique spécifique est simulé et illustré par le diagramme résultant ?"
  - "Quel est le rôle respectif de la porte de Hadamard et de la porte CNOT dans la création d'un état de Bell ?"
  - "De quels états spécifiques l'état de Bell obtenu est-il une superposition égale ?"
  - "Quel logiciel permet de simuler ce circuit et comment l'état |11⟩ est-il représenté dans ses résultats ?"
  - "Quelle bibliothèque Python est utilisée pour simuler le circuit quantique et générer l'histogramme ?"
  - "Combien de répétitions sont exécutées lors de cette simulation ?"
  - "Quel état quantique spécifique est simulé et illustré par le diagramme résultant ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

CirQ est une bibliothèque d'informatique quantique à code source ouvert développée en [Python](python.md) par Google, qui permet de construire, optimiser, simuler et exécuter des circuits quantiques. Plus particulièrement, CirQ permet de simuler des circuits sur des configurations spécifiques de qubits, ce qui peut optimiser un circuit pour une certaine architecture de qubits. L'information sur les fonctionnalités de la bibliothèque est disponible dans la [documentation](https://quantumai.google/cirq) et sur le [GitHub](https://github.com/quantumlib/Cirq) de CirQ. Tout comme [Snowflurry](snowflurry.md), CirQ peut être utilisée pour exécuter des circuits quantiques sur l'ordinateur quantique [MonarQ](monarq.md).

## Installation
Le simulateur d'ordinateur quantique CirQ est disponible sur toutes nos grappes. Le langage de programmation [Python](python.md) doit être chargé avant d'y avoir accès. Il est préférable de travailler dans un [environnement virtuel Python](python.md#créer-et-utiliser-un-environnement-virtuel).

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index cirq==1.4.1
python -c "import cirq"
pip freeze > cirq-1.4.1-reqs.txt
```

La dernière commande crée un fichier nommé `cirq-1.4.1-reqs.txt`, que vous pouvez réutiliser dans un script de tâche, tel que décrit ci-dessous.

## Exécution sur une grappe

```sh linenums="1" title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # indiquez le nom de votre compte
#SBATCH --time=00:15:00        # modifiez s'il y a lieu
#SBATCH --cpus-per-task=1      # modifiez s'il y a lieu
#SBATCH --mem-per-cpu=1G       # modifiez s'il y a lieu

# Chargez les dépendances des modules.
module load StdEnv/2023 gcc python/3.11 

# Générez l'environnement virtuel dans $SLURM_TMPDIR.                                                                                             
virtualenv --no-download ${SLURM_TMPDIR}/env                                                                                                                   
source ${SLURM_TMPDIR}/env/bin/activate  

# Installez CirQ et ses dépendances.                                                                                                                                                                                                                                                                                   
pip install --no-index --upgrade pip                                                                                                                            
pip install --no-index --requirement ~/cirq-1.4.1-reqs.txt

# Modifiez le programme CirQ.                                                                                                                                                             
python cirq_example.py
```

Vous pouvez ensuite [soumettre votre tâche à l'ordonnanceur](running-jobs.md).

## Exemple d'utilisation : États de Bell
Les états de Bell sont les états les plus simples qui permettent d'expliquer à la fois la superposition et l'intrication sur des qubits.
La bibliothèque [CirQ](https://github.com/quantumlib/Cirq) permet de construire un état de Bell comme ceci :

```python
import cirq
from cirq.contrib.svg import SVGCircuit
from cirq import H, CNOT

qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(H.on(qubits[0]),CNOT.on(qubits[0],qubits[1]))
circuit.append(cirq.measure(qubits, key='m'))
SVGCircuit(circuit)
```

Ce code construit et affiche un circuit qui prépare un état de Bell. La porte H (porte de Hadamard) crée une superposition égale de |0⟩ et |1⟩ sur le premier qubit tandis que la porte CNOT (porte X contrôlée) crée une intrication entre les deux qubits. Cet état de Bell est donc une superposition égale des états |00⟩ et |11⟩. La simulation de ce circuit à l'aide de CirQ permet de visualiser les résultats. Dans ce diagramme, le nombre entier 3 représente l'état |11⟩ puisque 3 s'écrit 11 en binaire.

```python
import matplotlib.pyplot as plt
s = cirq.Simulator().run(circuit, repetitions=1000)
counts = s.histogram(key='m')
cirq.plot_state_histogram(counts, plt.subplot())