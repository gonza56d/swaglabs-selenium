from selenium import webdriver
import platform
from resources.exceptions import InvalidBrowser, SystemValueError


def before_all(context):
    context.system = platform.system()


def before_feature(context, feature):
    context.browser = input('Please choose a browser to run the features, Opera or Chrome: ')
    if context.browser == 'Chrome':
        if context.system == 'Windows':
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/windows_chromedriver.exe')
            context.driver.maximize_window()
        elif context.system == 'Linux':
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/linux_chromedriver.exe')
            context.driver.maximize_window()
        elif context.system == 'Darwin':
            context.driver = webdriver.Chrome(executable_path=r'../drivers/Chrome/mac_chromedriver.exe')
        else:
            raise SystemValueError('platform.system() returned an invalid value.')

    elif context.browser == 'Opera':
        if context.system == 'Windows':
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/windows_opera_driver.exe')
            context.driver.maximize_window()
        elif context.system == 'Linux':
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/linux_opera_driver.exe')
            context.driver.maximize_window()
        elif context.system == 'Darwin':
            context.driver = webdriver.Opera(executable_path=r'../drivers/Opera/mac_opera_driver.exe')
            context.driver.maximize_window()
        else:
            raise SystemValueError('platform.system() returned an invalid value.')
    else:
        raise InvalidBrowser('Browser is not available or answer given is invalid.')


def after_feature(context, feature):
    context.driver.quit()
# need to check platforms
