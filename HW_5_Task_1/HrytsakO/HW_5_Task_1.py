Even_db2 = []
Odd_db3 = []
Other = []
for x in range(1, 11):
    if x % 2 == 0:
        Even_db2.append(x)
    elif x % 3 == 0 and x % 2 == 1:
        Odd_db3.append(x)
    else:
        Other.append(x)
print("""Even numbers that are divisible by 2 : {}
Odd numbers, which are divisible by 3 : {}
Numbers that are not divisible by 2 and 3 : {}
""".format(Even_db2, Odd_db3, Other))
