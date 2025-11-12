from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    button1 = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1.click()
    
    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text
    value = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    time.sleep(5)
    
finally:
    browser.quit()
    
    