# Intro

This repo contains the code to generate synthetic data for fine tuning an OpenAI LLM model and creating a simple Flask app to inspect the results.
Specifically, it fine tunes a model to respond like Benn Stancil, one of my favorite writers.
Fine tuning a LLM model can improve instruction adherence and inference costs. OpenAI has a [great explanation](https://platform.openai.com/docs/guides/optimizing-llm-accuracy/fine-tuning) of when fine tuning is useful.

# Design

### Synthetic training data generation

I put together a small seed dataset of question/response pairs using content from [Benn Stancil's Substack blog](https://benn.substack.com/).
The questions were manually curated from excerpts from his articles - those excerpts are considered the responses.

To scale the training dataset up, I used a LLM to generate additional questions using the seed dataset as guidance. Article excerpts were automatically scraped from Benn's blog using `BeautifulSoup` instead of manually extracted.
I did a final review of the training dataset and removed question/responses that didn't seem useful to ensure good data quality.

### Fine tuning

I wrangled the training data into the required format, uploaded it to the files API and started the fine tuning job with another API call.
Once the job finished, I can call the fine tuned model by passing its name into the `model` parameter of the chat completions API.


