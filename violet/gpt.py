import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY') 
error_model = open('violet/error-model.txt').read()

def generate(history: str, prompt: str) -> str:
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'{history}\nHuman: {prompt}\nAI: ',
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    message = completions.choices[0].text
    return message[1:]

def explain_error(prompt: str) -> str:
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'{error_model}\nHuman: {prompt}\nAI: ',
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    message = completions.choices[0].text
    return message[1:]
