def count_positives_sum_negatives(arr):
    arr2 = []
    sum_neg = 0
    sum_count_pos = 0
    for element in arr:
        if element > 0:
            sum_count_pos+=1
        else:
            sum_neg+=element
    if arr == []:
        return arr2
    else:
        arr2.append(sum_count_pos)
        arr2.append(sum_neg)
        return arr2
    
print(count_positives_sum_negatives([0,0,0,0]))
