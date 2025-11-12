from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select 

try:
	browser = webdriver.Chrome()
	browser.get("https://suninjuly.github.io/selects2.html")
	
	num1 = browser.find_element(By.ID, "num1").text
	num2 = browser.find_element(By.ID, "num2").text
	sum = int(num1) + int(num2)
	
	select = Select(browser.find_element(By.ID, "dropdown"))
	select.select_by_value(str(sum))
	
	button = browser.find_element(By.CLASS_NAME, "btn")
	button.click()
	
finally:
	time.sleep(20)
	browser.quit()
	
	