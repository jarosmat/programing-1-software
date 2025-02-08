import Utilities
from preproccesor import parser
from Utilities import Pointer
import os


file = input("Enter brainfuck file name or absolute path to brainfuck file, enter exit to end program: ")
while file != "exit":
    if not os.path.isfile(file):
        file = input("Enter existing brainfuck file name or absolute path to existing brainfuck file, "
                     "enter exit to end program: ")
        continue
    pont = Pointer(0, Utilities.NodeArray())
    parsed = parser(file)
    parsed.execute(pont)
    file = input("Enter brainfuck file name or absolute path to brainfuck file, enter exit to end program: ")
