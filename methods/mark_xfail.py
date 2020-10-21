import pytest
from selenium import webdriver

"""
XFail: помечать тест как ожидаемо падающий

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser): 
     browser.get(link)
     browser.find_element_by_css_selector("button.favorite")
     
Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. Пока разработчики исправляют баг, 
мы хотим, чтобы результат прогона всех наших тестов был успешен, но падающий тест помечался соответствующим образом, 
чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста.

"""

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")


"""
Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно 
проходит). После этого маркировку xfail для теста можно удалить. Кстати, к маркировке xfail можно добавлять параметр 
reason. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.

Дополнительно об использовании этих меток можно почитать в документации: Skip and xfail: dealing with tests that cannot 
succeed.  Там есть много разных интересных особенностей, например, как пропускать тест только при выполнении условия, 
как сделать так, чтобы внезапно прошедший xfailed тест в отчете стал красным, и так далее. 

https://stepik.org/lesson/236918/step/5?unit=209305
https://docs.pytest.org/en/latest/skipping.html
"""
