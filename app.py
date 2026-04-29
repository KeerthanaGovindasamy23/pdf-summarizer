import streamlit as st
import fitz # This is the PyMuPDF library (The PDF Reader)
import google.generativeai as genai # This is the Gemini library (The Brain)

# 1. Setup the AI Brain
genai.configure(api_key="AIzaSyB3dPtooPw64Ifefr3V_Vz9Nbyg3Zqln7k") # You get this from AI Studio
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Create the Website Layout (The "Face")
st.title("📚 Keerthana's PDF Summarizer")
st.write("Upload a document and I'll summarize it for you!")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    # 3. Read the PDF (Using PyMuPDF)
    with st.spinner("Reading the PDF..."):
        # Open the uploaded file
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        
    # 4. Ask Gemini to summarize (The "API Call")
    with st.spinner("AI is thinking..."):
        prompt = f"Summarize this document clearly in bullet points:\n\n{full_text}"
        response = model.generate_content(prompt)
        
        st.subheader("Summary:")
        st.write(response.text)
