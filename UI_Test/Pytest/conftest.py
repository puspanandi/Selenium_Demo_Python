import pytest
from selenium import webdriver

url = "www.google.com"

@pytest.fixture(params=["chrome"])
#@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver

    yield
    web_driver.close()


@pytest.fixture
def app_url():
    url = "https://chercher.tech/sample/"
    return url

@pytest.fixture
def hrm_url():
    url="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    return url