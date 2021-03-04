from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)


def response(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    input1 = browser.find_element_by_name('firstname').send_keys('Ivan')
    input2 = browser.find_element_by_name('lastname').send_keys('Petrov')
    input3 = browser.find_element_by_name('email').send_keys('mail@mail.mail')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'file.txt'
    file_path = os.path.join(current_dir, file_name)
    file_upload = browser.find_element_by_name('file').send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn').click()

    response(browser)

finally:
    browser.quit()
