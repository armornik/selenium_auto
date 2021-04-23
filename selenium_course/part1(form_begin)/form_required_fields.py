# from selenium import webdriver
# import time

# try:
#     # Working link
#     # link = "http://suninjuly.github.io/registration1.html"
#
#     # Not working link for check
#     link = "http://suninjuly.github.io/registration2.html"
#
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Kод, который заполняет обязательные поля
#     input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
#     input1.send_keys("Kolya")
#     input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
#     input2.send_keys("Nikolya")
#     input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#     input3.send_keys("Nikolya@mail.ru")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     first_name = browser.find_element_by_css_selector('input.form-control.first:required')
#     first_name.send_keys('test')
#     last_name = browser.find_element_by_css_selector('input.form-control.second:required')
#     last_name.send_keys('test')
#     email = browser.find_element_by_css_selector('input.form-control.third:required')
#     email.send_keys('test@test.com')
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(2)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

from selenium import webdriver
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block input.first')
    input1.send_keys('Answer')
    input2 = browser.find_element_by_css_selector('.first_block input.second')
    input2.send_keys('Answer')
    input3 = browser.find_element_by_css_selector('.first_block input.third')
    input3.send_keys('Answer')

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(3)
    browser.quit()
