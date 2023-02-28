def eea(a, b):
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    i = 1
    q = [0, 0]
    while r[i] != 0:
        q.append(r[i-1] / r[i])
        r.append(r[i-1] % r[i])
        s.append(s[i-1] - q[i] * s[i])
        t.append(t[i-1] - q[i] * s[i])
        i += 1
    print("GCD = " + str(r[i-1]))
    return t, s


x = int(input("Please enter your first integer:"))
y = int(input("Please enter your second integer:"))
eea(x, y)
