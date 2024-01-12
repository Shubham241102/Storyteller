import google.generativeai as genai
import base64
import io
import json
import mimetypes
import pathlib
import pprint
import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.getenv("GEMINI_API")
genai.configure(api_key=os.getenv("GEMINI_API"))
#genai.configure(api_key='AIzaSyAjk7S9WKFHPKpI-FLV-8YMez9Q_Ha1uhs')
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
model = 'gemini-pro'

with st.sidebar:
    st.title("storyteller")
    st.write('With an intuitive user interface and a user-friendly design, this web application invites users to embark on a creative odyssey. By simply providing a few details about the individual, such as their name, interests, and passions, the application harnesses the transformative power of Gemini Pro to generate a personalized poem. Whether it"s a heartfelt tribute to a loved one, a celebration of personal achievements, or a reflective exploration of lifes complexities, the application adapts to the users preferences, producing poems that resonate with authenticity and emotional depth.')

    st.title("Storyteller")
aoi = [
    "Reading",
    "Exercising",
    "Listening to music",
    "Watching movies",
    "Playing esports",
    "Traveling",
    "Cooking",
    "Gardening",
    "Photography",
    "Art and crafts",
    "DIY projects",
    "Learning new skills",
    "Meditation",
    "Spending time with friends and family",
    "Volunteering",
    "Technology",
    "Science",
    "History",
    "Politics",
    "Economics",
    "Philosophy",
    "Psychology",
    "Sociology",
    "Art",
    "Music",
    "Literature",
    "Film",
    "Fashion",
    "Travel",
    "Food and drink",
    "Health and wellness",
    "Sports",
    "Current events"
]

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input('Name')
    age = st.text_input('Age')
    interest = st.multiselect('Hobbies',options=aoi)
with col2:
    Address = st.text_input('State/Country ')
    profession = st.text_input('occupation')
    fav_movie_singer = st.text_input('Favourite movies/singer',placeholder='separated by comma')
with col3:
    gender = st.selectbox('Gender',options=['Male','Female'])
    language = st.selectbox('story language',['English','Hindi'])
    incident = st.text_input(' special incident happend in life',placeholder='seperated by comma')

contents = 'A person whose name is '+name+'. Gender is '+gender+'.Age is '+age+'. Area of interest are '+",".join(interest)
contents += '. Lives in state of '+Address+'.'
contents += 'Profession is '+profession+'. Favourite show and movies are '+fav_movie_singer+'.'
contents += 'Some of the incidents happened till now in my life were '+incident+'. which were some of the moments of my life both happy/sad/exciting'
contents += 'Write a high quality realistic story that looks like a story authored by a man and not by AI about 100 lines divided into certain chapters describing the person which will be a masterpiece when read by a user . Language of the poem would be'+language+'.'

a = st.button('Generate',key='gen')
if st.session_state.get("gen"):
    with st.spinner('Wait for it'):
        gemini = genai.GenerativeModel(model_name=model)
        response = gemini.generate_content(
            contents,
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False)

        if generation_config.get('candidate_count', 1) == 1:
            try:
                st.text_area(label ="",value=response.text,height=500)
            except Exception as e:
                st.failure('Retry after Some time')
        else:
            st.failure('It is Prohibited.')
        
    st.success('Done')
