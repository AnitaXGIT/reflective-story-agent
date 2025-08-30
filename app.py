"""
Hugging Face Spaces entry point for the Reflective Story Article Generator
"""

import os
import sys

# Add the src directory to the Python path
sys.path.append('src')

from ui.interface import story_interface
from config.settings import settings

# Launch with authentication enabled
if __name__ == "__main__":
    print("🤗 Launching Reflective Story Article Generator on Hugging Face Spaces")
    print("🔒 Authentication is enabled for privacy")
    
    # Launch with authentication
    story_interface.launch(
        share=False,
        auth=(settings.AUTH_USERNAME, settings.AUTH_PASSWORD),
        server_name="0.0.0.0",
        server_port=7860
    )