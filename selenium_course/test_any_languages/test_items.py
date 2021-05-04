import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "http://suninjuly.github.io/simple_form_find_task.html" # Link Button not found


def test_present_button_basket(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "Button not found"
    time.sleep(30)
