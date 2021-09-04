from behave import *
from selenium import webdriver
from time import sleep

from resources.users import StandardUser
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage



@Given('The user is in the login page')
def user_gets_to_login_page(context):
    #TODO chromedriver is not being tracked by git
    #use relative path OR use pathlib/os.dir in order to make webdriver work in any computer
    context.driver = webdriver.Chrome(r'C:/Users/pabni/Desktop/Scripts/ProjectsSelenium/swaglabs-selenium/swaglabs-selenium/chromedriver.exe')
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    sleep(1)
    

@When('The user enters username and password')
def logs_in(context):
    context.login_page.perform_login('standard_user', 'secret_sauce')
    sleep(1)
    
    
#TODO one .feature file = one .py file
#TODO PEP 8: "Surround top-level function and class definitions with two blank lines."    

@Then('It takes the user to the inventory page')
def validates_invetory_page(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.validate_page()
    sleep(2)
    context.inventory_page.logout()
    context.driver.quit()
    
    
    
    






