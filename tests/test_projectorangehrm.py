import pytest
from pages.login import LoginPage
from pages.basepage import BasePage
from pages.PIM_page import PIM_MODULE
import time
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('init_driver')
class Test_Login(BasePage):

    def test_login(self):

        #initiating logging
        log=self.logger()
        #importing from login.py and initialising driver
        login=LoginPage(self.driver)
        #verifiying element's visibility
        self.element_located("//input[@name='username']")
        #creating variable to do actions
        username=login.enter_user_name()
        #log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        #verifiying element's visibility
        self.element_located('//input[@name="password"]')
        password=login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_located= ("//button[@type='submit']")
        login_click=login.login_button1()
        login_click.click()
        log.info("logged in successfully")


@pytest.mark.usefixtures('init_driver')
class Test_failedLogin(BasePage):

    def test_login_invalid(self):

        message="Invalid credentials"
        log=self.logger()
        login=LoginPage(self.driver)
        self.element_located("//input[@name='username']")
        username=login.enter_user_name()
        log.info("username entered")
        username.send_keys("Admin")
        self.element_located('//input[@name="password"]')
        password=login.enter_pass_word()
        password.send_keys("invalid password")
        log.info("password entered")
        self.element_located ("//button[@type='submit']")
        login_click=login.login_button1()
        login_click.click()
        log.info(self.element_located("//p[text()='Invalid credentials']"))

        #log.info("unsuccessful login....please enter valid credentials")
        assert self.element_located("//p[text()='Invalid credentials']") == message


@pytest.mark.usefixtures('init_driver')
class Test_add_employeedetails(BasePage):

    def test_employee_details(self):

        message="successfully saved"
        log = self.logger()
        login = LoginPage(self.driver)
        self.element_located("//input[@name='username']")
        username = login.enter_user_name()
        username.send_keys("Admin")
        log.info("username entered")
        self.element_located('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_located = ("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")
        pim=PIM_MODULE(self.driver)
        self.element_located=("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button=pim.click_PIM()
        log.info("entering into PIM page")
        self.element_located=("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        add_button=pim.add_button1()
        log.info("clicked add button")
        self.element_located=("//input[@name='firstName']")
        first_name=pim.employee_details_firstname()
        first_name.send_keys("sravya")
        log.info("first name is sravya")
        self.element_located=("//input[@name='middleName']")
        middle_name=pim.employee_details_middlename()
        middle_name.send_keys("pinninti")
        log.info("middlename is pinninti")
        self.element_located=("//input[@name='lastName']")
        last_name=pim.employee_details_lastname()
        last_name.send_keys("pappula")
        log.info("last name is pappula")
        self.element_located=("//label[text()='Employee Id']/following::div[1]/input")
        employeeid=pim.employee_details_employeeid()
        #employeeid.send_keys(Keys.CONTROL,"a",Keys.BACKSPACE)
        log.info("employee id is auto-generated")
        employeeid.send_keys(Keys.ENTER)
        self.element_located=('//p[text()="Successfully Saved"]')
        log.info("employee details saved successfully")
        #assert self.element_located('//p[text()="Successfully Saved"]') == message



@pytest.mark.usefixtures('init_driver')
class Test_edit_employee_details(BasePage):

    def test_edit_employee_details(self):

        message="Successfully Updated"
        log = self.logger()
        login = LoginPage(self.driver)
        self.element_located("//input[@name='username']")
        username = login.enter_user_name()
        username.send_keys("Admin")
        log.info("username entered")
        self.element_located('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_located = ("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")
        pim = PIM_MODULE(self.driver)
        self.element_located = ("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_located = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        add_button = pim.add_button1()
        log.info("clicked add button")
        self.element_located = ("//input[@name='firstName']")
        first_name = pim.employee_details_firstname()
        first_name.send_keys("sravya")
        log.info("first name is sravya")
        self.element_located = ("//input[@name='middleName']")
        middle_name = pim.employee_details_middlename()
        middle_name.send_keys("pinninti")
        log.info("middlename is pinninti")
        self.element_located = ("//input[@name='lastName']")
        last_name = pim.employee_details_lastname()
        last_name.send_keys("pappula")
        log.info("last name is pappula")
        time.sleep(15)
        self.element_located = ("//label[text()='Employee Id']/following::div[1]/input")
        employeeid = pim.employee_details_employeeid()
        #employeeid.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        #employeeid.send_keys("2357")
        log.info("employee id is auto-generated")
        employeeid.send_keys(Keys.ENTER)
        self.element_located = ("//p[text()='Successfully Saved']")
        log.info("employee details saved successfully")
        #editing employeename
        self.element_located=("//input[@name='middleName']")
        edit_middlename=pim.edit_employee_middlename()
        edit_middlename.send_keys("Kumar")
        log.info("employee middle name is edited")
        edit_middlename.send_keys(Keys.ENTER)
        self.element_located=("//p[text()='Successfully Updated']")
        log.info("updated successfully")
        #assert self.element_located("//p[text()='Successfully Updated']") == message


@pytest.mark.usefixtures('init_driver')
class Test_delete_employee_details(BasePage):

    def test_delete_employee_details(self):
        log = self.logger()
        login = LoginPage(self.driver)
        self.element_located("//input[@name='username']")
        username = login.enter_user_name()
        username.send_keys("Admin")
        log.info("username entered")
        self.element_located('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_located = ("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")
        pim=PIM_MODULE(self.driver)
        self.element_located = ("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")

        #delete_employeedata
        self.element_located=("//input[@placeholder='Type for hints...']")
        search_name=pim.search_employee_name()
        search_name.send_keys("sravya pinninti pappula")
        log.info("found required employee")
        self.element_located=("//button[@type='submit']")
        submit=pim.submit_button()
        submit.click()
        self.element_located=("//div[text()='sravya pinninti']")
        delete_employeedata=pim.delete_employee_details()
        log.info("found data")
        self.element_located=("//button[@type='button']/following::i[@class='oxd-icon bi-trash']")
        delete=pim.deletebutton()
        delete.click()
        self.element_located=("//button[text()=' Yes, Delete ']")
        confirm=pim.confirm_delete()
        confirm.click()
        self.element_located=("//p[text()='Successfully Deleted']")
        log.info("succsessfully deleted")




















