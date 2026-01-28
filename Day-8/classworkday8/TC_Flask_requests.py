import requests
geturl="https://api.restful-api.dev/objects"
response=requests.get(geturl)
print(response.status_code)
print(response.json())

posturl="https://api.restful-api.dev/objects"
body1={
    'name': 'Apple MacBook Pro 16',
    'data': {
        'year': 2019,
        'price': 1849.99,
        'CPU model': 'Intel Core i9',
        'Hard disk size': '1 TB'}

}
r1=requests.post(posturl, json=body1)
print(r1.status_code)
print(r1.json())

obj_id=r1.json()['id']
puturl=f"https://api.restful-api.dev/objects/{obj_id}"
body2={
'name': 'Apple MacBook Pro 16',
    'data': {
        'year': 2019,
        'price': 1849.99,
        'CPU model': 'Intel Core i9',
        'Hard disk size': '1 TB',
        'color':'black',
        }
}
r2=requests.put(puturl, json=body2)
print(r2.status_code)
print(r2.json())

patchurl=f"https://api.restful-api.dev/objects/{obj_id}"
body3={
    'name': 'Apple MacBook Pro 16',
    'data': {
        'year': 2019,
        'price': 1849.99,
        'CPU model': 'Intel Core i9',
        'Hard disk size': '1 TB',
        'color':'black',
        "camera":"4K resolution",
    }
}
r3=requests.patch(patchurl, json=body3)
print(r3.status_code)
print(r3.json())



deleteurl=f"https://api.restful-api.dev/objects/{obj_id}"
r4=requests.delete(deleteurl)
print(r4.status_code)
print(r4.json())