from crawling import *
from autocrawling import *

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
                selector = get_selector(finded_data)
                if selector:
                    css_tags.add(selector)
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
