def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    pos = []
    for i in arr:
        if i > 0:
            pos += [i]
    sum_neg = []        
    for o in arr:
        if o < 0:
            sum_neg += [o] 
    return [len(pos), sum(sum_neg)]
