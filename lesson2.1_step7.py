from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input_y = browser.find_element(By.ID, 'answer')
    input_y.send_keys(str(y))
    cb = browser.find_element(By.ID, 'robotCheckbox')
    cb.click()
    rr = browser.find_element(By.ID, 'robotsRule')
    rr.click()
    sub = browser.find_element(By.CLASS_NAME, 'btn-default')
    sub.click()
    
finally:
    time.sleep(10)
    browser.quit()