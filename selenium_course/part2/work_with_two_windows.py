from selenium import webdriver
import time
import math


def calc(integer_from_site: str) -> str:
    return str(math.log(abs(12*math.sin(int(integer_from_site)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    # get name new window
    new_window = browser.window_handles[1]

    # redirect new window
    browser.switch_to.window(new_window)

    # находим элемент и скроллим до него
    x_element = browser.find_element_by_id("input_value")
    browser.execute_script('return arguments[0].scrollIntoView(true);', x_element)
    x = x_element.text

    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input1)
    input1.send_keys(y)

    button2 = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button2)
    button2.click()

    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
