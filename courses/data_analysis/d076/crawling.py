from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def html_parser(url, delay=0, headless=False, dynamic=True):
    if not dynamic:
        return BeautifulSoup(requests.get(url).text, "html.parser")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("headless")
    try:
        driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe", options=options)
        driver.get(url)
        time.sleep(delay)
        source = driver.page_source
        driver.quit()
        return BeautifulSoup(source, "html.parser")
    except:
        print("html parser got an error")
        return None


def get_text(target):
    if hasattr(target, "text"):
        return target.text
    try:
        return list(map(get_text, target))
    except:
        return ""
