PyTrojan

**PyTrojan** is a Python-based tool used for injecting payloads into Python tools to allow remote access to compromised systems. This tool is primarily designed for penetration testing, enabling attackers to implant backdoors in Python files or generate new malicious Python files with reverse shell code for system access.

## Requirements

- Python 3.x
- Required libraries:
  - `socket`: for network communication.
  - `threading`: for handling parallel processes.
  - `base64`: for encoding the payload.

## Installation

To install and use **PyTrojan**, follow the steps below:

1. Clone the repository to your system:
   ```bash
   git clone https://github.com/PhantomByte313/PyTrojan.git
   cd PyTrojan

2. Run the tool with Python:

python3 pyTrojan.py



Usage

Available Commands:

After launching PyTrojan, you can use the following commands:

1. help
Displays a list of available commands with a brief description:

CEF> help


2. infect
Generates a malicious Python file with a reverse shell payload:

CEF> infect
Enter LHOST (your IP): <IP address>
Enter LPORT: <Port number>
Enter output filename (e.g., shell.py): <Output filename>


3. bind
Injects a reverse shell payload into an existing Python tool:

CEF> bind
Enter the path of the Python tool to infect: <Tool file path>
Enter LHOST (your IP): <IP address>
Enter LPORT: <Port number>
Enter output filename (e.g., infected_tool.py): <Output filename>


4. listen
Listens on a specific port for incoming connections from compromised systems:

CEF> listen
Enter port to listen on: <Port number>


5. exit
Exits the tool and terminates ongoing processes:

CEF> exit



How It Works:

1. Run the tool:
After cloning the repository, navigate to the PyTrojan directory and run the following command to start the tool:

python3 pyTrojan.py


2. Injecting Payloads:
Use the infect or bind commands to either create a new malicious Python file or inject a payload into an existing Python tool.


3. Listening for Connections:
Once the payload is executed on the target machine, use the listen command to wait for incoming connections from the compromised system.



License

This project is licensed under the MIT License.

### Key Features:

- **Help Command**: Provides a list of available commands to interact with the tool.
- **Infect Command**: Allows the user to generate a new Python file with a reverse shell.
- **Bind Command**: Injects a reverse shell payload into an existing Python tool.
- **Listen Command**: Listens for incoming reverse shell connections on a specific port.
- **Exit Command**: Terminates the tool.
