import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

'''Approach_1'''
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

'''Approach_2
desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities= desired_capabilities)
'''
'''Approach_3
options = Options()
options.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
'''

driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.close()
