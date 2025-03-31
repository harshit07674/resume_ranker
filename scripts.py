import pdfplumber
import spacy

def extractText(padf_path):
    text=''
    with pdfplumber.open(padf_path) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()+'\n'
    return text.strip()

path="./harshit_khandelwal_software_resume (2).pdf"
print(extractText(path))