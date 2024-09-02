import os
import json
from dotenv import load_dotenv
from enum import Enum

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

class LLMModel(Enum):
    GPT_4O_MINI = 'gpt-4o-2024-08-06'
    GPT_4O_MINI_FINE_TUNED = 'ft:gpt-4o-2024-08-06:personal::A0LwpzoC'


class LLMManager():
    def __init__(self):
        load_dotenv("secrets.env")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        print("openai_api_key should be defined and this should print before the error")
        print(openai_api_key)
        self.client = OpenAI(api_key=openai_api_key)

    def get_benn_llm_response(self, model_version: str, user_input: str) -> str:

        system_prompt = "You are Benn Stancil."

        if model_version == 'zero_shot':
            model = LLMModel.GPT_4O_MINI
            user_prompt = "Answer the following question in the style of Benn Stancil: " + user_input
        
        elif model_version == 'few_shot':
            model = LLMModel.GPT_4O_MINI
            
            with open('data/seed_examples.json', 'r', encoding='utf-8') as file:
                examples = json.load(file)
            
            few_shot_prompt = ""
            for example in examples:
                few_shot_prompt += f"Question: {example['input']}\nResponse: {example['output']}\n\n"

            user_prompt = f"""{few_shot_prompt}
Answer the following question in the style of Benn Stancil. Question: {user_input}
Response: """

        elif model_version == 'fine_tuned':
            model = LLMModel.GPT_4O_MINI_FINE_TUNED
            user_prompt = "Answer the following question in the style of Benn Stancil. Do not repeat yourself over and over again: " + user_input

        else:
            raise ValueError("Invalid model version. Please choose 'zero_shot', 'few_shot', or 'fine_tuned'.")

        return self.call_llm(model, system_prompt, user_prompt)

    def call_llm(
            self,
            model: LLMModel,
            system_prompt: str,
            user_prompt: str,
            temperature: float = 0
        ) -> str:
        print(f"Calling LLM with system prompt: {system_prompt}\n\nUser prompt: {user_prompt}")
        response: ChatCompletion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=model.value,
            temperature=temperature,
            max_tokens=300
        )
        message = response.choices[0].message.content
        print(response)
        return message
