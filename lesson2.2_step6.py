from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    res = calc(x)
    input_res = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_res)
    input_res.send_keys(str(res))
    cb = browser.find_element(By.ID, 'robotCheckbox')
    cb.click()
    rr = browser.find_element(By.ID, 'robotsRule')
    rr.click()
    sub = browser.find_element(By.CLASS_NAME, 'btn')
    sub.click()    
 
finally:
    time.sleep(10)
    browser.quit()