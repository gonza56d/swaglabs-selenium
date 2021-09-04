from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 

from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage

@given('The user may encounter a performance glitch')
def step_impl(context):
    context.driver = webdriver.Chrome(r'C:/Users/pabni/Desktop/Scripts/ProjectsSelenium/swaglabs-selenium/swaglabs-selenium/chromedriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    sleep(1)
    

#TODO one .feature file = one .py file
#TODO PEP 8: "Surround top-level function and class definitions with two blank lines."    


@When('They enter username and password')
def step_impl(context):
    context.login_page.perform_login('standard_user', 'secret_sauce')
    
    
    

    

@Then('it should immediatly take them to the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    burger_menu = context.inventory_page.validate_page()
    assert burger_menu == True, 'Performance issue detected. Please contact support'
    context.driver.quit()
    