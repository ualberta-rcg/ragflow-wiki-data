---
title: "Snowflurry/fr"
slug: "snowflurry"
lang: "fr"

source_wiki_title: "Snowflurry/fr"
source_hash: "c0c815c14cbda674fe57ed2aca668941"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:32:32.556074+00:00"

tags:
  []

keywords:
  - "états de Bell"
  - "Julia"
  - "porte CNOT"
  - "circuits quantiques"
  - "porte de Hadamard"
  - "SnowflurryPlots"
  - "état de Bell"
  - "readout"
  - "superposition"
  - "informatique quantique"
  - "Snowflurry"
  - "mesure"
  - "intrication"
  - "plot_histogram"
  - "qubits"

questions:
  - "Qu'est-ce que la bibliothèque Snowflurry et quelles sont ses principales fonctionnalités dans le domaine de l'informatique quantique ?"
  - "Comment procéder à l'installation et au chargement de Snowflurry et de son outil de visualisation dans un environnement de programmation Julia ?"
  - "De quelle manière le code fourni en exemple utilise-t-il les portes quantiques pour construire et simuler un état de Bell ?"
  - "Quelle opération permet de spécifier quels qubits doivent être mesurés dans le circuit ?"
  - "Quelle bibliothèque et quelle fonction sont utilisées pour visualiser les résultats des mesures ?"
  - "Que représente le graphique généré par la simulation dans l'exemple fourni ?"
  - "Quel est le rôle de la porte de Hadamard sur le premier qubit ?"
  - "Quel état quantique final est obtenu après l'application de la porte CNOT ?"
  - "À quoi sert la fonction simulate dans ce contexte ?"
  - "Quelle opération permet de spécifier quels qubits doivent être mesurés dans le circuit ?"
  - "Quelle bibliothèque et quelle fonction sont utilisées pour visualiser les résultats des mesures ?"
  - "Que représente le graphique généré par la simulation dans l'exemple fourni ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) est une bibliothèque d'informatique quantique à code source ouvert développée en [Julia](julia.md) par [Anyon Systèmes](https://anyonsys.com/fr) qui permet de construire, de simuler et d'exécuter des circuits quantiques.
Une bibliothèque connexe nommée [SnowflurryPlots](https://github.com/SnowflurrySDK/SnowflurryPlots.jl/) permet de visualiser les résultats de la simulation dans un diagramme à bandes. Pratique pour explorer l'informatique quantique, les fonctionnalités sont disponibles dans la [documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/index.html) et le guide d'installation est disponible sur la page [GitHub](https://github.com/SnowflurrySDK/Snowflurry.jl). Tout comme la bibliothèque [PennyLane](pennylane.md), Snowflurry peut être utilisée pour exécuter des circuits quantiques sur l'ordinateur quantique [MonarQ](monarq.md).

## Installation
Le simulateur d'ordinateur quantique avec [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) est disponible sur toutes nos grappes. Le langage de programmation [Julia](https://julialang.org/) doit être chargé avant d'avoir accès à Snowflurry avec la commande :

```bash
module load julia
```

Ensuite, l'interface de programmation Julia est appelée et la bibliothèque quantique Snowflurry est chargée (environ 5 à 10 minutes) avec les commandes :

```julia
import Pkg
Pkg.add(url="https://github.com/SnowflurrySDK/Snowflurry.jl", rev="main")
Pkg.add(url="https://github.com/SnowflurrySDK/SnowflurryPlots.jl", rev="main")
using Snowflurry
```

Les portes logiques quantiques et les commandes sont décrites dans la [documentation de Snowflurry](https://snowflurrysdk.github.io/Snowflurry.jl/dev/).

## Exemple d'utilisation : États de Bell
Les états de Bell sont des états à deux qubits maximalement intriqués. Deux exemples simples de phénomènes quantiques sont la superposition et l'intrication. La bibliothèque [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) permet de construire le premier état de Bell comme suit :

```julia
using Snowflurry
circuit=QuantumCircuit(qubit_count=2);
push!(circuit,hadamard(1));
push!(circuit,control_x(1,2));
print(circuit)

# Expected output:
# Quantum Circuit Object:
#    qubit_count: 2
# q[1]:──H────*──
#             ¦
# q[2]:───────X──
```

Dans la section de code ci-dessus, la porte de Hadamard crée une superposition égale de `|0⟩` et `|1⟩` sur le premier qubit tandis que la porte CNOT (porte X contrôllée) crée une intrication entre les deux qubits. On retrouve une superposition égale des états `|00⟩` et `|11⟩`, soit le premier état de Bell. La fonction `simulate` permet de simuler l'état exact du système.

```julia
state = simulate(circuit)
print(state)

# Expected output:
# 4-element Ket{ComplexF64}:
# 0.7071067811865475 + 0.0im
# 0.0 + 0.0im
# 0.0 + 0.0im
# 0.7071067811865475 + 0.0im
```

Pour effectuer une mesure, l'opération `readout` permet de spécifier quels qubits seront mesurés. La fonction `plot_histogram` de la bibliothèque SnowflurryPlots permet de visualiser les résultats.

```julia
using SnowflurryPlots
push!(circuit, readout(1,1), readout(2,2))
plot_histogram(circuit,1000)