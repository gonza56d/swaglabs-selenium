from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path = r'../chromedriver.exe')
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()