from selenium import webdriver

"""
С помощью метода execute_script можно выполнить программу, написанную на языке JavaScript, как часть сценария 
автотеста в запущенном браузере. 

"""

# Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария:
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

# Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой:
browser.execute_script("document.title='Script executing';alert('Robots at work');")
