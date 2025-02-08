from operations import *


def create_instance(char):
    match char:
        case "+":
            return Addition(1)
        case "-":
            return Subtraction(1)
        case "<":
            return ShiftLeft(1)
        case ">":
            return ShiftRight(1)
        case ".":
            return Printer()
        case ",":
            return Inputer()
        case "[":
            return Task([])


def resolve_loop(loop: Task, task_len: int):
    def opposite_shifts(s1, s2):
        if s1.stamp == "<" and s2.stamp == ">":
            return True, -1
        elif s1.stamp == ">" and s2.stamp == "<":
            return True, +1
        else:
            return False, 0
    if task_len == 1 and (isinstance(loop.task[0], Subtraction) or isinstance(loop.task[0], Addition)):
        return SetNodeZero()
    opps = {"+", "-"}
    if task_len == 4:
        if loop.task[0].stamp == "-" and loop.task[2].stamp in opps:
            shifts = opposite_shifts(loop.task[1], loop.task[3])
            if shifts[0] and loop.task[1].num == loop.task[3].num:
                if loop.task[2].stamp == "+":
                    return MoveData(shifts[1] * loop.task[3].num, 1, loop.task[2].num)
                else:
                    return MoveData(shifts[1] * loop.task[3].num, -1, loop.task[2].num)

    return loop


def parser(file):
    """need to add bool if certain task does not contain other tasks and implement that"""
    main_task = MainTask([], False)
    task_stack = []
    curr_task = main_task
    last_op = MultiOperation()
    multi_ops = {"+", "-", "<", ">"}
    task_len = 0
    with open(file, "r") as sc:
        line = sc.readline()
        while line:
            for char in line:
                if char in multi_ops and last_op.stamp == char:
                    last_op.increment()
                elif char in multi_ops:
                    if last_op.stamp is not None:
                        curr_task.add_operation(last_op)
                        task_len += 1
                    last_op = create_instance(char)
                elif char == "[":
                    curr_task.top = False
                    new_task = Task([])
                    task_len = 0
                    if last_op.stamp is not None:
                        curr_task.add_operation(last_op)
                    task_stack.append(curr_task)
                    curr_task = new_task
                    last_op = MultiOperation()
                elif char == "]":
                    if last_op.stamp is not None:
                        curr_task.add_operation(last_op)
                        task_len += 1
                    if task_stack:
                        new_task = curr_task
                        curr_task = task_stack.pop()
                        if new_task.top is True:
                            curr_task.add_operation(resolve_loop(new_task, task_len))
                        else:
                            curr_task.add_operation(new_task)
                    else:
                        raise SyntaxError("Invalid brackets")
                    last_op = MultiOperation()
                elif char == "." or char == ",":
                    if last_op.stamp is not None:
                        curr_task.add_operation(last_op)
                        last_op = MultiOperation()
                    curr_task.add_operation(create_instance(char))
                    task_len += 1
            line = sc.readline()
        if last_op.stamp is not None:
            curr_task.add_operation(last_op)
    return main_task
