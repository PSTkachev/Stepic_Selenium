from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    #поиск кнопки через css
    #button = browser.find_element_by_css_selector("button.btn")
    #x-path
    browser.find_element_by_xpath("// button[text() = 'Submit']").click()
""" решения других чуваков
    # Решение №1 (тривиальное)
    buttons = driver.find_elements_by_xpath("//button[text()='Submit']")

    # решение № 2
    buttons = driver.find_elements_by_xpath("//button")
    for button in buttons:
        if button.text == 'Submit':
            button.click()
"""
finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
