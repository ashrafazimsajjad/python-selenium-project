from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Tools\\chromedriver.exe")
getUrl = "https://rahulshettyacademy.com/angularpractice/"

driver.get(getUrl)
driver.find_element_by_name("name").send_keys("Sajjad")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")