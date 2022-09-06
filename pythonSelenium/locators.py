from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
getUrl = "https://rahulshettyacademy.com/angularpractice/"

driver.get(getUrl)
getName = "name"
driver.find_element_by_name(getName).send_keys("sajjad")
driver.find_element_by_xpath("//input[@name='email']").send_keys("Hossain")
driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("123456")
driver.find_element_by_class_name("form-check-input").click()
dropDown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")
dropDown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "Success" in message
