from selenium import webdriver
import time
from math import *


def ln(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value')
    ans_x = int(x.text)
    answer_x = ln(ans_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(answer_x)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
