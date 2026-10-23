import numpy as np

def op_on_qubit(n_qubits, op, target):
    ops = [np.eye(2, dtype=complex)] * n_qubits
    ops[target] = op
    result = ops[0]
    for o in ops[1:]: result = np.kron(result, o)
    return result

def cnot_on(n_qubits, control, target):
    dim = 2**n_qubits
    M = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = [(i >> (n_qubits - 1 - k)) & 1 for k in range(n_qubits)]
        if bits[control] == 1: bits[target] = 1 - bits[target]
        j = 0
        for b in bits: j = (j << 1) | b
        M[j, i] = 1.0
    return M

class TeleportationBruit:
    def __init__(self):
        self.I = np.eye(2, dtype=complex)
        self.H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        self.X = np.array([[0, 1], [1, 0]], dtype=complex)
        self.Z = np.array([[1, 0], [0, -1]], dtype=complex)

    def appliquer_bruit(self, rho, gamma, n_total):
        if gamma == 0: return rho
        d_rho = np.zeros_like(rho)
        for q in range(n_total):
            Z_q = op_on_qubit(n_total, self.Z, q)
            LdL = Z_q.conj().T @ Z_q
            d_rho += gamma * (Z_q @ rho @ Z_q.conj().T - 0.5 * (LdL @ rho + rho @ LdL))
        rho_bruite = rho + d_rho
        evals, evecs = np.linalg.eigh(rho_bruite)
        evals = np.maximum(evals, 0); evals /= np.sum(evals)
        return evecs @ np.diag(evals) @ evecs.conj().T

    def teleporter(self, etat_charlie, gamma=0.0):
        n_total = 6
        etat_vide = np.array([1, 0], dtype=complex)
        etat_alice_bob = np.kron(etat_vide, etat_vide)
        psi = np.kron(np.kron(etat_charlie, etat_alice_bob), etat_alice_bob)
        rho = np.outer(psi, np.conj(psi))

        for a, b in [(2, 4), (3, 5)]:
            H_a = op_on_qubit(n_total, self.H, a)
            rho = H_a @ rho @ H_a.conj().T
            CNOT = cnot_on(n_total, a, b)
            rho = CNOT @ rho @ CNOT.conj().T

        rho = self.appliquer_bruit(rho, gamma, n_total)

        for c, a in [(0, 2), (1, 3)]:
            CNOT = cnot_on(n_total, c, a)
            rho = CNOT @ rho @ CNOT.conj().T
            H_c = op_on_qubit(n_total, self.H, c)
            rho = H_c @ rho @ H_c.conj().T

        rho_bob = np.zeros((4, 4), dtype=complex)
        for m in range(16):
            m_C0 = (m >> 3) & 1; m_C1 = (m >> 2) & 1
            m_A0 = (m >> 1) & 1; m_A1 = m & 1
            proj = np.zeros((16, 16), dtype=complex)
            proj[m, m] = 1.0
            P = np.kron(proj, np.eye(4, dtype=complex))
            bloc = (P @ rho @ P)[m*4:(m+1)*4, m*4:(m+1)*4]
            corr = np.eye(4, dtype=complex)
            if m_C0 == 1: corr = np.kron(self.Z, self.I) @ corr
            if m_C1 == 1: corr = np.kron(self.I, self.Z) @ corr
            if m_A0 == 1: corr = np.kron(self.X, self.I) @ corr
            if m_A1 == 1: corr = np.kron(self.I, self.X) @ corr
            rho_bob += corr @ bloc @ corr.conj().T

        trace = np.real(np.trace(rho_bob))
        if trace > 1e-15: rho_bob /= trace
        rho_charlie = np.outer(etat_charlie, np.conj(etat_charlie))
        return np.real(np.trace(rho_bob @ rho_charlie))

if __name__ == "__main__":
    print("=== TÉLÉPORTATION 2 QUBITS AVEC BRUIT ===")
    proto = TeleportationBruit()
    etat = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    print(f"\n{'Bruit (gamma)':>15} | {'Fidélité':>10} | Statut")
    for gamma in [0.0, 0.05, 0.1, 0.2, 0.4, 0.6]:
        fid = proto.teleporter(etat, gamma)
        if fid > 0.99: statut = "Parfaite"
        elif fid > 2/3: statut = "Avantage Quantique"
        else: statut = "Limite Classique"
        print(f"{gamma:15.2f} | {fid*100:8.2f} % | {statut}")
    input("\nAppuie sur Entrée...")
