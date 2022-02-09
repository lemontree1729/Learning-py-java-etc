import requests
from crawling import *
from urllib import parse
import re
import json


def getJson(
    url,
    query={},
    printInfo=False,
    init_api_url="https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=comic&pool=cbox3&lang=ko&objectId=183559_517&pageSize=100&page=1&sort=NEW",
):
    # make valid header
    url_query = get_url_query(url)
    new_url_query = {"titleId": url_query["titleId"], "no": url_query["no"]}
    comment_url = replace_url(url, path="/comment/comment", query=parse.urlencode(new_url_query, doseq=True))
    header = {
        "referer": comment_url,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }

    # get api url using query of init api url
    new_objectId = "_".join(new_url_query.values())
    query["objectId"] = new_objectId
    api_url = set_url_query(init_api_url, query)

    # removing useless prefix and subfix
    removeElse = re.compile("^[^{]+|[^}]+$")
    api_json = json.loads(removeElse.sub("", requests.get(api_url, headers=header).text))
    if printInfo:
        print("header:", header)
        print("api_url:", api_url)
    return api_json
