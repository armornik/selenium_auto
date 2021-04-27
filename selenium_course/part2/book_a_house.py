from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(integer_from_site: str) -> str:
    return str(math.log(abs(12*math.sin(int(integer_from_site)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = browser.find_element_by_id("book")

# говорим Selenium проверять в течение 12 секунд, пока цена дома не уменьшится до 100$
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button.click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()

answer = browser.switch_to.alert.text
print(answer.split()[-1])

browser.quit()
