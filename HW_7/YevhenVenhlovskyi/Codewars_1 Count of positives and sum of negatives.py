def count_positives_sum_negatives(arr):
    if bool(arr) == False:
        return arr
    else:
        list_2=[x for x in arr if x > 0]
        list_3=[x for x in arr if x < 0]
        result=[len(list_2),sum(list_3)]
        print (result)

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
# count_positives_sum_negatives([])

###################################################################################

# def count_positives_sum_negatives(arr):
#     if bool(arr) == False:
#         return arr
#     else:
#         list_2=[]
#         list_3=[]
#         for x in arr:
#             if x > 0:
#                 list_2.append(x)
#             else:
#                 list_3.append(x)
#         a=len(list_2)
#         b=sum(list_3)
#         result=[a,b]
#         print (result)

# count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
#count_positives_sum_negatives([])

##################################################################################

# def count_positives_sum_negatives(arr):
#     count_pos = 0
#     sum_neg = 0
#     for i in arr:
#         if i > 0:
#             count_pos += 1
#         else:
#             sum_neg += i
#     ans = []
#     ans.append(count_pos)
#     ans.append(sum_neg)
#     return ans

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(count_positives_sum_negatives(arr))

##################################################################################

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# list_2=[]
# list_3=[]

# for x in list_1:
#     if x >= 0:
#         list_2.append(x)
#     else:
#         list_3.append(x)
# a=len(list_2)
# b=sum(list_3)
# list_4=[a,b]
# print(list_4)