def solution(number):
    if number <= 0:
        return 0
    else:
        list = []
        sum = int()
        for x in range(1, number, 1):
            if x % 3 == 0 or x % 5 == 0:
                list.append(x)
                sum += x
        return sum


print(solution(0))