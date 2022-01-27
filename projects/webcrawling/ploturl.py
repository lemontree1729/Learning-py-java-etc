from crawling import *
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


def parse_date(string):
    return datetime.strptime(string, "%Y.%m.%d")


def get_rating_with_date(target_url):
    rating = []
    date = []
    while True:
        origin = html_parser(target_url, dynamic=False)
        rating.extend(list(map(float, get_text(origin.select(".rating_type>strong")))))
        date.extend(list(map(parse_date, get_text(origin.select(".num")))))
        next = origin.select_one(".next")
        if next is None:
            break
        target_url = "https://comic.naver.com" + next.attrs["href"]
    return pd.DataFrame(data=rating, index=date, columns=["rating"])


def plot_url(url):
    df = get_rating_with_date(url)
    plt.plot(df.index, df.rating)
    plt.show()
