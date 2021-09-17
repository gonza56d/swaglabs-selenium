from selenium.webdriver.common.by import By


class LoginPage(object):

    by_username_field = (By.ID, 'user-name')
    by_password_field = (By.ID, 'password')
    by_login_button = (By.ID, 'login-button')
    by_login_robot = (By.CLASS_NAME, 'bot_column')
    by_burger_menu = (By.ID, 'react-burger-menu-btn')
    by_error_message = (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')
    

    def validate_page(self): 
        login_robot  = self.driver.find_element(*self.by_login_button).is_displayed()
        return login_robot
        

    def open(self, url : str):
        self.driver.get(url)

    def __init__(self, driver) -> None:
        self.driver = driver

    def perform_login(self, username: str, password: str):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()


    def locked_out_message(self):
        error_text = self.driver.find_element(*self.by_error_message).text
        return error_text
    
    def clicks_item(self, item):
        self.driver.find_element(*item).click()

    def check(self, item):
        item = self.driver.find_element(*item).is_displayed()  
        return item    

    @property
    def username_field(self):
        return self.driver.find_element(*self.by_username_field)

    @property
    def password_field(self):
        return self.driver.find_element(*self.by_password_field)

    @property
    def login_button(self):
        return self.driver.find_element(*self.by_login_button)
