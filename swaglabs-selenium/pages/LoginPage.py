from selenium.webdriver.common.by import By

#TODO same PEP 8 observations
class LoginPage(object):

    by_username_field = (By.ID, 'user-name')
    by_password_field = (By.ID, 'password')
    by_login_button = (By.ID, 'login-button')
    by_login_robot = (By.CLASS_NAME, 'bot_column')
    by_error_message = (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')
    

    def validate_page(self): 
        login_robot  = self.driver.find_element(*self.by_login_robot).is_displayed()
        # TODO: assertions should be in the steps, pages should have
        # methods that return the values to be validated with assertions
        # but not making the assertions inside by itself.
        # (remember not to return Selenium stuff such as WebElements or Locators,
        # but their values (texts, states, etc), WebElements and Locators concern to pages only).
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
