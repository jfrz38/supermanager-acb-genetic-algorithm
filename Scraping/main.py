import sys

from acb import scrap_acb
from manage_driver import manage_driver
from manage_file import manage_file
from supermanager import scrap_supermanager

sys.path.append(".")

class main:

    manage_driver = manage_driver()
    driver = None

    def __init__(self) -> None:
        self.driver = manage_driver.create_driver(manage_driver)

    def scrap_acb(self):
        try:
            acb = scrap_acb()
            data = acb.start_scrap(self.driver)
            file = manage_file()
            file.save_acb_data_players(data)
        except Exception as e:
            print(e)
        finally:
            manage_driver.close_driver(manage_driver, self.driver)
    
    def scrap_supermanager(self):
        try:
            supermangaer = scrap_supermanager()
            data = supermangaer.start_scrap(self.driver)
            file = manage_file()
            file.save_supermanager_data_players(data)
        except Exception as e:
            print(e)
        finally:
            manage_driver.close_driver(manage_driver, self.driver)

    def create_result_file(self):
        file = manage_file()
        file.merge_files()

    def create_csv_file(self):
        file = manage_file()
        file.save_data_csv()

    def create_driver(self, is_headless = True):
        return manage_driver().create_driver(self, is_headless)
      

if __name__ == '__main__':
    main().scrap_acb()
    # main().scrap_supermanager()
    main().create_result_file()
    main().create_csv_file()
