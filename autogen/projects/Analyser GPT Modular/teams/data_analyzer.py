from agents import code_executor_agent, data_analyser_agent
from config.docker_util import Docker
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


async def get_data_analyzer_team(docker, model_client):

    code_agent = code_executor_agent.get_code_executor_agent(docker)
    data_agent = data_analyser_agent.get_data_analyzer_agent(model_client)

    team = RoundRobinGroupChat(
        participants=[data_agent, code_agent],
        termination_condition=TextMentionTermination('STOP'),
        max_turns=20
    )

    return team