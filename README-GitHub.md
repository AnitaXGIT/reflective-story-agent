# Reflective Story Article Generator

An AI-powered automation system that helps create meaningful articles containing stories designed to help people reflect on their lives. The system provides a structured workflow from initial concept to published article, with human oversight at key decision points.

## Features

- **Multiple Story Structures**: Choose from 7 different narrative frameworks including Personal Journey, Problem-Solution, Before-After Transformation, Life Lesson, Moment of Clarity, Overcoming Fear, and Unexpected Wisdom
- **AI-Powered Content Generation**: Uses OpenAI GPT models for outline and article generation
- **Human-in-the-Loop Workflow**: Review and edit capabilities at every step
- **Export Options**: Download finished articles as PDF or TXT files
- **User-Friendly Interface**: Clean Gradio-based web interface

## Workflow

1. **Define Story Parameters**: Select structure type, theme, target audience, word count, writing style, and key messages
2. **Generate Outline**: AI creates a detailed story outline based on selected structure
3. **Review & Edit**: Modify the outline as needed before article generation
4. **Generate Article**: AI writes the complete article following the approved outline
5. **Export**: Download your finished article as PDF or TXT file

## Installation

### Prerequisites
- Python 3.7+
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/AnilAXGit/reflective-story-agent.git
cd reflective-story-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
```

4. Run the application:
```bash
python src/main.py
```

5. Open your browser to `http://127.0.0.1:7860`

## Dependencies

- `gradio` - Web interface framework
- `openai` - OpenAI API integration
- `reportlab` - PDF generation
- `python-dotenv` - Environment variable management

## Project Structure

```
reflective-story-agent/
├── src/
│   ├── ai/                     # AI integration components
│   │   ├── outline_generator.py
│   │   └── article_generator.py
│   ├── export/                 # File export functionality
│   │   └── export_handler.py
│   ├── ui/                     # User interface
│   │   └── interface.py
│   ├── utils/                  # Utility functions
│   │   └── validators.py
│   └── main.py                 # Application entry point
├── config/
│   ├── settings.py             # Configuration settings
│   └── prompts.py              # AI prompt templates
├── requirements.txt
├── .env                        # Environment variables (create this)
└── README.md
```

## Story Structure Templates

The system includes seven predefined story structures:

- **Personal Journey**: Growth and transformation experiences
- **Problem-Solution**: Identifying and overcoming challenges
- **Before-After Transformation**: Clear contrast showing change
- **Life Lesson**: Learning from experience or mistakes
- **Moment of Clarity**: Specific realizations or epiphanies
- **Overcoming Fear**: Facing and conquering fears
- **Unexpected Wisdom**: Learning from unlikely sources

## Configuration

### OpenAI Settings
Configure your OpenAI preferences in `config/settings.py`:
- Model selection (GPT-4 recommended)
- Temperature settings
- Token limits

### Export Settings
Articles are automatically saved to your Downloads folder with timestamped filenames.

## Usage Examples

### Basic Usage
1. Select "Personal Journey" structure
2. Enter theme: "overcoming self-doubt"
3. Target audience: "young professionals"
4. Generate outline and review
5. Generate full article
6. Export as PDF

### Advanced Usage
- Edit generated outlines before article creation
- Experiment with different writing styles
- Customize key messages for specific audiences
- Use different structures for varied narrative approaches

## Technical Architecture

- **Backend**: Python with OpenAI API integration
- **Frontend**: Gradio web interface
- **AI Models**: OpenAI GPT-4/GPT-3.5-turbo
- **Export**: ReportLab for PDF generation
- **Storage**: Local file system (Downloads folder)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues, feature requests, or questions, please open an issue on GitHub.

## Development Status

Current version: MVP (Minimum Viable Product)
- Core functionality complete
- All story structures implemented
- Export functionality working
- Ready for deployment

## Future Enhancements

- Multi-language support
- Advanced analytics
- Template library expansion
- Collaboration features
- Direct publishing integrations