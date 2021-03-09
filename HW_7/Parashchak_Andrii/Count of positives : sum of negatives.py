def count_positives_sum_negatives(arr):
    if bool(arr) == False:
        return arr
    else:
        list_2=[x for x in arr if x > 0]
        list_3=[x for x in arr if x < 0]
        result=[len(list_2),sum(list_3)]
        print (result)

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
count_positives_sum_negatives([])