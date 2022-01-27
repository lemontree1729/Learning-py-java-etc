from crawling import *

target_url = "https://comic.naver.com/webtoon/list?titleId=783054&weekday=tue"
origin = html_parser(target_url, dynamic=False)
rating = origin.select(".rating_type>strong")
date = origin.select(".num")
print(get_text(rating), get_text(date))
