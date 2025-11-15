import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()
    el_x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
    y = calc(el_x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "lastname")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.NAME, "email")
    # input3.send_keys("IPetrov@mail.ru")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    # fileInput = browser.find_element(By.CSS_SELECTOR, 'input[id="file"]')
    # fileInput.send_keys(file_path)
    # button = browser.find_element(By.CSS_SELECTOR, "button")
    # button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()