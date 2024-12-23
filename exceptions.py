import sys
import os
import traceback
import inspect
from rich.console import Console

console = Console()

class CTEDExceptions:

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))  # base directory for relative paths
        sys.excepthook = self.custom_exception

    def custom_exception(self, type, value, tb):
        traceback_message = "This is a test. An error occurred."
        print(traceback_message)
        formatted_tb = traceback.format_exception(type, value, tb)
        vars = self._getVariables(tb)
        tb = self._absToRelPath(formatted_tb) 
        self.showVarDefinition(vars, tb)
        print("".join(tb))

    def returnVarDefinitions(self, vars_tuple, tb):
        # Returns the defintions of variables in the traceback. 
        # Returns a dictionary, keys are lines with definded variables, values are a tuple of variable and definition.
        relevant_vars = {}
        local_vars, global_vars = vars_tuple
        for line in tb:
            for var_dict in local_vars:
                for var in var_dict.keys():
                    if var in line:
                        pass
                        
            for var_dict in global_vars:
                for var in var_dict.keys():
                    if var in line:
                        pass

    def _getVariables(self, tb):
        # Walk through the traceback and collect local and global variables
        local_vars = []
        global_vars = []
        
        # Iterate through each frame in the traceback
        while tb:
            frame = tb.tb_frame  # Get the current frame
            locals_in_frame = frame.f_locals  # Local variables in the current frame
            globals_in_frame = frame.f_globals  # Global variables in the current frame
            local_vars.append(locals_in_frame)
            global_vars.append(globals_in_frame)
            
            # Move to the next frame in the traceback
            tb = tb.tb_next
        return local_vars, global_vars
    
    def _absToRelPath(self, tb: list):
        # changes the path of the traceback to a relative path.
        new_exception = []
        for line in tb:  # iterate through each line
            if "File " in line:
                path_start_index = line.find('"') + 1  # Start of the path.
                path_end_index = line.find('"', path_start_index)  # End of the path.
                if path_end_index == -1:  # If the find() does not find the correct str.
                    console.print(f"[bold red]ERROR[/bold red]: Traceback is in incorrect format. Defaulting to default traceback.\nIncorrect line of traceback: {line}", style="red underline")
                    new_exception.append(line)
                    continue
                abs_path = line[path_start_index:path_end_index]
                rel_path = os.path.relpath(abs_path, self.root_dir)
                rel_path_tb = line[:path_start_index - 1] + '"' + rel_path + line[path_end_index:]  # replace the absolute path with relative
                new_exception.append(rel_path_tb)
            else:
                new_exception.append(line)
        return new_exception