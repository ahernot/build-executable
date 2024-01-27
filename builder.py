import os
import subprocess
import warnings
from src.config import PYTHON_PATH


def run (path_module_entrypoint: str, path_exec: str, path_python: str = PYTHON_PATH, **kwargs):
    """_summary_

    Args:
        path_module_entrypoint (str): Path of the python module's entrypoint (typically [MODULE]/main.py, [MODULE]/app.py, …)
        path_python (str): _description_
        path_exec (str): _description_
    """

    # Parse arguments
    verbose = kwargs.get('verbose', False)
    dirpath_exec = os.path.split(path_exec)[0]

    # Check arguments
    if not os.path.exists(path_python):
        warnings.warn(f'Invalid Python path. Using default path from config file instead ({PYTHON_PATH})', UserWarning)
    if not os.path.exists(path_module_entrypoint):
        warnings.warn(f'Invalid entrypoint path. Executable will not be linked to an existing Python file.', UserWarning)
        # raise ValueError('Invalid entrypoint path.')
    if not os.path.exists(dirpath_exec):
        raise ValueError('Invalid executable path: directory "{dirpath_exec}" does not exist.')

    # Check permissions for executable build path
    sudo = False
    if not os.access(dirpath_exec, os.W_OK):
        sudo = True
        if verbose: print(f'Permission required to create executable in {dirpath_exec}.')

    # Build executable file
    text = f'#!/bin/bash\n{path_python} {path_module_entrypoint} "\$@"'
    text_escaped = text.replace('"', r'\"')

    # Build command
    if sudo: command = f'printf "{text_escaped}" | sudo tee "{path_exec}" >/dev/null && sudo chmod +x "{path_exec}"'
    else:    command = f'printf "{text_escaped}" > "{path_exec}" && chmod +x "{path_exec}"'
    
    # Run command
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        raise ValueError('Executable creation failed.')
