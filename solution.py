import json
import re
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from docx import Document
from typing import List, Dict, Union

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path: str) -> str:
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def parse_resume_text(text: str) -> Dict[str, Union[Dict[str, str], str, List[Dict[str, str]], List[str], List[Dict[str, str]], List[Dict[str, str]]]]:
    # Define regular expressions for extracting data
    name_pattern = r"Name:\s*(.*)"
    contact_pattern = r"Email:\s*(.*)\s*Phone:\s*(.*)"
    address_pattern = r"Address:\s*(.*)"
    summary_pattern = r"Professional Summary:\s*(.*)"
    experience_pattern = r"Experience:\s*((?:.*\n?)+)"
    education_pattern = r"Education:\s*((?:.*\n?)+)"
    skills_pattern = r"Skills:\s*((?:.*\n?)+)"
    certifications_pattern = r"Certifications:\s*((?:.*\n?)+)"
    languages_pattern = r"Languages:\s*((?:.*\n?)+)"
    
    def extract_section(pattern: str, text: str) -> str:
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def extract_list(pattern: str, text: str) -> List[str]:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            items = match.group(1).strip().split('\n')
            return [item.strip() for item in items if item.strip()]
        return []

    # Extract each section
    personal_info = {
        "name": extract_section(name_pattern, text),
        "contact": {
            "email": extract_section(contact_pattern, text).split()[0],
            "phone": extract_section(contact_pattern, text).split()[1] if len(extract_section(contact_pattern, text).split()) > 1 else ""
        },
        "address": extract_section(address_pattern, text)
    }
    
    summary = extract_section(summary_pattern, text)
    
    def parse_experience_section(experience_text: str) -> List[Dict[str, str]]:
        experiences = []
        exp_lines = experience_text.split('\n')
        for i in range(0, len(exp_lines), 5):
            if i + 4 < len(exp_lines):
                experiences.append({
                    "job_title": exp_lines[i].strip(),
                    "company": exp_lines[i+1].strip(),
                    "location": exp_lines[i+2].strip(),
                    "dates": exp_lines[i+3].strip(),
                    "responsibilities": exp_lines[i+4].strip()
                })
        return experiences

    experience = parse_experience_section(extract_section(experience_pattern, text))
    
    def parse_education_section(education_text: str) -> List[Dict[str, str]]:
        educations = []
        edu_lines = education_text.split('\n')
        for i in range(0, len(edu_lines), 4):
            if i + 3 < len(edu_lines):
                educations.append({
                    "degree": edu_lines[i].strip(),
                    "institution": edu_lines[i+1].strip(),
                    "location": edu_lines[i+2].strip(),
                    "dates": edu_lines[i+3].strip()
                })
        return educations
    
    education = parse_education_section(extract_section(education_pattern, text))
    
    skills = extract_list(skills_pattern, text)
    certifications = parse_experience_section(extract_section(certifications_pattern, text))  # Reusing experience parsing logic for certifications
    languages = parse_experience_section(extract_section(languages_pattern, text))  # Reusing experience parsing logic for languages

    return {
        "personal_information": personal_info,
        "summary": summary,
        "experience": experience,
        "education": education,
        "skills": skills,
        "certifications": certifications,
        "languages": languages
    }

def process_resume(file_path: str = None, url: str = None) -> Dict[str, Union[Dict[str, str], str, List[Dict[str, str]], List[str], List[Dict[str, str]], List[Dict[str, str]]]]:
    if file_path:
        if file_path.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.lower().endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a PDF or DOCX file.")
    elif url:
        text = extract_text_from_url(url)
    else:
        raise ValueError("No file path or URL provided.")
    
    return parse_resume_text(text)

# Example usage:
if __name__ == "__main__":
    # Replace 'resume.pdf' or 'resume.docx' with your file path or use a URL
    result = process_resume(url ='https://drive.google.com/file/d/1UDvA9Hk2rxY-0IBxrMbjiFd60bhhYINq/view?usp=share_link')
    print(json.dumps(result, indent=2))
