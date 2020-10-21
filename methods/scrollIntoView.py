from selenium import webdriver


browser = webdriver.Chrome()
"""
Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть на элемент, который внезапно 
оказывается перекрыт другим элементом на странице.
Для клика в WebDriver мы используем метод click(). Если элемент оказывается перекрыт другим элементом, то наша 
программа вызовет следующую ошибку:

selenium.common.exceptions.WebDriverException: Message: unknown error: Element <button type="submit" 
class="btn btn-default" style="margin-bottom: 1000px;">...</button> is not clickable at point (87, 420). 
Other element would receive the click: <p>...</p>

Из описания ошибки можно понять, что указанный нами элемент нельзя кликнуть в данной точке, т.к. клик произойдёт 
на другом элементе с тегом <p>.

Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскролить нужный элемент, чтобы он 
точно стал видимым. Делается это с помощью следующего скрипта:

"return arguments[0].scrollIntoView(true);"
"""

# В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# Также можно проскролить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")
