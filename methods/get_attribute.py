from selenium import webdriver


browser = webdriver.Chrome()

# Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element_by_id("peopleRule")

# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
