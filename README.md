# Panthéon Quantique - Laboratoire Virtuel

Ce dépôt contient une collection de simulations de mécanique quantique computationnelle développées en Python. Le projet explore l'évolution des systèmes ouverts (décohérence) et les protocoles de communication quantique (téléportation), avec une approche rigoureuse basée sur l'algèbre linéaire (NumPy) et la validation par tests de régression.

## 🌍 Une Architecture Multi-Environnements

Ce projet a la particularité d'avoir été développé et exécuté sur deux plateformes distinctes, illustrant une grande flexibilité d'adaptation :

1. **Termux (Android - Smartphone)** : Le berceau du projet. C'est dans cet environnement ultra-contraint que l'architecture "Négantropique" a été pensée (gestion de la dissipation, bus de signaux, systèmes distribués).
2. **Visual Studio Code (Windows - Laptop)** : L'environnement de déploiement final pour les simulations de ce dépôt. VS Code a permis d'exploiter toute la puissance du CPU pour faire tourner des matrices complexes (jusqu'à 64x64) et de générer les visualisations graphiques via la bibliothèque `turtle`.

## 📊 Résultats Scientifiques

### 1. Décohérence d'un Qubit (`qubit_visuel.py`)
Effondrement du vecteur de Bloch vers le centre de la sphère, illustrant la perte d'information quantique.

### 2. Intrication à 2 Qubits (`intrication.py`)
Création d'intrication (Concurrence) couplée à la dissipation (Pureté).

### 3. Téléportation Quantique sous Bruit (`teleportation.py`)
Démonstration de la limite de l'avantage quantique. Au-delà d'un certain seuil de bruit, un câble classique devient plus fiable que la téléportation quantique.

## 📁 Contenu du Dépôt
- `qubit_visuel.py` : Animation d'un qubit sur la Sphère de Bloch (Turtle).
- `pantheon.py` : Simulation d'un Qutrit (système à 3 niveaux) avec les matrices de Gell-Mann et l'équation de Lindblad.
- `intrication.py` : Intrication à 2 qubits (Espace 4x4) avec calcul de la Concurrence de Wootters.
- `teleportation.py` : Protocole de téléportation quantique avec test de robustesse face au bruit.

## ⚙️ Prérequis
- Python 3.x
- NumPy (`pip install numpy`)

## 🚀 Exécution
```bash
## 📊 Résultats Détaillés des Simulations

### 1. Décohérence d'un Qubit (`qubit_visuel.py`)
Effondrement du vecteur de Bloch vers le centre de la sphère, illustrant la perte d'information quantique due à l'environnement.

| Temps (s) | Pureté | État Physique |
| :---: | :---: | :--- |
| 0.0 | 1.000 | État pur (superposition parfaite) |
| 0.6 | 0.942 | Début de décohérence |
| 1.2 | 0.887 | Perte d'information quantique |
| 2.0 | 0.819 | Régime de dissipation avancé |
| 3.0 | 0.741 | État presque classique |
| Fin | 0.050 | Effondrement total (mélange statistique) |

### 2. Qutrit à 3 niveaux (`pantheon.py`)
Évolution d'un système SU(3) sous l'équation maîtresse de Lindblad avec les matrices de Gell-Mann.

| Tick | Pureté du Qutrit | Statut |
| :---: | :---: | :--- |
| 01 | 0.9993 | État initial |
| 05 | 0.9967 | Dissipation lente |
| 10 | 0.9934 | Perte de cohérence |
| 15 | 0.9902 | État final (stable) |

### 3. Intrication à 2 Qubits (`intrication.py`)
Création d'intrication (Concurrence) couplée à la dissipation (Pureté). Le système passe d'un état pur à un état intriqué.

| Temps (s) | Pureté | Concurrence (Intrication) |
| :---: | :---: | :---: |
| 0.00 | 0.9990 | 0.0006 |
| 0.05 | 0.9940 | 0.0202 |
| 0.10 | 0.9891 | 0.0674 |
| 0.15 | 0.9842 | 0.1408 |
| 0.20 | 0.9794 | 0.2391 |
| 0.25 | 0.9746 | 0.3613 |
| 0.29 | 0.9708 | 0.4777 (Pic d'intrication) |

### 4. Téléportation Quantique sous Bruit (`teleportation.py`)
Démonstration de la limite de l'avantage quantique. Au-delà d'un certain seuil de bruit, un câble classique devient plus fiable que la téléportation quantique.

| Taux de Bruit (γ) | Fidélité | Statut | Interprétation |
| :---: | :---: | :--- | :--- |
| **0.00** | **100.00 %** | ✅ Parfaite | Téléportation idéale sans perturbation |
| **0.05** | **70.00 %** | 🟡 Avantage Quantique | Le signal résiste au bruit |
| **0.10** | **40.00 %** | ❌ Limite Classique | Le bruit détruit l'information |
| **0.20** | **0.00 %** | ❌ Échec | L'état quantique est totalement perdu |python teleportation.py
