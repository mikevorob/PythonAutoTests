import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    el_x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
    y = calc(el_x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    option1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    option2.click()
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()