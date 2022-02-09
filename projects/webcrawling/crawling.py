from selenium import webdriver
from bs4.element import Tag
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time
import datetime
from urllib import parse


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


class ProgressBar:
    def __init__(self, length, division=50, fill="="):
        self.count = 0
        self.length = length
        self.division = division
        self.fill = str(fill)
        self.start = time.time()

    def next(self):
        self.count += 1
        bar = int(self.count / self.length * self.division)
        percent = int(self.count / self.length * 100)
        self.end = time.time()
        average_time = (self.end - self.start) / self.count
        eta = datetime.timedelta(seconds=int(average_time * (self.length - self.count)))
        print(
            f"process: [{self.fill*bar}{' '*(self.division-bar)}] | {percent:3d}% | {self.count}/{self.length} | eta: {eta}",
            end="\r",
        )
        if self.count == self.length:
            print(f"\ntook {datetime.timedelta(seconds=self.end - self.start)}")


def replace_url(url, initialize=False, **kwargs):
    if initialize:
        url = parse.urljoin(url, "/")
    return parse.urlunparse(parse.urlparse(url)._replace(**kwargs))


def get_url_query(url):
    return dict(parse.parse_qsl(parse.urlparse(url).query))


def set_url_query(url, new_query):
    if type(new_query) == str:
        return replace_url(url, query=new_query)
    if type(new_query) == dict:
        new_query = new_query.items()
    query = parse.parse_qs(parse.urlparse(url).query)
    for key, value in new_query:
        query[key] = value
    return replace_url(url, query=parse.urlencode(query, doseq=True))


def dict_filter(data: dict, *args):
    filtered_dict = {}
    for arg in args:
        filtered_dict[arg] = data.get(arg)
    return filtered_dict
