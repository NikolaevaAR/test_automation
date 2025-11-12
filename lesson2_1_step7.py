from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/get_attribute.html")
	time.sleep(5)
	
	img = browser.find_element(By.ID, "treasure")
	x = img.get_attribute("valuex")
	
	result = calc(x)
	
	input = browser.find_element(By.ID, "answer")
	input.send_keys(result)
	
	cb = browser.find_element(By.ID, "robotCheckbox")
	cb.click()
	
	rb = browser.find_element(By.ID, "robotsRule")
	rb.click()
	
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
	
finally:
	time.sleep(20)
	browser.quit()