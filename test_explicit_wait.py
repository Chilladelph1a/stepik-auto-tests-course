import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def f(ans):
    return str(math.log(abs(12 * math.sin(ans))))


def test_explicity_wait():
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100")
    )
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()

    xValue = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    x = int(xValue)
    ansInput = browser.find_element(By.XPATH, '//*[@id="answer"]')
    ansInput.send_keys(f(x))
    submitButton = browser.find_element(By.XPATH, '//*[@id="solve"]')
    submitButton.click()
    time.sleep(3)
