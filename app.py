import streamlit as st
from eli5 import *

st.title('ELI5')
st.text("Ask me about anything and I'll try to explain it to you like a 5 year old.")
st.markdown("""---""")

input_area = st.text_input("Just enter a topic below")

keywords = st.text_input("Provide more related keywords (seperated by commas) for better results")


if(st.button('Submit')):
    if len(input_area) > 0:
        ans = ask(input_area,keywords)
        st.write(ans)
        # st.success("Shukriya!")
    else:
        st.error("Njn pottana....?")