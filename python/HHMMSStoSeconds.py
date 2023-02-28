def split_function(string, character):
    temp_hold = ''
    temp_list = []
    for x in string:
        if x != character:
            temp_hold += x
        else:
            temp_list.append(temp_hold)
            temp_hold = ''
    if temp_hold != '':
        temp_list.append(temp_hold)
    return temp_list

time_string = input('Please enter the time in HH:MM:SS')
time_string = split_function(time_string, ',')[0]
time_components = split_function(time_string, ':')
time_total = 0
for i, entry in enumerate(time_components):
    time_total += int(entry) * pow(60, len(time_components)-(i+1))
print(time_total)