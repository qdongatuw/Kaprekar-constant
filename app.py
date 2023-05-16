import streamlit as st

def calculation(n):
    num_list = []
    num_list.append((0,0,n))
    digits_num = len(str(n))
    new_num = n
    while True:
        s = list(str(new_num).zfill(4))
        
        big = int(''.join(sorted(s, reverse=True)))
        small = int(''.join(sorted(s)))
        ans = big - small
        num_list.append((big, small, ans))

        if ans == new_num:
            return num_list
        new_num = ans
        

st.sidebar.header('Hi Mason!')
st.title("Kaprekar's constant")

ini_numer = st.sidebar.number_input('Input a number:', value=2048)
l = calculation(ini_numer)
st.write(f'The initial number is {l[0][-1]}')
for i in l[1:]:
    st.write(f'{i[0]} - {i1[1]} = {i[2]}')
st.write(f'{l[-1][-1]}')
