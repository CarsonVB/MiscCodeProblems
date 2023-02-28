def two_largest(a):
    n = len(a)
    large_1 = 0
    large_2 = 0
    for j in range(0, n):
        if a[j] > large_1:
            large_2 = large_1
            large_1 = a[j]
        elif large_2 < a[j]:
            large_2 = a[j]
    print("The two largest numbers present in the list are " + str(large_1) + " and " + str(large_2) + ".")


alist = []
arraysize = int(input("Please enter the size of your array:"))
for i in range(0, arraysize):
    value = float(input("Please enter element #" + str(i) + " of your array:"))
    alist.append(value)
    i += 1
two_largest(alist)
