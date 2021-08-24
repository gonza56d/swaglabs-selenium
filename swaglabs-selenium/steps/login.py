from behave import When
from resources.users import StandardUser
from selenium import webdriver

from pages.login import LoginPage
from pages.invetory import InventoryPage


@When('el usuario ingresa su usuario y contraseña')
def user_types_username_and_password(context):
    page = LoginPage(driver=context.driver)
    page.perform_login(username=StandardUser.username, password=StandardUser.password)


@When('efectúa el login exitoso')
def successful_login_is_done(context):
    page = InventoryPage()
    assert page.is_displayed_successful()
