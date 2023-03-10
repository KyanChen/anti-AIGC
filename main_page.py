import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="A demo of anti-AIGC",
    page_icon="👋",
    layout='centered'
)

st.write("# A Demo of Anti-AIGC 👋")


def inference_text(text: str) -> float:
    pass
    prob = len(text)
    return prob


def inference_img(img) -> float:
    img = np.array(img)  # HxWx3
    pass
    prob = 0.
    return prob


st.write("## Anti AI Text Generation:")

txt = st.text_area('Text to Analyze', '''
It was the best of times, it was the worst of times, it was
the age of wisdom, it was the age of foolishness, it was
the epoch of belief, it was the epoch of incredulity, it 
was the season of Light, it was the season of Darkness, it
was the spring of hope, it was the winter of despair, (...)
    ''')
if len(txt):
    prob_text = inference_text(txt)
    st.write(f'The Probability of the Text Generation by AI: **{prob_text:.2f}**')


st.write("## Anti AI Image Generation:")
my_upload = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    img = Image.open(my_upload).convert('RGB')
    st.image(img, width=400)
    prob_img = inference_img(img)
    st.write(f'The Probability of the Image Generation by AI: **{prob_img:.2f}**')
