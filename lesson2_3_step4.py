from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/alert_accept.html")
	
	button1 = browser.find_element(By.TAG_NAME, "button")
	button1.click()
	time.sleep(2)
	
	alert = browser.switch_to.alert
	alert.accept()
	time.sleep(2)
	
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	result = calc(x)
	
	answer = browser.find_element(By.ID, "answer")
	answer.send_keys(result)
	
	button2 = browser.find_element(By.CLASS_NAME, "btn")
	button2.click()
	
finally:
	time.sleep(20)
	browser.quit()
	
	