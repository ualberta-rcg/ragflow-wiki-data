---
title: "PennyLane/fr"
slug: "pennylane"
lang: "fr"

source_wiki_title: "PennyLane/fr"
source_hash: "e50eead13483a5548c406d6e782bb4de"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:22:12.485647+00:00"

tags:
  []

keywords:
  - "états de Bell"
  - "PennyLane"
  - "apprentissage automatique"
  - "version désirée"
  - "calcul quantique"
  - "circuits quantiques"
  - "MonarQ"
  - "environnement virtuel"
  - "pip install"
  - "pennylane"
  - "grappe"
  - "pennylane-reqs.txt"
  - "python"
  - "circuit quantique"

questions:
  - "Qu'est-ce que la plateforme PennyLane et quelles sont ses principales fonctionnalités dans le domaine du calcul quantique ?"
  - "Comment le plugiciel PennyLane-CalculQuebec permet-il d'exécuter des circuits quantiques sur le matériel MonarQ ?"
  - "Quelles sont les commandes requises pour créer un environnement virtuel Python et y installer PennyLane ?"
  - "Comment doit-on configurer le script SLURM pour préparer l'environnement et exécuter un programme PennyLane sur une grappe de calcul ?"
  - "Quelles portes quantiques et fonctions spécifiques de la bibliothèque PennyLane sont utilisées dans l'exemple pour générer et simuler un état de Bell ?"
  - "Quelles sont les ressources et références externes recommandées pour consulter la documentation officielle ou le code source du projet ?"
  - "Comment installer une version spécifique du paquet PennyLane en utilisant pip en ligne de commande ?"
  - "Quelle est la procédure pour utiliser un fichier de prérequis (pennylane-reqs.txt) afin d'automatiser l'installation ?"
  - "Quel module spécifique doit être chargé dans la session avant d'exécuter l'installation à partir du fichier texte ?"
  - "Comment doit-on configurer le script SLURM pour préparer l'environnement et exécuter un programme PennyLane sur une grappe de calcul ?"
  - "Quelles portes quantiques et fonctions spécifiques de la bibliothèque PennyLane sont utilisées dans l'exemple pour générer et simuler un état de Bell ?"
  - "Quelles sont les ressources et références externes recommandées pour consulter la documentation officielle ou le code source du projet ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[PennyLane](https://pennylane.ai/) est une plateforme logicielle à code source ouvert pour le calcul quantique différentiable dont [la première version a été publiée sur Github](https://github.com/calculquebec/pennylane-snowflurry) en 2018. Développée à Toronto par Xanadu, PennyLane permet de concevoir des circuits quantiques et de les exécuter sur divers simulateurs et matériels quantiques. La plateforme est conçue pour faciliter la simulation, l'optimisation et l’apprentissage d’algorithmes quantiques hybrides qui combinent des traitements classiques et quantiques.

## Fonctionnalités
PennyLane offre plusieurs fonctionnalités pour faciliter la recherche et le développement dans le domaine de l'informatique quantique différentiable.

### Interface quantique unifiée
PennyLane fournit une interface unifiée qui permet de concevoir des circuits quantiques et de les exécuter sur différents simulateurs et matériels quantiques. La plateforme prend en charge plusieurs simulateurs quantiques populaires, tels que [Qiskit](qiskit.md), [Cirq](cirq.md), Strawberry Field ou encore QuTip. PennyLane prend également en charge plusieurs matériels quantiques, notamment les dispositifs quantiques de Xanadu, IBM, Rigetti et IonQ.

Calcul Québec a développé le plugiciel [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) qui utilise l’interface PennyLane pour concevoir et exécuter des circuits quantiques sur [MonarQ](../../clusters/monarq.md).

### Intégration avec des bibliothèques d'apprentissage automatique
PennyLane s'intègre de manière transparente avec des librairies d'apprentissage automatique populaires telles que [TensorFlow](../tensorflow.md) et [PyTorch](../pytorch.md), et vous permet d'utiliser les outils d'apprentissage automatique pour construire des modèles d'apprentissage automatique quantiques hybrides et optimiser les circuits quantiques.

### Optimisation de circuits quantiques
En utilisant des techniques d'optimisation différentiables et en combinant les méthodes de différenciation classiques et quantiques, PennyLane optimise les paramètres des circuits quantiques afin de résoudre des problèmes variés.

### Outils de visualisation
PennyLane fournit des outils de visualisation pour faciliter la compréhension du fonctionnement des circuits quantiques.

### Communauté et développement
PennyLane est un projet à code source ouvert avec une communauté active de développeurs et d'utilisateurs. Le projet est constamment mis à jour avec de nouvelles fonctionnalités et améliorations, et tous peuvent contribuer au développement de la plateforme.

## Utiliser PennyLane avec MonarQ
[MonarQ](../../clusters/monarq.md) est conçu pour être programmé avec Snowflurry, une bibliothèque logicielle programmée en Julia et développée par Anyon Systems. Par contre, grâce au plugiciel PennyLane-CalculQuebec, les circuits PennyLane peuvent être créés en utilisant Snowflurry en arrière-plan. Cela permet d’exécuter des circuits sur [MonarQ](../../clusters/monarq.md) tout en bénéficiant des fonctionnalités et de l'environnement de développement offerts par PennyLane. Voir la documentation [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry) pour les guides d’installation et d’usage.

Un [transpileur quantique](transpileur_quantique.md) est également disponible à partir de PennyLane afin d'optimiser ses circuits pour [MonarQ](../../clusters/monarq.md).

## Création de l'environnement virtuel
[Créons un environnement virtuel Python](../python.md#creer-et-utiliser-un-environnement-virtuel) pour utiliser PennyLane.

```bash
module load python/3.11
virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index pennylane==X.Y.Z
python -c "import pennylane"
```
où `X.Y.Z` est la version désirée.

Vous pouvez également inscrire les trois dernières commandes ci-dessus dans un fichier `pennylane-reqs.txt` et appeler le fichier à l'intérieur d'une session avec les commandes :
```bash
module load python/3.11
pip install --no-index -r pennylane-reqs.txt
```

## Exécuter PennyLane sur une grappe
```sh title="script.sh"
#!/bin/bash
#SBATCH --account=def-someuser # Indiquez le nom de votre compte
#SBATCH --time=00:15:00        # Modifiez s'il y a lieu
#SBATCH --cpus-per-task=1      # Modifiez s'il y a lieu
#SBATCH --mem-per-cpu=1G       # Modifiez s'il y a lieu

# Chargez les dépendances des modules.
module load StdEnv/2023 gcc python/3.11

# Générez l'environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez Pennylane et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/pennylane_requirements.txt

# Modifiez votre programme PennyLane.
python pennylane_example.py
```
Vous pouvez ensuite soumettre votre tâche à [l'ordonnanceur](../../running-jobs/running_jobs.md).

## Exemple d’utilisation : États de Bell
Commençons par créer l'environnement virtuel, tel que décrit ci-dessus.

Nous allons ensuite générer le premier état de Bell en utilisant PennyLane.
```python
import pennylane as qml

# Définir le circuit quantique pour générer le premier état de Bell
def bell_circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

# Définir le simulateur de circuit quantique
dev = qml.device('default.qubit', wires=2)

# Définir le circuit quantique comme fonction QNode
@qml.qnode(dev)
def generate_bell_state():
    bell_circuit()
    return qml.state()

# Générer et afficher le premier état de Bell
bell_state_0 = generate_bell_state()
print("Premier état de Bell :", bell_state_0)
```
```text
Premier état de Bell :[0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

## Références
* [Site officiel de PennyLane](https://pennylane.ai)
* [Documentation de PennyLane sur GitHub](https://github.com/PennyLaneAI/pennylane)
* [PennyLane-CalculQuebec](https://github.com/calculquebec/pennylane-snowflurry)