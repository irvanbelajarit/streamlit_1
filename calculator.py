import streamlit as st

st.title("My Calculator Python App")

angka_satu = st.number_input("Masukan Angka Pertama",value=0)
angka_dua = st.number_input("Masukan Angka Kedua",value=0)

operation = st.selectbox("Pilih Operasi",["+","-","*","/"])
st.write("Hasilnya Adalah : ")
if operation == "+":
    st.write(angka_satu + angka_dua)
elif operation == "-":
    st.write(angka_satu - angka_dua)
elif operation == "*":
    st.write(angka_satu * angka_dua)
elif operation == "/":
    st.write(angka_satu / angka_dua)