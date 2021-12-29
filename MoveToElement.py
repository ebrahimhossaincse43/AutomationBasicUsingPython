import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pyshadow.main import Shadow

driver.implicitly_wait(5)
driver.get("https://www.daraz.com.bd/")
driver.maximize_window()
time.sleep(2)

'''XPATH'''
# notInterested = driver.find_element(By.CSS_SELECTOR, 'airship-btn airship-btn-deny')
ElectronicDevices = driver.find_element(By.XPATH, "//span[contains(text(),'Electronic Devices')]")
cameras = driver.find_element(By.XPATH, "//*[contains(text(),'Cameras')]")
dslr = driver.find_element(By.XPATH, "//*[contains(text(),'DSLR')]")

shadow = Shadow(driver)
notInterested = shadow.find_element(By.XPATH, "button[class='airship-btn airship-btn-deny']")
notInterested.click()

'''ACTION_CHAIN'''
act_chains = ActionChains(driver)

act_chains.move_to_element(ElectronicDevices).perform()
act_chains.move_to_element(cameras).perform()
dslr.click()
time.sleep(2)
driver.quit()
