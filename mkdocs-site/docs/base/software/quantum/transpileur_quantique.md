---
title: "Transpileur quantique"
slug: "transpileur_quantique"
lang: "base"

source_wiki_title: "Transpileur quantique"
source_hash: "c11223fd0b44fdc255498efcdb1682da"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:57:21.311358+00:00"

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

Classical transpilation describes the translation of code written in one programming language into code written in another language. It is a process analogous to compilation.

In the context of quantum computing, transpilation aims to ensure that a quantum circuit uses only the native gates of the quantum machine on which it will be executed. Transpilation also ensures that multi-qubit operations are assigned to physically connected qubits on the quantum chip.

## Transpilation Steps

### Measurement Decomposition
Measurements are performed in a given basis, such as the X, Y, or Z bases, among others. Most quantum computers measure in the Z basis (computational basis). If another basis is required, rotations must be added at the end of the circuit to adjust the measurement basis.

### Intermediate Decomposition
An initial decomposition of operations is necessary to execute the circuit on a quantum machine to limit the number of different operations used by the circuit. For example, operations with more than two qubits must be decomposed into two-qubit or single-qubit operations.

### Placement
The idea is to establish an association between the wires of the created quantum circuit and the physical qubits of the machine. This step can be reduced to a [subgraph isomorphism problem](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27isomorphisme_de_sous-graphes).

### Routing
Despite the placement step, some two-qubit operations may not be correctly assigned to physically available couplers on the machine. In this case, [swap operations](https://pennylane.ai/qml/glossary/what-is-a-swap-gate) are used to virtually bring the qubits closer and allow their connection. However, these swap operations are very costly, making optimal initial placement essential to minimize their use.

### Optimization
Qubits accumulate errors and lose their coherence over time. To limit these effects, the optimization process reduces the number of operations applied to each qubit using various classical algorithms. For example, it removes trivial and inverse operations; combines rotations on the same axis; and, more generally, replaces circuit sections with equivalent circuits, generating fewer errors.

### Native Gate Decomposition
Each quantum computer has a finite set of basic operations (native gates) from which all other operations can be composed. For example, MonarQ has a set of 13 native gates. Transpilation thus decomposes all non-native operations in a circuit into native operations.

## Using the Calcul Québec Transpiler with MonarQ
Calcul Québec has developed a transpiler that allows circuits to be sent to MonarQ transparently, using the transpilation steps mentioned above. This transpiler is integrated into a [PennyLane device](https://docs.pennylane.ai/en/stable/code/api/pennylane.device.html) and is therefore designed to be specifically used with [PennyLane](pennylane.md). For details, consult [the documentation](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).