class Node:
    """class instance represents one node in runtime memory
    MAX_NODE_VALUE represents maximum value, stored in one node, implicitly set to 255 (8-bit unsigned)"""

    MAX_NODE_VALUE = 255    # must correspond to certain amount of n bits in Node, the value is (2**n)-1

    def __init__(self, value=0):
        """constructor for Node class, node does not have to be initialized with zero value,
        if initialized with value greater than MAX_NODE_VALUE, value will be truncated to bits set by MAX_NODE_VALUE
        parameters:
            value:
        """
        if type(value) is not int:
            raise TypeError('Argument must be an integer')
        self.value = value & self.MAX_NODE_VALUE

    def set_value(self, value):
        """sets value of instance to value, """
        if type(value) is not int:
            raise TypeError('Argument must be an integer')
        else:
            self.value = value & self.MAX_NODE_VALUE
            return self.value

    def addition(self, value):
        if type(value) is not int:
            raise TypeError('Argument must be an integer')
        else:
            self.value = (self.value + value) & Node.MAX_NODE_VALUE
            return self.value

    def subtraction(self, value):
        if type(value) is not int:
            raise TypeError('Argument must be a integer')
        else:
            self.value = (self.value - value) & Node.MAX_NODE_VALUE
            return self.value


class NodeArray:
    NODES = 30_000

    def __init__(self, nodes=NODES):
        self.nodes = dict()
        self.max_nodes = nodes

    def initialize_node(self, pointer):
        if type(pointer) is not int:
            raise TypeError('Pointer must be an integer')
        elif 0 <= pointer < self.max_nodes:
            try:
                return self.nodes[pointer]
            except KeyError:
                self.nodes[pointer] = Node(0)
                return self.nodes[pointer]
        else:
            raise ValueError(f'Pointer must be within specified address space: 0 <= {pointer} < {self.max_nodes}')

    def get_node(self, pointer):
        return self.initialize_node(pointer)

    def set_node(self, pointer, value):
        node = self.get_node(pointer)
        node.set_value(value)
        return pointer

    def addition(self, pointer, value):
        if type(pointer) is not int:
            raise TypeError('Pointer must be an integer')
        else:
            node = self.get_node(pointer)
            node.add_value(value)
            return pointer

    def subtraction(self, pointer, value):
        node = self.get_node(pointer)
        node.subtraction(value)
        return pointer


class Pointer:
    def __init__(self, value, node_array: NodeArray):
        """actual_node represents the key of node that is stored in self.node"""
        if type(value) is not int:
            raise TypeError('Pointer must be an integer')
        if value > NodeArray.NODES:
            raise ValueError(f'Pointer value out of range ({NodeArray.NODES})')
        self.value = value
        self.node_array = node_array

    def shift_pointer_right(self, shifts):
        new_val = (shifts + self.value) % NodeArray.NODES
        self.value = new_val
        return new_val
    
    def shift_pointer_left(self, shifts):
        new_val = (self.value - shifts)
        if new_val < 0:
            new_val = NodeArray.NODES + new_val
        self.value = new_val
        return new_val

    def get_node(self) -> Node:
        return self.node_array.get_node(self.value)
