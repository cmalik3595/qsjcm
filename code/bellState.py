from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService
#from qiskit_ibm_provider import IBMProvider
import matplotlib.pyplot as plt

# QuantumCircuit is clss in qiskit.
# https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit
# This example is derived from IBM guide on hello world : https://docs.quantum.ibm.com/guides/hello-world
qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

# Add a Hadamard gate to qubit 0
"""
Description: Superposition using Hadamard gate

The Hadamard gate, often denoted as H, is a fundamental single-qubit quantum gate. It transforms a qubit into an equal superposition of the |0⟩ and |1⟩ states, or vice versa. This gate is crucial for creating superposition and enabling parallel computation in quantum algorithms.

Numerical representation, H = 1/√2 * [, [1, -1]] 

Uses:
Quantum Algorithms:
It is a key component in algorithms like Shor's algorithm and Grover's algorithm, enabling parallelism and superposition. 
Quantum Error Correction:
Its self-inverse property is useful in quantum error correction techniques. 
Generating Randomness:
Applying the Hadamard gate to a qubit initialized in a known state creates a uniformly random qubit that can be used in quantum random number generation. 


Links : 

1. https://pennylane.ai/qml/glossary/what-is-a-hadamard-gate#:~:text=The%20square%20of%20the%20Hadamard,is%20called%20HGate%20in%20Qiskit.
2. https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.HGate
3. https://en.wikipedia.org/wiki/Quantum_logic_gate#:~:text=in%20instruction%20sets.-,Hadamard%20gate,and

"""
qc.h(0)

# This function Perform a controlled-X gate on qubit 1, controlled by qubit 0
"""
Description: Entanglement qbit0(control) with qbit1(target) using Controlled-X or CNOT or CX gate. Now the two qbits are in Bell state.

A controlled-X gate, also known as a CNOT or CX gate, is a fundamental two-qubit quantum gate that acts on a control qubit and a target qubit. It applies an X gate (also known as a Pauli-X gate or bit flip) to the target qubit only when the control qubit is in the state |1⟩. If the control qubit is in the state |0⟩, the gate does nothing to the target qubit.

Here's a more detailed breakdown:
- Control and Target Qubits: The controlled-X gate operates on two qubits: a control qubit and a target qubit.
- Action on Target Qubit: The core function of the gate is to conditionally flip the state of the target qubit.
- Conditional Flip: If the control qubit is measured to be |1⟩, the controlled-X gate flips the state of the target qubit (e.g., |0⟩ becomes |1⟩, and |1⟩ becomes |0⟩).
- No Effect on Control Qubit: The controlled-X gate does not change the state of the control qubit.
- Common Usage: The controlled-X gate is a crucial component in constructing quantum circuits and is used for entanglement and other quantum computations.
- Notation: It's often denoted as CNOT or CX.
- Mathematical Representation: In the computational basis, the controlled-X gate can be represented by the following matrix:
    |1⟩ --> |1⟩ (control stays unchanged)
    |0⟩ --> |0⟩ (control stays unchanged)
    |0⟩ --> |1⟩ (if control is |1⟩)
    |1⟩ --> |0⟩ (if control is |1⟩)

Code:
     [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]]

Links

1. https://cnot.io/quantum_computing/two_qubit_operations.html
2. https://en.wikipedia.org/wiki/Controlled_NOT_gate#:~:text=In%20computer%20science%2C%20the%20controlled,used%20in%20classical%20reversible%20computing.
3. https://www.mathworks.com/help/matlab/ref/cxgate.html
"""
qc.cx(0, 1)

# Measure both qubit. This Collapses the quantum state into classical bits. You’ll observe either 00 or 11 with ~50% probability each.
qc.measure([0, 1], [0, 1])

# Return a text drawing of the circuit.
print(qc.draw())

# Simulation part
"""
- Uses the qasm_simulator to mimic quantum behavior.
- Runs the circuit 1024 times to gather statistics.
- get_counts() returns a histogram of outcomes, typically close to 50/50 for 00 and 11
"""
backend = Aer.get_backend("qasm_simulator")
compiled = transpile(qc, backend)
job = backend.run(compiled)
result = job.result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
#plt.show()

# Running on real hardware
# Setup IBM cloud account
QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token="7oB3zF3-YJ5Q_1HWgA322HrCtLBT6sxEu2wMYGMx6zVG",  # Replace with your actual token
    overwrite=True,
    set_as_default=True
)

# Load the Service and Choose a Backend
service = QiskitRuntimeService()
service.backends()  # List all available backends

backend = service.backend("ibmq_qasm_simulator")  # Or a real device like "ibmq_lima"

# Initialize the provider: Connects to your IBM Quantum account. You must have previously saved your API token using IBMProvider.save_account()
#IBMProvider.save_account("47277e1444e85d85dda57158d1b3c23726714caf1f5395164ea2dc080cb196d20904d52b935ad96e8025656f57e68264abbb3751dc60f2be80894953e79760ec", overwrite=True)

#provider = IBMProvider()

# Choose a backend:
# 'ibmq_qasm_simulator' is a cloud-based simulator.
# To run on real hardware, replace with a real device name like 'ibmq_lima' or 'ibmq_belem'.
#backend = provider.get_backend('ibmq_qasm_simulator')

# Submit the job: Sends your circuit to the selected backend for execution.
#job = execute(qc, backend, shots=1024)
job = backend.run(qc, shots=1024)

#  Retrieve results: Once the job finishes, you get the measurement outcomes.
#  Real hardware introduces noise, so results may deviate slightly from the ideal 50/50 split.
result = job.result()
print(result.get_counts())





