from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from math import *


def ln(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_id('book')
    book.click()

    x = browser.find_element_by_id('input_value')
    ans_x = int(x.text)
    answer_x = ln(ans_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(answer_x)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
