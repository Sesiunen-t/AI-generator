from langchain import PromptTemplate, OpenAI, LLMChain
from chains.expanders import expander_prompt_tasks, expander_task_to_tasks
from langchain.chains import SimpleSequentialChain
from chains.checkers import check_tasks_array


def standard_composition(payload):
    """Compose chains into a new chain."""
    if "prompt" not in payload:
        raise Exception("prompt is required")

    # task breakdown via the expander chains
    prompt_expander_chain = expander_prompt_tasks(payload["prompt"])
    task_expander_chain = expander_task_to_tasks()
    check_array_chain = check_tasks_array()

    overall_chain = SimpleSequentialChain(
        chains=[prompt_expander_chain, task_expander_chain, task_expander_chain, task_expander_chain], verbose=True)

    res = overall_chain.run(input="Explain the area of the circle")
    print(res)

    # populating the tasks with animations
