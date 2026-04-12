---
title: "Snowflurry"
slug: "snowflurry"
lang: "base"

source_wiki_title: "Snowflurry"
source_hash: "1e3feff1da1f37d2e6b05e4350e8720d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:31:47.182956+00:00"

tags:
  []

keywords:
  - "superposition égale"
  - "Circuits quantiques"
  - "porte CNOT"
  - "porte de Hadamard"
  - "opération readout"
  - "SnowflurryPlots"
  - "état de Bell"
  - "Informatique quantique"
  - "Snowflurry"
  - "Julia"
  - "mesure"
  - "intrication"
  - "États de Bell"
  - "qubits"
  - "plot_histogram"

questions:
  - "Qu'est-ce que la bibliothèque Snowflurry et quelles sont ses principales fonctionnalités dans le domaine de l'informatique quantique ?"
  - "Quelles sont les étapes et les commandes requises pour installer et charger Snowflurry sur une grappe de calcul ?"
  - "Comment peut-on utiliser Snowflurry pour construire et simuler un circuit quantique générant un état de Bell ?"
  - "Quelle opération permet de spécifier les qubits qui seront mesurés dans le circuit ?"
  - "Quelle fonction et quelle bibliothèque sont utilisées pour visualiser les résultats sous forme d'histogramme ?"
  - "Quel état quantique spécifique est simulé et représenté dans l'exemple fourni ?"
  - "Quel est le rôle spécifique de la porte de Hadamard sur le premier qubit ?"
  - "Quel état quantique final est obtenu grâce à l'intrication créée par la porte CNOT ?"
  - "Quelle est l'utilité de la fonction simulate dans le contexte de ce code ?"
  - "Quelle opération permet de spécifier les qubits qui seront mesurés dans le circuit ?"
  - "Quelle fonction et quelle bibliothèque sont utilisées pour visualiser les résultats sous forme d'histogramme ?"
  - "Quel état quantique spécifique est simulé et représenté dans l'exemple fourni ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) is an open-source quantum computing library developed in [Julia](../julia.md) by [Anyon Systems](https://anyonsys.com/fr) that allows users to build, simulate, and execute quantum circuits.
A related library called [SnowflurryPlots](https://github.com/SnowflurrySDK/SnowflurryPlots.jl/) allows for visualizing simulation results in a bar diagram. Useful for exploring quantum computing, its features are available in the [documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/index.html), and the installation guide is available on the [GitHub](https://github.com/SnowflurrySDK/Snowflurry.jl) page. Similar to the [PennyLane](pennylane.md) library, Snowflurry can be used to run quantum circuits on the [MonarQ](../../clusters/monarq.md) quantum computer.

## Installation
The quantum computer simulator with [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) is available on all our clusters. The [Julia](https://julialang.org/) programming language must be loaded before accessing Snowflurry with the command:

```bash
module load julia
```

Next, the Julia programming interface is invoked, and the Snowflurry quantum library is loaded (approximately 5-10 minutes) with the following commands:

```julia
julia
import Pkg
Pkg.add(url="https://github.com/SnowflurrySDK/Snowflurry.jl", rev="main")
Pkg.add(url="https://github.com/SnowflurrySDK/SnowflurryPlots.jl", rev="main")
using Snowflurry
```

Quantum logic gates and commands are described in the [Snowflurry documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/).

## Example Usage: Bell States
Bell states are maximally entangled two-qubit states. Two simple examples of quantum phenomena are superposition and entanglement. The [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) library allows for constructing the first Bell state as follows:

```julia
using Snowflurry
circuit=QuantumCircuit(qubit_count=2);
push!(circuit,hadamard(1));
push!(circuit,control_x(1,2));
print(circuit)

# Expected Output:
# Quantum Circuit Object:
#    qubit_count: 2
# q[1]:──H────*──
#             ¦
# q[2]:───────X──
```

In the code section above, the Hadamard gate creates an equal superposition of |0⟩ and |1⟩ on the first qubit, while the CNOT gate (controlled-X gate) creates entanglement between the two qubits. This results in an equal superposition of the |00⟩ and |11⟩ states, which is the first Bell state. The `simulate` function allows for simulating the exact state of the system.

```julia
state = simulate(circuit)
print(state)

# Expected Output:
# 4-element Ket{ComplexF64}:
# 0.7071067811865475 + 0.0im
# 0.0 + 0.0im
# 0.0 + 0.0im
# 0.7071067811865475 + 0.0im
```

To perform a measurement, the `readout` operation allows specifying which qubits will be measured. The `plot_histogram` function from the SnowflurryPlots library allows for visualizing the results.

```julia
using SnowflurryPlots
push!(circuit, readout(1,1), readout(2,2))
plot_histogram(circuit,1000)