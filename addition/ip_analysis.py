from collections import OrderedDict, defaultdict, deque

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]

    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1

data.update(spam)
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
    for k, v in data.items():
        f.write(f'{k} - {v}\n')
