import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from const import messenger_link, username_input_xpath, password_input_xpath, login_button_xpath


class MessengerBomb:
    def __init__(self):
        self.driver = webdriver.Chrome(os.path.join('bin', 'chromedriver.exe'))

    def login(self, username, password):
        self.driver.get(messenger_link)
        self.driver.implicitly_wait(10)
        username_elem = self.driver.find_element_by_xpath(username_input_xpath)
        password_elem = self.driver.find_element_by_xpath(password_input_xpath)
        username_elem.send_keys(username)
        password_elem.send_keys(password)

        login_button = self.driver.find_element_by_xpath(login_button_xpath)
        login_button.click()

    def send_message(self, message):
        actions = ActionChains(self.driver)
        actions.send_keys(message, Keys.RETURN)
        actions.perform()

    def start(self):
        username = input('請輸入帳號：')
        password = input('請輸入密碼：')
        self.login(username, password)
        user_id = input('請輸入你要傳送的使用者 id：')
        message = input('請輸入重複傳送的訊息：')
        self.driver.get(messenger_link + '/t/' + user_id)
        while True:
            self.send_message(message)


if __name__ == '__main__':
    app = MessengerBomb()
    app.start()
