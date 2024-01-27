import os
import subprocess

from src.config import PYTHON_PATH



def run (path_module_entrypoint: str, path_python: str, path_exec: str):
    """_summary_

    Args:
        path_module_entrypoint (str): Path of the python module's entrypoint (typically [MODULE]/main.py, [MODULE]/app.py, …)
        path_python (str): _description_
        path_exec (str): _description_
    """

    # Check permissions
    sudo = False
    dirpath_exec = os.path.split(path_exec)[0]
    if not os.access(dirpath_exec, os.W_OK):
        sudo = True

    # Build executable file
    text = f'#!/bin/bash\n{path_python} {path_module_entrypoint} "\$@"'
    text_escaped = text.replace('"', r'\"')

    command = ['printf', f'"{text_escaped}"', '>', f'"{path_exec}"', '&&', 'chmod', '+x', f'"{path_exec}"']
    if sudo: command_list = ['sudo'] + command_list
    command_string = ' '.join(command)
    subprocess.run(command_string, shell=True, check=True)        

    # # Make file executable
    # command_list = ['chmod', '+x', path_exec]
    # if sudo: command_list = ['sudo'] + command_list
    # subprocess.run(command_list)
