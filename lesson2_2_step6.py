from math import *
from selenium import webdriver
import time


def ln(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value')
    ans_x = int(x.text)
    answer_x = ln(ans_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(answer_x)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
