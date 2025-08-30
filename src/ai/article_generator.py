"""
Article generation functionality using OpenAI
"""

from openai import OpenAI
from config.settings import settings
from config.prompts import prompts

class ArticleGenerator:
    """Handles AI-powered full article generation from approved outlines"""
    
    def __init__(self):
        """Initialize the OpenAI client"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def generate_article(self, outline, theme, audience, length, style, key_messages):
        """
        Generate a complete article from an approved outline using OpenAI
        
        Args:
            outline (str): The approved story outline
            theme (str): The main theme/topic of the story
            audience (str): Target audience description
            length (int): Desired word count
            style (str): Writing style description
            key_messages (str): Key messages to convey
            
        Returns:
            str: Generated article or error message
        """
        try:
            # Format the article generation prompt
            user_prompt = prompts.ARTICLE_GENERATION.format(
                outline=outline,
                theme=theme,
                audience=audience,
                length=length,
                style=style,
                key_messages=key_messages
            )
            
            # Call OpenAI API with higher token limit for full articles
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_MESSAGE},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2000,  # Higher limit for full articles
                temperature=settings.TEMPERATURE
            )
            
            article = response.choices[0].message.content
            return f"✅ **Article Generated Successfully!**\n\n{article}"
            
        except Exception as e:
            return f"❌ **Error generating article:** {str(e)}\n\nPlease check your OpenAI API key and try again."
    
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

# Create global article generator instance
article_generator = ArticleGenerator()