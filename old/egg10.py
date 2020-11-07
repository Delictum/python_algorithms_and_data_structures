s = input()
t = input()
i = 0
while s:
    if s.startswith(t):
        i += 1
    s = s[1:]

print(i)
