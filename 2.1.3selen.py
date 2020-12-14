from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    x_element = browser.find_element_by_id("treasure")
    x_checked = x_element.get_attribute("valuex")
    y = calc(x_checked)

    print("value of treasure: ", x_checked)

    input = browser.find_element_by_id("answer").send_keys(y)

    #click_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    #click_radiobutton = browser.find_element_by_id("robotsRule").click()
    #button =  browser.find_element_by_css_selector("button.btn").click()

    for selector in ('#robotCheckbox', '#robotsRule', '.btn'):
        browser.find_element(By.CSS_SELECTOR, selector).click()

    alert = browser.switch_to_alert() #скопировать текст высплывающего окна
    print(alert.text)


finally:
    time.sleep(10) # успеваем скопировать код за 30 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
