import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
client.fine_tuning.jobs.create(
  training_file="file-GYma4luGkdoWKKmPX4yHRrMc", 
  model="gpt-4o-mini-2024-07-18"
)