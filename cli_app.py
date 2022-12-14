import requests
import urlextract


def make_str_list():
    str_lst = []
    while True:
        user_str = str(input("enter link, to finish enter 0 "))
        if user_str != "0":
            str_lst.append(user_str)
        else:
            break
    return str_lst


def get_http_data(str_lst):
    link_meth = {}
    extractor = urlextract.URLExtract()
    for i in str_lst:
        url = extractor.find_urls(i)
        if url:
            response = requests.get(i), requests.post(i), requests.put(i), requests.delete(i), requests.options(i)
            for res in response:
                request = res.request
                link_meth[request.method] = res.status_code
            data_json = {i: link_meth}
            print(data_json)
        else:
            print("string", i, "is not a link")


str_lst = make_str_list()
get_http_data(str_lst)
