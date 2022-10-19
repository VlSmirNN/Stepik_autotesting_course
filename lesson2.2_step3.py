from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text 
    s = int(x) + int(y)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(s))
    
    sub = browser.find_element(By.CLASS_NAME, 'btn-default')
    sub.click()    

finally:
    time.sleep(10)
    browser.quit()