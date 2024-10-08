from abc import ABC, abstractmethod


class OpenaiChatbotDomainRepository(ABC):
    @abstractmethod
    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        pass
