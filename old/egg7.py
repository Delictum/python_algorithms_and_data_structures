with open('dataset_24465_4.txt', 'r') as r_f, open('res_dataset_24465_4.txt', 'w') as w_f:
    text = r_f.read().splitlines()
    for i in range(len(text)-1, -1, -1):
        w_f.write(text[i]+'\n')
