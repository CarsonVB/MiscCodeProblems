import math


def parent(i):
    return math.floor(i / 2)


def left(i):
    return 2 * i


def right(i):
    return (2 * i) + 1


def maxheapify(A, i, leng):
    n = leng - 1
    l = left(i)
    r = right(i)
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxheapify(A, largest, leng)


def buildmaxheap(A, leng):
    n = leng - 1
    i = math.floor(n / 2)
    while i >= 0:
        maxheapify(A, i, leng)
        i = i - 1


def heapsort(A, leng):
    n = leng - 1
    buildmaxheap(A, leng)
    i = n
    while i >= 1:
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        leng = leng - 1
        maxheapify(A, 0, leng)
        i = i - 1
    A.reverse()
    thing = leng
    return A


def extractmaximum(A, leng):
    if leng < 1:
        print('error')
    else:
        max = A[0]
        A[0] = A[leng]
        leng = leng - 1
        maxheapify(A, 0, leng)
        return max


def increasekey(A, i, key):
    if key < A[i]:
        print('error 2')
        return
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        temp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = temp
        i = parent(i)


A = [30, 10, 15, 9, 7, 50, 8, 22, 5, 3]
print(heapsort(A, len(A)))
