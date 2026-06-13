import requests
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data =response.json()


print(data)
for user in data:
    print(f"Post ID: {user['id']} - title :{user['title']}")