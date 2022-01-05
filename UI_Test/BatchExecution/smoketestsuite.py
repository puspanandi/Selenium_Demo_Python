import unittest
# get all tests from SearchText and HomePageTest class
from UI_Test.UnitTestExample.UnitTestdecorator.Setup_Teardown_ClassLevel import OrangeHRM_Login_Logout
from UI_Test.UnitTestExample.UnitTestdecorator.UnitTest_Pytest1 import SearchText

search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(OrangeHRM_Login_Logout)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)