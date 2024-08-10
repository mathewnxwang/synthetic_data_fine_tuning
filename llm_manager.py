import os
from dotenv import load_dotenv

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion


class LLMManager():
    def __init__(self, model: str = 'gpt-4o'):
        self.model = model

        load_dotenv("secrets.env")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        print("openai_api_key should be defined and this should print before the error")
        print(openai_api_key)
        self.client = OpenAI(api_key=openai_api_key)

    def call_llm(self, system_prompt: str, user_prompt: str, temperature: float) -> str:
        print(f"Calling LLM with system prompt: {system_prompt}\n\nUser prompt: {user_prompt}")
        response: ChatCompletion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=self.model,
            temperature=temperature
        )
        message = response.choices[0].message.content
        print(response)
        return message