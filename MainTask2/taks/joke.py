import requests
res = requests.get("https://DavidTest.com")
if res.status_code == 200:
    joke = res.json()
    print(joke)
else:
    print("Fail to fetch joke")

