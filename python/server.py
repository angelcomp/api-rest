# Imports
from flask import Flask, jsonify
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from colorama import Fore, Style
import simplejson as json

# Constants
GITHUB_URL = r'https://github.com/'
H1_XPATH = '//h1[@class="h0-mktg mt-sm-6 mt-md-11 mt-lg-9 mb-2 mb-sm-4 position-relative z-2"]'
P_XPATH = '//p[@class="f1-mktg col-11 col-lg-10 text-normal color-fg-muted mr-lg-n4 mb-3 mb-md-4 mb-md-7 position-relative z-1"]'


def web_scraping_github():
    print(f"\n\n{Fore.LIGHTGREEN_EX}Start of web scraping process...\n\n")

    # Configuring browser options
    print(f"\n\t{Fore.BLUE}Configuring browser options...\n")
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--disable-plugins-discovery")

    # Setting browser option and opening github page
    print(f"\n\t{Fore.BLUE}Setting options for browser...\n")
    browser = webdriver.Chrome(options=chrome_options)
    browser.delete_all_cookies()
    print(f"\n\tOpening the Github page: {GITHUB_URL}\n")
    browser.get(GITHUB_URL)
    wait = WebDriverWait(browser, 20)

    # Grabbing h1 element text
    print(f"\n\tGrabbing the text of the 'h1' page element...\n")
    h1 = browser.find_element(
        By.XPATH, H1_XPATH
    )

    h1 = h1.text
    print(f"\n\t\t{Fore.YELLOW}Text extracted from the 'h1' element:\n\t\t\t{Fore.GREEN}"
          f"- {h1}")

    # Grabbing p element text
    print(f"\n\t{Fore.BLUE}Grabbing the text of the first 'p' page element...\n")
    p = browser.find_element(
        By.XPATH, P_XPATH
    )

    p = p.text
    print(f"\n\t\t{Fore.YELLOW}Text extracted from 'p' element:\n\t\t\t{Fore.GREEN}"
          f"- {p}")

    # Closing the browser
    print(f"\n\t{Fore.BLUE}Closing the browser...\n")
    browser.quit()

    # Create dictionary for elements extracted texts
    print(f"\n\t{Fore.BLUE}Generating a dictionary for the extracted page elements...\n")
    github_h1_and_p = {'h1': h1, 'p': p}
    print(f"\n\t\t{Fore.YELLOW}Generated dictionary:\n\t\t\t{Fore.GREEN}"
          f"- {github_h1_and_p['h1']}\n\t\t\t- {github_h1_and_p['p']}")

    print(f"\n\t{Fore.BLUE}Converting python dictionary to json format...\n")
    json_data = json.dumps(github_h1_and_p)

    print(f"\n\n{Fore.GREEN}SUCCESS!!!")
    print(f"\n{Fore.LIGHTMAGENTA_EX}End of web scraping process...{Style.RESET_ALL}\n\n")

    return json_data


app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route('/python', methods=['GET'])
def get_student_info():
    student_info = web_scraping_github()
    return student_info


if __name__ == '__main__':
    app.run()

