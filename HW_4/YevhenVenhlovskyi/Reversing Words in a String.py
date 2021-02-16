## Reversing Words in a String

def reverse(st):
    # Your Code Here
    st_list = st.split()
    st_list = reversed(st_list)
    st = " ".join(st_list)
    st.split()
    return st