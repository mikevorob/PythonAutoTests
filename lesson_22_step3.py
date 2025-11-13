import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, 'span[id="num1"]').text
    num2 = browser.find_element(By.CSS_SELECTOR, 'span[id="num2"]').text
    sum = int(num1) + int(num2)
    print(num1 + "+" + num2 + " = " + str(sum))
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select[id="dropdown"]'))
    select.select_by_visible_text(str(sum))
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()