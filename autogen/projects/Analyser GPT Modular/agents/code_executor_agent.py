from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_util import Docker


def get_code_executor_agent(code_executor: Docker):
    code_executor = CodeExecutorAgent(
        name='code_executore_agent',
        code_executor=code_executor.docker
    )

    return code_executor