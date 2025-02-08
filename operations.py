import Utilities as Utils
import sys


class MultiOperation:
    """represents one of these operations: <>+-, can represent more of these operations,
    that are in source code in continuous sequence
    """
    stamp = None

    def __init__(self, num=1):
        """construct a new MultiOperation, num represents how many continuous operations it represents"""
        self.num = num

    def increment(self, num=1):
        """increments how many continuous operations it represents"""
        self.num += num

    def __str__(self):
        """string representation of MultiOperation"""
        return f"/{self.num}{self.stamp}"


class Task:
    """represents one loop in source code"""
    def __init__(self, task, top=True):
        """construct a new Task instance, task represents sequence of operations in loop"""
        if isinstance(task, list):
            self.task = task
        else:
            raise TypeError('Task must be initialized as list')
        self.top = top

    def add_operation(self, operation):
        """add operation to loop"""
        self.task.append(operation)

    def execute(self, pointer: Utils.Pointer):
        """runs loop while active node at the beginning of loop is not set to zero"""
        while pointer.get_node().value != 0:
            for operation in self.task:
                operation.execute(pointer)

    def __str__(self):
        """string representation of a loop"""
        to_return = "["
        for operation in self.task:
            to_return += str(operation)
        return to_return + "]"


class MainTask(Task):
    """represents source code as sequence of operations"""
    def execute(self, pointer: Utils.Pointer):
        for operation in self.task:
            operation.execute(pointer)

    def __str__(self):
        """string representation of a loop"""
        to_return = ""
        for operation in self.task:
            to_return += str(operation)
        return to_return


class Addition(MultiOperation):
    """represents addition to node"""
    stamp = "+"

    def execute(self, pointer: Utils.Pointer):
        pointer.get_node().addition(self.num)


class Subtraction(MultiOperation):
    """represents subtraction from node"""
    stamp = "-"

    def execute(self, pointer: Utils.Pointer):
        pointer.get_node().subtraction(self.num)


class ShiftLeft(MultiOperation):
    """represents shifting pointer left"""
    stamp = "<"

    def execute(self, pointer: Utils.Pointer):
        pointer.shift_pointer_left(self.num)


class ShiftRight(MultiOperation):
    """represents shifting pointer right"""
    stamp = ">"

    def execute(self, pointer: Utils.Pointer):
        pointer.shift_pointer_right(self.num)


class Printer:
    """represents printing value of active node to console decoded as ASCII character"""
    stamp = "."

    @staticmethod
    def execute(pointer: Utils.Pointer):
        sys.stdout.write(chr(pointer.get_node().value))

    def __str__(self):
        return f"/{str(self.stamp)}"


class Inputer:
    """sets active node to ASCII encoded character inputted from console"""""
    stamp = ","

    @staticmethod
    def execute(pointer: Utils.Pointer):
        print("enter a char: ", end="")
        inpt = sys.stdin.readline()[0]
        if inpt.isascii():
            pointer.get_node().set_value(ord(inpt))
        else:
            raise Exception("invalid character, character must be valid ASCII character")

    def __str__(self):
        return f"/{str(self.stamp)}"


class SetNodeZero:
    """represents loop that sets active node to zero"""
    len = 1

    @staticmethod
    def execute(pointer: Utils.Pointer):
        pointer.get_node().set_value(0x00)

    def __str__(self):
        return "/S0"


class MoveData:
    """represents loop that moves data from one node to another,
    if sign is positive it adds data, else it subtracts data"""
    len = 4

    def __init__(self, diff: int, sign, mult):
        if sign not in {1, -1}:
            raise Exception("sign must be 1 or -1")
        self.sign = sign
        self.diff = diff
        self.mult = mult

    def execute(self, pointer: Utils.Pointer):
        pnt_val = pointer.get_node().value
        pointer.get_node().set_value(0)
        if self.diff > 0:
            pointer.shift_pointer_right(self.diff)
            pointer.get_node().addition(self.sign * pnt_val * self.mult)
            pointer.shift_pointer_left(self.diff)
        else:
            pointer.shift_pointer_left(abs(self.diff))
            pointer.get_node().addition(self.sign * pnt_val * self.mult)
            pointer.shift_pointer_right(abs(self.diff))

    def __str__(self):
        return f"/M{self.diff};{self.sign};{self.mult}"
