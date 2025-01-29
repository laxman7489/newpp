import streamlit as st
st.title("Python First Project")
st.subheader("Laxman")
Name = st.text_input("Enter Your Name")
Fname = st.text_input("Enter Your Father name")
Address = st.text_area("Enter Your Address")
Class   = st.selectbox("Enter Your Class : ",(1,2,3,4,5,6))
button=st.button("Done")
if button : st.markdown(f"""   
name: {Name}
Father name: {Fname}
Your Address: {Address}
Your Class : {Class}""")