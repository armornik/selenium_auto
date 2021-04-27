from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент и скроллим до него
    input1 = browser.find_element_by_name("firstname")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input1)
    input1.send_keys("Petya")

    # находим элемент и скроллим до него
    input2 = browser.find_element_by_name("lastname")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input2)
    input2.send_keys("Petrov")

    # находим элемент и скроллим до него
    input3 = browser.find_element_by_name("email")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input3)
    input3.send_keys("test@test.ru")

    # создаём файл, если не существует
    filename = "test.txt"
    if not os.path.exists(filename):
        open(filename, 'w').close()

    # получаем путь к директории текущего исполняемого скрипта
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # получаем путь к test.txt
    file_path = os.path.join(current_dir, filename)

    # находим элемент и скроллим до него, и отправляем файл
    input4 = browser.find_element_by_name("file")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input4)
    input4.send_keys(file_path)

    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

