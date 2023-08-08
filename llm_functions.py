from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document

#Function to initialize the large model
def initialize_llm(openai_api_key, model_name, temperature):
    llm=ChatOpenAI(openai_api_key=openai_api_key, model_name=model_name, temperature=temperature)
    return llm

#Function to initialize the summary chain

def initialize_summary(llm, chain_type, question_prompt, refine_prompt):
    strategy_chain=load_summarize_chain(llm=llm, chain_type=chain_type, question_prompt=question_prompt, refine_prompt=refine_prompt)
    return strategy_chain

#function to split the transcipt into chunks
def split_text(data, chunk_size, chunk_overlap):
    text_splitter= TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts=text_splitter.split_text(data)
    #Creates documents for further processing
    docs=[Document(page_content=t) for t in texts]
    return docs