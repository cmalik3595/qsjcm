from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

qc.h(0)        # Hadamard on qubit 0
qc.cx(0, 1)    # CNOT: qubit 0 controls qubit 1
qc.measure([0, 1], [0, 1])  # Measure both qubits

backend = Aer.get_backend("qasm_simulator")
compiled = transpile(qc, backend)
job = backend.run(compiled)
result = job.result()
counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()

