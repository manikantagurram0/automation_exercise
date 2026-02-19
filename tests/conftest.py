from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as Chromeservices
from selenium.webdriver.firefox.service import Service as Firefoxservices
from selenium.webdriver.chrome.options import Options as chromeoptions
from selenium.webdriver.firefox.options import Options as firefoxoptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(scope="session")
def driver(headless=None,browser="chrome"):

    if browser=="chrome":
        options=chromeoptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        if headless:
                options.add_argument("--headless")
        services=Chromeservices(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=services,options=options)
        yield driver
        driver.quit()

    elif browser=="firefox":
        options=firefoxoptions()
        services=Firefoxservices(GeckoDriverManager.install())
        driver=webdriver.Firefox(service=services,options=options)
        #options.add_argument("--diable-notifications")
        #options.add_argument("--start-maximized")
        #options.add_argument()
        driver.maximize_window()
        yield driver
        driver.quit()