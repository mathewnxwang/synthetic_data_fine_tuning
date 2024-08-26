# Intro

This repo contains the code to generate synthetic data for fine tuning an OpenAI model and creating a simple app to inspect the results.
Fine tuning a LLM model can improve instruction adherence and inference costs. OpenAI has a [great explanation](https://platform.openai.com/docs/guides/optimizing-llm-accuracy/fine-tuning) of when to implement this.

# Design

### Synthetic training data generation

First I put together a small seed dataset of question/response pairs using content from [Benn Stancil's Substack blog](https://benn.substack.com/).
The responses are semantically self-contained excerpts from his articles and I backed out a reasonable question that could result in the response.
From that seed dataset I used a LLM to generate additional questions based on automatically scraped excerpts from Benn's blog using `BeautifulSoup`.
To ensure good data quality, I did a final review of the training dataset to ensure good data quality and removed question/responses that weren't useful.




