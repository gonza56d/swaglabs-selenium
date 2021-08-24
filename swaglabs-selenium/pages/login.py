from selenium.webdriver.common.by import By


class LoginPage:

    by_username_field = (By.XPATH, 'askldjaklsjdas')
    by_password_field = (By.CLASS_NAME, 'tal clase')
    by_login_button = (By.ID, 'perform-login')

    def validate_page(self):
        # perform page validation
        pass

    def __init__(self, driver) -> None:
        self.driver = driver
        self.validate_page()
    
    def perform_login(self, username: str, password: str):
        self.username_field.send_keys(username)
        self.password_field.send_keys(username)
        self.login_button.click()

    @property
    def username_field(self):
        return self.driver.find_element_by(*self.by_username_field)

    @property
    def password_field(self):
        return self.driver.find_element_by(*self.by_password_field)

    @property
    def login_button(self):
        return self.driver.find_element_by(*self.by_login_button)
