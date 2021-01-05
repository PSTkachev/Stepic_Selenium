import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_enable_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    basket_button = browser.find_element_by_class_name('btn-add-to-basket')
    assert basket_button is not None, "basket_button is not found"

#pytest -v --tb=line --reruns 0 --language=ru test_conftest.py
