import requests , webbrowser
res = requests.get('https://www.youtube.com/')
print(res.status_code)
webbrowser.open('https://www.youtube.com/')