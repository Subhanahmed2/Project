# Bacterial Foraging Optimization Algorithm (BFOA) - Step-by-Step

## Input:
- Population size `P`
- Problem dimension `D`
- Search space bounds `[L, U]`
- Chemotaxis steps `Nc`
- Swim length `Ns`
- Reproduction steps `Nre`
- Elimination-dispersal steps `Ned`
- Elimination probability `Ped`

## Output:
- Best solution vector found `x_best`
- Corresponding objective value `f(x_best)`

---

## Algorithm Steps:

### 1. Initialization
- Set parameters: `P`, `Nc`, `Ns`, `Nre`, `Ned`, `Ped`, `step_size`.
- Generate `P` bacteria randomly in the D-dimensional search space.

### 2. Elimination–Dispersal Loop (`l = 1 to Ned`)
#### 2.1 Reproduction Loop (`k = 1 to Nre`)
##### 2.1.1 Chemotaxis Loop (`j = 1 to Nc`)
For each bacterium `i`:
1. Evaluate its objective cost: `J(i) = f(x)`.
2. Compute interaction forces (attraction and repulsion) to get `fitness(i)`.
3. **Tumble**: Generate a random direction and move by `step_size`.
4. **Swim**: While new position improves `fitness(i)` and `m < Ns`, continue swimming.
5. Record the nutrient consumed during movement.

##### 2.1.2 Reproduction Phase
- Sum total nutrient for each bacterium.
- Sort bacteria by health (nutrient consumed).
- Eliminate the bottom 50%; duplicate the top 50%.

#### 2.2 Elimination–Dispersal Phase
- For each bacterium:
  - With probability `Ped`, eliminate and randomly reposition it.

### 3. Return the best bacterium found with the lowest objective cost.

---

## Notes:
- **Attraction/Repulsion** models bacterial swarm behavior.
- Objective function used: `Sphere Function` → `f(x) = Σ xi²`
- The algorithm is stochastic and results vary slightly each run.
