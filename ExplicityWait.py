import time

from selenium.webdriver.support.wait import WebDriverWait

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.title)

wait = WebDriverWait(driver, 10)

element = wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]")))
element.click()
driver.close()
