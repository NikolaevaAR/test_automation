from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # elements = browser.find_elements(By.CSS_SELECTOR, "[required]")
    # for element in elements:
        # element.send_keys("test")
        
    first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    first_name.send_keys("Ivan")
        
    last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    email.send_keys("test@mail.ru")
        
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    time.sleep(6)
    t = browser.find_element(By.TAG_NAME, "h1")
    
    welcome_text = t.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "не проходит" 
    
finally:
    time.sleep(10)
    browser.quit