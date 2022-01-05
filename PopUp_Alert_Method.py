import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

'''Alert Method'''


def alert(element, choose):
    element.click()
    if choose == "accept":
        popup_alert = driver.switch_to.alert
        popup_alert.accept()
        time.sleep(2)

    else:
        popup_alert = driver.switch_to.alert
        popup_alert.dismiss()
        time.sleep(2)


def alert_with_value(element, choose, value):
    element.click()
    if choose == "accept":
        popup_alert = driver.switch_to.alert
        popup_alert.send_keys(value)
        popup_alert.accept()
        time.sleep(2)

    else:
        popup_alert = driver.switch_to.alert
        popup_alert.dismiss()
        time.sleep(2)


alert_button_1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
# alert(alert_button_1, 'accept')

alert_with_value(alert_button_1, 'accept', "Pop Up Value")
driver.close()
