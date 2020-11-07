import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    
    def traversal(self, code, acc):
        self.left.traversal(code, acc + "0")
        self.right.traversal(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):

    def traversal(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(string):
    frequencies = []

    for ch, freq in Counter(string).items():
        frequencies.append((freq, len(frequencies), Leaf(ch)))

    heapq.heapify(frequencies)
    count = len(frequencies)
    while len(frequencies) > 1:
        freq1, _count1, left = heapq.heappop(frequencies)
        freq2, _count2, right = heapq.heappop(frequencies)

        heapq.heappush(frequencies, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if frequencies:
        [(_freq, _count, root)] = frequencies
        root.traversal(code, "")

    return code

def huffman_decode(encoded, code):
    mas_char =[]
    encode_char = "" 
    for char in encoded: 
        encode_char += char
        for decode_char in code: 
            if code.get(decode_char) == encode_char:
                mas_char.append(decode_char)  
                encode_char = ""  
                break
    return "".join(mas_char)

'''
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
---------
abacabad

**************

3 10
a: 00
b: 1
c: 01
1011001011
'''
def huffman_get_code(amount_letter, encode_length):
    code = ()
    max_key_len = 0
    for i in range(amount_letter):
        key, value  = input().split(': ')
        temp = (key, value)
        code = code + (temp,)

        if max_key_len < len(key):
            max_key_len = len(key)

    string = input()

    decode_string = ''
    while string != '':
        for i in code:
            if not string or len(string) < len(i[1]):
                continue
            
            if string.startswith(i[1]):
                decode_string+=i[0][0]
                string=string[len(i[1]):]
                break

    print(decode_string)

'''
string = input()
code = huffman_encode(string)
encoded = "".join(code[ch] for ch in string)
print(len(code), len(encoded))

for ch in sorted(code):
    print(f"{ch}: {code[ch]}")
print(encoded)
print(huffman_decode(encoded, code))
'''

amount_letter, encode_length = [int(i) for i in input().split()]
huffman_get_code(amount_letter, encode_length)
