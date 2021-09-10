from selenium.webdriver.common.by import By

#TODO same PEP 8 observations
class LoginPage(object):

    by_username_field = (By.ID, 'user-name')
    by_password_field = (By.ID, 'password')
    by_login_button = (By.ID, 'login-button')
    by_login_robot = (By.CLASS_NAME, 'bot_column')
    by_error_message = (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')
    
    by_a = (By.ID, 'mock')
    by_b = (By.ID, 'mock')
    by_c = (By.ID, 'mock')

    def run_validations(self):
        self.validate_a()
        self.valudate_b()
        self.validate_c()
    
    def validate_a(self):
        text = 'a'
        a_text = self.driver.find_element(*self.by_a).text
        if text != a_text:
            raise ValueError("'A' text was not the expected")
    
    def validate_b(self):
        text = 'b'
        b_text = self.driver.find_element(*self.by_b).text
        if text != b_text:
            raise ValueError("'B' text was not the expected")

    def validate_c(self):
        text = 'c'
        c_text = self.driver.find_element(*self.by_c).text
        if text != c_text:
            raise ValueError("'C' text was not the expected")

    def validate_b(self):
        pass

    def validate_c(self):
        pass

    def validate_page(self): 
        login_robot  = self.driver.find_element(*self.by_login_robot).is_displayed()
        assert login_robot is True

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

    @property
    def username_field(self):
        return self.driver.find_element(*self.by_username_field)

    @property
    def password_field(self):
        return self.driver.find_element(*self.by_password_field)

    @property
    def login_button(self):
        return self.driver.find_element(*self.by_login_button)
