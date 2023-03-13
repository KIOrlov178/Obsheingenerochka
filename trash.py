def bin_8 (a):
    b = bin(a)[2:]
    c = ('0'*(8-len(b)))+b
    d = list(c)
    e = [int(elem) for elem in d]
    return e

print(bin_8(255))