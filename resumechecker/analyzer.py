import pdfplumber
import spacy
from groq import Groq
import json

def extractText(padf_path):
    text=''
    with pdfplumber.open(padf_path) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()+'\n'
    return text.strip()

grok_key='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'

def analyze_resume_with_llm(resume_text:str,job_description:str)->dict:
    prompt = f"""
     You are an AI assistant that analyzes resumes for diffrent domains in software engineering jobs.
     Given a resume and a job description, extract the following details:

     1. Identify all the skills mentioned in the resume.
     2. Calculate the total years of experience
     3. Categories the projects based on the domain (e.g, AI, web development, cloud etc)
     4. Rank the resume rlevance to the job description on a scale of 0 to 100.
     5. Suggest some relevant courses based on resume that will help the candidate to get the job.


     Resume:{resume_text}

     Job Description:{job_description}

     Provide the output in valid JSON format with this structure:
     {{
     'rank':"<percentage>",
     "skills":["skill1","skill2","skill3",......]
     "total_experience":"<number of years>",
     "project_category":["category1","category2",......],
     "relevant_courses":["course1","course2","course3",......]
     }}
    """
    try:
        client = Groq(api_key=grok_key)
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{'role':'user','content':prompt}],
            temperature=0.7,
            response_format={'type':'json_object'}
        )
        result=response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(e)

def process_resume(pdf_path,job_description):
    try:
        resume_text=extractText(pdf_path)
        data=analyze_resume_with_llm(resume_text,job_description)
        return data
    except Exception as e:
        print(e)
        return None
