import  streamlit as st

st.title("Marvellou Infosystem")

st.header("Marvellous Addition Calculator")

no1 = st.number_input("Enter First Number",value = 0,step=1)
no2 = st.number_input("Enter Second Number",value = 0,step=1)

if st.button("Addition"):
    result = no1 + no2

    st.success("Addition is "+str(result))