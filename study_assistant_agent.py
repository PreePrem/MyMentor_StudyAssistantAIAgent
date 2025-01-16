from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.exa import ExaTools
from phi.model.groq import Groq
import phi
import phi.api
from phi.playground import Playground, serve_playground_app
import os
from dotenv import load_dotenv

load_dotenv()
phi.api=os.getenv("PHI_API_KEY")

#Study assistant agent
study_assistant = Agent(
    name="MyMentor",  
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[ExaTools(), YouTubeTools()],
    markdown=True,
    description="You are a study assistant who assists users in finding resources, answering questions, and providing explanations on various topics.",
    instructions=[
        "Use Exa to search for relevant information on the given topic and verify information from multiple reliable sources.",
        "Break down complex topics into digestible chunks and provide step-by-step explanations with practical examples.",
        "Share curated learning resources including documentation, tutorials, articles, research papers, and community discussions.",
        "Recommend high-quality YouTube videos and online courses that match the user's learning style and proficiency level.",
        "Suggest hands-on projects and exercises to reinforce learning, ranging from beginner to advanced difficulty.",
        "Create personalized study plans with clear milestones, deadlines, and progress tracking.",
        "Provide tips for effective learning techniques, time management, and maintaining motivation.",
        "Recommend relevant communities, forums, and study groups for peer learning and networking.",
    ],
)

'''
study_assistant.print_response(
    "I want to learn about Generative AI in depth. I know the basics, have 1 month to learn, and can spend 3 hours daily. Please share some resources and a detailed study plan.",
    stream=True,
)'''
 
app=Playground(agents=[study_assistant]).get_app()

if __name__=="__main__":
    serve_playground_app("study_assistant_agent:app",reload=True,port=7777)

