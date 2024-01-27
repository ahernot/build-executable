import argparse
from src.builder import run
from src.config import PYTHON_PATH


if __name__ == '__main__':

    # Build arguments parser
    parser = argparse.ArgumentParser(description='Python program executable builder')  # TODO: description
    parser.add_argument('-i', '--input', help="Path to the Python module's entrypoint", required=True, type=str)
    parser.add_argument('-o', '--output', help="Path to the executable file to create", required=True, type=str)
    parser.add_argument('-p', '--python', help="Path to the python kernel to use", type=str, default=PYTHON_PATH)
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Run
    run(
        path_module_entrypoint=args.input,
        path_exec=args.output,
        path_python=args.python,
        verbose=args.verbose
    )


# TODO: build its own executable in the ./ root directory on run (python build_executable) / or add it directly to /usr/local/bin (Unix)
