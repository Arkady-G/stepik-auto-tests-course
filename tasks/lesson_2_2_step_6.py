from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)


def response(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    button_1 = browser.find_element_by_tag_name('button').click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    el_x = browser.find_element_by_id('input_value').text
    x = str(math.log(abs(12 * math.sin(int(el_x)))))

    input_1 = browser.find_element_by_tag_name('input').send_keys(x)
    input_2 = browser.find_element_by_tag_name('button').click()

    response(browser)

finally:
    browser.quit()
