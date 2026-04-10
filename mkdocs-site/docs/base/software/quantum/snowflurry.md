---
title: "Snowflurry"
slug: "snowflurry"
lang: "base"

source_wiki_title: "Snowflurry"
source_hash: "1e3feff1da1f37d2e6b05e4350e8720d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:21:31.114805+00:00"

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

Snowflurry is an open-source quantum computing library developed in [Julia](julia.md) by [Anyon Systems](https://anyonsys.com/fr) that allows for building, simulating, and executing quantum circuits. A related library named [SnowflurryPlots](https://github.com/SnowflurrySDK/SnowflurryPlots.jl/) enables the visualization of simulation results in a bar chart. Practical for exploring quantum computing, the features are available in the [documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/index.html) and the installation guide is available on the [GitHub](https://github.com/SnowflurrySDK/Snowflurry.jl) page. Like the [PennyLane](pennylane.md) library, Snowflurry can be used to execute quantum circuits on the [MonarQ](monarq.md) quantum computer.

## Installation
The quantum computer simulator with [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl) is available on all our clusters. The [Julia](https://julialang.org/) programming language must be loaded before accessing Snowflurry with the command:

```bash
module load julia
```

Next, the Julia programming interface is called and the Snowflurry quantum library is loaded (approximately 5-10 minutes) with the commands:

```julia
julia
julia> import Pkg
julia> Pkg.add(url="https://github.com/SnowflurrySDK/Snowflurry.jl", rev="main")
julia> Pkg.add(url="https://github.com/SnowflurrySDK/SnowflurryPlots.jl", rev="main")
julia> using Snowflurry
```

Quantum logic gates and commands are described in the [Snowflurry documentation](https://snowflurrysdk.github.io/Snowflurry.jl/dev/).

## Usage Example: Bell States
Bell states are maximally entangled two-qubit states. Two simple examples of quantum phenomena are superposition and entanglement. The [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl/) library allows for constructing the first Bell state as follows:

```julia
julia
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

In the code section above, the Hadamard gate creates an equal superposition of |0⟩ and |1⟩ on the first qubit, while the CNOT gate (controlled-X gate) creates entanglement between the two qubits. This results in an equal superposition of the |00⟩ and |11⟩ states, which is the first Bell state. The `simulate` function allows for simulating the exact state of the system.

```julia
julia> state = simulate(circuit)
julia> print(state)
4-element Ket{ComplexF64}:
0.7071067811865475 + 0.0im
0.0 + 0.0im
0.0 + 0.0im
0.7071067811865475 + 0.0im
```

To take a measurement, the `readout` operation allows you to specify which qubits will be measured. The `plot_histogram` function from the SnowflurryPlots library enables the visualization of the results.

```julia
julia
julia> using SnowflurryPlots
julia> push!(circuit, readout(1,1), readout(2,2))
julia> plot_histogram(circuit,1000)