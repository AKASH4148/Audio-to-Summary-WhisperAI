# Audio-to-Summary-WhisperAI
This code model is an app that uses OpenAI Whisper and Langchain to transcribe audio recordings into detailed meeting summaries.

To use the app, first, install the dependencies by running the following command:

```
pip install -r requirements.txt
```

Once the dependencies are installed, run the app by running the following command:

```
streamlit run app.py
```

The app will then open in your browser. You can then click the "Record your meeting" button to start recording your audio. Once you are finished recording, click the "Transcribe audio" button to transcribe the audio into text. The transcribed text will then be passed to Langchain, which will generate a detailed meeting summary. The summary will be displayed in the app's output.

Here are some additional details about the code:

* The `app.py` file contains the main code for the app. This file defines the app's user interface and logic.
* The `audio_function.py` file contains the code for transcribing audio recordings. This file uses the OpenAI Whisper API to transcribe audio into text.
* The `llm_functions.py` file contains the code for initializing the large language model (LLM) and the summary chain. This file uses the Langchain library to initialize the LLM and the summary chain.
* The `prompts.py` file contains the code for the prompts used by the summary chain. These prompts are used to generate the detailed meeting summaries.

I hope this helps!
