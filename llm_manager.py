import os
from dotenv import load_dotenv
from enum import Enum

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion


class LLMModel(Enum):
    GPT_4O = 'gpt-4o'
    FINE_TUNED_4O_MINI = 'ft:gpt-4o-mini-2024-07-18:personal::A0GUU7RH'


class LLMManager():
    def __init__(self, model: LLMModel = LLMModel.GPT_4O):
        self.model = model.value

        load_dotenv("secrets.env")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        print("openai_api_key should be defined and this should print before the error")
        print(openai_api_key)
        self.client = OpenAI(api_key=openai_api_key)

    def call_llm(self, system_prompt: str, user_prompt: str, temperature: float = 0) -> str:
        print(f"Calling LLM with system prompt: {system_prompt}\n\nUser prompt: {user_prompt}")
        response: ChatCompletion = self.client.chat.completions.create(
            messages=[
                # {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=self.model,
            temperature=temperature
        )
        message = response.choices[0].message.content
        print(response)
        return message

llm_manager = LLMManager(model=LLMModel.FINE_TUNED_4O_MINI)
system_prompt = "You are Benn Stancil."
user_prompt = "Answer the following question in the style of Benn Stancil: I have $100, what should I spend it on"
print(llm_manager.call_llm(system_prompt, user_prompt))
