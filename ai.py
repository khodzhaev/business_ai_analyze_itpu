import openai
from config import OPENAI_API_KEY
import logging  # Импортируем модуль логирования

openai.api_key = OPENAI_API_KEY

def get_llm_response(prompt: str, data: list):
    """Calls OpenAI API and gets a response."""
    logging.info(f"Calling OpenAI API with prompt: {prompt}")  # Логируем вызов API
    
    # Формируем сообщение с данными из Excel
    context = f"Данные из Excel: {data}\n\nВопрос: {prompt}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": context}]
    )
    return response['choices'][0]['message']['content']
