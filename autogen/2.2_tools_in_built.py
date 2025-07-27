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


from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.http import HttpTool

model_client = OpenAIChatCompletionClient(model="gpt-4o")


cat_fact_schema = {
    "type": "object",
    "properties": {
        "fact": {
            "type": "string",
            "description": "A fun or interesting fact, typically about cats"
        },
        "length": {
            "type": "integer",
            "description": "The number of characters in the 'fact' string"
        }
    },
    "required": ["fact", "length"]
}


# Create an HTTP tool for the httpbin API
http_cat_fact_tool = HttpTool(
    name="cat_fact",
    description="random cat fact",
    scheme="https",
    host="catfact.ninja",
    port=443,
    path="/fact",
    method="GET",
    json_schema=cat_fact_schema,
)



agent = AssistantAgent(
    name = "Assistant",
    model_client=model_client,
    tools=[http_cat_fact_tool],
    system_message="You are a helpful AI asistant that give random cat fact using tool `http_cat_fact_tool` ",
    reflect_on_tool_use=False
)

async def asyn_main():
    resp = await agent.run(task="Give me cat fact")
    print()
    print(resp.messages[-1].content)


import asyncio

if __name__ == "__main__":
    asyncio.run(asyn_main())
