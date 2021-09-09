from behave import *
from selenium import webdriver
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage


@Given('the user is in the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')

@When('the user logs in with {username} and {password}')
def step_impl(context, username, password):
    context.login_page.perform_login(username, password)

@When('reaches the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.validate_page()
    
    
@When('selects an item')
def step_impl(context):
    context.item = context.inventory_page.get_item()

@Then("it should take them to the item's page")
def step_impl(context):
    context.inventory_page.validate_item()

@Then('come back to the inventory page')
def step_impl(context):
    context.driver.find_element(*context.inventory_page.by_back_to_products).click()
    context.inventory_page.validate_page()

@Then('log out')
def step_impl(context):
    context.inventory_page.logout()
    context.driver.quit()
    