from selenium import webdriver
import platform


def before_all(context):
    context.system = platform.system()


def before_feature(context, feature):
    context.browser = input('Please choose a browser to run the features, Opera or Chrome: ')
    if context.browser == 'Chrome':
        if context.system == 'Windows':
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/windows_chromedriver.exe')
            context.driver.maximize_window()
        elif context.system == 'Darwin':
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/linux_chromedriver.exe')
            context.driver.maximize_window()
        else:
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/mac_chromedriver.exe')

    else:
        if context.system == 'Windows':
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/windows_opera_driver.exe')
            context.driver.maximize_window()
        elif context.system == 'Darwin':
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/linux_opera_driver.exe')
            context.driver.maximize_window()
        else:
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/mac_opera_driver.exe')
            context.driver.maximize_window()


def after_feature(context, feature):
    context.driver.quit()
# need to check platforms
