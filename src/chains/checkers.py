from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
MAX_TOKENS = os.environ["MAX_TOKEN"]
MODEL = os.environ["MODEL"]


def check_tasks_array():
    """
    expand the prompt into multiple logical tasks in order to
    """

    template = """
    I have a few concepts in a json, each one of them should be explaned in a few manim animation
    Some of the tasks are too abstract and need to be broken down further into smaller more concrete tasks
    I want you to take each task and check if it is too big to be explained in a few sentences or needs more than a few animations
    
    tell me in ajson array what tasks are too big and how they should be broken down further
    tell me in a second json array the tasks that are ok and don't need to be broken down further and how you would animate them
    
    text: {input}
    
    """

    # llm = ChatOpenAI(temperature=0.5, model_name=MODEL, max_tokens=MAX_TOKENS)
    llm = OpenAI(max_tokens=MAX_TOKENS)
    prompt_template = PromptTemplate.from_template(template=template)

    check_array = LLMChain(llm=llm, prompt=prompt_template, output_key="json_fixes_array")
    return check_array
