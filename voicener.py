import streamlit as st
import numpy as np
import pandas as pd
import whisper 
from audio_recorder_streamlit import audio_recorder
import io
from pydub import AudioSegment
from io import BytesIO
import whisper
import numpy as np
import pandas as pd 
import os
import torch
import ffmpeg
import speech_recognition as sr


def download_link(content, filename):
    """Function to create a download link for a given string."""
    # Create a hyperlink with the given content and filename
    href = f'<a href="data:text/plain;charset=utf-8,{content}" download="{filename}">Download {filename}</a>'
    return href

def main():
    audio_bytes = audio_recorder(
            text="Click icon on the right to record",
            recording_color="#088F8F",
            neutral_color="#474A8F",
            icon_name="fa-solid fa-microphone",
            icon_size="3x",
            pause_threshold=3.0
        )
    if audio_bytes:
        s = BytesIO(audio_bytes)
        AudioSegment.from_file(BytesIO(audio_bytes)).export('audio.mp3', format='mp3')
        filename = "audio.mp3"
        with sr.AudioFile('audio.mp3') as source:
            audio_data = r.record(source)
        
        r = sr.Recognizer()
        text = r.recognize_google(audio_data, language='en-US')
        
        st.write(result)
        if result: 
            m = st.text_input('-', 'none', 50)
            if m != 'none':
                result += ' | '
                result += m
                st.write(result)
                filename = m
                filename += '.txt'
                st.download_button('Download some text', result)
        
            

        
         
                            
if __name__ == "__main__":
    main()
