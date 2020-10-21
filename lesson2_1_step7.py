from selenium import webdriver
import time
from math import *


def ln(x):
    return str(log(abs(12*sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_xpath("//img[@src='images/chest.png']")
    x = int(chest.get_attribute('valuex'))
    answer_x = ln(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(answer_x)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
