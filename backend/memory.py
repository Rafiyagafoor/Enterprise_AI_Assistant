from langchain.memory import ConversationBufferWindowMemory

memory=ConversationBufferWindowMemory(
    k=5,
    return_messages=True
)