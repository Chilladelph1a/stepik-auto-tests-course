import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import math


def f(ans):
    return str(math.log(abs(12 * math.sin(ans))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

value1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
value2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
answer = str(str(int(value1) + int(value2)))
select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
select.select_by_value(answer)


submitButton = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
submitButton.click()

time.sleep(7)
browser.quit()
