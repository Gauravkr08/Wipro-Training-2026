import requests
geturl="http://127.0.0.1:5000/users"
headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"
}
response=requests.get(geturl)
print("get status code:",response.status_code)
print(response.json())

posturl="http://127.0.0.1:5000/users"
body1={
    "name": "Ramu",
}
response=requests.post(posturl,json=body1)
print(response.json())

