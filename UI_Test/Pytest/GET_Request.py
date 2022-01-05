
import time
import unittest

import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture
# def app_url():
#      url = "https://chercher.tech/sample/"
#      return url
#from UI_Test.Pytest.conftest import app_url
#from UI_Test.Pytest.conftest import app_url


@pytest.mark.usefixtures("driver_init","app_url")
class BasicTest:
	pass


class Test_Get(BasicTest):

    def test_get_id_details(self,app_url):
        emp_id = 4656
        print("swetha")
        url=app_url+"api/product/read?id=" + str(emp_id)
        r = requests.get(url)
        print(r.json())
        print(r.status_code)
        assert str(200) in str(r.status_code)
        json_string = r.json()
        self.name_value = json_string[0]["name"]
        print(self.name_value)
        return self.name_value

    def test_get_Verify_details(self,app_url):
        # Navigate to UI app
        #browser = webdriver.Chrome(ChromeDriverManager().install())
        #url="https://chercher.tech/sample/"
        url = app_url
        self.driver.get(url+"api-ui")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@placeholder='Search product...']").send_keys("4656")
        act_text = self.driver.find_element_by_xpath("//td[contains(text(),'Swetha')]").text
        time.sleep(3)
        print(act_text)
        self.test_get_id_details(app_url)
        print(self.name_value)
        assert self.name_value == act_text






