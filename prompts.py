CONVERSATION_INPUT_GENERATOR_SYSTEM_PROMPT = "You are a world class data labeler."

CONVERSATION_INPUT_GENERATOR_USER_PROMPT = """Generate a conversation prompt based the conversational response to that prompt.

{examples}

Conversational response: {conversation_output}
Conversation prompt: """