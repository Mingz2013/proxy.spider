# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests

if __name__ == "__main__":
    url = "http://localhost/api/get_one"

    response = requests.get(url)

    print response

    print response.content
