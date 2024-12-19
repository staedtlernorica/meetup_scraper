from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9221")     #https://stackoverflow.com/a/77682955/6030118
# chrome.exe --remote-debugging-port=9221 --user-data-dir="C:/ChromeProfile"    #PASTE THIS
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.meetup.com/mracx-multisport/events/?type=past')

actions = ActionChains(driver)

# Simulate pressing the END key and then the PAGE UP key
# actions.send_keys(Keys.END).send_keys(Keys.PAGE_UP).perform()

# code to dynamically remove elements on page
# =================================================================================================
# element = driver.find_element(By.CSS_SELECTOR, '#submain li:last-child  [id^="ep-"]:last-child')
# driver.execute_script("arguments[0].remove();", element)
# =================================================================================================
# https://stackoverflow.com/questions/33199740/webdriver-remove-element-from-page


import re 
last_event = 0
while last_event < 20:
    pass
    # lastest_event = driver.find_element(By.CSS_SELECTOR, '#submain li:last-child  [id^="ep-"]:last-child')
    # print(lastest_event.get_attribute('id'))
    # last_event = lastest_event.get_attribute('id')
    # res = int(re.sub(r'[^\d]+', '', last_event))
    # print(res)
    # print(last_event.get_attribute("id"))
    # actions.send_keys(Keys.END).send_keys(Keys.PAGE_UP).perform()


# Close the browser (optional)
# driver.quit()

# combine with beautiful soup
# soup = BeautifulSoup(driver.page_source)
# soup.find_all('div', class_='thumbnail')
# for div in soup.find_all('div', class_='thumbnail'):
#     caption = div.find('div', class_='caption')
#     price, title = caption.find_all('h4')
#     print(title.text, price.text)