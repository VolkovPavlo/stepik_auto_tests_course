from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    button1 = browser.find_element('css selector', '[type="submit"]')
    button1.click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    submit = browser.find_element("css selector",'[type="submit"]')
    submit.click()
finally:
    time.sleep(4)
    browser.quit()