from selenium import webdriver

validateText = "Sajjad"
driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.dismiss()