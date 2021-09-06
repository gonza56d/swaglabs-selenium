from behave import *
from selenium import webdriver
from time import sleep

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage


@Given('The user logs in')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    sleep(1)
    context.login_page.perform_login('standard_user', 'secret_sauce')

@Given('is in the inventory page')
def validates_inventory_page(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.validate_page()
    
@When('they select an item')
def selects_an_item(context):
    context.driver.find_element(*context.inventory_page.by_backpack_item)
    
@Then("it should take them to the item's page")
def validates_item_page(context):
    context.inventory_page.validate_item()
    context.driver.quit()
   