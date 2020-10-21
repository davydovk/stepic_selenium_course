from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/cats.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id('button')
    button.click()

finally:
    browser.quit()
