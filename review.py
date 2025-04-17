
triangle = 7
center = triangle // 2
for j in range(-center,center+1):
    num_star = triangle - abs(j) * 2
    to_print = '*' * num_star
    print(to_print)

data = [1, 2, 3, 4, 2, 1, 3, 1, 2, 2]
count_data = []
for j in data:
    count_data.append(data.count(j))

max_freq = max(count_data)
max_num = data[count_data.index(max_freq)]
print(f'최빈치 : {max_num}, 개수 : {max_freq}')