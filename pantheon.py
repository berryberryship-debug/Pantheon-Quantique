import numpy as np
import time

class TopologyEngine:
    def __init__(self):
        self.lam = [
            np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex),
            np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex),
            np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex),
            np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex),
            np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex),
            np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex),
            np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex),
            np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3)
        ]
        psi0 = np.ones(3, dtype=complex) / np.sqrt(3)
        self.rho = np.outer(psi0, psi0.conj())
        self.dt = 0.01
        
    def step(self, dissipation=0.15):
        H = 0.5 * self.lam[0] + 0.3 * self.lam[5]
        d_rho = -1j * (H @ self.rho - self.rho @ H)
        L = np.array([[0,0,0],[0,0,0],[0,0,1]], dtype=complex)
        L_dag_L = L.conj().T @ L
        d_rho += dissipation * (L @ self.rho @ L.conj().T - 0.5 * (L_dag_L @ self.rho + self.rho @ L_dag_L))
        
        self.rho += d_rho * self.dt
        self.rho = 0.5 * (self.rho + self.rho.conj().T)
        val_propres, vecteurs = np.linalg.eigh(self.rho)
        val_propres = np.maximum(val_propres, 0.0)
        somme = np.sum(val_propres)
        if somme <= 1e-15: self.rho = np.eye(3, dtype=complex) / 3.0
        else: self.rho = vecteurs @ np.diag(val_propres / somme) @ vecteurs.conj().T
            
        purity = float(np.real(np.trace(self.rho @ self.rho)))
        return purity

if __name__ == "__main__":
    print("=== PANTHÉON QUANTIQUE (3x3) ===")
    topo = TopologyEngine()
    for i in range(15):
        purity = topo.step()
        print(f"Tick {i+1:02d} | Pureté du Qutrit : {purity:.4f}")
        time.sleep(0.2)
    print("=== FIN ===")
    input("\nAppuie sur Entrée...")
