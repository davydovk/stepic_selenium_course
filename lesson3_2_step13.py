import unittest
from selenium import webdriver
import time


class TestRegistrationForm(unittest.TestCase):
    def test_form1(self):
        self.browser = webdriver.Chrome()
        self.link = 'http://suninjuly.github.io/registration1.html'
        self.browser.get(self.link)
        self.input1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        self.input3.send_keys("ip@gmail.com")
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)
        self.browser.quit()

    def test_form2(self):
        self.browser = webdriver.Chrome()
        self.link2 = 'http://suninjuly.github.io/registration2.html'
        self.browser.get(self.link2)
        self.input1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        self.input3.send_keys("ip@gmail.com")
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
