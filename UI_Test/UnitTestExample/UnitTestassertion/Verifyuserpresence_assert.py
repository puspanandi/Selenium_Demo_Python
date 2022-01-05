

import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRM_Login_Logout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        cls.driver.maximize_window()
        time.sleep(5)
    def test_02_login_to_orangeHRM(self):
        Act_Text = self.driver.title
        print("Actual Title is"+ Act_Text)
        Exp_Text ="OrangeHRM"
        # assertIs() to check that if first & second evaluated to same object
        self.assertTrue(Exp_Text==Act_Text,"Title matched")

        self.driver.find_element_by_name('txtUsername').send_keys("Admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()

        act_url = self.driver.current_url
        self.assertNotEqual("https://opensource-demo.orangehrmlive.com/index.php/auth/login", act_url,"Both value are not equal")
        time.sleep(5)

    # @unittest.skip("Dashboard is having known defect")
    # def test2_verify_Dashboard(self):
    #     time.sleep(5)
    #     Dashboard_text = self.driver.find_element_by_link_text("Dashboard").text
    #     print(Dashboard_text)
    #     assert Dashboard_text == "Dashboard"

    @unittest.skip("Logout is having known defect")
    def test_04_logout_from_orangeHRM(self):

        self.driver.find_element(By.ID, 'welcome').click()
        self.driver.implicitly_wait(2)  # seconds
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        time.sleep(5)
        self.driver.find_element_by_id('logInPanelHeading').is_displayed()

    def test_03_Addanddelete_users_PIM(self):
        #self.driver.find_element_by_xpath("//b[normalize-space()='PIM']").click()
        # Mouse Hover on to configurations
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath("//b[normalize-space()='PIM']")).perform()
        action.move_to_element(self.driver.find_element_by_link_text("Configuration")).perform()
        action.move_to_element(self.driver.find_element_by_link_text("Custom Fields")).perform()
        self.driver.find_element_by_link_text("Custom Fields").click()
        time.sleep(2)
        # Add the User
        self.driver.find_element_by_id("buttonAdd").click()

        # Add custom Fields
        fields_name = self.driver.find_element_by_id("customField_name")
        random_num = random.randint(11, 1000)
        user_name = fields_name.send_keys("Swetha" + str(random_num))
        time.sleep(5)

        # Enter the value in the Screen and type dropdown
        screen_dd = Select(self.driver.find_element_by_id("customField_screen"))
        default_option = screen_dd.first_selected_option
        print(default_option.text)
        screen_dd.select_by_value("personal")
        type_dd = Select(self.driver.find_element_by_id("customField_type"))
        type_dd.select_by_value("0")
        entered_user = fields_name.text
        self.driver.find_element_by_id("btnSave").click()
        source = self.driver.page_source
        self.assertIn(entered_user,source,"entered user is found")
        print("user entered is present")


        ExpUserName = "Swetha" + str(random_num)
        self.driver.refresh()
        cellvalue = self.driver.find_element_by_xpath("//a[text()='" + ExpUserName + "']")

        textvalue = cellvalue.text
        print(textvalue)
        assert ExpUserName == textvalue
        # Delete all users based on matching patern from WebTable


        rows = self.driver.find_elements_by_xpath("//table[@id='customFieldList']/tbody/tr")
        rowsLength = len(rows)
        print(rowsLength)

# Complete xpath to get first value "//*[@id='resultTable']/tbody/tr[]/td[2]"
        beforXpath = "//*[@id='customFieldList']/tbody/tr["
        AfterXpath = "]/td[2]"
        i = 1
        for row in range(rowsLength):

            name = self.driver.find_element_by_xpath(beforXpath + str(i) + AfterXpath).text
            print(name)

            if "Swetha" in name:
                self.driver.find_element_by_xpath("//*[@id='customFieldList']/tbody/tr[" + str(i) + "]/td[1]/input").click()
            i = i + 1
        time.sleep(5)

    #def test_05_deleteuser(self):
        #time.sleep(2)
        self.driver.find_element_by_id("buttonRemove").click()
        self.driver.find_element_by_id("dialogDeleteBtn").click()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)
        page_source=self.driver.page_source
        #entered_user = fields_name.text
        self.assertNotIn(entered_user,page_source,"entered user is successfully deleted")

    @classmethod
    def tearDownClass(self):
         # close the browser window
         self.driver.quit()

if __name__ == '__main__':
    unittest.main()




















