import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_add_to_basket = browser.find_elements_by_class_name('btn-add-to-basket')
    assert button_add_to_basket, f'Страница товара на сайте {link} не содержит кнопки добавления в корзину'
