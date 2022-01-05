from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Step 1) Open Firefox
# browser = webdriver.ie(executable_path=IEDriverManager().install())
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#browser = webdriver.Ie(executable_path=IEDriverManager().install())
#IEDrivermanager
#EdgeDrivermanager
# Step 2) Navigate to OrangeHRM
browser.get("https://netbanking.hdfcbank.com/netbanking/")
# Step 3) Search & Enter the Email or Phone field & Enter Password

# browser.switch_to.frame("login_page")
# browser.find_element_by_xpath("//input[@name='fldLoginUserId']").send_keys("1000")
# #browser.find_element_by_xpath("//img[@alt='continue']")[1]
# browser.switch_to.default_content()
# browser.switch_to.frame(1)
# browser.find_element_by_link_text("Terms and Conditions").click()
# password = browser.find_element_by_css_selector("input[name='txtPassword']")
# submit = browser.find_element_by_css_selector("input[name='Submit']")
# username.send_keys("Admin")
# password.send_keys("admin123")
# Step 4) Click Login
# submit.click()
# wait = WebDriverWait(browser, 20)
# page_title = browser.title
# print(page_title)
#assert page_title == "OrangeHRM"
browser.close()
