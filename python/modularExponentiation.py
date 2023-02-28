def binary_k(k):
    K = []
    tmp = k
    i = 0
    while tmp > 0:
        K.append(int((tmp % 2)))
        tmp = (tmp-K[i])/2
        i += 1
    return K


def modular_expo(a, k, n):
    if n == 1:
        return 0
    b = 1
    if not k:
        return b
    A = a
    if k[0] == 1:
        b = a
    for i in range(1, len(k)):
        A = (A*A) % n
        if k[i] == 1:
            b = (A*b) % n
    return b


print("a^k mod n")
x = int(input("Please enter a:"))
y = int(input("Please enter k:"))
z = int(input("Please enter n:"))
Y = binary_k(y)
mE = modular_expo(x, Y, z)
print(mE)
