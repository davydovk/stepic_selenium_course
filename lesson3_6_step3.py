from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def answer():
    answer = math.log(int(time.time()))
    return str(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_solution(browser, answer, links):
    link = f'{links}'
    browser.get(link)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'textarea'))).send_keys(answer)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'smart-hints__hint')))
    answer = browser.find_element_by_class_name('smart-hints__hint')

    assert 'Correct!' in answer.text, f'Ожидаемый тект >>> Correct!, Текущий текст >>> {answer.text}'
