import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    locator = (By.CSS_SELECTOR, 'h5[id="price"]')
    expected_text = "100"
    condition = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(locator, expected_text)
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    el_x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
    y = calc(el_x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button2.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()