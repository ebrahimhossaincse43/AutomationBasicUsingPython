import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# depart_form = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
# depart_form.click()
# time.sleep(2)
#
# depart_form.send_keys("New Delhi")
# time.sleep(2)
# depart_form.send_keys(Keys.ENTER)
# time.sleep(2)

going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
going_to.click()
time.sleep(2)

going_to.send_keys("NEW")
time.sleep(2)
search_result = driver.find_element(By.XPATH, "//div[@class='viewport']//div[1]//div[1]/li")
print(search_result)

# for results in search_result:
#     print(results)
# if "New York" in results.text:
#     results.click()
#     time.sleep(4)
#     break

driver.close()
