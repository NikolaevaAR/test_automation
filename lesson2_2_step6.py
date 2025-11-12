from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("https://SunInJuly.github.io/execute_script.html")
	
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	result = calc(x)
	
	answer = browser.find_element(By.ID, "answer")
	answer.send_keys(result)
	
	ch = browser.find_element(By.ID, "robotCheckbox")
	ch.click()
	
	rb = browser.find_element(By.ID, "robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
	rb.click()
	
	button = browser.find_element(By.CLASS_NAME, "btn")
	button.click()
	
finally:
	time.sleep(20)
	browser.quit()
	
	
