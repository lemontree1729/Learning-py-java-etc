import re
from crawling import *

parsed_html = html_parser(input("enter the path: "), 5)
data = []
keyword = input("import data to find: ")
finded_datas = parsed_html.find_all(text=re.compile(keyword))
css_tags = set()
for finded_data in finded_datas:
    css_tag = None
    temp = finded_data.find_parent()
    while temp.name != "body":
        if css_tag == None:
            css_tag = temp.name
        else:
            css_tag = temp.name + ">" + css_tag
        temp = temp.find_parent()
    print("css_tag:", css_tag)
    css_tags.add(css_tag)
datatype = input("data type to show: ")
if datatype == "text":
    func = get_text
else:
    func = lambda x: x.attrs.get(datatype, "")
for css_tag in css_tags:
    data.extend(list(map(func, parsed_html.select(css_tag))))
print(data)

