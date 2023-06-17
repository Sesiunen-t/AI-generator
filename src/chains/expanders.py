from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
MAX_TOKENS = os.environ["MAX_TOKEN"]
MODEL = os.environ["MODEL"]


def expander_prompt_tasks(prompt):
    """
    expand the prompt into multiple logical tasks in order to
    """

    template = """
    I want to do a animation video explaining the following concept given by the user
    Break down that concept in a few subconcepts/subtasks that the user needs to understand
    
    Format the output as JSON with the following keys:
    prompt: the initial prompt
    tasks
    tasks will be an array of jsons containing the task_description field
    
    text: {input}
    """

    llm = ChatOpenAI(temperature=0.5, max_tokens=MAX_TOKENS)
    # llm = OpenAI(max_tokens=MAX_TOKENS, temperature=0.25)
    prompt_template = PromptTemplate.from_template(template=template)

    initial_expander = LLMChain(llm=llm, prompt=prompt_template)
    return initial_expander


def expander_task_to_tasks():
    """
    expand a task into multiple logical tasks
    """

    template = """
    I want to do a manim animation video explaining the following concept given by the user
    You have a json list of the initial prompt and the tasks that need to be explained
    
    I want you to take each task and expand it into more concrete tasks, that will eventually become concrete animation descriptions.
    Each new subtask will be essentially a step to explaining the bigger overall class
    Expand the tasks only if necessary (if the task is too big to be explained in a few sentences or needs more than a few animations)
    
    THe output will be in the same format as the input. Only the tasks array will be expanded with more tasks
    I want each task you break down to be broken down into about 3 subtasks. 
    The original task will be removed from the tasks array and replaced with the subtasks
    
    the json data: {input}
    """

    llm = OpenAI(max_tokens=MAX_TOKENS, temperature=0.25)
    prompt_template = PromptTemplate.from_template(template=template)

    task_expander = LLMChain(llm=llm, prompt=prompt_template, output_key="json_data")
    return task_expander
