from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element('css selector', '[type="submit"]')
    time.sleep(2)
    button.click()
    all_windows = browser.window_handles
    print(all_windows)
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
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