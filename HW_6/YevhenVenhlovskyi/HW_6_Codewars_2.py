## Function of changing texts to correct form

def filter_words(st):
    st=st.lower()
    st=st.capitalize()
    res = " ".join(st.split())
    print(res)

filter_words('HELLO    world!')