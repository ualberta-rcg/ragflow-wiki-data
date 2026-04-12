---
title: "Snowflurry/en"
slug: "snowflurry"
lang: "en"

source_wiki_title: "Snowflurry/en"
source_hash: "bef0aa627f8393c2b3be4097d6ce00a5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:32:10.611215+00:00"

tags:
  []

keywords:
  - "simulations"
  - "circuit"
  - "état de Bell"
  - "SnowflurryPlots"
  - "Quantum circuits"
  - "simulate"
  - "Snowflurry"
  - "Julia"
  - "readout operation"
  - "Bell states"
  - "Quantum computing"
  - "plot_histogram"
  - "qubits"

questions:
  - "What is the Snowflurry library and what programming language is required to use it?"
  - "What are the necessary steps and commands to install and load Snowflurry on a cluster?"
  - "How can Snowflurry be used to construct and simulate a Bell state, and which quantum gates are involved?"
  - "Quelle bibliothèque Julia est utilisée pour générer l'histogramme du circuit quantique ?"
  - "Quel état quantique spécifique est simulé et représenté dans le graphique ?"
  - "Combien de simulations ont été exécutées pour produire les résultats affichés ?"
  - "How do you simulate a quantum circuit to obtain the exact state of the system?"
  - "What is the purpose of the `readout` operation?"
  - "Which function and library are used to visualize the measurement results?"
  - "Quelle bibliothèque Julia est utilisée pour générer l'histogramme du circuit quantique ?"
  - "Quel état quantique spécifique est simulé et représenté dans le graphique ?"
  - "Combien de simulations ont été exécutées pour produire les résultats affichés ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) is an open-source quantum computing library developed in [Julia](../julia.md) by [Anyon Systems](https://anyonsys.com/) that allows you to build, simulate, and run quantum circuits. A related library called [SnowflurryPlots](https://github.com/SnowflurrySDK/SnowflurryPlots.jl/) allows you to visualize the simulation results in a bar chart. Useful to explore quantum computing, its features are described in the [documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/index.html) and the [installation guide is available on the GitHub page](https://github.com/SnowflurrySDK/Snowflurry.jl). Like the [PennyLane](pennylane.md) library, Snowflurry can be used to run quantum circuits on the [MonarQ](../../clusters/monarq.md) quantum computer.

## Installation
The quantum computer simulator with [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) is available on all of our clusters. The [Julia](https://julialang.org/) programming language must be loaded before accessing Snowflurry.

```bash
[username@narval ~]$ module load julia
```

The Julia programming interface is then called and the Snowflurry quantum library is loaded (in about 5-10 minutes) with the commands:

```bash
[username@narval ~]$ julia
julia> import Pkg
julia> Pkg.add(url="https://github.com/SnowflurrySDK/Snowflurry.jl", rev="main")
julia> Pkg.add(url="https://github.com/SnowflurrySDK/SnowflurryPlots.jl", rev="main")
julia> using Snowflurry
```

Quantum logic gates and commands are described in the [Snowflurry documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/).

## Use case: Bell states
Bell states are maximally entangled two-qubit states. They are simple examples of two quantum phenomena: superposition and entanglement. The [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) library allows you to construct the first Bell state as follows:

```bash
[username@narval ~]$ julia
julia> using Snowflurry
julia> circuit=QuantumCircuit(qubit_count=2);
julia> push!(circuit,hadamard(1));
julia> push!(circuit,control_x(1,2));
julia> print(circuit)

Quantum Circuit Object:
   qubit_count: 2
q[1]:──H────*──
            ¦
q[2]:───────X──
```

In the above code section, the Hadamard gate creates an equal superposition of |0⟩ and |1⟩ on the first qubit while the CNOT gate (controlled X gate) creates an entanglement between the two qubits. We find an equal superposition of states |00⟩ and |11⟩, which is the first Bell state. The `simulate` function allows us to simulate the exact state of the system.

```julia
julia> state = simulate(circuit)
julia> print(state)
4-element Ket{ComplexF64}:
0.7071067811865475 + 0.0im
0.0 + 0.0im
0.0 + 0.0im
0.7071067811865475 + 0.0im
```

The `readout` operation lets you specify which qubits will be measured. The `plot_histogram` function from the SnowflurryPlots library allows you to visualize the results.

```bash
[username@narval ~]$ julia
julia> using SnowflurryPlots
julia> push!(circuit, readout(1,1), readout(2,2))
julia> plot_histogram(circuit,1000)