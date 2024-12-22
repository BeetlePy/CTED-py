import sys
import os
import traceback
from inspect import signature
import inspect

class CTEDExceptions:

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__)) # base directory for relative paths
        sys.excepthook = self.custom_exception

    def custom_exception(self, type, value, _traceback):
        for frame_info in inspect.trace():
            print(f"Function: {frame_info.function}")
            print(f"Line: {frame_info.lineno}")
            print(f"Code: {frame_info.code_context}")
            print(f"File: {frame_info.filename}")
            print("-" * 30)
        tb = _traceback
        traceback_message = "This is a test. An error occured."
        print(traceback_message)
        formatted_tb = traceback.format_exception(type, value, tb) 
        tb = self.createCustomTrace(formatted_tb) 
        print("\n".join(tb))  # Print the formatted traceback

    def createCustomTrace(self, exception):
        new_exception = []
        for line in exception:
            if "File " in line:
                #unction_name = line.split('in ')[-1].split('(')[0]
                #print(f'module:  {list(function_name)}')
                path_start_index = line.find('"') + 1 
                path_end_index = line.find('"', path_start_index) 
                if path_end_index == -1: 
                    print("ERROR: Traceback in incorrect fomat. Defaulting to default traceback.")
                    new_exception.append(line)
                    continue
                abs_path = line[path_start_index:path_end_index]
                rel_path = os.path.relpath(abs_path, self.root_dir)
                rel_path_tb = line[:path_start_index -1] + '(RelativePath): "' + rel_path + line[path_end_index:]
                new_exception.append(rel_path_tb)
            else: new_exception.append(line)
        return new_exception
                    