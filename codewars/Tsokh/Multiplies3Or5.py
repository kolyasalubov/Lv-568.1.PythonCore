def solution(number):
    new_list = []
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0 and x > 0:
            new_list.append(x)
    new_list = set(new_list)
    return sum(new_list)