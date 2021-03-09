## Grasshopper - Summation

def summation(num):
    y=0
    for x in range (1,num+1):
        y=y+x
    print(y)

summation(8)

# def summation(num):
#     return sum(range(1,num+1))

# test.assert_equals(summation(1), 1)
# test.assert_equals(summation(8), 36)
# test.assert_equals(summation(22), 253)
# test.assert_equals(summation(100), 5050)
# test.assert_equals(summation(213), 22791)