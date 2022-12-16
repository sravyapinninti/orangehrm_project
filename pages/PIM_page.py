from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class PIM_MODULE(BasePage):

    def __init__(self,driver):

        self.driver=driver

    #locators in PIM page
    click_pim = (By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']")

    add_button = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    firstname = (By.XPATH,"//input[@name='firstName']")

    middlename = (By.XPATH,"//input[@name='middleName']")

    lastname=(By.XPATH,"//input[@name='lastName']")

    employee_id = (By.XPATH,"//label[text()='Employee Id']/following::div[1]/input")

    save = (By.XPATH,"// button[ @ type = 'submit']")

    nickname = (By.XPATH,"//label[text()='Nickname']/following::div[1]/input")

    edit_employeemiddlename=(By.XPATH,"//input[@name='middleName']")

    search_employeename=(By.XPATH,"//input[@placeholder='Type for hints...']")

    submit=(By.XPATH,"//button[@type='submit']")

    delete_employeedetails=(By.XPATH,"//div[text()='sravya pinninti']")

    delete_button=(By.XPATH,"//button[@type='button']/following::i[@class='oxd-icon bi-trash']")

    confirmdelete=(By.XPATH,"//button[text()=' Yes, Delete ']")

    #page actions to add employee details
    def click_PIM(self):

        pim_button=self.driver.find_element(*PIM_MODULE.click_pim)
        pim_button.click()

    def add_button1(self):

        add_click=self.driver.find_element(*PIM_MODULE.add_button)
        add_click.click()

    def employee_details_firstname(self):

        return self.driver.find_element(*PIM_MODULE.firstname)

    def employee_details_middlename(self):

        return self.driver.find_element(*PIM_MODULE.middlename)

    def employee_details_lastname(self):

        return self.driver.find_element(*PIM_MODULE.lastname)

    def employee_details_employeeid(self):

        return self.driver.find_element(*PIM_MODULE.employee_id)

    def save_button(self):

        return self.driver.find_element(*PIM_MODULE.save)

    def nick_name(self):

        return self.driver.find_element(*PIM_MODULE.nickname)

    #page actions to edit and update employee details

    def edit_employee_middlename(self):

        return self.driver.find_element(*PIM_MODULE.edit_employeemiddlename)

    def search_employee_name(self):

        return self.driver.find_element(*PIM_MODULE.search_employeename)

    def submit_button(self):

        return self.driver.find_element(*PIM_MODULE.submit)

    #page actions to delete employee details

    def delete_employee_details(self):

        return self.driver.find_element(*PIM_MODULE.delete_employeedetails)

    def deletebutton(self):

        return self.driver.find_element(*PIM_MODULE.delete_button)

    def confirm_delete(self):

        return self.driver.find_element(*PIM_MODULE.confirmdelete)







