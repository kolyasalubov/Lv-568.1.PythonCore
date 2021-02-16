# for x in range(10):
#     if x%2==0:
#         print("even num ",x)
# for x in range(10):
#     if x%2==1:
#         print("odd num ",x)
# for x in range(10):
#     if x%2==0 and x%3==0:
#         pass
#     else:
#         print("num is not divisible by two and three ", x)
#
x = [print("even num", x) for x in range(10) if x % 2 == 0]
x = [print("odd num", x) for x in range(10) if x % 2 == 1]
x = [print("num is divisible by two and three ",x) if x % 2 == 0 and x % 3 == 0 else print("num is not divisible by two and three ", x) for x in range(10)]