def selection_sort(a):
    n = len(a)
    for f in range(n - 1):
        maxindex = f
        for g in range((f+1), n):
            if a[g] > a[maxindex]:
                maxindex = g
        if maxindex != f:
            tmp = a[f]
            a[f] = a[maxindex]
            a[maxindex] = tmp
    return alist


alist = []
arraysize = int(input("Please enter the size of your array:"))
for i in range(0, arraysize):
    value = float(input("Please enter element #" + str(i) + " of your array:"))
    alist.append(value)
    i += 1
print("unsorted array is " + str(alist))
alist = selection_sort(alist)
print("sorted array is " + str(alist))
