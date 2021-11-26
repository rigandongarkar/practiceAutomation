import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from test_package.test_LoginAutomate.baseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.mark.skip
    def test_newArrivals(self):
        itemsPresent = self.driver.find_elements_by_xpath(
            "//div[@class='themify_builder_sub_row clearfix gutter-default   sub_row_1-0-2']/div/div/div/ul/li/a/h3")
        itemsCount = 0

        for itemsList in itemsPresent:
            itemName = itemsList.text
            print(itemName)
            itemsCount = itemsCount + 1

        print(itemsCount)
        assert itemsCount == 3

    def test_newArrivalImageNavigation(self):

        self.driver.execute_script("window.scrollTo(0, 500)")
        Link = self.driver.find_elements_by_xpath(
            "//div[contains(@class,'themify_builder_sub_row clearfix gutter-default')]/div/div/div/ul/li/a/img")

        for imgLink in Link:
            actions = ActionChains(self.driver)
            actions.move_to_element(imgLink).perform()

            ActionChains(self.driver).key_down(Keys.CONTROL).click(imgLink).key_up(Keys.CONTROL).perform()

        parentWindow = self.driver.window_handles[0]
        childWindow1 = self.driver.window_handles[1]
        childWindow2 = self.driver.window_handles[2]
        childWindow3 = self.driver.window_handles[3]

        self.driver.switch_to.window(childWindow1)
        itemTitle = self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/h1").text
        print("Child Window 1 item title: " + itemTitle)

        self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/form/button").click()
        addedToBasketText = self.driver.find_element_by_xpath("//div[@class='woocommerce-message']").text

        textToVerify = "has been added to your basket."
        assert textToVerify in addedToBasketText

        self.driver.switch_to.window(childWindow2)
        itemTitle = self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/h1").text
        print("Child Window 2 item title: " + itemTitle)

        self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/form/button").click()
        addedToBasketText = self.driver.find_element_by_xpath("//div[@class='woocommerce-message']").text

        textToVerify = "has been added to your basket."
        assert textToVerify in addedToBasketText

        self.driver.switch_to.window(childWindow3)
        itemTitle = self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/h1").text
        print("Child Window 3 item title: " + itemTitle)

        self.driver.find_element_by_xpath("//div[contains(@class,'entry-summary')]/form/button").click()
        addedToBasketText = self.driver.find_element_by_xpath("//div[@class='woocommerce-message']").text

        textToVerify = "has been added to your basket."
        assert textToVerify in addedToBasketText

        self.driver.switch_to.window(parentWindow)
