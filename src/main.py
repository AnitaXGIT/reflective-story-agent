"""
Main entry point for the Reflective Story Article Generator with Authentication
"""

import sys
import os

# Add parent directory to Python path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.interface import story_interface
from config.settings import settings

if __name__ == "__main__":
    # Enable authentication for Hugging Face deployment
    # For local development, set auth=None to disable authentication
    
    # Check if running on Hugging Face (they set this environment variable)
    is_huggingface = os.getenv("SPACE_ID") is not None
    
    if is_huggingface:
        print("🤗 Running on Hugging Face Spaces with authentication enabled")
        story_interface.launch(share=False, auth=(settings.AUTH_USERNAME, settings.AUTH_PASSWORD))
    else:
        print("💻 Running locally - authentication disabled for development")
        story_interface.launch(share=False, auth=None)