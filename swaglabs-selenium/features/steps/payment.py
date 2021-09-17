from behave import *


@When('user fills the payment with the code {QR}')
def step_imp(context):
    data = context.payment_page.get_page_data()
