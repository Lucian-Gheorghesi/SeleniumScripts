

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingLogin():

    def LoginOK(self):
        webdriver.Chrome(executable_path = "C:\\Users\\gng_a\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get ("https://www.google.ro")


        print("Am ajuns aici")

test = TestingLogin()
test.LoginOK()