import time

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame("login_page")
#userid = browser.find_element_by_xpath("//input[@name='fldLoginUserId']")
cont = browser.find_element_by_xpath("//img[@alt='continue']").click()
#time.sleep(2)
alert = browser.switch_to.alert
text=alert.text
print(text)
time.sleep(5)
assert text=="Customer ID  cannot be left blank."
alert.accept()


#userid.send_keys(1000)
#browser.switch_to.default_content()
#browser.switch_to.frame(1)
#terms = browser.find_element_by_link_text("Terms and Conditions")

#terms.click()
# cont.click()


time.sleep(5)

browser.close()