import os

# API Keys and Database
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///business.db")  # Change for PostgreSQL
