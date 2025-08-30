"""
Outline generation functionality using OpenAI
"""

from openai import OpenAI
from config.settings import settings
from config.prompts import prompts

class OutlineGenerator:
    """Handles AI-powered outline generation"""
    
    def __init__(self):
        """Initialize the OpenAI client"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def generate_outline(self, structure_type, theme, audience, length, style, key_messages):
        """
        Generate a detailed story outline using OpenAI with selected structure
        
        Args:
            structure_type (str): Selected story structure type
            theme (str): The main theme/topic of the story
            audience (str): Target audience description
            length (int): Desired word count
            style (str): Writing style description
            key_messages (str): Key messages to convey
            
        Returns:
            str: Generated outline or error message
        """
        try:
            # Get the appropriate prompt template for the selected structure
            user_prompt = prompts.get_outline_prompt(
                structure_type, theme, audience, length, style, key_messages
            )
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_MESSAGE},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=settings.MAX_TOKENS,
                temperature=settings.TEMPERATURE
            )
            
            outline = response.choices[0].message.content
            
            # Get the structure name for display
            structure_name = prompts.STORY_STRUCTURES.get(structure_type, "Personal Journey")
            
            return f"✅ **Outline Generated Successfully!**\n\n**Structure Used:** {structure_name}\n\n{outline}"
            
        except Exception as e:
            return f"❌ **Error generating outline:** {str(e)}\n\nPlease check your OpenAI API key and try again."
    
    def validate_api_connection(self):
        """
        Test if OpenAI API connection is working
        
        Returns:
            bool: True if connection is working, False otherwise
        """
        try:
            # Make a simple test call
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=5
            )
            return True
        except Exception:
            return False

# Create global outline generator instance
outline_generator = OutlineGenerator()