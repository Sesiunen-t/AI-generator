from .typechecking import typecheck_builder_animation_state, typecheck_builder_task_animation_description, \
    typecheck_builder_animation_narration


# collection of all chains that build/generate data from scratch
@typecheck_builder_task_animation_description
def builder_task_animation_description(task_data):
    """
    build the animation logic infered from the subtasks given
    and adds the animation description to the json
    """
    print("ceva2")

    pass


@typecheck_builder_animation_state
def builder_animation_state(task_data):
    """
    # build the animation state logic infered from the task and
    animation description
    """

    pass


@typecheck_builder_animation_narration
def builder_animation_narration(task_data):
    """
    # build the animation narration logic infered from the task and
    animation description
    """

    pass


builders_collections = {
    "animationDescription": builder_task_animation_description,
    "animationState": builder_animation_state,
    "animationNarration": builder_animation_narration,
}
