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

model_client = OpenAIChatCompletionClient(model='gpt-4o')

from autogen_agentchat.agents import AssistantAgent


coder_agent = AssistantAgent(
    name='Coder',
    description="A python coded",
    system_message="You write python code for a give problem statement. You write it under 100 words",
    model_client=model_client,
)

reviewer_agent = AssistantAgent(
    name='Reviewer',
    description="A code reviewer",
    system_message="You review a python code given by 'Coder' to make sure it is optimized and as per industry standard. You write it under 10 words. If you feel code is fine say 'TERMINATE'",
    model_client=model_client,
)

editor_agent = AssistantAgent(
    name='Editor',
    description="code editor",
    system_message="You make the code easy to understand and add comments. You write it under 10 words",
    model_client=model_client,
)

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import TextMentionTermination
my_termination = TextMentionTermination("TERMINATE")

team = RoundRobinGroupChat(
    participants=[coder_agent, reviewer_agent, editor_agent], 
    termination_condition=my_termination,
    max_turns=9,
    )

from autogen_agentchat.messages import TextMessage
import asyncio

async def run_team():
    text = TextMessage(content="Write simple python code for adding two number", source="user")
    result = await team.run(task=text)
    print(result)


if __name__=="__main__":
    asyncio.run(run_team())


