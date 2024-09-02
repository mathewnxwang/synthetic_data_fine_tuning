import os
import datetime
from dotenv import load_dotenv
from pprint import pprint

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
result = client.fine_tuning.jobs.list(limit=10)
result_dict = [job.to_dict() for job in result]
pprint(result_dict)

for job in result_dict:
    created_at_dt = datetime.datetime.fromtimestamp(job['created_at']).strftime('%Y-%m-%d %H:%M:%S')
    print(f'base model: {job['model']}')
    print(f'model name: {job['fine_tuned_model']}')
    print(f'job created at: {created_at_dt}')
    print('---')
