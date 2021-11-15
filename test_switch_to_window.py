import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def f(ans):
    return str(math.log(abs(12 * math.sin(ans))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

switchButton = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
switchButton.click()
windows = browser.window_handles
print(windows)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

xValue = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
x = int(xValue)
ansInput = browser.find_element(By.XPATH, '//*[@id="answer"]')
ansInput.send_keys(f(x))
submitButton = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
submitButton.click()

