def count_positives_sum_negatives(arr):
    pos=0
    neg=0
    if arr==[]:
        return arr
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=i
    return [pos,neg]
        