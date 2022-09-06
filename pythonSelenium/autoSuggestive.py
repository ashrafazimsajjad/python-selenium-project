import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("aus")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Austria":
        country.click()
        break

# print(driver.find_element_by_id("autosuggest").text)
# assert driver.find_element_by_id("autosuggest").get_attribute('value') == "Austria"