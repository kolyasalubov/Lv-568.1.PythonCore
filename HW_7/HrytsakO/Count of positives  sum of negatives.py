def count_positives_sum_negatives(arr):
    count_pos = []
    sum_neg = []
    for x in arr:
        
        if x >= 0:
            count_pos.append(x)
        else:
            sum_neg.append(x)
    return [len(set(count_pos)), sum(sum_neg)]
