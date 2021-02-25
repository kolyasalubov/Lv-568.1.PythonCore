s = "String"
c = ""
for x in s:
    x += x
    c += ''.join(x)
print(c)