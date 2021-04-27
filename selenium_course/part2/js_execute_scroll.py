from selenium import webdriver
import time
import math


def calc(integer_from_site: str) -> str:
    return str(math.log(abs(12*math.sin(int(integer_from_site)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x = browser.find_element_by_id('input_value').text

    # scroll on 100px
    browser.execute_script("window.scrollBy(0, 100);")

    # находим элемент и скроллим до него
    answer = browser.find_element_by_id('answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(calc(x))

    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
    robotsRule.click()

    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
