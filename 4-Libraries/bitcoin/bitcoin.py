import requests

json = requests.get("https://musical-guide-v6wwv9p47gp3p7w5.github.dev/", data={"bpi"})
print(json.text)
