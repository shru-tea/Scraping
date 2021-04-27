from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = "C:\\Users\\..\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_score = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice"+str(i))
         for i in range(2)]
# for item in items:
#    print(type(int(item.text)))
# items = driver.find_element_by_id("productPrice0")
# print(type(int(items.text)))

# selecting a new actionChains object, its gonna act on the web driver
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_score.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()
