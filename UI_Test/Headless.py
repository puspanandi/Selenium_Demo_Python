from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

opt=Options()
#opt.set_headless(False)
#opt.headless()
opt.add_argument('incognito')
# Step 1) Open Chrome
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=opt)
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(browser, 20)
page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"
browser.close()
