from selenium import webdriver
from selenium.webdriver.chrome.options import Options


WAITING_TIME = 1


def before_scenario(context, temp):
    context.chrome_options = Options()
    context.chrome_options.add_argument("--disable-extensions")
    context.chrome_options.add_argument("--disable-popup-blocking")
    context.driver = webdriver.Chrome(options=context.chrome_options)
    context.driver.maximize_window()