import time
import math
import pytest
from selenium import webdriver

send_answer = ""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(send_answer)  # print answer after test


links_id = ("236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905")


@pytest.mark.parametrize('link', links_id)
def test_guest_should_see_login_link(browser, link):
    global send_answer
    link = f"https://stepik.org/lesson/{link}/step/1"

    browser.implicitly_wait(10)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('textarea').send_keys(answer)
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        send_answer += check_text  # save answer if check
