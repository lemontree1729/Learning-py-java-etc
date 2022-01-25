import re
from bs4.element import Tag
from crawling import *


def get_css_selector(tag, exact=False, current=""):
    if tag is None:
        return None
    if tag.name == "body":
        return "body" + current
    parent = tag.find_parent()
    if tag.name is None:
        return get_css_selector(parent, exact, current)
    if not exact:
        return get_css_selector(parent, exact=False, current=f">{tag.name}{current}")
    count = 1
    for child in parent.children:
        if child is tag:
            return get_css_selector(parent, exact=True, current=f">{tag.name}:nth-child({count}){current}")
        if child.name == tag.name:
            count += 1


def parse_css_selector(css_selector):
    return list(map(lambda x: x.split(":nth-child"), css_selector.split(">")))


def stringify(parsed_css_selector):
    pass


def extract_data(html, css_selector, rank):
    target = html
    stack = []
    while len(stack) > 0:
        pass

    for tag in parse_css_selector(css_selector):
        pass
    pass


def find_pattern(css_selector):
    pass


def show_tag_tree(css_selector):
    pass


def show_tag(css_selector):
    pass


while True:
    toggle_menu = input("1:move url, 2:find data>>")
    if toggle_menu == "1":
        parsed_html = html_parser(input("url to move>>"), 5)
    elif toggle_menu == "2":
        data = []
        toggle_data = input("1:string, 2:css tag>>")
        if toggle_data == "1":
            keyword = input("enter string to find>>")
            finded_datas = parsed_html.find_all(text=re.compile(keyword))
            css_tags = set()
            for finded_data in finded_datas:
                css_selector = get_css_selector(finded_data)
                if css_selector:
                    css_tags.add(css_selector)
            css_tags = list(css_tags)
            print(f"{len(css_tags)} css_tags found")
            for cnt in range(len(css_tags)):
                print(f"css_tag{cnt}: {css_tags[cnt]}")
                similerdata = get_text(parsed_html.select(css_tags[cnt]))
                print("similer data-----", *similerdata[: min(len(similerdata), 15)], sep="\n")
                data.extend(similerdata)

            # datatype = input("enter data type to show>>")
            # if datatype == "text":
            #     func = get_text
            # else:
            #     func = lambda x: x.attrs.get(datatype, "")
            # for css_tag in css_tags:
            #     data.extend(list(map(func, parsed_html.select(css_tag))))
        if toggle_data == "2":
            keyword = input("enter css tag to find>>")
            finded_datas = parsed_html.select(keyword)
        # print(data)
    else:
        print("wrong input!")

