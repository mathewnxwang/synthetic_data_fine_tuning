import os
from dotenv import load_dotenv
from pprint import pprint

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
result = client.fine_tuning.jobs.list(limit=10)
result_dict = [job.to_dict() for job in result]
pprint(result_dict)
