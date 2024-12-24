import sys
import os
import traceback
from rich.console import Console
from visualizer import  VisulizeVariablesInTracback

console = Console()

class CTEDExceptions:

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))  # base directory for relative paths
        sys.excepthook = self._custom_exception

    def _custom_exception(self, type, value, tb):
        traceback_message = "This is a test. An error occurred."
        print(traceback_message)
        v = VisulizeVariablesInTracback(tb) # vizulizeds variables in tracebacks
        tb = self._absToRelPath(traceback.format_exception(type, value, tb)) # converts paths to relative paths
        print("".join(tb))
            
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

_ = CTEDExceptions()