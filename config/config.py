from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestData:

    chrome_executablepath=ChromeDriverManager().install()
    firefox_executablepath=GeckoDriverManager().install()
    edge_executablepath=EdgeChromiumDriverManager().install()

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"



