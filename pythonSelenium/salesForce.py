from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")

getUrl = "https://login.salesforce.com/"

driver.get(getUrl)
driver.find_element_by_id("username").send_keys("Sajjad")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_name("cancel").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)