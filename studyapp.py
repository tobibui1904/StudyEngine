import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="StudyEngine",page_icon=":book:",layout="wide")
image=Image.open("studyengine.jpg")
st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(204, 49, 49); } </style>""", unsafe_allow_html=True)

with st.sidebar:
    selected=option_menu(
        menu_title="Main menu",
        menu_icon="book",
        options=["Home","Opportunities","Duration","Search","Questions_Opportunities","Activity"]
    )
if selected=="Home":
    left4_column,middle6_column,right4_column=st.columns(3)
    with middle6_column:
        st.image(image)
    st.markdown("<h1 style='text-align: center; color: orange;'>Welcome to Study Engine</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>Register to start finding opportunities made for you!</h1>", unsafe_allow_html=True)
    left_column,middle_column,right_column=st.columns(3)
    with right_column:
        st.button("ORGS AND CLUBS")

    username=st.text_input("USERNAME")
    password=st.text_input("PASSWORD")
    email=st.text_input("E-MAIL")
    phone=st.text_input("PHONE NUMBER")
    if email=='':
        pass
    else:
        left1_column,middle1_column,right1_column=st.columns(3)
        with right1_column:
            st.button(" STARTS")

if selected=="Opportunities":
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: orange;'>Help us find the best opportunities for you</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>Indicate your age:</h1>", unsafe_allow_html=True)
    number = st.number_input('Insert a number',min_value=1,max_value=120)
    st.markdown("<h1 style='text-align: center; color: orange;'>I want opportunities related to:</h1>", unsafe_allow_html=True)
    left2_column,middle2_columnm,middle3_column,right2_column=st.columns(4)
    with middle2_columnm:
        st.button("Science")
        st.button("Leadership")
        st.button("Humanities")
    with middle3_column:
        st.button("Technology")
        st.button("Volunteering")
        st.button("Others")
    with right2_column:
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        x=st.button("Next")

if selected=="Duration":
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: orange;'>Duration(Optional)</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>I want an activity with a duration of:</h1>", unsafe_allow_html=True)
    left3_column,middle4_columnm,middle5_column,right3_column=st.columns(4)
    with middle4_columnm:
        st.button("1 day")
        st.button('1 month')
    with middle5_column:
        st.button("1 week")
        st.button("1 year")
    left5_column,middle7_columnm,right5_column=st.columns(3)
    with middle7_columnm:
        image1=Image.open("clock.jpg")
        st.image(image1)
    with right5_column:
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.button("Next!")

if selected=="Search":
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: orange;'>Save your search</h1>", unsafe_allow_html=True)
    left6_column,middle8_columnm,right6_column=st.columns(3)
    with middle8_columnm:
        st.write("By saving your search")
        st.write("you can access the")
        st.write("results whenever you")
        st.write("without answering the")
        st.write("previous questions again")
    left7_column,middle9_columnm,right7_column=st.columns(3)
    with middle9_columnm:
        st.button("V")
    with right7_column:
        st.button("X")

if selected=="Questions_Opportunities":
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: orange;'>Answer the following questions for us to know what opportunities your organization offers</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>Activity related to</h1>", unsafe_allow_html=True)
    left8_column,middle10_columnm,middle11_column,right8_column=st.columns(4)
    with middle10_columnm:
        st.button("Science!")
        st.button("Leadership!")
        st.button("Humanities!")
    with middle11_column:
        st.button("Technology!")
        st.button("Volunteering!")
        st.button("Others!")
    with right8_column:
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        x=st.button("next!")

if selected=="Activity":
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: orange;'>About the activity</h1>", unsafe_allow_html=True)
    st.text_input("NAME")
    st.number_input('AGE RANGE',min_value=1,max_value=120)
    st.text_input("Durations")
    st.selectbox(
        "Meeting format",
        ('In-Person', 'Virtual'))
    st.text_area("Where to sign up or apply")
    st.text_area('Description')
