

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


a = create_array(10)
print(a)
