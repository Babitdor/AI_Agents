import fitz
import ollama

# from langchain_community.llms import Ollama


# Tools
def extract_text_from_pdf(file):
    document = fitz.open(stream=file.read(), filetype="pdf")
    return " ".join([page.get_text() for page in document])


def generate_answer(context, question):
    prompt = f""" You are my personal assistant who is very precise and informative: 
    Based on the following Context: {context}

    Question: {question}

    Answer: """

    response = ollama.chat(
        model="mistral:latest", messages=[{"role": "user", "content": prompt}]
    )

    return response["message"].content
