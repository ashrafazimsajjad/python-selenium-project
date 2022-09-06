from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkBoxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkBoxes))
for checkBox in checkBoxes:
    if checkBox.get_attribute('value') == "option2":
        checkBox.click()
        assert checkBox.is_selected()

radioButtons = driver.find_elements_by_xpath("//input[@type='radio']")
radioButtons[1].click()
assert radioButtons[1].is_selected()
# print(len(radioButtons))
# for radioButton in radioButtons:
#     if radioButton.get_attribute('value') == "radio3":
#         radioButton.click()
#         assert radioButton.is_selected()