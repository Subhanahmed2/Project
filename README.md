# Project
# Bacterial Foraging Optimization Algorithm (BFOA)

## 🧠 Overview

This project implements the **Bacterial Foraging Optimization Algorithm (BFOA)**, a nature-inspired optimization technique that simulates the foraging behavior of E. coli bacteria. BFOA is particularly effective for solving nonlinear, multidimensional optimization problems.

### 🔬 Key Concepts

- **Chemotaxis:** Movement behavior based on nutrient gradients.
- **Swarming:** Communication among bacteria through chemical signaling.
- **Reproduction:** Healthier bacteria (better solutions) are replicated.
- **Elimination-Dispersal:** Random elimination and reinitialization of some bacteria to maintain diversity.

### 📊 Time Complexity

**O(P × Nc × Ns × Nre × Ned)**  
Where:
- **P** = Number of bacteria (population size)  
- **Nc** = Number of chemotaxis steps  
- **Ns** = Swim length  
- **Nre** = Number of reproduction steps  
- **Ned** = Number of elimination-dispersal events  

This means the algorithm scales linearly with the number of bacteria and each iterative parameter, so performance tuning should consider this carefully.

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Repository


### 2. Environment Requirements

This project requires **Python 3.x**. All dependencies are from the standard library.

### 3. Run the Algorithm

```bash
python bfoa.py
```

### 4. Output

- The results are saved to a CSV file in the `bfoa_results` folder.
- Each line logs bacterial positions, fitness, interaction effects, and nutrient absorption at every step.
- Console output shows progress per chemotaxis and reproduction round.

---

## 📁 File Structure

- `bfoa.py` – Main Python script implementing BFOA.
- `bfoa_results/` – Automatically generated folder storing results per run.

---

## 📝 Example Configuration

You can modify algorithm parameters at the bottom of `bfoa.py`:

```python
bfoa = BFOA(pop_size=600, elim_disp_steps=3, repro_steps=4, chem_steps=40)
```

Adjust the parameters like `pop_size`, `chem_steps`, `swim_length`, etc., to suit your optimization needs.

---

## 📌 Notes

- The default objective function is **Sphere Function**: _f(x) = ∑ xᵢ²_.
- This implementation focuses on clarity and educational value, ideal for research or learning.
