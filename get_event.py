from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_experimental_option("prefs", {
#     "detach": True,
#     "debuggerAddress": "127.0.0.1:9222"
#     })     # cd../../Program Files (x86)\Google\Chrome\Application\ chrome.exe --remote-debugging-port=9224

chrome_options.add_experimental_option("detach", True)
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--remote-debugging-port=9224")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

with open('all past mracx events.txt', 'r') as file:
    data = file.read()
events = eval(data)


def login():
    driver.get("https://www.meetup.com/login")  # Replace with the actual URL of the login page
    username_field = driver.find_element(By.ID, "email")  # Use the correct locator for your page
    username_field.send_keys("longvuong@live.com")  # Replace with your username
    password_field = driver.find_element(By.ID, "current-password")  # Use the correct locator for your page
    password_field.send_keys("kick@ssthemovie")  # Replace with your password
    login_button = driver.find_element(By.CSS_SELECTOR, "button[name='submitButton']")  # Use the correct locator for your page
    login_button.click()
    driver.implicitly_wait(15)
    # driver.quit()   

login()
driver.implicitly_wait(15)
# driver.get(events[0])

while(True):
    pass



# soup = BeautifulSoup(driver.page_source)
