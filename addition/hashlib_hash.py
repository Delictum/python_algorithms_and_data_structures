import hashlib


s = hashlib.sha1(b'Hello world.').hexdigest()
print(s)
print(hashlib.sha1(b'gsdagsd' + bytes(s.encode('utf-8'))).hexdigest())
print('*'*100)


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b), 'Строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha};\nhash 2 = {hb}.')

    return ha == hb


s1 = input('Введите строку 1:')
s2 = input('Введите строку 2:')

print('Строки одинаковые' if is_eq_str(s1, s2, True) else 'Строки разные')
