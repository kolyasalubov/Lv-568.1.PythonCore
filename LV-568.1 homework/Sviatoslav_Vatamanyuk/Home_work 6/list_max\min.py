# q = (int(input("enter quantity of numbers  ")))
# list = []
# for i in range(q):
#     list.append(int(input("enter ur number ")))
# print(min(list))
# print(max(list))
# print(list)

list = [int(input("enter ur number ")) for i in range(int(input("Enter quantity ")))]
print(min(list))
print(max(list))
print(list)