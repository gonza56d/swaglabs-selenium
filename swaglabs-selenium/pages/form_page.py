from selenium.webdriver.common.by import By

from typing import Dict


class FormPage:

    by_origin_account = (By.ID, 'origin_account')
    by_destination_account = (By.ID, 'destination_account')
    by_amount = (By.ID, 'amount')

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_page_data(self) -> Dict[str: str]:
        return {
            'origin_account': self.get_origin_account(),
            'destination_account': self.get_destination_account(),
            'amount': self.get_amount()
        }

    def get_origin_account(self):
        return self.driver.find_element(*self.by_username_field).text
    
    def get_destination_account(self):
        return self.driver.find_element(*self.by_destination_account).text
    
    def get_amount(self):
        return self.driver.find_element(*self.by_amount).text
