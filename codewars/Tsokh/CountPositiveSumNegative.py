def count_positives_sum_negatives(arr):
    #your code here
    pos = []
    neg = []
    if arr:
        for i in arr:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
        return [len(pos), sum(neg)]
    else:
        return []