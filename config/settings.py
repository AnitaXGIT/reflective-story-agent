"""
Configuration settings for the Reflective Story Article Generator
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    # Application Info
    APP_TITLE = "Reflective Story Article Generator"
    APP_DESCRIPTION = """
    Create meaningful articles with stories designed to help people reflect on their lives. 
    Choose from multiple story structures, generate AI-powered outlines, and create compelling articles.
    """
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "3000"))
    
    # Word Count Settings
    DEFAULT_WORD_COUNT = 800
    MIN_WORD_COUNT = 300
    MAX_WORD_COUNT = 5000
    
    # Authentication Settings
    AUTH_USERNAME = os.getenv("AUTH_USERNAME", "admin")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "reflective2024")
    
    # Hugging Face Deployment Settings
    HF_SPACE_NAME = os.getenv("HF_SPACE_NAME", "reflective-story-generator")

# Create settings instance
settings = Settings()