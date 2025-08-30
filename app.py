"""
Hugging Face Spaces entry point for the Reflective Story Article Generator
"""

import os
import sys

# Add the src directory to the Python path
sys.path.append('src')

def authenticate_user(username, password):
    """Simple authentication function"""
    # Get credentials from environment variables
    auth_username = os.getenv("AUTH_USERNAME", "admin")
    auth_password = os.getenv("AUTH_PASSWORD", "reflective2024")
    
    return username == auth_username and password == auth_password

if __name__ == "__main__":
    print("🤗 Starting Reflective Story Article Generator on Hugging Face Spaces")
    print("🔒 Authentication is enabled for privacy")
    
    try:
        from src.ui.interface import story_interface
        
        # Launch with authentication
        story_interface.demo = story_interface.create_interface()
        story_interface.demo.launch(
            auth=authenticate_user,
            server_name="0.0.0.0",
            server_port=7860,
            share=False
        )
        
    except Exception as e:
        print(f"Error launching app: {e}")
        import traceback
        traceback.print_exc()