from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    button1 = browser.find_element_by_class_name('btn.btn-primary').click()
    confirm = browser.switch_to.alert.accept()  #для отказа на всплывающих окнах .dismiss()

    x_element = browser.find_element_by_id("input_value").text
    y = calc(int(x_element))
    print("input value: ", x_element)

    input = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to_alert()  # скопировать текст высплывающего окна
    print(alert.text)

finally:
    time.sleep(2) # успеваем скопировать код за 2 секунд
    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
