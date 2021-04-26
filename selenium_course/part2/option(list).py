from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)

    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)

    sum_two_num = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_two_num)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
