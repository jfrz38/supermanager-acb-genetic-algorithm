import csv
import json
import os
import sys
import unicodedata


class manage_file():

    def __init__(self) -> None:
        pass
    
    def save_acb_data_players(self, data):
        self.save_data_players('acb_data', data)

    def save_supermanager_data_players(self, data):
        self.save_data_players('supermanager_data', data)

    def save_merged_data(self, data):
        self.save_data_players('merged_data', data)

    def save_data_players(self, path, data):
        with open(os.path.join(sys.path[0], '../Files/' + path + '.json'), 'w+', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))

    def merge_files(self):
        acb_data = self.read_file("acb_data")
        supermanager_data = self.read_file("supermanager_data")
        for data in acb_data:
            team = data["team"]
            for player in data["players"]:
                name = player["name"]
                found_player = self.find_supermanager_player(name, team, supermanager_data)
                if found_player:
                    player["price"] = found_player["price"]
                    player["position"] = found_player["position"]
                else:
                    player["price"] = 1000000000
        self.save_merged_data(acb_data)

    def find_supermanager_player(self, name, team, supermanager_data):
        found_players = list(filter(lambda x: x["team"].casefold() == team.casefold(), supermanager_data))
        if len(found_players) <= 0:
            return None
        name = self.convert_name(name)
        found_player = next(filter(lambda x: self.create_lambda_name(x["name"]).casefold() == name.casefold(), found_players), None)
        if(not found_player):
            print(f'{name} de {team} NOT FOUND')
        return found_player

    def convert_name(self, name):
        name_parts = self.remove_accents(name).split(' ')
        return f'{name_parts[0][0]}. {" ".join(name_parts[1:])}'
    
    def remove_accents(self, data):
        return (unicodedata.normalize('NFKD', u''+data).encode('ASCII', 'ignore').lower()).decode("utf-8") 

    def create_lambda_name(self, name):
        name = self.remove_accents(name)
        # Hay algunos nombres que no coinciden entre ACB y Super manager
        match name:
            case "bj johnson": return "b. johnson iii"
            case "a. balcerowski": return "o. balcerowski"
            case "aj slaughter": return "a. slaughter"
            case "w. tavares": return "e. tavares"
            case "n.williams-goss": return "n. williams-goss"
            case "n. dedovic": return "n. djedovic"
            case "j. webb": return "j. webb iii"
            case "lopez-arostegui": return "x. lopez-arostegui"
            case _: return name

    def read_file(self, filename):
        with open(os.path.join(sys.path[0], '../Files/' + filename + '.json'), encoding="utf8") as file:
            return json.loads(file.read())

    def create_csv_format(self, data):
        result = []
        for d in data:
            team = d["team"]
            for player in d["players"]:
                result.append([team, player["name"], player["position"], player["value"], player["price"], player["permiso"]])
        return result

    def save_data_csv(self, data = None):
        if(not data):
            self.merge_files()
        data = self.read_file('merged_data')
        csv_data = self.create_csv_format(data)
        header = ["team", "name", "position", "value", "price", "work_permit"]
        with open(os.path.join(sys.path[0],'../Files/data.csv'), 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(csv_data)
