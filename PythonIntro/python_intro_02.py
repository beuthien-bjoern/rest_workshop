"""Second Python script to learn the basic concepts.

This is a simple python script to get in touch with basic concepts of the language.
The setting is originated in networking, to be more precise ip address checking.
Basic concepts:
* Importing and using packages
* Command line input
* Reading and writing to files
* Using default parameters from function

Run from console with "python python_intro_02.py filename.txt"
Check for style with "pylint python_intro_02.py"
"""
import socket
import sys
from datetime import datetime



def read_log(log_file_name: str):
    """Function reads the given file and prints it to console.

        Args:
                log_file_name: The file name of the log file we want to read

        Returns:
                nothing

        """
    with open(log_file_name, 'r', encoding='utf-8') as log_file:
        print(log_file.read())

def write_log(log_file_name: str):
    """Function writes date and current ip address to file with given name.

        Args:
                log_file_name: The file name of the log file we want to write to

        Returns:
                nothing

        """
    log_time = datetime.now()
    current_ip_address = socket.gethostbyname_ex(socket.gethostname())[-1]

    with open(log_file_name, 'a', encoding='utf-8') as log_file:
        log_file.writelines(f"File opened to write at {str(log_time)} from {current_ip_address}\n")

if __name__ == "__main__":
    try:
        # read first argument from the console
        cli_arg_log_file_name = sys.argv[1]
        write_log(cli_arg_log_file_name)
        read_log(cli_arg_log_file_name)
    except IndexError:
        print("Please provide a log file name as command line argument")
        print("Example: python python_intro_02.py <log_file_name>")
