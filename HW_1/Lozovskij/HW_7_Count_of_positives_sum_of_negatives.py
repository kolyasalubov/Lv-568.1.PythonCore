def count_positives_sum_negatives(arr):
    positive_num=0
    negative_num=0
    if arr==[]:
        return []
    for i in arr:
        if i>0:
            positive_num+=1
        else:
            negative_num+=i
    return [positive_num,negative_num]