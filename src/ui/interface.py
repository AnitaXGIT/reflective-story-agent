"""
Gradio user interface components with authentication
"""

import gradio as gr
from config.settings import settings
from config.prompts import prompts
from src.utils.validators import validator
from src.ai.outline_generator import outline_generator
from src.ai.article_generator import article_generator
from src.export.export_handler import export_handler

class StoryInterface:
    """Main interface for the story generator application"""
    
    def __init__(self):
        """Initialize the interface"""
        self.demo = None
    
    def authenticate_user(self, username, password):
        """
        Simple authentication function for Gradio
        
        Args:
            username (str): Entered username
            password (str): Entered password
            
        Returns:
            bool: True if credentials are correct, False otherwise
        """
        return username == settings.AUTH_USERNAME and password == settings.AUTH_PASSWORD
    
    def process_story_parameters(self, structure_type, theme, audience, length, style, key_messages):
        """
        Process and validate story parameters including structure
        
        Returns:
            str: Validation result and parameter summary
        """
        # Validate parameters (including structure)
        is_valid, error_message = validator.validate_parameters(
            structure_type, theme, audience, length, style, key_messages
        )
        
        if not is_valid:
            return error_message
        
        # Return formatted summary
        return validator.format_parameter_summary(
            structure_type, theme, audience, length, style, key_messages
        )
    
    def generate_outline(self, structure_type, theme, audience, length, style, key_messages):
        """
        Generate AI outline after validation
        
        Returns:
            tuple: (outline_for_display, outline_for_editor) - Returns same content twice for both outputs
        """
        # Validate parameters first
        is_valid, error_message = validator.validate_parameters(
            structure_type, theme, audience, length, style, key_messages
        )
        
        if not is_valid:
            error_msg = f"⚠️ **Please fix the following issues before generating outline:**\n\n{error_message}"
            return error_msg, ""  # Return error for display, empty for editor
        
        # Generate outline with selected structure
        outline = outline_generator.generate_outline(
            structure_type, theme, audience, length, style, key_messages
        )
        
        # Extract just the outline content for the editor (remove success message formatting)
        if outline.startswith("✅"):
            # Find the actual outline content after the success message
            lines = outline.split('\n')
            if len(lines) > 2:
                editor_content = '\n'.join(lines[2:])  # Skip first 2 lines (success message and blank line)
            else:
                editor_content = outline
        else:
            editor_content = outline
        
        return outline, editor_content  # Return formatted version for display, clean version for editor
    
    def generate_article(self, edited_outline, theme, audience, length, style, key_messages):
        """
        Generate full article from the edited outline
        
        Args:
            edited_outline (str): The user-reviewed and possibly edited outline
            theme, audience, length, style, key_messages: Original parameters
            
        Returns:
            str: Generated article or error message
        """
        if not edited_outline or not edited_outline.strip():
            return "❌ **Error:** Please generate an outline first or provide outline content."
        
        # Generate the full article
        return article_generator.generate_article(
            edited_outline, theme, audience, length, style, key_messages
        )
    
    def export_txt(self, article_content, structure_type, theme, audience, length):
        """
        Export article as TXT file
        
        Returns:
            str: Success message with file path or error message
        """
        try:
            if not article_content or not article_content.strip():
                return "❌ **Error:** No article content to export. Please generate an article first."
            
            filepath = export_handler.export_to_txt(
                article_content, theme, audience, length, structure_type
            )
            
            file_size = export_handler.get_file_size(filepath)
            return f"✅ **TXT Export Successful!**\n\nFile saved: {filepath}\nSize: {file_size}"
            
        except Exception as e:
            return f"❌ **Export Error:** {str(e)}"
    
    def export_pdf(self, article_content, structure_type, theme, audience, length):
        """
        Export article as PDF file
        
        Returns:
            str: Success message with file path or error message
        """
        try:
            if not article_content or not article_content.strip():
                return "❌ **Error:** No article content to export. Please generate an article first."
            
            filepath = export_handler.export_to_pdf(
                article_content, theme, audience, length, structure_type
            )
            
            file_size = export_handler.get_file_size(filepath)
            return f"✅ **PDF Export Successful!**\n\nFile saved: {filepath}\nSize: {file_size}"
            
        except Exception as e:
            return f"❌ **Export Error:** {str(e)}"
    
    def create_interface(self):
        """Create and return the Gradio interface with authentication"""
        with gr.Blocks(title=settings.APP_TITLE, theme=gr.themes.Soft()) as demo:
            gr.Markdown(f"# 🌟 {settings.APP_TITLE}")
            gr.Markdown(settings.APP_DESCRIPTION)
            gr.Markdown("---")
            
            # Step 1: Input Parameters
            with gr.Group():
                gr.Markdown("## Step 1: Define Your Story Parameters")
                
                with gr.Row():
                    with gr.Column():
                        # Story Structure Selection
                        structure_type = gr.Dropdown(
                            label="📖 Story Structure",
                            choices=prompts.get_structure_options(),
                            value="personal_journey",
                            info="Choose the narrative structure that best fits your story"
                        )
                        
                        theme = gr.Textbox(
                            label="🎯 Theme",
                            placeholder="e.g., overcoming fear, finding purpose, dealing with change...",
                            lines=2
                        )
                        
                        audience = gr.Textbox(
                            label="👥 Target Audience", 
                            placeholder="e.g., young professionals, parents, retirees...",
                            lines=1
                        )
                        
                        length = gr.Number(
                            label="📝 Word Count",
                            value=settings.DEFAULT_WORD_COUNT,
                            minimum=settings.MIN_WORD_COUNT,
                            maximum=settings.MAX_WORD_COUNT
                        )
                        
                        style = gr.Textbox(
                            label="✍️ Writing Style (Optional)",
                            placeholder="e.g., conversational, inspirational, thoughtful, warm...",
                            lines=1
                        )
                        
                        key_messages = gr.Textbox(
                            label="💡 Key Messages",
                            placeholder="What main points or insights should readers take away? What should they reflect on?",
                            lines=4
                        )
                        
                        process_btn = gr.Button("📋 Review Parameters", variant="secondary")
                    
                    with gr.Column():
                        step1_output = gr.Markdown(label="Parameter Review")
            
            # Step 2: Generate Outline
            with gr.Group():
                gr.Markdown("## Step 2: Generate Article Outline")
                
                with gr.Row():
                    generate_outline_btn = gr.Button("🚀 Generate Outline", variant="primary")
                    
                with gr.Row():
                    outline_output = gr.Markdown(label="Generated Outline")
            
            # Step 3: Review & Edit Outline
            with gr.Group():
                gr.Markdown("## Step 3: Review & Edit Outline")
                gr.Markdown("*Review the generated outline below. You can edit it before generating the full article.*")
                
                with gr.Row():
                    outline_editor = gr.Textbox(
                        label="📝 Editable Outline",
                        placeholder="Your generated outline will appear here for review and editing...",
                        lines=15,
                        max_lines=20
                    )
            
            # Step 4: Generate Full Article
            with gr.Group():
                gr.Markdown("## Step 4: Generate Full Article")
                
                with gr.Row():
                    generate_article_btn = gr.Button("✍️ Generate Article", variant="primary", size="lg")
                
                with gr.Row():
                    article_output = gr.Markdown(label="Generated Article")
            
            # Step 5: Export Article
            with gr.Group():
                gr.Markdown("## Step 5: Export Article")
                gr.Markdown("*Download your generated article in your preferred format.*")
                
                with gr.Row():
                    with gr.Column():
                        export_txt_btn = gr.Button("📄 Export as TXT", variant="secondary")
                        export_pdf_btn = gr.Button("📑 Export as PDF", variant="secondary")
                    
                    with gr.Column():
                        export_status = gr.Markdown(label="Export Status")
            
            # Connect buttons to functions
            process_btn.click(
                fn=self.process_story_parameters,
                inputs=[structure_type, theme, audience, length, style, key_messages],
                outputs=step1_output
            )
            
            generate_outline_btn.click(
                fn=self.generate_outline,
                inputs=[structure_type, theme, audience, length, style, key_messages],
                outputs=[outline_output, outline_editor]  # Update both display and editor
            )
            
            generate_article_btn.click(
                fn=self.generate_article,
                inputs=[outline_editor, theme, audience, length, style, key_messages],
                outputs=article_output
            )
            
            export_txt_btn.click(
                fn=self.export_txt,
                inputs=[article_output, structure_type, theme, audience, length],
                outputs=export_status
            )
            
            export_pdf_btn.click(
                fn=self.export_pdf,
                inputs=[article_output, structure_type, theme, audience, length],
                outputs=export_status
            )
        
        self.demo = demo
        return demo
    
    def launch(self, share=False, auth=None):
        """
        Launch the Gradio interface with optional authentication
        
        Args:
            share (bool): Whether to create a public link
            auth (tuple): (username, password) or None for no auth
        """
        if not self.demo:
            self.create_interface()
        
        print(f"🌟 Starting {settings.APP_TITLE}...")
        
        # Set up authentication if provided
        if auth:
            print("🔒 Authentication enabled")
            print("📱 Open your browser to: http://127.0.0.1:7860")
            self.demo.launch(share=share, auth=self.authenticate_user)
        else:
            print("📱 Open your browser to: http://127.0.0.1:7860")
            self.demo.launch(share=share)

# Create global interface instance
story_interface = StoryInterface()