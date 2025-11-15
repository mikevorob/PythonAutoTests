import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    el_x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
    y = calc(el_x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()