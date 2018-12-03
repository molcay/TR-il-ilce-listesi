import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import selenium.webdriver.support.ui as UI


BASE_URL = 'https://www.e-icisleri.gov.tr/Anasayfa/MulkiIdariBolumleri.aspx'


def get_cities(browser, wait):
    result = []
    SELECTOR = "#ctl00_cph1_CografiBirimControl_DropDownListIl"
    i = 1
    while i < 82:
        browser.get(BASE_URL)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, SELECTOR)))

        select_element = UI.Select(
            browser.find_element_by_css_selector(SELECTOR))

        for option in select_element.options[i:i+1]:
            plate = option.get_attribute('value')
            name = option.text
            if int(plate) > 0:
                districts = get_districts(browser, wait, select_element, plate)
                result.append({
                    'plate': plate,
                    'name': name,
                    'districts': districts
                })

        i += 1
        time.sleep(0.5)
    return result


def get_districts(browser, wait, select_element, plate):
    result = []
    SELECTOR = "#ctl00_cph1_CografiBirimControl_DropDownListIlce"

    select_element.select_by_value(plate)
    wait.until(presence_of_element_located((By.CSS_SELECTOR, SELECTOR)))

    select_element_for_districts = UI.Select(
        browser.find_element_by_css_selector(SELECTOR))
    for option in select_element_for_districts.options:
        district_id = option.get_attribute('value')
        name = option.text
        if int(district_id) > 0:
            result.append({
                'district_id': district_id,
                'name': name
            })

    return result


def run():
    with webdriver.Firefox() as browser:
        wait = WebDriverWait(browser, 10)
        cities = get_cities(browser, wait)
        with open('il-ilce-list.json', 'w') as f:
            f.write(json.dumps(cities, indent=2))


if __name__ == "__main__":
    run()
