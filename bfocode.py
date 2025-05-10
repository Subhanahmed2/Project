import os
import random
import math
import csv
import binascii

class BFOA:
    def __init__(self, pop_size=100, problem_size=2, dimension=(-1, 1), elim_disp_steps=1, repro_steps=4, chem_steps=30):
        self.step_index = 0
        self.run_id = binascii.hexlify(os.urandom(6)).decode()

        self.problem_size = problem_size
        self.dimension = dimension
        self.search_space = [self.dimension for _ in range(self.problem_size)]

        self.pop_size = pop_size
        self.step_size = 0.1

        self.elim_disp_steps = elim_disp_steps
        self.repro_steps = repro_steps
        self.chem_steps = chem_steps
        self.swim_length = 3
        self.p_eliminate = 0.25

        self.d_attr = 0.1
        self.w_attr = 0.2
        self.h_rep = self.d_attr
        self.w_rep = 10

        self.cells = [{'vector': self.random_vector(self.search_space)} for _ in range(self.pop_size)]

    def objective_function(self, vector):
        return sum(x ** 2 for x in vector)

    def random_vector(self, minmax):
        return [random.uniform(x[0], x[1]) for x in minmax]

    def generate_random_direction(self):
        return self.random_vector([self.dimension for _ in range(self.problem_size)])

    def compute_cell_interaction(self, cell, d, w):
        total = 0.0
        for other_cell in self.cells:
            diff = sum((cell['vector'][i] - other_cell['vector'][i]) ** 2 for i in range(self.problem_size))
            total += d * math.exp(w * diff)
        return total

    def attract_repel(self, cell):
        attract = self.compute_cell_interaction(cell, -self.d_attr, -self.w_attr)
        repel = self.compute_cell_interaction(cell, self.h_rep, -self.w_rep)
        return attract + repel

    def evaluate(self, cell):
        cell['cost'] = self.objective_function(cell['vector'])
        cell['inter'] = self.attract_repel(cell)
        cell['fitness'] = cell['cost'] + cell['inter']
        return cell

    def tumble_cell(self, cell):
        step = self.generate_random_direction()
        vector = [
            max(min(cell['vector'][i] + self.step_size * step[i], self.search_space[i][1]), self.search_space[i][0])
            for i in range(self.problem_size)
        ]
        return {'vector': vector}

    def save(self):
        filename = f'bfoa_{self.run_id}.csv'
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if self.step_index == 0:
                writer.writerow(["step_index", "x", "y", "cost", "inter", "fitness", "sum_nutrients"])
            for cell in self.cells:
                writer.writerow([
                    self.step_index, cell['vector'][0], cell['vector'][1],
                    cell['cost'], cell['inter'], cell['fitness'], cell.get('sum_nutrients', 0)
                ])

    def chemotaxis(self):
        best = None
        for j in range(self.chem_steps):
            moved_cells = []
            for cell in self.cells:
                sum_nutrients = 0.0
                cell = self.evaluate(cell)
                if best is None or cell['cost'] < best['cost']:
                    best = cell
                sum_nutrients += cell['fitness']

                for _ in range(self.swim_length):
                    new_cell = self.tumble_cell(cell)
                    new_cell = self.evaluate(new_cell)
                    if new_cell['fitness'] > cell['fitness']:
                        break
                    cell = new_cell
                    sum_nutrients += cell['fitness']
                    if cell['cost'] < best['cost']:
                        best = cell

                cell['sum_nutrients'] = sum_nutrients
                moved_cells.append(cell)

            print(f"  >> chemo={j}, f={best['fitness']:.4f}, cost={best['cost']:.4f}")
            self.cells = moved_cells
            self.save()
            self.step_index += 1
        return best

    def search(self):
        best = None
        for l in range(self.elim_disp_steps):
            for k in range(self.repro_steps):
                c_best = self.chemotaxis()
                if best is None or c_best['cost'] < best['cost']:
                    best = c_best
                print(f" > best fitness={best['fitness']:.4f}, cost={best['cost']:.4f}")

                self.cells.sort(key=lambda c: c.get('sum_nutrients', 0))
                top_half = self.cells[:self.pop_size // 2]
                self.cells = top_half + top_half.copy()
                self.save()
                self.step_index += 1

            for cell in self.cells:
                if random.random() <= self.p_eliminate:
                    cell['vector'] = self.random_vector(self.search_space)

            self.save()
            self.step_index += 1

        print("Best solution:", best)
        return best

if __name__ == "__main__":
    os.makedirs('bfoa_results', exist_ok=True)
    os.chdir('bfoa_results')
    bfoa = BFOA(pop_size=600, elim_disp_steps=3, repro_steps=4, chem_steps=40)
    best = bfoa.search()
