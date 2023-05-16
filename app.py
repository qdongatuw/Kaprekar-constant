import streamlit as st

def calculation(n):
    num_list = []
    num_list.append((0,0,n))
    digits_num = len(str(n))
    new_num = n
    while True:
        s = list(str(new_num).zfill(digits_num))
        
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
if ini_numer > 9999 or ini_numer < 100:
    st.info('It only works for 3 or 4 digit numbers.')
    st.stop()
l = calculation(ini_numer)
st.write(f'The initial number is {l[0][-1]}')
for i in l[1:]:
    st.write(f'{i[0]} - {i[1]} = {i[2]}')
st.write(f'End in {l[-1][-1]}')
