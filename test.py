from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException


debugging = True
load_dotenv()

import os
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

script_directory = Path(__file__).resolve().parent
driver_path = script_directory.joinpath("chromedriver-win64", "chromedriver.exe")

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option("detach", True)
else:
    chrome_options.add_argument("--headless")

def change_html(driver, element):
    driver.execute_script(f"")

def wait_for_element(driver, by, el_identifier, timeout=5):
    try:
        el_present = EC.presence_of_all_elements_located((by, el_identifier))
        WebDriverWait(driver, timeout).until(el_present)
    except TimeoutException:
        print(f'timedout waiting for {el_identifier}')
        return None
    return driver.find_element(by, el_identifier)

def login_to_account(driver):
    driver.get('https://www.meetup.com/login')
    wait_for_element(driver, By.ID, "email").send_keys(EMAIL)
    wait_for_element(driver, By.ID, "current-password").send_keys(PASSWORD)
    wait_for_element(driver, By.CSS_SELECTOR, "button[name='submitButton']").click()

with open('all past mracx events.txt', 'r') as file:
    data = file.read()
events = eval(data)

import time, json, re
from bs4 import BeautifulSoup

def scrape_event_page(driver, event_page):
    time.sleep(3)
    driver.get(event_page)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    name = soup.h1.text
    meta = soup.css.select('script[type="application/ld+json"]')[1].text
    meta = json.loads(meta)
    date = (meta['startDate'], meta['endDate'])
    group = meta['organizer']['name']
    location = meta['location']['address']['streetAddress']
    place = meta['location']['name']
    meta2 = soup.css.select('script[type="application/ld+json"]')[2].text
    attendees1 = json.loads(meta2)['additionalNumberOfGuests']
    attendees2 = soup.css.select('#attendees h2')[0].text
    attendees2 = re.sub("[^0-9]", "", attendees2)
    attendees = attendees1 or attendees2
    tags = soup.css.select('a[id][title]')
    tags = [tuple((i.get('id'), i.get('title'))) for i in tags]

    return (name, group, date, location, place, attendees, tags)



def main():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_to_account(driver)
    except WebDriverException as e:
        print(f"general webdriver error: {e}")
    finally:
        if not debugging:
            driver.quit()

    
    x = scrape_event_page(driver, events[0])
    print(x)


if __name__ == '__main__':
    main()