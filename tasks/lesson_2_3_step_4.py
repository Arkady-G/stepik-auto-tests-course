from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)


def response(remote: webdriver.Remote):
    alert2 = remote.switch_to.alert
    print(alert2.text.split()[-1])
    alert2.accept()


try:
    button1 = browser.find_element_by_tag_name('button').click()
    alert1 = browser.switch_to.alert
    alert1.accept()

    el_x = browser.find_element_by_id('input_value').text
    x = str(math.log(abs(12 * math.sin(int(el_x)))))

    input1 = browser.find_element_by_tag_name('input').send_keys(x)
    button2 = browser.find_element_by_class_name('btn').click()

    response(browser)

finally:
    browser.quit()
