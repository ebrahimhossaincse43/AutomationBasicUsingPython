import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

'''Full Page Screen Shot Method'''


def screenshot_full_page(choose, screenshotName):
    if choose == "full":
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.set_window_size(S('Width'), S('Height'))
        n = random.randint(0, 22)
        driver.find_element(By.TAG_NAME, 'body').screenshot("Screenshot/"+screenshotName)
    elif choose == "current":
        driver.get_screenshot_as_file('Screenshot/'+screenshotName)
    else:
        print("Something went ")


screenshot_full_page("current", "sc_02.png")
driver.close()
