from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.XPATH, '// *[@type="checkbox"]')
    checkbox.click()
    radio = browser.find_element("css selector", '[for="robotsRule"]')
    radio.click()
    submit = browser.find_element("css selector",'[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()