for i in range(1, 101):
    if ((i % 3) == 0) or ((i % 5) == 0):
        output = ''
        if (i % 3) == 0:
            output += 'Fizz'
        if (i % 5) == 0:
            output += 'Buzz'
    else:
        output = i
    print(output)