from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.ID, 'num1')
    num1 = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    num2 = y_element.text
    total = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(f'{total}')
    submit = browser.find_element("css selector",'[type="submit"]')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()    