import streamlit as st
from database import query_database
from ai import get_llm_response
from crm_api import send_to_crm, read_from_excel
import pandas as pd
import logging  # Импортируем модуль логирования

# Настройка логирования
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

st.title("Business Analysis AI Agent")

# Загрузка файла Excel
uploaded_file = st.file_uploader("Загрузите файл Excel", type=["xlsx"])
if uploaded_file is not None:
    # Читаем данные из загруженного файла
    data = pd.read_excel(uploaded_file)
    st.write("Данные из Excel:", data)

    # Сохраняем данные в переменной для дальнейшего использования
    excel_data = data.to_dict(orient='records')  # Преобразуем в список словарей для удобства

# User input for AI business analysis
prompt = st.text_area("Введите вопрос о данных из Excel:")
if st.button("Получить AI ответы"):
    if 'excel_data' in locals():  # Проверяем, загружены ли данные
        try:
            response = get_llm_response(prompt, excel_data)  # Передаем данные из Excel
            st.write("AI Ответ:", response)
            logging.info(f"AI Insights for prompt: {prompt} - Response: {response}")  # Логируем ответ AI
        except Exception as e:
            st.error(f"Ошибка: {str(e)}")
            logging.error(f"Ошибка получения AI ответов для запроса: {prompt} - Ошибка: {str(e)}")  # Логируем ошибку
    else:
        st.error("Сначала загрузите файл Excel.")
