from behave import *
from selenium import webdriver
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from resources.exceptions import PageValidationError, ItemValidationError


@Given('the user is in the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open('https://www.saucedemo.com')
    login_robot = context.login_page.validate_page()
    if not login_robot:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')


@When('the user logs in with {username} and {password}')
def step_impl(context, username, password):
    context.login_page.perform_login(username, password)


@When('reaches the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    burger_menu = context.inventory_page.validate_page()
    if not burger_menu:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')


@Then('log out')
def step_impl(context):
    context.inventory_page.logout()
    login_robot = context.login_page.validate_page()
    if not login_robot:
        raise PageValidationError('Unable to validate the page by presence of element being searched.')
    