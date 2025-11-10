import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_img = browser.find_element(By.CSS_SELECTOR, 'img')
    print(x_img.get_attribute('valuex'))
    x = x_img.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
