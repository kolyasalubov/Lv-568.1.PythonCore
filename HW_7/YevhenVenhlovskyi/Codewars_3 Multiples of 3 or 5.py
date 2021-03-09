## Multiples of 3 or 5

def solution(number):
    if number <0:
        return 0
    else:
        list_1=[]
        for x in range (1,number):
            if x%3==0 or x%5==0:
                list_1.append(x)
        print(sum(list_1))

solution(10)
