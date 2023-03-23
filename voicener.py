import streamlit as st
import numpy as np
import pandas as pd
import whisper 
from audio_recorder_streamlit import audio_recorder
import io
import soundfile as sf
from pydub import AudioSegment
from pydantic import BaseModel
from pydub import AudioSegment
from io import BytesIO
import whisper
import base64
import torch
import numpy as np
import pandas as pd 
import os

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
        w_audio = whisper.load_audio(filename)
        pad_w_audio =whisper.pad_or_trim(w_audio)
        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = whisper.load_model("small.en")
        model = model.to(torch_device)
        mel = whisper.log_mel_spectrogram(pad_w_audio).to(model.device)
        decode_options = dict(language="en")
        transcribe_options = dict(task="transcribe", **decode_options)
        transcription = model.transcribe(filename, **transcribe_options)
        result = transcription["text"]
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
