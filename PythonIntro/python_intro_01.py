"""First Python script to see the basic concepts.

This is a simple python script to get in touch with basic concepts of the language.
The setting is originated in networking, to be more precise ip address checking.
Basic concepts:
* script structure and format
* variable declaration and usage
* if statements
* loop
* function definition
* main function
* type hints
* basic error handling

Run from console with "python python_intro_01.py"
Check for style with "pylint python_intro_01.py"
"""
# Define function for later use
def check_valid_ip_address(ip_address_to_check: str) -> bool:
    """Function checks if the given ip_address string is a valid ip address.

    Args:
            ip_address_to_check: A string containing a possible ip address

        Returns:
            True: if the string argument represents an ip address
            False: if the string argument doesn't represent an ip address

            example:
            "192.168.21.2" returns True
            "192.156.260.2" returns False
    """
    octets = ip_address_to_check.split(".")
    if len(octets) != 4:
        print("A valid ip address consists of four octets")
        return False
    for octet in octets:
        try:
            octet_number = int(octet)
            if octet_number < 0 or octet_number > 255:
                print("Each octet needs to be a number between 0 and 255")
                return False
        except ValueError as error:
            # Use of an f-string where a variable can be used inside a string
            print(f"Error: {error}\nEach octet needs to be a number")
            return False
    return True

# Run this part if the Python file is executed as a script using the command line.
# The special variable __name__ that contains a string whose value depends on how the code is
# being used.
# For more information on main functions see i.e. https://realpython.com/python-main-function/
if __name__ == "__main__":
    ip_address = input("Please give a valid ip address: ")
    if check_valid_ip_address(ip_address):
        print("This is a valid ip address")
