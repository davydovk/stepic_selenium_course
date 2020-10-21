from selenium import webdriver
import time
from math import *


def ln(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']").click()

    new_window = browser.window_handles[1]
    print(browser.window_handles)
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value')
    ans_x = int(x.text)
    answer_x = ln(ans_x)
    answer = browser.find_element_by_id('answer').send_keys(answer_x)
    button2 = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
