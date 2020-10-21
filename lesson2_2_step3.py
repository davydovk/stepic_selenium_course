from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id('num1')
    num_number1 = number1.text
    number2 = browser.find_element_by_id('num2')
    num_number2 = number2.text
    sum_numbers = int(num_number1) + int(num_number2)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(sum_numbers))

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
