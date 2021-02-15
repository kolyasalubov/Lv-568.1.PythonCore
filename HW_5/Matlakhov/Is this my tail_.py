# def correct_tail(body, tail):
#     """function name correct_tail
#        input paranetrs two: body, tail
#        Check if the tail is the same as the last letter of the first argument body.
#        if matches then return True elso return False """
#     if body[-1] == tail:
#         return True
#     else:
#         return False

def correct_tail(body, tail):
    return True if body[len(body)-len(tail):len(body)] == tail else False


r = correct_tail('dog', 'g')
print(r)
print(len('dog'))

body = 'dog'
tail = 'g'
print(body[len(body)-len(tail):len(body)])
