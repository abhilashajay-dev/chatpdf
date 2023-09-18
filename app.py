import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS




def get_pdf_text(Pdf_docs):
    text = ""
    for pdf in Pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text    

        


def get_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len

    )
    chunks = text_splitter.split_text(raw_text)
    return chunks



def get_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(chunks, embeddings)
    return vector_store







def main():
    load_dotenv()

    st.set_page_config(page_title='ChatPdf', page_icon=':Lion:', layout='wide')
    st.header("Chat with your PDF")
    st.subheader("Upload your PDF and start chatting with it")
    st.text_input("Ask your question here")

    with st.sidebar:
        st.subheader("Documnets")
        Pdf_docs = st.file_uploader("Upload your PDF's here", type=['pdf'], accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner('Processing'):
                # get pdftest

        
                raw_text = get_pdf_text(Pdf_docs)

                # text Chuncks
                chunks = get_chunks(raw_text)

                # create vector Store
                vector_store = get_vectorstore(chunks)








if __name__ == '__main__':
    main()