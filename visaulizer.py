import rich
from rich.console import Console
import traceback
import re

VARIABLE_RGB = "rgb(215,215,170)"
ARROW_RGB = "rgb(215,215,150)"
BOTTOM_RIGHT_ARROW = "└→"
LONGPIPE = "│"


class VisulizeVariablesInTracback():
    def __init__(self, tb):
        vars = self._getVariables(tb)
        rel_vars = self._getRelevantVarInformation(vars, tb)
        self._showVarDefinitions(rel_vars, tb)

    def _showVarDefinitions(self, rel_vars: dict, tb):
        # creates colored arrows
        # input should be in the same format as _returnVarDefinitions method output.
        # returns modified traceback as a list. (each line is one element)
        pass
        

    def _getRelevantVarInformation(self, vars_tuple, tb):
        likley_vars = set()
        local_vars, global_vars = vars_tuple
        formatted_tb = traceback.format_tb(tb) 
        all_vars = set(local_vars.keys()).union(set(global_vars.keys()))
        likley_vars_line_index = {}
        for line in formatted_tb:
            potential_vars = set(re.findall(r'\b\w+\b', line))
            likley_var = potential_vars.intersection(all_vars)
            likley_vars |= likley_var
            likley_vars_line_index[str(next(iter(likley_var)))] = formatted_tb.index(line)  # TODO: FIX MAYBE TURN THE SETS INTO DICTS
        likley_vars = list(likley_vars)
        vars_and_def = {}
        for var in likley_vars:
            if var in local_vars.keys(): vars_and_def[var] = local_vars[var]
            else: vars_and_def[var] = global_vars[var]
        dicts = [vars_and_def, likley_vars_line_index]
        combined_dict = {}
        print(f' {dicts[0].keys()} = {dicts[1].keys()}')
        # Iterate over each key in the first dictionary (vars_and_def)
        for k in dicts[0]:
            # Combine the values from both dictionaries into a list
            combined_dict[k] = [dicts[0].get(k), dicts[1].get(k)]

        # Print the combined dictionary
        print(combined_dict)
        return combined_dict


    def _getVariables(self, tb):
        local_vars = {}
        global_vars = {}
        while tb:
            frame = tb.tb_frame 
            locals_in_frame = frame.f_locals 
            globals_in_frame = frame.f_globals
            local_vars |= locals_in_frame
            global_vars |= globals_in_frame
            tb = tb.tb_next
        return local_vars, global_vars