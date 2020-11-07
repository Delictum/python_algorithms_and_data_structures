import requests
import re


href = input()
# href = 'http://localhost:5000/stepic'
content = requests.get(href).text

result = []
for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", content):
    domain = link[8]
    if domain not in result:
        result.append(domain)

result.sort()

for domain in result:
    print(domain)
