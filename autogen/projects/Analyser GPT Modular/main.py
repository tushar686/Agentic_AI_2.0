import asyncio
from config.docker_util import Docker
from models.openai_model_clients import get_model_client
from teams.data_analyzer import get_data_analyzer_team


async def main():
    docker = Docker()
    model_client = get_model_client()
    team = await get_data_analyzer_team(docker, model_client)
    try:
        await docker.start()
        # task = 'Can you give me a graph of dies and survivd in my titanic.csv'
        task = 'Can you give me a graph of types of flowers in my data iris.csv'
        async for message in team.run_stream(task=task):
            print(f'{message}')
            print()
    except Exception as e:
        print(f'error {e}')
    finally:
        await docker.stop()

if __name__ == '__main__':
    asyncio.run(main())
    