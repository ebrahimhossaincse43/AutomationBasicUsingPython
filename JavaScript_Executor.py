import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].click();", best_sellers)

title = driver.execute_script("return document.title;")
print(title)

driver.execute_script("history.go(0);")
innerText = driver.execute_script("return document.documentElement.innerText;")
print(innerText)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


