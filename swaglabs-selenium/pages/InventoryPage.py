from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class InventoryPage(object):

    by_title = (By.CLASS_NAME, 'title')
    by_burger_menu = (By.ID, 'react-burger-menu-btn')
    by_logout_button = (By.ID, 'logout_sidebar_link')
    by_backpack_item = (By.ID, 'item_4_title_link')
    by_large_item = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')

    def __init__(self, driver):
        self.driver = driver
        self.validate_page()

    def validate_page(self): 
        burger_menu = WDW(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'react-burger-menu-btn'))).is_displayed()
        return burger_menu

    def validate_item(self):
        item_text = self.driver.find_element(*self.by_backpack_item).text
        self.backpack_item.click()
        large_item = self.driver.find_element(*self.by_large_item).text
        assert item_text == large_item
    
    def get_item(self):
        self.backpack_item.text
        
    def logout(self):   
        burger_menu = self.driver.find_element(*self.by_burger_menu)
        sleep(1)
        burger_menu.click()
        sleep(1)
        logout_button = self.driver.find_element(*self.by_logout_button)
        logout_button.click()
    
    @property
    def backpack_item(self):
        return self.driver.find_element(*self.by_backpack_item)

    @property
    def item_large_size(self):
        return self.driver.find_element(*self.by_large_item)
