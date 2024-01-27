import argparse
from builder import run


if __name__ == '__main__':

    # Build arguments parser
    parser = argparse.ArgumentParser(description='Python program executable builder')  # TODO: description
    parser.add_argument('-i', '--input', help="Path to the Python module's entrypoint", required=True, type=str)
    parser.add_argument('-o', '--output', help="Path to the executable file to create", required=True, type=str)
    parser.add_argument('-p', '--python', help="Path to the python kernel to use", type=str)
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


# /usr/local/bin/python3.9 /Users/anatole/Documents/GitHub/build-executable/main.py -i "/Users/anatole/Documents/GitHub/build-executable/main.py" -o "/Users/anatole/Downloads/exec1"  #! Build exec1
# /Users/anatole/Downloads/exec1 -i "/Users/anatole/Documents/GitHub/build-executable/main.py" -o "/Users/anatole/Downloads/exec2" -p "/usr/local/bin/python3.9"  #! Use exec1
# /Users/anatole/Downloads/exec1 -i "/Users/anatole/Documents/GitHub/build-executable/main.py" -o "/usr/local/bin/exec2" -p "/usr/local/bin/python3.9"  #! Test SUDO
