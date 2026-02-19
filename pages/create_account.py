from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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
    first_name=(By.XPATH,"//input[@data-qa='first_name']")
    last_name=(By.XPATH,"//input[@data-qa='last_name']")
    address=(By.XPATH,"//input[@data-qa='address']")
    country=(By.ID,"country")
    State=(By.XPATH,"//input[@data-qa='state']")
    city=(By.XPATH,"//input[@data-qa='city']")
    zipcode=(By.XPATH,"//input[@data-qa='zipcode']")
    mobile_number=(By.XPATH,"//input[@data-qa='mobile_number']")
    create_accounts=(By.XPATH,"//button[@data-qa='create-account']")

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
            self.wait.until(EC.visibility_of_element_located(self.username)).send_keys("maniK@gpu.com")
            self.wait.until(EC.visibility_of_element_located(self.password)).send_keys("123645@gpu.com")
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

            self.driver.execute_script("window.scrollBy(0,1000)")
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element_year)  
            time.sleep(10)

            self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys("Mani")
            self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys("KAnta")
            self.wait.until(EC.visibility_of_element_located(self.address)).send_keys("chennai, Tamilnadu")
            element_country=self.wait.until(EC.visibility_of_element_located(self.country))
            select=Select(element_country)
            select.select_by_visible_text("India")

            self.wait.until(EC.visibility_of_element_located(self.State)).send_keys("Tamilnadu")
            time.sleep(10)
            self.wait.until(EC.visibility_of_element_located(self.city)).send_keys("Chennai")
            time.sleep(10)
            self.wait.until(EC.visibility_of_element_located(self.zipcode)).send_keys("600001")
            self.wait.until(EC.visibility_of_element_located(self.mobile_number)).send_keys("9876543210")
            time.sleep(10)
           # self.driver.execute_script("window.scrollBy(0,4000)")
            button=self.wait.until(EC.element_to_be_clickable(self.create_accounts))
            #self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",button)
           # button.click()
            #self.driver.execute_script("window.scrollBy(0,0)")
            ActionChains(self.driver).move_to_element(button).click().perform()
            time.sleep(10)


            #-----------------------------------------------------------------------------------------------------
        except Exception as E:
            print("error in entering account details",E)





