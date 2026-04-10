---
title: "Snowflurry/fr"
slug: "snowflurry"
lang: "fr"

source_wiki_title: "Snowflurry/fr"
source_hash: "c0c815c14cbda674fe57ed2aca668941"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:22:21.383956+00:00"

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

[Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) est une bibliothèque d'informatique quantique à code source ouvert développée en [Julia](julia.md) par [Anyon Systèmes](https://anyonsys.com/fr) qui permet de construire, de simuler et d'exécuter des circuits quantiques.
Une bibliothèque connexe nommée [SnowflurryPlots](https://github.com/SnowflurrySDK/SnowflurryPlots.jl/) permet de visualiser les résultats de la simulation dans un diagramme à bandes. Pratique pour explorer l'informatique quantique, les fonctionnalités sont disponibles dans la [documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/index.html) et le guide d'installation est disponible sur la page [GitHub](https://github.com/SnowflurrySDK/Snowflurry.jl). Tout comme la bibliothèque [PennyLane](pennylane.md), Snowflurry peut être utilisée pour exécuter des circuits quantiques sur l'ordinateur quantique [MonarQ](monarq.md).

## Installation
Le simulateur d'ordinateur quantique avec [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) est disponible sur toutes nos grappes. Le langage de programmation [Julia](https://julialang.org/) doit être chargé avant d'avoir accès à Snowflurry avec la commande suivante :

```bash
module load julia
```

Ensuite, l'interface de programmation Julia est appelée, puis la bibliothèque quantique de Snowflurry chargée avec les commandes suivantes :

!!! note "Temps de chargement"
    L'installation initiale de la bibliothèque peut prendre environ 5 à 10 minutes.

```julia
julia
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
```

```text
Quantum Circuit Object:
   qubit_count: 2
q[1]:──H────*──
            ¦
q[2]:───────X──
```

Dans la section de code ci-dessus, la porte de Hadamard crée une superposition égale de |0⟩ et |1⟩ sur le premier qubit tandis que la porte CNOT (porte X contrôlée) crée une intrication entre les deux qubits. On retrouve une superposition égale des états |00⟩ et |11⟩, soit le premier état de Bell. La fonction `simulate` permet de simuler l'état exact du système.

```julia
state = simulate(circuit)
print(state)
```

```text
4-element Ket{ComplexF64}:
0.7071067811865475 + 0.0im
0.0 + 0.0im
0.0 + 0.0im
0.7071067811865475 + 0.0im
```

Pour prendre une mesure, l'opération `readout` permet de spécifier quels qubits seront mesurés. La fonction `plot_histogram` de la bibliothèque SnowflurryPlots permet de visualiser les résultats.

```julia
using SnowflurryPlots
push!(circuit, readout(1,1), readout(2,2))
plot_histogram(circuit,1000)