from selenium import webdriver
from selenium.webdriver.common.by import By
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
browser.get('http://suninjuly.github.io/execute_script.html')
xValue_text = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
xValue = int(xValue_text)
answerInput = browser.find_element(By.XPATH, '//*[@id="answer"]')
answerInput.send_keys(f(xValue))
checkBox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkBox)
checkBox.click()
radioButton = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[4]/label')
radioButton.click()
submitButton = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
submitButton.click()

time.sleep(7)
browser.quit()

