from behave import Given
from selenium import webdriver

from pages.login import LoginPage


@Given('que el usuario se dirige a la pagina de SwagLabs')
def user_goes_to_swaglabs(context):
    context.driver = webdriver.Chrome(executable_path='../../binario')
    context.driver.maximize_window()
    context.driver.get('https://www.saucedemo.com/')
