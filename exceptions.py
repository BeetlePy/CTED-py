import sys
import os
import traceback

class CTEDExceptions:

    def __init__(self):
        self.root = os.path.dirname(os.path.abspath(__file__)) 
        sys.excepthook = self.custom_exception

    def custom_exception(self, type, value, _traceback):
        tb = _traceback
        traceback_message = "This is a test. An error occured."
        print(traceback_message)
        formatted_tb = traceback.format_exception(type, value, tb)   
        print("\n".join(formatted_tb))  # Print the formatted traceback

    def isolatePartsOfException(self, execption):
        execption = list(execption)
        for char in execption:
            if char == "F" and execption(char.index()+3) == 'e':
                print(True)


_ = CTEDExceptions()

def zero_division(n):
    return n / 0

print(zero_division(5))
