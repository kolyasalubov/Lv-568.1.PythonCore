# def revers(st):
#     a, b = st.split()
#     return b + " " + a


# s = str(input("Введи два слова: "))
# m = revers(st)
# print(m)

def reverse(st):
    st = st.split()
    st.reverse()
    return " ".join(st)


s = str(input("Введи строку: "))
a = reverse(s)
print(a)


# def reverse(stg):
#     return ' '.join(reversed(stg.split()))

# def reverse(stg):
#     return ' '.join(reversed(stg.split()))

# def reverse(st):
#     s = st.split()
#     return ' '.join(s[::-1])
