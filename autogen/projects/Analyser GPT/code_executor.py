from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#Langsmith Tracking And Tracing
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")


from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

async def main():
    docker = DockerCommandLineCodeExecutor(image="python:3-slim-workspace", work_dir="/Users/tusharshinde/code/my/AI/agentic_n_gen_ai/my/Agentic_AI_2.0/autogen/projects/Analyser GPT/workspace")

    code_executor_agent = CodeExecutorAgent(name="codeExecutor", code_executor=docker)

    task = TextMessage(content="""Here is the python code
```python
print('hello world!')
```
        """, source="user")
    
    await docker.start()
    
    result = await code_executor_agent.on_messages(messages=[task], cancellation_token=CancellationToken())
    print(result)
    
    await docker.stop()


if __name__ == "__main__":
    asyncio.run(main())
    