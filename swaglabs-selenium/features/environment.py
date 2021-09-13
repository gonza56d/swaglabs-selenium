from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path = r'../drivers/windows_chromedriver.exe')
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()


#Before_feature check platforms
