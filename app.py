import openai
import streamlit as st
from audio_recorder_streamlit import audio_recorder
from audio_function import NamedBytesIO, transcribe_audio
from prompts import PROMPT_SUMMARY, REFINE_PROMPT_SUMMARY
from llm_functions import initialize_llm, initialize_summary, split_text

#setting open api key
openai_api_key="OPENAI_API_KEY"

#setting openai api key for whisper
openai.api_key="OPENAI_API_KEY"

with st.container():
    st.markdown("""
# Audio Transcription Into Detailed meeting summaries
With this new app, `Whisper Notes` you can effortlessly transform your recorded or general thoughts into comprehinsive meettings notes. This streamlit appliction leverages the power for accurate audio transcription and employs Langchain's capabilities to post-process the transcriptions into detailed meetings summaries.
                
 Here's how 'Whisper Notes' works:
1. **Record and Transcribe:** Using your phone or laptop, you can record meetings or any spoken content you want to capture. OpenAI Whisper, a cutting-edge automatic speech recognition system, processes the audio and convert it into text with remarkable accuracy.

2. **Generate Meeting Summaries:** The transcribed text is then passed through langchain, a robust tool specialized in language model prompt generation. Langchain refines and structures the text, converting it into detailed and well organized meeting summaries.
3. **Efficient and Effective:** 'Whisper Notes' streamlines the process of note-taking, saving you valuable time and effort. Instead of manually transcribing and summarizing lengthy recordings, you can rely on the power of AI to produce comprehensive meeting notes automatically.

4. **Versatile Use:** Whether you're a professional in a corporate setting or a student attending lectures, 'Whisper Notes' is a versatile tool that caters to various scenarios. Record your ideas, brainstorming sessions, or important meetings, and transform them into actionable and easy-to-digest notes.

5. **Seamless User Experience:** The user interface of 'Whisper Notes' is designed to be intuitive and user-friendly. With just a few clicks, you can turn your audio recordings into detailed meeting summaries effortlessly.

6. **Privacy and Security:** We understand the importance of data privacy. Rest assured, your recordings and transcriptions are processed securely and won't be shared with any third parties.

`Whisper Notes` is part of the ongoing exploration of the capabilities of OpenAI Whisper and LangChain. Experience the convenience and productivity of automatic meeting note generation today!

Check out the the code and the development process on my [Github](https://github.com//AKASH4148). 
                            
"""
                )
with st.container():
    #Experimental Streamlit feature to record audio. Set the pause_threshold to the amount of selent seconds you want to wait before the recording steps.
    audio_bytes=audio_recorder(text="Record your meeting", pause_threshold=5, icon_size="5x")
    if audio_bytes:
        st.audio(audio_bytes)

        #convert the audio bytes to a NameByteIO object
        audio_bytes=NamedBytesIO(audio_bytes, name="audio.mp3")

        #Get response from openai whisper api
        response= transcribe_audio(audio_bytes=audio_bytes, openai_api_key=openai_api_key)

        #Assign the transcript to a variable
        transcript=response["text"]

        #Split the transcprit into chunks
        transcript_chunks= split_text(data=transcript, chunk_size=2000, chunk_overlap=50)

        #initialize the large language model
        llm=initialize_llm(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-16k", temperature=0.2)

        #initialize the summarize chain
        summarize_chain= initialize_summary(llm=llm, chain_type="refine", question_prompt=PROMPT_SUMMARY, refine_prompt=REFINE_PROMPT_SUMMARY)

        #run the summarize chain
        summary=summarize_chain.run(transcript_chunks)

        #Print the summary
        st.code(summary)


    