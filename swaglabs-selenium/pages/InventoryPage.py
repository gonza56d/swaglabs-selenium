from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class InventoryPage(object):

    by_title = (By.CLASS_NAME, 'title')
    by_burger_menu = (By.ID, 'react-burger-menu-btn')
    by_logout_button = (By.ID, 'logout_sidebar_link')
    by_backpack_item = (By.ID, 'item_4_title_link')
    by_large_item = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    by_back_to_products = (By.ID, 'back-to-products')
    by_error_message = (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')
    by_add_to_cart_backpack_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
    by_add_to_cart_tshirt_button = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    by_add_to_cart_light_button = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    by_dropdown_list = (By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')
    by_shopping_cart = (By.ID, 'shopping_cart_container')
    by_remove_light_button = (By.ID, 'remove-sauce-labs-bike-light')
    by_checkout = (By.ID, 'checkout')
    by_first_name = (By.ID, 'first-name')
    by_last_name = (By.ID, 'last-name')
    by_postal_code = (By.ID, 'postal-code')
    by_continue = (By.ID, 'continue')
    by_item_total = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
    by_tax = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    by_total = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
    by_checkout_complete = (By.ID, 'checkout_complete_container')
    by_finish = (By.ID, 'finish')

    def __init__(self, driver):
        self.driver = driver

    def continues(self):
        self.continue_button.click()

    def fill_checkout(self):
        self.first_name_field.send_keys('Test_first_name')
        self.last_name_field.send_keys('Test_last_name')
        self.postal_code_field.send_keys('0000')

    def checkout(self):
        self.checkout_button.click()

    def removes_light(self):
        self.remove_light.click()

    def adds_tshirt(self):
        self.tshirt_button.click()

    def adds_backpack(self):
        self.backpack_button.click()

    def adds_light(self):
        self.light_button.click()

    def to_shopping_cart(self):
        self.shopping_cart.click()

    def check_shopping_cart(self):
        q_items = int(self.shopping_cart.text)
        return q_items
        
    def validate_page(self): 
        burger_menu = self.burger_menu.is_displayed()
        return burger_menu
    
    def check(self, item):
        item = self.driver.find_element(*item).is_displayed()  
        return item
    
    def clicks_item(self, item):
        self.driver.find_element(*item).click()
    
    def get_backpack_text(self):
        return self.backpack_item.text

    def selects_item(self):
        self.backpack_item.click()


    def selects_order(self):
        expected_options = ['Name (A to Z)',
                            'Name (Z to A)',
                            'Price (low to high)',
                            'Price (high to low)']

        actual_options = []

        select_order = Select(self.driver.find_element(*self.by_dropdown_list))

        for option in select_order.options:
            actual_options.append(option.text)

        if expected_options == actual_options:
            print(expected_options, "\n", actual_options)

        select_order.select_by_index(2)

    def gets_large_item_text(self):
        text = self.item_large_size.text
        return text

    def go_back_to_inventory(self):
        self.back_to_products.click()

    def logout(self):   
        burger_menu = self.driver.find_element(*self.by_burger_menu)
        burger_menu.click()
        self.driver.implicitly_wait(1)
        logout_button = self.driver.find_element(*self.by_logout_button)
        logout_button.click()

    def calculates_total(self):
        item_total = self.item_total.text
        tax = self.tax.text
        total = self.total.text
        print(f'The item total is:{item_total} \n the tax total is: {tax}\n the final total is:{total}')

    def checks_complete(self):
        complete = self.checkout_complete.is_displayed()
        return complete

    def finish_checkout(self):
        self.finish_button.click()

    @property
    def finish_button(self):
        return self.driver.find_element(*self.by_finish)
    @property
    def checkout_complete(self):
        return self.driver.find_element(*self.by_checkout_complete)
    @property
    def tax(self):
        return self.driver.find_element(*self.by_tax)

    @property
    def total(self):
        return self.driver.find_element(*self.by_total)

    @property
    def item_total(self):
        return self.driver.find_element(*self.by_item_total)
    @property
    def continue_button(self):
        return self.driver.find_element(*self.by_continue)

    @property
    def postal_code_field(self):
        return self.driver.find_element(*self.by_postal_code)
    @property
    def last_name_field(self):
        return self.driver.find_element(*self.by_last_name)
    @property
    def first_name_field(self):
        return self.driver.find_element(*self.by_first_name)

    @property
    def checkout_button(self):
        return self.driver.find_element(*self.by_checkout)

    @property
    def remove_light(self):
        return self.driver.find_element(*self.by_remove_light_button)

    @property
    def tshirt_button(self):
        return self.driver.find_element(*self.by_add_to_cart_tshirt_button)

    @property
    def backpack_button(self):
        return self.driver.find_element(*self.by_add_to_cart_backpack_button)

    @property
    def light_button(self):
        return self.driver.find_element(*self.by_add_to_cart_light_button)

    @property
    def burger_menu(self):
        return self.driver.find_element(*self.by_burger_menu)

    @property
    def backpack_item(self):
        return self.driver.find_element(*self.by_backpack_item)

    @property
    def item_large_size(self):
        return self.driver.find_element(*self.by_large_item)

    @property
    def shopping_cart(self):
        return self.driver.find_element(*self.by_shopping_cart)

    @property
    def back_to_products(self):
        return self.driver.find_element(*self.by_back_to_products)
