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


from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio

model_client = OpenAIChatCompletionClient(model='gpt-4o')

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent

assistant_agent = AssistantAgent(
    name="Assitant",
    description="Helpful Assistant",
    system_message="You are a helpful assitant helping user with give task",
    model_client=model_client
)

userProxyAgent = UserProxyAgent(
    name="UserProxy",
    description="UserProxy agent",
    input_func=input
)

from autogen_agentchat.conditions import TextMessageTermination
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat

termination_condition = TextMessageTermination("Approve")

team = RoundRobinGroupChat(
    participants=[assistant_agent, userProxyAgent],
    termination_condition=termination_condition,
    max_turns=10
)

async def main():
    stream = team.run_stream(task="Write python code for adding two integers")
    await Console(stream=stream)


if __name__=="__main__":
    asyncio.run(main())

