import asyncio

class AgentBus:
    def __init__(self):
        self.queue = asyncio.Queue()
