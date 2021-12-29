import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)

"""XPATH"""
userName = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_subdomain']")
name = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Name']")
email = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Email']")
phoneNumber = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Contact']")

"""ACTIONS"""
userName.send_keys("ZSS")
name.send_keys("Test")
email.send_keys("abc@gmail.com")
phoneNumber.send_keys("+8801710899336")

"""DROP_DOWN Method"""


def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


country = driver.find_element(By.XPATH, "//select[@id='Form_submitForm_Country']")
# select = Select(country)
# select.select_by_visible_text("Bangladesh")
# select.select_by_value("Bangladesh")
# select_values(country, "Bangladesh")


driver.close()
