from bs4 import BeautifulSoup
import requests
import time
import datetime
from urllib import parse


def html_selector(url, selector, filter=lambda x: x.text):
    return list(map(filter, BeautifulSoup(requests.get(url).text, "html.parser").select(selector)))


def get_url_query(url):
    return dict(parse.parse_qsl(parse.urlparse(url).query))


def set_url(url, **kwargs):  # query should be dict
    if kwargs.get("query"):
        kwargs["query"] = parse.urlencode(kwargs["query"], doseq=True)
    return parse.urlunparse(parse.urlparse(url)._replace(**kwargs))


def replace_url(url, **kwargs):
    if kwargs.get("query"):
        for key, value in get_url_query(url).items():
            kwargs["query"][key] = value
    return set_url(url, **kwargs)


def dict_key_filter(data: dict, filter):
    filtered_dict = {}
    for arg in filter:
        filtered_dict[arg] = data.get(arg)
    return filtered_dict


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
