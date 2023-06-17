def typecheck_builder_animation_narration(func):
    def wrapper(task_data):
        if "task_description" not in task_data:
            raise KeyError("task_description not found in chain_data")

        func(task_data)

    return wrapper


def typecheck_builder_animation_state(func):
    def wrapper(task_data):
        if "task_description" not in task_data:
            raise KeyError("task_description not found in chain_data")

        if "animation_narration" not in task_data:
            raise KeyError("task_description not found in chain_data")

        if "animation_description" not in task_data:
            raise KeyError("task_description not found in chain_data")

        func(task_data)

    return wrapper


def typecheck_builder_task_animation_description(func):
    def wrapper(task_data):
        
        if "task_description" not in task_data:
            raise KeyError("task_description not found in chain_data", task_data)

        if "task_narration" not in task_data:
            raise KeyError("task_narration not found in chain_data", task_data)

        func(task_data)

    return wrapper
