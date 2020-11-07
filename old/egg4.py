with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as inp:
    passwords = inp.read()

print(encrypted.strip())
print(passwords.strip())
