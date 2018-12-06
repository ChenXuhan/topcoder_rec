import requests

test_url = "http://192.168.3.239:8000/api/users/"
upload = {"username":"andrea2","email":"chenxh@act.buaa.edu.cn","groups":[]}
r = requests.get(test_url, data=upload, params=upload)
print(r.content)
