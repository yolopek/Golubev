import urllib3
import requests
import json

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
res = requests.get(url)
r_dict = res.json()
items = r_dict["items"]

count_private = 0
for item in items:
    if item["private"]:
        count_private += 1

print("Количество приватных проектов:", count_private)

for item in items:
    print(f"{item['owner']['login']} создал проект {item['name']}")
    print()