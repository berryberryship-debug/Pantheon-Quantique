import numpy as np
import time

class DeuxQubits:
    def __init__(self):
        self.I = np.eye(2, dtype=complex)
        X = np.array([[0, 1], [1, 0]], dtype=complex)
        Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
        Z = np.array([[1, 0], [0, -1]], dtype=complex)
        
        self.X1 = np.kron(X, self.I)
        self.X2 = np.kron(self.I, X)
        self.Z1 = np.kron(Z, self.I)
        self.Z2 = np.kron(self.I, Z)
        self.Y1 = np.kron(Y, self.I)
        self.Y2 = np.kron(self.I, Y)
        
        self.rho = np.zeros((4, 4), dtype=complex)
        self.rho[1, 1] = 1.0 
        self.dt = 0.01
        
    def calculer_concurrence(self):
        YY = self.Y1 @ self.Y2
        rho_star = np.conj(self.rho)
        R = self.rho @ YY @ rho_star @ YY
        evals = np.linalg.eigvalsh(R)
        evals = np.sort(np.maximum(evals, 0))[::-1]
        sqrt_evals = np.sqrt(evals)
        C = max(0.0, sqrt_evals[0] - sqrt_evals[1] - sqrt_evals[2] - sqrt_evals[3])
        return float(np.real(C))

    def step(self):
        J = 1.0 
        H = J * (self.X1 @ self.X2 + self.Y1 @ self.Y2 + self.Z1 @ self.Z2)
        gamma = 0.05
        sm = np.array([[0, 1], [0, 0]], dtype=complex)
        L1 = np.kron(sm, self.I) 
        L2 = np.kron(self.I, sm)
        
        d_rho = -1j * (H @ self.rho - self.rho @ H)
        for L in [L1, L2]:
            L_dag_L = L.conj().T @ L
            d_rho += gamma * (L @ self.rho @ L.conj().T - 0.5 * (L_dag_L @ self.rho + self.rho @ L_dag_L))
            
        self.rho += d_rho * self.dt
        self.rho = 0.5 * (self.rho + self.rho.conj().T)
        evals, evecs = np.linalg.eigh(self.rho)
        evals = np.maximum(evals, 0.0)
        evals /= np.sum(evals)
        self.rho = evecs @ np.diag(evals) @ evecs.conj().T
        
        purity = np.real(np.trace(self.rho @ self.rho))
        concurrence = self.calculer_concurrence()
        return purity, concurrence

if __name__ == "__main__":
    print("=== 2 QUBITS (4x4) ===")
    print("Temps |  Pureté  | Concurrence")
    systeme = DeuxQubits()
    for i in range(30):
        purity, conc = systeme.step()
        print(f"{i*0.01:5.2f} | {purity:8.4f} | {conc:8.4f}")
        time.sleep(0.1)
    input("\nAppuie sur Entrée...")
