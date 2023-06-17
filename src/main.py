import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain import PromptTemplate, OpenAI, LLMChain
from chains.builders import builder_task_animation_description
from src.composers import standard_composition

payload = {
    "prompt": "Explain to me the area of the circle",
}

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    standard_composition(payload)
    pass
