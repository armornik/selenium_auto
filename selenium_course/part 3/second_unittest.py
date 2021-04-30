import unittest
from selenium import webdriver
import time


def text_from_link(link: str) -> str:
    # Working link
    # link = "http://suninjuly.github.io/registration1.html"

    # Not working link for check
    # link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Kод, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Kolya")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Nikolya")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("Nikolya@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text


class TestAbs(unittest.TestCase):
    def test_link1(self):
        welcome_text = text_from_link("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "registration is failed")

    def test_link2(self):
        welcome_text = text_from_link("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "registration is failed")


if __name__ == "__main__":
    unittest.main()
