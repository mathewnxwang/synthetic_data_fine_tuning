import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
client.fine_tuning.jobs.create(
  training_file="file-YXY7ieew6m2IzMJaDtaLH0bE", 
  model="gpt-4o-2024-08-06"
)