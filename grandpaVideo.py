import streamlit as st
from PIL import Image
import io

# Load the MP4 file
video_file = open('Grandpas_90th.mp4', 'rb')
video_bytes = video_file.read()

st.title("Grandpa's 90th Birthday Video")
st.subheader("Here is a custom website for you Nana \U0001F600")
st.subheader("You can download the video to your computer from here too.")

# Display the MP4 video
st.video(video_bytes)

# Add a download button for the MP4 file
with open("Grandpas_90th.mp4", "rb") as f:
    video_bytes = f.read()
st.download_button(label="Download MP4", data=video_bytes, file_name="Grandpas_90th.mp4")
