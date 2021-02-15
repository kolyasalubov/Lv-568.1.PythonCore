def enough(cap, on, wait):
    ''' function name enough
        input parametrs three: cap, on, wait
        we calculate the number of extra passengers
        return 0 if there are no extra passengers
        return s if there are extra passengers
    '''
    s = wait-(cap - on)
    if s > 0:
        return print(int(s))
    return print(int(0))


a = int(input())
b = int(input())
c = int(input())

t = enough(a, b, c)
