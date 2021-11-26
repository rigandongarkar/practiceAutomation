import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_95\\chromedriver", options=chromeOptions)
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(20)

    request.cls.driver = driver

    yield
    driver.close()

