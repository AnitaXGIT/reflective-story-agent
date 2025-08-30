import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Configuration settings for the application"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
    
    # Application Configuration
    APP_TITLE = "Reflective Story Article Generator"
    APP_DESCRIPTION = "Create meaningful articles with stories designed to help people reflect on their lives."
    
    # Default Values
    DEFAULT_WORD_COUNT = 800
    MIN_WORD_COUNT = 300
    MAX_WORD_COUNT = 3000
    
    # OpenAI API Parameters
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7

# Create global settings instance
settings = Settings()