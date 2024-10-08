import json
import pandas as pd
from pydantic import BaseModel

from llm_manager import LLMManager
from substack_scraper import SubstackScraper
from prompts import CONVERSATION_INPUT_GENERATOR_SYSTEM_PROMPT, CONVERSATION_INPUT_GENERATOR_USER_PROMPT


class ConversationData(BaseModel):
    input: str
    output: str


class SyntheticDataGenerator:

    def __init__(self):
        self.llm_manager = LLMManager()
        self.scraper = SubstackScraper()

    def generate_conversation_inputs(self, urls: list[str]) -> list[ConversationData]:

        seed_examples = self.import_seed_examples('seed_examples.json')
        formatted_examples = self.format_seed_examples(seed_examples)

        conversation_dataset = []
        for url in urls:
            paragraphs: list[str] = self.scraper.get_post_content(url)
            chunks = self.chunk_content(paragraphs)

            for chunk in chunks:
                user_prompt = CONVERSATION_INPUT_GENERATOR_USER_PROMPT.format(
                    examples=formatted_examples, conversation_output=chunk
                )
                conversation_input = self.llm_manager.call_llm(
                    system_prompt=CONVERSATION_INPUT_GENERATOR_SYSTEM_PROMPT,
                    user_prompt=user_prompt,
                    temperature=0
                )
                conversation_dataset.append(
                    ConversationData(input=conversation_input, output=chunk)
                )
        
        data_dicts = [{"input": example.input, "output": example.output} for example in conversation_dataset]
        df = pd.DataFrame(data_dicts)
        df.to_csv('data/conversation_dataset.csv', index=False, encoding='utf-8')
        print(f"Generated synthetic conversation inputs and saved them to a local csv file.")

        return conversation_dataset

    def chunk_content(self, paragraphs: list[str]) -> list[str]:
        """
        Chunk every 3 paragraphs together with a 2 paragraph sliding window.
        Every sequential chunk should have 1 overlapping paragraph.
        """
        chunks = []
        for i in range(0, len(paragraphs) - 2, 2):
            chunks.append(paragraphs[i] + paragraphs[i+1] + paragraphs[i+2])
        
        print(f"Chunked content successfully: {chunks}")
        return chunks

    def import_seed_examples(file_path: str) -> list[ConversationData]:
        with open(file_path, 'r', encoding='utf-8') as file:
            examples = json.load(file)
        
        structured_examples = [ConversationData(input=example['input'], output=example['output']) for example in examples]

        print(f"Imported seed examples succesfully: {structured_examples}")
        return structured_examples

    def format_seed_examples(seed_examples: list[ConversationData]) -> str:
        formatted_examples = ""
        for example in seed_examples:
            formatted_examples += f"Conversation response: {example.output}\nConversation prompt: {example.input}\n\n"
        
        print(f"Formatted seed examples successfully: {formatted_examples}")
        return formatted_examples
