from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# driver.get("http://automationpractice.com/index.php")
driver.get("https://phptravels.com/")
driver.maximize_window()
print("Title : "+driver.title)

act_chains = ActionChains(driver)

# dresses = driver.find_element(By.XPATH, "//a[@title='Women']")
# summer_dress = driver.find_element(By.XPATH, "//a[@title='Summer Dresses']")
# act_chains.move_to_element(dresses).move_to_element(summer_dress).click().perform()

Features = driver.find_element(By.XPATH, "//span[contains(text(),'Features')]")
Flights_Module = driver.find_element(By.XPATH, "//a[contains(text(),'Flights Module')]")

'''Process_1'''
# act_chains.move_to_element(Features).move_to_element(Flights_Module).click().perform()
'''Process_2'''
act_chains.move_to_element(Features).perform()
act_chains.move_to_element(Flights_Module).click().perform()

driver.implicitly_wait(10)
driver.close()


