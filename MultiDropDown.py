import time

from WebDriver_CrossBrowser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()

"""XPATH"""
multiSelection = driver.find_element(By.ID, 'justAnInputBox')
dropList = driver.find_elements(By.XPATH, "//span[@class='comboTreeItemTitle']")

"""Methods"""


def select_values_from_dropdown(optionsList, values):
    if not values[0] == 'all':
        for element in optionsList:
            for selectValues in range(len(values)):
                if element.text == values[selectValues]:
                    element.click()
                    break
    else:
        try:
            for element in optionsList:
                element.click()
        except Exception as e:
            print(e)


"""ACTIONS"""
multiSelection.click()
# values = ['choice 1', 'choice 2', 'choice 2 2', 'choice 4']
values = ['all']
select_values_from_dropdown(dropList, values)
time.sleep(2)
driver.quit()
