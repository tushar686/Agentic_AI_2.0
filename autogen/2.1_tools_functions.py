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


def reverse_string(input:str)->str:
    """
        This tool reverse a input string
    """

    return input[::-1]


from autogen_core.tools import FunctionTool

reverse_string_tool = FunctionTool(reverse_string, description="A tool to reverse a string")

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(model="gpt-4o")

agent = AssistantAgent(
    name = "Assistant",
    model_client=model_client,
    tools=[reverse_string_tool],
    system_message="You are a helpful AI asistant that can reverse a string using `reverse_string_tool` ",
    reflect_on_tool_use=True
)

async def asyn_main():
    resp = await agent.run(task="reverse 'hello world' string'")
    # print(resp)
    print()
    print(resp.messages[-1].content)


import asyncio

if __name__ == "__main__":
    asyncio.run(asyn_main())
