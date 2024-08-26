# Intro

This repo contains the code to generate synthetic data for fine tuning an OpenAI model and creating a simple app to inspect the results.
Fine tuning a LLM model can improve instruction adherence and inference costs. OpenAI has a [great explanation](https://platform.openai.com/docs/guides/optimizing-llm-accuracy/fine-tuning) of when LLM fine tuning is useful.

# Design

### Synthetic training data generation

First I put together a small seed dataset of question/response pairs using content from [Benn Stancil's Substack blog](https://benn.substack.com/).
The responses are self-contained excerpts from his articles and the questions are backed out from them.  
From that seed dataset I used a LLM to generate additional questions based on automatically scraped excerpts from Benn's blog using `BeautifulSoup`.
To ensure good data quality, I did a final review of the training dataset to ensure good data quality and removed question/responses that weren't useful.

### Fine tuning

First I wrangled the training data into a format that the OpenAI fine tuning API accepts.
I uploaded the training data with the files API and then start the fine tuning job.
Once it's done, I can call the fine tuned model simply by passing its name into the `model` parameter of the chat completions API.

# How to run

* clone the repo locally
* install `poetry`, a dependency/virtual environment manager
* navigate to the repo directory and run `poetry install` to install dependencies
* create or copy your OpenAI api key from https://platform.openai.com/api-keys
* create a `secrets.env` file and add `OPENAI_API_KEY=<your OpenAI api key here>` to it
* run the flask app with the command `python app.py` in terminal
* go to http://127.0.0.1:5000 in your local browser to interact with the app!


