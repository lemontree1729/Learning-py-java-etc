import re
from bs4.element import Tag
from crawling import *
from copy import copy


class Selector:
    def __init__(self, html, tag):
        newhtml = html.copy()
        temp = []
        while temp:
            pass

    def get_selector(html, tag):
        pass

    def parse_selector(selector):
        pass


def get_selector(tag, exact=False, current=""):
    if tag is None:
        return None
    if tag.name == "body":
        return "body" + current
    parent = tag.find_parent()
    if tag.name is None:
        return get_selector(parent, exact, current)
    if not exact:
        return get_selector(parent, exact=False, current=f">{tag.name}{current}")
    count = 1
    for child in parent.children:
        if child is tag:
            return get_selector(parent, exact=True, current=f">{tag.name}:nth-child({count}){current}")
        if child.name == tag.name:
            count += 1


def parse_selector(selector):
    return list(map(lambda x: x.split(":nth-child"), selector.split(">")))


def preprocess(html, selector):
    html
    pass


def stringify(parsed_css_selector):
    pass


def extract_data(html, selector, rank):
    target = html
    stack = []
    while len(stack) > 0:
        pass

    for tag in parse_selector(selector):
        pass
    pass


def find_pattern(selector):
    pass


def show_tag_tree(selector):
    pass


def show_tag(selector):
    pass


html = html_parser(
    "https://ko.wikipedia.org/wiki/%ED%8A%B9%EC%88%98:%EC%B5%9C%EA%B7%BC%EB%B0%94%EB%80%9C?hidebots=1&hidecategorization=1&hideWikibase=1&limit=50&days=7&urlversion=2",
    dynamic=False,
)

# html = html_parser("https://namu.wiki/RecentChanges", delay=5)


def printTree(tree, maxcount=10, rank=[], end=True):
    sign = "├─"
    if end:
        sign = "└─"
    for i in rank:
        if i == 1:
            print("│  ")
        else:
            print("   ")
    if type(tree) in (str or int):
        print(f"{sign}{tree}")
        return
    foo = None
    print(f"{sign}{tree}")
    if hasattr(tree, "popitem"):
        foo = lambda x: x.popitem()[0]
    elif hasattr(tree, "pop"):
        foo = lambda x: x.pop()
    while (len(tree)>1):


    if len(tree) == 1:
        print(f"└─")
    for i in len(tree):
        if i == len(tree) - 1:
            sign = "└─"
        if type(tree[i]) is str or int:
            printTree(tree, maxcount, rank, end)
        else:
            if 1:
                pass


from collections import Counter

a = Counter([1, 2, 3, 4, 1, 2, 1, 2, 1, 2, 2, 2, 3, 1, 1, 11, 1, 1])
print(a)
print(a.most_common())


common_selector = Counter(map(get_selector, html.select("*"))).most_common(10)
for selector in common_selector:
    target_selector = get_text(html.select(selector[0]))
    print(f"├─{selector[0]}({selector[1]})")
    for i in range(len(target_selector)):
        if i in (9, len(target_selector)):
            print(f"│  └─{target_selector[i]}")
            break
        print(f"│  ├─{target_selector[i]}")
classes = []
for element in html.find_all(class_=True):
    classes.extend(element["class"])
common_class = Counter(classes).most_common(10)
for class_ in common_class:
    target_class = get_text(html.find_all(class_=class_[0]))
    print(f"├─{class_[0]}({class_[1]})")
    print("│  ├─", *target_class[: min(10, len(target_class))], sep="\n│  ├─")

