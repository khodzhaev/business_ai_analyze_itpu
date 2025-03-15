import pandas as pd
import os
import logging  # Импортируем модуль логирования

EXCEL_FILE = "./business_data.xlsx"

def save_to_excel(data: dict):
    """Сохраняет данные в Excel вместо отправки в CRM."""
    
    # Логируем сохранение данных
    logging.info(f"Saving data to Excel: {data}")

    # Проверяем, существует ли файл
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
    else:
        df = pd.DataFrame(columns=["order_id", "status"])

    # Добавляем новые данные
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)

    # Сохраняем файл
    df.to_excel(EXCEL_FILE, index=False)
    return {"message": "Data saved to Excel"}

def read_from_excel():
    """Читает данные из Excel и возвращает их в виде DataFrame."""
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        logging.info("Data read from Excel successfully.")
        return df
    else:
        logging.warning("Excel file does not exist.")
        return pd.DataFrame()  # Возвращаем пустой DataFrame, если файл не существует

def send_to_crm(data: dict):
    """Отправляет данные в CRM (здесь можно добавить логику отправки)."""
    # Логируем отправку данных
    logging.info(f"Sending data to CRM: {data}")
    
    # Здесь должна быть логика отправки данных в CRM
    # Например, можно использовать requests для отправки данных
    return {"message": "Data sent to CRM"}
