import requests


api_url = 'http://numbersapi.com/{}/math?json=true'

rec = open('out.txt', 'w')

with open('dataset_24476_3.txt', 'r') as file:
    for i in file.readlines():
        i = i.rstrip()
        req = requests.get(api_url.format(i))
        for j in req.json().items():
            if j[0] == 'found':
                rec.write('Interesting\n') if j[1] else rec.write('Boring\n')
rec.close()
                
