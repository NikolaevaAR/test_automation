from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")
	
	elements = browser.find_elements(By.CSS_SELECTOR, ".form-group input")
	for element in elements:
		element.send_keys("test")
		
	file_input = browser.find_element(By.ID, "file")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'test.txt')
	
	file_input.send_keys(file_path)
	
	button = browser.find_element(By. TAG_NAME, "button")
	button.click()
	
finally:
	time.sleep(20)
	browser.quit()
	
	