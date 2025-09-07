import random

from team import Team


class GeneticAlgorithmSearch:
    def __init__(self) -> None:
        self.n_iteraciones = 10000000
        self.actual_population = []
        self.probabilidad_mutacion = 10  # 10%
        self.salary_cap = 5000000

    def start_search(self):
        self.actual_population = self.generate_init_population()
        for _ in range(self.n_iteraciones):
            self.actual_population.sort(key=self.evaluate_chromosome)
            self.best_genes = self.actual_population[-1]
            new_population = []
            new_population.append(self.best_genes)
            population_to_choose = self.create_population_to_choose()
            while(True):
                parents = None
                parent1 = None
                parent2 = None
                if len(population_to_choose) > 1:
                    parents = random.sample(population_to_choose, 2)
                    parent1 = parents[0]
                    parent2 = parents[1]
                else:
                    parent1 = population_to_choose[0]
                    parent2 = population_to_choose[0]
                child = self.do_crossover(parent1, parent2)
                child = self.do_mutation(child)
                if not self.check_team(child):
                    continue
                else:
                    new_population.append(child)
                    break
            self.actual_population = new_population

    def evaluate_chromosome(self, team):
        return sum(player.value for player in team)

    def create_population_to_choose(self):
        to_return = []
        for position, chromosome in enumerate(self.actual_population):
            to_return.extend([chromosome]*position)
        return to_return

    def do_crossover(self, parent1, parent2):
        crossover_index = random.randint(0, len(parent1))
        new_team = Team(parent1[:crossover_index] + parent2[crossover_index:])
        return new_team

    def check_team(self, team) -> bool:
        """
        Comprobar que:
            1. NO se sobrepasa el límite de dinero
            2. Hay el número exacto de jugadores por posición
            3. Comprobar que se cumplen las reglas de los permisos de trabajo:
                3.1. Máximo de 2 jugadores extracomunitarios (bandera europea tachada)
                3.2. Mínimo de 4 jugadores locales (bandera española)
        """
        return (
            sum(player.price for player in team) < self.salary_cap
            and self.count_position(1, team) == 2
            and self.count_position(3, team) == 4
            and self.count_position(5, team) == 4
            and len(set(team)) == 10
            and self.count_work_permit("EXT", team) <= 2
            and self.count_work_permit("JFL", team) >=4
        )

    def count_position(self, position, team):
        return sum(player.position == position for player in team)
    
    def count_work_permit(self, permit, team):
        return sum(player.work_permit == permit for player in team)
    
    def get_result(self):
        if self.check_team(self.best_genes):
            return self.best_genes 
        else:
            return []
