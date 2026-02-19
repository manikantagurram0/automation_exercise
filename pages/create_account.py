from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

class create_account:
    homepage_url="https://automationexercise.com/"
    login_button=(By.XPATH,"//i[@class='fa fa-lock']/parent::a")
    #-------------------------------------------------------------------------------------------------------------------#
    #SIGNUP USER NAME AND PASSWORD
    username=(By.XPATH,"//input[@placeholder='Name']")
    password=(By.XPATH,"//input[@data-qa='signup-email']")
    Signup_button=(By.XPATH,"//button[@data-qa='signup-button']")
    #-------------------------------------------------------------------------------------------------------------------#
    #Enter account details
    acc_password=(By.ID,"password")
    day=(By.ID,"days")
    month=(By.ID,"months")
    year=(By.ID,"years")
    #------------------------------------------------------------------------------------------------


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

        
    def login_page(self):
        self.driver.get(self.homepage_url)
        self.wait.until(EC.visibility_of_element_located(self.login_button)).click()
        time.sleep(10)
    def create_account(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.username)).send_keys("mani@gpu.com")
            self.wait.until(EC.visibility_of_element_located(self.password)).send_keys("1234@gpu.com")
            self.wait.until(EC.element_to_be_clickable(self.Signup_button)).click()
        except Exception as E:
            print("issue in login or signup is failed",E)
    def enter_account_information(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.acc_password)).send_keys("mahdew#04")
            self.element_day=self.wait.until(EC.visibility_of_element_located(self.day))
            select=Select(self.element_day)
            select.select_by_visible_text("3")
            #----------------------------------------------------------------------------------------------
            element_month=self.wait.until(EC.visibility_of_element_located(self.month))
            select=Select(element_month)
            select.select_by_visible_text("July")
            #--------------------------------------------------------------------------------------------------
            element_year=self.wait.until(EC.visibility_of_element_located(self.year))
            select=Select(element_year)
            select.select_by_visible_text("2000")
            time.sleep(10)
            #-----------------------------------------------------------------------------------------------------
        except Exception as E:
            print("error in entering account details")





