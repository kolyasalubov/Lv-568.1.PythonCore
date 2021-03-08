def reverse_list(l):
  # 'return a list with the reverse order of l'
    reversed_list = []
    for x in l:
        reversed_list.insert(0, x)
    return reversed_list