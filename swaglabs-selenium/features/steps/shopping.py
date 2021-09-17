from behave import *
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from resources.exceptions import *


@Given('The user has logged in with {username} and {password}')
def step_impl(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    login_robot = context.login_page.validate_page()
    if not login_robot:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')
    context.login_page.perform_login(username, password)
    context.inventory_page = InventoryPage(context.driver)
    burger_menu = context.inventory_page.validate_page()
    if not burger_menu:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')


@When('They order the price from low to high')
def step_impl(context):
    context.inventory_page.selects_order()


@When('Selects an item')
def step_impl(context):
    context.backpack_text = context.inventory_page.get_backpack_text()
    context.inventory_page.selects_item()


@When("Visits the item's page")
def step_impl(context):
    text = context.inventory_page.gets_large_item_text()
    if text != context.backpack_text:
        raise ItemValidationError("Item's page does not match item selected in the inventory page")


@When('goes back')
def step_impl(context):
    context.inventory_page.go_back_to_inventory()


@When('They add things to the shopping cart')
def step_impl(context):
    context.inventory_page.adds_tshirt()
    context.inventory_page.adds_backpack()
    context.inventory_page.adds_light()


@When('checks the shopping cart')
def step_impl(context):
    items = context.inventory_page.check_shopping_cart()
    print(items)
    if items != 3:
        raise ItemQuantityError()
    context.inventory_page.to_shopping_cart()


@When('removes an item')
def step_impl(context):
    context.inventory_page.removes_light()


@When('checks out')
def step_impl(context):
    context.inventory_page.checkout()
    context.inventory_page.fill_checkout()
    context.inventory_page.continues()


@Then('the total should match the sum of the items plus taxes')
def step_impl(context):
    total = context.inventory_page.calculates_total()
    assert total is True, 'Total does not match items total plus taxes.'
    context.inventory_page.finish_checkout()


@Then('completes the process')
def step_impl(context):
    complete = context.inventory_page.checks_complete()
    assert complete is True, 'Could not complete the process'
