"""
Input validation utilities
"""

from config.settings import settings
from config.prompts import prompts

class StoryParameterValidator:
    """Validates story parameters input by users"""
    
    @staticmethod
    def validate_parameters(structure_type, theme, audience, length, style, key_messages):
        """
        Validate all story parameters including structure
        
        Args:
            structure_type (str): Selected story structure
            theme (str): Story theme
            audience (str): Target audience
            length (int): Word count
            style (str): Writing style
            key_messages (str): Key messages
            
        Returns:
            tuple: (is_valid, error_message)
        """
        # Check story structure
        if not structure_type or structure_type not in prompts.STORY_STRUCTURES:
            return False, "❌ Story Structure is required. Please select a valid story structure."
        
        # Check required fields
        if not theme or not theme.strip():
            return False, "❌ Theme is required. Please describe what your story should be about."
        
        if not audience or not audience.strip():
            return False, "❌ Target Audience is required. Please describe who this story is for."
        
        if not key_messages or not key_messages.strip():
            return False, "❌ Key Messages is required. Please describe what insights readers should gain."
        
        # Check word count
        if length < settings.MIN_WORD_COUNT or length > settings.MAX_WORD_COUNT:
            return False, f"❌ Word count must be between {settings.MIN_WORD_COUNT} and {settings.MAX_WORD_COUNT} words."
        
        # Optional fields can be empty, but check if they're reasonable length
        if style and len(style.strip()) > 200:
            return False, "❌ Writing Style description is too long. Please keep it under 200 characters."
        
        if len(theme.strip()) > 500:
            return False, "❌ Theme description is too long. Please keep it under 500 characters."
        
        if len(audience.strip()) > 300:
            return False, "❌ Target Audience description is too long. Please keep it under 300 characters."
        
        if len(key_messages.strip()) > 1000:
            return False, "❌ Key Messages is too long. Please keep it under 1000 characters."
        
        return True, ""
    
    @staticmethod
    def format_parameter_summary(structure_type, theme, audience, length, style, key_messages):
        """
        Format a summary of the validated parameters including structure
        
        Returns:
            str: Formatted parameter summary
        """
        # Get the human-readable structure name
        structure_name = prompts.STORY_STRUCTURES.get(structure_type, "Unknown Structure")
        
        return f"""📝 **Story Parameters Captured:**

**Story Structure:** {structure_name}
**Theme:** {theme}
**Target Audience:** {audience}
**Length:** {length} words
**Style:** {style if style else 'Not specified (AI will choose appropriate style)'}
**Key Messages:** {key_messages}

✅ Parameters validated successfully! Ready to generate outline."""

# Create global validator instance
validator = StoryParameterValidator()