import streamlit as st

# Setting page configuration at the top level
st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

def main():
    st.header("Chat with multiple PDFs")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Upload your PDFs")
        st.file_uploader("Upload your PDFs here and click on 'Process", type="pdf", accept_multiple_files=True)

if __name__ == '__main__':
    main()
