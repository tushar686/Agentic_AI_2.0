
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import IMAGE, WORK_DIR

class Docker:
    
    def __init__(self):
        self.docker = DockerCommandLineCodeExecutor(image=IMAGE, work_dir=WORK_DIR)

    
    async def start(self):
        print("Starting Docker container")
        await self.docker.start()
        print("Started Docker container")

    async def stop(self):
        print("Stopping Docker container")
        await self.docker.stop()
        print("Stopped Docker container")
