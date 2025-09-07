import time
import os

from selenium.webdriver.common.by import By


class scrap_supermanager():

    def start_scrap(self, driver):
        searchUrl = "https://supermanager.acb.com/#/session/signin-email"
        driver.get(searchUrl)
        self.login(driver)
        return self.get_players_price(driver)

    def login(self, driver):
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@id='control-email']").send_keys(os.environ.get("USER_EMAIL"))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@id='control-password']").send_keys(os.environ.get("USER_PASSWORD"))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)

    def get_players_price(self, driver):
        guards = self.get_guards_import(driver)
        forwards = self.get_forwards_import(driver)
        centers = self.get_centers_import(driver)
        return sum([guards, forwards, centers], [])
    
    def get_guards_import(self, driver):
        print("Scraping Guards")
        return self.get_import(driver, "1")

    def get_forwards_import(self, driver):
        print("Scraping Forwards")
        return self.get_import(driver, "3")

    def get_centers_import(self, driver):
        print("Scraping Centers")
        return self.get_import(driver, "5")

    def get_import(self, driver, position):
        driver.execute_script(f'window.open("https://supermanager.acb.com/#/market?position={position}","_blank");')
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)
        table_rows = driver.find_elements(By.XPATH, "//div[@class='table-responsive']//table//tbody//tr")
        players = []
        for row in table_rows:
            columns = row.find_elements(By.XPATH, "./td")
            name = columns[1].find_element(By.XPATH, "./div//strong").text
            team = columns[3].find_element(By.XPATH, "./div//img").get_attribute("title")
            # Parsear el precio a entero pero tener cuidado con el punto por si lo coge como decimal
            price = columns[4].find_element(By.XPATH, "./div//span").text
            players.append({"name":name, "team":team, "position": int(position), "price": int(price.replace(" ","").replace(".", ""))})
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return players

