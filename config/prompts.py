"""
AI prompts for the Reflective Story Article Generator
"""

class Prompts:
    """Container for all AI prompts used in the application"""
    
    SYSTEM_MESSAGE = """You are an expert story and article writer who specializes in creating meaningful, reflective content that helps people examine their lives. You write with empathy, wisdom, and the ability to connect universal human experiences to personal insights."""
    
    # Story structure options with descriptions
    STORY_STRUCTURES = {
        "personal_journey": "Personal Journey - Someone's growth and transformation experience",
        "problem_solution": "Problem-Solution - Identifying and overcoming a challenge",
        "before_after": "Before-After Transformation - Clear contrast showing change",
        "life_lesson": "Life Lesson - Learning from experience or mistake",
        "moment_of_clarity": "Moment of Clarity - A specific realization or epiphany",
        "overcoming_fear": "Overcoming Fear - Facing and conquering something scary",
        "unexpected_wisdom": "Unexpected Wisdom - Learning from an unlikely source"
    }
    
    # Base outline generation templates for each structure
    OUTLINE_TEMPLATES = {
        "personal_journey": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as a PERSONAL JOURNEY story with these sections:
1. HOOK/INTRODUCTION - Engaging opening that hints at the transformation to come
2. STARTING POINT - Where the person was before their journey (mindset, situation, challenges)
3. THE CATALYST - What triggered the need for change or growth
4. THE JOURNEY - Key experiences, struggles, and small victories along the way
5. TRANSFORMATION MOMENT - The pivotal point where real change occurred
6. NEW UNDERSTANDING - What the person learned and how they changed
7. REFLECTION QUESTIONS - 3-4 questions for readers to consider their own journeys
8. CONCLUSION - How this transformation continues to impact life and what readers can take away

Focus on creating an authentic progression that readers can relate to their own growth experiences.""",

        "problem_solution": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as a PROBLEM-SOLUTION story with these sections:
1. HOOK/INTRODUCTION - Present the problem in a compelling way
2. CONTEXT SETTING - Background and why this problem matters
3. PROBLEM DEFINITION - Clear description of the challenge and its impact
4. INITIAL ATTEMPTS - Early efforts to solve the problem and why they failed
5. BREAKTHROUGH APPROACH - The solution that actually worked
6. IMPLEMENTATION - How the solution was put into practice
7. RESULTS & LEARNING - What changed and what was learned in the process
8. REFLECTION QUESTIONS - 3-4 questions about readers' own problem-solving approaches
9. CONCLUSION - Key insights about problem-solving and personal growth

Emphasize the learning process and how failure led to eventual success.""",

        "before_after": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as a BEFORE-AFTER TRANSFORMATION story with these sections:
1. HOOK/INTRODUCTION - Tease the dramatic contrast between before and after
2. THE BEFORE - Detailed picture of the starting situation, mindset, or condition
3. THE TRIGGER - What event or realization sparked the need for change
4. DECISION POINT - The moment of commitment to transformation
5. THE PROCESS - Key steps, challenges, and milestones in the change
6. THE AFTER - Clear picture of the new reality and how different it is
7. UNEXPECTED DISCOVERIES - What surprised them about the transformation
8. REFLECTION QUESTIONS - 3-4 questions about readers' own potential transformations
9. CONCLUSION - The ongoing impact and what others can learn

Create a vivid contrast that helps readers envision their own potential transformations.""",

        "life_lesson": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as a LIFE LESSON story with these sections:
1. HOOK/INTRODUCTION - Set up the situation that led to important learning
2. THE SETUP - Context and circumstances leading to the experience
3. THE EXPERIENCE - What happened that contained the lesson (could be mistake, success, or observation)
4. INITIAL REACTION - First thoughts and feelings about what occurred
5. DEEPER REFLECTION - Looking beyond the surface to find the real meaning
6. THE LESSON EMERGES - What insight or wisdom was gained
7. APPLICATION - How this lesson changed future decisions or perspectives
8. REFLECTION QUESTIONS - 3-4 questions about readers' own learning experiences
9. CONCLUSION - Why this lesson matters and how others can apply it

Focus on the journey from experience to wisdom and practical application.""",

        "moment_of_clarity": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as a MOMENT OF CLARITY story with these sections:
1. HOOK/INTRODUCTION - Build anticipation for the revelation to come
2. THE BUILDUP - Confusion, struggle, or questions that preceded the clarity
3. CONTEXT & CIRCUMSTANCES - Where and when this moment occurred
4. THE MOMENT ITSELF - Detailed description of the realization or epiphany
5. IMMEDIATE IMPACT - How this clarity felt and first reactions
6. CONNECTING THE DOTS - How this insight explained or resolved previous confusion
7. LIFE CHANGES - What shifted as a result of this new understanding
8. REFLECTION QUESTIONS - 3-4 questions about readers' own moments of insight
9. CONCLUSION - The lasting impact and how readers might recognize their own clarity moments

Emphasize the power of sudden understanding and its transformative effect.""",

        "overcoming_fear": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as an OVERCOMING FEAR story with these sections:
1. HOOK/INTRODUCTION - Introduce the fear and its hold on the person
2. THE FEAR'S ORIGIN - How and why this fear developed
3. IMPACT ON LIFE - How the fear limited choices and experiences
4. THE DECISION - What motivated the choice to face the fear
5. PREPARATION - Mental, emotional, or practical steps taken
6. THE CONFRONTATION - The actual experience of facing the fear
7. BREAKTHROUGH - The moment courage overcame fear
8. NEW CONFIDENCE - How overcoming this fear changed everything
9. REFLECTION QUESTIONS - 3-4 questions about readers' own fears and courage
10. CONCLUSION - Insights about fear, courage, and personal growth

Focus on the universal experience of fear and the empowerment that comes from facing it.""",

        "unexpected_wisdom": """Create a detailed outline for a reflective story article with these parameters:

Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Structure this as an UNEXPECTED WISDOM story with these sections:
1. HOOK/INTRODUCTION - Set up the unlikely source or situation
2. THE ORDINARY MOMENT - Describe the seemingly mundane situation or encounter
3. THE UNEXPECTED TEACHER - Introduce the surprising source of wisdom (child, stranger, situation, etc.)
4. THE EXCHANGE - What was said, observed, or experienced
5. INITIAL DISMISSAL - Why this wisdom was almost overlooked or dismissed
6. RECOGNITION - The moment of realizing the profound truth in simple words
7. DEEPER UNDERSTANDING - Unpacking the full meaning and implications
8. LIFE APPLICATION - How this wisdom changed perspective or behavior
9. REFLECTION QUESTIONS - 3-4 questions about finding wisdom in unexpected places
10. CONCLUSION - The value of staying open to learning from any source

Emphasize how profound truths often come from the most unexpected places."""
    }
    
    ARTICLE_GENERATION = """Based on the following approved outline, write a complete reflective story article:

OUTLINE:
{outline}

ORIGINAL PARAMETERS:
Theme: {theme}
Target Audience: {audience}
Word Count: {length} words
Writing Style: {style}
Key Messages: {key_messages}

Please write a complete article that:
- Follows the approved outline structure
- Maintains the specified writing style and tone
- Speaks directly to the target audience
- Incorporates the key messages naturally
- Aims for approximately {length} words
- Creates genuine moments for self-reflection
- Ends with actionable insights or questions

Write in a warm, engaging manner that invites readers to examine their own experiences."""

    @classmethod
    def get_outline_prompt(cls, structure_type, theme, audience, length, style, key_messages):
        """
        Get the appropriate outline prompt based on selected structure
        
        Args:
            structure_type (str): The selected story structure key
            theme (str): Story theme
            audience (str): Target audience
            length (int): Word count
            style (str): Writing style
            key_messages (str): Key messages
            
        Returns:
            str: Formatted prompt for the selected structure
        """
        if structure_type not in cls.OUTLINE_TEMPLATES:
            structure_type = "personal_journey"  # Default fallback
            
        template = cls.OUTLINE_TEMPLATES[structure_type]
        
        return template.format(
            theme=theme,
            audience=audience,
            length=length,
            style=style,
            key_messages=key_messages
        )
    
    @classmethod
    def get_structure_options(cls):
        """
        Get list of structure options for UI dropdown
        
        Returns:
            list: List of tuples (description, key) for dropdown options - Gradio format
        """
        return [(desc, key) for key, desc in cls.STORY_STRUCTURES.items()]

# Create global prompts instance
prompts = Prompts()