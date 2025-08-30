import os
from dotenv import load_dotenv
import gradio as gr

# Load environment variables
load_dotenv()

def test_function():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key.startswith('sk-'):
        return "✅ Environment setup successful! OpenAI API key found."
    else:
        return "❌ OpenAI API key not found or invalid."

# Create simple Gradio interface
demo = gr.Interface(fn=test_function, inputs=[], outputs="text", title="Setup Test")

if __name__ == "__main__":
    demo.launch()