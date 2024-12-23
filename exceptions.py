import sys
import os
import traceback
from inspect import signature
import inspect

class CTEDExceptions:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__)) # base directory for relative paths
        sys.excepthook = self.custom_exception

    def custom_exception(self, type, value, tb):
        traceback_message = "This is a test. An error occured."
        print(traceback_message)
        formatted_tb = traceback.format_exception(type, value, tb) 
        passed_args = self._getPassedParameters(type, value, tb)
        print(passed_args)
        tb = self._absToRelPath(formatted_tb) 
        print("\n".join(tb))  # Print the formatted traceback

    def _getPassedParameters(self, type, value, tb):
        while tb:
            frame = tb.tb_frame
            func_name = frame.f_code.co_name
            file = frame.f_code.co_name
            line_num = tb.tb_lineno
            arguments = inspect.getargvalues(frame)
            passed_arguments = {func_name: {arg: arguments.locals[arg] for arg in arguments.args}}
            tb = tb.tb_next
        return passed_arguments
    
    def _absToRelPath(self, exception:list):
        # changes the path of the traceback to a relative path.
        # input: a formatted traceback, where each line is the elemnent in a list
        # output: list of strs, for each line of the traceback, relative paths added.
        new_exception = []
        for line in exception: # iterate through each line
            if "File " in line: 
                path_start_index = line.find('"') + 1 # Start of the path.
                path_end_index = line.find('"', path_start_index) # End of the path.
                if path_end_index == -1: # If the find() does not find the correct str.
                    print("ERROR: Traceback in incorrect fomat. Defaulting to default traceback.")
                    new_exception.append(line)
                    continue
                abs_path = line[path_start_index:path_end_index] 
                rel_path = os.path.relpath(abs_path, self.root_dir)
                rel_path_tb = line[:path_start_index -1] + '"' + rel_path + line[path_end_index:] # replace the abosulte path with relative
                new_exception.append(rel_path_tb)
            else: new_exception.append(line)
        return new_exception