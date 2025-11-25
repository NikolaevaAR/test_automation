from selenium.webdriver.common.by import By
import time

def test_the_product_page_contains_an_add_to_cart_button (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_add_card = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button_add_card) > 0, "Button not found"