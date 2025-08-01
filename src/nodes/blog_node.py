
from src.states.blogstate import BlogState


class BlogNode:
    """A class representing a blog node in the AgenticBlogGenerator system."""

    def __init__(self,llm):
        """
        Initializes the BlogNode with a language model.

        Args:
            llm: An instance of a language model to be used for generating blog content.
        """
        self.llm = llm
        
    
    def title_creation(self,state:BlogState):
        """
        Creates a title for the blog based on the provided topic.
        """
        if "topic" in state and state['topic']:
            prompt = """
                You are an expert blog content writer. Use Markdown formatting. Generate a blog title for the {topic}.
                This title should be creative \
                and SEO friendly.
            
                    """
            system_message = prompt.format(topic=state['topic'])
            response = self.llm.invoke(system_message)
            return {"blog":{"title": response.content}}
    
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}