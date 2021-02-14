def filter_words(st):
    alphabet_lower_list = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet_upper_list = ["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    st_b = str(st).lstrip()
    list_st=[]
    for i in range(len(st_b)):
        list_st.append(st_b[i])
    for i in range(len(list_st)):
        for j in range(len(alphabet_upper_list)):
            if list_st[i] == alphabet_upper_list[j]:
                list_st[i] = alphabet_lower_list[j]
    index_upper = alphabet_lower_list.index(list_st[0])
    list_st[0]=alphabet_upper_list[index_upper]
    
    st_a = "".join(list_st)
    return " ".join(st_a.split())