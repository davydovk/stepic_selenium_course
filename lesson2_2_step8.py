from selenium import webdriver
import time
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Konstantin')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Davydov')
    email = browser.find_element_by_name('email')
    email.send_keys('davydov@rosenergo.com')
    review = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    review.send_keys(file_path)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
