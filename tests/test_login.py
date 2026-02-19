from pages.create_account import create_account
import requests


def test_login(driver):
    obj=create_account(driver)
    obj.login_page()
    assert "New User Signup!" in driver.page_source
def test_signup(driver):
     obj=create_account(driver)
     obj.create_account()
     assert "Enter Account Information" in driver.page_source
def test_account_information(driver):
     obj=create_account(driver)
     obj.enter_account_information()
     assert "3" in driver.page_source
     assert "July" in driver.page_source
     assert "2000" in driver.page_source
