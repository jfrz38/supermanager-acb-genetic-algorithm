
import csv
import random
import sys

from player import Player
from search import GeneticAlgorithmSearch
from team import Team

sys.path.append(".")

class BestTeamSearch(GeneticAlgorithmSearch):

    def __init__(self, filename: str, population_size = 20):
        GeneticAlgorithmSearch.__init__(self)
        self._population_size = population_size
        self._players = self.generate_data(filename)
        self.guards = [x for x in self._players if x.position == 1]
        self.forwards = [x for x in self._players if x.position == 3]
        self.centers = [x for x in self._players if x.position == 5]
        self.position_to_player_list_map = {
            1: self.guards,
            3: self.forwards,
            5: self.centers,
        }
        

    def generate_data(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            return [
                Player(
                    team = row['team'],
                    name = row['name'],
                    position = int(row['position']),
                    value = int(row['value']),
                    price = int(row['price']),
                    work_permit = row['work_permit'],
                )
                for row in reader
            ]
    
    def generate_init_population(self):
        population = []
        for _ in range(self._population_size):
            roster = [random.sample(self.guards, 2)]
            roster.append(random.sample(self.forwards, 4))
            roster.append(random.sample(self.centers, 4))
            population.append(Team(self.flat_list(roster)))
        return population
    
    def flat_list(self, list):
        return [item for sublist in list for item in sublist]

    def do_mutation(self, team):
        for index, player in enumerate(team):
            if random.randint(0, 100) < self.probabilidad_mutacion:
                team[index] = self.random_player(team, player.position)
        return team
    
    def random_player(self, team, position):
        return random.choice(list(set(self.position_to_player_list_map[position]).difference({p for p in team if p.position == position})))

if __name__ == '__main__':
    search = BestTeamSearch('../Files/data.csv')
    search.start_search()
    best_team = search.get_result()
    if(len(best_team)>0):
        print('Mejor equipo: {} puntos por {}€'.format(sum(player.value for player in best_team),sum(player.price for player in best_team)))
        for player in best_team:
            print(player)
    else:
        print("No se ha podido encontrar ningún equipo")
