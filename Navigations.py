import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()


def navigation_select(element, value):
    element.click()
    time.sleep(1)
    if value == "back":
        driver.back()
        time.sleep(1)
    elif value == "forward":
        driver.forward()
        time.sleep(1)
    elif value == "refresh":
        driver.refresh()
        time.sleep(1)
    else:
        print("Invalid Navigation Command")


element = driver.find_element(By.XPATH, "//a[contains(text(),'Mobiles')]")
navigation_select(element, "refresh")
driver.close()
