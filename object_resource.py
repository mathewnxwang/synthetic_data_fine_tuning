from pydantic import BaseModel

class ConversationData(BaseModel):
    input: str
    output: str
