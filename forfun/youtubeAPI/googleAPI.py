import requests
from crawling import *

def get_youtube_api_json(path, query: dict, show=False):
    base_url = f"https://www.googleapis.com/youtube/v3/{path}"
    api_url = set_url(base_url, query=query)
    html = requests.get(api_url)
    try:
        api_json = html.json()
    except:
        api_json = BeautifulSoup(html.text, "html.parser")
    if show:
        print("api_url:", api_url)
    return api_json
