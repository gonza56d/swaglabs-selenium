from behave import *
from selenium import webdriver
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from resources.exceptions import PageValidationError, ItemValidationError


@Given('the user is in the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    login_robot = context.login_page.check(context.login_page.by_login_robot)
    if not login_robot:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')


@When('the user logs in with {username} and {password}')
def step_impl(context, username, password):
    context.login_page.perform_login(username, password)


@When('reaches the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    burger_menu = context.inventory_page.check(context.inventory_page.by_burger_menu)
    if not burger_menu:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')
    
    
@When('selects an item')
def step_impl(context):
    context.backpack_text = context.inventory_page.get_text_from(context.inventory_page.by_backpack_item)
    context.inventory_page.clicks_item(context.inventory_page.by_backpack_item)    


@Then("it should take them to the item's page")
def step_impl(context):
    large_text = context.inventory_page.get_text_from(context.inventory_page.by_large_item)
    if large_text != context.backpack_text:
        raise ItemValidationError("Item's page does not match item selected in the inventory page")


@Then('come back to the inventory page')
def step_impl(context):
    context.inventory_page.clicks_item(context.inventory_page.by_back_to_products)
    burger_menu = context.inventory_page.check(context.inventory_page.by_burger_menu)
    if not burger_menu:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')


@Then('log out')
def step_impl(context):
    context.inventory_page.logout()
    login_robot = context.login_page.check(context.login_page.by_login_robot)
    if not login_robot:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')
    