import os
import sys

from selenium import webdriver


class manage_driver:
    driver = None

    def __init__(self) -> None:
        pass

    def create_driver(self, is_headless = True):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--incognito")
        options.add_argument("--disable-dev-shm-usage")
        if is_headless:
            options.add_argument('--headless')

        DRIVER_PATH = self.get_driver_path(self)
        return webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        
    def get_driver_path(self):
        platform = sys.platform
        if platform == "linux" or platform == "linux2":
            return '/snap/bin/chromium.chromedriver'
        elif platform == "win32":
            return f'{os.path.dirname(os.path.realpath(__file__))}/chromedriver_last.exe'
        elif platform == "darwin":
            raise Exception("No disponible para MAC OS")
    
    def close_driver(self, driver):
        if(driver):
            driver.quit()
   