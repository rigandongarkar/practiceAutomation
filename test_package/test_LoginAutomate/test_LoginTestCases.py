import time

from test_package.test_LoginAutomate.baseClass import BaseClass


class TestLogin(BaseClass):
    username = "san112020222@mail.com"
    password = "asdfafewrr234afwe1ssssw2"

    # @pytest.mark.skip
    def test_RegisterUser(self):
        self.driver.find_element_by_xpath("//ul[@id='main-nav']/li[2]").click()
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.username)
        passwordField = self.driver.find_element_by_xpath("//input[@id='reg_password']")

        for passwd in self.password:
            passwordField.send_keys(passwd)
            time.sleep(0.2)
        registerButton = self.driver.find_element_by_name("register").is_displayed()
        print(registerButton)
        self.driver.find_element_by_xpath("//input[@name='register']").click()
        successRegisterText = self.driver.find_element_by_xpath("//div[@class='woocommerce-MyAccount-content']/p[2]").text
        print(successRegisterText)
        # assert successLoginText in "From your account dashboard you can view your"
        # user registered successfully
        self.driver.find_element_by_xpath("//div[@class='woocommerce-MyAccount-content']/p/a").click()

    def test_valid_user_password(self):
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_css_selector("form[class='login'] p:nth-child(2) input").send_keys(self.password)
        self.driver.find_element_by_css_selector("form[class='login'] p:nth-child(3) input:nth-child(3)").click()
        successLoginText = self.driver.find_element_by_xpath("//div[@class='woocommerce-MyAccount-content']/p[2]").text
        print(successLoginText)
        loginText = "From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details."
        assert successLoginText in loginText
