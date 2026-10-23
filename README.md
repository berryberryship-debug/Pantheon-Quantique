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
python teleportation.py
