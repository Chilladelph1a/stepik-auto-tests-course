import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import math


def f(ans):
    return str(math.log(abs(12 * math.sin(ans))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')
anwIn = browser.find_element(By.XPATH, '//*[@id="answer"]')
answerInput = browser.find_element(By.XPATH, '//*[@id="treasure"]')
answerText = int(answerInput.get_attribute('valuex'))
x = f(answerText)
print(answerText)
print(x)
anwIn.send_keys(x)
checkBox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
checkBox.click()
radioButton = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
radioButton.click()
submitButton = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
submitButton.click()

time.sleep(7)
browser.quit()
