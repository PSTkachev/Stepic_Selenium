from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer").send_keys(y)

    click_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    click_radiobutton = browser.find_element_by_id("robotsRule").click()

    button = browser.find_element_by_css_selector('[type="submit"]').click()



finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
