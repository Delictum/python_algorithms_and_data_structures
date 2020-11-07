count_items, max_weight = [int(x) for x in input().split()]

mas = [[int(x) for x in input().split()] for i in range(count_items)]
mas.sort(key=lambda x: x[0]/x[1], reverse=True)

cost = weight = 0

for i in range(len(mas)):
    current_item = 0
    
    while weight < max_weight and current_item < mas[i][1]:
        cost += mas[i][0]/mas[i][1]
        weight += 1
        current_item += 1

print(f"{cost:.3f}")
