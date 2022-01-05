import time

import pytest


# @pytest.fixture
# def app_url():
#     url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
#     return url


@pytest.mark.usefixtures("driver_init", "hrm_url")
class BasicTest:
    pass


@pytest.mark.parametrize("uname, upass, expresult",
                         [("Admin", "admin123", "Dashboard"), ("Admin1", "admin123", "Invalid credentials"),
                          ("", "admin123", "Username cannot be empty"), ("Admin", "admin123", "Dashboard")])
class Test_OrangeHRM_Login(BasicTest):

    def test_open_url(self, uname, upass, expresult, hrm_url):
        i=0
        # Step 2) Navigate to OrangeHRM
        # self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.get(hrm_url)
        # Step 3) Enter the Username & Enter Password
        username = self.driver.find_element_by_name("txtUsername")
        password = self.driver.find_element_by_name("txtPassword")
        submit = self.driver.find_element_by_name("Submit")
        username.send_keys(uname)
        password.send_keys(upass)
        for i in range(4):

            expresult=self.driver.find_element_by_xpath("//b[normalize-space()='Dashboard']")
        # Step 4) Click Login
        submit.click()
        time.sleep(3)

        # Logout from application
        self.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)