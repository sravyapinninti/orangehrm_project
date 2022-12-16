from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

   #constructors
    def __init__(self,driver):
        self.driver=driver

    # locators for login page
    enter_username = (By.XPATH,"//input[@name='username']")
    enter_password = (By.XPATH,' //input[@name="password"]')
    login_button = (By.XPATH, "//button[@type='submit']")
    invalid = (By.XPATH, "//p[text()='Invalid credentials']")

    #page actions
    #to_login

    def enter_user_name(self):

        return self.driver.find_element(*LoginPage.enter_username)

    def enter_pass_word(self):

        return self.driver.find_element(*LoginPage.enter_password)

    def login_button1(self):

        return self.driver.find_element(*LoginPage.login_button)








