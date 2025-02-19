"""Third Python script to learn the basic concepts.

This is a simple python script to get in touch with basic concepts of the language.
The setting is originated in networking, to be more precise ip address checking.
Basic concepts:
* Data structures: Lists, Dictionaries
* Reading csv files

Run from console with "python python_intro_03.py"
Check for style with "pylint python_intro_03.py"
"""
import csv

def read_subnet_assignment(assignment_csv_file_name: str) -> dict[str, str]:
    """Function reads the given file and prints it to console.

        Args:
                log_file_name: The file name of the log file we want to read

        Returns:
                nothing

        """
    with open(assignment_csv_file_name, 'r', encoding='utf-8') as assignment_csv_file:
        # The reader object can handle different csv files. This is done by using special parameters:
        # - delimiter: character used to separate each field (default: ',').
        # - quotechar: character used to surround fields that contain the delimiter character (default: ' " ').
        # - escapechar: character to escape the delimiter character when quotes not used (default: no escape character).
        assignments_reader = csv.reader(assignment_csv_file, delimiter=',')
        line_count = 0
        # create an empty dict to store the assignments.
        assignments = {}
        for row in assignments_reader:
            # A row is a list of string values that were separated in the file by the delimiter
            if line_count == 0:
                print(f"Reading assignment file with columns {', '.join(row)}...")
            else:
                # The assignments are stored in the dict. The key is the department, the value is the subnet
                assignments[row[0]] = row[1]
            line_count += 1

        return assignments


def set_host_from_subnet(subnet_address: str, new_host_index: int) -> str:
    """Function Returns the host ip address at given index (starting at 0).

            Args:
                    subnet_address: The subnet address with prefix as a string, e.g. "192.168.12.0/24"
                    new_host_index: Index for the host address of the subnet given by subnet_address

            Returns:
                    host address with prefix in the given subnet and index

            Examples:
                    set_host_from_subnet("192.168.10.0/24", 3) --> "192.168.10.4/24"
                    set_host_from_subnet("192.168.10.128/24", 5) --> "192.168.10.134/24"

            """
    subnet_with_prefix = subnet_address.split('/')
    subnet_ip = subnet_with_prefix[0]
    subnet_prefix = subnet_with_prefix[1]
    subnet_octets = subnet_ip.split('.')
    index_last_octet = 3
    subnet_octets[index_last_octet] = str(int(subnet_octets[index_last_octet]) + new_host_index + 1)
    host_address = ".".join(subnet_octets) + "/" + subnet_prefix
    return host_address

if __name__ == "__main__":
    subnet_assignments = read_subnet_assignment("C:/Users/Philipp/Development/Fobi REST/rest_workshop/PythonIntro/files/department_to_subnet.csv")
    # Print assignments to console
    for key in subnet_assignments.keys():
        print(f"{key}: {subnet_assignments[key]}")

    servers = ["File Server", "Mail Server", "Web Server", "Database Server", "Application Server"]
    for key in subnet_assignments.keys():
        print(f"Servers for the department {key} with subnet {subnet_assignments[key]}")
        for server_index in range(0, len(servers)):
            subnet = subnet_assignments[key]
            server_ip = set_host_from_subnet(subnet, server_index)
            print(f"Assign IP {server_ip} to {servers[server_index]}")
