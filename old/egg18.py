from xml.etree import ElementTree


'''
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
'''
# root = ElementTree.fromstring(input())
# root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>')
root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>')
'''
<cube color="blue">
    <cube color="red">
        <cube color="green">
            <cube color="green">
                <cube color="green">
                    <cube color="blue">
                    </cube>
                    <cube color="green">
                    </cube>
                    <cube color="red">
                    </cube>
                </cube>
            </cube>
        </cube>
    </cube>
    <cube color="red">
        <cube color="blue">
        </cube>
    </cube>
</cube>
'''
colors = {'red': 0, 'green': 0, 'blue': 0}
values = []


def rec(child, level, childs=[]):
    if not child:
        return level
            
    level += 1
    for i in child:
        values.append((i.attrib['color'], level))
        rec(i, level)
    

rec([root], 0)
for color, level in values:
    colors[color] += level

for i in colors:
    print(colors[i], end=' ')
