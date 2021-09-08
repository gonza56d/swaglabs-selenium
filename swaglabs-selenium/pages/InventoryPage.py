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
    by_back_to_products = (By.ID, 'back-to-products')
    by_error_message = (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')

    def __init__(self, driver):
        self.driver = driver
        self.validate_page()

    def validate_page(self): 
        try:
            burger_menu = self.driver.find_element(*self.by_burger_menu).is_displayed()
            assert burger_menu is True, 'This user has been locked out'
        except:
            error_text = self.driver.find_element(*self.by_error_message).text
            assert error_text == 'Epic sadface: Sorry, this user has been locked out.'

    def validate_item(self):
        item_text = self.driver.find_element(*self.by_backpack_item).text
        self.backpack_item.click()
        large_item = self.driver.find_element(*self.by_large_item).text
        assert item_text == large_item, "Problem encountered. Item's page does not match item selected."
    
    def get_item(self):
        backpack_text = self.driver.find_element(*self.by_backpack_item).text   
        self.driver.find_element(*self.by_backpack_item)
        return backpack_text
        
    def logout(self):   
        burger_menu = self.driver.find_element(*self.by_burger_menu)
        burger_menu.click()
        self.driver.implicitly_wait(1)
        logout_button = self.driver.find_element(*self.by_logout_button)
        logout_button.click()
    
    @property
    def backpack_item(self):
        return self.driver.find_element(*self.by_backpack_item)

    @property
    def item_large_size(self):
        return self.driver.find_element(*self.by_large_item)
