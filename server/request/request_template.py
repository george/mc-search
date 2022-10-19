from abc import abstractmethod


class RequestTemplate:

    @abstractmethod
    async def complete(self, session, username, data):
        pass
