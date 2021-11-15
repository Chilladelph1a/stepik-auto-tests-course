import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test_file.html')

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
name.send_keys('Bagdaulet')
lastName = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
lastName.send_keys('Aizhanov')
email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
email.send_keys('baga')
fileinput = browser.find_element(By.XPATH, '//*[@id="file"]')
fileinput.send_keys(file_path)

submitButton = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
submitButton.click()