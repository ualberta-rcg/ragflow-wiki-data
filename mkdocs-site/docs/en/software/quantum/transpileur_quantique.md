---
title: "Transpileur quantique/en"
slug: "transpileur_quantique"
lang: "en"

source_wiki_title: "Transpileur quantique/en"
source_hash: "48efa85a8efa38de104d6d1c7c00df19"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:57:31.823861+00:00"

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

Classical transpilation describes the translation of code written in one programming language to code written in another language. It is a process similar to compilation.

In quantum computing, transpilation aims to ensure that a quantum circuit uses only the native gates of the quantum machine on which it will be executed. Transpilation also ensures that operations involving multiple qubits are assigned to qubits that are physically connected on the quantum chip.

## Transpilation steps

### Measurement decomposition
Measurements are made in a given basis, such as X, Y or Z bases, among others. Most quantum computers measure in the Z base (computing base). If another base is required, rotations must be added at the end of the circuit to adjust the measurement base.

### Intermediate decomposition
A first decomposition of the operations is necessary to run the circuit on a quantum machine in order to limit the number of different operations used by the circuit. For example, operations with more than two qubits must be decomposed into operations with two or one qubits.

### Placement
The idea is to establish an association between the wires of the user-created quantum circuit and the physical qubits of the machine. This step can be reduced to a [subgraph isomorphism problem](https://en.wikipedia.org/wiki/Subgraph_isomorphism_problem).

### Routing
Despite the placement step, some two-qubit operations may not be properly assigned to physical couplers available on the machine. In this case, [swap](https://pennylane.ai/qml/glossary/what-is-a-swap-gate) operations are used to virtually bring the qubits together and allow them to connect. However, these swap operations are very expensive, making optimal initial placement essential to minimize their use.

### Optimization
Qubits accumulate errors and lose their coherence over time. To limit this, the optimization process reduces the number of operations applied to each qubit using different classic algorithms. For example, it removes trivial and inverse operations; combines rotations on the same axis; and more generally replaces sections of circuits with equivalent circuits that generate fewer errors.

### Native gate decomposition
Every quantum computer has a finite set of basic operations (native gates) from which all other operations can be composed. For example, MonarQ has a set of 13 native gates. Transpilation thus decomposes all non-native circuit operations into native operations.

## Using the Calcul Québec transpiler with MonarQ
Calcul Québec has developed a transpiler that allows you to send circuits to MonarQ transparently, using the transpilation steps described above. This transpiler is integrated into a [PennyLane device](https://docs.pennylane.ai/en/stable/code/api/pennylane.device.html) and is therefore designed to be specifically used with [PennyLane](pennylane.md). For details, see [this documentation page](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).