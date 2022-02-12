import requests
from crawling import *
import re
import json


def get_naver_comment_json(ticket, query: dict, show=False):
    base_comment_url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json"
    header = {
        "referer": "https://naver.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }
    pool_info = {"comic": "cbox3", "news": "cbox5", "blog": "cbox9"}
    base_query = {"ticket": ticket, "pool": pool_info[ticket], "lang": "ko", "pageSize": 100, "sort": "new"}
    for key, value in query.items():
        base_query[key] = value
    api_url = set_url(base_comment_url, query=base_query)
    # removing useless prefix and subfix
    html = requests.get(api_url, headers=header)
    html.encoding = "utf8"
    try:
        api_json = json.loads(re.sub("^[^{]+|[^}]+$", "", html.text))
    except:
        api_json = BeautifulSoup(html.text, "html.parser")
    if show:
        print("header:", header)
        print("api_url:", api_url)
    return api_json


def get_naver_map_json():
    pass
