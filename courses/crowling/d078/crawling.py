from selenium import webdriver
from bs4.element import Tag
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time


def html_parser(url: str, delay=0, headless=False, dynamic=True, log_level=0):
    if not dynamic:
        return BeautifulSoup(requests.get(url).text, "html.parser")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("headless")
    try:
        # silencing log not working
        driver = webdriver.Chrome(ChromeDriverManager(log_level=log_level).install(), options=options)
        driver.get(url)
        time.sleep(delay)
        source = driver.page_source
        driver.quit()
        return BeautifulSoup(source, "html.parser")
    except:
        print("html parser got an error")
        return None


def get_text(target: Tag, recursive=True):
    if type(target) == str:
        return target
    if hasattr(target, "text"):
        if not recursive:
            return "".join(get_text(filter(lambda x: x.name == None, target.children)))
        return target.text.strip()
    try:
        return list(map(get_text, target))
    except:
        return ""
