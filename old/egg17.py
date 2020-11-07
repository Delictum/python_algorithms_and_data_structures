import requests
import json


client_id = '822c6237a6d9e9d9c0bf'
client_secret = 'a76429a594b96d27a7d6d3b76da36498'
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
api_url = "https://api.artsy.net/api/artists/{}"

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

rec = open('out.txt', 'w')
headers = {"X-Xapp-Token" : token}

results = []
with open('dataset_24476_4.txt', 'r') as file:
    for line in file.readlines():
        res = requests.get(api_url.format(line.rstrip()), headers=headers)
        res.encoding = 'utf-8'

        j = json.loads(res.text)
        sortable_name = ''
        for i in j.items():
            if i[0] == 'sortable_name':
                sortable_name = i[1]
            elif i[0] == 'birthday':
                results.append([sortable_name, i[1]])
                break

results = sorted(results, key=lambda x: (x[1], x[0]))
for i in results:
    print(i[0])
'''
buf = [
    ['Warhol Andy', '1928'],
    ['Abbas Hamra', '1928'],
    ['Abbott Mary', '1928'],
    ['Abbott Mary', '1938'],
    ['Abbott Mary', '1918'],
    ]

buf = sorted(buf, key=lambda x: (x[1], x[0]))
for i in buf:
    print(i)
'''
                
