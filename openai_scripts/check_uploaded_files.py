import os
from dotenv import load_dotenv
from pprint import pprint

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
result = client.files.list()
result_dict = [file.to_dict() for file in result]
pprint(result_dict)