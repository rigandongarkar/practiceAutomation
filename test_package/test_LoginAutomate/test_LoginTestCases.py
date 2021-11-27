import time

import pytest

from test_package.Utilities import excel_utils
from test_package.test_LoginAutomate.baseClass import BaseClass


class TestLogin(BaseClass):
    # username = "san112020222@mail.com"
    # password = "asdfafewrr234afwe1ssssw2"

    @pytest.mark.sanity
    def test_RegisterUser(self):

        path = "C:\\Users\\rigan\\PycharmProjects\\practiceLogin\\test_package\\Utilities\\userdata.xlsx"
        rows = excel_utils.getRow(path, "Sheet1")

        for row in range(2, rows + 1):

            emailid = excel_utils.readData(path, "Sheet1", row, 1)
            password = excel_utils.readData(path, "Sheet1", row, 2)
            self.driver.find_element_by_xpath("//ul[@id='main-nav']/li[2]").click()
            self.driver.find_element_by_xpath("//input[@type='email']").send_keys(emailid)
            passwordField = self.driver.find_element_by_xpath("//input[@id='reg_password']")

            for passwd in password:
                passwordField.send_keys(passwd)
                time.sleep(0.3)
            registerButton = self.driver.find_element_by_name("register").is_displayed()
            print(registerButton)
            self.driver.find_element_by_xpath("//input[@name='register']").click()
            successRegisterText = self.driver.find_element_by_xpath(
                "//div[@class='woocommerce-MyAccount-content']/p[2]").text
            print(successRegisterText)
            if "From your account dashboard you can view your" in successRegisterText:
                excel_utils.writeData(path, "Sheet1", row, 3, "User Created Successfully")
            else:
                excel_utils.writeData(path, "Sheet1", row, 3, "User not created")
            # assert successLoginText in "From your account dashboard you can view your"
            # user registered successfully
            self.driver.find_element_by_xpath("//div[@class='woocommerce-MyAccount-content']/p/a").click()

    @pytest.mark.regressiontest
    def test_valid_user_password(self):
        self.driver.find_element_by_xpath("//ul[@id='main-nav']/li[2]").click()
        path = "C:\\Users\\rigan\\PycharmProjects\\practiceLogin\\test_package\\Utilities\\userdata.xlsx"
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(
            excel_utils.readData(path, "Sheet1", 2, 1))
        self.driver.find_element_by_css_selector("form[class='login'] p:nth-child(2) input").send_keys(excel_utils.readData(path, "Sheet1", 2, 2))
        self.driver.find_element_by_css_selector("form[class='login'] p:nth-child(3) input:nth-child(3)").click()
        successLoginText = self.driver.find_element_by_xpath("//div[@class='woocommerce-MyAccount-content']/p[2]").text
        print(successLoginText)
        loginText = "From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details."
        assert successLoginText in loginText
