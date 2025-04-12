import re
import fitz  # PyMuPDF
import docx
from PIL import Image
import pytesseract

COMMON_SKILLS = [
    "python", "sql", "excel", "power bi", "machine learning", "deep learning", "java", "c++",
    "aws", "azure", "html", "css", "javascript", "react", "django", "flask", "linux",
    "tensorflow", "kotlin", "flutter", "selenium", "oop", "networking"
]

def extract_skills(text):
    text = text.lower()
    extracted = []

    for skill in COMMON_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            extracted.append(skill)

    return list(set(extracted))

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)

def read_text(file):
    return file.read().decode("utf-8")

def parse_resume(uploaded_file):
    file_type = uploaded_file.type

    if "pdf" in file_type:
        text = read_pdf(uploaded_file)
    elif "word" in file_type or uploaded_file.name.endswith(".docx"):
        text = read_docx(uploaded_file)
    elif "image" in file_type or uploaded_file.name.lower().endswith((".jpg", ".png")):
        text = read_image(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        text = read_text(uploaded_file)
    else:
        text = ""

    skills = extract_skills(text)
    return {
        "skills": skills,
        "clean_text": text
    }
