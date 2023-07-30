from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from config import TEMPLATE, API_KEY

__all__ = ('ConversationAgent')


class ConversationAgent:
    """
    """
    def __init__(self, verbose=False):
        prompt = PromptTemplate(input_variables=["history", "input"],
                                 template=TEMPLATE)
        self.chat_chain = LLMChain(llm=OpenAI(temperature=0, openai_api_key=API_KEY, model_name="gpt-4"),
                                   prompt=prompt,
                                   verbose=verbose,
                                   memory=ConversationBufferWindowMemory(k=2))
    
    def respond(self, input):
        """
        Function to respond to a particular
        query
        """
        return self.chat_chain.predict(input=input)
