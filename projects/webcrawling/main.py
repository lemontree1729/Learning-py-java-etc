from crawling import *
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


def parse_date(string):
    return datetime.strptime(string, "%Y.%m.%d")


def get_rating_with_date(target_url):
    target_url = "https://comic.naver.com/webtoon/list?titleId=783054&weekday=tue"
    rating = []
    date = []
    while True:
        origin = html_parser(target_url, dynamic=False)
        rating.extend(get_text(origin.select(".rating_type>strong")))
        date.extend(list(map(parse_date, get_text(origin.select(".num")))))
        next = origin.select_one(".next")
        if next is None:
            break
        target_url = "https://comic.naver.com" + next.attrs["href"]
    return {"rating": rating, "date": date}


url = "https://comic.naver.com/webtoon/list?titleId=787411&weekday=sat"
data = get_rating_with_date(url)
df = pd.DataFrame(data=data["rating"], index=data["date"], columns=["rating"])
print(df)
plt.plot(x=df.index, y=df.rating)

