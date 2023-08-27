import streamlit as st

#title comment
st.title("My First Streamlit App")
st.header("Hello WORLD")
st.write("Here's our first attempt at using streamlit to create a basic app.")

st.markdown("mark down")

st.success("Success!")
st.info("Info")
st.error("Error")
st.warning("Warning")
st.help("help")
#st.exeption("Exception")

a = 10
st.write(a)

#check box
if st.checkbox("show"):
    st.write("you have selected the checkbox")

#radio button
option = st.radio("select",["apple","banana","cherry"])
st.write("you have selected",option)

#selectbox
option = st.selectbox("select",["apple","banana","cherry"])
st.write("you have selected",option)

#slider
range = st.slider("select :",1,100)
st.write("you have selected",range)

#button
if st.button("click me"):
    st.write("you have clicked the button")

#Text Input
name = st.text_input("enter your name")
st.write("your name is",name)
password = st.text_input("enter your password",type="password")

#Text area
message = st.text_area("enter your message")

#datetime
date = st.date_input("enter your date")
time = st.time_input("enter your time")

#json
data = st.json({"name":"john","age":23})

#code
st.code("import streamlit as st")

#spinner
st.sidebar.title("My Side Bar")
st.sidebar.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

#expander
with st.expander("click me"):
    st.write("you have clicked the expander")

st.write("this is the end")
st.write("this is the end")
st.write("this is the end")

#upload file
data = st.file_uploader("upload file")
