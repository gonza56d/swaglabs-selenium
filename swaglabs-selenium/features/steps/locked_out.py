from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from pages.LoginPage import LoginPage


@Given('The user gets to the login page')
def get_to_login_page(context):
    context.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    sleep(1)

@When('It enters username and password')
def log_in(context):
    context.login_page.perform_login('locked_out_user', 'secret_sauce')
    
@Then('An error message should appear')
def finds_error(context):
    error_text = context.login_page.locked_out_message()
    assert error_text =='Epic sadface: Sorry, this user has been locked out.'
    context.driver.quit()
  