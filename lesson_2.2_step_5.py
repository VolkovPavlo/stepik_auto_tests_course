from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(3)
button.click()


# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# time.sleep(3)
