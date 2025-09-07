import time

from selenium.webdriver.common.by import By


class scrap_acb():

    def start_scrap(self, driver):
        searchUrl = "https://www.acb.com/"
        driver.get(searchUrl)
        return self.iterate_all_teams(driver)
    
    def iterate_all_teams(self, driver):
        teams = []
        teams_found = driver.find_elements(By.XPATH, "//div[@class='contenedor_logos_equipos']//a")
        for team in teams_found:
            url = team.get_attribute("href")
            teams.append(self.open_team(driver, url))
            time.sleep(2)
        return teams

    def open_team(self, driver, url):
        driver.execute_script(f'window.open("{url}","_blank");')
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)
        team_name = driver.find_element(By.XPATH, "//div[@class='datos']//h1").text
        print(f'Scraping team {str(team_name)}')
        players_found = driver.find_elements(By.XPATH, "//div[@class='grid_plantilla principal']//article")
        players = []
        for player in players_found:
            players.append(self.get_player_data(driver, player))
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return {"team": team_name, "players": players}

    def get_player_data(self, driver, player):
        data = player.find_element(By.XPATH, "./div[@class='datos']//div//a")
        player_url = data.get_attribute("href")
        player_name = data.text
        position = player.find_element(By.XPATH, "./div[@class='info_basica']//div[@class='posicion roboto_condensed']").text
        permiso = (player.find_elements(By.XPATH,"./div[@class='datos']//div[@class='info_personal roboto']//span")[-1]).text
        value = self.open_player(driver, player_url)
        return {"name": player_name, "position": position, "permiso": permiso, "value": int(value)}

    def open_player(self, driver, url):
        driver.execute_script(f'window.open("{url}","_blank");')
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(10)
        table = driver.find_element(By.XPATH, "//table[@data-toggle='table-estadisticas-jugador']")
        rows = table.find_elements(By.XPATH, "./tbody//tr")
        value = 0
        if(len(rows) > 2):
            last_season = rows[-3]
            last_season_row = last_season.find_elements(By.TAG_NAME, "td")
            if(last_season_row[0].text == "21-22"):
                value = last_season.find_elements(By.TAG_NAME, "td")[-3].text
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        return value
