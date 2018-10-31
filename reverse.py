text_list = ['a', 'b', 'c', 'd', 'e']
m = len(text_list)/2
last_index = len(text_list) - 1
first_index = 0
while first_index < m:
    temp = text_list[last_index]
    text_list[last_index] = text_list[first_index]
    text_list[first_index] = temp
    last_index -= 1
    first_index += 1
print(text_list)