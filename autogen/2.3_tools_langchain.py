from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#Langsmith Tracking And Tracing
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
os.environ['SERPER_API_KEY']=os.getenv("SERPER_API_KEY")


from langchain_community.utilities import GoogleSerperAPIWrapper

search_tool_wrapper = GoogleSerperAPIWrapper(type="news")

def search(query:str) -> str:
    """This tool searches query on web"""
    try:
        result = search_tool_wrapper.run(query)
        return result
    except Exception as e:
        print(f'search threw an exception {e}')
        return 'No results found'
    

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(model='gpt-4o')

search_agent = AssistantAgent(
    model_client=model_client,
    tools=[search],
    name="search_news",
    description="Searches news from the web",
    system_message="You are an helpful AI assistance helping with latest 2025 news to user queries using search_news tool",
    reflect_on_tool_use=True
)

import asyncio

async def search_news(query:str):
    resp = await search_agent.run(task=query)
    print(resp)


if __name__=="__main__":
    asyncio.run(search_news("who won latest IPL"))


        
