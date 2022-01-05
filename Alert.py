import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

'''Alert : Accept'''
alert_button_1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
alert_button_1.click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
print("Popup Accept Successful")

'''Alert : Dismiss'''
alert_button_2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
alert_button_2.click()
time.sleep(2)
alert = driver.switch_to.alert
alert.dismiss()
print("Popup Dismiss Successful")

'''Alert: Send Values'''
alert_button_3 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
alert_button_3.click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("something")
alert.accept()
time.sleep(2)
print("Popup Value Sending Successful")

driver.close()