# orangehrm_project
This project includes "Page Object Model" implementation with "pytest"
Requirements:
(i) Python
(ii) Pytest
(iii) Selenium Python Library
(iv) Webdriver for respective Web-browser
(v) Web-browser

This project has pages and tests folders 

'Pages' folder includes:
(i) Basepage.py
This page acts as parent page for all pages.
Functions created here is used in the test cases and other files.

(ii) Login.py
This page contains all elements of a login page.
It has locators which can be used to find an element using XPath,ID,NAME etc.
Using these locators,functions are created to do actions in test file.

(iii)PIM_page.py
This page contains all elements of a PIM module page.
It has locators which can be used to find an element using XPath,ID,NAME etc.
Using these locators,functions are created to do actions in test file.

'Tests' folder includes:
(i) conftest.py
This file has drivers required for test cases to run.
It initiates the test file and then closes once its done.

(ii) geckodriver.log
It has log report

(iii) orangehrm1.log(log created for project test cases)
This log report is created and updates once the test file is run and keeps updating the log report.
This has 'time stamp' and message ,so that user understands the flow of test file.

(iv)report_orangehrm.html(html report for project)
HTML report is created to see the staus of test cases whether its passed/failed/errors etc.

(v)test_projectorangehrm.py(test file)
This is the test file of this project.
(a) Test_login 
Initialising the driver and loginpage of the url is opened.
username and password is entered using 'send_keys' method and login successfully.

(b) Test_failedLogin
Initialising the driver and loginpage of the url is opened.
This class tries to login with invalid credentials.
Login is unsuccessful and log report reflects once invalid credentials message is popped up.

(c) Test_add_employeedetails
Initialising the driver and loginpage of the url is opened.
Login credentials are entered and logged in successfully.
In this,First homepage is opened.
THen,click on PIM where we are lead to adding employee details using 'click'.
Employee details are filled by 'send_keys' method.
Then all details are saved successfully.
Log is created once 'Successfully Saved' message pops up on the page.

(d) Test_edit_employee_details
Initialising the driver and loginpage of the url is opened.
Login credentials are entered and logged in successfully.
In this,First homepage is opened.
THen,click on PIM where we are lead to adding employee details using 'click'.
Employee details are filled by 'send_keys' method.
Then,one of the details are edited and updated.
Log is created once 'Successfully Updated' message pops up on the page.

(e) Test_delete_employee_details
Initialising the driver and loginpage of the url is opened.
Login credentials are entered and logged in successfully.
In this,First homepage is opened.
Then,click on PIM where we are lead to adding employee details using 'click'.
Then an employee name is enetered and searched.
Once,the employee name is reflected delete respective employee data.
Log is created once 'Successfully Deleted' message pops up on the page.



