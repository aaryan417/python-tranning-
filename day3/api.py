import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data =response.json()






# print(f"name : {data['name']}")
# print(f"email : {data['email']}")
# print(f"city : {data['address']['city'] }")



print(data)
for user in data:
    print(f"nmae: {user['name']} - Email :{user['email']}")