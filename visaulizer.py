import rich
from rich.console import Console
import traceback

VARIABLE_RGB = "rgb(215,215,170)"
ARROW_RGB = "rgb(215,215,150)"
BOTTOM_RIGHT_ARROW = "└→"
LONGPIPE = "│"


class VisulizeVariablesInTracback():
    def __init__(self, tb):
        vars = self._getVariables(tb)
        rel_vars = self._returnVarInformation(vars, tb)
        print(rel_vars)
        self._showVarDefinitions(rel_vars, tb)

    def _showVarDefinitions(self, relative_variables: dict, tb):
        # creates colored arrows
        # input should be in the same format as _returnVarDefinitions method output.
        # returns modified traceback as a list. (each line is one element)
        rel_vars = relative_variables
        

    def _returnVarInformation(self, vars_tuple, tb):
        formatted_tb = traceback.format_tb(tb) 
        

    def _getVariables(self, tb):
        local_vars = []
        global_vars = []
        while tb:
            frame = tb.tb_frame 
            locals_in_frame = frame.f_locals 
            globals_in_frame = frame.f_globals
            local_vars.append(locals_in_frame)
            global_vars.append(globals_in_frame)
            tb = tb.tb_next
        return local_vars, global_vars