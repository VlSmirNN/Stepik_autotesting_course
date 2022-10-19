import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Vlad')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Smir')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('dl@ru') 
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    
    sub = browser.find_element(By.CLASS_NAME, 'btn')
    sub.click()
    
finally:
    time.sleep(10)
    browser.quit()    