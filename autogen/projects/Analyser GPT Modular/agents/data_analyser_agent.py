from autogen_agentchat.agents import AssistantAgent

from .data_analyzer_prompt import DATA_ANALYZER_SYSTEM_MESSAGE


def get_data_analyzer_agent(model_client):
    data_analyzer_agent = AssistantAgent(
        name='data_analyzer_agent',
        model_client=model_client,
        description='An AI Agent that solver Data Analysis problem and gives the code as well to execute',
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE
    )

    return data_analyzer_agent