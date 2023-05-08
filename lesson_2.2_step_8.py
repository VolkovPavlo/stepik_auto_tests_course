from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Pavlo')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Volkov')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('@')
    # 1
    directory = '/Users/pavelvolkov/Desktop/'
    file_name = 'Shopping_List.txt'
    file_path = os.path.join(directory, file_name)
    # 2
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_name = 'file_example.txt'
    # file_path = os.path.join(current_dir, file_name)
    send_file = browser.find_element(By.NAME, 'file')
    send_file.send_keys(file_path)
    button = browser.find_element('css selector', '[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

